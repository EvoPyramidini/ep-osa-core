#!/data/data/com.termux/files/usr/bin/bash
# ============================================================
# EvoPyramid OS — Termux Boot Script
# Z17 Global Nexus — Pocket Orchestrator
# ============================================================
# Запуск:
#   chmod +x boot.sh
#   ./boot.sh
#
# Что делает:
#   1. Обновляет Canon из GitHub (git pull)
#   2. Активирует виртуальное окружение
#   3. Поднимает Z16 Trinity Router + HTTP сервер
#   4. Держит 10-секундный heartbeat в фоне
# ============================================================

set -e  # Остановить при любой ошибке

REPO_DIR="$HOME/ep-osa-core"
VENV_DIR="$REPO_DIR/.venv"
PORT=8000
LOG_FILE="$REPO_DIR/pyramid.log"

# ─── Цвета для терминала ──────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
GOLD='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo ""
echo -e "${CYAN}🔺 EvoPyramid OS — Boot Sequence${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# ─── Шаг 1: Проверить/клонировать репозиторий ─────────────
if [ ! -d "$REPO_DIR" ]; then
    echo -e "${GOLD}[Z17] Cloning Canon from GitHub...${NC}"
    git clone https://github.com/EvoPyramidini/ep-osa-core.git "$REPO_DIR"
else
    echo -e "${GOLD}[Z17] Syncing Canon from GitHub...${NC}"
    cd "$REPO_DIR"
    git pull origin main 2>&1 | tail -3
fi

cd "$REPO_DIR"

# ─── Шаг 2: Виртуальное окружение ─────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${GOLD}[Z15] Creating Python virtual environment...${NC}"
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

# ─── Шаг 3: Зависимости ───────────────────────────────────
echo -e "${GOLD}[Z15] Installing dependencies...${NC}"
pip install --quiet fastapi uvicorn[standard] 2>&1 | tail -2

# ─── Шаг 4: Предотвратить убийство процесса Android ───────
echo -e "${GOLD}[SYS] Acquiring wake lock...${NC}"
termux-wake-lock 2>/dev/null || echo "  (wake-lock skipped — no Termux:API)"

# ─── Шаг 5: Получить IP для фронтенда ─────────────────────
LOCAL_IP=$(ip route get 1 2>/dev/null | awk '{print $7; exit}' || hostname -I | awk '{print $1}')
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🔺 Z17 Global Nexus ONLINE${NC}"
echo -e "${GREEN}   React UI → http://${LOCAL_IP}:${PORT}${NC}"
echo -e "${GREEN}   WebSocket → ws://${LOCAL_IP}:${PORT}/ws${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# ─── Шаг 6: Запуск оркестратора ───────────────────────────
echo -e "${CYAN}[Z15] Starting Orchestrator on port ${PORT}...${NC}"
uvicorn server:app \
    --host 0.0.0.0 \
    --port "$PORT" \
    --log-level info \
    2>&1 | tee -a "$LOG_FILE"
