**Serves:** journal TOOL-aLiftedCeiling-2

# Build brief — TOOL-aLiftedCeiling-2

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- Unit 1 is CLOSED: the instruction-edits leg's ceiling is 420 s and its evidence row stands at 110 s. The closing review's round 1
  (`memory/builds/aLiftedCeiling/reviews/2026-11-12-review-TOOL-aLiftedCeiling-1-diff-review-round1.md`) CONVERGED clean with one
  LOW, promoted to this unit: the row's source names no host load and a commit other than the spec's.
- The spec's F1 is resolved: the source names the commit the race ran at. The row is rewritten by the kit's `--reset` and
  `--observed` in one call, inside a fresh scratch clone taken at HEAD, and the generated file is copied back; never run `--write`
  in this worktree. The value stays 110.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-aLiftedCeiling-2`, its trailer block carrying `Pass: TOOL-aLiftedCeiling-2` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/aLiftedCeiling/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/aLiftedCeiling/build/2026-11-12-build-TOOL-aLiftedCeiling-2-ledger.md`; each line leads
  with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background.
- Run no gate leg, no suite, no bar. If the role hook refuses the ceiling check, name it in your return for the main loop.
