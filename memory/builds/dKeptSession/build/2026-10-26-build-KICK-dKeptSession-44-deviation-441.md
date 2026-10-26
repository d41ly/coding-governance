# KICK-dKeptSession-44 deviation 441 — the round-1 spec audit promoted a batch unit for its minors

**Serves:** deviation KICK-dKeptSession-44

- **Departs from:** dKeptSession [roster]
- **Hand-off:** design-to-spec
- **Before:** dKeptSession's roster carries twenty-eight units, `KICK-dKeptSession-1` to `KICK-dKeptSession-28`, one per clause of its row, beside `KICK-dKeptSession-29`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `KICK-dKeptSession-44`, the round-1 spec audit's 42 minor findings, closed after every unit they land on is built.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the MEDIUM and LOW findings, batched: spec-audit round1 of the dKeptSession spec set, minors batch, MEDIUM ids 3 5 6 7 34 8 37 9 10 11 15 19 20 21 46 23 24 27 33 35 36 40 48 49 50 51 52 56 59 60 61 62 63 and LOW ids 12 13 14 44 18 41 42 43 53. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-1 spec audit, `memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`; the rescope add row for `KICK-dKeptSession-44` in `memory/builds/dKeptSession/RUN.md`; the unit's spec, `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit KICK-dKeptSession-44
- **Caused-by:** PLAY-dClosedLoop-2
