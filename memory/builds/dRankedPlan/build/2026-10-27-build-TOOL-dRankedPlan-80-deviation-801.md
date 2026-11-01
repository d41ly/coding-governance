# TOOL-dRankedPlan-80 deviation 801 — the round-8 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-80

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-77`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-80`, a JavaScript declarator that opens with a destructuring pattern ends at its value, so the declarator after it is bound.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-68 to -77 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) id 15 HIGH item H2: unit 72's declarator walk has no rule for a destructuring declarator, so a plain declarator after one is never bound; repairs TOOL-dRankedPlan-72. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-8 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-80` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-80.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-80
- **Caused-by:** PLAY-dClosedLoop-2
