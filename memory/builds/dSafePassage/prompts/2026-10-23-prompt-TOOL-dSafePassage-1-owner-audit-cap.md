**Serves:** research TOOL-dSafePassage-1

# Owner instruction — the spec audit stops after round 7

## The prompt

> stop reviewing the specs after this round

— owner, 2026-10-23, in the run's session while the round-7 spec audit (`wf_33e17e24-003`) was running over
TOOL-dSafePassage-51 and TOOL-dSafePassage-52.

## How the run applies it

- Round 7 completes, and its record, roster rows and deviation records are committed as in rounds 1 to 6.
- No round 8 runs. Any unit round 7's disposal promotes is specced, deferred and carried to the build run with no
  spec audit, and the close records the `specs-audited` override citing this record.
- The spec run's closing review over its spec commits (the execution plan's `[phase-2]`, spec-run row "The closing
  review") would review the same spec-only diff, so the run reads the instruction as covering it, does not run it,
  and records that at the close. The build run's closing review, over code, is not touched by this instruction.
