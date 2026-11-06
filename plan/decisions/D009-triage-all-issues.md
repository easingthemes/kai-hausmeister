---
id: D009
title: Triage every new issue automatically, with hard limits
status: proposed
date: 2026-11-06
features: [F05, F07]
supersedes: null
superseded_by: null
---

# D009: Triage every new issue, with limits

## Context
Q1: anyone can open an issue in the target repo. Issue text is untrusted input to the agent (prompt injection, R1) and every issue costs LLM tokens (spam, R2).

## Options

| Option | Pro | Con |
|---|---|---|
| **A: every new issue, automatic, with limits** | fast feedback for everyone; the actual point of triage | needs guards against spam and injection |
| B: only after a maintainer adds a label (e.g. `agent:triage`) | no cost from spam; maintainer filters first | manual step for every issue; slow |
| C: automatic for maintainers/collaborators, label needed for others | spam-safe, still fast for team | external users (most issues?) wait for a maintainer |

## Decision
Proposed: **A**, with these guards:
- read-only GitHub token for code; comment is the only write (no labels/edits in phase 1)
- issue text passed as clearly delimited untrusted data, truncated to a max length
- limits per run (iterations, tokens) and per day (total runs, total cost); stop and post nothing when hit
- per-author limit (e.g. max 3 triaged issues per author per day); bots ignored
- comment states it is automated and not a maintainer decision

Switch to C if spam shows up.

## Consequences
F05 must implement the guards before the webhook goes live. Daily budget values go into the workflow config (F05), cost is logged per run.
