---
id: D001
title: Self-hosted n8n + exported template in repo
status: decided
date: 2026-11-06
features: [F02, F04, F06]
supersedes: null
superseded_by: null
---

# D001: Self-hosted n8n + exported template

## Context
Where the n8n workflow lives and how it stays reusable. Full option list in [research.md](../research.md#hosting-options).

## Options

| Option | Pro | Con |
|---|---|---|
| A: template only (JSON + README) | no maintenance, no cost | does nothing by itself |
| B: self-host on VPS | always on; webhooks; room for sandbox | updates, backup, security on us |
| C: n8n Cloud | no maintenance | paid; no place for sandbox |
| **D: B + A** | live flow + reusable template | bit more work than B |

## Decision
D. Only self-hosting allows phase 3 (sandbox); template keeps it reusable.

## Consequences
We operate the server (F04). Workflow must be exported after changes (F06).
