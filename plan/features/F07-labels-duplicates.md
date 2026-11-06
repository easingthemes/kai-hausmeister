---
id: F07
title: "Phase 2: labels + duplicate detection"
status: done
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
- [x] deploy via "Deploy workflow" (D014) and test with a duplicate issue

## Acceptance
- Duplicate test issue gets link to the original.

## Notes
- 2026-11-06: **done.** Deployed with the new API deploy. Test issue reworded from an earlier one: comment listed the earlier issue under Possible duplicates, skipped the issue itself, labels `bug` + `platform/claude-code` set.
- 2026-11-06: workflow updated (12 nodes, max 10 iterations). Not yet live.
