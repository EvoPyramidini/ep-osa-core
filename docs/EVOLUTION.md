# Evolution Roadmap

## Current phase
Stabilize topology and architectural boundaries before implementation-heavy expansion.

## Near-term priorities
1. Formalize core contracts around orchestration, routing, and supervision.
2. Preserve strict separation between Core and Memory ecosystem.
3. Model layered routing semantics (intent -> context -> capability selection -> execution).
4. Keep capability integrations interchangeable through stable interfaces.

## Engineering lake principle
Historic repositories and old experiments are not discarded; they are treated as evolutionary engineering biomass:
- reusable patterns;
- historical execution artifacts;
- future architectural resources.

## Success criteria
- Core remains lightweight and coordination-focused.
- Memory systems are externally composable and execution-aware.
- Capability layers scale without converting Core into a monolith.
