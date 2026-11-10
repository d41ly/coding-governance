**Serves:** journal PLAY-dOrderedCharter-76

# Build brief — PLAY-dOrderedCharter-76

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dOrderedCharter's build run. Unit 76 carries the later commit PLAY-dOrderedCharter-37's spec deferred, plus unit 37's three
  lint reds, a CRLF fix to its plant and the step gate's help page. It became a unit of its own because reopening CLOSED spec 37 made
  its AC12 token live and `--dispatch` refused it.
- Every unit your spec depends on is built and committed on this branch: PLAY-dOrderedCharter-37 at `19648821f`, PLAY-dOrderedCharter-40
  at `c91c26904`, PLAY-dOrderedCharter-33's later commit at `4dd011712`, and PLAY-dOrderedCharter-75 at `8198bad3f`, which leaves the
  tags leg green. PLAY-dOrderedCharter-31 is parked and will not land in this run; nothing you build may rest on it.
- Where the tree moved since your spec's base, the code at this branch's HEAD is the truth, and a difference that changes what you
  must build is a DIVERGENCE; a small mechanical mismatch within the spec's stated intent is a recorded deviation.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-76`, its trailer block carrying `Pass: PLAY-dOrderedCharter-76` beside the
  attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move your spec's status to `INPROGRESS` before your first product write, since the write gate refuses a DEFERRED spec, and commit it
  only as `CLOSED`. Run `gen_build_index.py --write` after staging and commit every file it rewrites.
- Your acceptance ledger is `memory/builds/dOrderedCharter/build/2026-11-10-build-PLAY-dOrderedCharter-76-ledger.md`, one line per AC
  with the probe you ran and what it printed, committed with the pass. A departure from the spec is a `deviation` record.
- Declare your whole write set in ONE `--dispatch`, one `--writes` per path: each call takes about ten minutes here. A file on the
  kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output; declare both.
- Run no gate leg, no suite, no bar. The layers check, the core meta-check and the tags check are the main loop's to observe after your
  pass: your role may not run them.
