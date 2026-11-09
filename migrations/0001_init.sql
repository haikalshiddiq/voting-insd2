CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
INSERT OR IGNORE INTO settings(key,value) VALUES ('open','true'),('round','1'),('round2_candidates','[]');
CREATE TABLE IF NOT EXISTS redeems (round INTEGER NOT NULL, nim_hash TEXT NOT NULL, token_hash TEXT NOT NULL UNIQUE, used INTEGER NOT NULL DEFAULT 0, redeemed_at TEXT NOT NULL, used_at TEXT, PRIMARY KEY(round,nim_hash));
CREATE TABLE IF NOT EXISTS ballots (id TEXT PRIMARY KEY, round INTEGER NOT NULL, candidate_nim TEXT NOT NULL, created_at TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS idx_ballots_round ON ballots(round);
