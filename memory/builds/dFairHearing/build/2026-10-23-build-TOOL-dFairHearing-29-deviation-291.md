# TOOL-dFairHearing-29 deviation 291 — the round-3 spec audit promoted a unit for its high H1

**Serves:** deviation TOOL-dFairHearing-29

- **Departs from:** dFairHearing [roster]
- **Hand-off:** design-to-spec
- **Before:** dFairHearing's roster carries the specced units `TOOL-dFairHearing-1` to `TOOL-dFairHearing-18`, `TOOL-dFairHearing-20` to `TOOL-dFairHearing-23` and `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27`, the round-2 spec audit's promotions `TOOL-dFairHearing-25` to `TOOL-dFairHearing-27` the last specced.
- **After:** the roster also carries `TOOL-dFairHearing-29`, ordered at 21: the five escaped-quote `rule0` arms of the hook's suite, pinned at `3708a705` by their source bytes, each checked by name as present at base, at home in the pack's suite and gone from the hook's suite, so no pinned total can hide one.
- **Cause:** review finding
- **Reason:** BUILD-METHOD M4 promotes every confirmed finding at a review's exit, a HIGH to a unit whose mechanism closes it. This unit closes one confirmed high of the round-3 spec audit, item H1 (finding id 1). Unit 26's S1 and AC1 say the census population holds the escaped-quote array arm, while its pinned counts hold only the reading that drops every escaped-quote label, so its members and its counts disagree and a probe tuned to the counts drops 5 arms. This is a spec run, so the unit is specced, audited and carried forward once, and the build run after it builds it (`UNATTENDED-STOPS.md` §15, the carry-forward term's second condition).
- **Evidence:** the round-3 spec audit, `memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`; the rescope add row for `TOOL-dFairHearing-29` in `memory/builds/dFairHearing/RUN.md`; the unit's spec, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-29.md`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dFairHearing-29
- **Caused-by:** PLAY-dClosedLoop-2
