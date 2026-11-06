# Decision log

| Date | Decision | Why | Status |
|---|---|---|---|
| 2026-11-06 | Self-hosted n8n + exported template in repo | self-host needed for sandbox (phase 3); template keeps it reusable | decided |
| 2026-11-06 | Self-host first, n8n Cloud evaluated later | compare operating it ourselves vs managed | decided |
| 2026-11-06 | Docker Compose (instead of `npx n8n`) | easy update and rollback, DB in same file, Docker needed for phase 3 | proposed |
| 2026-11-06 | Phases 1–2 on an existing small VPS | enough resources, no extra cost; revisit before phase 3 | decided |
| 2026-11-06 | Separate repo for the integration; target repo connected via webhook + GitHub API | no code changes in target repo; reusable for more repos | decided |
| 2026-11-06 | n8n Webhook node with manual webhook + secret (not GitHub Trigger node) | token needs no webhook-admin permission; smaller blast radius | decided |
| — | SQLite or Postgres | SQLite lighter, enough for single user; Postgres is the production setup | open |
