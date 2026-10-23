# TOOL-dFairHearing-37 deviation 371 — the round-4 spec audit promoted its 19 minors on units 30 and 32 as one of two batch units

**Serves:** deviation TOOL-dFairHearing-37

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-32`, the round-3 spec audit's promotions `TOOL-dFairHearing-28` to `TOOL-dFairHearing-32` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-37`, ordered at 24 after `TOOL-dFairHearing-32` at 23 and beside `TOOL-dFairHearing-36` at 24: one of two batch units, closing the round-4 spec audit's 14 MEDIUM findings and 5 LOW findings that land on units 30 and 32, built after every unit it repairs.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed MEDIUM and LOW at a review's exit, batched into a unit naming them all. This unit closes the round-4 spec audit's minors on units 30 and 32: MEDIUM ids 1 2 4 5 10 12 13 20 23 25 33 34 35 36 (items M1 M2 M4 M5 M6 M8 M9 M11 M12 M13 M17 M18 M19 M20) and LOW ids 6 8 17 26 37 (items L1 L3 L6 L9 L11). The other 13 minors land on units 28, 29 and 31 and are `TOOL-dFairHearing-36`'s, and the two write sets are disjoint by M6 (the unit's §4 "Why two batch units" and §8 F2). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-4 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-37` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-37.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-37
- **Caused-by:** PLAY-dClosedLoop-2
