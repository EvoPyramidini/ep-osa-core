# ADR-003: Schema-First Governance

- **Status**: Accepted
- **Date**: 2026-05-18

## Decision
EP-OSA treats `schemas/` and `contracts/` as primary execution truth.
Human-oriented prose (`docs/`) is secondary explanatory context.

## Consequences
- Agents and runtime must prioritize machine-readable policy and contract artifacts.
- Documentation may not override schema/contract constraints.
- CI policy should enforce schema/contract validation before execution.

## Invariant impact
Reinforces invariants around governance-first and validated execution.
