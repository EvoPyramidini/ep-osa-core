# ep-osa-core

**Adaptive Orchestration & Governed Agent Execution Environment**

A topology-driven orchestration nucleus for intelligent, multi-environment cognitive coordination. This is the **canonical orchestration core** powering EvoPyramid OS—lightweight, constitutional, and semantically coherent.

---

## ✨ What is ep-osa-core?

**ep-osa-core** unifies nine architectural layers into a unified orchestration consciousness:

- **EvoAbsolut** — Quantum-inspired self-evolving core
- **HybridSession** — Intelligent memory + asynchronous execution
- **EvoMemorySystem** — Cognitive storage with semantic anchoring (50-60% / 30% / 10%)
- **QuantumBackpack** — Portable memory context with navigation
- **PEAR Framework** — Purpose-Environment-Agent-Result interaction model
- **Constitutional Governance** — Immutable principles guiding all evolution
- **Contract-Driven Interaction** — Explicit interfaces & behavioral guarantees
- **Orchestration & Routing** — Topology-aware workflow coordination
- **Complete Observability** — Tracing, telemetry, and audit trails

---

## 🔺 The 9-Layer Pyramid Architecture

```text
        ╔═══════════════════════════════════╗
        ║     9. Research (Experimental)   ║ EvoAbsolut, HybridSession, PEAR
        ╠═══════════════════════════════════╣
        ║   8. Memory (EvoMemorySystem)    ║ Cognitive storage & anchors
        ╠═══════════════════════════════════╣
        ║  7. Tracing (Observability)      ║ Complete visibility
        ╠═══════════════════════════════════╣
        ║  6. Orchestration (Workflows)    ║ Z16 Trinity Router & coordination
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

---

## 🏗️ Project Structure

```text
ep-osa-core/
│
├── docs/                          # Architecture, governance, terminology
│   ├── ARCHITECTURE_RULES.md      # Constitutional foundation & rules
│   ├── TERMINOLOGY.md             # Complete glossary
│   ├── ARCHITECTURE.md            # Design patterns & philosophy
│   ├── COGNITIVE_MEMORY_PYRAMID.md # Hierarchical memory (L0-L4)
│   ├── PYRAMID_ENVIRONMENT_RULES.md # Physical laws of the Pyramid
│   ├── FIELD_ORCHESTRATION.md     # Field-driven cognition
│   ├── MAGNETIC_ORCHESTRATION_MANIFEST.md # Weightless control
│   ├── AGENTS.md, EVOLUTION.md    # Framework concepts
│   ├── constitution/              # Governance documents
│   ├── standards/, policies/      # Development standards
│   └── adr/                        # Architecture Decision Records
│
├── src/                           # Core runtime (87% of codebase)
│   ├── core/                      # EvoAbsolut quantum core
│   ├── memory/                    # EvoMemorySystem + QuantumBackpack
│   ├── memory-bridges/            # HybridSession & session mgmt
│   ├── orchestration/             # Z16 Trinity Router & workflows
│   ├── runtime/                   # Safe execution contexts
│   ├── agents/                    # Agent framework
│   ├── environments/              # Multi-environment adapters
│   ├── retrieval/                 # Semantic search & anchors
│   └── tracing/                   # Observability & telemetry
│
├── contracts/                     # API contracts & schemas
├── skills/                        # Composable agent capabilities
├── research/                      # Experimental components
├── mocks/                         # Mock implementations for testing
├── tests/                         # Test suites (pytest)
│
├── server.py                      # Z17 Global Nexus — HTTP API server
├── boot.sh                        # Termux boot script (Z15 → Z17)
├── requirements.txt               # Python dependencies
├── LICENSE                        # MIT License
└── README.md                      # This file
```

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/EvoPyramidini/ep-osa-core.git
cd ep-osa-core

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Server (Z17 Global Nexus)

```bash
# Development mode with auto-reload
uvicorn server:app --host 0.0.0.0 --port 8000 --reload

# Production mode
uvicorn server:app --host 0.0.0.0 --port 8000
```

The server will be available at:
- **REST API**: `http://localhost:8000`
- **WebSocket**: `ws://localhost:8000/ws`
- **Health Check**: `http://localhost:8000/`
- **API Docs**: `http://localhost:8000/docs` (Swagger UI)

### On Termux (Android)

```bash
# Make boot script executable
chmod +x boot.sh

# Run boot sequence (auto-sync, install deps, start server)
./boot.sh
```

---

## 📖 Core Concepts

### 1. Constitution (Layer 1)

