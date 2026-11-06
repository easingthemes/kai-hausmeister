# workflows/

Exported n8n workflows (template, D001). Import: n8n → **Workflows → ⋯ → Import from file**.

## triage.json (phase 1 + 2, F05, F07)

New issue → one triage comment with possible duplicates, plus whitelisted labels, written by an AI agent ([D011](../plan/decisions/D011-ai-agent-node.md), [D013](../plan/decisions/D013-labels-and-duplicates.md)).

```
GitHub webhook → Verify & filter → Get issue → Guards → Triage agent → Prepare comment → Post comment → Add labels
                                                          ├─ Claude Haiku (model)
                                                          ├─ List directory (tool, read-only)
                                                          ├─ Read file (tool, read-only)
                                                          └─ Search issues (tool, read-only, open + closed)
```

| Node | What it does |
|---|---|
| Verify & filter | HMAC SHA-256 check of `X-Hub-Signature-256` on the raw body (fails the execution if wrong); only `issues/opened` for the configured repo. Holds `CONFIG` |
| Get issue | Re-reads the issue from the GitHub API; the agent sees API data, not the webhook payload |
| Guards | D009: no PRs/bots, each issue once, max 20 runs/day, max 3 issues per author/day. Counters in workflow static data |
| Triage agent | `claude-haiku-5-5`, max 10 iterations, browses and reads repo files, searches issues for duplicates, writes the comment and a `LABELS:` line. Issue text marked as untrusted |
| Prepare comment | Takes the `LABELS:` line, keeps only whitelisted labels (max 3); strips images, non-github links and @mentions; adds footer |
| Add labels | Adds the filtered labels (empty list = nothing added) |

### Deploy changes (D014)
After a change to `triage.json` is merged: private ops repo → Actions → **Deploy workflow** (ref `main`). It updates the existing workflow in n8n through the public API (same id, same webhook URL), injects the webhook secret and credential ids, and publishes it. No manual import.

Edits made directly in the n8n UI are overwritten by the next deploy. Change the repo instead, or export first (below).

### First setup (new instance)
1. `NODE_FUNCTION_ALLOW_BUILTIN=crypto` in the n8n container (in `docker/docker-compose.yml`; redeploy once).
2. Import `triage.json`.
3. Credentials: select yours in **Get issue**, **Post comment**, **Add labels**, **List directory**, **Read file**, **Search issues** (GitHub) and **Claude Haiku** (Anthropic). Names in the file: `GitHub dx-aem-flow`, `Anthropic hausmeister`.
4. **Claude Haiku** node: check the model is `claude-haiku-5-5` (pick it from the list if the field is empty).
5. **Verify & filter**: set `CONFIG.webhookSecret`. Repo and branch (`main`) are also in the two tool URLs.
6. **Publish** (n8n 2.x: changes autosave as drafts; Publish makes them live, replaces the old Activate toggle). Production URL: `https://<n8n host>/webhook/github-issues`.
7. Add the webhook in the target repo (F03): that URL, `application/json`, same secret, event **Issues** only.

**Never commit the workflow with the real secret.** When exporting again, put `REPLACE_WITH_WEBHOOK_SECRET` back; CI fails otherwise.

### Cost
`claude-haiku-5-5`: $0.10 / $0.50 per million input / output tokens (prompts ≤ 100K). The agent node reports no token usage, so the $1/day cap (D009) is enforced indirectly: 20 runs/day × ~$0.05 worst case. Set a spend limit on the Anthropic workspace as hard stop, and check real cost per run in the Anthropic console.

## Export after changes (F06)
1. Private ops repo → Actions → **n8n Ops** → `export-workflows`. It prints all workflows; the webhook secret is already replaced.
2. Save the JSON between `=====BEGIN EXPORT=====` and `=====END EXPORT=====` to a file.
3. `python3 workflows/sanitize.py export.json workflows/triage.json`. It removes instance data (ids, versions, owner/project with name and email, static data, credential ids) and refuses to write if a secret, a 64-char hex string or an email address is left.
4. Review the diff, commit on a branch.
