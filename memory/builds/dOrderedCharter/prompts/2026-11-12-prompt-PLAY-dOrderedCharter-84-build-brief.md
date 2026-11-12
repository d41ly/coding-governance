**Serves:** journal PLAY-dOrderedCharter-84

# Build brief — PLAY-dOrderedCharter-84

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's close. The owner ruled on 2026-11-12 that no file is owner-only to a run under its mandate
  (`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-guard-ruling.md`). This unit is the guard's
  half: `tools/policy/guard.py` admits a guarded change committed on a live run's branch.
- Its sibling PLAY-dOrderedCharter-85, the lander's merge fold, builds in parallel in this same worktree. The two share no file:
  never stage or touch a path of spec 85's, and expect its commits to appear on the branch while you work.
- Spec 84's AC6, the run's own guarded commit, is the main loop's to observe after both units close.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-84`, its trailer block carrying `Pass: PLAY-dOrderedCharter-84` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-84-ledger.md`; each line
  leads with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background. A stale codebase map needs the
  map generator's output; declare it.
- Gov's guarded `.governance/` files refuse an agent's commit until this unit lands; do not stage them.
- Run no gate leg, no suite, no bar.
