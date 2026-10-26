# KICK-dKeptSession-31 deviation 311 — the round-1 spec audit promoted a unit for a blocker

**Serves:** deviation KICK-dKeptSession-31

- **Departs from:** dKeptSession [roster]
- **Hand-off:** design-to-spec
- **Before:** dKeptSession's roster carries twenty-eight units, `KICK-dKeptSession-1` to `KICK-dKeptSession-28`, one per clause of its row, beside `KICK-dKeptSession-29`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `KICK-dKeptSession-31`, the message id derived over its recipient and its content key, so two legitimate notices never share one id.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a BLOCKER: spec-audit round1 of the dKeptSession spec set, finding id 54 at BLOCKER, report item B2; id 4 is the same defect at HIGH, item H3, promoted as KICK-dKeptSession-35. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`; the rescope add row for `KICK-dKeptSession-31` in `memory/builds/dKeptSession/RUN.md`; the unit's spec, `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-31.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit KICK-dKeptSession-31
- **Caused-by:** PLAY-dClosedLoop-2
