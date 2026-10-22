# TOOL-dTrueNorth-31 deviation 34 — the dispatch reads a consumes-from none that holds a backticked token as unreadable, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-31

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the edge reader `--dispatch` refuses on
- **After:** TOOL-dTrueNorth-31 makes `read_consumes_from` admit a consumes-from payload of `none`, bare or backticked, only when no backtick follows it, so a `none` whose prose holds a backticked token is unreadable and `--dispatch` refuses it with code 49, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The round-2 closing diff review's finding 1 found that TOOL-dTrueNorth-26's `none` admission skips a bullet whatever follows it, so a `none` naming a same-build producer in prose lets `--dispatch` admit its consumer while that producer is open, and hygiene check 12's sibling-in-prose arm runs for `external` alone. Every mechanism that closes it is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2.md`, item M1 (finding 1); the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6`; TOOL-dTrueNorth-31 §8 F1
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-31
- **Caused-by:** 2026-10-22-review-TOOL-dTrueNorth-23-closing-diff-review-round2
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, through `read_consumes_from`: a consumes-from payload of none followed by a backticked token reads as unreadable
