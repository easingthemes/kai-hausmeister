---
id: D010
title: Fixed two-call pipeline instead of AI Agent node (phase 1)
status: decided
date: 2026-11-06
features: [F05]
supersedes: null
superseded_by: null
---

# D010: Fixed pipeline instead of AI Agent node

## Context
F05 must enforce D009 (daily $1 cost cap, per-run limits) on public, untrusted issues. The original plan used n8n's AI Agent node with a "read file" tool.

## Options

| Option | Pro | Con |
|---|---|---|
| **Fixed pipeline: HTTP calls to the Messages API (pick files → triage)** | exact token usage from every response → exact cost cap; bounded: always 2 calls, max 5 files; prompt injection can only pick files from the repo list | less flexible than an agent; agent can't follow leads across files |
| n8n AI Agent node + tools | standard n8n pattern; agent explores freely | no token usage in output → cost cap only estimated; loop length depends on the model; tools reachable by injected instructions |

## Decision
Fixed pipeline for phase 1. Model `claude-haiku-5-5`, effort `low`.

## Consequences
- Revisit for phase 2/3 if triage quality needs exploration; an agent would need its own cost tracking.
- Workflow: `workflows/triage.json`.
