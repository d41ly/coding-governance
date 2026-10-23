# TOOL-dFairHearing-17 deviation 171 — a non-terminal round reads CONVERGING

**Serves:** deviation TOOL-dFairHearing-17

- **Departs from:** `cl-dClosedLoop-0084@5c5896a3` [design]
- **Hand-off:** design-to-spec
- **Before:** each round's state in the review report, CONVERGED, NON-CONVERGENT, BOUNDED or CEILING, computed against the round before from its blocker and high count at the round limit its caller passes, seen red on a planted flat sequence and an oscillating one, and on a strictly falling sequence that reaches its caller's limit, read BOUNDED, and one run past it, read CEILING (P39, the owner's SL-3, the parked debt's review)
- **After:** each round's state in the review report, CONVERGED, NON-CONVERGENT, BOUNDED or CEILING, or CONVERGING on a round with blockers or highs standing that is the first or falls below the round before, while under its caller's limit or when its caller passes none, computed against the round before from its blocker and high count at the round limit its caller passes, seen red on a planted flat sequence and an oscillating one, and on a strictly falling sequence that reaches its caller's limit, read BOUNDED, and one run past it, read CEILING (P39, the owner's SL-3, the parked debt's review)
- **Cause:** design defect
- **Reason:** The clause lists four states, all terminal, so a round that has blockers or highs standing, fell below the round before and has not reached its limit takes none of them. The unattended driver names that round CONVERGING (`tools/unattended/unattended.sh:12606-12617`), and keeping its token lets the harness's rule be compared with the driver's over every sequence, the parity arm TOOL-dFairHearing-17 §8 F3 relies on. A `null` there would make a falling round indistinguishable from one whose state could not be computed. Every one of the clause's own red cases reads as the clause states.
- **Evidence:** TOOL-dFairHearing-17 §8 F4 and AC1 to AC3, AC6; `review_state` and its header comment (`tools/unattended/unattended.sh:12606-12617`); the flow-steps record naming the driver's loop states CONVERGING, CONVERGED, NON-CONVERGENT and BOUNDED (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:822-823`)
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dFairHearing's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0084@5c5896a3
- **Caused-by:** PLAY-dClosedLoop-1
