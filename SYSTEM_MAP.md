# EP-OSA System Map

## Layer Topology
- governance/
- schemas/
- contracts/
- runtime/
- memory/
- agents/
- adr/
- environments/

## Primary Invariants
1. Governance precedes execution.
2. Every intent MUST pass a validation gate.
3. Agents never execute raw prompts directly.
4. Decisions MUST be traceable and replayable.
5. Memory is partitioned by scope.
6. Model instances are interchangeable cognitive processors; project state lives outside the model.

## Context Loading Profiles
- Cold: philosophy, architecture, ontology, invariants.
- Warm: active schemas, contracts, current ADR set, environment manifests.
- Hot: task state, changed files, execution trace window.

## Source of Truth Priority
1. schemas/
2. contracts/
3. policies/
4. adr/
5. manifests in `environments/*/manifests/`
6. docs/

## Runtime Reconstruction Flow
1. Load governance + invariants.
2. Load environment manifest + provider map.
3. Negotiate allowed capabilities/actions.
4. Materialize task context (cold/warm/hot).
5. Produce auditable artifacts and state updates.

## Navigation Contract
- Human-readable docs explain intent and rationale.
- Machine-readable schemas, contracts, and manifests govern executable truth.
- If prose conflicts with schema/contract/manifest rules, machine-readable artifacts win.


## Federation Anchor
- `environments/federation-map.json` defines active environment mesh roles and synchronization invariants.
