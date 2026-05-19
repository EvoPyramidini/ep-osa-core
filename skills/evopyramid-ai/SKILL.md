---
name: evopyramid-ai-connector
description: >
  Skill for interacting with the evopyramid-ai backend.
  Provides access to LLM reasoning, prompt generation, and neural network inference capabilities.
  Use this skill when the agent needs to delegate complex cognitive tasks to the dedicated AI engine.
---

# evopyramid-ai Integration

This skill defines the interface between the EP-OSA agent (the Puck) and the `evopyramid-ai` backend.

## Identity & Purpose

- **Role:** AI compute offloading and specialized reasoning.
- **Scope:** Allows the orchestrator to pass raw data or complex queries to the backend AI engine for processing.

## Capabilities

1. `generate_completion`: Requests a text completion or reasoning step from the backend LLM.
2. `analyze_data`: Sends structured data for pattern recognition or summarization.

## Usage Rules

- All requests must conform to the schemas defined in `contract.yaml`.
- Do not use this skill for simple logic that can be executed natively via Python/Bash.
- Handle timeouts gracefully, as backend AI operations may be slow (Async-First Rule).

## Memory Integration

Results from `evopyramid-ai` should typically be stored in the Primary Session memory, or anchored if they represent a significant evolutionary step.
