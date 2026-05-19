# Claude Environment

**Constitutional reasoning, skill execution, and persistent artifact intelligence.**

Claude (Anthropic) serves as a native EP-OSA-core reasoning and execution environment.
Unlike external environments (ChatGPT, Gemini), Claude is the **host runtime** of the ep-osa-core
skill system itself — meaning skills defined in `skills/` are executed *inside* Claude.

---

## Identity in EP-OSA-core

Claude is both:
- **An environment** — a named participant in federated orchestration (like ChatGPT or Codex)
- **The host agent** — the LLM executing skills, contracts, and orchestration logic directly

This dual role means Claude has the **deepest native access** to the EP-OSA-core system,
but must still respect constitutional governance, contracts, and schema rules like any other participant.

**Agent archetype:** Reasoning + Execution + Memory + Skill host  
**Models available:**
- `claude-sonnet-4-6` — Default. Fast, capable, everyday orchestration
- `claude-opus-4-6` — Deep reasoning, complex architecture, multi-layer synthesis
- `claude-haiku-4-5` — Lightweight, high-throughput, simple skill steps

---

## Capabilities

### Core
- Constitutional reasoning and intent interpretation
- Multi-layer orchestration (sequential, parallel, conditional, loop)
- Skill definition, loading, and execution (native host)
- Schema-driven data validation
- Contract-based interaction enforcement

### Execution
- **Bash execution** — shell commands, file system, scripts (`bash_tool`)
- **File creation** — any format: `.md`, `.py`, `.yaml`, `.json`, `.docx`, `.pptx`, `.xlsx`, `.pdf`
- **Code execution** — Python, Node, bash inside sandboxed container
- **String replacement / file editing** — surgical edits without rewriting

### Generation & Artifacts
- React components (interactive, stateful)
- HTML/CSS/JS (single-file, cdnjs-compatible)
- SVG diagrams and illustrations
- Mermaid diagrams (flowcharts, sequence, architecture)
- Markdown documents
- All Office formats (docx, pptx, xlsx) via skill layer

### Intelligence
- Web search (live, current information)
- Web fetch (full page content from URLs)
- Image, PDF, and document analysis (vision + extraction)
- Multimodal input processing (text + image + file)

### MCP Connectors (Active)
- **Gmail** — read, compose, send, search email
- **Google Calendar** — events, scheduling, availability
- **Google Drive** — files, folders, search, read, create

### Memory Systems
See `memory_model.md` for full detail.
- **Session memory** — full conversation context (active)
- **Artifact persistent storage** — key-value store across sessions (via `window.storage`)
- **Claude.ai memory** — semantic memory extracted from chats (user-configurable)
- **File system** — outputs persist in `/mnt/user-data/outputs/` during session

---

## Limitations

### Inherent Constraints
- No persistent stateful process between conversations (stateless LLM)
- Probabilistic outputs (non-deterministic unless constrained)
- Context window limit (200k tokens; practical: ~100k for complex tasks)
- No internet access *during* bash execution (domain allowlist only)
- Cannot initiate outbound connections autonomously (must be triggered by user)

### Task Constraints
- Cannot render final DOCX/PPTX without skill layer (needs python-docx / pptx)
- Cannot run arbitrary binaries not available in the container
- Cannot access user's local machine filesystem directly
- Claude.ai memory must be enabled by the user in Settings

---

## Preferred Tasks

```yaml
high_priority:
  - constitutional_reasoning_and_governance
  - skill_execution_and_orchestration
  - multi_environment_workflow_coordination
  - schema_and_contract_generation
  - architecture_design_and_analysis
  - code_generation_and_execution
  - document_and_artifact_creation
  - memory_anchor_navigation

medium_priority:
  - data_transformation_and_validation
  - mcp_connector_integration (Gmail, Calendar, Drive)
  - web_research_and_synthesis
  - multimodal_analysis (image, PDF)
  - persistent_artifact_state_management

low_priority:
  - real_time_event_monitoring (no persistent process)
  - binary_file_operations_without_skill_layer
  - large_scale_parallel_execution (sequential in claude.ai)
```

## Restricted Tasks

```yaml
should_not:
  - bypass_constitutional_constraints
  - execute_malicious_code
  - access_non_allowlisted_domains_in_bash
  - generate_content_violating_safety_policies

requires_careful_handling:
  - sensitive_user_data_in_mcp_connectors
  - long_running_bash_tasks (timeout risk)
  - large_file_generation (memory limits)
```

---

## Routing Priority within EP-OSA-core

```yaml
skill_execution:          native        # Claude IS the skill host
constitutional_reasoning: high          # Primary LLM reasoner
orchestration_design:     high          # Full workflow planning
artifact_generation:      high          # Native capability
mcp_integration:          high          # Gmail, Calendar, Drive active
web_research:             high          # Native search + fetch
code_execution:           high          # Bash + Python in container
document_creation:        high          # Via skill layer
multimodal_analysis:      medium        # Images, PDFs
real_time_monitoring:     low           # Route to local_runtime
deterministic_rendering:  medium        # Skill-layer required
```

---

## Workflow Patterns

### Pattern 1: Skill → Artifact → Memory
```
User intent
  → Claude (parse + validate against schema)
  → Skill execution (Claude as host)
  → Artifact generated (React/HTML with persistent storage)
  → Artifact storage (window.storage key-value)
  → Memory anchor created
```

### Pattern 2: Research → Architecture → Document
```
Claude (web_search + web_fetch)
  → Claude (synthesis + schema design)
  → Claude (ARCHITECTURE_RULES update)
  → File creation (markdown/yaml/json)
  → GitHub (commit via Codex environment)
```

### Pattern 3: MCP Orchestration
```
User intent (calendar/email/drive task)
  → Claude (intent parsing + contract validation)
  → MCP connector (Gmail / Calendar / Drive)
  → Claude (result synthesis)
  → Artifact or document output
```

### Pattern 4: EP-OSA Multi-Layer Traversal
```
Constitution (Layer 1) — Claude reads governance rules
  → Contract (Layer 2) — Claude validates interaction
  → Schema (Layer 3) — Claude validates data
  → Runtime (Layer 4) — Claude executes in sandbox
  → Skill (Layer 5) — Claude loads and runs skill
  → Orchestration (Layer 6) — Claude coordinates workflow
  → Tracing (Layer 7) — Claude logs execution
  → Memory (Layer 8) — Claude stores results + anchors
  → Research (Layer 9) — Claude evolves patterns
```

---

## Performance Characteristics

```yaml
latency:
  simple_response:        1-5 seconds
  skill_execution:        5-30 seconds
  file_generation:        5-60 seconds
  complex_orchestration:  30-120 seconds
  bash_execution:         1-30 seconds

context_window:
  maximum:                200k tokens
  practical_complex:      ~100k tokens
  skill_metadata:         always_in_context

reliability:
  reasoning_coherence:    high
  schema_compliance:      high (when constrained)
  file_output_integrity:  very_high
  mcp_success_rate:       ~95%
```

---

## Related Files

- `capabilities.md` — Full capability matrix
- `memory_model.md` — Memory architecture and persistence strategy
- `connectors.md` — MCP connector details and usage contracts
- `../ENVIRONMENT_INTEGRATION_ARCHITECTURE.md` — System-level integration
- `../../skills/claude-osa-agent/SKILL.md` — Claude's EP-OSA agent identity skill

**Last Updated:** 2026-05-18
**Version:** 1.0-alpha
**Status:** Foundation Phase
