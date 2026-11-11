**Serves:** journal PLAY-dOrderedCharter-82

# Build brief — PLAY-dOrderedCharter-82

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's close. The third close bar over `8ecef2cf1` failed five legs; one is a product red,
  PLAY-dOrderedCharter-81's matrix change leaving the `govkit acceptance matrix` leg importing fourteen files outside its guard,
  and this micro-spec fixes it. The rest are not this unit's: memory hygiene was the main loop's records, fixed at `824887660`;
  the policy check is inherited from the merge base; the dead-path hit on gov's install receipt is the lander's to rewrite; the
  instruction-edits red was a `database is locked` collision on the shared index.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-82`, its trailer block carrying `Pass: PLAY-dOrderedCharter-82` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-11-build-PLAY-dOrderedCharter-82-ledger.md`; each line leads
  with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background. A stale codebase map needs the
  map generator's output; declare it.
- Gov's guarded `.governance/` files other than `policy.toml` refuse an agent's commit; do not stage them.
- Run no gate leg, no suite, no bar.
