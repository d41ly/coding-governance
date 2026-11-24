**Serves:** journal TOOL-dBoundRoles-62

# TOOL-dBoundRoles-62 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on its worktree
before the pass commit at base `9eb0630c9`. No gate, suite or bar ran in the pass: the suite's executed count against
the floor, the arm the spec declares with its RED-first observation on a floor one above the executed count, and the
legs the spec's gate line lists, the testsuite-counts leg beside them, are owed to the main loop at the close. Both
specs this unit restates are CLOSED, so the restated text is the After field of
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-62-deviation-623.md`, and a criterion that greps a
frozen spec is answered AMENDED, by `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md`.

## Items a landed unit had already left

- S1: unit 43's pass left no floor, its AC27 standing OWED, so the fallback branch applies and all four parts are added.
- S4: unit 60's pass left unit 58's frozen arm line as it stood; deviation record 623 restates it, and unit 58's ledger
  is untouched, no criterion of that unit changing.

**Evidences:** TOOL-dBoundRoles-62
- AC1 — `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$'` — AMENDED by `TOOL-dBoundRoles-64`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-64-deviation-643.md`: the floor's shape is read through `compliant`, and the scratch-shell halves stand; each read the same on the built tree. Over `tools/roles/spawn-guard.test.sh` it printed 1 (DERIVED on the staged tree). A scratch shell sourcing only the floor line and the comparison line, both copied out by `grep`, printed `FAIL executed 193 assertions against a floor of 194` with the count one below and nothing with it equal. `tools/check-testsuite-counts.sh#compliant`, cut out and called alone, returned 0 on the suite and 1 on a copy with the floor line deleted. OWED: `spawn-guard self-test` and the arm's RED-first observation at the close.
- AC2 — `python -c` — AMENDED by `TOOL-dBoundRoles-64`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-64-deviation-643.md`: a term also names `TOOL-dBoundRoles-50`. On that unit's staged tree the probe read the comment block above the floor: base 187, on which `TOOL-dBoundRoles-43` stands, and the terms, `+1` naming `TOOL-dBoundRoles-50` and `+6` naming `TOOL-dBoundRoles-58`, sum to the floor's 194 (DERIVED). A scratch shell sourcing the floor and comparison lines alone printed the failure line with the count at the floor less unit 50's term. The call-site count is 182 and the executed count 194 (DERIVED from source at the pass): three loops assert, the `--only=` loop over four items, the direct spawns over six and the refused spawns over five, every helper asserts once per call, and no arm has a skip branch. Six `BR58` rows are unit 58's, one per execution. OWED: the executed count of the suite's run against the floor at the close.
- AC3 — `FLOOR_ASSERTIONS` — AMENDED by the main loop's decision, item 4: spec 60 is frozen, and a probe cutting S24 and AC15 out of deviation record 623's text for `TOOL-dBoundRoles-60@rev-9` found both suites by path in each, with a red for a suite holding no `FLOOR_ASSERTIONS` line; AMENDED again by `TOOL-dBoundRoles-64`, whose `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-64-deviation-643.md` has AC15 name units 52, 53, 58, 59, 60 and 61 for the adopter suite, with no condition, and units 50 and 58 for the spawn guard's; the record stands for the revision-log line naming `TOOL-dBoundRoles-62`. The restated AC15's name halves hold on the tree: each of those units stands in a `+<n>` term of its suite.
- AC4 — `grep -n '^New arm: .*spawn-guard'` — AMENDED by the main loop's decision, item 4: spec 58 is frozen and its line still ends in `none`; deviation record 623's text for `TOOL-dBoundRoles-58@rev-7` names `FLOOR_ASSERTIONS` after its last `·`.
