# EP-OSA System Map

## Layer Topology
- governance/
- schemas/
- contracts/
- runtime/
- memory/
- agents/
- adr/

## Primary Invariants
1. Governance precedes execution.
2. Every intent MUST pass a validation gate.
3. Agents never execute raw prompts directly.
4. Decisions MUST be traceable and replayable.
5. Memory is partitioned by scope.

## Context Loading Profiles
- Cold: philosophy, architecture, ontology, invariants.
- Warm: active schemas, contracts, current ADR set.
- Hot: task state, changed files, execution trace window.

## Source of Truth Priority
1. schemas/
2. contracts/
3. policies/
4. adr/
5. docs/

## Navigation Contract
- Human-readable docs explain intent and rationale.
- Machine-readable schemas and contracts govern executable truth.
- If prose conflicts with schema/contract rules, schema/contract wins.
