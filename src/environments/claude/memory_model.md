# Claude Memory Model

Claude operates with a **layered memory architecture** — each layer has different
persistence duration, capacity, and use cases within EP-OSA-core.

---

## Memory Layers (Mapped to EvoMemorySystem Proportions)

### Layer 1: Session Context (~60% — Primary Operational)

**What it is:** The active conversation window. Everything said and done in the
current session is in context.

**Properties:**
- Duration: Single conversation session
- Capacity: Up to 200k tokens (practical ~100k)
- Access: Instantaneous, native
- Persistence: Lost on session end

**EP-OSA role:** Primary operational memory. Active skill state, current schemas,
execution traces, recent orchestration results.

**Usage in ep-osa-core:**
```
Active during: skill execution, contract validation, schema checks,
               orchestration coordination, tracing
Contains: current task, loaded skills, active contracts, execution trace window
```

---

### Layer 2: Artifact Persistent Storage (~30% — Buffer Layer)

**What it is:** A key-value store accessible from Claude Artifacts (React/HTML).
Data persists **across sessions** — survives conversation end.

**API:**
```javascript
// Store
await window.storage.set('memory:anchor:001', JSON.stringify(anchor));

// Retrieve
const result = await window.storage.get('memory:anchor:001');
const anchor = result ? JSON.parse(result.value) : null;

// List all anchors
const keys = await window.storage.list('memory:anchor:');

// Shared across all users
await window.storage.set('shared:pattern:001', data, true);
```

**Key naming convention for ep-osa-core:**
```
memory:anchor:{id}        — Memory anchors
memory:context:{id}       — Saved context snapshots
session:trace:{id}        — Execution traces
skill:state:{skill_name}  — Skill runtime state
evo:pattern:{id}          — Approved patterns (evo-research-brainstorms)
agent:checkpoint:{id}     — Agent evolution checkpoints
```

**Properties:**
- Duration: Persistent (cross-session, indefinite)
- Capacity: Up to 5MB per key
- Access: Via Artifact code only
- Persistence: Permanent until explicitly deleted

**EP-OSA role:** Buffer layer and evolution seeds. Stores memory anchors, approved
patterns, context snapshots, skill states.

**Limitations:**
- Only accessible inside Artifacts, not from bash or Claude's direct reasoning
- Text/JSON only (no binary)
- Rate limited (batch related data in single keys)

---

### Layer 3: Claude.ai Memory (~10% — Reserve / Semantic Index)

**What it is:** When enabled by user, Claude extracts semantic memories from
conversations and stores them as persistent facts about the user, their projects,
and preferences.

**Properties:**
- Duration: Permanent (user-controlled)
- Capacity: Managed by Anthropic (~thousands of facts)
- Access: Automatic injection into new conversations
- Persistence: Until user deletes

**Enable:** Settings → Memory → Enable memory

**EP-OSA role:** Reserve memory and semantic anchors. High-value facts about the
EP-OSA architecture, user intent, long-term goals, approved decisions.

**What Claude should store here (suggest to user):**
```
- Core EvoPyramid architectural decisions
- User's preferred interaction patterns
- Key terminology definitions
- Approved patterns from evo-research-brainstorms/approved_patterns/
- Current project phase and priorities
```

**Limitations:**
- User must enable manually
- Claude cannot force what gets stored (it's extracted automatically)
- Not queryable programmatically

---

### Layer 4: File System (Operational — Session-scoped)

**What it is:** Files created during a session in `/mnt/user-data/outputs/` are
downloadable and persistent on the user's side if saved.

**Properties:**
- Duration: Session (available for download during and after)
- Capacity: Container disk limits
- Access: bash_tool, create_file, str_replace
- Persistence: User must download to keep

**EP-OSA role:** Implementation of schema/contract/skill artifacts, generated
documents, execution traces written to disk.

---

## Memory Navigation (QuantumBackpack Equivalent)

Within EP-OSA-core, Claude uses the following navigation strategy:

### Cold Load (session start)
```
1. Read SYSTEM_MAP.md → understand topology
2. Read constitution/ → load governance
3. Read ontology/ → load terminology and invariants
4. Check context/cold.md profile
```

### Warm Load (active task)
```
1. Read relevant schemas/ for current task
2. Read relevant contracts/ for interaction type
3. Load applicable ADR files
4. Check context/warm.md profile
```

### Hot Load (execution)
```
1. Current task specification
2. Changed files in scope
3. Execution trace window from tracing/
4. Check context/hot.md profile
```

---

## Memory Anchors Strategy

When Claude creates a memory anchor within ep-osa-core artifacts:

```json
{
  "id": "anchor_{timestamp}_{slug}",
  "semantic_label": "Human-readable description",
  "layer": "primary | buffer | reserve",
  "content_summary": "What this anchor points to",
  "tags": ["ep-osa", "layer-name", "relevant-concept"],
  "created_at": "ISO timestamp",
  "evolution_value": "high | medium | low",
  "connections": ["anchor_id_1", "anchor_id_2"]
}
```

---

## Memory Proportions in Practice

```
EP-OSA Rule 1.4 / Rule 8.1: 50-60% Primary / 30% Buffer / 10% Reserve

Claude mapping:
├── 50-60%: Session context (active conversation)
│           Skills loaded, contracts validated, current execution
├── 30%:    Artifact storage (cross-session key-value)
│           Anchors, patterns, snapshots, skill states
└── 10%:    Claude.ai memory (semantic reserve)
            Core facts, user intent, architectural decisions
```

---

**Last Updated:** 2026-05-18
**Version:** 1.0-alpha
