# TOOL-dRankedPlan-58 deviation 581 — the round-5 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-58

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-52`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-58`, every `ratify.py` word comparison of the shell reader goes through one resolving test.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-46 to -52 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md) id 29 HIGH item H5: unit 49 S2 resolves a bound name only at unit 32's two comparison sites; repairs TOOL-dRankedPlan-49. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-58` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-58.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-58
- **Caused-by:** PLAY-dClosedLoop-2
