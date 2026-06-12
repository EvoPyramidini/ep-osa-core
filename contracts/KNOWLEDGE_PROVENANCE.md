# STANDARD: KNOWLEDGE_PROVENANCE.md

**Version:** 1.0  
**Status:** Stable  
**Layer:** Layer 2 (Contracts)  
**Depends on:** INTER_ENVIRONMENT_HANDOFF.md, memory-snapshot.json

---

## 1. Purpose

To define a model‑agnostic method for any EP‑OSA environment to declare the **provenance of its knowledge claims** – i.e., where a statement, fact, or conclusion comes from.

This enables a receiving environment or Human Governor to distinguish between observed facts, logical inferences, emulated behaviours, and proposed extensions.

---

## 2. Scope

**In scope:**

- Any factual claim made by an environment (state entries, answers, documentation, responses).  
- Knowledge embedded in handoff snapshots.  
- Environment self‑descriptions (`capabilities.md`, `limitations.md`).

**Out of scope:**

- Low‑level model internals (weights, activations).  
- Cryptographic proof of origin.

---

## 3. Provenance Categories

| Category | Definition | Example |
| -------- | ---------- | ------- |
| **Observed** | Directly available in the environment’s specification, API, runtime introspection, or supplied artifacts. | “The environment has no file system.” (from `capabilities.md`) |
| **Inferred** | Logically derived from Observed facts without new assumptions. | “Because JSON parsing is available, the environment can validate schemas.” |
| **Emulated** | Behaves *as if* a capability exists, but it is not natively implemented. Must state what is emulated. | “HCMP memory hierarchy is emulated via text descriptions; no real L1–L4 storage.” |
| **Proposed** | A recommendation to change the federation, add a contract, or modify a schema. Not yet observed or validated. | “A new field `emulated_layers` should be added to memory‑snapshot.json.” |
| **External** | Information obtained from outside the environment (user message, retrieved document). Source must be cited. | “The user stated that the repository contains `x.md`.” |
| **Uncertain** | The environment cannot confidently assign any other category. Forces Human Governor review. | “It is unclear whether this capability is observed or emulated.” |

---

## 4. Required Fields

For each knowledge claim in a structured artifact (snapshot, handoff payload, or explicit answer), include:

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | string | Unique identifier within the snapshot (e.g., `know-abc123`). |
| `statement` | string | The claim being made. |
| `primary_category` | enum (above) | Main provenance category. |
| `evidence` | array of strings | References to source artifacts or observations. |
| `confidence` | enum (High, Medium, Low) | Certainty of the claim. |

---

## 5. Serialization

### 5.1 JSON Schema Fragment

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "KnowledgeProvenance",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "statement": { "type": "string" },
    "primary_category": {
      "type": "string",
      "enum": ["Observed", "Inferred", "Emulated", "Proposed", "External", "Uncertain"]
    },
    "evidence": { "type": "array", "items": { "type": "string" } },
    "confidence": { "type": "string", "enum": ["High", "Medium", "Low"], "default": "High" }
  },
  "required": ["id", "statement", "primary_category", "evidence"]
}
```

### 5.2 Markdown Serialization

```markdown
## Knowledge Provenance

- **ID:** know-001
  - **Statement:** The environment has no persistent memory.
  - **Category:** Observed
  - **Evidence:** `capabilities.md`, line 12
  - **Confidence:** High
```

---

## 6. Handoff & Federation Implications

· When sending a snapshot, the environment MUST attach knowledge provenance to each state entry.
· The receiving environment SHALL NOT upgrade an Emulated claim to Observed without independent verification.
· If a claim’s provenance is missing, treat as Uncertain and request clarification.

---

End of Standard
