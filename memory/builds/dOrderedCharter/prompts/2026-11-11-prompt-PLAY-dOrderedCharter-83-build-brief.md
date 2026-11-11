**Serves:** journal PLAY-dOrderedCharter-83

# Build brief — PLAY-dOrderedCharter-83

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's close. Every roster unit through PLAY-dOrderedCharter-82 is CLOSED. The lander's
  `push-main.sh --prepare` refused: merging the run branch onto `origin/main` at `47ed57fab` conflicts in fifty files. This
  unit makes that merge on the run branch, by the sha, `--no-ff`, resolving each file as spec 83 disposes it.
- The spec writer resolved every disposition over a scratch copy of the trial tree `1f56beed`; its F1 is ratified on the owner's
  "take forks' recommendations": keep the drive row, and the main loop files the ask at the close.
- Re-take the conflict set at the merge and record any difference from the spec's in your acceptance ledger. A file whose
  disposition does not fit the bytes you find is a deviation record, never a silent choice.
- Where a re-render or a check reds on bytes the other side brought, hand it back rather than widen the unit: the main loop runs
  the legs after your pass and folds any red into one next unit.

## What the main loop needs from your commit

- The merge commit carries `Pass: PLAY-dOrderedCharter-83` beside the attribution trailer, its subject naming the unit, and the
  merge's two parents are the branch's pre-merge tip and `47ed57fab`. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before the merge and commit it only as `CLOSED`, in a follow-up records commit if the
  merge commit cannot carry it. Run `gen_build_index.py --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-11-build-PLAY-dOrderedCharter-83-ledger.md`; each line
  leads with a backticked token its criterion carries.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background. The kickoff manifest re-stamp
  and the codebase map's generator output are part of it.
- Gov's guarded `.governance/` files other than `policy.toml` refuse an agent's commit; the spec's S-item on the policy mirror
  says which side the merge keeps.
- Run no gate leg, no suite, no bar.
