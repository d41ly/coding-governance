# TOOL-dRankedPlan-28 deviation 281 — the round-1 spec audit promoted a unit for a high

**Serves:** deviation TOOL-dRankedPlan-28

- **Departs from:** dRankedPlan [roster]
- **Hand-off:** design-to-spec
- **Before:** dRankedPlan's roster carries sixteen units, `TOOL-dRankedPlan-1` to `TOOL-dRankedPlan-16`, one per clause of its row, beside `TOOL-dRankedPlan-17`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `TOOL-dRankedPlan-28`, the `triage` and `dupes` record kinds join the binding reader, the factory table and the HYGIENE kind list.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 28 HIGH item H6: the triage and dupes record kinds skip the binding reader, the factory table and the HYGIENE kind list; repairs TOOL-dRankedPlan-3. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`; the rescope add row for `TOOL-dRankedPlan-28` in `memory/builds/dRankedPlan/RUN.md`; the unit's spec, `memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-28.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dRankedPlan-28
- **Caused-by:** PLAY-dClosedLoop-2
