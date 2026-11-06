# Project instructions

kai-hausmeister: n8n integration that triages GitHub issues with an AI agent and later fixes them in a sandbox.

## Read first
1. **`plan/INDEX.md`**: status of all features, decisions, open questions, and what is next.
2. Then open only the linked files you need. `docs/architecture.md` for how the system fits together.

## Plan folder
```
plan/
  INDEX.md        status overview, links to everything
  features/       FNN-name.md, one per feature (YAML header: status, depends_on, ...)
  decisions/      DNNN-name.md, one per decision (options with pro/con)
  research.md     facts and comparisons, no decisions
  questions.md    open questions (QN)
  risks.md        risks (RN): likelihood, impact, mitigation, status
  check.py        validates headers/refs, generates INDEX tables
  log.md          one line per change, newest on top
  _templates/     copy these for new files
```

## Rules for keeping docs in sync
- Status lives in the YAML header of the feature/decision file. INDEX feature/decision tables are **generated**: after editing headers run `python3 plan/check.py --write` and commit the result. Never edit those tables by hand.
- Before commit: `python3 plan/check.py` must pass (CI runs it too).
- On any change: update `updated:` in the header and add one line to `plan/log.md`.
- New feature/decision: copy from `plan/_templates/`, next free ID, then `python3 plan/check.py --write` adds the INDEX row.
- Decision changes: never rewrite a `decided` one; create a new one with `supersedes:` and set the old one to `superseded`.
- New or changed risk: edit the row in `risks.md` (status in last column).
- Answered question: fill answer in `questions.md`, update the files it affects.
- Keep "Next up" in INDEX current (max 3 items).
- Research results go in `research.md` with date and source; decisions only link to it.

## Public repo: no server specifics
This repo is **public**. The ops repo `kai-hausmeister-private` is private.
- Here: plans, decisions, generic architecture, conclusions.
- Not here: IPs, hostnames, user names, paths on the server, software versions, process/app names, ports, uptime, raw check output, anything copied from private repos. Put those in the private repo (`docs/server.md`) and link to it as "private ops repo".
- **Security findings** (leaks, weaknesses, exposed data, how to exploit something) never go here: not in files, commit messages, PR titles/bodies or issues. Describing a weakness in public is a new leak. Put them in the private repo (`docs/security.md`); here at most "see private ops repo".
- Before commit, check the diff and the commit message for such details.

## General
- Secrets never in the repo; only `.env.example` with variable names.
- Work on a branch, never commit directly to `main`.
