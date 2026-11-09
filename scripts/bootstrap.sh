#!/usr/bin/env bash
set -euo pipefail
npm install
npx wrangler d1 create voting-insd2 --update-config
echo "$ADMIN_KEY" | npx wrangler secret put ADMIN_KEY
echo "$TURNSTILE_SECRET_KEY" | npx wrangler secret put TURNSTILE_SECRET_KEY
npx wrangler d1 migrations apply voting-insd2 --remote
npm run qa
npx wrangler deploy
