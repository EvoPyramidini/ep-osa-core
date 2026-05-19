# ep-osa-core

**Adaptive Orchestration & Governed Agent Execution Environment**

Evo-OSIII is an advanced orchestration core for cognitive AI agents with intelligent memory, quantum-inspired navigation, and constitutional governance.

## The 9-Layer Pyramid Architecture

```
        ╔═══════════════════════════════════╗
        ║     9. Research (Experimental)   ║ Emerging patterns & exploration
        ╠═══════════════════════════════════╣
        ║   8. Memory (EvoMemorySystem)    ║ Cognitive storage & anchors
        ╠═══════════════════════════════════╣
        ║  7. Tracing (Observability)      ║ Complete visibility
        ╠═══════════════════════════════════╣
        ║  6. Orchestration (Workflows)    ║ Skill composition & coordination
        ╠═══════════════════════════════════╣
        ║  5. Skills (Capabilities)        ║ Composable agent abilities
        ╠═══════════════════════════════════╣
        ║  4. Runtime (Execution)          ║ Safe execution contexts
        ╠═══════════════════════════════════╣
        ║  3. Schemas (Data Definition)    ║ Type & validation
        ╠═══════════════════════════════════╣
        ║  2. Contracts (Interfaces)       ║ Explicit guarantees
        ╠═══════════════════════════════════╣
        ║  1. Constitution (Governance)    ║ Immutable principles
        ╚═══════════════════════════════════╝
```

## What is ep-osa-core?

**ep-osa-core** unifies:
- **EvoAbsolut**: Quantum-inspired self-evolving core
- **HybridSession**: Intelligent memory + asynchronous execution
- **EvoMemorySystem**: Cognitive storage with semantic anchoring
- **QuantumBackpack**: Portable memory context with navigation
- **Constitution**: Governance principles that guide all evolution
- **PEAR Framework**: Purpose-Environment-Agent-Result interaction model

## How It Works

### 1. Constitution (Layer 1)
Immutable governance principles guide all operations.

### 2. Contracts (Layer 2)
Every interaction is explicit with defined input/output and guarantees.

### 3. Schemas (Layer 3)
All data validated against explicit schemas for type safety.

### 4. Runtime (Layer 4)
Secure, resource-bounded execution with failure isolation.

### 5. Skills (Layer 5)
Composable agent capabilities respecting contracts.

### 6. Orchestration (Layer 6)
Workflow coordination combining multiple skills.

### 7. Tracing (Layer 7)
Complete observability into system operation.

### 8. Memory (Layer 8)
Intelligent storage with:
- **50-60%** Primary operational memory
- **30%** Buffer layer for transitions  
- **10%** Reserve for critical operations
- Semantic anchors for navigation
- Self-evolving indices

### 9. Research (Layer 9)
Experimental exploration of quantum jumping, self-evolution, and emerging patterns.

## Quick Start

### Installation
```bash
git clone https://github.com/EvoPyramidini/ep-osa-core.git
cd ep-osa-core
pip install -r requirements.txt
```

### First Agent
```python
from ep_osa_core.runtime import Agent
from ep_osa_core.skills import BasicSkill

# Define a skill
skill = BasicSkill(
    name="greet",
    input_schema={"type": "object"},
    output_schema={"type": "string"}
)

# Create an agent
agent = Agent(name="greeting_bot")
agent.add_skill(skill)

# Execute
result = await agent.execute({"input": "World"})
print(result)
```

## Key Concepts

### EvoAbsolut (Quantum Core)
Self-evolving core with quantum-inspired jumping:
- Non-linear state transitions
- Energy conservation principles
- Self-reflection and adaptation
- External integration points

### HybridSession (Memory Bridge)
Intelligent session management:
- Dual-buffer architecture
- Asynchronous optimization zones
- Chaos management
- Session coherence

### Memory Anchors
Navigational landmarks in cognitive space:
- Semantic references
- Historical markers
- Connection points
- Evolution seeds

