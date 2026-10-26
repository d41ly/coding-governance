# KICK-dKeptSession-49 deviation 491 — the round-2 spec audit promoted a unit for a high

**Serves:** deviation KICK-dKeptSession-49

- **Departs from:** dKeptSession [roster]
- **Hand-off:** design-to-spec
- **Before:** dKeptSession's roster carries the twenty-eight clause units `KICK-dKeptSession-1` to `KICK-dKeptSession-28` and the round-1 promotions `KICK-dKeptSession-30` to `KICK-dKeptSession-44`, beside `KICK-dKeptSession-29`, the opening's build ask in `BACKLOG.md`.
- **After:** the roster also carries `KICK-dKeptSession-49`, the JS mirror reader takes the inputs it compares from its own code, so a mirror missing the preset store reads stale.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER or HIGH to a unit whose mechanism closes it and the MEDIUM and LOW findings to one batch unit; this unit closes a HIGH: spec-audit round1 of the round-1 promotions KICK-dKeptSession-30 to -44, finding id 22 at HIGH, report item H3, which it shares with id 48, promoted as KICK-dKeptSession-50; id 9 is the same defect at MEDIUM, item M8, batched into KICK-dKeptSession-56. This is a spec run, so the unit is specced, audited as M4 provides and carried forward once, and the build run after it builds it.
- **Evidence:** the round-2 spec audit, `memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`; the rescope add row for `KICK-dKeptSession-49` in `memory/builds/dKeptSession/RUN.md`; the unit's spec, `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-49.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit KICK-dKeptSession-49
- **Caused-by:** PLAY-dClosedLoop-2
