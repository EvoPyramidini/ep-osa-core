# Environments Layer

**Federated execution ecosystems and external system integration.**

This layer manages orchestration across multiple execution environments.

## Purpose

The Environments layer provides:
- Normalized environment interaction
- Capability-aware routing
- Cross-environment orchestration
- Execution ecology management
- Environment governance
- LLM app self-identification through local environment directories
- File-backed skills, memory, and session handoff without mandatory backend routing

## Agent Order

EP-OSA environment execution follows this order:

```text
AI-agent -> LLM-app -> environment directory -> skills/memory/session context -> execution
```

See `AI_AGENT_LLM_APP_ENVIRONMENT.md` for the full protocol.

## Supported Environments

### 1. ChatGPT
- Advanced reasoning
- Architecture analysis
- Planning and synthesis
- Context-aware response generation

**See:** `chatgpt/`

### 2. Codex
- Code generation
- Repository management
- GitHub integration
- DevOps automation

**See:** `codex/`

### 3. M365
- Document execution
- Excel processing
- Strict schema validation
- Business automation

**See:** `m365/`

### 4. GitHub
- Repository governance
- Version control
- Issue and PR management
- Release management

**See:** `github/`

### 5. Gemini
- Multimodal analysis
- Image reasoning
- Media processing
- Visual understanding

**See:** `gemini/`

### 6. Local Runtime
- Private computation
- Deterministic execution
- Offline operation
- Security-sensitive tasks

**See:** `local_runtime/`

### 7. Antigravity
- Reserved LLM app environment
- Future IDE and agent-workspace workflows

**See:** `antigravity/`

### 8. Google AI Studio
- Reserved LLM app environment
- Model prototyping and API-oriented workflows

**See:** `google_ai_studio/`

### 9. DeepSeek
- Reserved LLM app environment
- Reasoning, coding, and cost-aware execution paths

**See:** `deepseek/`

## Key Principles

### 1. Environment Awareness
All routing decisions aware of environment capabilities and constraints.

### 2. Capability-Driven
Tasks routed to environments best suited for their requirements.

### 3. Governed Integration
All cross-environment interaction respects constitutional principles.

### 4. Observable Execution
All environment calls traced and audited.

### 5. Federated Collaboration
Environments may collaborate through controlled orchestration.

## Environment Model

Each environment defines:
- **Capabilities**: What it can do
- **Limitations**: What it cannot do
- **Preferred Tasks**: What it excels at
- **Restricted Tasks**: What it should not do
- **Routing Priority**: How important it is for different tasks
- **Integration Rules**: How to interact with it
- **Governance Constraints**: What policies apply
- **Bootstrap Rules**: How the LLM self-identifies and starts work
- **Memory Map**: Which files count as durable environment memory
- **Session Rules**: How chats, notebooks, pinned files, and handoffs are interpreted

## Orchestration Flow

```
1. Task arrives at orchestration layer
   ↓
2. Analyze task requirements
   ↓
3. Evaluate environment compatibility
   ↓
4. Select optimal environment(s)
   ↓
5. Route to environment with proper contracts
   ↓
6. Execute with full tracing
   ↓
7. Collect results and validate
   ↓
8. Merge results or route to next environment
   ↓
9. Return to orchestration layer
```

## Related Files

- See `ENVIRONMENT_INTEGRATION_ARCHITECTURE.md` for system design
- See `{environment}/README.md` for environment-specific details
- See `../orchestration/` for workflow coordination
- See `../ARCHITECTURE_RULES.md` for integration rules
- See `../TERMINOLOGY.md` for definitions

## Directory Structure

```
environments/
├── ENVIRONMENT_INTEGRATION_ARCHITECTURE.md
├── README.md
├── chatgpt/
│   ├── README.md
│   ├── manifest.yaml
│   ├── capabilities.md
│   ├── workflows.md
│   └── integration_rules.md
├── codex/
│   ├── README.md
│   ├── manifest.yaml
│   ├── implementation_policy.md
│   └── workflows.md
├── m365/
│   ├── README.md
│   ├── manifest.yaml
│   ├── strict_document_execution.md
│   └── workflows.md
├── github/
│   ├── README.md
│   ├── manifest.yaml
│   ├── repository_governance.md
│   └── workflows.md
├── gemini/
│   ├── README.md
│   ├── manifest.yaml
│   ├── multimodal_workflows.md
│   └── integration_rules.md
└── local_runtime/
    ├── README.md
    ├── manifest.yaml
    ├── privacy_constraints.md
    └── workflows.md
```

**Last Updated:** 2026-05-14
