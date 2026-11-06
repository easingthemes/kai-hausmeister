---
id: F03
title: Webhook + fine-grained token in target repo
status: todo
phase: 0
depends_on: [F04]
decisions: [D005, D006]
questions: [Q1]
created: 2026-11-06
updated: 2026-11-06
---

# F03: GitHub access

## Goal
Target repo (dx-aem-flow) sends `issues` events to n8n; n8n can read code and comment.

## Tasks
- [ ] fine-grained token: only target repo, `Issues: Read and write`, `Contents: Read-only` (Metadata read is automatic)
- [ ] n8n credential "GitHub API" with that token
- [ ] webhook secret: `openssl rand -hex 32`, kept in password manager + n8n
- [ ] webhook in target repo: URL `https://<n8n host>/webhook/github-issues`, content type `application/json`, secret, only event `Issues`
- [ ] add webhook only after F05 guards exist (D009); until the workflow is published, deliveries return 404 (expected)

## Acceptance
- Test issue → delivery shows 2xx in GitHub webhook log.

## Notes
- 2026-11-06: Q1 answered: anyone can open issues → D009 (automatic triage with hard limits).
