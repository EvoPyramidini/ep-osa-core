# Hierarchical Cognitive Memory Pyramid (HCMP)

> **Status:** Architectural Specification — v1.0
> **Origin:** Distilled from AlexCreator's architectural directive, 2026-05-19

---

## Core Principle

Memory в EP-OSA — это **не история сообщений**.
Это иерархическая, адресуемая, семантически управляемая когнитивная структура.

```text
memory exists ≠ memory is loaded
```

Каждый слой активируется **только при наличии контекстуальной релевантности задачи**.
Это называется: **contextual memory activation**.

---

## Topology: 5 Layers

### L0 — Active Cognitive Context

*Что нужно прямо сейчас. Минимальный entropy footprint.*

```json
{
  "current_task": "...",
  "active_constraints": [],
  "execution_state": "running",
  "immediate_dependencies": []
}
```

Содержит **только** то, что блокирует текущий шаг выполнения.
Не содержит рассуждений, вариантов, истории.

---

### L1 — Task Memory Cell

*Дистиллированная память конкретной задачи.*

**Что сохраняется:**

- validated findings
- architectural decisions
- execution summaries
- resolved blockers
- accepted mutations

**Что НЕ сохраняется:**

- raw chain-of-thought
- tool call logs
- transient reflections
- failed branches
- exploration artifacts

---

### L2 — Domain Layer

*Тематические кластеры знаний.*

Примеры доменов в EP-OSA:

- `governance` — Trinity protocol, constitutional rules
- `reflection` — validation patterns, coherence checks
- `tool_orchestration` — skill contracts, MCP mappings
- `memory` — HCMP topology itself
- `runtime` — Z-cascade, execution engine
- `mutation_engine` — field weights, quantum jumps

---

### L3 — System Architecture Layer

*Глобальные инварианты системы. Изменяются только через директиву AlexCreator.*

```text
- ontology (Z-level semantics, Sector definitions)
- protocols (Trinity, JSON Supreme, TaskEnvelope)
- schemas (contracts/, schemas/)
- orchestration contracts (SKILL.md, capability_discovery.json)
- governance laws (ARCHITECTURE_RULES.md, PYRAMID_ENVIRONMENT_RULES.md)
```

---

### L4 — Deep Archive (Cold Memory)

*Старые execution traces. Не загружаются автоматически.*

- Прошлые сессионные логи
- Отклонённые варианты мутаций
- Завершённые sprint-отчёты

Активируется только при явном retrieval-запросе к конкретной задаче.

---

## Retrieval Flow

```text
Task Intake
    ↓
Semantic Locator  (intent resolution → memory address)
    ↓
Memory Pyramid Navigation  (L0→L4, sparse traversal)
    ↓
Relevant Cell Retrieval  (only activated layers)
    ↓
Context Reconstruction  (minimal coherent state)
    ↓
Execution
    ↓
Distillation  (raw trace → architectural facts)
    ↓
Reintegration  (update L1/L2, archive trace to L4)
    ↓
Next Task
```

---

## Cognitive Distillation Rule

```text
100 000 строк execution trace
         ↓
    Trace Distiller
         ↓
3 validated architectural mutations
```

Лог рассуждений ≠ архитектурное состояние.

| Тип данных              | Судьба              |
|:------------------------|:--------------------|
| architectural decisions | → L1 / L3 (persist) |
| validated insights      | → L1 (persist)      |
| ontology mutations      | → L3 (persist)      |
| protocol changes        | → L3 (persist)      |
| raw chain-of-thought    | → L4 (archive)      |
| tool noise              | → DELETE            |
| temporary hypotheses    | → DELETE            |
| failed branches         | → DELETE            |
| exploration artifacts   | → L4 (cold archive) |

---

## Insight Intake Protocol

Когда поступает новая архитектурная идея **во время активного task execution**:

```text
Insight Intake
    ↓
Classification  (architectural / operational / ephemeral)
    ↓
Relevance Scoring  (к текущей задаче: HIGH / LOW / DEFERRED)
    ↓
Deferred Integration Queue  (если LOW/DEFERRED)
    ↓
Current Task Preservation  (execution graph не прерывается)
```

**Критическое правило:**
Новая идея не попадает в `L0 Active Context` —
она фиксируется в `L1 Task Cell` как `deferred_insight` и активируется при следующей релевантной задаче.

---

## Semantic Addressability

Каждая сущность в памяти имеет:

```yaml
memory_entity:
  id: "unique-semantic-id"
  hierarchy: "L1.task.governance.mutation_003"
  coordinates: [z: 15, domain: "governance", task: "trinity-schema"]
  semantic_tags: ["validated", "architectural", "z15"]
  dependency_graph: ["schema/core/task_envelope.json"]
  activation_conditions:
    - task_domain: "governance"
    - z_level_range: [14, 17]
```

---

## Quantum Jumps (Parallel Mutation Hypotheses)

"Квантовые скачки" — это параллельные мутационные гипотезы:

```text
Request
    ↓
Intent Resolution
    ↓
Variant Generation:
  ├─ Variant A: minimal surface mutation
  ├─ Variant B: runtime-level change
  ├─ Variant C: full topology update
  └─ Variant D: region-aware orchestration
    ↓
Survivability Score (coherence × cost × risk)
    ↓
Winner Integration
    ↓
Losers → L4 Archive (не удаляются, addressable для retrieval)
```

Каждый вариант **дистиллируется**, а не просто отбрасывается.
Проигравшие варианты сохраняются как `cold hypotheses` — могут быть извлечены при изменении контекста.

---

## Components Required

| Компонент                | Функция                                              | Статус        |
|:-------------------------|:-----------------------------------------------------|:--------------|
| `SemanticLocator`        | Переводит task intent в memory address               | `[ planned ]` |
| `ContextLoader`          | Собирает минимальный необходимый state из пирамиды   | `[ planned ]` |
| `TraceDistiller`         | Преобразует execution trace в architectural facts    | `[ planned ]` |
| `MemoryGarbageCollector` | Удаляет шум, архивирует, схлопывает дубликаты        | `[ planned ]` |
| `InsightIntakeQueue`     | Принимает deferred insights без прерывания execution | `[ planned ]` |
| `HypothesisArchive`      | Хранит проигравшие mutation variants для retrieval   | `[ planned ]` |

---

## Connection to Pyramid Architecture

HCMP физически отображается на Z-уровни Пирамиды:

| Memory Layer | Z-Level | Role in Pyramid                   |
|:-------------|:--------|:----------------------------------|
| L0 Active    | Z17     | Global Nexus — current execution  |
| L1 Task Cell | Z15–Z16 | Engineering Bay / Trinity Transit |
| L2 Domain    | Z11–Z14 | Alpha Canon Layer                 |
| L3 System    | Z7–Z10  | Beta Functional Layer             |
| L4 Archive   | Z1–Z6   | Gamma Deep Archive                |

Память не просто логическая — она **пространственно адресована** в 3D-структуре Пирамиды.

---

## Summary

> Пирамида памяти — это не storage system.
> Это **Persistent Reflective Cognitive OS** где память:
>
> - иерархическая,
> - адресуемая,
> - семантическая,
> - управляемая,
> - контекстно-активируемая.

**Ключевое отличие от обычных AI-систем:**
Не `всё всегда загружено` →
а `только релевантное, только тогда, когда нужно`.
