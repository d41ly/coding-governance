# TOOL-dRankedPlan-5 deviation 51 — the live-build mapping covers every live build outside the chain, not only v1's rows

**Serves:** deviation TOOL-dRankedPlan-5

- **Departs from:** cl-dClosedLoop-0373@70fb5631
- **Hand-off:** design-to-spec
- **Before:** the mapping is "v1's table with one change" (v2:1787), the 24 rows of v1's live-build table (v1:147-177).
- **After:** the mapping's population is every build the plan view lists at the build run's base, less the 22 chain builds of v2's `[chain]` table, derived by TOOL-dRankedPlan-5 §8 F1's probe; at `0689e7fa1` that is v1's 24 rows plus `aScoutedSeam` and `dClosedLoop`, each of the two recorded `kept` since v1 names no chain build for it.
- **Cause:** design defect
- **Reason:** v1's table was written on 2026-10-14 and omits `aScoutedSeam`, opened 2026-10-11 and live at base, and `dClosedLoop`, the chain's own design build; mapping v1's rows alone would leave two live builds with no record, where the clause carries out the mapping of the live builds. Neither is absorbed, because no owner-approved row names an absorbing build for either.
- **Evidence:** `memory/LIVE.md` at `0689e7fa1` lists 46 builds; 20 are chain builds, 24 are v1's rows, and `aScoutedSeam` and `dClosedLoop` are the two remaining (`memory/builds/aScoutedSeam/README.md`, `opened: 2026-10-11`).
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of the harness's spec stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0373@70fb5631
- **Caused-by:** PLAY-dClosedLoop-4
