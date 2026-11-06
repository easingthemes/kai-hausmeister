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
- [ ] webhook in target repo: URL `https://n8n.<domain>/webhook/...`, content type JSON, secret, event `Issues`
- [ ] fine-grained token: only target repo, `Issues: write`, `Contents: read`
- [ ] store secret + token as n8n credentials (never in repo)

## Acceptance
- Test issue → delivery shows 2xx in GitHub webhook log.

## Notes
