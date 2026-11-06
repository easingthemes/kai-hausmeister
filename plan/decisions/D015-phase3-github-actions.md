---
id: D015
title: "Phase 3 runs as GitHub Actions in the target repo, triggered by label"
status: decided
date: 2026-11-06
features: [F08]
supersedes: D005
superseded_by: null
---

# D015: Phase 3 in GitHub Actions of the target repo

## Context
Phase 3 (F08): an agent writes and runs code to fix an issue and opens a PR. That code runs on untrusted input (issue text), so it needs real isolation (R7). D005 said the target repo gets no changes; phase 3 needs a different setup. The owner already runs this pattern (label = dx skill name → Actions) on another project.

## Options

| Option | Pro | Con |
|---|---|---|
| **A: GitHub Actions in the target repo** (`anthropics/claude-code-action`), triggered by `issues: labeled` | fresh VM per run, deleted after (isolation for free); no extra server; free minutes for public repos; documented, standard; only users with triage/write access can add labels; Anthropic auth can use workload identity federation instead of a static key | target repo gets a workflow file and secrets (changes D005); cost and limits live in the target repo |
| B: own VPS with Docker sandbox, started by n8n | target repo untouched; full control | new server (~€4–5/month) and maintenance; we build and keep the isolation (network rules, gVisor) |
| C: Claude Managed Agents (Anthropic-hosted sandbox), started by n8n | no server; Anthropic runs loop and container | beta; usage-based cost; less control over the environment |

## Decision
**A.** Labels named after the dx skill (e.g. `dx-bug-all`) start the matching run. Supersedes D005 for phase 3 only: phases 1–2 still run in n8n and need no files in the target repo.

## Consequences
- **n8n is not in the phase 3 path.** GitHub triggers the workflow on the label directly; routing through n8n would add a hop, a second secret store and a new failure point without new capability. n8n keeps phases 1–2 (triage on every issue).
- Target repo gets `.github/workflows/` file(s), an Anthropic credential (or federation) and branch protection on the default branch (agent PRs need review).
- Guards move to the workflow: label allowlist, `concurrency` per issue, `timeout-minutes`, max turns, minimal `permissions`, separate Anthropic workspace with its own spend limit.
- Open: the dx skills take an ADO/Jira work item, not a GitHub issue (Q3).
- Update 2026-11-06 (Q3 answered): "label = dx skill name" was an example; phase 3 will not use the dx plugins for now. Label name and prompt decided when F08 starts.
