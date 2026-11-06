---
id: F05
title: "Phase 1: webhook → AI agent → comment"
status: todo
phase: 1
depends_on: [F03, F04]
decisions: [D006, D009]
questions: [Q1]
created: 2026-11-06
updated: 2026-11-06
---

# F05: Triage comment

## Goal
New issue in target repo gets one comment from the agent: type, affected area, next steps.

## Tasks
- [ ] Webhook node, verify signature, filter `action == opened`
- [ ] AI Agent node with Anthropic chat model
- [ ] tool: read file from repo (GitHub contents API)
- [ ] GitHub node: create comment
- [ ] verify `X-Hub-Signature-256` (HMAC SHA-256 over raw body with webhook secret); reject otherwise
- [ ] guards from D009: per-run limits (iterations, tokens), daily run cap + cost cap $1/day, max 3 issues per author per day, ignore bots, truncate issue text
- [ ] prompt treats issue text as untrusted, delimited data (prompt injection, R1)
- [ ] comment marked as automated; log cost per run

## Acceptance
- 3 test issues (bug, feature, nonsense) get sensible comments; nothing else changes in repo.

## Notes
