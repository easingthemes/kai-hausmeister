---
id: F08
title: "Phase 3: sandboxed fix → PR"
status: todo
phase: 3
depends_on: [F07]
decisions: [D004]
questions: []
created: 2026-11-06
updated: 2026-11-06
---

# F08: Sandbox fix

## Goal
Maintainer sets label `agent:fix` → Claude Code headless in isolated container fixes the issue and opens a PR.

## Tasks
- [ ] separate small server for sandbox (revisit D004)
- [ ] container: network only GitHub + Anthropic, no host access
- [ ] separate token: `Contents: write`, `Pull requests: write`
- [ ] trigger only on maintainer label, never automatic

## Acceptance
- Simple test issue → PR with passing checks.

## Notes
