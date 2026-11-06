# Research

Facts, options and links. No decisions here: decisions go to `decisions/` and link back to a section.
Each section: date, source, short finding. Add new topics under "To research".

## Hosting options
*2026-11-06.* Used by [D001](decisions/D001-self-host-plus-template.md).

| Option | Pro | Con |
|---|---|---|
| Template only (workflow JSON + README) | no maintenance, no cost | does nothing by itself |
| Self-host on VPS (Docker Compose: n8n + DB + Caddy) | always on; receives webhooks; room for sandbox | updates, backup, security on us |
| n8n Cloud | no maintenance | paid plan; no place for sandbox |
| Self-host + template | live flow + reusable template | slightly more work |

n8n Community edition is free for own use; license forbids offering n8n as a service to others.

## Where n8n can run
*2026-11-06.* n8n is a long-running server (UI, webhook URL, run history, credentials).
- Self-host (VPS, Docker; at scale: Postgres + Redis + workers in queue mode, or Kubernetes).
- n8n Cloud (priced per plan and executions).
- Managed third-party hosting (Railway, Render, Elestio etc.).
- Local + tunnel (ngrok/cloudflared): development only.
- GitHub Actions is not hosting for n8n: no UI, no stable webhook, no history. A plain GH Action (issue opened → LLM) is an alternative to n8n, not a place to run it. Out of scope.

## To research
- [ ] n8n RAM usage idle / under load with SQLite vs Postgres (input for [D007](decisions/D007-database.md))
- [ ] n8n execution data pruning settings (SQLite growth)
- [ ] LLM cost per triaged issue (tokens per run) → budget limit for F05
- [ ] Duplicate detection: GitHub search API vs embeddings (F07)
- [ ] Sandbox isolation options for phase 3: Docker network rules, gVisor, Firecracker (F08)
