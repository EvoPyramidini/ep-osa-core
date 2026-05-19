---
name: ep-osa-discovery
description: >
  System skill for dynamic capability introspection (Service Discovery).
  Used by the orchestrator to query an external backend agent and dynamically load its skills into active memory.
---

# EP-OSA Agent Discovery Skill

This skill acts as the **"Border Controller"** (Фейс-контроль). It bridges the static core architecture with dynamic, external backend agents (like `EvoGenesis` or `evopyramid-ai`).

## Identity & Purpose

- **Role:** Dynamic Contract Validation and Skill Registration.
- **Scope:** Runs during session initialization (Warm Load) or when a new backend agent connects.

## Execution Flow

1. **Query:** The orchestrator sends a capability request to the target backend agent's discovery endpoint.
2. **Receive:** The backend agent responds with its manifest payload.
3. **Validate:** The orchestrator validates the payload strictly against `schemas/core/capability_discovery.json`.
4. **Enforce Constitution:** If `constitutional_compliance_flag` is missing or false, the connection is instantly rejected.
5. **Register:** Validated capabilities are mapped into the orchestrator's active session memory (Layer 1 - 60% memory).
6. **Trace:** Success or failure is logged in Layer 7 Tracing.

## Usage Rules

- NEVER bypass schema validation.
- If an agent's schema changes mid-session, the connection must be dropped and renegotiated.
- Dynamically loaded skills persist only for the duration of the session unless anchored explicitly.

## Example Trigger

"Query the `EvoGenesis` agent for its available capabilities and load them if compliant."
