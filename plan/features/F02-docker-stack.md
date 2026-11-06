---
id: F02
title: "Docker stack: compose, Caddy, .env.example, DNS"
status: blocked
phase: 0
depends_on: [F01, D007]
decisions: [D003, D007, D008]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F02: Docker stack

## Goal
`docker/` folder in this repo that starts n8n (+ DB if Postgres) and is reachable as `https://n8n.<domain>` via existing Caddy.

## Tasks
- [ ] `docker/docker-compose.yml` (n8n, optional Postgres, volumes, restart policy)
- [ ] `docker/n8n.caddy` site file for `n8n.<domain>`
- [ ] main Caddyfile gets an `import` of a sites folder; ops workflow deploys `n8n.caddy` there
- [ ] `docker/.env.example` (names only, no values)
- [ ] DNS A record `n8n.<domain>`

## Acceptance
- `docker compose up -d` on server works, n8n UI loads over HTTPS.

## Notes
- 2026-11-06: main Caddyfile is managed and overwritten by another project's deploy. n8n block must live in a separate imported file, else next deploy deletes it.
- 2026-11-06: blocked until D007 (DB choice) and F01 (server check).
