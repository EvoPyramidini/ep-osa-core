# Agent Coordination Policy

## Agent role in EP-OSA-Core
Agents are bounded operators in a topology-first orchestration system.

## Behavioral contract
Agents must operate as constrained executors:
- they do not own global system state;
- they do not define topology rules;
- they do not bypass routing and supervision contracts.

## Mandatory behavior
- Respect Core vs Memory vs Capability boundaries.
- Treat EP-OSA-Core as coordination intelligence, not a general backend.
- Publish outputs through contracts and orchestration surfaces.
- Route memory/capability usage via topology semantics and explicit protocols.
- Prefer predictable, contract-compliant actions over opportunistic shortcuts.

## Anti-patterns
- Embedding RAG/vector/state internals directly into Core runtime.
- Conflating orchestration and heavy execution logic in one module.
- Building giant-agent control planes that bypass topology contracts.
- Treating agents as autonomous owners of infrastructure policy.
