---
id: D007
title: SQLite or Postgres
status: open
date:
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
Open, **recommendation: SQLite** + execution data pruning. F01: RAM would fit Postgres too, but single user + few runs per day don't need it. Revisit if queue mode is needed.

## Consequences
Postgres → extra service in compose and backup job.
