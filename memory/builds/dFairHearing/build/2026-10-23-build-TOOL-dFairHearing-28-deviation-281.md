# TOOL-dFairHearing-28 deviation 281 — the round-3 spec audit promoted a unit for its blocker B1

**Serves:** deviation TOOL-dFairHearing-28

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27`, the round-2 spec audit's promotions `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-28`, ordered at 21 after `TOOL-dFairHearing-26` at 20: the hook suite's census re-pinned to a population of 59 and 14, measured by a script file whose pattern no shell can fold, with unit 26's placement check run over the whole population.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a BLOCKER to a unit whose mechanism closes it. This unit closes the one confirmed blocker of the round-3 spec audit, item B1 (finding id 11). Unit 26 pins its census at 66 labels and a population of 54 and 14, but base `3708a705` holds 71 labels and a population of 59 and 14, so a correct census reds against the pin, and a census tuned to the pin leaves 5 arms unchecked. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-28` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-28.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-28
- **Caused-by:** PLAY-dClosedLoop-2
