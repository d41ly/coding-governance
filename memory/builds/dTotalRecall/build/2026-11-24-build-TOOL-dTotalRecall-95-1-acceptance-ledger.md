# TOOL-dTotalRecall-95 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-95
**Caused-by:** TOOL-dTotalRecall-95

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-2 over base
`5d0ce047a7f2e41501fee11b3f541ff82406c4f6` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.
`key59`, its two runs and the fixture are §4's fences and `has_deviation` is spec 93 rev-2 §4's. Each was extracted
verbatim from its spec into a file under the scratch directory and sourced. `PY` was unset, so each ran under `python`.

Read before the first edit (DERIVED 2026-11-24, at the base): the labelled-line strings and the guards' tokens of spec 90
rev-3 §4 bear out §4's key table, unit 59's row the only one with a token outside the recipe. Unit 90's ledger records
`s1-59` 1 and no record of unit 59, and unit 83's records S1 as 1 and none owed, so S3's and S4's writes stay cut.

| Run | Printed (DERIVED 2026-11-24, these runs) |
|---|---|
| first `key59 "$FX"` | `key59 missing` naming `-59-deviation-591` of the fixture, then `key59 1 0` |
| second `key59 "$FX"` | the same `key59 missing` line, then `key59 2 1` |
| third `key59 "$FX"` | `key59 1 1` alone |
| fourth, over a probe that returns non-zero | `key59 red the probe failed` alone |
| `key59 memory/builds/dTotalRecall/build` | `key59 0 0` alone |
| `has_deviation --paths memory/builds/dTotalRecall/build 59` | one `rec` line naming `-59-deviation-591`, then 1 |

Beside them, `key59` over the build folder with a probe whose Python raises printed `key59 red the probe failed` alone,
and over an empty folder `key59 0 0` (DERIVED 2026-11-24, those runs).

S3 and S4: no record of `TOOL-dTotalRecall-59` lacks the key and none names the departure, so the ledger names no
unowed record, no path is handed to `TOOL-dTotalRecall-89`, and this pass writes no record.

**Evidences:** TOOL-dTotalRecall-95
- AC1 — `key59` — over §4's fixture its four calls printed what §4's table pins: the `key59 missing` line with `key59 1 0`, the same line with `key59 2 1`, `key59 1 1` with no `missing` line, and `key59 red the probe failed` with no numbers (DERIVED 2026-11-24, that run).
- AC2 — `key59 memory/builds/dTotalRecall/build` — printed `key59 0 0` and no `missing` line, and `has_deviation memory/builds/dTotalRecall/build 59` with the string printed 0, before this ledger was written and again after. With no token `has_deviation --paths` there listed `memory/builds/dTotalRecall/build/2026-10-26-build-TOOL-dTotalRecall-59-deviation-591.md` and 1. `grep -l 'Caused-by:.. TOOL-dTotalRecall-95'` over the folder's `*-build-TOOL-dTotalRecall-59-deviation-*.md` files, that one file, listed nothing and exited 1; over the fixture it listed `-59-deviation-592`, so the zero is no unmovable probe (DERIVED 2026-11-24, these commands).
