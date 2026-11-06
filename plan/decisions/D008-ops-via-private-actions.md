---
id: D008
title: Server ops via GitHub Actions in a private repo
status: decided
date: 2026-11-06
features: [F01, F02, F04]
supersedes: null
superseded_by: null
---

# D008: Server ops via private GitHub Actions

## Context
Claude Code runs in a cloud container (also from the mobile app) and needs to run commands on the VPS. Outbound port 22 is blocked there, and there is no safe place for an SSH key in the cloud environment.

## Options

| Option | Pro | Con |
|---|---|---|
| **Private repo with `workflow_dispatch` + SSH action** | key stays in GitHub secrets; works from phone; logs private; same pattern as ki-bundestag ops | one more repo; output only via Actions logs |
| SSH key in cloud environment variable | direct shell | key in plain text, visible to all sessions; port 22 blocked |
| `claude remote-control` on the VPS | full shell, approve each command | Claude process on prod server; must be started by hand |
| Run commands by hand, paste output | no access needed | slow |

## Decision
Private ops repo with GitHub Actions (`server-status`, `server-command`). Public repo keeps no server details, because Actions logs of public repos are public.

## Consequences
- Secrets (`DEPLOY_HOST`, `DEPLOY_USER`, `SSH_PRIVATE_KEY`, `DEPLOY_PORT`) set in the private repo, environment `production`.
- New ops tasks (deploy compose, update Caddy site file) become workflows there.
