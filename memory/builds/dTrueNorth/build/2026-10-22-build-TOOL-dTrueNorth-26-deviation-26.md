# TOOL-dTrueNorth-26 deviation 26 — the dispatch reads a consumes-from none as no edge, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-26

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the edge reader `--dispatch` refuses on
- **After:** TOOL-dTrueNorth-26 makes `read_consumes_from` read a consumes-from payload of `none`, bare or backticked, as it reads `external`, so `--dispatch` no longer refuses a build whose spec declares no producer that way, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The closing diff review's finding 13 found two CLOSED specs whose `none` payload reads as unreadable, so every later --dispatch of their builds is refused with a remedy that rewrites a frozen spec, while the hygiene engine admits the same form. Every mechanism that clears it is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`, item M5 (finding 13); the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6`; TOOL-dTrueNorth-26 §8 F4
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-26
- **Caused-by:** 2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, through `read_consumes_from`: a consumes-from payload of none reads as no edge
