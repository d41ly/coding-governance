# TOOL-dFairHearing-25 deviation 251 — the spec audit of units 20 to 23 promoted a unit for its high H1

**Serves:** deviation TOOL-dFairHearing-25

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18` and `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23`, the round-1 spec audit's promotions `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-25`, ordered directly after `TOOL-dFairHearing-23`: the owed replays of units 1 and 15 run once, on the replay contract unit 23 corrects, and their verdicts set the dark switches.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes one confirmed high of the spec audit of units 20 to 23, item H1 (finding id 1): units 1 and 15 run their replays at orders 15 and 16, before unit 23 at order 19 corrects the contract they run on. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the spec audit of units 20 to 23, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-25` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-25
- **Caused-by:** PLAY-dClosedLoop-2
