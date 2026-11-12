**Serves:** journal TOOL-aLiftedCeiling-1

# Build brief — TOOL-aLiftedCeiling-1

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is aLiftedCeiling's one unit, on the owner's 2026-11-12 answer "Yes, raise it". The spec's forks are resolved in it: the
  ceiling is 420 s, and the evidence row is written by the kit's own verb inside a scratch clone, never in this worktree, whose run
  record would rewrite other legs' rows.
- Any probe that writes a tag index runs in a scratch repository of its own; a `database is locked` from a probe against the node's
  index is contention with another session, retried once.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-aLiftedCeiling-1`, its trailer block carrying `Pass: TOOL-aLiftedCeiling-1` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/aLiftedCeiling/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/aLiftedCeiling/build/2026-11-12-build-TOOL-aLiftedCeiling-1-ledger.md`; each line leads
  with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background, the kickoff manifest among them.
- Run no gate leg, no suite, no bar beyond the ceiling check and the race the spec's criteria name.
