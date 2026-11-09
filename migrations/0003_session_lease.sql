ALTER TABLE redeems ADD COLUMN last_seen_at TEXT;
CREATE INDEX IF NOT EXISTS idx_redeems_last_seen ON redeems(round, nim_hash, used, last_seen_at);
