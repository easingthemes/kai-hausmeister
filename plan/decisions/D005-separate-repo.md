---
id: D005
title: Separate repo, target via webhook + GitHub API
status: decided
date: 2026-11-06
features: [F03]
supersedes: null
superseded_by: null
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
Separate repo. Target connected only via webhook + GitHub API.

## Consequences
More repos later = add webhook + extend token.

Note 2026-11-06: phase 3 may need a workflow file in the target repo, if [D015](D015-phase3-runtime.md) option A is chosen. Then a new decision supersedes this one for phase 3.
