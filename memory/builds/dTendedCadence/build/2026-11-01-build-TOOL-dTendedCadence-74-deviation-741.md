# TOOL-dTendedCadence-74 deviation 741 — a spec audit promoted a unit for its findings

**Serves:** deviation TOOL-dTendedCadence-74

- **Departs from:** dTendedCadence [roster]
- **Hand-off:** design-to-spec
- **Before:** dTendedCadence's roster carries eighteen units, `TOOL-dTendedCadence-1` to `TOOL-dTendedCadence-18`, one per clause of its row, beside `TOOL-dTendedCadence-19` and `TOOL-dTendedCadence-20`, the opening's asks in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dTendedCadence-74`.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the 19 MEDIUM and 7 LOW findings of memory/builds/dTendedCadence/reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md batched as one unit: MEDIUM ids 2 3 6 40 7 8 9 33 15 16 42 18 32 20 23 25 31 41 43 and LOW ids 11 12 17 19 34 39 44
- **Evidence:** the spec audit, `memory/builds/dTendedCadence/reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`; the rescope add row for `TOOL-dTendedCadence-74` in `memory/builds/dTendedCadence/RUN.md`; the unit's spec, `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-74.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTendedCadence-74
- **Caused-by:** PLAY-dClosedLoop-2
