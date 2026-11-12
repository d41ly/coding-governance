**Serves:** journal PLAY-dOrderedCharter-33

# Build brief — PLAY-dOrderedCharter-33, its later commit

You build the later commit unit 33's spec defers in its section 8 F5. Unit 33's first pass is CLOSED; this pass lands only what
F5 holds back until a gov unit row is tracked, which PLAY-dOrderedCharter-40's pass now gives.

## What this pass lands

- S5's `unit` class row in `tools/govkit/surface-classes.toml`, its reader, plant and witness as S5 names them, and the class's
  `[[class]]` row in `tools/govkit/usage.toml`, usage shape `none`, with the `why` S5 gives. Nothing else of unit 33.
- Observe unit 33's AC7 and AC11 against the tree with unit 40's rows tracked, and append those observations to unit 33's acceptance
  ledger, `memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-33-ledger.md`, as lines naming this pass.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-33` and the later commit, its trailer block carrying
  `Pass: PLAY-dOrderedCharter-33` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move spec 33's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`; add a section 9 line only
  where the spec's own text changes. Commit every file `gen_build_index.py --write` rewrites.
- A departure from the spec is a `deviation` record committed with the pass. Bump no kit version.
- A file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit; a stale codebase map needs the map
  generator's output committed with the pass. Declare both in `--dispatch` when you touch them.
- Run no gate leg, no suite, no bar. Before committing, run `python tools/playbook/check_layers.py` and
  `python tools/playbook/core.py meta-check` and add no red of your own.
