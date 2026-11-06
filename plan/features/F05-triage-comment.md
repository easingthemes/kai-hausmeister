---
id: F05
title: "Phase 1: webhook → AI agent → comment"
status: todo
phase: 1
depends_on: [F03, F04]
decisions: [D006]
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
- [ ] limits: max iterations, max tokens; log cost per run
- [ ] prompt treats issue text as untrusted (prompt injection)

## Acceptance
- 3 test issues (bug, feature, nonsense) get sensible comments; nothing else changes in repo.

## Notes
