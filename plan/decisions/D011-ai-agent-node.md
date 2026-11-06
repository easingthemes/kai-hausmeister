---
id: D011
title: AI Agent node with GitHub tools for triage (phase 1)
status: decided
date: 2026-11-06
features: [F05]
supersedes: D010
superseded_by: null
---

# D011: AI Agent node with GitHub tools

## Context
D010 chose a fixed two-call pipeline to measure cost exactly. Owner priority (2026-11-06): a real agent matters more, with as little custom code as possible for now.

## Options

| Option | Pro | Con |
|---|---|---|
| **A: n8n AI Agent node + tools ("List directory", "Read file")** | real agent: explores the repo, follows leads across files; standard n8n building blocks, little custom code; easy to add tools later (search, labels in phase 2); closer to what phase 3 needs | cost per run not measured exactly (agent node gives no token usage) → $1/day only enforced indirectly; run length depends on the model (capped by max iterations); tools are reachable by injected instructions (read-only, one repo); harder to test deterministically |
| B: fixed two-call pipeline (D010) | exact cost from `usage`; always 2 calls, max 5 files; predictable | not an agent; more custom Code nodes; can't explore beyond the first file pick |

## Decision
**A.** Model `claude-haiku-5-5`, max 8 iterations, read-only GitHub tools on the target repo.

## Consequences
- D009 cost cap is enforced indirectly: daily run cap 20 × worst-case ~$0.05 per run (8 iterations, Haiku) ≤ $1/day, plus the spend limit on the Anthropic workspace as hard stop.
- Remaining custom code: signature check, guards (bots, once per issue, run caps), comment sanitizing. Everything else is stock nodes.
- Measure real cost per run in the Anthropic console after go-live; lower the run cap if needed.
- Exact per-run cost tracking would need token usage from the agent; revisit if the console numbers are off.
