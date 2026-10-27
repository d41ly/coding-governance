# TOOL-dRankedPlan-33 deviation 331 — the round-2 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-33

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries sixteen units, `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16`, one per clause of its row, the round-1 promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-29`, and `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-33`, the shared `plan.exit` fixtures plant a witnessed plan record, so the precondition holds only where a plant removes it.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 21 HIGH item H3: unit 19's plan-record precondition reds every earlier admitted plan.exit arm of the shared fixture; repairs TOOL-dRankedPlan-19. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-33` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-33.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-33
- **Caused-by:** PLAY-dClosedLoop-2
