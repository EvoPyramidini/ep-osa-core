# Skills Layer

**Agent capabilities and behaviors.**

This layer defines composable, contract-respecting capabilities that agents can execute to accomplish their tasks.

## Purpose

Skills provide:

- Composable units of capability
- Clear input/output contracts
- Schema-driven interaction
- Observable execution
- Reusable components

## Skill Definition

```python
class Skill:
    name: str              # Unique skill name
    version: str           # Semantic versioning
    description: str       # What skill does
    input_schema: Schema   # Expected input
    output_schema: Schema  # Expected output
    
    async def execute(self, input_data) -> output_data:
        """Execute skill with input, return output"""
        pass
```

## Skill Categories

### Foundation Skills

- State observation
- Memory access
- Basic operations
- Error handling

### Domain Skills

- Domain-specific expertise
- Complex behaviors
- Multi-step operations
- Integration points

### Composite Skills

- Combine multiple skills
- Sequence operations
- Handle coordination
- Manage failure cases

## Skill Properties

### Required

- Name (unique within skill namespace)
- Version
- Input schema
- Output schema
- Execute function

### Optional

- Pre-conditions
- Post-conditions
- Side-effects
- Resource limits
- Timeout
- Retry strategy

## Skill Execution

1. Agent selects skill
2. Validates input against schema
3. Checks pre-conditions
4. Executes skill async
5. Validates output against schema
6. Checks post-conditions
7. Returns result or error
8. Records in trace

## Skill Composition

Skills can be combined:

```python
SkillA | SkillB | SkillC  # Sequential
SkillA & SkillB           # Parallel
if condition: SkillA else: SkillB
while condition: Skill
```

## Error Handling

Skills must handle:

- Invalid input
- Timeout conditions
- Resource exhaustion
- Downstream failures
- Cancellation requests

## Skill Development

### Creating a New Skill

1. Define contract in contracts/
2. Define schemas in schemas/
3. Implement in skills/
4. Add documentation
5. Add unit tests
6. Add integration tests

### Skill Versioning

- Follow semantic versioning
- Maintain backward compatibility
- Deprecate old versions gradually
- Support migration paths

## Related Files

- See ../ARCHITECTURE_RULES.md for skill rules
- See ../contracts/ for skill contracts
- See ../schemas/ for data schemas
- See ../TERMINOLOGY.md for definitions

**Last Updated:** 2026-05-14
