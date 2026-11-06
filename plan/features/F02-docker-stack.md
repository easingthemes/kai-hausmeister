---
id: F02
title: "Docker stack: compose, Caddy, .env.example, DNS"
status: done
phase: 0
depends_on: [F01, D007]
decisions: [D003, D007, D008]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F02: Docker stack

## Goal
`docker/` folder in this repo that starts n8n (SQLite) and is reachable as `https://n8n.<domain>` via existing Caddy.

## Tasks
- [x] `docker/docker-compose.yml` (n8n, SQLite, named volume, port on localhost only, memory limit, log rotation, pruning)
- [x] `docker/n8n.caddy` site file
- [x] `docker/.env.example` (names only)
- [x] server prep (private ops repo, root once): swap, Docker, Caddy sites folder
- [x] main Caddyfile gets an `import` of the sites folder (in the project that owns it)
- [x] DNS A record for the n8n hostname
- [x] ops workflow: copy files, write `.env` from secrets, `docker compose up -d`, deploy Caddy site

## Acceptance
- `docker compose up -d` on server works, n8n UI loads over HTTPS.

## Notes
- 2026-11-06: **done.** First deploy via ops workflow; n8n healthy, reachable over HTTPS, other site on the server unaffected.
- 2026-11-06: main Caddyfile is managed and overwritten by another project's deploy. n8n block must live in a separate imported file, else next deploy deletes it.
- 2026-11-06: `import` line prepared on a branch in the project that owns the main Caddyfile; needs merge + deploy there. Ops repo only writes the n8n site file (one owner per file).
- 2026-11-06: server prep done (swap, Docker, Caddy sites folder); DNS record added. Details in private ops repo.
- 2026-11-06: unblocked: D003 Docker and D007 SQLite decided. Compose files written.
