---
id: F05
title: "Phase 1: webhook → AI agent → comment"
status: in-progress
phase: 1
depends_on: [F03, F04]
decisions: [D006, D009, D010]
questions: [Q1]
created: 2026-11-06
updated: 2026-11-06
---

# F05: Triage comment

## Goal
New issue in target repo gets one comment from the agent: type, affected area, next steps.

## Tasks
- [x] workflow drafted: `workflows/triage.json` (D010: fixed two-call pipeline, Haiku)
- [ ] import in n8n, set credentials + webhook secret, test with a manual run
- [x] verify `X-Hub-Signature-256` (HMAC SHA-256 over raw body with webhook secret); reject otherwise
- [x] guards from D009: per-run limits (iterations, tokens), daily run cap + cost cap $1/day, max 3 issues per author per day, ignore bots, truncate issue text
- [x] prompt treats issue text as untrusted, delimited data (prompt injection, R1)
- [x] comment marked as automated; log cost per run

## Acceptance
- 3 test issues (bug, feature, nonsense) get sensible comments; nothing else changes in repo.

## Notes
- 2026-11-06: draft workflow written; needs `NODE_FUNCTION_ALLOW_BUILTIN=crypto` (compose) and a redeploy. Not yet tested against real n8n.
