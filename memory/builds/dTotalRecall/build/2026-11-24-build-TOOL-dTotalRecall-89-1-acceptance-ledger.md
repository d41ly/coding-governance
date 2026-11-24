# TOOL-dTotalRecall-89 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-89
**Caused-by:** TOOL-dTotalRecall-89

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-3 over base
`dba20826707cfa087630079e4440705610fdfcc3` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The reads are §4's two fences, verbatim, with the first bash fence of unit 81 §4, unit 90 §4's `s1` fence and unit 93
§4's `has_deviation` fence sourced before them, each extracted from its spec into a file under the scratch directory.
`PY` was unset, so `has_deviation` ran under `python`.

§4's first fence, its lines in order (DERIVED 2026-11-24, that run at the base):

```text
s1-59 206422580b7363ab9582e37ffe7de7c25773a721 1 `absorbs` is absent
0
0
p83 39ffc882ed18d2f5234fe4b86739ca4175a1d656
rec memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md before-p83 9443f6b3d152b71fd88e9e9d1e8f01c5ab6536d8
```

§4's red reads (DERIVED 2026-11-24, that run; each `check_ancestry` line is shown by its verdict):

| Read | Printed (DERIVED 2026-11-24) |
|---|---|
| `check_ancestry` at `HEAD`, `462d20f3`, `deadbeef`, the red line | `before-p83`, `at-or-after-p83`, `red ancestry rc=128`, `ungraded p83 red 83 no pass commit` |
| the absent path | `at-or-after-p83 untracked` |
| `s1-999` | `red 999 no pass commit` |
| the scratch folder, the string, then the key | 1, then 0 |

S1, the arm: `s1-59` reads 1 at `206422580b7363ab9582e37ffe7de7c25773a721`, the arm of a count of 1 or more. Beside it,
`2026-11-24-build-TOOL-dTotalRecall-83-1-acceptance-ledger.md` records S1 as the same sha and 1, and
`2026-11-24-build-TOOL-dTotalRecall-90-1-acceptance-ledger.md` its `s1-59` line as the same sha and 1
(DERIVED 2026-11-24, the read and the two ledgers).

S2, the population: no live record of `TOOL-dTotalRecall-59` names the string and none names the key, so no record is
listed, none lacks the key and none is counted. The one walk line is the roster record's, which is the walk's liveness.
Unit 88's S19 read, run again, listed nothing, exit 1, and with `roster` for the pattern the roster record alone, as its
ledger records (DERIVED 2026-11-24, the fence and both greps).

S3: the fourth row of §4's table holds, S1 1 or more and S2's count 0, so AC13 is green, none owed and none written. No
record is named fabricated. S4: none is owed, so this pass writes no record of unit 59. S5: unit 88's ledger answers AC13
on the same arm, "the arm that wants no record of unit 59", with none listed and nothing merged, so the two answers
agree, no record of unit 88 is owed and none is written (DERIVED 2026-11-24, that table and that ledger).

**Evidences:** TOOL-dTotalRecall-89
- AC1 — `s1-59` — led exactly one line, the sha and the count 1 that §4 pins; the two `has_deviation` calls printed one count each, 0 and 0; `p83` printed `39ffc882ed18d2f5234fe4b86739ca4175a1d656`, the commit `pass_of 83` printed when called alone; and the walk printed one line, `2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md` `before-p83`, for the one live record of unit 59. Every red read printed what §4 pins for it (DERIVED 2026-11-24, those runs).
- AC2 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-89" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone once it was written. S1's arm is 1 at `206422580b7363ab9582e37ffe7de7c25773a721`, beside unit 83's S1, the same sha and 1, and unit 90's `s1-59` line, the same sha and 1. S2's two counts are 0 for the string and 0 for the key. No record is counted, so no counted path, verdict or adding commit stands; the walk's one record is `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md`, `before-p83`, added at `9443f6b3d152b71fd88e9e9d1e8f01c5ab6536d8`. Unit 88's S19 list is empty. AC13 is green by the fourth row of §4's table. After this ledger was written `has_deviation` for unit 59 with the string printed 0 again. The grep for this unit as the cause, over the one `*-build-TOOL-dTotalRecall-59-deviation-*.md` file, listed nothing, exit 1; with `PLAY-dClosedLoop-2` it listed the roster record, exit 0 (DERIVED 2026-11-24, these commands).
- AC3 — `has_deviation memory/builds/dTotalRecall/build 88 'audit-77 id 1 s5'` — printed 0, the two AC13 answers agreeing, before this ledger was written and again after; with no token it printed 2 for unit 88, so the 0 is no unmovable probe (DERIVED 2026-11-24, these commands).
