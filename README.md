# kai-hausmeister

n8n integration that triages GitHub issues with an AI agent. A new issue comes in, the agent reads it, browses the relevant code and searches existing issues, then posts one comment (type, affected area, possible duplicates, next steps) and sets whitelisted labels. A later phase adds an automated fix in a sandbox that opens a PR.

First target repo: [dx-aem-flow](https://github.com/easingthemes/dx-aem-flow).

The n8n workflow is self-hosted and also exported to this repo as a reusable template ([D001](plan/decisions/D001-self-host-plus-template.md)). The repo is the source of truth: merged changes are deployed to n8n via its API ([D014](plan/decisions/D014-deploy-workflow-via-api.md)).

## Status
**Phases 1 and 2 live** (2026-11-06).

| Phase | What | Status |
|---|---|---|
| 0 | Server, Docker stack, HTTPS, GitHub webhook + token, backups | done |
| 1 | Webhook → AI agent (Claude Haiku, read-only tools) → triage comment | done |
| 2 | Whitelisted labels + duplicate search (open + closed issues) | done |
| 3 | Sandboxed fix → PR, only on maintainer label | todo |

Limits: every issue is triaged, max 20 runs/day, max 3 issues per author/day, cost cap $1/day ([D009](plan/decisions/D009-triage-all-issues.md)). Measured cost ~$0.01 per triage.

Details and next steps: [plan/INDEX.md](plan/INDEX.md).

## How it works
```
issue opened → GitHub webhook → n8n: verify signature → guards → triage agent → comment + labels
```
Node by node: [workflows/README.md](workflows/README.md). Big picture and security: [docs/architecture.md](docs/architecture.md).

## Docs
- [plan/INDEX.md](plan/INDEX.md): features, decisions, questions, risks, status
- [docs/architecture.md](docs/architecture.md): how it connects, flow phases, security
- [workflows/README.md](workflows/README.md): triage workflow, setup, deploy, export
- [docker/README.md](docker/README.md): run, update, backup n8n

## Layout
```
docker/      docker-compose.yml, n8n.caddy, .env.example
workflows/   exported n8n workflow JSON (template) + sanitize.py
plan/        index, features, decisions, research, questions, risks, log
docs/        architecture
```

Server specifics and ops (deploy, backup, export actions) live in a private ops repo ([D008](plan/decisions/D008-ops-via-private-actions.md)).
