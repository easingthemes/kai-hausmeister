---
id: F08
title: "Phase 3: sandboxed fix → PR"
status: todo
phase: 3
depends_on: [F07]
decisions: [D015]
questions: [Q3]
created: 2026-11-06
updated: 2026-11-06
---

# F08: Sandbox fix

## Goal
Maintainer adds a fix label to an issue → a GitHub Actions run in the target repo uses Claude Code to work on the issue and opens a PR. A human reviews and merges; the agent never merges.

## Flow
```
issue labeled (only triage/write users can label)
  → .github/workflows/<name>.yml in target repo (on: issues: labeled)
  → job runs only if the label is in the allowlist
  → anthropics/claude-code-action: checkout, branch, change, test
  → PR linked to the issue + comment with result
```

## Tasks
- [x] answer Q3: no dx plugins for now (example only)
- [ ] choose label name and prompt (plain Claude Code, no dx skills)
- [ ] reuse the owner's existing workflow from the other project as template (no project data copied)
- [ ] workflow: `on: issues: types: [labeled]`, `if:` label in allowlist, `concurrency` per issue, `timeout-minutes`, max turns, model
- [ ] `permissions`: `contents: write`, `pull-requests: write`, `issues: write`; nothing else
- [ ] Anthropic auth: separate workspace + spend limit; federation if available, else API key secret
- [ ] branch protection on the default branch: PR + review required
- [ ] remove the label after the run (so a second run needs a new label)
- [ ] test on a simple issue

## Acceptance
- Simple test issue + label → PR with passing checks, linked to the issue; no change lands without review.

## Notes
- 2026-11-06: paused. Q3: dx plugins not used (too much work to adapt to GitHub). Later idea: dx-aem-flow fixing itself with its own skills. Wait for F10 before building.
- 2026-11-06: D015: GitHub Actions in the target repo; n8n not involved in phase 3.
