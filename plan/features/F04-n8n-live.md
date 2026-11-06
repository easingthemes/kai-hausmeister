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
- [x] start stack, create owner account (strong password)
- [ ] backup plan for n8n volume + `N8N_ENCRYPTION_KEY`: ops workflow action `backup` (keeps last 7 on server); key in password manager. Open: off-server copy
- [x] update procedure written down: ops workflow "Deploy n8n" with new pinned version; rollback = same workflow with previous version (see `docker/README.md`). Take a backup first.

## Acceptance
- UI reachable over HTTPS, test webhook workflow receives a request.

## Notes
- 2026-11-06: owner account created.
- 2026-11-06: stack running and reachable over HTTPS (F02). Owner account next. Ops workflow has backup/restart/logs actions.
