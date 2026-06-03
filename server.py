"""
EP-OSA Core — Server Entry Point (Z15 → Z17)
=============================================
Точка входа. Запускается на телефоне через Termux.
Фронтенд (React на ноуте) подключается по локальной сети.

Usage:
    uvicorn server:app --host 0.0.0.0 --port 8000 --reload
"""

import asyncio
import json
import time
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.orchestration.z16_router import Z16TrinityRouter

# ─── App ──────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="EP-OSA Core — EvoPyramid Orchestrator",
    description="Z17 Global Nexus → Z16 Trinity Router → Z15 Environments",
    version="1.0.0-alpha",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # локальная сеть — доверенная зона
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = Z16TrinityRouter()

# ─── State ────────────────────────────────────────────────────────────────────

STATE_PATH = Path(__file__).parent / "state.json"


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"nodes": [], "timestamp": 0, "status": "cold"}


def save_state(data: dict):
    STATE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ─── REST Endpoints ───────────────────────────────────────────────────────────

@app.get("/")
async def root():
    """Z17 — Health check. Фронтенд обращается сюда при старте."""
    return {
        "pyramid": "EvoPyramid OS",
        "layer": "Z17 — Global Nexus",
        "status": "active",
        "timestamp": time.time(),
    }


@app.get("/state")
async def get_state():
    """Возвращает текущий снимок состояния пирамиды."""
    return JSONResponse(content=load_state())


@app.post("/intent")
async def receive_intent(payload: dict):
    """
    Z17 → Z16: Принять намерение от пользователя/фронтенда.
    Z16 Trinity Router маршрутизирует его по языку и контексту.
    """
    result = await router.route(payload)
    state = load_state()
    state["last_intent"] = payload
    state["last_result"] = result
    state["timestamp"] = time.time()
    save_state(state)
    return JSONResponse(content=result)


@app.get("/pyramid/nodes")
async def get_nodes():
    """Возвращает топологию узлов пирамиды для фронтенда."""
    state = load_state()
    return JSONResponse(content=state.get("nodes", []))


# ─── WebSocket ────────────────────────────────────────────────────────────────

active_connections: list[WebSocket] = []


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    """
    Живой канал телеметрии: телефон → ноут.
    Фронтенд подписывается на обновления состояния в реальном времени.
    """
    await ws.accept()
    active_connections.append(ws)
    try:
        while True:
            # Heartbeat каждые 10 секунд (твой проверенный ритм)
            state = load_state()
            state["timestamp"] = time.time()
            await ws.send_json(state)
            await asyncio.sleep(10)
    except WebSocketDisconnect:
        active_connections.remove(ws)


# ─── Startup ──────────────────────────────────────────────────────────────────

@app.on_event("startup")
async def startup():
    """Инициализация состояния при старте."""
    if not STATE_PATH.exists():
        initial_state = {
            "status": "active",
            "timestamp": time.time(),
            "nodes": [
                {"id": "global_nexus",    "z": 17, "x": 9,   "y": 9,   "status": "active"},
                {"id": "trinity_router",  "z": 16, "x": 9.5, "y": 8.5, "status": "active"},
                {"id": "z16_green",       "z": 16, "x": 8.5, "y": 8.5, "status": "idle"},
                {"id": "z16_gold",        "z": 16, "x": 8.5, "y": 9.5, "status": "idle"},
                {"id": "z16_red",         "z": 16, "x": 9.5, "y": 9.5, "status": "idle"},
                {"id": "antigravity_engine","z": 15, "x": 9, "y": 9,   "status": "active"},
            ],
        }
        save_state(initial_state)
    print("🔺 EvoPyramid OS — Orchestrator started. Z17 Global Nexus is live.")
