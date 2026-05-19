# ADR 001: Dynamic Skill Discovery (Agent Introspection)

## Status

Accepted

## Context

Initially, the `ep-osa-core` architecture relied on static contract definitions (`contract.yaml`) and markdown specifications (`SKILL.md`) mapped manually for each external backend system (e.g., `evopyramid-ai`, `Project-EP-OS`, `EvoGenesis`). This created a high maintenance burden and violated the principle of agent autonomy, as the core had to dictate what external agents could do.

## Decision

We decided to adopt a **Dynamic Capability Discovery** model (Service Discovery via Agent Introspection).
Instead of hardcoding external agent capabilities, `ep-osa-core` now defines a strict boundary schema: `schemas/core/capability_discovery.json`.

External agents are responsible for generating and serving their own capability manifests matching this schema. The orchestrator uses the new `ep-osa-discovery` skill to poll, validate, and dynamically load these capabilities at runtime.

## Consequences

### Positive

- **Decentralization:** Backend teams can update their agents' capabilities without requiring a PR to `ep-osa-core`.
- **Autonomy:** Agents act as independent subjects proposing their skills ("Шайба берет магнит").
- **Scalability:** New backend projects can join the EvoPyramid federation instantly if they comply with the schema.

### Negative

- **Validation Overhead:** The orchestrator must perform strict JSON Schema validation on every new connection.
- **Security Risks:** Malformed or malicious capability manifests could break the orchestrator if validation (the "Border Controller") is flawed. This mitigates the need for strict compliance checks.

## Implementation Details

- Added `schemas/core/capability_discovery.json`
- Added `skills/ep-osa-discovery/SKILL.md`
- **Rule Update:** All dynamically loaded skills are confined to Layer 1 (Session Context) memory to prevent permanent corruption of the host.
