# TOOL-dTrackedAtlas-11 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-11

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command from the worktree root, with `$PY`, `$ATLAS`, `$TPL` and `$L1` set as section 5 sets them and the
probe `argv_readers.py` in the run's scratch directory. Each red ran the generator before this unit, the
blob at the pass's base `2a9ddae08`, from a scratch copy compiled in memory under the generator's own path
so its `HERE` and `REPO` resolved as the tree's do; the AC4 red ran a scratch copy of the pass's generator
with the one staged line its red names. No tracked file was edited to stage a red, and no ref was written.

**Evidences:** TOOL-dTrackedAtlas-11
- AC1 — `"$PY" argv_readers.py "$ATLAS"` printed `read_options`, and `VALUED_OPTIONS` reads
  `--page --ref --claims --plant --out`. Red: the probe over the generator at `2a9ddae08` printed `main`.
- AC2 — for each of `--ref`, `--claims`, `--plant` and `--out`, both `--check "$o"` and `"$o" --check`
  exited `1` within seconds with `0` bytes on stdout and the one stderr line `atlas: $o takes a value`,
  no `Traceback`; the whole AC1 to AC3 sweep took `2` s (PINNED, this pass). Red: the generator at
  `2a9ddae08` ended `--check --ref`, `--check --claims` and `--check --plant` each in a `Traceback`
  whose last line read `IndexError: list index out of range`; `--ref --check` read
  `atlas: --ref takes a revision, not --check`, and `--check --out` and `--out --check` each exited `0`
  with the `atlas: derived —` line, the bare `--out` never refused.
- AC3 — `--check --page "$TPL" "$o"` for each of `--ref`, `--claims`, `--plant` and `--out` exited `2`
  with `0` bytes on stdout and the one stderr line `atlas: cannot check: $o takes a value`, and
  `--check --page` exited `2` with `atlas: cannot check: --page takes a value`. Red: the generator at
  `2a9ddae08` answered the bare `--ref` and the bare `--page` with
  `atlas: cannot check: --page takes a page path and runs with --check and an optional --ref alone`, and
  each of the other three with that line ending `, not <the option>`.
- AC4 — `--check --page "$TPL" --ref HEAD` exited `1` with
  `atlas: unstamped — memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html: its data carries no stamp`;
  `--check --page "$TPL" --plant view-unread` exited `2` with the mixed-option line ending `not --plant`;
  `--check --claims maybe` exited `1` with `atlas: --claims takes cache or none, not maybe`; and
  `--check --claims none` exited `0` with its one line
  `atlas: derived — 264 records, 4594 sections, 220 decision sections, 16 comparison areas, 42 principles`
  in `27` s (PINNED, this pass). Red: a scratch copy whose `read_options` stores `argv[at - 1]`, the
  option's own position, refused `--check --claims none` with `atlas: --claims takes cache or none, not --claims`,
  exit `1`, and `--check --page "$TPL" --ref HEAD` with `atlas: cannot check: --ref takes a revision, not --ref`,
  exit `2`.
- AC5 — `grep -n "gains .predecessors." "$L1"` printed nothing, `grep -n "derive_predecessors" "$L1"`
  printed the one `Cleared since:` line beneath the owed line, and the `^def derive_predecessors` grep over
  the build-state module printed one line. Red: the ledger at `81cfc29dc` printed its line `56` for the
  first grep and nothing for the second.

S4's pane observations are not this unit's: by the spec's §4 "The pane observations at the close" the main
loop makes them at the close and records them in ledgers 2 and 3. This pass made none and claims none.

Owed to the close: the plain bar, whose legs section 6 names, and S4's two pane observations. No suite arm
is added, so no `New arm:` observation is owed.
