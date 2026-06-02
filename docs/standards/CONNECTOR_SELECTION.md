# Connector Selection Standard

Version: 0.1-draft
Status: Foundational
Purpose: Define how EP-OSA AI work environments choose connector routes without binding behavior to model names.

## Core Principle

EP-OSA does not bind behavior to model names.

```text
Models are participants.
Environments are operational contexts.
Connectors are routes.
Users approve actions.
```

An AI assistant must not choose a connector because of model identity, preference, or convenience. Connector selection is driven by the active environment, the user's intent, available capabilities, governance constraints, risk, and user confirmation.

## Connector Neutrality Principle

Connectors are not rights granted to an AI.

Connectors are conditional routes that may be used only when the current task, environment, permissions, risk level, and user confirmation allow it.

For example:

```text
github
```

means:

```text
A GitHub route may exist.
```

It does not mean:

```text
The AI has permission to read, write, commit, open pull requests, or modify repository state.
```

## Selection Flow

Connector selection follows this order:

```text
Environment
  -> Intent
  -> Capability Check
  -> Connector Check
  -> Governance Check
  -> User Confirmation
  -> Action
```

### 1. Environment

Identify the AI work environment first.

Examples:

- ChatGPT
- Claude
- Gemini
- Codex
- Google Antigravity
- Google AI Studio
- DeepSeek

These are treated as operational contexts where an AI assistant interacts with the user and project. The active model inside the environment is secondary unless the environment exposes it explicitly.

### 2. Intent

Identify the user's actual task intent.

Examples:

- inspect a repository;
- edit project files;
- search external knowledge;
- read a document;
- send a message;
- create an event;
- run a local check;
- hand off work to another environment.

### 3. Capability Check

Determine whether the current environment can satisfy the task without a connector.

If local context is enough, no connector should be selected.

### 4. Connector Check

If the task needs an external route, check whether the environment profile declares a relevant connector route.

A declared connector route is still conditional. It is not an authorization.

### 5. Governance Check

Check the task against EP-OSA governance, contracts, schemas, environment limitations, and risk envelope.

The AI must separate:

- read-only inspection;
- reversible local changes;
- external writes;
- irreversible or sensitive actions.

### 6. User Confirmation

State-changing or externally visible actions require explicit user confirmation.

Examples:

- sending email;
- creating or updating calendar events;
- modifying files;
- committing or pushing changes;
- opening pull requests;
- deleting resources;
- sharing documents;
- changing permissions.

Read-only actions may be used when the user request clearly implies them and the environment allows them, but the AI should still disclose the route used.

### 7. Action

Use the selected connector only for the narrow task that justified it.

If conditions are not met, do not use the connector. Ask for confirmation, use a safer route, or explain that the route is unavailable.

## Per-Environment Responsibility

Each environment profile should define:

- what the AI can see in that interface;
- what it can do directly;
- which connector routes may exist;
- which actions require confirmation;
- which actions are forbidden;
- how handoff to another environment should work.

Environment profiles live under:

```text
src/environments/<environment>/
```

## Session Self-Assessment

The AI may describe its current strengths for the active task, but this is not permanent truth.

Session self-assessment is temporary unless the user approves saving it.

The AI should express uncertainty when it cannot verify its own environment, connector access, or available tools.

Recommended self-assessment format:

```text
Environment: <active AI work environment>
Task intent: <interpreted user intent>
Current strengths for this task: <short list>
Limitations: <short list>
Connector needed: yes/no
Candidate connector route: <route or none>
Risk level: low/medium/high
User confirmation required: yes/no
Confidence: low/medium/high
```

## Examples

### Repository Inspection

User intent:

```text
Check this GitHub repository.
```

Decision:

```text
Environment -> current AI app
Intent -> repository inspection
Capability Check -> local repo or GitHub route may satisfy task
Connector Check -> GitHub route if remote inspection is required
Governance Check -> read-only
User Confirmation -> not required if the request clearly implies inspection
Action -> inspect repository and report findings
```

### Sending a Summary

User intent:

```text
Send the architecture summary by email.
```

Decision:

```text
Environment -> current AI app
Intent -> external message delivery
Capability Check -> cannot complete without external connector
Connector Check -> Gmail/email route
Governance Check -> externally visible write
User Confirmation -> required
Action -> send only after explicit confirmation
```

### Google Antigravity

User works inside Google Antigravity.

Decision:

```text
Environment -> Google Antigravity
Active model -> secondary or unknown
Intent -> derived from user request
Connector Check -> based on Antigravity environment profile
Action -> chosen route must follow Antigravity profile and user confirmation rules
```

## Final Rule

No connector is selected because an AI wants to use it.

A connector is selected because the task requires a route, the environment supports it, governance permits it, and the user has approved any external or state-changing action.

