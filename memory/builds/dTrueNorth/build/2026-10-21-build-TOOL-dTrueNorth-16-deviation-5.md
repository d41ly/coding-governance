# TOOL-dTrueNorth-16 deviation 5 — the dispatch refuses a consumer before its producer, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-16

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the dispatch order gate of `tools/unattended/unattended.sh`
- **After:** TOOL-dTrueNorth-16 adds a refusal beside the `--dispatch` order gate of `tools/unattended/unattended.sh`: a unit whose spec consumes from a unit of its own build that is neither CLOSED nor WONTDO is refused with code 49, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The round-1 spec audit's id 3 found units that consume from one another sharing an order value, which the order gate reads as one parallel group, so a consumer may be dispatched before its producer and build against code that does not exist yet. Every mechanism that closes it without renumbering is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option, the refusal at the act.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`, item M2 (id 3); the standing ruling ER:388 as the execution plan's rung 5 states it (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6` (`memory/DECISIONS.md:234`); TOOL-dTrueNorth-16 §8 F3
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-16
- **Caused-by:** 2026-10-21-review-TOOL-dTrueNorth-1-spec-audit
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, a code-49 refusal of a unit whose consumes-from producer in its own build is not terminal
