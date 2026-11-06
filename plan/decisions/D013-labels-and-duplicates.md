---
id: D013
title: Agent sets whitelisted labels and links possible duplicates
status: decided
date: 2026-11-06
features: [F07]
supersedes: null
superseded_by: null
---

# D013: Labels from a whitelist, duplicates as links

## Context
Phase 2 (F07): labels and duplicate detection. The target repo is small (~20 issues) and already has labels for type, platform, severity, tier and resolution.

## Options

**Labels**

| Option | Pro | Con |
|---|---|---|
| **Set from a whitelist** (type + platform) | issue list shows triage state at once; prompt injection can at worst set a wrong type label | wrong labels possible; maintainer corrects by hand |
| Only suggest in comment | zero risk | every label added by hand |
| Set any fitting label | most automation | injected or wrong `invalid`/`duplicate`/`wontfix`/severity can hide or mis-rank issues |

**Duplicates**

| Option | Pro | Con |
|---|---|---|
| **Search open + closed issues** | also finds "already fixed" | more results to read |
| Open issues only | fewer tokens | misses closed fixes |
| Embeddings | semantic matching | extra service; not needed for ~20 issues |

## Decision
- Labels set automatically only from: `bug`, `enhancement`, `question`, `documentation`, `platform/claude-code`, `platform/copilot-cli`, `platform/vscode-chat`, `cross-platform`. Never `duplicate`, `invalid`, `wontfix`, `severity/*`, `tier/*`, `released`, `actionable`, `blocked/*`, `good first issue`, `help wanted`.
- Duplicates: agent searches open and closed issues with the GitHub search API and lists candidates in the comment. It never closes or labels an issue as duplicate.
- The whitelist is enforced in code (Prepare comment), not only in the prompt.

## Consequences
- Same token permission (`Issues: write` covers labels).
- Revisit embeddings if the repo grows to hundreds of issues.
