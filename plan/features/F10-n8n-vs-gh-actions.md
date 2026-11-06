---
id: F10
title: "Research: n8n vs GitHub Actions for this project"
status: todo
phase: later
depends_on: []
decisions: [D001, D011, D015]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F10: n8n vs GitHub Actions

## Goal
Clear answer to "what does n8n add here?". Phases 1–2 (triage comment, labels, duplicates) could also run as a GitHub Actions workflow on `issues: opened`, like phase 3 might (D015). The result also decides D015.

## Tasks
- [ ] list what phases 1–3 need: trigger, secrets, agent loop, tools, limits/cost caps, logs, state (counters, seen issues), multi-repo
- [ ] compare n8n (current) vs GitHub Actions (+ `claude-code-action`) per need: setup, ops effort (server, updates, backups), cost, security, debugging, reuse for other repos
- [ ] note where n8n clearly wins (e.g. non-GitHub triggers, visual editing, cross-repo state, integrations) and where it doesn't
- [ ] write result in `research.md`; if the answer is "drop n8n", new decision superseding D001

## Acceptance
- Comparison table in `research.md` and a recommendation.

## Notes
- 2026-11-06: owner question: phase 1 comment could have been a GitHub workflow too; what is n8n for?
