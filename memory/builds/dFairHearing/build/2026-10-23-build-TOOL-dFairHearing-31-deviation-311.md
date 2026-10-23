# TOOL-dFairHearing-31 deviation 311 — the round-3 spec audit promoted a unit for its high H3

**Serves:** deviation TOOL-dFairHearing-31

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27`, the round-2 spec audit's promotions `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-31`, ordered at 22 after `TOOL-dFairHearing-27` at 21: unit 27's version-line check re-run on the base the merge bar's guards diff against, `GATE_BASE` or the merge-base with the remote ladder's observed branch, refusing with exit 2 and its reason when that base cannot be resolved, before any diff is read.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it. This unit closes one confirmed high of the round-3 spec audit, item H3 (finding id 34). Unit 27's AC10 diffs from `$(git merge-base HEAD main)` and passes when the pipeline prints nothing, so with no local `main` git fails on stderr, stdout stays empty, and the check passes having diffed nothing. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-31` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-31.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-31
- **Caused-by:** PLAY-dClosedLoop-2
