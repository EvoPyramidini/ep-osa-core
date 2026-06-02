# Environment Directory Template

Use this template when adding a new LLM app environment.

```text
src/environments/<environment>/
  README.md
  AGENT_BOOTSTRAP.md
  manifests/
    environment-manifest.json
    memory-map.json
  skills/
    README.md
  memory/
    README.md
  sessions/
    README.md
```

## README.md

Describe the LLM app as an EP-OSA environment:

- identity;
- capabilities;
- limitations;
- preferred tasks;
- restricted tasks;
- routing priority;
- integration rules.

## AGENT_BOOTSTRAP.md

Define the first instructions the LLM must follow after discovering this directory.

It should include:

- self-identification;
- required files to read;
- source inspection order;
- memory handling;
- skill handling;
- execution rules;
- response style.

## manifests/environment-manifest.json

Machine-readable capability declaration.

Recommended fields:

```json
{
  "environment": "environment_name",
  "display_name": "Environment Name",
  "status": "draft",
  "agent_order": ["AI-agent", "LLM-app", "environment"],
  "capabilities": [],
  "limitations": [],
  "preferred_tasks": [],
  "restricted_tasks": [],
  "bootstrap": "AGENT_BOOTSTRAP.md",
  "memory_map": "manifests/memory-map.json"
}
```

## manifests/memory-map.json

Machine-readable memory index.

Recommended fields:

```json
{
  "environment": "environment_name",
  "memory_sources": {
    "local": ["memory/README.md"],
    "sessions": ["sessions/README.md"],
    "skills": ["skills/README.md"],
    "project": ["README.md", "docs/", "contracts/", "src/"]
  },
  "rules": [
    "Prefer repository facts over model assumptions.",
    "Separate facts from hypotheses.",
    "Record durable session knowledge in files when requested."
  ]
}
```

## skills/README.md

Explain how this LLM app should use EP-OSA skills.

## memory/README.md

Explain what counts as memory for this LLM app.

## sessions/README.md

Explain how the LLM app should interpret chats, notebooks, pinned files, and handoff notes.

