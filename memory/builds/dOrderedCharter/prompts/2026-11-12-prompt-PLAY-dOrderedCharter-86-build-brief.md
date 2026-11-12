**Serves:** journal PLAY-dOrderedCharter-86

# Build brief — PLAY-dOrderedCharter-86

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's close. The close leg list over `948b91720` failed six legs; two are product reds this micro-spec fixes.
  The rest are not this unit's: memory hygiene was the main loop's records, fixed at `1f82d4bdc`; the dead-path hit on gov's
  install receipt is the lander's to rewrite; instruction edits hit `database is locked` on the shared index; and the held-leg
  budget leg read a filtered leg list the close will not use.
- Where a fixed leg hits a later refusal, hand it back as a deviation rather than widen the fix.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-86`, its trailer block carrying `Pass: PLAY-dOrderedCharter-86` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-86-ledger.md`; each line
  leads with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map generator's
  output; declare both.
- Run no gate leg, no suite, no bar.
