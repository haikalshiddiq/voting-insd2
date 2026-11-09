# Deployment tanpa Cloudflare Zero Trust

Versi ini melindungi panel admin hanya dengan ADMIN_KEY. Turnstile tetap melindungi redeem dan pengiriman suara.

1. Upload seluruh isi paket ke root repository GitHub dan timpa file lama.
2. Pastikan secrets: CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN, ADMIN_KEY, TURNSTILE_SECRET_KEY.
3. Jalankan Actions > Bootstrap and Deploy Cloudflare Voting > Run workflow.
4. Isi Turnstile Site Key produksi.
5. Setelah hijau, buka https://voting-insd2.hicall.workers.dev/admin.html dan masukkan ADMIN_KEY.

ADMIN_KEY harus acak minimal 32 karakter dan tidak dibagikan.
