# KICK-dKeptSession-65 deviation 651 — the round-6 spec audit promoted a batch unit for its minors

**Serves:** deviation KICK-dKeptSession-65

- **Departs from:** dKeptSession [roster]
- **Hand-off:** design-to-spec
- **Before:** dKeptSession's roster carries the twenty-eight clause units `KICK-dKeptSession-1` to `KICK-dKeptSession-28` and the promotions of rounds 1 to 5, `KICK-dKeptSession-30` to `KICK-dKeptSession-64`, beside `KICK-dKeptSession-29`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `KICK-dKeptSession-65`, the round-5 minors batch's audit's 26 minor findings, closed after the batch they land on is built.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the MEDIUM and LOW findings, batched: spec-audit round1 of the round-5 minors batch KICK-dKeptSession-64, minors batch, MEDIUM ids 1 2 3 4 9 10 11 15 16 20 21 23 24 and LOW ids 5 6 7 8 12 13 14 17 18 19 22 25 26. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-6 spec audit, `memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-64-spec-audit.md`; the rescope add row for `KICK-dKeptSession-65` in `memory/builds/dKeptSession/RUN.md`; the unit's spec, `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-65.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit KICK-dKeptSession-65
- **Caused-by:** PLAY-dClosedLoop-2
