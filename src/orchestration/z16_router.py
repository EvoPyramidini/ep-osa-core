"""
Z16 — Trinity Memory Router
============================
Сердце маршрутизации EvoPyramid OS.

Принимает намерение (intent) с Z17,
определяет язык и контекст,
распределяет в нужный сектор памяти:

  🟩 Green  → UK (Украинский)
  🟨 Gold   → EN (Английский)
  🟥 Red    → RU (Русский)

Паттерн "проскока":
  Z17 (Намерение) → Z16 (Фильтр/Маршрут) → Z15 (Исполнение)
  ↑                                                    ↓
  └──────────── Z16 (Снимок памяти) ◄──────────────────┘
"""

import time
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class MemorySector(str, Enum):
    GREEN = "green"   # UK — Украинский
    GOLD  = "gold"    # EN — Английский
    RED   = "red"     # RU — Русский
    GRAY  = "gray"    # Неопределен — Router сам решает


@dataclass
class RoutedIntent:
    """Результат маршрутизации через Z16."""
    original_text: str
    detected_language: str
    sector: MemorySector
    z15_target: str              # Какой Z15-агент должен исполнить
    gravity_weight: float        # Магнитный вес (0.0 — 1.0)
    memory_snapshot: dict        # Слепок памяти для передачи на Z15
    timestamp: float = field(default_factory=time.time)


# ─── Language Detection ───────────────────────────────────────────────────────

# Простые unicode-ориентиры для детекции языка без внешних зависимостей
_UK_PATTERN = re.compile(r'[іїєґІЇЄҐ]')   # Уникальные украинские символы
_RU_PATTERN = re.compile(r'[ёъЁЪ]')        # Уникальные русские символы
_EN_PATTERN = re.compile(r'^[a-zA-Z\s\W\d]+$')  # Только латиница


def detect_language(text: str) -> tuple[str, MemorySector]:
    """
    Определяет язык текста и возвращает (lang_code, MemorySector).
    Без внешних библиотек — чистая локальная логика.
    """
    if _UK_PATTERN.search(text):
        return "uk", MemorySector.GREEN
    if _RU_PATTERN.search(text):
        return "ru", MemorySector.RED
    if _EN_PATTERN.match(text.strip()):
        return "en", MemorySector.GOLD
    # Кириллица без маркеров — по умолчанию RU
    if re.search(r'[а-яА-Я]', text):
        return "ru", MemorySector.RED
    return "en", MemorySector.GOLD


# ─── Gravity Weights ──────────────────────────────────────────────────────────

# Магнитные веса для Z15-агентов (Magnetic Orchestration Algorithm)
DEFAULT_GRAVITY: dict[str, float] = {
    "antigravity_engine":  1.0,   # Основной агент — всегда активен
    "gemini_advanced_hub": 0.8,   # Аналитика — высокий приоритет
    "github_pipeline":     0.5,   # Git-операции — средний приоритет
    "mcp_local_sensors":   0.4,   # MCP — по запросу
    "gcp_firebase":        0.2,   # Облако — минимальный приоритет (суверенитет!)
}


def select_z15_agent(intent: dict, gravity: dict[str, float]) -> str:
    """
    Выбирает Z15-агента с максимальным весом гравитации для данного намерения.
    """
    task_type = intent.get("task_type", "general")

    overrides = {
        "code":    "gemini_advanced_hub",
        "git":     "github_pipeline",
        "file":    "mcp_local_sensors",
        "memory":  "antigravity_engine",
        "general": "antigravity_engine",
    }

    preferred = overrides.get(task_type, "antigravity_engine")
    return max(gravity, key=lambda k: gravity[k] if k == preferred else gravity[k] * 0.5)


# ─── Z16 Trinity Router ───────────────────────────────────────────────────────

class Z16TrinityRouter:
    """
    Маршрутизатор Z16 — Ферзь Пирамиды.

    Принимает сырой intent от Z17,
    определяет язык, выбирает Z15-агента,
    формирует слепок памяти для передачи.
    """

    def __init__(self):
        self._memory: dict[MemorySector, list[dict]] = {
            MemorySector.GREEN: [],
            MemorySector.GOLD:  [],
            MemorySector.RED:   [],
            MemorySector.GRAY:  [],
        }
        self._gravity = DEFAULT_GRAVITY.copy()

    async def route(self, intent: dict) -> dict:
        """
        Главный метод маршрутизации.
        Принимает словарь intent, возвращает RoutedIntent как dict.
        """
        text = intent.get("text", "")
        lang, sector = detect_language(text)
        z15_agent = select_z15_agent(intent, self._gravity)

        # Сохраняем в сектор памяти
        memory_entry = {
            "text": text,
            "lang": lang,
            "timestamp": time.time(),
            "z15_target": z15_agent,
        }
        self._memory[sector].append(memory_entry)

        # Слепок последних 5 записей из нужного сектора
        snapshot = {
            "sector": sector.value,
            "recent": self._memory[sector][-5:],
        }

        routed = RoutedIntent(
            original_text=text,
            detected_language=lang,
            sector=sector,
            z15_target=z15_agent,
            gravity_weight=self._gravity.get(z15_agent, 0.5),
            memory_snapshot=snapshot,
        )

        return {
            "status": "routed",
            "layer": "Z16 — Trinity Router",
            "language": routed.detected_language,
            "sector": routed.sector.value,
            "z15_target": routed.z15_target,
            "gravity_weight": routed.gravity_weight,
            "memory_snapshot": routed.memory_snapshot,
            "timestamp": routed.timestamp,
        }

    def adjust_gravity(self, agent_id: str, weight: float):
        """Динамически обновить магнитный вес агента."""
        if agent_id in self._gravity:
            self._gravity[agent_id] = max(0.0, min(1.0, weight))

    def get_memory(self, sector: Optional[MemorySector] = None) -> dict:
        """Получить текущее состояние памяти."""
        if sector:
            return {sector.value: self._memory[sector]}
        return {k.value: v for k, v in self._memory.items()}
