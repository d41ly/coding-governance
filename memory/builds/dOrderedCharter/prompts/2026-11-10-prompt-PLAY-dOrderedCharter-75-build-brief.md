**Serves:** journal PLAY-dOrderedCharter-75

# Build brief — PLAY-dOrderedCharter-75

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's build run. Unit 75 was added after PLAY-dOrderedCharter-40's pass `c91c26904` left the tags leg red on 42
  declared selectors; spec 40 is CLOSED, so this unit lands the correction on top of it.
- Every unit your spec depends on is built and committed on this branch. PLAY-dOrderedCharter-31 is parked and will not land in this
  run; nothing you build may rest on it.
- Where the tree moved since your spec's base, the code at this branch's HEAD is the truth, and a difference that changes what you
  must build is a DIVERGENCE; a small mechanical mismatch within the spec's stated intent is a recorded deviation.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-75`, its trailer block carrying `Pass: PLAY-dOrderedCharter-75` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write, since the write gate refuses a DEFERRED spec, and commit it
  only as `CLOSED`. Commit every file `gen_build_index.py --write` rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-75-ledger.md`, one line per AC
  with the probe you ran and what it printed, committed with the pass. A departure from the spec is a `deviation` record.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path: each call takes about ten minutes here.
- A stale codebase map needs the map generator's output committed with the pass; declare it. Bump no kit version.
- Run no gate leg, no suite, no bar. The tags leg's check is the main loop's to observe after your pass: your role may not run it.