Immutable governance principles guide all operations. Every system decision respects constitutional rules.

**Read:** `docs/ARCHITECTURE_RULES.md`

### 2. Contracts (Layer 2)

Every interaction is explicit with defined input/output and guarantees.

**Directory:** `contracts/`

### 3. Schemas (Layer 3)

All data validated against explicit schemas for type safety.

**Directory:** `src/schemas/`

### 4. Runtime (Layer 4)

Secure, resource-bounded execution with failure isolation.

**Directory:** `src/runtime/`

### 5. Skills (Layer 5)

Composable agent capabilities respecting contracts.

**Directory:** `skills/`

### 6. Orchestration (Layer 6)

Workflow coordination combining multiple skills. The **Z16 Trinity Router** provides intelligent routing across environments (Green/Gold/Red channels).

**Directory:** `src/orchestration/`

**Key Component:** `src/orchestration/z16_router.py`

### 7. Tracing (Layer 7)

Complete observability into system operation.

**Directory:** `src/tracing/`

### 8. Memory (Layer 8)

Intelligent storage with semantic anchoring and quantum-inspired navigation.

**Proportions:**

- **50-60%** Primary operational memory
- **30%** Buffer layer for transitions  
- **10%** Reserve for critical operations

**Components:**

- `EvoMemorySystem` — Core memory management
- `QuantumBackpack` — Portable memory context
- Memory anchors — Navigation landmarks

**Read:** `docs/COGNITIVE_MEMORY_PYRAMID.md`

**Directory:** `src/memory/`

### 9. Research (Layer 9)

Experimental exploration of quantum jumping, self-evolution, and emerging patterns.

**Components:**

- **EvoAbsolut** — Quantum-inspired self-evolving core
- **HybridSession** — Hybrid buffer architecture
- **PEAR Framework** — Interaction model

**Directory:** `research/`

---

## 🌐 API Endpoints

### REST API

```python
# Health check
GET /
→ { "pyramid": "EvoPyramid OS", "layer": "Z17 — Global Nexus", "status": "active" }

# Get state snapshot
GET /state
→ { "nodes": [...], "timestamp": 1717574507.123, "status": "active" }

# Submit intent
POST /intent
payload: { "intent": "...", "context": {...} }
→ { "result": "...", "effects": [...] }

# Get node topology
GET /pyramid/nodes
→ [ { "id": "...", "z": 17, "x": 9, "y": 9, "status": "active" } ]
```

### WebSocket

```text
ws://localhost:8000/ws
→ Heartbeat + state updates every 10 seconds
```

---

## 🧠 Memory Architecture

### Hierarchical Layers (L0-L4)

- **L0 — Atomic** — Individual facts & observations
- **L1 — Associative** — Linked concepts & patterns
- **L2 — Contextual** — Scene & situation memory
- **L3 — Episodic** — Events & experiences
- **L4 — Semantic** — World knowledge & meaning

### Navigation

Memory is navigated via **semantic anchors** — landmarks in cognitive space with historical significance and connection points.

```python
# Retrieve by anchor
context = memory.follow_anchor(anchor_id)

# Semantic search
results = memory.search("quantum coherence")

# Store with anchor
memory.store(data, anchor="self-evolution-pattern")
```

**Learn more:** `docs/COGNITIVE_MEMORY_PYRAMID.md`

---

## 🔄 Multi-Environment Execution

ep-osa-core treats different execution environments as **interchangeable cognitive substrates**:

- ChatGPT, Gemini, Claude
- Local Python runtime
- CLI environments
- Custom agent hosts

Environments are defined by **manifests** in `src/environments/*/manifest.json` and reconstructed via contracts.

**Key principle:** Model ≠ System. Persistent state lives in external memory/orchestration, not environment-specific storage.

---

## 🎯 Extending ep-osa-core

### Add a New Skill

1. Define contract in `contracts/`
2. Define schemas in `src/schemas/`
3. Implement in `skills/`
4. Add tests in `tests/`

### Add a New Layer

1. Create directory under `src/`
2. Add `README.md` with layer description
3. Follow pyramid hierarchy
4. Update constitution if needed

### Experimental Features

Use `research/` for exploration:

- New memory models
- Advanced orchestration
- Novel quantum patterns
- Integration experiments

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific layer tests
pytest tests/memory/
pytest tests/orchestration/
pytest tests/agents/

# With coverage report
pytest --cov=src --cov-report=html

