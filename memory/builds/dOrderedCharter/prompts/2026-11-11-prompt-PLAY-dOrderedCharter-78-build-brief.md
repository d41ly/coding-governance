**Serves:** journal PLAY-dOrderedCharter-78

# Build brief — PLAY-dOrderedCharter-78

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This unit builds the owner's picks for the three reds the close parked
  (`memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-1-owner-fork-picks.md`). It sits at order 37 and must
  land before PLAY-dOrderedCharter-49, which the dispatch order gate refuses until this unit is dispatched.
- Spec 78 is rev-1, written before PLAY-dOrderedCharter-31 and PLAY-dOrderedCharter-39 built. Unit 31 is CLOSED at `5e98256fe`: it
  retired the agent-instructions kit into `playbook-render`, added `playbook-render` to the default selection, and added the shared
  retired-kit reader `tools/lib/retired_kits.py`. Unit 39 is CLOSED at `ee40561c9`: it wrote the `agent-instructions wiring` leg back on
  gov's bar only. Section 8 F2's precondition, unit 31 CLOSED, holds.
- Read units 31 and 39's ledgers and deviations in `memory/builds/dOrderedCharter/build/` first. Where the spec names a line or a value
  either unit moved, build to the spec's stated intent over HEAD and record the difference as a deviation; hand back only what truly
  blocks the build.
- Unit 39's builder found govkit's selfcheck naming the `check-microformats` entry's `micro-format definitions` argv, which names a
  template `playbook-render` now ships. It is unit 31's area, not this unit's scope; name it in your return if your pass touches it.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-78`, its trailer block carrying `Pass: PLAY-dOrderedCharter-78` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`. Run `gen_build_index.py
  --write` after staging and commit every file it rewrites, the dClosedLoop as-built view and `memory/backlog/PLAY.md` among them.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-11-build-PLAY-dOrderedCharter-78-ledger.md`. A departure from
  the spec is a `deviation` record.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path, run in the background: the machine is shared and the verb
  has taken up to an hour. A file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale
  codebase map needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. The legs your criteria name are the main loop's to observe after your pass.
