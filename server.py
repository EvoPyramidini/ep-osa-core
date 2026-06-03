"""
EP-OSA Core — HTTP Entry Point
Z15 → Z17 Gateway

This is the public face of the ep-osa-core orchestrator.
It receives requests from the external world (asdi-ep-os frontend,
Termux, or any LLM environment) and routes them through the
Z16 Trinity Router for memory-aware processing.

Flow:
    [Caller Z17/Z15] → server.py → z16_router.py → [Memory/Agents]
"""

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, Optional

from src.orchestration.z16_router import Z16TrinityRouter

# ─────────────────────────────────────────────────────────────────────────────
# App Bootstrap
# ─────────────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="EP-OSA Core Orchestrator",
    description="Z17 Global Nexus — Adaptive orchestration for EvoPyramid OS",
    version="1.0.0",
)

# Allow asdi-ep-os frontend (localhost:5173) to communicate with this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Z16 Trinity Router (Memory & Orchestration Layer)
router = Z16TrinityRouter()


# ─────────────────────────────────────────────────────────────────────────────
# Request / Response Schemas
# ─────────────────────────────────────────────────────────────────────────────
class OrchestratorRequest(BaseModel):
    """
    Universal contract for all requests to the Nexus.
    Every block must carry its Spatial Passport (z, x, y).
    """
    intent: str                          # What the caller wants to achieve
    source_z: int                        # Z-level of the caller (e.g., 17 = AlexCreator)
    target_z: Optional[int] = 16        # Z-level of the target (default: Z16 Trinity)
    payload: Dict[str, Any] = {}        # Arbitrary data (chat history, commands, etc.)
    session_id: Optional[str] = None    # Chat session ID for memory continuity
    language: Optional[str] = "RU"     # UK | EN | RU — language tag for Trinity routing


class OrchestratorResponse(BaseModel):
    status: str
    routed_to: str
    result: Any
    provenance: Optional[Dict[str, Any]] = None


# ─────────────────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────────────────
@app.get("/health", tags=["System"])
async def health_check():
    """Heartbeat endpoint. Used by asdi-ep-os to verify Nexus is alive."""
    return {"status": "alive", "environment": "ep-osa-core", "active_z": [17, 16, 15]}


@app.post("/orchestrate", response_model=OrchestratorResponse, tags=["Orchestration"])
async def orchestrate(request: OrchestratorRequest):
    """
    Main orchestration endpoint.
    Accepts an intent from Z17 (AlexCreator + AI) or Z15 (LLM Environments)
    and passes it through Z16 Trinity Router for processing and memory management.
    """
    result = await router.route(
        intent=request.intent,
        source_z=request.source_z,
        target_z=request.target_z,
        payload=request.payload,
        session_id=request.session_id,
        language=request.language,
    )
    return OrchestratorResponse(
        status="success",
        routed_to=f"Z{request.target_z} Trinity Router",
        result=result,
    )


@app.post("/snapshot", tags=["Memory"])
async def receive_snapshot(payload: Dict[str, Any]):
    """
    Accepts a Provenance Snapshot from any environment.
    Z16 stores it in memory and updates the pyramid state.
    """
    snapshot_id = await router.store_snapshot(payload)
    return {"status": "stored", "snapshot_id": snapshot_id}


@app.get("/snapshot/{session_id}", tags=["Memory"])
async def retrieve_snapshot(session_id: str):
    """Retrieves the latest Provenance Snapshot for a given session."""
    snapshot = await router.get_snapshot(session_id)
    if not snapshot:
        return JSONResponse(status_code=404, content={"error": "Snapshot not found"})
    return snapshot


@app.get("/pucks", tags=["Visualization"])
async def get_pucks():
    """
    Returns current puck state for asdi-ep-os frontend visualization.
    Maps active Z-level assignments to spatial coordinates.
    """
    return await router.get_puck_states()


# ─────────────────────────────────────────────────────────────────────────────
# Entry
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
