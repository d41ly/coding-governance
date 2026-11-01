# TOOL-dRankedPlan-29 deviation 291 — the round-1 spec audit batched its minors into a unit

**Serves:** deviation TOOL-dRankedPlan-29

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries sixteen units, `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16`, one per clause of its row, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-29`, the round-1 spec audit's 39 medium and low findings, closed in one batch.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the MEDIUM and LOW findings batched into one unit: spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) the 39 MEDIUM and LOW findings batched into one unit: ids 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 22 23 24 25 26 29 30 31 32 33 34 35 36 38 40 41 42 43 44 45 46 47 48 49 (items M1 to M21 and L1 to L12). This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-29` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-29.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-29
- **Caused-by:** PLAY-dClosedLoop-2
