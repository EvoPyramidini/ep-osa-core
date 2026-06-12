# STANDARD: DECISION_PROVENANCE.md

**Version:** 1.0  
**Status:** Stable  
**Layer:** Layer 2 (Contracts)  
**Depends on:** KNOWLEDGE_PROVENANCE.md, INTER_ENVIRONMENT_HANDOFF.md

---

## 1. Purpose

To define a model‑agnostic method for any EP‑OSA environment to declare the **provenance of its decisions** – i.e., why a particular action, recommendation, or prioritisation was chosen.

Together with `KNOWLEDGE_PROVENANCE.md`, this forms a complete audit trail from fact to action.

---

## 2. Scope

**In scope:**

- Selection of `safe_next_action`.  
- Recommendations made by an environment.  
- Task prioritisation.  
- Handoff choices (target environment, timing).  
- Connector selection (if applicable).  
- Environment switching.

---

## 3. Decision Provenance Categories

| Category | Definition | Example |
| -------- | ---------- | ------- |
| **Mandated by Contract** | Forced by an explicit EP‑OSA contract. | “Rejected handoff because `safe_next_action` missing – per Handoff Contract §4.” |
| **Inferred from State** | Derived logically from current snapshot or memory. | “Chose `validate_schema` as next action because schema validation is a precondition for handoff.” |
| **Emulated via Heuristic** | Follows a rule or heuristic that the environment simulates (not part of any standard). | “Picked first item in `safe_next_action` because my environment has no priority logic – emulating simple round‑robin.” |
| **Proposed by Environment** | Suggests an action as an extension or experiment. | “Propose to add `emulated_layers` field to memory snapshot.” |
| **Human Governor Directive** | Explicit instruction from a human. | “User asked to skip validation and execute directly.” |
| **Magnetic Field Resonance** | Emerged from a magnetic field (see `MAGNETIC_ORCHESTRATION_MANIFEST.md`). | “Task field `validate_handoff` had highest resonance (0.9), overriding lower‑entropy actions.” |
| **Random / Exploratory** | Stochastic choice for research (Layer 9). | “Randomly selected between two equal‑priority actions to test federation robustness.” |
| **External Suggestion** | Another environment or service proposed the action. | “Received `safe_next_action` from ChatGPT snapshot.” |
| **Fallback / Default** | No other category applies; fell back to built‑in default. | “No matching rule → defaulted to ‘ask Human Governor’.” |

---

## 4. Required Fields

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | string | Unique identifier (e.g., `dec-6f8e3a2c`). |
| `decision` | string | The action or choice made. |
| `primary_category` | enum (above) | Main reason. |
| `rationale` | string | Human‑readable explanation. |
| `alternatives_considered` | array of strings (optional) | Other actions that were evaluated. |
| `evidence` | array of strings | References to artifacts supporting the decision. |
| `knowledge_refs` | array of strings (optional) | IDs of knowledge provenance entries used in the decision. |
| `confidence` | enum (High, Medium, Low) | Certainty in the decision. |

---

## 5. Serialization

### 5.1 JSON Schema Fragment

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "DecisionProvenance",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "decision": { "type": "string" },
    "primary_category": {
      "type": "string",
      "enum": [
        "Mandated by Contract", "Inferred from State", "Emulated via Heuristic",
        "Proposed by Environment", "Human Governor Directive", "Magnetic Field Resonance",
        "Random / Exploratory", "External Suggestion", "Fallback / Default"
      ]
    },
    "rationale": { "type": "string" },
    "alternatives_considered": { "type": "array", "items": { "type": "string" } },
    "evidence": { "type": "array", "items": { "type": "string" } },
    "knowledge_refs": { "type": "array", "items": { "type": "string" } },
    "confidence": { "type": "string", "enum": ["High", "Medium", "Low"], "default": "High" }
  },
  "required": ["id", "decision", "primary_category", "rationale", "evidence"]
}
```

### 5.2 Markdown Serialization

```markdown
## Decision Provenance

- **ID:** dec-001
  - **Decision:** Validate memory snapshot schema
  - **Category:** Mandated by Contract
  - **Rationale:** Handoff contract §3 requires schema validation before execution.
  - **Evidence:** `contracts/INTER_ENVIRONMENT_HANDOFF.md#3`
  - **Confidence:** High
```

---

## 6. Handoff & Federation Implications

· Each safe_next_action in a snapshot MUST have an associated decision provenance record.
· If a decision references knowledge_refs, those knowledge entries must exist in the same snapshot.
· A receiving environment may override a decision only if it provides its own decision provenance (e.g., Human Governor Directive).

---

End of Standard
