**Serves:** journal TOOL-dSafePassage-88

# TOOL-dSafePassage-88 — acceptance ledger

The unit as built, at spec rev-2. Product writes: `tools/govkit/govkit.py` (S1: `_cmd_update`'s
`renamed` write arm gains `own_file`, asked through `samefile`, and `in_place`, by exact spelling;
the occupancy refusal runs only when `not own_file`, the staging lines and `git mv` only when
`not in_place`; an in-place row joins `changed`, prints an `in place` line, and its landing-failure
message names an in-place landing) and `tools/govkit/selftest.py` (S2: `build_rename_gov` gains `root`
and `src` with defaults that keep its four callers unchanged, and two `[dSP-88]` checks follow the
occupied-destination checks in the `DEPL-dCarriedReceipt-11` block). No function added, so
`memory/map/generated/symbols.json` is not regenerated.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1, AC3, AC4 and AC5 were
observed on node a (Windows 11, `git config core.ignorecase` reads `true`) from this worktree's root.
The §4 probe ran verbatim from the run's scratch; its `tempfile.mkdtemp(prefix="p88-")` fixture repos
went under `%TEMP%`, the short-path exception for fixture repositories, and were removed afterwards.

Owed at the close: AC2, the moved-clone walk, which needs the foreign-prefix leg's own
`set_tool_root` sourced out of `tools/run-gates/foreign-prefix.gov.test.sh` and the `upgrade-walk`
run (a suite slice a unit pass does not run); the RED-first observation of §7's `New arm:` line, the
two `[dSP-88]` checks staged red by the occupancy test kept unconditional and, on a case-insensitive
node, by the bare string test deciding the occupancy skip; and the §7 legs at the bar. The red
probes below ran against a scratch copy of the engine and do not discharge the arm's staged-break
observation inside the selftest.

**Evidences:** TOOL-dSafePassage-88
- AC1 — `python <scratch>/p88_probe.py` — its second line printed `update exit 0 | refused in place: False | bytes: FOUR | source: moved/demo/keep.txt | moved dir in target: False`. Against a scratch engine holding HEAD's (`ed22e3ef4`) `govkit.py` it printed `update exit 1 | refused in place: True | bytes: four | source: pinned/demo/keep.txt`, the red side. `update`'s output as built carried `  in place         [engine] pinned/demo/keep.txt · source moved/demo/keep.txt · bytes gov` and `wrote 2, moved 0`.
- AC2 — owed at the close (above); not observed in this pass.
- AC3 — the same run's last line printed `occupied refused: True | own file kept: True`, as built and against HEAD's engine.
- AC4 — `git grep -n -F "[dSP-88]" -- tools/govkit/selftest.py` — printed two lines, the two checks' labels, inside the `DEPL-dCarriedReceipt-11` block.
- AC5 — the same run's third line printed `case-only: update exit 0 | refused as its own occupant: False | receipt: ['pinned/demo/Keep.txt']`. With `own_file` reduced to the bare string test in a scratch engine copy it printed `case-only: update exit 1 | refused as its own occupant: True | receipt: ['pinned/demo/keep.txt']`, the red side; against HEAD's engine the same.

AC2 — observed at the close by the main loop, at this unit's commit `112e587ea`, in a `git clone --no-hardlinks` under the temp root moved to `scripts` by the foreign-prefix leg's own `set_tool_root` (`403df383e foreign-prefix: tool root at scripts, gov's declarations with it`). `FOREIGN_PREFIX_PROBE=1 python upgrade_walk.py --case up` from `scripts/govkit` printed `upgrade-walk: release-0 applied by the pinned clone's own apply over the fixture's kits line · exit 0 · receipt schema 3`, `upgrade-walk: pin 60d90cb71db51e651aa1c5efe3f6d48ba21a997d · landed ref 1a61f21a238c5d9364dd5c6e91ab0d8b805fcfa3 · tip a6cac7c5457d96d7ae8f841368377b09779551d7 · 3 step(s)`, `upgrade-walk: GREEN`, `foreign-prefix-probe: stopped after 1 arm` and `upgrade-walk: summary · … · up 1 passed 0 red · red lines 0 · … · 318 s`, exit 0 in 335 s. The `vendor/gov` and repo-root prefixes were not run, a non-goal of this spec.
