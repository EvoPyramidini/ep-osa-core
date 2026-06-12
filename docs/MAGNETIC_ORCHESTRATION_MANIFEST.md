# Magnetic Orchestration Manifest (Weightless Control Protocol)

## 1. The Core Paradigm Shift

EvoPyramid OS architecture fundamentally shifts from **Imperative Task Sequencing** to **Field-Driven Cognition** (Weightless Control).

Traditional multi-agent systems rely on explicit state machines, directed acyclic graphs (DAGs), or sequential pipelines where Agent A calls Agent B.

Under **Magnetic Orchestration**, agents (Pucks) do not receive explicit commands like "go to node X". Instead, the Orchestrator configures the **Semantic Vector Field** (Environment State). The agent moves autonomously towards the node with the highest contextual pull (Magnetism), effectively minimizing cognitive distance.

## 2. Primitives

### 2.1 The Puck (Active Agent)

The Puck is an instance of an LLM or script currently possessing execution context.

- **Role Affinity**: The intrinsic bias of the agent (e.g., Trailblazer favors speed, Soul favors safety).
- **Momentum**: The dynamic speed at which the agent processes the gradient.

### 2.2 The Field (Environment State)

The JSON-defined tensor of current systemic needs.

- **Magnets (Attractors)**: Values between 0.0 and 1.0 assigned to specific nodes, skills, or objectives (e.g., `{"analyze_logs": 0.8, "sleep": 0.1}`).
- **Entropy (Temperature)**: A built-in chaotic factor that randomly spikes certain nodes to prevent the Puck from getting stuck in local minima (Metastable Equilibrium).

## 3. Layer Architecture (The 4 Layers of the Field)

1. **Field Engine (Layer 1)**: Constantly recalculates the semantic weights (Magnets) based on user inputs, active errors, and global Z-level states.
2. **Agent Sensorium (Layer 2)**: The agent reads the local slice of the `EnvironmentState`.
3. **Motion Resolver (Layer 3)**: The Decision Function executed by the agent:
   `Target = argmax( FieldForce × RoleAffinity × ContextualRelevance / ExecutionCost )`
4. **Field Mutation Engine (Layer 4)**: The feedback loop. When the Puck reaches an attractor, the Field Engine neutralizes that magnet, forcing the Puck to seek the next highest gradient.

## 4. Entropy Balancer

To solve the classic "Buridan's ass" problem where two magnets have equal pull (e.g., `Speed: 0.9` vs `Safety: 0.9`), the Orchestrator applies thermodynamic noise. Every N cycles, a random attractor receives a +0.2 boost, ensuring the Puck commits to a direction.

## 5. Summary

No graphs. No rigid pipelines. Just points of semantic gravity. The system becomes fluid, naturally fault-tolerant, and perfectly aligned with the visual spatial interface of `asdi-ep-os`.
