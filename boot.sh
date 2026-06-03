#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
#  EP-OSA Core — Boot Script
#  Compatible: Termux (Android) + Windows (Git Bash / WSL) + Linux/macOS
#
#  Usage:
#    chmod +x boot.sh
#    ./boot.sh
#
#  This script activates the Python environment and launches the Z15→Z17
#  HTTP Gateway (server.py), making the Z16 Trinity Router available
#  to the asdi-ep-os frontend and any LLM environment.
# ═══════════════════════════════════════════════════════════════════════════════

set -e  # Exit immediately on error

# ─── Color Palette ──────────────────────────────────────────────────────────
GOLD='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
GRAY='\033[0;37m'
NC='\033[0m' # No Color

echo ""
echo -e "${GOLD}  EvoPyramid OS — EP-OSA Core${NC}"
echo -e "${GRAY}  Z17 Nexus → Z16 Trinity → Z15 Environments${NC}"
echo -e "${GRAY}  ─────────────────────────────────────────${NC}"
echo ""

# ─── Environment Detection ───────────────────────────────────────────────────
detect_env() {
  if [ -d "/data/data/com.termux" ]; then
    echo "termux"
  elif [ "$OS" = "Windows_NT" ]; then
    echo "windows"
  else
    echo "unix"
  fi
}

ENV_TYPE=$(detect_env)
echo -e "${GRAY}  Platform: ${GREEN}${ENV_TYPE}${NC}"

# ─── Python & Virtual Environment ────────────────────────────────────────────
VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
  echo -e "${GRAY}  Creating virtual environment...${NC}"
  python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
if [ "$ENV_TYPE" = "windows" ]; then
  source "$VENV_DIR/Scripts/activate"
else
  source "$VENV_DIR/bin/activate"
fi

echo -e "${GREEN}  ✓ Virtual environment activated${NC}"

# ─── Dependencies ────────────────────────────────────────────────────────────
echo -e "${GRAY}  Installing dependencies...${NC}"
pip install -q -r requirements.txt 2>/dev/null || {
  echo -e "${GRAY}  requirements.txt not found. Installing core dependencies...${NC}"
  pip install -q fastapi uvicorn pydantic
}
echo -e "${GREEN}  ✓ Dependencies ready${NC}"

# ─── Environment Variables ───────────────────────────────────────────────────
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
  echo -e "${GREEN}  ✓ Environment variables loaded from .env${NC}"
fi

# ─── Z16 Trinity Router Check ────────────────────────────────────────────────
if [ ! -f "src/orchestration/z16_router.py" ]; then
  echo -e "${RED}  ✗ Z16 Router not found. Aborting.${NC}"
  exit 1
fi
echo -e "${GREEN}  ✓ Z16 Trinity Router detected${NC}"

# ─── Launch ──────────────────────────────────────────────────────────────────
echo ""
echo -e "${GOLD}  Launching Z17 HTTP Gateway on http://0.0.0.0:8000${NC}"
echo -e "${GRAY}  Frontend bridge: http://localhost:5173 (asdi-ep-os)${NC}"
echo -e "${GRAY}  API Docs:        http://localhost:8000/docs${NC}"
echo -e "${GRAY}  Health Check:    http://localhost:8000/health${NC}"
echo ""

python3 server.py
