# Voting InSD2 UX Edition
Deadline server: 11 November 2026 20:00 WIB (13:00 UTC).

Sebelum upload, pertahankan database_id D1 asli dari wrangler.jsonc repository karena ZIP memakai placeholder. Timpa file lain, commit, lalu jalankan workflow Deploy Voting UX dengan Turnstile Site Key produksi. Logout membatalkan redeem yang belum digunakan sehingga NIM bisa login kembali.


Fix deployment: compatibility_date telah ditetapkan ke 2026-11-09 agar tidak ditolak sebagai tanggal masa depan oleh Cloudflare API. Workflow juga menormalisasi tanggal sebelum deploy.
