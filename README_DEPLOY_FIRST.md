# Deployment paling singkat

1. Ekstrak ZIP dan upload seluruh file/folder ke root repository GitHub, bukan file ZIP-nya.
2. Di GitHub repository secrets, isi tepat:
   - CLOUDFLARE_ACCOUNT_ID
   - CLOUDFLARE_API_TOKEN
   - ADMIN_KEY
   - TURNSTILE_SECRET_KEY
3. Buka Actions > Bootstrap and Deploy Cloudflare Voting > Run workflow.
4. Untuk deployment pertama, field Turnstile Site Key boleh dikosongkan. Workflow memakai test site key agar hostname workers.dev dapat muncul.
5. Setelah deploy sukses, salin hostname workers.dev dari Cloudflare Workers dashboard.
6. Buat/update widget Turnstile dengan hostname itu. Setelah memperoleh Site Key produksi, jalankan workflow lagi dan isi field turnstile_site_key.
7. Lindungi path /admin* di Cloudflare Zero Trust Access untuk email haikal.shiddiq@cakrawala.ac.id.

Workflow otomatis:
- membuat atau menemukan D1 voting-insd2;
- menulis D1 database ID ke wrangler.jsonc;
- menjalankan migration;
- memasang ADMIN_KEY dan TURNSTILE_SECRET_KEY sebagai Worker secrets;
- menjalankan QA;
- deploy ke workers.dev;
- commit database ID ke repository.

Catatan: API token harus memiliki Workers Scripts Edit dan D1 Edit. Untuk Cloudflare Access, konfigurasi policy tetap dilakukan dari Zero Trust karena memerlukan pilihan identity provider dan policy akun.
