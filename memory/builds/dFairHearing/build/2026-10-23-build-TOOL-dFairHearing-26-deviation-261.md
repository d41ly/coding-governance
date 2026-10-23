# TOOL-dFairHearing-26 deviation 261 — the round-2 spec audit promoted its high H2 to a unit

**Serves:** deviation TOOL-dFairHearing-26

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-25`, the last added by the same disposal moments before for the audit's high H1.
- **After:** the roster also carries `TOOL-dFairHearing-26`, every rule 0 and rule 5 arm of the hook's suite found at its new home and gone from the old one, counted by label whatever helper writes it.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit to a unit whose mechanism closes it, a HIGH to a unit of its own; this unit closes one confirmed high of the round-2 spec audit, the audit of units 20 to 23, item H2 (finding id 10). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-2 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-26` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-26.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-26
- **Caused-by:** PLAY-dClosedLoop-2
