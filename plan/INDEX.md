# Plan index

Single entry point for status. Read this first, then open only the files you need.
Feature and decision tables are generated from the YAML headers by `python3 plan/check.py --write`. Do not edit them by hand (rules: [CLAUDE.md](../CLAUDE.md)).

**Phase:** phase 2 live · **Last updated:** 2026-11-06

## Next up
1. Watch real issues (quality, labels, cost).
2. [F08](features/F08-sandbox-fix.md): phase 3 planning (separate sandbox server).

## Features

<!-- gen:features -->
| ID | Feature | Phase | Status | Depends on |
|---|---|---|---|---|
| [F01](features/F01-server-check.md) | Check server (RAM, Docker) | 0 setup | done | – |
| [F02](features/F02-docker-stack.md) | Docker stack: compose, Caddy, .env.example, DNS | 0 setup | done | F01, D007 |
| [F03](features/F03-github-access.md) | Webhook + fine-grained token in target repo | 0 setup | done | F02 |
| [F04](features/F04-n8n-live.md) | n8n live behind HTTPS, owner account | 0 setup | done | F02 |
| [F05](features/F05-triage-comment.md) | Phase 1: webhook → AI agent → comment | 1 | done | F03, F04 |
| [F06](features/F06-workflow-export.md) | Export workflow JSON + setup docs | 1 | done | F05 |
| [F07](features/F07-labels-duplicates.md) | Phase 2: labels + duplicate detection | 2 | done | F05 |
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
| [D009](decisions/D009-triage-all-issues.md) | Triage every new issue automatically, with hard limits | decided | 2026-11-06 |
| [D010](decisions/D010-fixed-pipeline.md) | Fixed two-call pipeline instead of AI Agent node (phase 1) | superseded | 2026-11-06 |
| [D011](decisions/D011-ai-agent-node.md) | AI Agent node with GitHub tools for triage (phase 1) | decided | 2026-11-06 |
| [D012](decisions/D012-webhook-secret-in-workflow.md) | Webhook secret stays in the Code node config | decided | 2026-11-06 |
| [D013](decisions/D013-labels-and-duplicates.md) | Agent sets whitelisted labels and links possible duplicates | decided | 2026-11-06 |
| [D014](decisions/D014-deploy-workflow-via-api.md) | Deploy workflows from the repo via the n8n public API | decided | 2026-11-06 |
<!-- /gen:decisions -->

Status values: `open` · `proposed` · `decided` · `superseded`

## Open questions
See [questions.md](questions.md). No open questions.

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
