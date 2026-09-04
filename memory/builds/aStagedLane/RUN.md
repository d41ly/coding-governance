# aStagedLane - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 92a6f7fc31ba8c747cb0cfa74386bec2ae9eda83
phase: BUILDING
mode: slug
anchor-kind: default-branch
keepalive: 92d609a5
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: c4fcf5add1d0a553097f9eef70935a056896cf16
anchor-ref: refs/heads/main
base: c4fcf5add1d0a553097f9eef70935a056896cf16

## Parked

2026-09-04T19:08:12Z review · item aStagedLane-spec-set · reason verdict BLOCKED · blockers 4

2026-09-04T19:44:45Z review · item aStagedLane-spec-set · reason verdict BLOCKED · blockers 2

2026-09-04T19:51:56Z decision · item TOOL-aStagedLane-4 cannot be built inside memory/guides/BUILD-METHOD.md's declared byte budget. Raise M1's budget, name a sanctioned deletion that funds the edit, or drop the unit? · reason The guide is 24553 bytes against M1's declared 24576, leaving 23. Unit 4's S1 and S2 are both pure ADDITIONS: rev-2 planned to fund S1 by replacing an existing plan-verb mention, and there is none -- grep -- '--plan' over the guide returns nothing and its only driver mention is --resume at :204. The path literal tools/workflows/unattended-build.js that S2 must carry is 35 bytes by itself. Under S8 F1's owner ruling the method must also carry the mode SEMANTICS, which is larger again. Two fundings exist and both are owner turns under M3 veto 2: raising M1's budget, which M3 places inside that veto BY NAME, and deleting method prose to make room, which is a change to a governance carrier beyond the scope ratified at rev-2 -- the owner approved ADDING two names to the method, not removing anything from it. So no option survives the vetoes and the fork is parked rather than taking the least-bad one. Units 1 to 3 are unaffected and land.

2026-09-04T19:52:04Z rescope · item retire TOOL-aStagedLane-4 · reason Cannot be built inside M1's declared byte budget for memory/guides/BUILD-METHOD.md: 23 bytes remain and both of its scope items are pure additions, the path literal alone being 35. Both fundings are owner turns under M3 veto 2 -- raising the budget, which M3 names explicitly, and deleting method prose, which is a governance-carrier change beyond the rev-2 ratified scope. Parked for the owner rather than resolved; the decision is on the run-state file with all three options. Units 1 to 3 do not depend on it.

2026-09-04T20:16:17Z review · item aStagedLane-spec-set · reason verdict BLOCKED · blockers 1

2026-09-04T20:51:00Z review · item aStagedLane-spec-set · reason verdict BLOCKED · blockers 3 · NON-CONVERGENT · disposition fold

2026-09-04T20:54:12Z dispatch · item 92a6f7fc TOOL-aStagedLane-1 · reason tools/unattended/check-pass-order.sh tools/unattended/check-pass-order.test.sh tools/unattended/run-unattended-gates.sh tools/gate-legs.json memory/project/pass-order-waiver.txt .memory-tree.conf