### PEAR Framework
Interaction model:
- **P**urpose: What we aim to achieve
- **E**nvironment: Context and constraints
- **A**gent: Actor with capabilities
- **R**esult: Outcome evaluation

## Architecture Rules

See `docs/ARCHITECTURE_RULES.md` for comprehensive governance:
- Constitutional foundation
- Contract-based interaction
- Schema-driven design
- Memory proportions
- Semantic preservation
- Quantum jump principles
- Soul coherence
- Async-first execution
- Observability requirements
- Evolution and failure handling

## Recent Architecture Additions (2026-05-19)

### Новые документы этой сессии

| Документ | Расположение | Описание |
|----------|-------------|----------|
| **PYRAMID_ENVIRONMENT_RULES.md** | `docs/` | Физические законы среды Пирамиды + **Rule 6: Server Environment Anchor** (`us-west / America`) |
| **MAGNETIC_ORCHESTRATION_MANIFEST.md** | `docs/` | Weightless Control Protocol — Field-Driven Cognition, Puck/Field/Entropy primitives |
| **COGNITIVE_MEMORY_PYRAMID.md** | `docs/` | Hierarchical Cognitive Memory — 5 слоёв (L0–L4), retrieval flow, Insight Intake Protocol, Quantum Jumps |

### Изменения в `asdi-ep-os` (UI Layer)

- **App.tsx** — статус-баннер обновлён: `US-WEST ENVIRONMENT ACTIVE`
- **App.tsx** — Swarm Terminal: добавлены лог-записи о миграции региона с меткой времени
- Регион `us-west (America)` теперь — **каноническая среда выполнения** всех Z15-сервисов

### Test Run Results (Quantum Jumps)

```
EvoPyramid OS / tests/  →  61 passed, 0 failed, 10 warnings  (2.67s)
```

Предупреждения: Pydantic enum serializer — не блокируют работу, требуют `use_enum_values=True` при следующей итерации.


## Terminology

See `docs/TERMINOLOGY.md` for complete glossary:
- Core concepts (EvoAbsolut, HybridSession, etc.)
- Memory systems (EvoMemorySystem, QuantumBackpack)
- Quantum mechanics (Quantum Jumps, Coherence)
- Governance (Constitution, Contracts, Schemas)
- And much more...

## Extending ep-osa-core

### Add a New Skill

1. Define contract in `contracts/`
2. Define schemas in `schemas/`
3. Implement in `skills/`
4. Add tests in `tests/`

### Add a New Layer

1. Create directory under root
2. Add `README.md` with layer description
3. Follow pyramid hierarchy
4. Update constitution if needed

### Experimental Features

Use `research/` for exploration:
- New memory models
- Advanced orchestration
- Novel quantum patterns
- Integration experiments

## Project Structure

```
ep-osa-core/
├── docs/               # Architecture rules, terminology, and governance
├── contracts/          # Schemas and API contracts
├── src/                # Runtime, orchestration, agents, memory
├── skills/             # Agent capabilities
├── research/           # Experimental components and brainstorms
├── tests/              # Test suites
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Testing

```bash
# Run all tests
pytest

# Run specific layer tests
pytest tests/memory/
pytest tests/orchestration/

# With coverage
pytest --cov=ep_osa_core
```

## Contributing

1. Read `ARCHITECTURE_RULES.md`
2. Understand the layer you're working on
3. Add/update contracts and schemas
4. Implement following constitution
5. Add comprehensive tests
6. Update documentation
7. Submit pull request

## Resources

- **Architecture Rules**: See `docs/ARCHITECTURE_RULES.md`
- **Terminology**: See `docs/TERMINOLOGY.md`  
- **Constitution**: See `docs/constitution/ep-osa-core-constitution.md`
- **Layer Details**: See `{layer}/README.md`

## License

MIT License - See LICENSE file

## Contact

Project: [EvoPyramidini](https://github.com/EvoPyramidini)  
Repository: [ep-osa-core](https://github.com/EvoPyramidini/ep-osa-core)

---

**Version:** 1.0-alpha  
**Last Updated:** 2026-05-14  
**Status:** Foundation Phase