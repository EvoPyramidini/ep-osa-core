# Gemini Environment

**Multimodal analysis and visual reasoning.**

Gemini serves as the multimodal analysis engine for ep-osa-core.

## Capabilities

### Core Capabilities
- Image understanding and analysis
- Multimodal reasoning (text + images)
- Document image processing
- Visual pattern recognition
- Diagram interpretation
- Media analysis
- Context-aware multimodal synthesis

### Advanced Features
- Complex image reasoning
- Multi-page document analysis
- Diagram structure extraction
- Visual relationship extraction
- Media content analysis

## Limitations

### Inherent Constraints
- Probabilistic interpretation (not deterministic)
- Context window limits
- Non-deterministic outputs
- File format constraints
- Size limitations for media

### Task Constraints
- Cannot execute code (delegate to Codex/local)
- Cannot generate structured documents deterministically
- Cannot replace ChatGPT for pure text reasoning
- Cannot perform high-precision OCR

## Preferred Tasks

```yaml
high_priority:
  - image_understanding
  - document_image_analysis
  - diagram_interpretation
  - visual_pattern_recognition
  - multimodal_reasoning

medium_priority:
  - media_content_analysis
  - visual_documentation
  - screenshot_analysis
  - chart_interpretation

low_priority:
  - pure_text_reasoning (use ChatGPT)
  - code_generation (use Codex)
  - data_processing (use M365/local)
```

## Restricted Tasks

```yaml
should_not:
  - pure_semantic_reasoning (use ChatGPT)
  - code_generation (use Codex)
  - document_creation (use M365)
  - repository_management (use GitHub)

requires_verification:
  - sensitive_content_analysis
  - medical_imagery_interpretation
  - face_recognition_analysis
  - personally_identifiable_information
```

## Routing Priority

```yaml
image_analysis: high             # Primary use case
multimodal_reasoning: high       # Core capability
document_processing: high        # Well-supported

media_analysis: medium           # With specification
visual_understanding: medium     # Contextual

pure_text_reasoning: low         # Use ChatGPT
code_generation: low             # Use Codex
```

## Integration Rules

### 1. Contract Structure
```python
{
  "environment": "gemini",
  "task_type": "image_analysis|multimodal_reasoning",
  "input": {
    "media": {
      "type": "image|video|document",
      "format": "png|jpg|pdf|etc",
      "path_or_url": "location",
      "size_bytes": size_limit
    },
    "text_context": "additional context",
    "reasoning_type": "analysis|extraction|interpretation"
  },
  "expected_output": {
    "type": "description|structured_data|reasoning",
    "format": "natural_language|json|markdown",
    "confidence_level": "required_confidence"
  }
}
```

### 2. Multimodal Workflow Patterns

#### Pattern 1: Screenshot Analysis → Documentation
```
System Screenshot (captured)
  → Gemini (visual analysis)
  → ChatGPT (semantic interpretation)
  → M365 (documentation)
  → GitHub (storage)
```

#### Pattern 2: Document Processing
```
Document Image (PDF/image)
  → Gemini (page analysis)
  → OCR/extraction (data)
  → M365 (structured document)
  → GitHub (archive)
```

#### Pattern 3: Architecture Diagram Analysis
```
Architecture Diagram (image)
  → Gemini (structure extraction)
  → ChatGPT (interpretation)
  → Codex (implementation)
  → GitHub (code)
```

### 3. Media Processing

#### Image Analysis
- Format support: PNG, JPG, GIF, WebP
- Size limits: Up to 20MB per image
- Resolution: Optimal 1024x768+
- Color: RGB, grayscale, indexed

#### Video Analysis
- Format support: MP4, WebM, MOV
- Duration limits: Up to 25 minutes
- Frame rate: Standard video rates
- Codec support: H.264, VP8, VP9

#### Document Analysis
- Format support: PDF, images of documents
- Page limit: Up to 1000 pages
- Text density: Optimal for structured documents
- Languages: Multilingual support

### 4. Context Handling

#### Providing Context
```yaml
visual_context:
  - What is visible in the media
  - What should be analyzed
  - Any relevant background

semantics:
  - Purpose of analysis
  - Expected output format
  - Confidence requirements
  - Special considerations
```

#### Result Validation
- Semantic consistency check
- Format compliance check
- Confidence level assessment
- Cross-reference when possible

## Performance Characteristics

```yaml
latency:
  image_analysis: 3-10 seconds
  document_analysis: 10-30 seconds
  video_analysis: 30-120 seconds
  complex_reasoning: 5-15 seconds

throughput:
  concurrent_requests: 10+
  batch_size: 1 per request
  tokens_per_image: 2-50k
  requests_per_minute: 60+

reliability:
  analysis_consistency: 85-95%
  format_compliance: 90%+
  semantic_coherence: high
```

## Best Practices

### 1. Image Preparation
- Clear, well-lit images
- Readable text and diagrams
- Relevant framing
- Multiple angles if needed

### 2. Context Provision
- Clear analysis requests
- Relevant background information
- Expected output format
- Specific focus areas

### 3. Result Handling
- Validate analysis results
- Cross-check with other sources
- Document confidence levels
- Archive results with source media

### 4. Integration
- Use Memory layer for context
- Leverage Orchestration for workflows
- Implement validation at boundaries
- Trace all operations

## Related Files

- See `../ENVIRONMENT_INTEGRATION_ARCHITECTURE.md` for system design
- See `multimodal_workflows.md` for workflow examples
- See `context_handling.md` for detailed context guidance
- See `../orchestration/` for orchestration patterns
- See `../memory/` for context management

**Last Updated:** 2026-05-14