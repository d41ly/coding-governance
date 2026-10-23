**Serves:** research TOOL-dGroundRules-1

# Owner instruction — the spec audit stops after round 6

## The prompt

> Cap the spec audit at round 6: close dGroundRules' spec run with units 44-52 under a recorded specs-audited override, defer every unit and land.

— owner, 2026-10-23, in the run's session, answering the parked decision the run handed off at owner-decision
(`f09da0a7f`): six rounds had promoted 9, 4, 7, 2, 9 and 9 units at precision 0.85-1.00.

## How the run applies it

- No round 7 runs. Units TOOL-dGroundRules-44 to TOOL-dGroundRules-52, which round 6's disposal promoted, stay
  specced as written and unaudited, and the close records the `specs-audited` override citing this record.
- Every unit of the roster, the eleven the README opened with and the forty-one the audit promoted, is deferred
  against TOOL-dGroundRules-12 and carried forward to the build run, which builds them (README rule 1).
- The run then closes and lands as the spec run of the execution plan's `[phase-2]` states.
