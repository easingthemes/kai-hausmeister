# workflows/

Exported n8n workflows (template, D001). Import: n8n → **Workflows → ⋯ → Import from file**.

## triage.json (phase 1, F05)

New issue → one triage comment. Fixed pipeline with two Claude calls, no agent loop ([D010](../plan/decisions/D010-fixed-pipeline.md)):

```
GitHub webhook → Verify & filter → Get issue → Guards → Get repo tree
→ Build file request → Claude: pick files → Parse file list → Get file (per file)
→ Build triage request → Claude: triage → Prepare comment → Post comment
```

| Step | What it does |
|---|---|
| Verify & filter | HMAC SHA-256 check of `X-Hub-Signature-256` on the raw body (fails the execution if wrong); only `issues/opened` for the configured repo. Holds `CONFIG`. |
| Get issue | Re-reads the issue from the GitHub API: everything after this uses API data, not the webhook payload |
| Guards | D009 limits: no PRs/bots, each issue once, max runs/day, max issues per author/day, daily cost cap. Counters in workflow static data |
| Claude: pick files | Haiku picks up to 5 files from the repo file list (structured JSON output); unknown paths are dropped |
| Claude: triage | Haiku writes the comment from issue + files |
| Prepare comment | Adds both calls' cost to the daily total; strips images, non-github links and @mentions; adds footer; posts nothing on refusal/empty output |

### Setup
1. Needs `NODE_FUNCTION_ALLOW_BUILTIN=crypto` in the n8n container (already in `docker/docker-compose.yml`; redeploy once).
2. Import `triage.json`.
3. Credentials: select yours in every **GitHub** HTTP node (Get issue, Get repo tree, Get file, Post comment) and both **Claude** nodes. Names in the file: `GitHub dx-aem-flow`, `Anthropic hausmeister`.
4. Open **Verify & filter**, set `CONFIG.webhookSecret` (and check `repo`, `branch`).
5. Activate the workflow. Production URL: `https://<n8n host>/webhook/github-issues`.
6. Add the webhook in the target repo (F03): that URL, `application/json`, same secret, event **Issues** only.

**Never commit the workflow with the real secret.** When exporting again, put the placeholder `REPLACE_WITH_WEBHOOK_SECRET` back; CI fails otherwise.

### Limits (in `CONFIG`)
`dailyCostCapUsd` 1.0 · `dailyRunCap` 30 · `perAuthorDailyCap` 3 · `maxIssueChars` 6000 · `maxFiles` 5 · `maxFileChars` 12000 · `maxCommentChars` 4000.

Counters, last skip reason and a log of the last 50 runs (cost per run) are in the workflow's static data. They only persist for production (active) executions, not for manual test runs.

### Cost
`claude-haiku-5-5`: $0.10 / $0.50 per million input / output tokens (prompts ≤ 100K tokens). A run reads roughly 10–40K input tokens and writes 1–3K output tokens, so about $0.002–0.006 per issue. The $1/day cap is a safety net, not the expected spend.
