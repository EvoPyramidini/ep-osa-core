# GitHub Environment

**Repository governance and version control.**

GitHub serves as the central repository and governance engine for ep-osa-core.

## Capabilities

### Core Capabilities
- Repository management
- Version control operations
- Issue and PR management
- Branch strategy enforcement
- Release management
- Workflow automation
- Repository governance

### Advanced Features
- GitHub Actions workflows
- Branch protections
- Code review enforcement
- Status checks
- Release automation
- Archive and audit

## Limitations

### Inherent Constraints
- API rate limits
- Webhook limits
- File size constraints
- Repository limits

### Task Constraints
- Cannot perform reasoning (delegate to ChatGPT)
- Cannot generate code (delegate to Codex)
- Cannot process documents (delegate to M365)
- Cannot execute arbitrary code

## Preferred Tasks

```yaml
high_priority:
  - repository_management
  - version_control
  - issue_management
  - pull_request_workflows
  - branch_strategy

medium_priority:
  - release_management
  - workflow_automation
  - status_tracking
  - contribution_tracking

low_priority:
  - code_generation (use Codex)
  - reasoning (use ChatGPT)
  - document_processing (use M365)
```

## Restricted Tasks

```yaml
should_not:
  - semantic_reasoning
  - code_generation (delegate to Codex)
  - document_processing (delegate to M365)
  - arbitrary_computation

requires_careful_handling:
  - sensitive_credentials
  - large_file_operations
  - bulk_operations
  - destructive_operations
```

## Routing Priority

```yaml
repository_operations: high      # Primary use case
version_control: high            # Core capability
issue_management: high           # Well-integrated

workflow_automation: medium      # Configurable
release_management: medium       # Orchestrated

code_generation: low             # Use Codex
reasoning: low                   # Use ChatGPT
```

## Integration Rules

### 1. Contract Structure
```python
{
  "environment": "github",
  "operation": "repository_op|version_control|issue_management",
  "repository": "owner/repo",
  "context": {
    "branch": "branch_name",
    "commit_sha": "sha_or_ref",
    "pull_request": "pr_number"
  },
  "action": {
    "type": "read|write|delete",
    "target": "files|issues|prs|releases"
  },
  "validation": {
    "permissions_required": ["permission_list"],
    "status_checks": ["check_list"]
  }
}
```

### 2. Repository Governance

#### Branch Strategy
```
main
  - Production-ready code
  - Only merged via PR
  - Status checks required
  - Protected from direct push

develop
  - Integration branch
  - Feature PRs merge here
  - Status checks required
  - Protected from direct push

feature/*
  - Individual feature branches
  - Created from develop
  - PR to develop
  - Deleted after merge

hotfix/*
  - Emergency fixes
  - Created from main
  - PR to main
  - Backported to develop
```

#### PR Workflow
1. Create feature branch from develop
2. Implement changes with full tracing
3. Push to branch
4. Create PR with description
5. Ensure all checks pass
6. Request reviews
7. Address feedback
8. Merge when approved
9. Delete feature branch

### 3. Issue Management

#### Issue Types
- **Bug**: Something not working
- **Feature**: New capability
- **Enhancement**: Improve existing
- **Documentation**: Docs improvement
- **Architecture**: System design
- **Research**: Investigation

#### Issue Lifecycle
```
Opened
  → Triaged (assigned, labeled)
  → In Progress (started work)
  → In Review (awaiting feedback)
  → Closed (resolved or rejected)
```

### 4. Traceability

#### Commits
- Atomic commits (single logical change)
- Descriptive messages
- Reference related issues: `Fixes #123`
- Sign commits if required

#### PRs
- Link to related issues
- Clear description of changes
- Test coverage documentation
- Performance impact assessment

#### Releases
- Semantic versioning
- Changelog entries
- Release notes
- Tagged commits

## Workflow Patterns

### Pattern 1: Issue → Implementation → Release
```
GitHub Issue (requirement)
  → Feature Branch (create)
  → Codex (implement)
  → Tests (generate & validate)
  → PR (submit)
  → Review (feedback)
  → Merge (integrate)
  → Release (tag & publish)
```

### Pattern 2: Multi-Environment Orchestration
```
GitHub Issue (task)
  → ChatGPT (design)
  → Codex (implementation)
  → M365 (documentation)
  → GitHub (commit & PR)
  → Testing (validation)
  → GitHub (merge & release)
```

### Pattern 3: Continuous Governance
```
GitHub Actions (trigger)
  → Linting (code quality)
  → Testing (unit & integration)
  → Security (analysis)
  → Performance (benchmarks)
  → Merge (if all pass)
```

## Performance Characteristics

```yaml
latency:
  api_call: 100-500ms
  push_operation: 1-5 seconds
  pr_creation: 1-3 seconds
  status_check: 30-120 seconds

throughput:
  rate_limit: 5000/hour (authenticated)
  concurrent_operations: 10s
  batch_size: 100 items

reliability:
  api_availability: 99.9%
  data_integrity: 100%
  operation_success: 99%+
```

## Best Practices

### 1. Repository Organization
- Clear directory structure
- Comprehensive documentation
- Reusable workflows
- Consistent conventions

### 2. Code Review
- Review before merge
- Check tests pass
- Verify quality standards
- Ensure documentation

### 3. Release Management
- Semantic versioning
- Clear changelogs
- Tagged releases
- Release notes

### 4. Automation
- GitHub Actions for CI/CD
- Automated testing
- Automated deployment
- Status checks

## Related Files

- See `../ENVIRONMENT_INTEGRATION_ARCHITECTURE.md` for system design
- See `repository_governance.md` for detailed governance rules
- See `branching_strategy.md` for branch details
- See `pull_request_policy.md` for PR guidelines
- See `../orchestration/` for workflow patterns

**Last Updated:** 2026-05-14