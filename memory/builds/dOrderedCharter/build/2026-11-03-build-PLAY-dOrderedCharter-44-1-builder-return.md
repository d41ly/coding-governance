# dOrderedCharter — unit 44's builder return

**Serves:** journal PLAY-dOrderedCharter-44

Run wf_7ef495a3-4bf, summarized from its return.

- Built at rev-2 as pass commit `757d12bfb`: the `blob_parsed(blob, extractor, version)` table replacing unit 19's
  `parsed` sentinel row in `blob_row`; versions derived as the first 12 hex of the SHA-256 of each extractor's module;
  `INDEX_SCHEMA = 1` stamped through `PRAGMA user_version` with a rebuild on any other stamp; the build summary's
  `<n> extractor runs, <m> skipped as fresh`; four plants (`new-extractor`, `extractor-edit`, `tagless`, `schema`).
- `Decided:` trailer: unit 19's built code already keyed freshness on (blob, extractor) through its sentinel, so AC1 and
  AC2 held at the base; the version key, the schema stamp and the plants are what this pass adds.
- Probe over the real tree: a cold build made 10360 extractor runs in 21.7 s, a warm walk 0 runs and 10360 skipped in
  2.3 s.
- Owed by the checklist (two-answers-to-one-question): the `schema` arm row in `tools/playbook/adopt-playbook.sh`
  spells `schema 0 to 1`, a second copy of `INDEX_SCHEMA`; the write gate refused the edit after the CLOSED flip, so it
  is handed to PLAY-dOrderedCharter-22's brief.
- Owed at the close: RED then GREEN for the four new `adopt-playbook.sh` rows against a staged blob-only freshness
  rule (not unit 19's code, which already keyed per extractor); the playbook render selftest, govkit acceptance matrix,
  encoding posture, spec tokens and `tags` legs.
- Handed to PLAY-dOrderedCharter-51: two worktrees sharing the index at different extractor versions rebuild over each
  other.
