---
id: D007
title: SQLite or Postgres
status: decided
date: 2026-11-06
features: [F02]
supersedes: null
superseded_by: null
---

# D007: SQLite or Postgres

## Context
n8n stores workflows, credentials and run history in a DB. Blocks F02.

## Options

| Option | Pro | Con |
|---|---|---|
| SQLite (default) | no extra container; lighter on small VPS; backup = copy volume | not for queue mode / scaling; DB file grows with run history (needs pruning) |
| Postgres | production setup; needed for queue mode later | extra container + RAM; more to back up and update |

## Decision
**SQLite**, because of the project scope: one user, a few issues per day, one n8n instance. Postgres would fit in RAM (F01), but its extra service, backup and updates are not worth it at this size. Execution data pruning is on to keep the DB file small.

## Consequences
- Backup = n8n volume + `N8N_ENCRYPTION_KEY`.
- Revisit (new decision, `supersedes: D007`) if we need queue mode, several instances, or many repos with high issue volume.
