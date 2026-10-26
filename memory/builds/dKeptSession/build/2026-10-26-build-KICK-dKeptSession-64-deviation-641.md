# KICK-dKeptSession-64 deviation 641 — the round-5 spec audit promoted a batch unit for its minors

**Serves:** deviation KICK-dKeptSession-64

- **Departs from:** dKeptSession [roster]
- **Hand-off:** design-to-spec
- **Before:** dKeptSession's roster carries the twenty-eight clause units `KICK-dKeptSession-1` to `KICK-dKeptSession-28` and the promotions of rounds 1 to 4, `KICK-dKeptSession-30` to `KICK-dKeptSession-63`, beside `KICK-dKeptSession-29`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `KICK-dKeptSession-64`, the round-4 minors batch's audit's 20 minor findings, closed after the batch they land on is built.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes the MEDIUM and LOW findings, batched: spec-audit round1 of the round-4 minors batch KICK-dKeptSession-63, minors batch, MEDIUM ids 1 2 3 4 5 11 12 13 14 15 19 20 21 and LOW ids 6 7 8 9 10 17 18. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-5 spec audit, `memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-63-spec-audit.md`; the rescope add row for `KICK-dKeptSession-64` in `memory/builds/dKeptSession/RUN.md`; the unit's spec, `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-64.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit KICK-dKeptSession-64
- **Caused-by:** PLAY-dClosedLoop-2
