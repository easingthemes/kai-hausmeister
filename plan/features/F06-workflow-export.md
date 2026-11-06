---
id: F06
title: Export workflow JSON + setup docs
status: done
phase: 1
depends_on: [F05]
decisions: [D001]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F06: Workflow export

## Goal
Workflow is reusable: JSON in `workflows/` + README how to import and configure.

## Tasks
- [x] export from the live instance (ops action `export-workflows`, secret redacted before printing)
- [x] compared with `workflows/triage.json`: same nodes, parameters and code; only instance data differs
- [x] `workflows/sanitize.py` strips instance data and refuses secrets, hex keys and emails
- [x] README: import steps, credentials, webhook setup, export procedure

## Acceptance
- Fresh n8n instance can import and run it by following README.

## Notes
- 2026-11-06: **done.** Live workflow matches the repo template. A raw export contains the owner's name and email (project data); `sanitize.py` removes it.
