---
name: project-ep-os-ui
description: >
  Skill for interacting with the Project-EP-OS local browser and Pyramid widget.
  Use this skill to update the user interface, push notifications, or read user events from the OS shell.
---

# Project-EP-OS UI Integration

This skill defines the interface for manipulating the spatial visualization and local browser environment of the EvoPyramid OS.

## Identity & Purpose
- **Role:** User Interface and OS Shell integration.
- **Scope:** Controls what the user sees on the "Board" (the 3D pyramid widget, local browser DOM, etc.).

## Capabilities
1. `update_pyramid_state`: Changes the color, animation, or structural representation of the Pyramid widget based on agent states.
2. `push_notification`: Sends a message to the local browser UI.
3. `read_user_event`: Polls or listens for specific interactions from the UI layer.

## Usage Rules
- UI updates must be non-blocking.
- Never send raw backend error traces directly to the UI without formatting them into human-readable notifications.

## Memory Integration
UI state changes are ephemeral and should only be logged in Tracing (Layer 7), not persisted in long-term memory unless they represent a major state transition.
