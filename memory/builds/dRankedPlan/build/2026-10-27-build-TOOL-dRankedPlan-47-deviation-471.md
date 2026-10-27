# TOOL-dRankedPlan-47 deviation 471 — the round-4 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-47

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-45`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-47`, a heredoc body fed to a Python interpreter is read by the Python reader, over unit 32's interpreter class.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) id 30 HIGH item H1 (shared with id 1): a heredoc body fed to a $ variable interpreter such as "$py" reaches only the textual rule, so its argv call to ratify.py passes; repairs TOOL-dRankedPlan-45. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-4 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-47` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-47.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-47
- **Caused-by:** PLAY-dClosedLoop-2
