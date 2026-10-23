# TOOL-dFairHearing-32 deviation 321 — the round-3 spec audit promoted its 32 minors as one batch unit

**Serves:** deviation TOOL-dFairHearing-32

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27`, the round-2 spec audit's promotions `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-32`, ordered at 23 after `TOOL-dFairHearing-31` at 22: one batch unit closing the round-3 spec audit's 21 MEDIUM findings (items M1 to M14) and 11 LOW findings (items L1 to L9) on units 4, 14, 25 and 27, built after every unit of the build.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed MEDIUM and LOW at a review's exit, batched into one unit naming them all. This unit closes the round-3 spec audit's minors, MEDIUM ids 2 3 5 6 7 12 13 14 17 20 23 24 25 26 30 31 32 33 35 36 37 and LOW ids 4 8 9 10 15 16 19 21 27 29 38, and they do not split into two disjoint write sets by M6 (the unit's §4 "Why one unit and not two" and §8 F1). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-32` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-32.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-32
- **Caused-by:** PLAY-dClosedLoop-2
