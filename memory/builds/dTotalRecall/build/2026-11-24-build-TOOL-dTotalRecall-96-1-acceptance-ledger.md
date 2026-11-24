# TOOL-dTotalRecall-96 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-96
**Caused-by:** TOOL-dTotalRecall-96

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-2 over
base `543895ec97bac428141c9be3a6e53f77cdd9c5f0` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The classifier, the fixture and the answer's loop are §4's fences, `c5_input` is spec 97 rev-2 §4's and the probe spec
93 rev-2 §4's, each extracted verbatim into a file under the scratch directory and sourced from the repository root.

Read before the first edit: the checker is the blob `c34c4a8cb300871245f1726d77512f997447d634` at `f7011dd6f`, at
`ff3c1b93a`, at `b59778f81` and at the base, and its refusals stand there as §1 cites them (DERIVED 2026-11-24,
`git rev-parse <rev>:<path>` and a read of that blob).

§4's fixture, read by `c5_of` (DERIVED 2026-11-24, that run):

| Label, shallow | Printed (DERIVED 2026-11-24) |
|---|---|
| `p69`, false | `p69 C5 passed` |
| `p69^`, false | `p69^ C5 failed` |
| `q`, false | `q C5 not-evaluated rc=2` |
| `r`, false | `r C5 not-evaluated check-2` |
| `s`, false | `s C5 passed` |
| `t`, false | `t C5 not-evaluated check-3` |
| `x`, false | `x C5 not-evaluated rc1-no-failure-line` |
| `z`, false | `z C5 not-evaluated contradictory` |
| `w`, false | `w C5 not-evaluated contradictory` |
| `v`, false | `v C5 not-evaluated unplaced 1` |
| `none`, false | `none C5 not-evaluated no-status-line` |
| `p69`, true | `p69 C5 not-evaluated shallow` |

A failure line whose dash is the byte `97` hex, no UTF-8, under a status of 1 read `passed` as its check-9 line asks
(DERIVED 2026-11-24, that run), so the encoding fold of rev-2 holds.

§4's answer over unit 80's ledger, the `c5_input` output for `p69` then `p69^` (DERIVED 2026-11-24, that loop at the base):

```text
p69 rc=0
p69 unplaced 0
p69^ rc=0
p69^ unplaced 0
```

The verdict can move. Over scratch copies of that ledger whose `p69` status line was altered, the same loop body
printed for label `p69` `not-evaluated rc1-no-failure-line` at a bare status of 1, `not-evaluated contradictory` for a
status of 0 beside a check-5 line and for two status lines, `not-evaluated unplaced 1` for a bullet of two reads,
`not-evaluated no-status-line` with the line deleted, `failed` at a status of 1 with a check-5 line, and `passed` at a
status of 1 with a check-9 line alone; an empty path made `c5_input` exit 1 (DERIVED 2026-11-24, these runs).

**Evidences:** TOOL-dTotalRecall-96
- AC1 — `c5_of "$SCRATCH/c5in96.txt" <label> false` — printed the verdict §4 pins for every label, the table above, among them `x C5 not-evaluated rc1-no-failure-line` and `z C5 not-evaluated contradictory` (DERIVED 2026-11-24, that run).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-96" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone once it was written. `LEDGER80` held `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-80-1-acceptance-ledger.md`. The `c5_input` output is the fenced block above: `p69 rc=0` and `p69 unplaced 0`, then `p69^ rc=0` and `p69^ unplaced 0`. The shallow value is `false`. `c5_of` printed `p69 C5 passed` and `p69^ C5 passed`. Unit 69's AC1 is answered GREEN at pass(69), from the `p69` verdict `passed`, a read whose one status agrees with its having no failure line. Unit 91's answer beside it is GREEN, from the same read; the two agree. The parent read passed too (DERIVED 2026-11-24, these commands).
- AC3 — `has_deviation memory/builds/dTotalRecall/build 91 'audit-89 id 12 s3'` — printed 0 before any write, and 0 for units 69 and 80 with that token; unit 91's answer does not differ, AC2 is resolved and names no parse failure, so no record is owed, none is written, and all three print 0 after the pass. `has_deviation memory/builds/dTotalRecall/build 69 'audit-77 id 23 s4'` printed 0. With no token it printed 1 for units 91 and 69 and 2 for unit 80, and with `spec changed at` 1 for unit 70, so the zeros are no unmovable probe (DERIVED 2026-11-24, these runs).
