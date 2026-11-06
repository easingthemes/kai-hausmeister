# docker/

n8n with SQLite, run with Docker Compose behind the host's Caddy.

| File | Purpose |
|---|---|
| `docker-compose.yml` | n8n service, named volume, port only on `127.0.0.1` |
| `.env.example` | variable names; real `.env` lives only on the server |
| `n8n.caddy` | Caddy site block, imported by the main Caddyfile |

## Run (manual)
```bash
cp .env.example .env   # fill values
docker compose up -d
docker compose logs -f n8n
```

In this project the stack is deployed by a workflow in the private ops repo (D008): it copies these files, writes `.env` from GitHub secrets and runs `docker compose up -d`.

## Update / rollback
Change `N8N_VERSION`, then `docker compose pull && docker compose up -d`. Rollback = previous version.

## Backup
Data is in the `kai-hausmeister_n8n_data` volume (SQLite + config). Back it up together with `N8N_ENCRYPTION_KEY`.
