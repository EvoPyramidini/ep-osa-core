"""
EP-OSA Core — Z16 Gray Gateway
Layer: Z16 (Single Enforced Entry Point)

══════════════════════════════════════════════════════════════════════
ARCHITECTURAL RULE (IMMUTABLE):
    ALL interaction with Z16 (Trinity Memory Clusters, Router, Snapshots)
    MUST pass exclusively through this Gray Gateway.

    No external caller, no LLM environment (Z15), and no Nexus command
    (Z17) may directly address the Trinity clusters or z16_router.py.
    The Gray Gateway is the ONLY legal interface to Z16.
══════════════════════════════════════════════════════════════════════

Why "Gray" (Colorless)?
    The three Trinity clusters carry language identity:
        🟩 Green [UK]   🟨 Gold [EN]   🟥 Red [RU]
    The Gray Gateway is deliberately neutral — it belongs to no language,
    no agent, no project. It is pure infrastructure. It reads the raw
    incoming payload, detects the language tag, strips unnecessary
    metadata, validates the Spatial Passport (z/x/y), and only then
    hands the cleaned payload to z16_router.py.

    This mirrors the App.tsx terminal log description:
        "Gray extracts raw texts → passes to Green/Gold/Red →
         they digest in native languages → Gray unifies and responds."

Flow:
    [Z17 / Z15 caller]
         │
         ▼
    ┌──────────────────────────────┐
    │   Z16 GRAY GATEWAY           │  ← This file (sole entry)
    │   • Validates Passport       │
    │   • Detects language         │
    │   • Enforces Z16 contract    │
    │   • Strips forbidden fields  │
    └───────────────┬──────────────┘
                    │  (internal only)
                    ▼
    ┌──────────────────────────────┐
    │   z16_router.py              │  ← Internal, never called directly
    │   • Trinity clusters         │
    │   • Provenance generation    │
    │   • Snapshot management      │
    └──────────────────────────────┘
"""

import uuid
import re
from typing import Any, Dict, Optional
from datetime import datetime, timezone
from pydantic import BaseModel, Field, field_validator

from src.orchestration.z16_router import Z16TrinityRouter


# ─────────────────────────────────────────────────────────────────────────────
# Spatial Passport — Every block must carry one
# ─────────────────────────────────────────────────────────────────────────────
class SpatialPassport(BaseModel):
    """
    The geographic identity of any block interacting with Z16.
    Without a valid passport, the request is rejected at the gate.
    """
    z: int = Field(..., ge=1, le=17, description="Z-level of the caller (1-17)")
    x: int = Field(default=9, ge=0, le=18)
    y: int = Field(default=9, ge=0, le=18)
    block_id: str = Field(..., description="Unique block identifier, e.g. 'puck_z17_nexus'")

    @field_validator("z")
    @classmethod
    def z_must_not_be_16(cls, v: int) -> int:
        """Z16 cannot call itself. Prevents circular routing."""
        if v == 16:
            raise ValueError("Z16 cannot initiate requests to itself via the Gray Gateway.")
        return v


# ─────────────────────────────────────────────────────────────────────────────
# Gateway Request — The ONLY accepted input format for Z16
# ─────────────────────────────────────────────────────────────────────────────
class GatewayRequest(BaseModel):
    """
    The universal contract for all Z16 interactions.
    This is the ONLY data structure the Gray Gateway accepts.
    """
    passport: SpatialPassport
    intent: str = Field(..., min_length=1, max_length=2000)
    payload: Dict[str, Any] = Field(default_factory=dict)
    session_id: Optional[str] = Field(default=None)
    language: Optional[str] = Field(
        default=None,
        description="UK | EN | RU. If omitted, Gateway auto-detects from text content."
    )


class GatewayResponse(BaseModel):
    """Standardized response from the Gray Gateway."""
    accepted: bool
    gateway_ref: str           # Unique ID for this gateway transaction
    detected_language: str     # The language cluster that processed this request
    memory_id: Optional[str]   # ID in the Trinity cluster
    result: Dict[str, Any]
    timestamp: str


