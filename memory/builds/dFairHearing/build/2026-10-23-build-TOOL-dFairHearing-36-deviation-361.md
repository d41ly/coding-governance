# TOOL-dFairHearing-36 deviation 361 — the round-4 spec audit promoted its minors on units 28, 29 and 31 as one batch unit

**Serves:** deviation TOOL-dFairHearing-36

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-32`, the round-3 spec audit's promotions `TOOL-dFairHearing-28` to `TOOL-dFairHearing-32` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-36`, ordered at 24 after `TOOL-dFairHearing-32` at 23: one batch unit closing the round-4 spec audit's 6 MEDIUM findings (items M3, M7, M10, M14, M15 and M16) and 7 LOW findings (items L2, L4, L5, L7, L8 and L10) on units 28, 29 and 31, built after every unit it repairs and concurrently with `TOOL-dFairHearing-37`, whose write set is disjoint.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a MEDIUM or LOW to a unit whose mechanism closes it, batched where the findings share a unit. This unit closes the round-4 spec audit's minors that land on units 28, 29 and 31, MEDIUM ids 3, 11, 19, 27, 28 and 29 and LOW ids 7, 9, 15, 18, 21, 24 and 30: the five escaped-quote arms moved twice in parallel, a census copy that never reaches its population assertion, census and member probes that decode `git show` by the locale codec, a placement check never seen red, a member label that raises on a quote-less line, a cited extractor path that does not exist, an omitted receiving leg, and a version check that merge-bases an explicit `GATE_BASE` and keeps a third hand copy of the bar's base rule. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-4 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-36` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-36.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-36
- **Caused-by:** PLAY-dClosedLoop-2
