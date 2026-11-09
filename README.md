# Voting InSD2 on Cloudflare Workers

Stack: Workers + D1 + Static Assets + Turnstile + Cloudflare Access (admin) + ADMIN_KEY.

## Required from owner
- Cloudflare Account ID
- API token with Workers Scripts:Edit, D1:Edit, Account Settings:Read, and Access Apps/Policies:Edit if Access is automated
- Turnstile site key and secret key
- Admin email allowed by Cloudflare Access
- ADMIN_KEY random >=32 characters
- A hostname for Access, recommended custom domain such as vote.example.ac.id. workers.dev can deploy the app, but Access setup is easiest with a hostname you control.

## First deploy
1. `npm install`
2. `npx wrangler login` or export CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID.
3. Create Turnstile widget, then replace TURNSTILE_SITE_KEY in wrangler.jsonc.
4. Replace ADMIN_EMAILS in wrangler.jsonc.
5. `npx wrangler d1 create voting-insd2 --update-config`
6. `npx wrangler secret put ADMIN_KEY`
7. `npx wrangler secret put TURNSTILE_SECRET_KEY`
8. `npx wrangler d1 migrations apply voting-insd2 --remote`
9. `npm run qa && npx wrangler deploy`
10. In Cloudflare Zero Trust > Access > Applications, protect `/admin*` for the admin email. The Worker API still requires both the Access email header and ADMIN_KEY.

## Local
Copy `.dev.vars.example` to `.dev.vars`, use Cloudflare Turnstile test keys, then `npm run db:local` and `npm run dev`.
