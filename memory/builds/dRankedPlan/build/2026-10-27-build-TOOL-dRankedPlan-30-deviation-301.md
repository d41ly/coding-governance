# TOOL-dRankedPlan-30 deviation 301 — the round-2 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-30

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries sixteen units, `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16`, one per clause of its row, the round-1 promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-29`, and `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-30`, the declared callers of the session-scoped predicate are kit anchors, resolved at run time.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 19 HIGH item H1: SESSION_PREDICATE_CALLERS spells two literal kit paths the install-prefix ban counts; repairs TOOL-dRankedPlan-22. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-30` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-30.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-30
- **Caused-by:** PLAY-dClosedLoop-2
