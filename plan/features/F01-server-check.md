---
id: F01
title: Check server (RAM, Docker)
status: done
phase: 0
depends_on: []
decisions: [D004, D008]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F01: Check server (RAM, Docker)

## Goal
Know if the existing VPS has enough room for n8n (+ DB) next to what already runs there.

## Tasks
- [x] set secrets + `production` environment in private ops repo (D008)
- [x] run **Server Status → `f01-server-check`** 
- [x] write results into Notes below

## Acceptance
- Free RAM and disk noted; Docker + Compose present (or install steps noted).

## Notes
- 2026-11-06: done. Full results in the private ops repo (`docs/server.md`). Conclusions:
  - enough RAM and disk for n8n next to the existing apps
  - Docker not installed (needs one-time root install, see D003)
  - no swap: add some before n8n as safety net
  - Caddy config has no `import` yet (see F02)
