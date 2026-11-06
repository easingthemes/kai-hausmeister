---
id: F02
title: "Docker stack: compose, Caddy, .env.example, DNS"
status: in-progress
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
- [ ] server prep (private ops repo, root once): swap, Docker, Caddy sites folder
- [ ] main Caddyfile gets an `import` of the sites folder (in the project that owns it)
- [ ] DNS A record `n8n.<domain>`
- [ ] ops workflow: copy files, write `.env` from secrets, `docker compose up -d`, deploy Caddy site

## Acceptance
- `docker compose up -d` on server works, n8n UI loads over HTTPS.

## Notes
- 2026-11-06: main Caddyfile is managed and overwritten by another project's deploy. n8n block must live in a separate imported file, else next deploy deletes it.
- 2026-11-06: unblocked: D003 Docker and D007 SQLite decided. Compose files written.
