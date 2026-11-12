**Serves:** journal TOOL-aQueuedIndex-3

# Build brief — TOOL-aQueuedIndex-3

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- Units 1 and 2 are CLOSED. The closing review's round 2
  (`memory/builds/aQueuedIndex/reviews/2026-11-12-review-TOOL-aQueuedIndex-2-diff-review-round2.md`) CONVERGED clean with one
  LOW, promoted to this unit: the busy timeout has no check that fails if it shrinks.
- The spec's F1 is resolved: the plant's green verdict requires the timeout at 600 or more, and the plant prints it.
- No change to the timeout's value or to the locking. Any probe that writes an index runs in a scratch repository of its own.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-aQueuedIndex-3`, its trailer block carrying `Pass: TOOL-aQueuedIndex-3` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/aQueuedIndex/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/aQueuedIndex/build/2026-11-12-build-TOOL-aQueuedIndex-3-ledger.md`; each line leads
  with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background; include every generated file
  the index generator rewrites.
- Run no gate leg, no suite, no bar. The arm's staged break is the main loop's to observe after your pass.
