# TOOL-dTotalRecall-93 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-93
**Caused-by:** TOOL-dTotalRecall-93

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-2 over base
`fce47ddedbfc98cfc3a8fb90df0d983154d22e53` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
The probe is §4's fence and unit 90's is spec 90 rev-3 §4's, each body extracted verbatim from its spec into a file under
the scratch directory and sourced. `PY` was unset, so each ran under `python`.

Read before the first edit (DERIVED 2026-11-24, a probe at the base): `_ID.pattern` equals the text of
`tools/memory-tree/build_records.py#ID`; `_ID` joined to a string raises `TypeError`; every one of the folder's 150
deviation records has a stem and a Serves line naming one unit, 72 depart from their own unit and none from another unit
of this build (DERIVED 2026-11-24, that read). Both probes' rows of §4's unit table read as pinned (DERIVED 2026-11-24).
Unit 90's key reads 0 for 46 of the 89 units holding a live record and the right count for 17 (DERIVED 2026-11-24).

S4: each guard unit 90's AC2 ledger line names, in its order, run again over the build folder:

| Unit | Token | Unit 90 recorded (DERIVED 2026-11-24, its ledger) | New key (DERIVED 2026-11-24, this pass) | Owed by a decision |
|---|---|---|---|---|
| 67 | `TOOL-dTotalRecall-56` | 0 | 0 | no |
| 59 | `` `absorbs` is absent `` | 0 | 0 | no |
| 70 | `SUFFIX_RE` | 0 | 0 | no |
| 74 | `s1-59` | 0 | 0 | no |
| 74 | `SUFFIX_RE` | 0 | 0 | no |
| 83 | `audit-77 id 22 s1-59` | 0 | 0 | no |
| 84 | `audit-77 id 22 s1-46` | 0 | 0 | no |

Unit 90's ledger, `2026-11-24-build-TOOL-dTotalRecall-90-1-acceptance-ledger.md`, owes no record by any decision. No row
counts two live records, so this pass writes no owed record and no correcting record. With `spec changed at` for the
token, units 70 and 83 print 1 each under the new key and under unit 90's, so the zeros are no unmovable probe
(DERIVED 2026-11-24, that run). Unit 59 with `pass(59)` prints 0 under both (DERIVED 2026-11-24, that run).

The scratch folder of AC2, each record a copy of `2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md` under its new stem,
read by this probe and by unit 90's, unit then count (DERIVED 2026-11-24, these runs):

| Folder | This probe, 59 | This probe, 89 | Unit 90's, 59 | Unit 90's, 89 |
|---|---|---|---|---|
| the three records (DERIVED 2026-11-24) | 2 | 1 | 1 | 0 |
| and the correcting record of the second (DERIVED 2026-11-24) | 1 | 1 | 1 | 0 |
| and `note-deviation-x.md`, departing from unit 59 (DERIVED 2026-11-24) | 1 | 1 | 2 | 0 |

With no token, units 590 and 5 print 0 over that folder and unit 59 prints 0 over an empty one. Run where the tree's
`tools/memory-tree` does not resolve, the probe prints no count and exits non-zero (DERIVED 2026-11-24, these runs).

**Evidences:** TOOL-dTotalRecall-93
- AC1 — `has_deviation memory/builds/dTotalRecall/build <n>` — the loop over the 89 units a record's stem names, with 10 and 590, ran in the background at the base. Each unit's count was set beside its `ls` of 150 stems less the 3 that a `**Supersedes:**` line names, 147 in all, and the loop ended `loops 91 bad 0`. Units 10 and 590 printed 0 beside 1 for unit 100 and 1 for unit 59. Unit 90's key, read in one process over the same records, gives 0 for 46 of the 89, so the comparison can fail (DERIVED 2026-11-24, these runs).
- AC2 — `has_deviation --paths` — over the three-record folder, for unit 59 and `pass(59)`: two `rec` lines, the paths of `-59-deviation-9001` and `-59-deviation-9002`, then 2; for unit 89, one `rec` line, the path of `-89-deviation-9003`, then 1 (DERIVED 2026-11-24, that run). Unit 90's probe printed 1 and 0 there (DERIVED 2026-11-24).
- AC3 — `git grep -l "consumes-from\*\* .TOOL-dTotalRecall-93." -- memory/builds/dTotalRecall/spec` — listed the specs of units 89, 91, 92, 94, 95, 96, 99 and 100 and no other. `git grep -lE "has_deviation|unit_of" -- memory/builds/dTotalRecall/spec` listed those and the specs of units 90, 93 and 98, and spec 98 consumes unit 92 (DERIVED 2026-11-24, these commands at the base).
- AC4 — `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-93" -- memory/builds/dTotalRecall/build` — printed this ledger's block line alone. Each guard beside its count, unit 90's recorded and then the new key's, no row owed: 67 `TOOL-dTotalRecall-56` 0 and 0, 59 `` `absorbs` is absent `` 0 and 0, 70 `SUFFIX_RE` 0 and 0, 74 `s1-59` 0 and 0, 74 `SUFFIX_RE` 0 and 0, 83 `audit-77 id 22 s1-59` 0 and 0, and 84 `audit-77 id 22 s1-46` 0 and 0 (DERIVED 2026-11-24, these commands).
