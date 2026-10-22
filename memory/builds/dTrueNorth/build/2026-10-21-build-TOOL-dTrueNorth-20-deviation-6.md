# TOOL-dTrueNorth-20 deviation 6 — the dispatch refuses a consumes-from cycle and an unreadable edge, a carrier change no clause names

**Serves:** deviation TOOL-dTrueNorth-20

- **Departs from:** `dTrueNorth` [grant]
- **Hand-off:** design-to-spec
- **Before:** the chain's grant PLAY-dClosedLoop-3 lifts veto 2 only for the governance-carrier changes dTrueNorth's own `[chain]` clauses name, and none of `cl-dClosedLoop-0001` to `cl-dClosedLoop-0006` names the dispatch verb of `tools/unattended/unattended.sh`
- **After:** TOOL-dTrueNorth-20 adds two code-49 refusals to `--dispatch`: a consumes-from cycle among a build's units, a self-edge included, and a spec whose Edges block holds a consumes-from line from which no unit id is read, taken under the owner's standing ruling for a fork whose only options trip veto 2 outside the grant
- **Cause:** review finding
- **Reason:** The round-2 spec audit's id 42 found that a malformed Edges block reads as fewer edges, which blocks nothing, and that a cycle wedges the run at --dispatch with no named stop. Every mechanism that refuses either at the act is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the most capable option.
- **Evidence:** `memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`, item M3 (id 42); the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`); the decision row `PLAY-dClosedLoop-6`; TOOL-dTrueNorth-20 §8 F4
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, citing `PLAY-dClosedLoop-6` (ER:388), under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dTrueNorth-20
- **Caused-by:** 2026-10-21-review-TOOL-dTrueNorth-8-spec-audit
- **Surface:** the `--dispatch` verb of `tools/unattended/unattended.sh`, two code-49 refusals: a consumes-from cycle, and an Edges block whose consumes-from line yields no id
