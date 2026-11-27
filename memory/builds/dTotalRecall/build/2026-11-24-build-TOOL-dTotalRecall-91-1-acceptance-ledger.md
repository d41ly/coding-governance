# TOOL-dTotalRecall-91 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-91
**Caused-by:** TOOL-dTotalRecall-91

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-3 over
base `b13fe3c5eb8c0c78c85ce6108c5c176b86b58062` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The classifier, the fixture reads and the answer's block are spec 91 rev-3 §4's fences, and the probe is spec 93 rev-2
§4's, each extracted verbatim from its spec into a file under the scratch directory and sourced.

Read before the first edit (DERIVED 2026-11-24, a probe at the base): the parent of `f7011dd6f` is `ff3c1b93a`, the
checker is the blob `c34c4a8cb300871245f1726d77512f997447d634` at both, and the manifest carries its marker line at
each. The checker's refusals, its block parse, its range guard and its check-5 line stand at that blob as §1 cites them.

The classifier over copies of unit 80's ledger, each with its `p69` status line altered, printed for label `p69`
`not-evaluated rc=2` where the status was 2, `not-evaluated check-2` where a check-2 line stood under a status of 1,
and `not-evaluated no-status-line` where the line was deleted (DERIVED 2026-11-24, these runs), so AC2's verdict can
move off `passed` over the real ledger's shape.

**Evidences:** TOOL-dTotalRecall-91
- AC1 — `c5_of` — over §4's fixture reads with shallow `false`, labels `p69`, `p69^`, `q`, `r`, `s` and `t` printed `passed`, `failed`, `not-evaluated rc=2`, `not-evaluated check-2`, `passed` and `not-evaluated check-3`, label `none` printed `not-evaluated no-status-line`, and `p69` with shallow `true` printed `not-evaluated shallow`, the eight verdicts §4 pins (DERIVED 2026-11-24, that run).
- AC2 — `git rev-parse --is-shallow-repository` — printed `false` at the base. `LEDGER80` held one path, `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-80-1-acceptance-ledger.md`. Its reads are `p69 rc=0` and `p69^ rc=0`, with no failure line under either label; `c5_of` printed `p69 C5 passed` and `p69^ C5 passed`. Unit 69's AC1 is answered GREEN at pass(69), from the `p69` read, in which C5 ran and passed. Unit 80's answer beside it is GREEN, from the same read; the two agree. The parent read passed too, so no red preceded the pass (DERIVED 2026-11-24, these commands).
- AC3 — `has_deviation memory/builds/dTotalRecall/build 80 'audit-77 id 23 s4'` — printed 0 before any write, and 0 for unit 69 with that token; unit 80's answer does not differ and S3 is resolved, so no record is owed and none is written, and both print 0 after the pass. With no token it printed 2 for unit 80 and 1 for unit 69, and with `spec changed at` 1 for unit 70, so the zeros are no unmovable probe (DERIVED 2026-11-24, these runs).
