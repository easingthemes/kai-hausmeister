# Roadmap

| # | Step | Status |
|---|---|---|
| 1 | Check server: `free -h`, `docker --version` | Not started |
| 2 | Decide SQLite vs Postgres | Not started |
| 3 | `docker/docker-compose.yml`, Caddy snippet, `.env.example`; DNS record | Not started |
| 3b | Add webhook (with secret) in target repo; create fine-grained token (Issues: write) | Not started |
| 4 | n8n running behind HTTPS, owner account | Not started |
| 5 | Phase 1: Webhook node → AI Agent → comment (fine-grained token) | Not started |
| 6 | Export workflow JSON to `workflows/`, document setup in README | Not started |
| 7 | Phase 2: labels + duplicates | Not started |
| 8 | Phase 3: sandboxed fix → PR (separate server) | Not started |
| 9 | Run the same workflow on n8n Cloud, document differences | Not started |

## Open questions
- Does the target repo get issues from external users, or only from maintainers?
- SQLite or Postgres.
