**Serves:** research TOOL-dFairHearing-1

# Owner instruction — stop the spec-audit chain after round 5

## The prompt

> Stop reviewing the specs.

> No, that round was almost finished, let it run to completion, but stop after.

— owner, 2026-10-23, while the round-5 spec audit of units 33 to 37 (run `wf_c5e50b0a-6a8`) was in its disposal stage. The run had stopped that workflow on the first message, then resumed it on the second.

## What the run was doing

- BUILD-METHOD M4: each promoted unit of a SPEC subject is audited as a SPEC, and each audit takes a fresh subject, so only a promoting round whose precision falls below the review protocol's 0.5 floor ends the chain. The harness's `nextAction` named the next round after every one.
- Rounds 1 to 5 read precision 0.98, 0.80, 0.95, 0.95 and 0.95, and promoted 52, 33, 36, 35 and 37 findings, into four, three, five, five and three units (`TOOL-dFairHearing-38` to `-40` from round 5). Nothing in the chain was converging.

## How the run applies it

- Round 5 runs to completion, its disposal included, and no spec-audit round runs after it.
- Round 5's promotions are specced and recorded like every earlier round's, each with its departure record, and carried forward once. No audit names them. They close under a recorded override of `specs-audited`, citing this record, as M4 already provides when a chain ends.
- The wrap-up names the chain's non-convergence and the round-5 promotions as unaudited.
