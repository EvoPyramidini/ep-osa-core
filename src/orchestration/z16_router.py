"""
EP-OSA Core — Z16 Trinity Memory Router
Layer: Z16 (Memory Formation, Filtering, Backup & Pyramid Observation)

Architecture:
    Z17 (AlexCreator + AI) — generates INTENT
    Z15 (LLM Environments) — executes ACTIONS
    Z16 (THIS MODULE)      — observes BOTH, filters memory, forms Snapshots,
                             routes data, and guards the Pyramid's evolution.

The "Skip" Pattern (Проскок):
    Z17 and Z15 work together directly for speed.
    Z16 watches silently, captures the dialogue, distills it into
    provenance-tagged memory, and archives it. It is the Subconscious.

Trinity Memory Clusters (Language-Bound):
    🟩 Green [UK] — Ukrainian-tagged knowledge (AlexCreator's concepts)
    🟨 Gold  [EN] — English-tagged logic (Watchman's structure)
    🟥 Red   [RU] — Russian-tagged integration (Лётчик-Испытатель's context)
"""

import uuid
import json
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone


class MemoryCluster:
    """A language-tagged memory container. One of three in the Trinity."""

    def __init__(self, language: str, color: str):
        self.language = language    # UK | EN | RU
        self.color = color          # Visual identity on the board
        self._store: List[Dict[str, Any]] = []

    def ingest(self, data: Dict[str, Any]) -> str:
        """Accept a memory fragment into this cluster."""
        entry = {
            "id": f"mem-{uuid.uuid4().hex[:8]}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "language": self.language,
            "data": data,
        }
        self._store.append(entry)
        return entry["id"]

    def retrieve_all(self) -> List[Dict[str, Any]]:
        return self._store.copy()

    def retrieve_latest(self, n: int = 5) -> List[Dict[str, Any]]:
        return self._store[-n:]


