# TOOL-dFairHearing-30 deviation 301 — the round-3 spec audit promoted a unit for its high H2

**Serves:** deviation TOOL-dFairHearing-30

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27`, the round-2 spec audit's promotions `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-30`, ordered at 21 after `TOOL-dFairHearing-25` at 20: unit 15's with-and-without replay, handed over by unit 25, run with one fresh clone per record and arm, each checked clean before its harness call, so no arm reviews a tree holding the other arm's report.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it. This unit closes one confirmed high of the round-3 spec audit, item H2 (finding id 28). Unit 25 runs the `selected` and `ungated` arms of each record in one clone, and the harness writes each report under `${repo}/${reviewDir}` (`tools/workflows/tier2-review.template.js:297`, `:1749`), so the first arm's report sits in the tree the second arm reviews and the recall comparison that decides spec 15 S6 can be contaminated. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-30` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-30.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-30
- **Caused-by:** PLAY-dClosedLoop-2
