# TOOL-dFairHearing-23 deviation 231 — the round-1 spec audit promoted its 49 minors as one batch unit

**Serves:** deviation TOOL-dFairHearing-23

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries twenty-two units, `TOOL-dFairHearing-1` to `TOOL-dFairHearing-22`, the last three added by the same disposal moments before for the audit's three highs.
- **After:** the roster also carries `TOOL-dFairHearing-23`, one batch unit closing the round-1 spec audit's 37 MEDIUM findings (items M1 to M28) and 12 LOW findings (items L1 to L12).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed MEDIUM and LOW at a review's exit, batched into one unit naming them all, and the minors do not split into two disjoint write sets by M6 (the unit's §4 "Why one unit" and §8 F1). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-1 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-23` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-23
- **Caused-by:** PLAY-dClosedLoop-2
