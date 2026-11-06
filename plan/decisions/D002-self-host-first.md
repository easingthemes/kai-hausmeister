---
id: D002
title: Self-host first, n8n Cloud evaluated later
status: decided
date: 2026-11-06
features: [F09]
supersedes: null
superseded_by: null
---

# D002: Self-host first, Cloud later

## Context
We want to compare operating n8n ourselves vs managed.

## Options

| Option | Pro | Con |
|---|---|---|
| **Self-host first** | needed anyway for phase 3; learn ops | more work upfront |
| Cloud first | fast start | no sandbox; would need migration |

## Decision
Self-host first; Cloud comparison as F09.

## Consequences
F09 runs after the workflow is exported (F06).
