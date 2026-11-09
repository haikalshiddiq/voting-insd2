# Session lifecycle fix
Token browser memakai sessionStorage, tab close mengirim sendBeacon logout, heartbeat berjalan tiap 30 detik, sesi tanpa heartbeat kedaluwarsa 120 detik, dan logout idempotent. Jika browser gagal mengirim beacon saat ditutup, NIM dapat diredeem ulang paling lambat sekitar 2 menit kemudian. Migration 0003 wajib diterapkan oleh workflow.
