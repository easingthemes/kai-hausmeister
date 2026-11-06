# workflows/

Exported n8n workflows (template, D001). Import: n8n → **Workflows → ⋯ → Import from file**.

## triage.json (phase 1, F05)

New issue → one triage comment, written by an AI agent ([D011](../plan/decisions/D011-ai-agent-node.md)).

```
GitHub webhook → Verify & filter → Get issue → Guards → Triage agent → Prepare comment → Post comment
                                                          ├─ Claude Haiku (model)
                                                          ├─ List directory (tool, read-only)
                                                          └─ Read file (tool, read-only)
```

| Node | What it does |
|---|---|
| Verify & filter | HMAC SHA-256 check of `X-Hub-Signature-256` on the raw body (fails the execution if wrong); only `issues/opened` for the configured repo. Holds `CONFIG` |
| Get issue | Re-reads the issue from the GitHub API; the agent sees API data, not the webhook payload |
| Guards | D009: no PRs/bots, each issue once, max 20 runs/day, max 3 issues per author/day. Counters in workflow static data |
| Triage agent | `claude-haiku-5-5`, max 8 iterations, browses and reads repo files, writes the comment. Issue text marked as untrusted |
| Prepare comment | Strips images, non-github links and @mentions; adds footer |

### Setup
1. `NODE_FUNCTION_ALLOW_BUILTIN=crypto` in the n8n container (in `docker/docker-compose.yml`; redeploy once).
2. Import `triage.json`.
3. Credentials: select yours in **Get issue**, **Post comment**, **List directory**, **Read file** (GitHub) and **Claude Haiku** (Anthropic). Names in the file: `GitHub dx-aem-flow`, `Anthropic hausmeister`.
4. **Claude Haiku** node: check the model is `claude-haiku-5-5` (pick it from the list if the field is empty).
5. **Verify & filter**: set `CONFIG.webhookSecret`. Repo and branch (`main`) are also in the two tool URLs.
6. **Publish** (n8n 2.x: changes autosave as drafts; Publish makes them live, replaces the old Activate toggle). Production URL: `https://<n8n host>/webhook/github-issues`.
7. Add the webhook in the target repo (F03): that URL, `application/json`, same secret, event **Issues** only.

**Never commit the workflow with the real secret.** When exporting again, put `REPLACE_WITH_WEBHOOK_SECRET` back; CI fails otherwise.

### Cost
`claude-haiku-5-5`: $0.10 / $0.50 per million input / output tokens (prompts ≤ 100K). The agent node reports no token usage, so the $1/day cap (D009) is enforced indirectly: 20 runs/day × ~$0.05 worst case. Set a spend limit on the Anthropic workspace as hard stop, and check real cost per run in the Anthropic console.
