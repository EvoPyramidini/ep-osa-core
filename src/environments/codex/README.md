# Codex Environment

**Code generation and repository management.**

Codex serves as the primary implementation engine for ep-osa-core.

## Capabilities

### Core Capabilities
- High-quality code generation
- Repository management
- GitHub API integration
- DevOps automation
- Code review and analysis
- Implementation guidance
- Framework-specific patterns

### Advanced Features
- Multi-language support
- Context-aware code generation
- Technical architecture implementation
- Testing code generation
- Documentation code generation

## Limitations

### Inherent Constraints
- Probabilistic generation (not guaranteed optimal)
- May generate anti-patterns if not guided
- Limited understanding of long-term system goals
- Cannot guarantee performance optimization

### Task Constraints
- Cannot design system architecture (delegate to ChatGPT)
- Cannot validate business logic correctness
- Cannot ensure testing coverage
- Cannot manage cross-repository coordination

## Preferred Tasks

```yaml
high_priority:
  - code_generation
  - implementation_from_spec
  - repository_file_operations
  - github_workflow_creation
  - devops_automation

medium_priority:
  - code_refactoring
  - test_generation
  - documentation_code
  - example_implementation

low_priority:
  - architectural_planning
  - strategic_decisions
```

## Restricted Tasks

```yaml
should_not:
  - system_architecture_design (use ChatGPT)
  - business_logic_design (use ChatGPT)
  - strategic_planning (use ChatGPT)
  - document_formatting (use M365)

requires_verification:
  - security_sensitive_code
  - cryptographic_operations
  - performance_critical_code
  - data_processing_logic
```

## Routing Priority

```yaml
implementation_tasks: high       # Primary use case
code_generation: high            # Core capability
github_operations: high          # Well-integrated

refactoring: medium              # Requires review
test_generation: medium          # Needs validation

architecture: low                # Delegate to ChatGPT
strategy: low                    # Delegate to ChatGPT
```

## Integration Rules

### 1. Contract Structure
```python
{
  "environment": "codex",
  "task_type": "code_generation",
  "context": {
    "repository": "owner/repo",
    "branch": "branch_name",
    "language": "python|javascript|etc",
    "framework": "framework_name",
    "style_guide": "style_guide_url"
  },
  "specification": {
    "description": "what to implement",
    "requirements": ["req1", "req2"],
    "constraints": ["constraint1"]
  },
  "expected_output": {
    "files": ["file1.py", "file2.py"],
    "tests": ["test_file1.py"],
    "documentation": ["docstring", "comments"]
  }
}
```

### 2. Workflow Patterns

#### Pattern 1: Specification → Implementation
```
ChatGPT (architecture spec)
  → Codex (implementation)
  → Codex (test generation)
  → GitHub (push and PR)
```

#### Pattern 2: Repository Enhancement
```
GitHub (PR/Issue analysis)
  → ChatGPT (solution design)
  → Codex (implementation)
  → Codex (test generation)
  → GitHub (commit and merge)
```

#### Pattern 3: Multi-File Orchestration
```
Orchestration (task list)
  → Codex (file1 implementation)
  → Codex (file2 implementation)
  → Codex (test generation)
  → GitHub (batch push)
```

### 3. Repository Governance

#### Code Style
- Follow repository style guide
- Automatic formatting enforcement
- Linting rules compliance
- Type hints required
- Docstring standards

#### Testing Requirements
- Unit tests for all public functions
- Integration tests for cross-module interactions
- Minimum coverage threshold (e.g., 80%)
- Edge case testing

#### Documentation
- Comprehensive docstrings
- Type annotations
- Example usage
- Architecture decision records

### 4. GitHub Integration

#### Branch Strategy
- Feature branches from develop
- Branch naming: `feature/description`
- Pull requests required for merge
- Status checks must pass
- Code review required

#### Commit Standards
- Descriptive commit messages
- Atomic commits (single logical change)
- Reference issues when applicable
- Sign commits if required

#### PR Workflow
1. Create feature branch
2. Generate implementation code
3. Generate tests
4. Push and create PR
5. Wait for review
6. Address feedback
7. Merge when approved

## Performance Characteristics

```yaml
latency:
  simple_function: 5-10 seconds
  complex_module: 15-30 seconds
  multi_file_project: 30-120 seconds

throughput:
  lines_per_generation: 100-500
  files_per_batch: 1-10
  tokens_per_request: up to 128k

reliability:
  code_compilability: 95%+
  style_compliance: 90%+
  test_validity: 80%+
```

## Best Practices

### 1. Specification Quality
- Clear, detailed descriptions
- Include context and constraints
- Provide examples if complex
- Reference existing patterns

### 2. Code Review
- Always review generated code
- Check for security issues
- Verify performance implications
- Test before merging

### 3. Testing
- Validate all generated tests
- Add missing edge cases
- Ensure sufficient coverage
- Test integration points

### 4. Documentation
- Review generated docstrings
- Ensure accuracy
- Add architecture notes
- Update README if needed

## Related Files

- See `../ENVIRONMENT_INTEGRATION_ARCHITECTURE.md` for system design
- See `../github/` for repository governance details
- See `../orchestration/` for workflow patterns
- See `../runtime/` for execution contexts

**Last Updated:** 2026-05-14