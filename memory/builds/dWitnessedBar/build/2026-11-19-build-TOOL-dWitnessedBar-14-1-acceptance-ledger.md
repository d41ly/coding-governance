# TOOL-dWitnessedBar-14 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-14

This pass ran no merge bar, no self-test suite and no gate leg except the naming lexicon's
`--suggest`. Every criterion below was checked on node d on 2026-11-19 by the unit's own CLI or a
`python -c` probe of the changed code, in the worktree or in a scratch clone under `%TEMP%` carrying
the pass's diff. `ratchet.py --fixture` ran whole once, before its legs were manifest rows; after that
the role hook refused the legs' own argv, so the AC7 plant is a `python -c` probe of
`run_keys_not_scalar`. Still owed to the close: the RED-first observation of the `New arm:` line in
spec section 7 (`ratchet selftest`, its failing cases staged by `gain`, `gain-refused`, `laundering`,
`rename` and `home-moved`), every leg that section names, and the nine new legs as bar rows.

**Evidences:** TOOL-dWitnessedBar-14
- AC1 — `never-gains` — `--fixture --plant gain` exits 1 printing `fix-pop · gained · b`, and again for a
  swapped key at an equal count; `ceiling-raised` exits 1 printing `above ceiling · a`; `append-edited`
  exits 1 printing `edited · a`.
- AC2 — `gain-widened` — the door wrote the record and the row, and with the record tracked
  `never-gains` exits 0 printing `admitted by`; with its Reason emptied it exits 1 `not admitted`; a
  `widened:` row naming no tracked record exits 1. `gain-refused` under `refuse`: a widened row whose
  record is new exits 1 `is refuse`, `ratchet.py widen` exits 2 writing no record and no row, and a
  widened row whose record the base commit tracks exits 0. `ceiling-widened`: the door raises a ceiling
  row and `never-gains` exits 0 with no `above ceiling` line.
- AC3 — `both-ways` — a measured key with no row and a row no seed finds exit 1 printing
  `undeclared site · c` and `unmeasured row · b`; another leg's registration prints
  `graded by other leg`, its planted seed never ran (no `ran.txt`), exit 0; with no registration
  naming the leg it exits 0 printing `unarmed · ratchet (both ways) · no registration names this leg`
  and no pass line.
- AC4 — `unarmed-green` — a home holding the failed seed's `# unarmed` line and a row exits 1
  `reads armed`; `populated-empty-armed` exits 1 printing
  `fix-pop · empty · reads unarmed, no seen-red reader`, no seen-red record in the fixture.
- AC5 — `laundering` — a re-dated row, a disposition turned back to `seeded` and a re-dated null-SHA row
  exit 1 naming `alpha`, `beta` and `nul`; a row drained because its seed no longer measures it exits 0;
  a row removed while its seed still measures it exits 1. Deviation 143 records (DERIVED) the seed run.
- AC6 — `rename` — a staged `git mv src/x.sh src/y.sh` with its rows re-keyed exits 0; the rows left
  on the old path exit 1 printing `rename src/x.sh -> src/y.sh`.
- AC7 — `keys-not-scalar` — on the built tree, before the leg was a manifest row, it exited 0 printing
  nine `held` rows (PINNED 2026-11-19, measured at `53307674f`); in the clone with `FOO_PIN="3"` appended
  to `.memory-tree.conf`, `run_keys_not_scalar` returned 1 printing
  `undeclared site · .memory-tree.conf` and `FOO_PIN`, TAB-joined. `--measure` exits 0 printing the nine TAB rows, and
  `python tools/lib/legacy_ledger.py read conf-scalar-pins` prints the nine rows `seed --population
  conf-scalar-pins` wrote (`armed conf-scalar-pins 9`).
- AC8 — `key-shape` — `--fixture --plant key-number` exits 1 naming `412`.
- AC9 — `untouched-quiet` — a baselined offence outside the unit's hunks exits 0, an unbaselined one
  planted there exits 1 `gained · src/new.sh`; under `merge` two branches each draining one row merge
  through `merge-rows.sh` to the one row `c`, and `never-gains` and `both-ways` each exit 0.
- AC10 — `pack` — the criterion's own `python -c` over `tools/gate-legs.json` printed the nine legs,
  each paired with `('feature.memory-tree-hygiene',)`.
- AC11 — `--print-bindings` — in the clone, `ratchet.py widen conf-scalar-pins` wrote
  `2026-11-19-build-TOOL-dWitnessedBar-14-widen-1.md`; committed, `gen_build_index.py --print-bindings`
  run in `tools/memory-tree/` printed its `S` row with kind `widen` and no `A` row.
- AC12 — `new-population` — `never-gains` and `seed-laundering` each exit 0 printing `new at` and
  `2 rows`; `home-moved` exits 1 printing `unresolved`. On the built tree both legs printed
  `conf-scalar-pins · new at 9e21ac760dc0 · 9 rows`.
