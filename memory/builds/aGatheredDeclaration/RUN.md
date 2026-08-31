# aGatheredDeclaration - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 08d1389f04e091ebf7941ac8eae62a0cd4dc4a66
phase: BUILDING
branch-sha: 44734f152c0f6a2d7ea5c6438dc969de8a7e9f33
branch-ref: refs/heads/branch/gate-bar-tooling-review-020565
mode: prompt
anchor-kind: run-branch
keepalive: 5d32537e
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 14e21399f7dd0559224837a2754fcbf9fc4a754b
anchor-ref: refs/heads/main
base: 44734f152c0f6a2d7ea5c6438dc969de8a7e9f33

## Parked

2026-08-30T22:42:29Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 5

2026-08-30T22:43:33Z rescope · item add TOOL-aGatheredDeclaration-8 · reason F9 and F29 of the round-1 spec audit: unit 2's S6 lanes and S7 tool probe cannot be built without rewriting the dispatch loop (one pool at one width, one global longest-first hint), which S2 asserts does not change and Section 5 prices as no regression. R3 of the architecture record reaches the same place from the migration side — a behaviour change inside a format change is unreviewable. Lanes and the tool probe become their own unit so unit 2 is provably behaviour-neutral.

2026-08-30T23:16:43Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 4

2026-08-30T23:46:31Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 3

2026-08-31T02:27:36Z review · item aGatheredDeclaration · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT
