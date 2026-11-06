# kai-hausmeister

n8n integration that triages GitHub issues with an AI agent. A new issue comes in, the agent reads it and the relevant code, and posts a comment (type, affected area, next steps). Later phases add labels, duplicate detection, and an automated fix in a sandbox that opens a PR.

First target repo: [dx-aem-flow](https://github.com/easingthemes/dx-aem-flow).

The n8n workflow is self-hosted and also exported to this repo as a reusable template.

## Status
Planning. Nothing deployed yet. See [plan/INDEX.md](plan/INDEX.md).

## Docs
- [plan/INDEX.md](plan/INDEX.md): features, decisions, questions, status
- [docs/architecture.md](docs/architecture.md): how it connects, flow phases, security

## Layout
```
docker/      docker-compose.yml, n8n.caddy, .env.example
workflows/   exported n8n workflow JSON (template)
plan/        index, features, decisions, research, questions, log
docs/        architecture
```
