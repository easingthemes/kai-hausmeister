---
id: F04
title: n8n live behind HTTPS, owner account
status: in-progress
phase: 0
depends_on: [F02]
decisions: [D003]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F04: n8n live

## Goal
n8n running on the VPS, owner account created, basic ops known.

## Tasks
- [ ] start stack, create owner account (strong password)
- [ ] backup plan for n8n volume + `N8N_ENCRYPTION_KEY`
- [ ] update procedure (pull image, restart) written down

## Acceptance
- UI reachable over HTTPS, test webhook workflow receives a request.

## Notes
- 2026-11-06: stack running and reachable over HTTPS (F02). Owner account next. Ops workflow has backup/restart/logs actions.
