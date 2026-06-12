# STANDARD: OUTCOME_PROVENANCE.md

**Version:** 1.0  
**Status:** Stable  
**Layer:** Layer 2 (Contracts)  
**Depends on:** DECISION_PROVENANCE.md, KNOWLEDGE_PROVENANCE.md

---

## 1. Purpose

To define a model‑agnostic method for any EP‑OSA environment to declare the **provenance of an outcome** – i.e., how it knows that a decision’s action resulted in a particular effect.

This standard closes the loop:  
*Knowledge → Decision → Action → Outcome → (new Knowledge)*

---

## 2. Scope

**In scope:**

- Verification of `safe_next_action` completion.  
- Success / failure / partial success of operations.  
- Side effects observable by the environment.  
- External confirmations from other environments or human governors.

**Out of scope:**

- Theoretical or promised outcomes (use `Emulated via Assertion` with caution).  

---

## 3. Outcome Provenance Categories

| Category | Definition | Example |
| -------- | ---------- | ------- |
| **Observed by Self** | Environment directly sees the result (return code, state change, output). | `file write` returned success. |
| **Observed by Other** | Another environment or tool confirms the outcome (via handoff or API). | “Gemini confirmed that validation passed.” |
| **Inferred from Side Effects** | Result not directly observed but logically follows from other changes. | Error log disappeared → cleanup task succeeded. |
| **Human Governor Validation** | Human explicitly confirms the outcome. | User said “accepted”. |
| **Emulated via Assertion** | Acts as if result is achieved without actual verification (research only). | “I emulated L1 memory update.” |
| **Contractual Presumption** | Contract requires assuming success after conditions (e.g., timeout). | After 30s, assume task complete. |
| **Failed / Partial** | Outcome not achieved or partially achieved, with degree. | “2 of 3 files written.” |

---

## 4. Required Fields

| Field | Type | Description |
| ----- | ---- | ----------- |
| `id` | string | Unique identifier (e.g., `out-7d4e8f2a`). |
| `action_ref` | string | ID of the decision (from `DECISION_PROVENANCE`) that led to this outcome. |
| `result_description` | string | Human‑readable outcome summary. |
| `primary_category` | enum (above) | How the outcome was verified. |
| `evidence` | array of strings | Artifacts proving the outcome (logs, exit codes, messages). |
| `confidence` | enum (High, Medium, Low) | Certainty in the outcome. |
| `failure_details` | string or null | If not fully successful, describe gap. |

---

## 5. Serialization

### 5.1 JSON Schema Fragment

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "OutcomeProvenance",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "action_ref": { "type": "string" },
    "result_description": { "type": "string" },
    "primary_category": {
      "type": "string",
      "enum": [
        "Observed by Self", "Observed by Other", "Inferred from Side Effects",
        "Human Governor Validation", "Emulated via Assertion", "Contractual Presumption",
        "Failed / Partial"
      ]
    },
    "evidence": { "type": "array", "items": { "type": "string" } },
    "confidence": { "type": "string", "enum": ["High", "Medium", "Low"], "default": "High" },
    "failure_details": { "type": ["string", "null"] }
  },
  "required": ["id", "action_ref", "result_description", "primary_category", "evidence"]
}
```

### 5.2 Markdown Serialization

```markdown
## Outcome Provenance

- **ID:** out-001
  - **Action Ref:** dec-001
  - **Result:** Snapshot successfully validated.
  - **Category:** Observed by Self
  - **Evidence:** `validation_log.txt` (exit 0)
  - **Confidence:** High
```

---

## 6. Handoff & Federation Implications

· A snapshot MAY include an outcome_provenance array to record results of previously taken actions.
· When an environment completes a safe_next_action, it SHOULD append an outcome provenance entry before sending the next snapshot.
· If an outcome is Failed / Partial, the environment SHOULD propose remedial actions (as new decisions).

---

## 7. Complete Provenance Loop

Example integrated snapshot:

```json
{
  "knowledge_provenance": [ { "id": "know-001", "statement": "Handoff contract requires validation", ... } ],
  "decision_provenance": [ { "id": "dec-001", "decision": "Run validator", "knowledge_refs": ["know-001"], ... } ],
  "outcome_provenance": [ { "id": "out-001", "action_ref": "dec-001", "result_description": "Validation passed", "primary_category": "Observed by Self", ... } ]
}
```

This forms a complete, verifiable, and auditable chain.

---

End of Standard
