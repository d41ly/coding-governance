# TOOL-dRankedPlan-23 deviation 231 — the round-1 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-23

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries sixteen units, `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16`, one per clause of its row, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-23`, `show` reports a revision's ratification from the record of how the re-entering move was admitted.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 4 HIGH item H3 (related id 38): show re-asks the predicate instead of reading how the gate released the re-entry; repairs TOOL-dRankedPlan-15. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-23` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-23.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-23
- **Caused-by:** PLAY-dClosedLoop-2
