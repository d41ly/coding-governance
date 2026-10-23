# TOOL-dFairHearing-27 deviation 271 — the spec audit of units 20 to 23 promoted its 31 minors as one batch unit

**Serves:** deviation TOOL-dFairHearing-27

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries ids `TOOL-dFairHearing-1` to `TOOL-dFairHearing-26`, the last two added by the same disposal moments before for the audit's two highs.
- **After:** the roster also carries `TOOL-dFairHearing-27`, ordered after `TOOL-dFairHearing-25` and `TOOL-dFairHearing-26`: one batch unit closing the spec audit of units 20 to 23's 24 MEDIUM findings (items M1 to M19) and 7 LOW findings (items L1 to L7).
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed MEDIUM and LOW at a review's exit, batched into one unit naming them all, and the minors do not split into two disjoint write sets by M6 (the unit's §4 "Why one unit and not two" and §8 F1). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the spec audit of units 20 to 23, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-27` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-27.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-27
- **Caused-by:** PLAY-dClosedLoop-2
