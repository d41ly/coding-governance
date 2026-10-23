# TOOL-dFairHearing-21 deviation 211 — the round-1 spec audit promoted its high H2 to a unit

**Serves:** deviation TOOL-dFairHearing-21

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries twenty units, `TOOL-dFairHearing-1` to `TOOL-dFairHearing-20`, the last added by the same disposal moments before for the audit's high H1.
- **After:** the roster also carries `TOOL-dFairHearing-21`, the scorer factory's held-out freeze check hashes the bytes it scores against the freeze's blob and refuses a shallow history.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit to a unit whose mechanism closes it, a HIGH to a unit of its own; this unit closes one confirmed high of the round-1 spec audit, item H2 (finding id 39). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-1 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-21` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-21.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-21
- **Caused-by:** PLAY-dClosedLoop-2
