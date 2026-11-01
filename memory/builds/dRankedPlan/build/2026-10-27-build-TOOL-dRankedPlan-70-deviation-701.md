# TOOL-dRankedPlan-70 deviation 701 — the round-7 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-70

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-67`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-70`, every expression-end call of the JavaScript reader passes the lexer's facts, each declarator's included.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-63 to -67 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md) id 16 HIGH item H1 (shared with ids 1, 8 and 22): the reused read_ts_expr_end is called without the arguments parse_ts_source passes, and unit 64 inherits it per declarator; repairs TOOL-dRankedPlan-64. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-7 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-70` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-70.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-70
- **Caused-by:** PLAY-dClosedLoop-2
