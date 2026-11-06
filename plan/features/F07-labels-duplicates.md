---
id: F07
title: "Phase 2: labels + duplicate detection"
status: todo
phase: 2
depends_on: [F05]
decisions: []
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F07: Labels + duplicates

## Goal
Agent proposes/sets a label and links similar open issues.

## Tasks
- [ ] decide: set label directly or only propose in comment (new decision)
- [ ] fetch open issues, compare (search API or embeddings, see research)
- [ ] add to comment / set label

## Acceptance
- Duplicate test issue gets link to the original.

## Notes
