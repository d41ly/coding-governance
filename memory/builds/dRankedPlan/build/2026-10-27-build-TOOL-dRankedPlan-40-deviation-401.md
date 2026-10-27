# TOOL-dRankedPlan-40 deviation 401 — the round-3 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-40

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-37`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-40`, a command led by a prefix command or a case-arm pattern is read past it.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 34 HIGH item H2 (shared with id 2): a command led by exec or another prefix command, or by a case-arm pattern, is never read as an invocation; repairs TOOL-dRankedPlan-32. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-3 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-40` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-40.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-40
- **Caused-by:** PLAY-dClosedLoop-2
