# Log

One line per change, newest on top: `YYYY-MM-DD · ID · what changed`.

- 2026-11-06 · D015, D005, F08, Q3, R7 · Phase 3 via GitHub Actions in the target repo (supersedes D005 for phase 3); F08 plan; Q3 opened.
- 2026-11-06 · F07, D014 · Deploy via API works; Caddy blocks /api from outside; F07 done (duplicate found, labels set). Phase 2 complete.
- 2026-11-06 · D014 · Workflows deploy from the repo via n8n public API (researched options); Caddy blocks /api/* from outside.
- 2026-11-06 · D013, F07 · Whitelisted labels + duplicate search (open + closed) added to the workflow.
- 2026-11-06 · F05, F06 · F05 done (spend limit set). F06 done: live workflow matches repo; sanitize script for future exports. Phase 1 complete.
- 2026-11-06 · F05 · Measured cost ~$0.01 per triage (first run).
- 2026-11-06 · F04 · First off-server backup OK; schedule weekly.
- 2026-11-06 · F04, R6 · Daily encrypted off-server backup; F04 done, R6 mitigated.
- 2026-11-06 · D012 · Webhook secret stays in the Code node (options A–D with pros/cons).
- 2026-11-06 · F05 · Comments stay on the owner account (no bot account for now).
- 2026-11-06 · F03, F05 · F03 done; first end-to-end triage on a test issue worked.
- 2026-11-06 · D010, D011, F05 · Real agent preferred: D011 (AI Agent node + GitHub tools) supersedes D010; workflow rebuilt.
- 2026-11-06 · F05 · Docs: n8n 2.x uses Publish instead of Activate.
- 2026-11-06 · F05, D010 · Draft triage workflow (fixed two-call pipeline, Haiku); compose allows crypto in Code node; CI checks workflow has no secret.
- 2026-11-06 · D009 · Decided: triage every issue with limits, cost cap $1/day.
- 2026-11-06 · F04 · First backup OK.
- 2026-11-06 · Q1, D009, R2, F03, F04, F05 · Anyone can open issues: D009 proposed (auto triage with hard limits); update procedure written.
- 2026-11-06 · F04 · Owner account created.
- 2026-11-06 · F02, F04 · F02 done: n8n deployed and reachable over HTTPS; F04 started.
- 2026-11-06 · F02 · Caddy import line prepared in owning project; ops repo got caddy-check / caddy-site actions.
- 2026-11-06 · F02 · Server prep done (swap, Docker, Caddy sites folder), DNS record added.
- 2026-11-06 · D003, D007, Q2, F02 · Docker + SQLite decided (SQLite because of project scope); compose, Caddy site, .env.example added.
- 2026-11-06 · F01, F02, D003, D007, R10 · Removed server specifics from public repo; moved to private ops repo.
- 2026-11-06 · F01, D003, D007, R10 · F01 done (server check); SQLite recommended; Docker not installed; isolation risk added.
- 2026-11-06 · D008, F01, F02 · Ops via private repo GitHub Actions; server facts and Caddy overwrite issue noted.
- 2026-11-06 · R1–R8 · Added `risks.md` with initial risks.
- 2026-11-06 · – · Added `check.py` (validation + generated INDEX tables) and CI workflow.
- 2026-11-06 · – · Moved roadmap + decision log into `plan/` (index, one file per feature/decision, research, questions, log).
- 2026-11-06 · D001–D006 · Initial decisions recorded; D007 open.
