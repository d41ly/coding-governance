# aBatchedMinors - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 3c119504015294d72ad6eb626422fd19781e3728
phase: BUILDING
branch-sha: 5ba0fc4fcdab79eeeb7f75a97a48102bb10bfefa
branch-ref: refs/heads/branch/unattended-closing-review-promotion-227ff0
may: none
mode: prompt
run-branch: refs/heads/branch/unattended-closing-review-promotion-227ff0
anchor-kind: run-branch
lease-utc: 2026-10-04T15:32:08Z
pid-image: claude.exe
host: compeeto-agent
pid: 6980
session: abecbd71-5777-4b59-88f7-f6dba672a289
keepalive: 9b5c6b93
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: ac65de998f094a244540905b35d7c5f6880ab850
anchor-ref: refs/heads/main
base: 5ba0fc4fcdab79eeeb7f75a97a48102bb10bfefa

## Parked

2026-10-04T15:36:50Z rescope · item retire TOOL-aBatchedMinors-1 · reason speccing found the harness return already determines the count: blockers and highs are integers only when every confirmed id sits in one severity, so MEDIUM+LOW = confirmed - blockers - highs exactly, the arithmetic unattended-build.js already uses; a minors key would be a second answer to one question

2026-10-04T15:37:52Z brief · item TOOL-aBatchedMinors-2 · reason f28c9e08ab1d memory/builds/aBatchedMinors/prompts/2026-10-04-prompt-TOOL-aBatchedMinors-2-1-build-brief.md

2026-10-04T15:37:55Z brief · item TOOL-aBatchedMinors-3 · reason cce2874fc3d6 memory/builds/aBatchedMinors/prompts/2026-10-04-prompt-TOOL-aBatchedMinors-3-1-build-brief.md

2026-10-04T15:37:58Z brief · item TOOL-aBatchedMinors-4 · reason 7cdfd7ea7b00 memory/builds/aBatchedMinors/prompts/2026-10-04-prompt-TOOL-aBatchedMinors-4-1-build-brief.md
