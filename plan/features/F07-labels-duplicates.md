---
id: F07
title: "Phase 2: labels + duplicate detection"
status: in-progress
phase: 2
depends_on: [F05]
decisions: [D013]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F07: Labels + duplicates

## Goal
Agent proposes/sets a label and links similar open issues.

## Tasks
- [x] decide: whitelisted labels set automatically, duplicates linked (D013)
- [x] workflow: "Search issues" tool (open + closed), duplicates section in comment
- [x] workflow: agent proposes labels, code filters by whitelist, labels set after the comment
- [ ] update the live workflow in n8n and test

## Acceptance
- Duplicate test issue gets link to the original.

## Notes
- 2026-11-06: workflow updated (12 nodes, max 10 iterations). Not yet live.
