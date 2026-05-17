# core

Coordination nucleus of EP-OSA-Core.

## Owns
- orchestration and routing primitives;
- contracts and topology semantics;
- event coordination and supervision abstractions.

## Does not own
- memory persistence, vector stores, or RAG internals;
- heavyweight execution backends.
This directory is reserved for the topology-first EP-OSA architecture.

## Purpose
- Keep runtime lightweight and orchestration-centric.
- Isolate concerns from memory and capability ecosystems.

## Status
- Scaffold only; implementation to be introduced incrementally.
