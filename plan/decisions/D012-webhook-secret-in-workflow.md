---
id: D012
title: Webhook secret stays in the Code node config
status: decided
date: 2026-11-06
features: [F05]
supersedes: null
superseded_by: null
---

# D012: Webhook secret in the Code node

## Context
The signature check needs the webhook secret inside a Code node. n8n Community has no secret store readable from Code nodes (credentials are encrypted but not readable there; Variables and External Secrets are paid features).

## Options

| Option | Pro | Con |
|---|---|---|
| **A: secret in the Code node `CONFIG`** | simple, works now | visible to anyone with n8n access (only the owner); stored unencrypted in the DB and backups |
| B: env variable + `$env` | not visible in UI or exports | needs `N8N_BLOCK_ENV_ACCESS_IN_NODE=false`: every expression and Code node can read all env vars, incl. the credentials encryption key |
| C: GitHub Trigger node instead of Webhook node | n8n manages webhook and secret, nothing visible | token needs `Webhooks: write` (reverses D006) |
| D: External Secrets / Variables | proper secret store | paid plan |

## Decision
**A.** Impact of a leak is low: a forged webhook can only make the workflow re-read an existing issue from the GitHub API, and guards allow each issue once plus daily caps. B would weaken a more important secret.

## Consequences
- Exported workflows in this repo keep the placeholder; CI checks it.
- Revisit with C if n8n gets more users or the secret needs rotation without editing the workflow.
