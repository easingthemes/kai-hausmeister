# Architecture

## Hosting options

| | Option | Pro | Con |
|---|---|---|---|
| A | Template only (workflow JSON + README) | no maintenance, no cost | does nothing by itself |
| B | Self-host on a VPS (Docker Compose: n8n + DB + Caddy for HTTPS) | always on; receives GitHub webhooks; room for a sandbox (phase 3) | updates, backup and security are on us |
| C | n8n Cloud | no maintenance | paid plan; no place for a sandbox |
| D | **B + A** | live flow on the VPS + exported template in repo | slightly more work than B |

**Chosen: D.** Only self-hosting allows phase 3; the exported template keeps the workflow reusable.
n8n Community edition is free for own use (the license forbids offering n8n as a service to others).

## Where n8n can run
n8n is a **long-running server** (UI, webhook URL, run history, credentials):
- **Self-host** (VPS, Docker; at scale: Postgres + Redis + workers in queue mode, or Kubernetes).
- **n8n Cloud** (priced per plan and executions).
- **Managed third-party hosting** (Railway, Render, Elestio etc.).
- **Local + tunnel** (ngrok/cloudflared): development only.
- **GitHub Actions is not hosting for n8n**: no UI, no stable webhook, no history. A plain GH Action (issue opened → LLM) is an alternative to n8n, not a place to run it. Out of scope here, since this project is an n8n integration.

## How it connects to the target repo
This repo holds only the setup (`docker/`, exported `workflows/`). The workflow itself runs in n8n on the server and talks to the target repo through the GitHub API. The target repo needs no code changes.

- **Trigger:** the target repo sends a webhook to `https://n8n.<domain>/webhook/...` on `issues: opened`.
  - **Chosen: n8n Webhook node.** Webhook is added once by hand in the target repo (Settings → Webhooks) with a secret; n8n verifies the signature. The token then needs no webhook permission.
  - Alternative: GitHub Trigger node, which creates the webhook itself, but the token needs permission to manage repo webhooks.
- **Reading code:** agent reads files via GitHub API (contents endpoint), no clone needed.
- **Comment / label:** fine-grained token, target repo only, `Issues: write`.
- **Phase 3 (fix):** container clones the target repo, creates a branch, opens a PR. Only then the token needs `Contents: write` and `Pull requests: write` (separate token).
- **More repos later:** add the webhook there and extend the token to that repo; same workflow.

## Server
- A small VPS.
- Caddy already in front (HTTPS). n8n goes behind it as `n8n.<domain>`: one DNS A record + a Caddyfile entry.
- Phases 1–2 run here. Phase 3 (sandbox running untrusted code) should get a separate small server.

## Flow (phases)
1. **Triage comment.** Webhook node (issues: opened, signature check) → AI Agent (Anthropic Chat Model, tool: read file from repo) → GitHub: create comment.
2. **Labels + duplicates.** Agent proposes a label and links similar open issues.
3. **Fix in sandbox.** Maintainer adds a label (e.g. `agent:fix`) → n8n starts Claude Code headless in a Docker container (network limited to GitHub/Anthropic) → PR.

## Security
- **Target repo is public: anyone can open an issue.** Issue text goes into the agent (prompt injection). Use a fine-grained token: comments only, one repo; no code write in phases 1–2.
- Phase 3 runs only on a label set by a maintainer, never automatically.
- Limit iterations and tokens per run; log cost per run.
- n8n behind HTTPS, strong owner password, regular image updates.
- Secrets only in server `.env` / n8n credentials, never in this repo.
