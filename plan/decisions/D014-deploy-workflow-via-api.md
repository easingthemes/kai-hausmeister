---
id: D014
title: Deploy workflows from the repo via the n8n public API
status: decided
date: 2026-11-06
features: [F06, F07]
supersedes: null
superseded_by: null
---

# D014: Repo → n8n via public API

## Context
`workflows/*.json` in this repo should be the source of truth. Until now every change meant a manual import in n8n: unpublish the old workflow, import, select credentials, paste the secret, publish. Research 2026-11-06 (n8n docs): see options.

## Options

| Option | Pro | Con |
|---|---|---|
| n8n Source control & environments (Git pull, `autoPublish`) | official n8n way, built for CI/CD | paid plans only (Business/Enterprise) |
| **Public REST API: `PUT /api/v1/workflows/{id}` + publish** | available in all self-hosted editions; updates the running instance, no restart; same workflow id, webhook URL unchanged | needs an n8n API key; we map credential ids and inject the secret ourselves |
| CLI `n8n import:workflow` in the container | no API key | writes to the DB behind n8n's back; imported workflows come in unpublished; documented bug keeps old triggers running until restart → restart needed, webhooks lost meanwhile |
| Manual import in the UI | nothing to build | many manual steps per change, error-prone |

## Decision
Public REST API, called from the server itself (`localhost:5678`) by an ops workflow in the private repo ("Deploy workflow"). Caddy blocks `/api/*` from outside, so the API key is only usable on the server.

## Consequences
- Change flow: edit in repo → PR → merge → run "Deploy workflow".
- Secrets: `N8N_API_KEY` and `N8N_WEBHOOK_SECRET` in the private repo's GitHub secrets. The webhook secret is injected at deploy time; D012 still applies inside n8n (the deployed Code node contains it).
- Credential ids of the instance live in the private ops repo, not here.
- Edits made directly in the n8n UI are overwritten by the next deploy: change the repo instead, or export first (F06).
