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
- Clear the three reds unit 37's first pass left, which the main loop observed after `19648821f`: the layers check reds the
  renderer's probe of the docs leg (`tools/playbook/render_playbook.py#read_fingerprint_lines`), since core kit `playbook-render`
  depends on non-core kit `govkit` with no optional descriptor row naming the file; and the core meta-check reds the legs `help
  reference pages` and `help page commands`, which carry no `enforces` and no pending row. Name the principles each leg enforces,
  or a pending row with its arming build, and resolve the layer edge within the kit descriptors' own grammar. Record each as a
  deviation.
- Fix `tools/playbook/render_playbook.py#write_unit_usage_plant` before registering its class: it removes a row with
  `replace(u.body, ...)`, but `read_units` yields LF bodies while the step gate's fixture clone checks out CRLF, so the plant removes
  nothing and the gate reads 0 vanished. PLAY-dOrderedCharter-33's later commit `4dd011712` fixed the same defect in
  `tools/playbook/pins.py#write_unit_plant` (its deviation 336): match the body in the file's own line endings and raise naming the tag
  when it is not found. Record it as a deviation.
- Bring `help/step-gate.md`'s class table current: it lists neither `unit` (unit 33's later commit), nor `drive` and `kind` (unit 37's
  first pass), nor the `unit-usage` class this pass registers.

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
