# TOOL-dRankedPlan-79 deviation 791 — the round-8 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-79

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-77`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-79`, the loop selftest re-checks the four-argument class over the JavaScript reader at every close.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-68 to -77 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) id 1 HIGH item H1 (shared with id 16): unit 70 AC2 runs once at its tip, so the calls units 71 and 72 rewrite later are never checked against the four-argument class; repairs TOOL-dRankedPlan-70. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-8 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-79` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-79.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-79
- **Caused-by:** PLAY-dClosedLoop-2
