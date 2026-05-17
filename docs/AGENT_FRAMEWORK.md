# Agent Framework

This document explains the lightweight coordination framework for agents within the ep-osa-core architecture.

## Overview
The Agent Framework provides a minimal yet flexible structure for building and orchestrating agents. These agents coordinate tasks between ep-osa-core and external backend systems.

### Key Features
- Lightweight architecture.
- Configurable task routing.
- Backend integrations (e.g., AI engineering, data solutions).
- Extendable agent behaviors.

---

## Structure

### Directories
```
ep-osa-core/
├── agents/
│   ├── base_agent.py        # Base class for all agents
│   └── osi_agent/
│       ├── osi.py           # Orchestrator agent
│       └── directives.py    # Task-specific instructions
│
├── orchestration/
│   ├── agent_orchestrator.py    # Central coordination logic
│   ├── task_router.py           # Routes tasks to proper destinations
│   └── environment_selector.py  # Selects environment context
│
├── interfaces/
│   ├── backend_connector.py     # API calls to external services
│   └── websocket_bridge.py      # Real-time WebSocket handling
│
└── config/
    ├── backend_endpoints.yaml   # Configurable backend endpoints
    ├── agent_config.yaml        # General agent configurations
    └── routing_rules.yaml       # Task routing rules
```

### Agents
- `OsiAgent`: Coordinates tasks and invokes orchestration paths.
- `BaseAgent`: Parent class with default behaviors and lifecycle management.

### Orchestration
- `AgentOrchestrator`: Routes tasks to appropriate agents or backend systems.
- `TaskRouter`: Resolves the correct endpoint for a task.
- `EnvironmentSelector`: Identifies which environment/context to use.

---

## Next Steps
- Implement base agent classes.
- Finalize backend endpoint configurations.
- Begin writing lightweight integration tasks.
