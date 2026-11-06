---
id: D005
title: Separate repo, target via webhook + GitHub API
status: superseded
date: 2026-11-06
features: [F03]
supersedes: null
superseded_by: D015
---

# D005: Separate repo for integration

## Context
Where the integration setup lives relative to the target repo (dx-aem-flow).

## Options

| Option | Pro | Con |
|---|---|---|
| **Separate repo (this one)** | no code changes in target; reusable for more repos | one more repo |
| Inside target repo | everything in one place | mixes concerns; not reusable |

## Decision
**Superseded by [D015](D015-phase3-github-actions.md) (2026-11-06) for phase 3 only: the fix agent runs as GitHub Actions in the target repo. Phases 1–2 still follow this decision.**

Separate repo. Target connected only via webhook + GitHub API.

## Consequences
More repos later = add webhook + extend token.
