# Voting InSD2 UX + Logout Fix + Admin Audit

Perbaikan:
- Tombol logout memakai event listener eksplisit, menampilkan status loading, memanggil `/api/logout`, menghapus redeem yang belum dipakai dari D1, lalu kembali ke validasi NIM.
- Migration `0002_admin_audit.sql` menambahkan `voter_nim` ke redeem dan ballot.
- Admin dapat melihat pemilih, status sesi, kandidat yang dipilih, dan waktu pengiriman.
- Data sebelum migration mungkin tidak dapat dipetakan ke pemilih karena versi lama memang menyimpan ballot secara terpisah tanpa identitas.
- Deadline tetap 11 November 2026 pukul 20:00 WIB.

## Deploy
1. Pertahankan `database_id` D1 asli pada `wrangler.jsonc`.
2. Timpa repository dengan isi ZIP.
3. Jalankan workflow `Deploy Voting UX` dan isi Turnstile Site Key produksi.
4. Workflow migration akan menerapkan `0002_admin_audit.sql` sebelum deploy.
