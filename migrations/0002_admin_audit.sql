ALTER TABLE redeems ADD COLUMN voter_nim TEXT;
ALTER TABLE ballots ADD COLUMN voter_nim TEXT;
CREATE INDEX IF NOT EXISTS idx_redeems_voter_nim ON redeems(round, voter_nim);
CREATE INDEX IF NOT EXISTS idx_ballots_voter_nim ON ballots(round, voter_nim);
