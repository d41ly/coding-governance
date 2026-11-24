# TOOL-dTotalRecall-94 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-94
**Caused-by:** TOOL-dTotalRecall-94

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-2 over base
`ea222030e1c3fcf4420873ba153f2a8c48fe941e` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The census, `scan_foreign` and the fixture are §4's fences, `has_deviation` is spec 93 rev-2 §4's and `has_deviation_90`
is spec 90 rev-3 §4's with its first line's name changed and nothing else, seen by `diff`. Each was extracted verbatim
from its spec into a file under the scratch directory and sourced, the runs at the foot of the first two fences made by
the runner. `PY` was unset, so each ran under `python`. No record was written between a census's start and its end.

Read before the first edit (DERIVED 2026-11-24, a probe at the base): the folder holds 150 deviation records, 72 of them
departing from their own unit, 65 from the build, 3 from a clause and 10 from a spec of another build, and none from
another unit of this build. `unattended.sh#verb_dispatch` reads `lib-unattended.sh#read_consumes_from` as §4 cites, and 150 stems match
the census's file pattern (DERIVED 2026-11-24, `ls` and `grep`).

The two censuses over the build folder, both run in the background at once (DERIVED 2026-11-24, these runs):

| Probe | `census` lines | File counts, summed | Probe counts, summed | `red census` lines |
|---|---|---|---|---|
| `has_deviation` (DERIVED 2026-11-24) | 89 | 147 | 147 | 0 |
| `has_deviation_90` (DERIVED 2026-11-24) | 89 | 147 | 72 | 72 |

Both censuses read the same unit set and the same file counts, and 17 units agree under `has_deviation_90`. Each took
238 s beside the other, and `scan_foreign` took 22 s (DERIVED 2026-11-24, by `time`). An empty folder prints no census
line (DERIVED 2026-11-24, that run).

The fixture's counts with the tokens `pass(59)` and `` `absorbs` is absent `` (DERIVED 2026-11-24, these runs):

| Probe | 59 | 5 | 89 | 61 | 590 | 59 after the superseding record |
|---|---|---|---|---|---|---|
| `has_deviation` (DERIVED 2026-11-24) | 2 | 1 | 1 | 1 | 0 | 2 |
| `has_deviation_90` (DERIVED 2026-11-24) | 1 | 1 | 0 | 0 | 0 | 1 |

`census "$FX" has_deviation` printed four `census` lines, units 5, 59, 61 and 89, and no `red` line, before the
superseding record and after it. `census "$FX" has_deviation_90` and `scan_foreign "$FX"` each printed `red census 59`,
`red census 61` and `red census 89` both times, and no other (DERIVED 2026-11-24, these runs).

S4: unit 90's AC3 answer is §4's first row. Its ledger records its fixture's 1, 1 and 2, spec 90 rev-3 §4's pins, with
a fourth state, 0 for the quoting ledger alone, which is no count of that criterion, and claims nowhere that the probe
counts every record of a unit. No record of `TOOL-dTotalRecall-90` is owed by it, and this pass writes none.

**Evidences:** TOOL-dTotalRecall-94
- AC1 — `census memory/builds/dTotalRecall/build has_deviation` — run in the background at the base, printed 89 `census` lines, at least the 89 of §4, and no `red census` line; its file counts sum to 147 and its probe counts to 147, the 150 record files less the 3 a `**Supersedes:**` line names (DERIVED 2026-11-24, that run).
- AC2 — `census memory/builds/dTotalRecall/build has_deviation_90` — printed 89 `census` lines and 72 `red census` lines. Sorted, they are `diff`-equal to the 72 lines of `scan_foreign memory/builds/dTotalRecall/build`, sorted, and `red census 59` is one of them, beside `census 59 probe 0 files 1` (DERIVED 2026-11-24, these runs).
- AC3 — `has_deviation "$FX" <n>` — over §4's fixture with the two tokens printed 2, 1, 1, 1 and 0 for units 59, 5, 89, 61 and 590, §4's first row; after the superseding record unit 59 printed 2. `census "$FX" has_deviation_90` printed `red census 59`, `red census 61` and `red census 89` alone (DERIVED 2026-11-24, these runs).
- AC4 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-94" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone. Unit 90's AC3 answer, of `2026-11-24-build-TOOL-dTotalRecall-90-1-acceptance-ledger.md`: "0 with the quoting ledger alone, 1 with the first record added, 1 with an uncommitted second record whose `**Supersedes:**` names the first, and 2 with that line taken out". Beside it, `census 59 probe 1 files 1` and `census 90 probe 1 files 1` under `has_deviation`, and `census 59 probe 0 files 1` and `census 90 probe 0 files 1` under `has_deviation_90`. §4's first row, no record: `has_deviation memory/builds/dTotalRecall/build 90 'audit-89 id 28 ac3'` printed 0 before the pass and 0 after. With no token it counts 1 for unit 90, so the zero is no unmovable probe (DERIVED 2026-11-24, these commands).
