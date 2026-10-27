# TOOL-dRankedPlan-66 deviation 661 — the round-6 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-66

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries the sixteen clause units `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16` and the earlier rounds' promotions `TOOL-dRankedPlan-19` to `TOOL-dRankedPlan-62`, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-66`, the command substitutions of an expanded heredoc body fed to any other command are read as commands.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit of TOOL-dRankedPlan-53 to -62 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md) id 31 HIGH item H3: an expanded heredoc body fed to a command word in neither the shell nor the Python class is read by nothing; repairs TOOL-dRankedPlan-53. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-6 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-53-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-66` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-66.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-66
- **Caused-by:** PLAY-dClosedLoop-2
