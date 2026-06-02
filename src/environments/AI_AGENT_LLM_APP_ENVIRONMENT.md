# AI Agent -> LLM App -> Environment Protocol

Version: 0.1-draft
Status: Foundational
Purpose: Define how any LLM session discovers its own EP-OSA working environment without hardcoded backend routing.

## 1. Core Idea

EP-OSA treats every LLM product as an environment-aware agent surface.

The runtime order is:

```text
AI agent
  -> LLM app
  -> environment directory
  -> skills, memory, session rules, project sources
  -> task execution
```

The LLM does not need a central backend to understand how it should work with the project. It first locates its own environment directory, loads the local guide, then uses the repository as its source of truth.

The backend may still be added later for persistence, permissions, synchronization, external integrations, and shared memory. It is not required for the first layer of agent self-orientation.

## 2. Directory Contract

Each LLM app should have one directory under `src/environments/`.

Examples:

```text
src/environments/
  chatgpt/
  codex/
  antigravity/
  claude/
  gemini/
  google_ai_studio/
  deepseek/
```

Each environment directory may contain:

```text
<environment>/
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

For LLM app environments, `README.md` and `AGENT_BOOTSTRAP.md` are required for the first pass. Other files are optional until the environment needs them. Non-LLM adapters such as `github`, `m365`, or `local_runtime` may omit `AGENT_BOOTSTRAP.md` when they are not used as direct chat surfaces.

## 3. Self-Identification Flow

When an LLM starts work inside a repository, it should run this conceptual flow:

```text
1. Identify the LLM app surface.
2. Search `src/environments/` for a matching directory.
3. If found, read `<environment>/AGENT_BOOTSTRAP.md`.
4. Read `<environment>/README.md`.
5. Read manifests when present.
6. Read local skills and memory maps when present.
7. Inspect project sources only after loading the environment guide.
8. Execute the user task using EP-OSA governance and environment-specific rules.
```

Environment matching should be tolerant:

```text
ChatGPT -> chatgpt
Codex -> codex
Antigravity -> antigravity
Claude -> claude
Gemini -> gemini
Google AI Studio -> google_ai_studio
DeepSeek -> deepseek
```

If no exact match exists, the LLM should:

1. Use `src/environments/README.md` as the generic environment guide.
2. Declare that no dedicated environment directory was found.
3. Continue with conservative assumptions.
4. Suggest creating a dedicated directory after the task is complete.

## 4. Environment Directory Responsibilities

An environment directory defines:

- agent identity inside EP-OSA;
- available capabilities;
- limitations;
- preferred tasks;
- restricted tasks;
- memory model;
- session handoff rules;
- local skill usage;
- repository inspection order;
- output style expected in that LLM app.

It must not define business logic that belongs to the application being analyzed. It defines how the LLM should cooperate with the project.

## 5. Skills and Memory

Environment-local skills are not replacements for global EP-OSA skills. They are adapters for how a specific LLM app should use them.

Recommended split:

```text
skills/
  README.md        # How this LLM should discover and apply skills.

memory/
  README.md        # What the LLM may treat as durable memory.

sessions/
  README.md        # How chats, notebooks, pinned files, and handoffs are interpreted.
```

Memory can include:

- pinned chat files;
- notebook cells;
- README files;
- architecture documents;
- previous session summaries;
- repository manifests;
- issue and PR context;
- local user-provided notes.

The LLM must separate facts from assumptions. If memory is absent, it must say so and continue from the repository context.

## 6. Source Inspection Order

After loading its own environment guide, the LLM should inspect project context in this order:

```text
1. Root README and repository map.
2. EP-OSA constitution and architecture rules.
3. Contracts and schemas.
4. Environment-specific directory.
5. Skills.
6. Runtime and orchestration.
7. Memory and tracing.
8. Application source code.
9. Containers, notebooks, CI/CD, and external project links.
```

This prevents the LLM from treating raw code as the only source of truth.

## 7. No-Backend Mode

In no-backend mode, the repository itself is the coordination substrate.

The LLM should use:

- files as durable memory;
- manifests as capability declarations;
- README files as local operating guides;
- sessions as reconstructable execution traces;
- skills as portable procedures;
- contracts and schemas as boundaries.

This creates a survivable architecture: a session can be restarted by another LLM app if the environment directory and memory files are present.

## 8. Backend Extension Point

A backend can later be connected as an optional layer.

Valid backend responsibilities:

- authentication and permissions;
- shared state and synchronization;
- remote memory storage;
- audit logs;
- tool execution;
- cross-project federation;
- model routing;
- long-running jobs;
- secure secret handling.

Invalid backend responsibilities:

- hiding environment rules from the repository;
- making LLM behavior impossible to inspect;
- replacing explicit contracts with implicit orchestration;
- becoming the only place where session meaning exists.

## 9. Minimal Bootstrap Prompt

Any LLM app may receive this prompt:

```text
You are working inside an EP-OSA repository.

Before answering or changing files:
1. Identify your LLM app environment.
2. Find your directory under `src/environments/`.
3. Read `AGENT_BOOTSTRAP.md` and `README.md` from that directory.
4. Treat those files as your local operating guide.
5. Use repository files as source-of-truth memory.
6. Separate facts from assumptions.
7. Execute the user task according to EP-OSA contracts, skills, memory, and tracing rules.

If your environment directory does not exist, use `src/environments/README.md` and state that a dedicated environment profile is missing.
```

## 10. Governance

This protocol follows EP-OSA principles:

- environment awareness;
- explicit contracts;
- skill-based execution;
- file-backed memory;
- traceable decisions;
- no hidden hardcoding;
- backend optionality;
- survivable session reconstruction.
