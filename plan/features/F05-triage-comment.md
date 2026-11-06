---
id: F05
title: "Phase 1: webhook → AI agent → comment"
status: done
phase: 1
depends_on: [F03, F04]
decisions: [D006, D009, D011, D012]
questions: [Q1]
created: 2026-11-06
updated: 2026-11-06
---

# F05: Triage comment

## Goal
New issue in target repo gets one comment from the agent: type, affected area, next steps.

## Tasks
- [x] workflow drafted: `workflows/triage.json` (D011: AI Agent node + read-only GitHub tools, Haiku)
- [x] import in n8n, set credentials + webhook secret, publish
- [x] end-to-end test: test issue in target repo got a triage comment (2026-11-06)
- [x] comments are posted as the token owner's account: OK for now (owner decision 2026-11-06); revisit if a bot account is needed
- [x] verify `X-Hub-Signature-256` (HMAC SHA-256 over raw body with webhook secret); reject otherwise
- [x] guards from D009: max 8 iterations, daily run cap 20 (cost proxy for $1/day, D011), max 3 issues per author per day, ignore bots, truncate issue text
- [x] Anthropic workspace spend limit as hard stop (set 2026-11-06)
- [x] prompt treats issue text as untrusted, delimited data (prompt injection, R1)
- [x] comment marked as automated
- [x] check real cost per run: ~$0.01 for the first test issue (Anthropic console, 2026-11-06)

## Acceptance
- 3 test issues (bug, feature, nonsense) get sensible comments; nothing else changes in repo.

## Notes
- 2026-11-06: **done.** Live, tested end to end, spend limit set, cost ~$0.01 per run.
- 2026-11-06: **first end-to-end run OK.** Agent browsed the repo, read the relevant skill file, posted a structured comment (type, area, summary, missing info, next steps). File references checked and correct. Missed that the target README already documents the prerequisite; acceptable for a first triage.
- 2026-11-06: switched to AI Agent node (D011 supersedes D010).
- 2026-11-06: draft workflow written; needs `NODE_FUNCTION_ALLOW_BUILTIN=crypto` (compose) and a redeploy. Not yet tested against real n8n.
