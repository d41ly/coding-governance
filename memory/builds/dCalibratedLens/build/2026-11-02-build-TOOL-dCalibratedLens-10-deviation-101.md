# TOOL-dCalibratedLens-10 deviation 101 — the held leg re-runs the suite's scoring and owes the replay, never runs the items

**Serves:** deviation TOOL-dCalibratedLens-10

- **Departs from:** `cl-dClosedLoop-0467@58bd6ee5`
- **Hand-off:** design-to-spec
- **Before:** instruction evals: a replay suite of recorded items with known outcomes, scored through dFairHearing's scorer factory, re-run as a held leg when an instruction unit changes, a confirmed finding whose cause is an instruction adding a case (night pass, point 6)
- **After:** instruction evals: a replay suite of recorded items with known outcomes, scored through dFairHearing's scorer factory, its scoring re-run as a held leg when an instruction unit changes, the leg red on each case whose replay the change made owed until the replay is recorded, a confirmed finding whose cause is an instruction adding a case (night pass, point 6)
- **Cause:** design defect
- **Reason:** The clause scores the suite through dFairHearing's scorer factory, and that factory re-derives every figure from committed raw outputs and runs no agent, so the suite a leg can re-run is a scoring of committed replays. A replay is a role agent's item and a review of its output, about 0.81 M tokens for a design audit, which a gate leg cannot launch without a harness dependency and an automation surface at bar time. The spec keeps the clause's intent: a change to a file an instruction case loads makes that case owed, the held leg reds naming the case, the moved paths and the procedure that runs the replay, and a recorded replay below its best score reds as fallen. What it does not do is produce the replay itself. TOOL-dCalibratedLens-10 §8 F2 records the options and why the others were discarded.
- **Evidence:** the factory's contract, `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-12.md` §1 and §3 ("the factory reads committed outputs and runs no agent"); the held tier's guard selection, `tools/run-gates/run-gates.sh:3075-3080`; the cost of a review, gap-review-03 at `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:437`; the fork, `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-10.md` §8 F2; rung 3, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:909`; the new hash, `derive_clause_hash` (`tools/memory-tree/design_lib.py:173`) over the After text, `0bd9d49f`, which returns `58bd6ee5` over the Before text
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dCalibratedLens's spec run, under the chain's `author-recorded` value (README rule 5); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0467@58bd6ee5
- **Caused-by:** TOOL-dCalibratedLens-10
