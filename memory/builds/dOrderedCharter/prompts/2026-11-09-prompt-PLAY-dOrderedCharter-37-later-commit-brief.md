**Serves:** journal PLAY-dOrderedCharter-37

# Build brief — PLAY-dOrderedCharter-37, its later commit

You build the later commit unit 37's spec defers in its section 8 F8, F10 and F11. Unit 37's first pass is CLOSED at `19648821f`;
this pass lands only what waited for PLAY-dOrderedCharter-40's unit rows to be tracked.

## What this pass lands

- The units `[[reference]]` row in `tools/playbook/references.toml`, its page under `help/reference/`, and every row's `unit` field
  (F10). The units row carries an `h1` like the three rows unit 40 gave one, or the tags leg's purpose check reds: spec 40 rev-4's
  F4 states why. Spec 37 does not say so; record it as a deviation.
- The unit-line check and every page's unit line (F11, S8).
- The `unit-usage` class's `[[class]]` rows in `tools/govkit/surface-classes.toml` and `tools/govkit/usage.toml` (F8).
- Observe AC1's four-page half, AC8 and AC10's `unit-usage` half, and append them to unit 37's acceptance ledger,
  `memory/builds/dOrderedCharter/build/2026-11-02-build-PLAY-dOrderedCharter-37-ledger.md`, as lines naming this pass.

## What the main loop needs from your commit

- One pass commit, its subject naming `PLAY-dOrderedCharter-37` and the later commit, its trailer block carrying
  `Pass: PLAY-dOrderedCharter-37` beside the attribution trailer. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dOrderedCharter/RUN.md` with the pass, since `--brief` and `--dispatch` stage rows in it.
- Move spec 37's status to `INPROGRESS` before your first product write and commit it only as `CLOSED`; add a section 9 line only
  where the spec's own text changes. Commit every file `gen_build_index.py --write` rewrites.
- A departure from the spec is a `deviation` record committed with the pass. Bump no kit version.
- A file on the kickoff manifest's `watch:` list needs the manifest re-stamped in the same commit; a stale codebase map needs the map
  generator's output committed with the pass. Declare both in `--dispatch` when you touch them.
- Run no gate leg, no suite, no bar. Before committing, run `python tools/playbook/check_layers.py`,
  `python tools/playbook/core.py meta-check` and `python tools/playbook/gov_tag.py check`, and add no red of your own.
