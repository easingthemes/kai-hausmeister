# kai-hausmeister

n8n integration that triages GitHub issues with an AI agent. A new issue comes in, the agent reads it and the relevant code, and posts a comment (type, affected area, next steps). Later phases add labels, duplicate detection, and an automated fix in a sandbox that opens a PR.

First target repo: [dx-aem-flow](https://github.com/easingthemes/dx-aem-flow).

The n8n workflow is self-hosted and also exported to this repo as a reusable template.

## Status
Planning. Nothing deployed yet. See [docs/roadmap.md](docs/roadmap.md).

## Docs
- [docs/architecture.md](docs/architecture.md): hosting, flow phases, security
- [docs/decisions.md](docs/decisions.md): decision log
- [docs/roadmap.md](docs/roadmap.md): steps and open questions

## Layout (planned)
```
docker/      docker-compose.yml, Caddy snippet, .env.example
workflows/   exported n8n workflow JSON (template)
docs/        architecture, decisions, roadmap
```
