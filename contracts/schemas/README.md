# Schemas Layer

**Data structures and type definitions.**

This layer defines the shape, validation rules, and semantics of all data flowing through the system.

## Purpose

Schemas provide:
- Data structure definitions
- Validation rules
- Type safety
- Cross-environment compatibility
- Serialization standards
- Documentation

## Schema Categories

### 1. Core Schemas
- State representations
- Event definitions
- Message formats
- Configuration structures

### 2. Domain Schemas
- Domain-specific data types
- Business entity definitions
- Integration data formats
- API contracts

### 3. System Schemas
- Traces and logs
- Metrics and observability
- Error representations
- Resource descriptors

## Schema Format

Schemas use JSON Schema standard with extensions:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "Schema Title",
  "description": "Schema description",
  "properties": {
    "field1": {
      "type": "string",
      "description": "Field description"
    }
  },
  "required": ["field1"]
}
```

## Schema Organization

```
schemas/
├── core/           # Core system schemas
├── domain/         # Domain-specific schemas
├── system/         # System and observability schemas
└── definitions/    # Reusable schema components
```

## Schema Versioning

- Each schema has explicit version
- Breaking changes increment major version
- Backward compatible changes increment minor version
- Patch version for fixes

## Related Files

- See ../contracts/ for contract schemas
- See ../ARCHITECTURE_RULES.md for schema rules
- See ../TERMINOLOGY.md for definitions

**Last Updated:** 2026-05-14