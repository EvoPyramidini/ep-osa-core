# Codex Local Skill Notes

Codex uses this directory for environment-specific skill guidance.

Global EP-OSA skills live at:

```text
skills/
```

Codex should:

- inspect global skills before inventing a workflow;
- use local notes here only as adapters for Codex-specific execution;
- keep implementation steps tied to real repository files;
- prefer small, verifiable edits;
- update documentation when an environment rule changes.

Suggested Codex skill sequence:

```text
1. Discover task intent.
2. Load Codex bootstrap.
3. Inspect relevant EP-OSA skill files.
4. Inspect target source files.
5. Edit only scoped files.
6. Verify when feasible.
7. Report changes and residual risk.
```

