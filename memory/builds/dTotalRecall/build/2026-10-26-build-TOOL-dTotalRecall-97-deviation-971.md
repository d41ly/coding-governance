# TOOL-dTotalRecall-97 deviation 971 — the round-9 spec audit promoted a unit for a HIGH finding

**Serves:** deviation TOOL-dTotalRecall-97

- **Departs from:** dTotalRecall [roster]
- **Hand-off:** design-to-spec
- **Before:** dTotalRecall's roster carries twenty-six units, `TOOL-dTotalRecall-1` to `TOOL-dTotalRecall-26`, one per clause of its row, beside `TOOL-dTotalRecall-27`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dTotalRecall-97`, the round-9 spec audit's id 30 HIGH, item H3 shared with id 12.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the minors batched into one unit; this unit closes spec-audit round 9's id 30 HIGH, item H3 shared with id 12. This is a spec run, so the unit is specced and left unaudited by the owner's stop at round 9, carried forward once, and the build run after it builds it.
- **Evidence:** the round-9 spec audit, `memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`; the rescope add row for `TOOL-dTotalRecall-97` in `memory/builds/dTotalRecall/RUN.md`; the unit's spec, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-97.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTotalRecall-97
- **Caused-by:** PLAY-dClosedLoop-2
