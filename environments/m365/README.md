# M365 Environment

**Document execution and strict schema validation.**

M365 serves as the deterministic document processing engine for ep-osa-core.

## Capabilities

### Core Capabilities
- Precise Word document creation
- Excel data processing
- Strict schema validation
- Deterministic rendering
- Document structure enforcement
- Business document automation
- Data ingestion from Excel

### Advanced Features
- Template-based document generation
- Complex Excel formulas
- Cross-sheet data integration
- Validation rule enforcement
- Document versioning

## Limitations

### Inherent Constraints
- Limited to Office document formats
- Performance constraints for large datasets
- No direct API for all operations
- Requires proper authentication

### Task Constraints
- Cannot perform reasoning (delegate to ChatGPT)
- Cannot generate code (delegate to Codex)
- Cannot manage repositories (delegate to GitHub)
- Cannot handle unstructured reasoning

## Preferred Tasks

```yaml
high_priority:
  - word_document_creation
  - excel_data_processing
  - schema_validation
  - deterministic_document_rendering
  - structured_data_ingestion

medium_priority:
  - document_templates
  - data_transformation
  - report_generation
  - compliance_documentation

low_priority:
  - freeform_writing (use ChatGPT)
  - data_analysis (use local runtime)
```

## Restricted Tasks

```yaml
should_not:
  - semantic_reasoning (delegate to ChatGPT)
  - code_generation (delegate to Codex)
  - repository_operations (delegate to GitHub)
  - probabilistic_generation (incompatible)

requires_careful_handling:
  - sensitive_data (minimize handling)
  - large_datasets (performance impact)
  - complex_formulas (verify correctness)
```

## Routing Priority

```yaml
document_creation: high          # Primary use case
data_validation: high            # Core capability
excel_processing: high           # Well-integrated

template_generation: medium      # With specification
data_transformation: medium      # Pre-validated

reasoning: low                   # Not designed for
code_generation: low             # Use Codex
```

## Integration Rules

### 1. Contract Structure
```python
{
  "environment": "m365",
  "task_type": "document_generation|data_processing",
  "document_spec": {
    "type": "word|excel|powerpoint",
    "template": "template_path",
    "schema": "validation_schema",
    "structure": {
      "sections": ["section_specs"],
      "tables": ["table_specs"],
      "formatting": "formatting_rules"
    }
  },
  "data_input": {
    "source": "data_source",
    "format": "csv|json|excel",
    "validation_rules": ["rule1", "rule2"]
  },
  "output": {
    "format": "docx|xlsx|pptx",
    "path": "output_path",
    "schema_compliance": true
  }
}
```

### 2. Strict Document Execution

#### Validation Layers
```
1. Input Validation
   - Schema compliance check
   - Data type verification
   - Required fields check
   - Format validation

2. Processing Validation
   - Formula correctness
   - Calculation verification
   - Reference validation
   - Constraint checking

3. Output Validation
   - Structure validation
   - Schema compliance check
   - Rendering correctness
   - Content verification
```

#### Error Handling
- Validation failures block output
- Detailed error reporting
- Rollback on failure
- Recovery procedures

### 3. Workflow Patterns

#### Pattern 1: Architecture → Documentation
```
ChatGPT (architecture design)
  → Data Capture (structured data)
  → M365 (document generation)
  → GitHub (store in repo)
```

#### Pattern 2: Excel Data Processing
```
Data Source (raw data)
  → M365 Excel (validation & transformation)
  → M365 Word (report generation)
  → GitHub (archive)
```

#### Pattern 3: Compliance Document Generation
```
Requirement Definition
  → M365 Excel (data organization)
  → M365 Word (document generation)
  → Validation (schema check)
  → Distribution
```

### 4. Excel Ingestion

#### Data Ingestion Process
1. **Source Definition**: Specify Excel location and sheets
2. **Schema Validation**: Validate against defined schema
3. **Data Transformation**: Apply transformation rules
4. **Quality Checks**: Validate transformed data
5. **Integration**: Make available to other systems

#### Validation Rules
```yaml
data_types:
  - field_name: type_constraint
  - values: min-max ranges
  - format: regex patterns

integrity:
  - uniqueness: [column_list]
  - referential: foreign_keys
  - custom: validation_rules

completeness:
  - required_fields: [field_list]
  - null_policy: allow|reject
```

### 5. Template Management

#### Template Structure
```
templates/
├── word/
│   ├── architecture_document.docx
│   ├── requirements_spec.docx
│   └── report_template.docx
├── excel/
│   ├── data_collection.xlsx
│   ├── validation_template.xlsx
│   └── report_template.xlsx
└── schemas/
    ├── document_schema.json
    ├── data_schema.json
    └── validation_rules.json
```

## Performance Characteristics

```yaml
latency:
  simple_document: 2-5 seconds
  complex_document: 10-30 seconds
  excel_processing: 5-60 seconds (depends on data volume)
  validation: 1-5 seconds

throughput:
  documents_per_batch: 1-100
  rows_per_excel: up to 1M (practical: 100k)
  tokens_per_document: varies

reliability:
  document_correctness: 99%+
  schema_compliance: 100%
  data_integrity: 100%
```

## Best Practices

### 1. Template Design
- Clear structure with named sections
- Placeholder naming conventions
- Consistent formatting
- Reusable components

### 2. Data Validation
- Strict schema enforcement
- Multi-layer validation
- Clear error messages
- Audit trail maintenance

### 3. Document Generation
- Validate data before generation
- Test with sample data
- Verify output structure
- Archive generated documents

### 4. Excel Integration
- Define schemas clearly
- Validate data quality
- Document transformation rules
- Test with various datasets

## Related Files

- See `../ENVIRONMENT_INTEGRATION_ARCHITECTURE.md` for system design
- See `strict_document_execution.md` for detailed validation rules
- See `excel_ingestion.md` for data processing details
- See `../schemas/` for schema definitions
- See `../orchestration/` for workflow patterns

**Last Updated:** 2026-05-14