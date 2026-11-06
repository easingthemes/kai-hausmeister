---
id: F06
title: Export workflow JSON + setup docs
status: todo
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
- [ ] export workflow to `workflows/triage.json` (check no credentials inside)
- [ ] README: import steps, needed credentials, webhook setup

## Acceptance
- Fresh n8n instance can import and run it by following README.

## Notes
