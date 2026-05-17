# Field Orchestration

## Intent
Model EP-OSA behavior through orchestrated fields rather than centralized autonomous agents.

## Core concepts
- Field signals are first-class runtime inputs.
- Orchestrators coordinate transitions and routing.
- Agents remain modular executors, not system owners.

## Design constraints
- Prioritize topology consistency over local implementation shortcuts.
- Keep orchestration deterministic where possible.
- Route memory/capability interactions through contracts.
