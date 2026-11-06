---
id: D004
title: Phases 1–2 on existing small VPS
status: decided
date: 2026-11-06
features: [F01, F08]
supersedes: null
superseded_by: null
---

# D004: Existing VPS for phases 1–2

## Context
Where to run n8n.

## Options

| Option | Pro | Con |
|---|---|---|
| **Existing small VPS** | no extra cost; Caddy already there | shared resources with other apps |
| New VPS | isolated | extra cost and setup |

## Decision
Existing VPS for phases 1–2.

## Consequences
Revisit before phase 3: sandbox runs untrusted code → separate server (F08). Depends on F01 results.
