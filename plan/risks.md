# Risks

Likelihood and impact: `low` · `med` · `high`. Status (last column): `open` · `mitigated` · `accepted` · `closed`.
When a mitigation is done, set status and add a line to `log.md`.

| ID | Risk | Likelihood | Impact | Mitigation | Affects | Status |
|---|---|---|---|---|---|---|
| R1 | Prompt injection via public issue text makes agent leak data or post harmful content | high | med | issue text treated as untrusted in prompt; token only `Issues: write` + `Contents: read`; no code write in phases 1–2 | F05, F07 | open |
| R2 | LLM cost runs away (spam issues, agent loops) | high | med | max iterations and tokens per run; daily run cap + $1/day cost cap; max 3 issues per author per day; log cost per run (D009) | F05 | open |
| R3 | Webhook endpoint abused (fake requests) | med | med | verify GitHub signature (secret); reject everything else | F03, F05 | open |
| R4 | Token or n8n credentials leak | low | high | fine-grained token, one repo, minimal scope; secrets only in server `.env` / n8n credentials; rotate on suspicion | F03, F04 | open |
| R5 | VPS overloaded, n8n hurts other apps on same server | med | med | check resources first (F01); memory limit in compose; move if needed (D004) | F01, F02 | open |
| R6 | Data loss (workflows, credentials, history) | low | high | weekly backup on server + encrypted off-server copy (30 days); workflow also exported to repo (F06) | F04, F06 | mitigated |
| R7 | Sandbox escape: untrusted code in phase 3 reaches host or secrets | med | high | separate server; network limited to GitHub + Anthropic; only on maintainer label | F08 | open |
| R9 | Ops workflow `server-command` runs any command with deploy key; compromise of GitHub account = server access | low | high | non-root deploy user; dedicated key with no forwarding; 2FA on GitHub; `production` environment | F01, F04 | open |
| R10 | n8n on shared server reads or breaks other apps' data (same user, Code node, prompt injection) | med | high | run n8n in Docker container with only its own volume (D003); no host mounts | F02, F04 | open |
| R11 | Old force-pushed commits (from when the repo was private) are still reachable on GitHub by SHA and contain server specifics (no secrets, no IP) | med | low | GitHub Support request to purge unreferenced commits; keep server patched so the details go stale | – | open |
| R8 | Outdated n8n image with known vulnerabilities | med | med | regular updates; pinned tag + update procedure (F04) | F04 | open |
