# KICK-dKeptSession-41 deviation 411 — the round-1 spec audit promoted a unit for a high

**Serves:** deviation KICK-dKeptSession-41

- **Departs from:** dKeptSession [roster]
- **Hand-off:** design-to-spec
- **Before:** dKeptSession's roster carries twenty-eight units, `KICK-dKeptSession-1` to `KICK-dKeptSession-28`, one per clause of its row, beside `KICK-dKeptSession-29`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `KICK-dKeptSession-41`, the three catalogue rows that already stand given their summary and usage, one row per name, never a second minted beside them.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round1 of the dKeptSession spec set, finding id 45 at HIGH, report item H8; ids 7 and 34 are the same defect at MEDIUM, item M4, batched into KICK-dKeptSession-44. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`; the rescope add row for `KICK-dKeptSession-41` in `memory/builds/dKeptSession/RUN.md`; the unit's spec, `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-41.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit KICK-dKeptSession-41
- **Caused-by:** PLAY-dClosedLoop-2
