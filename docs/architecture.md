# Architecture

Hosting choice: [D001](../plan/decisions/D001-self-host-plus-template.md). Options and where n8n can run: [plan/research.md](../plan/research.md).

## How it connects to the target repo
This repo holds only the setup (`docker/`, exported `workflows/`). The workflow itself runs in n8n on the server and talks to the target repo through the GitHub API. The target repo needs no code changes.

- **Trigger:** the target repo sends a webhook to `https://n8n.<domain>/webhook/...` on `issues: opened`.
  - **Chosen: n8n Webhook node.** Webhook is added once by hand in the target repo (Settings → Webhooks) with a secret; n8n verifies the signature. The token then needs no webhook permission.
  - Alternative: GitHub Trigger node, which creates the webhook itself, but the token needs permission to manage repo webhooks.
- **Reading code:** agent reads files via GitHub API (contents endpoint), no clone needed.
- **Duplicates:** agent searches open and closed issues via the GitHub search API.
- **Comment / label:** fine-grained token, target repo only, `Issues: write` + `Contents: read`.
- **Phase 3 (fix):** container clones the target repo, creates a branch, opens a PR. Only then the token needs `Contents: write` and `Pull requests: write` (separate token).
- **More repos later:** add the webhook there and extend the token to that repo; same workflow.

## Server
- A small VPS.
- Caddy already in front (HTTPS). n8n goes behind it as `n8n.<domain>`: one DNS A record + a site file imported by the main Caddyfile.
- n8n runs in Docker Compose with SQLite ([D003](../plan/decisions/D003-docker-compose.md), [D007](../plan/decisions/D007-database.md)), port only on localhost. Files: [`docker/`](../docker/).
- Workflows are deployed from this repo through the n8n public API, called on the server itself; `/api/*` is not reachable from outside ([D014](../plan/decisions/D014-deploy-workflow-via-api.md)).
- Daily encrypted off-server backup (F04).
- Phases 1–2 run here. Phase 3 (sandbox running untrusted code) should get a separate small server.

## Flow (phases)
1. **Triage comment** (live). Webhook (issues: opened, signature check) → guards (D009) → AI Agent (Claude Haiku, read-only tools: list directory, read file, search issues) → GitHub comment ([D011](../plan/decisions/D011-ai-agent-node.md)); details in [`workflows/README.md`](../workflows/README.md).
2. **Labels + duplicates** (live). Agent sets up to 3 whitelisted labels and links possible duplicates (open + closed) in the comment ([D013](../plan/decisions/D013-labels-and-duplicates.md)).
3. **Fix in sandbox** (todo, F08). Maintainer adds a label (e.g. `agent:fix`) → n8n starts Claude Code headless in a Docker container (network limited to GitHub/Anthropic) → PR.

## Security
- **Target repo is public: anyone can open an issue.** Issue text goes into the agent (prompt injection). Its damage is limited by the token below.
- **GitHub token (phases 1–2):** fine-grained personal access token, scoped to the target repo only:
  - `Issues: Read and write`: read the issue, search issues, post the comment, add labels.
  - `Contents: Read-only`: list directories and read files for the agent.
  - `Metadata: Read-only`: added by GitHub automatically.
  - Nothing else: no code write, no PRs, no webhook or settings access. Worst case with this token is a bad comment or label, not a code change.
  - Stored only as an n8n credential on the server. Comments appear as the token owner's account (no bot account for now, F05).
- Phase 3 runs only on a label set by a maintainer, never automatically.
- Limit iterations and tokens per run; log cost per run.
- n8n behind HTTPS, strong owner password, regular image updates.
- Secrets only in server `.env` / n8n credentials, never in this repo.