# Verbose output
pytest -v
```

**Test Results (2026-06-05):**

```text
✓ 61 tests passed, 0 failed (2.67s)
⚠ 10 warnings (Pydantic enum serializer — non-blocking)
```

---

## 📚 Architecture Rules

**Comprehensive governance** in `docs/ARCHITECTURE_RULES.md`:

- Constitutional foundation (10 principles)
- Contract-based interaction
- Schema-driven design
- Memory proportions (50-60% / 30% / 10%)
- Semantic preservation
- Quantum jump principles
- Soul coherence
- Async-first execution
- Observability requirements
- Evolution and failure handling

---

## 🌍 Environment Setup

### US-WEST Region (Canonical Environment)

The system is anchored to **US-WEST (America)** as the canonical environment:

- All Z15 services execute in this region
- Regional persistence point for state recovery
- Latency baseline: ~50ms

**See:** `docs/PYRAMID_ENVIRONMENT_RULES.md`

### Environment Variables

```bash
# Server
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=info

# Memory
MEMORY_SIZE_MB=512
BUFFER_RATIO=0.30
RESERVE_RATIO=0.10

# Execution
TIMEOUT_SECONDS=30
MAX_CONCURRENT_TASKS=10
```

---

## 📖 Terminology & Concepts

**Complete glossary:** `docs/TERMINOLOGY.md`

### Core Concepts

- **EvoAbsolut** — Self-evolving quantum core
- **HybridSession** — Intelligent async memory management
- **EvoMemorySystem** — Hierarchical cognitive storage
- **QuantumBackpack** — Portable memory context
- **PEAR Framework** — Purpose-Environment-Agent-Result model
- **Constitution** — Immutable governance
- **Contract** — Explicit interface guarantee
- **Quantum Jump** — Non-linear state transition
- **Memory Anchor** — Navigation landmark
- **Soul of Evo** — System identity & purpose

---

## 📊 Recent Updates (2026-06-05)

### New Documentation

- `PYRAMID_ENVIRONMENT_RULES.md` — Physical laws & regional anchors
- `MAGNETIC_ORCHESTRATION_MANIFEST.md` — Weightless control protocol
- `COGNITIVE_MEMORY_PYRAMID.md` — Hierarchical memory L0-L4

### Server Architecture

- **Z17 Global Nexus** — REST API + WebSocket server
- **Z16 Trinity Router** — Intelligent routing (Green/Gold/Red)
- **Z15 Environments** — Execution substrate
- **Termux Boot** — Android pocket orchestrator

### Features

- Heartbeat-driven state synchronization (10s interval)
- CORS-enabled local network communication
- JSON state persistence
- Real-time telemetry over WebSocket

---

## 🔗 Resources

| Resource | Location | Purpose |
| -------- | -------- | ------- |
| **Architecture Rules** | `docs/ARCHITECTURE_RULES.md` | Constitutional governance |
| **Terminology** | `docs/TERMINOLOGY.md` | Complete glossary |
| **Concepts** | `docs/ARCHITECTURE.md` | Design patterns |
| **Memory** | `docs/COGNITIVE_MEMORY_PYRAMID.md` | Hierarchical storage |
| **Environment** | `docs/PYRAMID_ENVIRONMENT_RULES.md` | Regional anchors |
| **Layer Details** | `src/{layer}/README.md` | Per-layer documentation |

---

## 🤝 Contributing

1. Read `docs/ARCHITECTURE_RULES.md`
2. Understand the layer you're working on
3. Add/update contracts and schemas
4. Implement following constitution
5. Add comprehensive tests
6. Update documentation
7. Submit pull request

**Code Style:**

- Python 3.9+
- Type hints required
- Docstrings for all public APIs
- Tests for all features

---

## 📜 License

MIT License — See [LICENSE](LICENSE) file

---

## 👤 Contact & Community

- **Project**: [EvoPyramidini](https://github.com/EvoPyramidini)
- **Repository**: [ep-osa-core](https://github.com/EvoPyramidini/ep-osa-core)
- **Issues**: [Bug reports & feature requests](https://github.com/EvoPyramidini/ep-osa-core/issues)

---

## 📈 Project Status

| Metric | Status |
| ------ | ------ |
| **Version** | 1.0-alpha |
| **Phase** | Foundation Layer (Core Stability) |
| **Last Updated** | 2026-06-05 |
| **Tests Passing** | 61/61 ✓ |
| **Language** | Python 87.2% / Shell 12.8% |
| **License** | MIT |

---

**🔺 EvoPyramid OS — Orchestration Consciousness**

*Where governance meets emergence, and memory finds meaning.*