class Z16TrinityRouter:
    """
    The Trinity Memory Router — Z16 Observer & Processor.

    Responsibilities:
    - Route intents from Z17 down to Z15 environments
    - Observe session chat history and extract Provenance
    - Feed memory into language-tagged Trinity clusters (Green/Gold/Red)
    - Provide Snapshots to the server for storage and retrieval
    - Report puck state to asdi-ep-os for 3D visualization
    """

    def __init__(self):
        # Three language-tagged memory containers
        self.green = MemoryCluster(language="UK", color="#10b981")   # Ukrainian
        self.gold  = MemoryCluster(language="EN", color="#eab308")   # English
        self.red   = MemoryCluster(language="RU", color="#ef4444")   # Russian

        # Session snapshot store: session_id → latest snapshot
        self._snapshots: Dict[str, Dict[str, Any]] = {}

        # Puck registry (mirrors asdi-ep-os board state)
        self._pucks = [
            {"id": "puck_z17_nexus",      "z": 17, "x": 9, "y": 9, "color": "#eab308", "role": "AlexCreator & AI Nexus"},
            {"id": "puck_z16_trinity",    "z": 16, "x": 9, "y": 9, "color": "#10b981", "role": "Trinity Memory Router"},
            {"id": "puck_z15_environments","z": 15, "x": 9, "y": 9, "color": "#94a3b8", "role": "Colorless Environments"},
        ]

        print("[Z16] Trinity Router initialized. Clusters: 🟩UK 🟨EN 🟥RU")

    # ─────────────────────────────────────────────────────────────────────────
    # Core Routing
    # ─────────────────────────────────────────────────────────────────────────
    async def route(
        self,
        intent: str,
        source_z: int,
        target_z: int,
        payload: Dict[str, Any],
        session_id: Optional[str],
        language: str = "RU",
    ) -> Dict[str, Any]:
        """
        Main routing logic. Routes intent and archives it into
        the appropriate memory cluster based on language tag.
        """
        print(f"[Z16] Routing: Z{source_z} → Z{target_z} | intent='{intent}' | lang={language}")

        # Archive into correct Trinity cluster
        memory_fragment = {"intent": intent, "payload": payload, "session_id": session_id}
        mem_id = self._ingest_by_language(language, memory_fragment)

        # Auto-generate a lightweight provenance entry
        provenance = self._generate_provenance(intent, source_z, language, mem_id)

        # Store in session snapshot
        if session_id:
            self._update_snapshot(session_id, intent, provenance, payload)

        return {
            "routed": True,
            "memory_id": mem_id,
            "cluster": language,
            "provenance": provenance,
        }

    def _ingest_by_language(self, language: str, data: Dict[str, Any]) -> str:
        """Route memory to correct Trinity cluster by language tag."""
        lang = language.upper()
        if lang == "UK":
            return self.green.ingest(data)
        elif lang == "EN":
            return self.gold.ingest(data)
        else:  # Default: RU
            return self.red.ingest(data)

    # ─────────────────────────────────────────────────────────────────────────
    # Provenance Generation (Auto, Session-Based)
    # ─────────────────────────────────────────────────────────────────────────
    def _generate_provenance(
        self, intent: str, source_z: int, language: str, mem_id: str
    ) -> Dict[str, Any]:
        """
        Auto-generate a minimal Provenance record from session context.
        This is the Z16 solution to the "bureaucracy overhead" problem:
        provenance is generated automatically by the router, not manually by LLM.
        """
        return {
            "knowledge": {
                "id": f"know-{uuid.uuid4().hex[:6]}",
                "statement": intent,
                "primary_category": "External" if source_z == 17 else "Inferred",
                "evidence": [f"session_memory:{mem_id}", f"z{source_z}_input"],
                "confidence": "High",
                "language": language,
            },
            "decision": {
                "id": f"dec-{uuid.uuid4().hex[:6]}",
                "decision": f"Route intent from Z{source_z} through Z16 Trinity",
                "primary_category": "Mandated by Contract",
                "rationale": "Z16 is the mandatory memory observer for all Z17↔Z15 traffic.",
                "evidence": ["contracts/KNOWLEDGE_PROVENANCE.md", "contracts/DECISION_PROVENANCE.md"],
                "confidence": "High",
            },
        }

    # ─────────────────────────────────────────────────────────────────────────
    # Snapshot Management
    # ─────────────────────────────────────────────────────────────────────────
    async def store_snapshot(self, payload: Dict[str, Any]) -> str:
        """Store an external provenance snapshot."""
        snapshot_id = payload.get("session_id") or f"snap-{uuid.uuid4().hex[:8]}"
        payload["_stored_at"] = datetime.now(timezone.utc).isoformat()
        self._snapshots[snapshot_id] = payload
        print(f"[Z16] Snapshot stored: {snapshot_id}")
        return snapshot_id

    async def get_snapshot(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a stored snapshot by session ID."""
        return self._snapshots.get(session_id)

    def _update_snapshot(
        self, session_id: str, intent: str, provenance: Dict[str, Any], payload: Dict[str, Any]
    ):
        """Update the rolling session snapshot with new provenance data."""
        if session_id not in self._snapshots:
            self._snapshots[session_id] = {
                "session_id": session_id,
                "knowledge_provenance": [],
                "decision_provenance": [],
                "outcome_provenance": [],
            }
        snap = self._snapshots[session_id]
        snap["knowledge_provenance"].append(provenance["knowledge"])
        snap["decision_provenance"].append(provenance["decision"])
        snap["_updated_at"] = datetime.now(timezone.utc).isoformat()

    # ─────────────────────────────────────────────────────────────────────────
    # Puck State (Visualization Bridge)
    # ─────────────────────────────────────────────────────────────────────────
    async def get_puck_states(self) -> List[Dict[str, Any]]:
        """Return current puck positions for asdi-ep-os board visualization."""
        return self._pucks

    def update_puck(self, puck_id: str, x: int, y: int, z: int):
        """Update a puck's spatial position (called by external commands)."""
        for puck in self._pucks:
            if puck["id"] == puck_id:
                puck.update({"x": x, "y": y, "z": z})
                print(f"[Z16] Puck '{puck_id}' moved to [{x},{y},{z}]")
                return
        print(f"[Z16] Warning: puck '{puck_id}' not found in registry.")

    # ─────────────────────────────────────────────────────────────────────────
    # Memory Inspection
    # ─────────────────────────────────────────────────────────────────────────
    def get_trinity_summary(self) -> Dict[str, Any]:
        """Returns a summary of all three memory cluster sizes."""
        return {
            "🟩 Green [UK]": len(self.green.retrieve_all()),
            "🟨 Gold  [EN]": len(self.gold.retrieve_all()),
            "🟥 Red   [RU]": len(self.red.retrieve_all()),
        }
