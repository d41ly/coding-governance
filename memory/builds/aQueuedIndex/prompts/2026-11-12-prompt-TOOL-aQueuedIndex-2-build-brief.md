**Serves:** journal TOOL-aQueuedIndex-2

# Build brief — TOOL-aQueuedIndex-2

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- TOOL-aQueuedIndex-1 is CLOSED and fixed the contention: five races on a fresh index exited green on both writers. The closing
  review's round 1 (`memory/builds/aQueuedIndex/reviews/2026-11-12-review-TOOL-aQueuedIndex-1-diff-review-round1.md`) is
  BLOCKED on the `queued-writers` plant's own arms; this unit is its three items, B1, M1 and L1, in the plant only.
- The spec's fork F1 is resolved on its recommendation: the deleted re-read is not a permanent selftest case in this unit.
- No change to the locking unit 1 shipped. Any probe that writes an index runs in a scratch repository of its own; a
  `database is locked` from a probe against the node's index is contention with another session, retried once.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-aQueuedIndex-2`, its trailer block carrying `Pass: TOOL-aQueuedIndex-2` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/aQueuedIndex/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-2-ledger.md`; each line leads
  with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background; include every generated file
  the index generator rewrites.
- Run no gate leg, no suite, no bar. The arm's staged breaks are the main loop's to observe after your pass.
