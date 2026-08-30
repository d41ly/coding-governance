# aLexedStripper - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 79d082249f37035d16618ff798f6c22e99b989dd
phase: REVIEWING
branch-sha: 19d9b328c26ca41d9d275ef43abfa76f7efbef20
branch-ref: refs/heads/branch/kit-degradations-review-2faa8d
mode: prompt
anchor-kind: run-branch
keepalive: 81a43dbc
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: ffa01a07ee02bf1f4190d9a20ae11350cf9f0adf
anchor-ref: refs/heads/main
base: 19d9b328c26ca41d9d275ef43abfa76f7efbef20

## Parked

2026-08-29T23:56:01Z review · item TOOL-aLexedStripper-1 · reason verdict BLOCKED · blockers 2

2026-08-29T23:56:22Z review · item TOOL-aLexedStripper-2 · reason verdict BLOCKED · blockers 2

2026-08-30T00:34:49Z review · item TOOL-aLexedStripper-1 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT

2026-08-30T00:34:56Z review · item TOOL-aLexedStripper-2 · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT

2026-08-30T00:35:21Z rescope · item add TOOL-aLexedStripper-5 · reason promoted from round-2 spec audit blocker 1+37 (NON-CONVERGENT exit): renderCodeView inherits blankLiterals' lack of a regex-literal mode, so a backtick inside a regex literal opens template mode and never closes, and S3's fail-closed branch then DENIES a legal script BASE admits. Reproduced: two shapes exit 0 at BASE and 2 under the prototype

2026-08-30T00:35:28Z rescope · item add TOOL-aLexedStripper-6 · reason promoted from round-2 spec audit blocker 26+30 (NON-CONVERGENT exit): no field of the six-field profile can express a Python f-string replacement field, whose braces hold real code. Reproduced: 73 ground-truth identifiers missed across 25 files in this repo, and -1's AC3 100% recall on selftest.py is unreachable by any implementation of the rev-2 design (measured 99.7%, sole miss 'or')
