# TOOL-dFairHearing-35 deviation 351 — the round-4 spec audit promoted a unit for its high H2

**Serves:** deviation TOOL-dFairHearing-35

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-32`, the round-3 spec audit's promotions `TOOL-dFairHearing-28` to `TOOL-dFairHearing-32` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-35`, ordered at 22 after `TOOL-dFairHearing-30` at 21: unit 15's replay scored by one attempt rule written before any run. Refused attempts count for nothing, only the first two completed attempts of a record and arm are eligible, and the first of them that is not void is scored. A record and arm with no such attempt ends the replay with no decision. The scoring and the decision move here from unit 30.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it. This unit closes one confirmed high of the round-4 spec audit, item H2 (finding id 32). Unit 30 S3 allows a re-run of any record and arm for any cause, S5 records every attempt, and nothing says which completed attempt is scored. The cap and the dead-run rule sit in unit 32 S20 and S21, at order 23, after the runs they govern. So the decision that lands spec 15 S6 can rest on whichever attempt the runner prefers. The skeptic's fix puts the rule in unit 30, but M4 refuses an edit to a spec the audit reviewed. This unit therefore holds a scoring rule, not a run rule, and the rule is fixed before unit 30's runs at order 21 (the spec's §4 and F1). This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-4 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-35` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-35.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-35
- **Caused-by:** PLAY-dClosedLoop-2
