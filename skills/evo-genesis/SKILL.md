---
name: evo-genesis-bootstrap
description: >
  Skill for interacting with the EvoGenesis backend.
  Use this skill to initiate system bootstrapping, world-building generation, or major structural mutations in the environment.
---

# EvoGenesis Integration

This skill defines the interface for triggering genesis and evolutionary generation processes on the EvoGenesis backend.

## Identity & Purpose
- **Role:** System bootstrapping and major structural generation.
- **Scope:** Allows the orchestrator to trigger heavy, long-running processes that generate new environments, agents, or foundational data structures.

## Capabilities
1. `bootstrap_environment`: Triggers the creation of a new workspace or agent topology.
2. `mutate_structure`: Requests an evolutionary change to an existing data structure based on new parameters.

## Usage Rules
- All operations are highly resource-intensive and must strictly follow the `Async-First` execution rule.
- Do not call Genesis operations for trivial data updates.
- Must provide full context of the current state before requesting a mutation (Soul Coherence).

## Memory Integration
Genesis events are critical. They must always result in the creation of a High-Value Memory Anchor (Reserve Semantic Layer) so the system remembers its evolutionary leaps.
