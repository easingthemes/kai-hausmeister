---
id: D003
title: Docker Compose instead of npx n8n
status: proposed
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
| **Docker Compose** | easy update/rollback (image tag); DB in same file; Docker needed for phase 3 anyway | Docker overhead; needs Docker on server |
| npm global + process manager | same pattern as other apps on the server; no Docker daemon; less RAM | runs as the same system user as other apps → n8n (Code node, prompt injection) can read their files and secrets; harder rollback |

## Decision
Proposed: Docker Compose. F01 (2026-11-06): Docker is **not** installed, so this needs a one-time root install. Main reason to keep Docker: isolation from other apps on the shared server (see R10). Waiting for confirmation.

## Consequences
`docker/` folder in repo (F02). Docker install needs root once. Deploy user in `docker` group = root-equivalent (R9 gets heavier).
