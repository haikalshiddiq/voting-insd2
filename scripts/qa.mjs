import fs from 'node:fs';
const worker=fs.readFileSync('src/index.js','utf8');
const front=fs.readFileSync('public/index.html','utf8');
const admin=fs.readFileSync('public/admin.html','utf8');
const migration=fs.readFileSync('migrations/0002_admin_audit.sql','utf8');
const eligible=JSON.parse(fs.readFileSync('src/eligible.json'));
const checks={
  eligible: eligible.length===22 && new Set(eligible.map(x=>x.nim)).size===22,
  logoutApi: worker.includes("u.pathname==='/api/logout'") && worker.includes("DELETE FROM redeems WHERE round=? AND token_hash=? AND used=0"),
  logoutUi: front.includes("getElementById('logout').addEventListener('click',logout)") && front.includes('Membatalkan sesi...'),
  auditSchema: migration.includes('voter_nim') && worker.includes('INSERT INTO ballots(id,round,candidate_nim,created_at,voter_nim)'),
  auditApi: worker.includes('auditRows=') && worker.includes('candidateName'),
  auditUi: admin.includes('Audit pemilih') && admin.includes('audit-table'),
  deadline: worker.includes('2026-11-11T13:00:00.000Z'),
  disclosure: front.includes('admin dapat melihat siapa yang sudah memilih dan kandidat yang dipilih')
};
for(const [k,v] of Object.entries(checks)) if(!v){console.error('FAIL',k);process.exit(1)}
console.log('QA PASS',checks);
