---
id: F04
title: n8n live behind HTTPS, owner account
status: done
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
- [x] backup plan: weekly ops workflow (Sunday 03:17 UTC) makes a backup on the server (keeps 7) and copies it off-server as an encrypted artifact (30 days); restore steps in the private ops repo; `N8N_ENCRYPTION_KEY` in password manager
- [x] update procedure written down: ops workflow "Deploy n8n" with new pinned version; rollback = same workflow with previous version (see `docker/README.md`). Take a backup first.

## Acceptance
- UI reachable over HTTPS, test webhook workflow receives a request.

## Notes
- 2026-11-06: **done.** Off-server backup workflow added; first manual run OK, artifact present. Schedule changed to weekly.
- 2026-11-06: first backup OK via ops workflow (~0.5 MB, n8n stops a few seconds). Open: off-server copy of backups.
- 2026-11-06: owner account created.
- 2026-11-06: stack running and reachable over HTTPS (F02). Owner account next. Ops workflow has backup/restart/logs actions.
