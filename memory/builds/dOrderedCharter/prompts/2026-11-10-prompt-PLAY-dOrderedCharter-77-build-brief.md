**Serves:** journal PLAY-dOrderedCharter-77

# Build brief — PLAY-dOrderedCharter-77

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's close. The full bar over `3c63fe888` failed sixteen legs; fifteen were this build's own, and the main loop
  fixed the record-only ones at `de36424bf` and `51cd8b402`. This unit carries every remaining fix under `tools/` and `skills/`.
- The main loop measured the five held self-test legs over the tree, each run alone:
  - `core selftest` 38 s, green (DERIVED at 51cd8b402);
  - `instruction edits selftest` 103 s, green (DERIVED at 51cd8b402);
  - `tags positional selftest` 108 s, pass (DERIVED at 51cd8b402);
  - `tags bundle selftest` 22 s, pass (DERIVED at 51cd8b402);
  - `instruction units selftest` 161 s (DERIVED at 51cd8b402), one expectation red on `database is locked`, because another
    session's suite held the shared `.git/gov/index.db` at that moment.
- Use these walls for the budget rows; the main loop re-runs the last one with the index quiet and reports any real red.
- The tags leg ran 210 s alone over the tree, green (DERIVED at de36424bf).
- PLAY-dOrderedCharter-31 is parked and will not land in this run; nothing you build may rest on it.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-77`, its trailer block carrying `Pass: PLAY-dOrderedCharter-77` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-77-ledger.md`. The owed
  observations for units 18, 65 and 72 go in their own ledgers, as lines naming this pass, each leading with a backticked token its
  criterion carries. A departure from the spec is a `deviation` record.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path: each call takes about ten minutes here. A file on the
  kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map generator's
  output; declare both.
- Run no gate leg, no suite, no bar. The legs your criteria name are the main loop's to observe after your pass.
