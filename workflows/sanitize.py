#!/usr/bin/env python3
"""Turn an n8n export into a reusable template for this public repo.

Usage: python3 workflows/sanitize.py <export.json> <out.json>
Input is one workflow or the array from `n8n export:workflow --all`
(the private ops repo action "export-workflows" prints it, secret already replaced).

Removes instance data (ids, versions, owner/project with name and email,
static data counters, credential ids) and refuses to write if a webhook
secret or a 64-char hex string is still present.
"""
import json
import re
import sys

DROP_TOP = {"id", "createdAt", "updatedAt", "active", "isArchived", "staticData", "meta",
            "versionId", "activeVersionId", "versionCounter", "triggerCount", "shared",
            "versionMetadata", "sourceWorkflowId", "tags", "description", "nodeGroups"}
PLACEHOLDER = "REPLACE_WITH_WEBHOOK_SECRET"


def sanitize(wf):
    out = {k: v for k, v in wf.items() if k not in DROP_TOP}
    out["active"] = False
    out["pinData"] = {}
    for node in out.get("nodes", []):
        for cred in (node.get("credentials") or {}).values():
            cred.pop("id", None)
    return out


def main():
    src, dst = sys.argv[1], sys.argv[2]
    data = json.load(open(src))
    wf = data[0] if isinstance(data, list) else data
    clean = sanitize(wf)
    text = json.dumps(clean, indent=2, ensure_ascii=False) + "\n"
    for m in re.finditer(r"webhookSecret:\s*['\"`]([^'\"`]*)", text):
        if m.group(1) != PLACEHOLDER:
            sys.exit("webhook secret not replaced, refusing to write")
    if re.search(r"[0-9a-fA-F]{64}", text):
        sys.exit("64-char hex string found, refusing to write")
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text.replace("@​", "")):
        sys.exit("email address found, refusing to write")
    open(dst, "w").write(text)
    print(f"wrote {dst}: {len(clean.get('nodes', []))} nodes")


if __name__ == "__main__":
    main()