# ─────────────────────────────────────────────────────────────────────────────
# Gray Gateway
# ─────────────────────────────────────────────────────────────────────────────
class Z16GrayGateway:
    """
    The sole enforced entry point to Z16 Trinity Memory Layer.

    Responsibilities:
    1. Validate the Spatial Passport of every incoming request
    2. Auto-detect language if not explicitly provided
    3. Sanitize payload (remove forbidden/private fields)
    4. Delegate to Z16TrinityRouter (internal, opaque to callers)
    5. Return a unified GatewayResponse

    Enforcement:
    - server.py initializes ONLY the Gateway, never the Router directly
    - The Router is instantiated privately inside the Gateway
    - No external code may import Z16TrinityRouter and call it directly
    """

    # Language detection patterns
    _LANG_PATTERNS = {
        "UK": re.compile(
            r"[а-яёА-ЯЁіІїЇєЄґҐ].*[іІїЇєЄґҐ]|[іІїЇєЄґҐ]", re.UNICODE
        ),
        "RU": re.compile(r"[а-яёА-ЯЁ]{3,}", re.UNICODE),
        "EN": re.compile(r"[a-zA-Z]{3,}"),
    }

    # Fields that must never pass through the gateway into memory clusters
    _FORBIDDEN_FIELDS = {"password", "token", "secret", "api_key", "private_key"}

    def __init__(self):
        # The Router is private — only the Gateway holds a reference
        self._router = Z16TrinityRouter()
        print("[Z16 Gray Gateway] Initialized. Z16 is now sealed. All traffic must pass through me.")

    # ─────────────────────────────────────────────────────────────────────────
    # Public Interface (the ONLY callable method from outside Z16)
    # ─────────────────────────────────────────────────────────────────────────
    async def process(self, request: GatewayRequest) -> GatewayResponse:
        """
        The single public method. Validates, sanitizes, routes, and responds.
        This is all external callers should ever see of Z16.
        """
        gateway_ref = f"gw-{uuid.uuid4().hex[:8]}"
        timestamp = datetime.now(timezone.utc).isoformat()

        print(
            f"[Z16 Gray Gateway] {gateway_ref} | "
            f"Z{request.passport.z} [{request.passport.block_id}] → "
            f"intent='{request.intent[:60]}...'"
        )

        # Step 1: Sanitize payload
        clean_payload = self._sanitize(request.payload)

        # Step 2: Detect / confirm language
        language = self._detect_language(request.language, request.intent)

        # Step 3: Delegate to internal Router (opaque to caller)
        result = await self._router.route(
            intent=request.intent,
            source_z=request.passport.z,
            target_z=16,
            payload=clean_payload,
            session_id=request.session_id,
            language=language,
        )

        print(f"[Z16 Gray Gateway] {gateway_ref} | Processed → cluster={language} | mem_id={result.get('memory_id')}")

        return GatewayResponse(
            accepted=True,
            gateway_ref=gateway_ref,
            detected_language=language,
            memory_id=result.get("memory_id"),
            result=result,
            timestamp=timestamp,
        )

    # ─────────────────────────────────────────────────────────────────────────
    # Delegation Methods (thin wrappers, keep Router internal)
    # ─────────────────────────────────────────────────────────────────────────
    async def store_snapshot(self, payload: Dict[str, Any]) -> str:
        return await self._router.store_snapshot(payload)

    async def get_snapshot(self, session_id: str) -> Optional[Dict[str, Any]]:
        return await self._router.get_snapshot(session_id)

    async def get_puck_states(self):
        return await self._router.get_puck_states()

    def get_trinity_summary(self) -> Dict[str, Any]:
        return self._router.get_trinity_summary()

    # ─────────────────────────────────────────────────────────────────────────
    # Internal Utilities
    # ─────────────────────────────────────────────────────────────────────────
    def _sanitize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Remove any forbidden fields before data enters the memory clusters."""
        return {k: v for k, v in payload.items() if k.lower() not in self._FORBIDDEN_FIELDS}

    def _detect_language(self, provided: Optional[str], text: str) -> str:
        """
        If language is explicitly provided and valid, use it.
        Otherwise, auto-detect from the intent text content.
        Priority: UK > RU > EN (to preserve Ukrainian identity).
        """
        if provided and provided.upper() in ("UK", "EN", "RU"):
            return provided.upper()

        # Ukrainian takes priority (contains specific characters)
        if self._LANG_PATTERNS["UK"].search(text):
            return "UK"
        if self._LANG_PATTERNS["RU"].search(text):
            return "RU"
        return "EN"
