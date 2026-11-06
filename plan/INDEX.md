# Plan index

Single entry point for status. Read this first, then open only the files you need.
Feature and decision tables are generated from the YAML headers by `python3 plan/check.py --write`. Do not edit them by hand (rules: [CLAUDE.md](../CLAUDE.md)).

**Phase:** planning · **Last updated:** 2026-11-06

## Next up
1. [F04](features/F04-n8n-live.md): owner account, first backup, write down update procedure.
2. [F03](features/F03-github-access.md): webhook + fine-grained token in target repo.

## Features

<!-- gen:features -->
| ID | Feature | Phase | Status | Depends on |
|---|---|---|---|---|
| [F01](features/F01-server-check.md) | Check server (RAM, Docker) | 0 setup | done | – |
| [F02](features/F02-docker-stack.md) | Docker stack: compose, Caddy, .env.example, DNS | 0 setup | done | F01, D007 |
| [F03](features/F03-github-access.md) | Webhook + fine-grained token in target repo | 0 setup | todo | F04 |
| [F04](features/F04-n8n-live.md) | n8n live behind HTTPS, owner account | 0 setup | in-progress | F02 |
| [F05](features/F05-triage-comment.md) | Phase 1: webhook → AI agent → comment | 1 | todo | F03, F04 |
| [F06](features/F06-workflow-export.md) | Export workflow JSON + setup docs | 1 | todo | F05 |
| [F07](features/F07-labels-duplicates.md) | Phase 2: labels + duplicate detection | 2 | todo | F05 |
| [F08](features/F08-sandbox-fix.md) | Phase 3: sandboxed fix → PR | 3 | todo | F07 |
| [F09](features/F09-n8n-cloud-compare.md) | Run on n8n Cloud, compare | later | todo | F06 |
<!-- /gen:features -->

Status values: `todo` · `in-progress` · `blocked` · `done` · `dropped`

## Decisions

<!-- gen:decisions -->
| ID | Decision | Status | Date |
|---|---|---|---|
| [D001](decisions/D001-self-host-plus-template.md) | Self-hosted n8n + exported template in repo | decided | 2026-11-06 |
| [D002](decisions/D002-self-host-first.md) | Self-host first, n8n Cloud evaluated later | decided | 2026-11-06 |
| [D003](decisions/D003-docker-compose.md) | Docker Compose instead of npx n8n | decided | 2026-11-06 |
| [D004](decisions/D004-existing-vps.md) | Phases 1–2 on existing small VPS | decided | 2026-11-06 |
| [D005](decisions/D005-separate-repo.md) | Separate repo, target via webhook + GitHub API | decided | 2026-11-06 |
| [D006](decisions/D006-webhook-node.md) | Webhook node + manual webhook (not GitHub Trigger node) | decided | 2026-11-06 |
| [D007](decisions/D007-database.md) | SQLite or Postgres | decided | 2026-11-06 |
| [D008](decisions/D008-ops-via-private-actions.md) | Server ops via GitHub Actions in a private repo | decided | 2026-11-06 |
<!-- /gen:decisions -->

Status values: `open` · `proposed` · `decided` · `superseded`

## Open questions
See [questions.md](questions.md). Open now: Q1.

## Risks
See [risks.md](risks.md). Top open: R1 (prompt injection), R2 (LLM cost).

## Other files
- [research.md](research.md): findings, options compared, links. Facts only, no decisions.
- [questions.md](questions.md): open and answered questions.
- [risks.md](risks.md): risks with likelihood, impact, mitigation.
- [log.md](log.md): what changed when (one line per change).
- [check.py](check.py): validates headers and references, regenerates tables. Runs in CI.
- [_templates/](_templates/): templates for new feature and decision files.
- [../docs/architecture.md](../docs/architecture.md): current target architecture and security.
