---
id: D003
title: Docker Compose instead of npx n8n
status: decided
date: 2026-11-06
features: [F02, F04]
supersedes: null
superseded_by: null
---

# D003: Docker Compose

## Context
How n8n is installed on the VPS.

## Options

| Option | Pro | Con |
|---|---|---|
| **Docker Compose** | isolation (own volume, no host paths); easy update/rollback (image tag); Docker needed for phase 3 anyway | Docker overhead; needs one-time root install |
| npm global + process manager | same pattern as other apps on the server; no Docker daemon; less RAM | runs as the same system user as other apps → n8n (Code node, prompt injection) can read their files and secrets; harder rollback |

## Decision
**Docker Compose** (confirmed 2026-11-06). Main reason: isolation from other apps on the shared server (R10). Docker is not installed yet (F01), so it needs a one-time root install.

## Consequences
`docker/` folder in repo (F02). Docker install needs root once. Deploy user in `docker` group = root-equivalent (R9 gets heavier).
