# TOOL-dRankedPlan-62 deviation 621 — the round-5 spec audit batched its minors into a unit

**Serves:** deviation TOOL-dRankedPlan-62

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-52`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-62`, the spec audit of units 46 to 52: its 23 medium and low findings, closed in one batch.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the MEDIUM and LOW findings batched into one unit: spec-audit of TOOL-dRankedPlan-46 to -52 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) the 23 MEDIUM and LOW findings batched into one unit: ids 1 2 4 5 8 9 10 11 12 13 14 15 16 17 18 19 20 21 24 25 26 33 34 (items M1 to M14 and L1 to L7). This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-62` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-62
- **Caused-by:** PLAY-dClosedLoop-2
