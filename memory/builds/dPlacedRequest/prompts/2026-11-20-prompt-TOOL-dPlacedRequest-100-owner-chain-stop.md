**Serves:** research TOOL-dPlacedRequest-100

# Owner ruling — the spec audit chain stops at its ceiling, and unit 100 is built unaudited

## The prompt

> Build 95–100, override 100

— owner, 2026-11-20, answering the run's hand-off under `owner-decision`, whose parked decision
`spec-audit-chain-ceiling` offered three options: audit unit 100 as a fifth round past the ceiling, build units 95
to 100 now and close with `specs-audited` overridden for unit 100 alone, or stop the run.

## What the run was doing

- The spec audit chain's fourth round audited the closing review's promoted units `TOOL-dPlacedRequest-95` to `-99`.
  It converged with no BLOCKER, folded every local finding into those specs, and promoted one new-mechanism finding to
  `TOOL-dPlacedRequest-100`, specced and never audited.
- That round is the chain's ceiling, so `--chain-verdict` read HOLD and the run handed off to the owner.

## How the run applies it

- The chain ends here: this record is cited by an `owner-stop` row, so the verdict reads STOP and the roster is
  dispatched.
- Units 95 to 100 are built in their declared order from their specs as written.
- Unit 100 closes under a recorded `--close --override specs-audited` citing this record; units 95 to 99 owe no
  override, because round 4 audited them.
