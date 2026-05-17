# EP-OSA Core Architecture

## Architectural stance
EP-OSA-Core is a **lightweight orchestration nucleus**. It must not evolve into a heavyweight backend monolith.

## Core responsibilities
EP-OSA-Core owns only coordination-centric concerns:
- orchestration;
- routing;
- contracts;
- topology semantics;
- event coordination;
- agent protocols;
- supervision abstractions;
- environment coordination.

## Coordination HQ model
The HQ layer is a **coordination consciousness layer**, not a centralized server platform.

## Separation of concerns
### In-scope for EP-OSA-Core
- topology-driven orchestration;
- semantic routing across environments;
- protocol-level coordination between agents and capabilities.

### Out-of-scope for EP-OSA-Core
Memory-heavy and data-plane cognition systems are externalized to Pyramid/SKneogen layers, including:
- RAG infrastructure;
- vector storage;
- operational experience graphs;
- topology persistence;
- contextual reconstruction pipelines.

## Guardrails
- Keep runtime minimal and orchestration-first.
- Do not embed memory internals into runtime core.
- Do not collapse memory + capability + orchestration into a giant agent.
- Keep heavy computation and infrastructure external.

## Final ecosystem model
Pyramid -> Topology Engine -> Memory Layer <-> Capability Layer -> External Infrastructure.
