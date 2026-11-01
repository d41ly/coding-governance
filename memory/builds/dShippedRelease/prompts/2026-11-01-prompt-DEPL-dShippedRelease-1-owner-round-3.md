**Serves:** research DEPL-dShippedRelease-1

# Owner ruling — run spec-audit round 3

## The prompt

> Run round 3

— owner, 2026-11-01, answering the question RUN.md parked after round 2 (the run HELD `host-owner-action` until
owner at `865267ad`), which offered: run round 3 over units 79 to 106, stop the chain as for dKeptSession,
dLinkedLibrary, dIndexedDesign and dMindYourWords, or re-scope the landing-review and records-landing units.

## What the run was doing

- Two spec-audit rounds confirmed 106 and 106 findings, with blockers 7 and 8 and highs 22 and 19, at precision 0.97
  and 0.93. Round 2's blockers land on mechanisms round 1's promotions added, and its promotions
  DEPL-dShippedRelease-79 to -106 are the only specs no spec-audit record names.

## How the run applies it

- Round 3 audits units 79 to 106 through `tools/workflows/unattended-build.js` with `round: 3` and those `auditIds`,
  and its disposal promotes what it confirms, as M4 states.
- The owner's standing stop rule still governs the round after it: the chain stops without asking at the first round
  confirming no HIGH; if round 3's highs do not fall, the run parks the question and holds for the owner again.
