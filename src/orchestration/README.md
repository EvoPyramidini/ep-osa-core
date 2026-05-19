# Orchestration Layer (Weightless Control)

**Field-Driven Agent Direction & Coordination.**

This layer abandons classic hard-coded execution paths (DAGs, imperative sequences) in favor of the **Weightless Control Protocol** (Magnetic Orchestration). Execution is emergent, guided by semantic gravity fields rather than explicit "Go To X" commands.

## Purpose

The Orchestration layer provides:
- **Semantic Vector Field Generation**: Turning user needs into spatial attractors.
- **Puck (Agent) Injection**: Placing agents into the field to resolve tension.
- **Entropy Balancing**: Ensuring agents do not get trapped in metastable equilibrium (local minima).
- **Dynamic Routing**: Autonomous agent movement towards high-priority nodes.

## The Paradigm Shift

### OLD (Deprecated)
```
Start → Skill1 → if(x) → Skill2 → End
```
*Rigid, fragile, prone to routing explosions when scaling.*

### NEW (Magnetic Orchestration)
```
EnvironmentState: {
  "target_ruins": 0.8,
  "system_pressure": 1.5,
  "entropy": 0.1
}

Puck (Agent) => Calculates argmax() of field => Moves to "target_ruins".
```
*Fluid, scalable, naturally fault-tolerant.*

## The 4 Layers of the Field

1. **Field Engine**: Constantly evaluates global Z-levels and outputs the `EnvironmentState` tensor (JSON). It is the source of gravity.
2. **Agent Sensorium**: The active Agent (Puck) continuously polls the `EnvironmentState`.
3. **Motion Resolver**: The Agent applies its specific `Role Affinity` against the field weights to determine its next target node/skill.
4. **Field Mutation Engine**: Once a Puck resolves a high-gravity node, the engine neutralizes that magnet, altering the field topology so the Puck moves to the next highest gradient.

## The Entropy Balancer

To prevent "Buridan's ass" deadlocks (where an agent is caught equally between two 0.9 magnets), the Field Engine injects thermodynamic noise (entropy). Every N cycles, random attractors receive a temporary gradient boost (+0.2) to force a decision.

## Related Files

- See `../docs/MAGNETIC_ORCHESTRATION_MANIFEST.md` for the full architectural vision.
- See `../schemas/core/environment_state.json` for the field tensor schema.
- See `../ARCHITECTURE_RULES.md` for constitutional limits on agent motion.

**Last Updated:** 2026-05-19