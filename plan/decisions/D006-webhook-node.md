---
id: D006
title: Webhook node + manual webhook (not GitHub Trigger node)
status: decided
date: 2026-11-06
features: [F03, F05]
supersedes: null
superseded_by: null
---

# D006: Webhook node

## Context
How n8n receives issue events.

## Options

| Option | Pro | Con |
|---|---|---|
| **Webhook node + manual webhook with secret** | token needs no webhook-admin permission; smaller blast radius | one manual step per repo; we verify signature ourselves |
| GitHub Trigger node | creates webhook automatically | token needs permission to manage repo webhooks |

## Decision
Webhook node with manual webhook + secret.

## Consequences
F03 includes adding webhook by hand; F05 verifies signature.
