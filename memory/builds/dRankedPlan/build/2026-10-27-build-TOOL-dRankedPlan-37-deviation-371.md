# TOOL-dRankedPlan-37 deviation 371 — the round-2 spec audit batched its minors into a unit

**Serves:** deviation TOOL-dRankedPlan-37

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries sixteen units, `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16`, one per clause of its row, the round-1 promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-29`, and `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-37`, the spec audit of units 19 to 29: its 25 medium and low findings, closed in one batch.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the MEDIUM and LOW findings batched into one unit: spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) the 25 MEDIUM and LOW findings batched into one unit: ids 1 2 3 4 5 7 8 9 11 12 13 14 16 17 18 22 23 24 25 27 31 32 33 34 35 (items M1 to M12 and L1 to L6). This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-37` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-37.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-37
- **Caused-by:** PLAY-dClosedLoop-2
