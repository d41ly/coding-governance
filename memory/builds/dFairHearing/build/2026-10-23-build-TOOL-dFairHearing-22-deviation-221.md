# TOOL-dFairHearing-22 deviation 221 — the round-1 spec audit promoted a unit for its high H3

**Serves:** deviation TOOL-dFairHearing-22

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries twenty-one units, `TOOL-dFairHearing-1` to `TOOL-dFairHearing-21`, the last two added by the same disposal moments before for the audit's highs H1 and H2.
- **After:** the roster also carries `TOOL-dFairHearing-22`, agent-cap fails closed on a spec-audit call when the opt-in pack is not beside it.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it; this unit closes one confirmed high of the round-1 spec audit, item H3 (finding id 40), a partial `govkit update` landing the hook without rule 0 and without the review kit's opt-in pack. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-1 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-22` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-22.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-22
- **Caused-by:** PLAY-dClosedLoop-2
