**Serves:** journal PLAY-dOrderedCharter-85

# Build brief — PLAY-dOrderedCharter-85

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's close. The run's `push-main.sh --prepare` stopped at its regeneration: the upgrade step
  `playbook/adopter-rules-to-overlay` wrote `.governance/instructions.toml` and `policy.py mirror --write` refused it uncommitted
  (`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-landing.md`). This unit is the lander's half
  of the owner's 2026-11-12 ruling: the prepare folds what its steps wrote before it regenerates.
- Its sibling PLAY-dOrderedCharter-84, the guard's run admission, builds in parallel in this same worktree. The two share no file:
  never stage or touch a path of spec 84's, and expect its commits to appear on the branch while you work.
- Spec 85's AC2 is this run's own `--prepare`, the main loop's to observe after both units close. Never run `--prepare` yourself.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-85`, its trailer block carrying `Pass: PLAY-dOrderedCharter-85` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-85-ledger.md`; each line
  leads with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map generator's
  output; declare both.
- Run no gate leg, no suite, no bar.
