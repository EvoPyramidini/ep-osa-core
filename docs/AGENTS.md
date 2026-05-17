# Agent Coordination Policy

## Agent role in EP-OSA
Agents are bounded operators in a topology-first system.

## Mandatory behavior
- Respect core/memory/capability separation.
- Avoid introducing giant-agent patterns.
- Publish outputs through contracts and orchestration surfaces.

## Anti-patterns
- Embedding retrieval/state internals directly into runtime core.
- Blending orchestration and heavy execution logic in one module.
- Treating agents as the primary architecture instead of orchestrated components.
