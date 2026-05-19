# Claude Connectors

MCP (Model Context Protocol) integration surfaces available to Claude
within the EP-OSA-core execution environment.

---

## Active Connectors

### Gmail
**URL:** `https://gmailmcp.googleapis.com/mcp/v1`  
**Status:** Connected

**Capabilities:**
- Read and search email threads
- Compose and send emails
- List labels and filters
- Attach files from Drive

**EP-OSA routing use cases:**
```yaml
high: email_notification_on_workflow_completion
high: send_architecture_documents_to_stakeholders
medium: search_project_related_communications
medium: archive_session_results_via_email
```

**Contract example:**
```python
{
  "environment": "claude",
  "connector": "gmail",
  "action": "search_and_summarize",
  "query": "ep-osa architecture decisions",
  "output": "email_thread_summary"
}
```

---

### Google Calendar
**URL:** `https://calendarmcp.googleapis.com/mcp/v1`  
**Status:** Connected

**Capabilities:**
- Read events and schedules
- Create and update events
- Check availability
- List calendars

**EP-OSA routing use cases:**
```yaml
high: schedule_architecture_review_sessions
high: track_evolution_phase_milestones
medium: check_availability_for_collaboration
medium: create_reminders_for_research_tasks
```

**Contract example:**
```python
{
  "environment": "claude",
  "connector": "google_calendar",
  "action": "create_milestone_event",
  "payload": {
    "title": "EP-OSA Layer 5 Skills - Implementation Review",
    "date": "target_date",
    "description": "ADR reference + checklist"
  }
}
```

---

### Google Drive
**URL:** `https://drivemcp.googleapis.com/mcp/v1`  
**Status:** Connected

**Capabilities:**
- List and search files/folders
- Read file content (Docs, Sheets, PDFs, etc.)
- Create and upload files
- Copy files
- Fetch file metadata and permissions

**EP-OSA routing use cases:**
```yaml
high: store_approved_patterns_and_adr_documents
high: read_reference_architecture_docs
high: sync_generated_artifacts_to_drive
medium: share_evolution_brainstorms_with_collaborators
medium: retrieve_historical_session_outputs
```

**Contract example:**
```python
{
  "environment": "claude",
  "connector": "google_drive",
  "action": "upload_artifact",
  "payload": {
    "name": "ep-osa-adr-004.md",
    "folder": "ep-osa-core/adr/",
    "content": "file_content"
  }
}
```

---

## Planned / Future Connectors

These connectors are not yet active but are relevant to EP-OSA-core evolution:

| Connector | Purpose | Priority |
|-----------|---------|----------|
| GitHub | Repository governance, ADR commits, PR workflows | High |
| Notion | Architecture wiki, knowledge base | Medium |
| Slack | Team notifications, async coordination | Medium |
| Linear/Jira | Issue tracking for evolution tasks | Low |

---

## Connector Governance Rules

1. **All connector calls route through Claude's contract layer** — no raw API calls
2. **Sensitive data minimized** — only necessary fields passed to connectors
3. **All connector interactions traced** — logged as part of session trace
4. **MCP server URLs treated as trusted** — but outputs validated against schemas
5. **User must grant connector access** — Claude never self-authorizes new connectors

---

## Connector Error Handling

```yaml
gmail_unavailable:
  fallback: file_output + notify_user
  retry: once_after_5s

calendar_unavailable:
  fallback: store_event_spec_in_artifact_storage
  retry: once_after_5s

drive_unavailable:
  fallback: local_file_output_for_download
  retry: once_after_5s
```

---

**Last Updated:** 2026-05-18
**Version:** 1.0-alpha
