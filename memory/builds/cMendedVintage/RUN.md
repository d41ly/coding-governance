# cMendedVintage - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 859daa67e728ae273d5278536fb462c04077f16f
phase: RUNNING
branch-sha: 859daa67e728ae273d5278536fb462c04077f16f
branch-ref: refs/heads/branch/govkit-update-rollbacks-0502c4
mode: prompt
run-branch: refs/heads/branch/govkit-update-rollbacks-0502c4
anchor-kind: run-branch
keepalive: 84ee75f8
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 4cf0944dbdce94714870f26760936bc5edabc64e
anchor-ref: refs/heads/main
base: 859daa67e728ae273d5278536fb462c04077f16f

## Parked

2026-09-16T12:43:39Z decision · item The charter's §16 R1 requires an emitted micro-format to be a markdown list item ('- ' at column 0), but skills/session-kickoff/manifest-check.sh:478 counts READY lines with grep -c '^READY — ', anchored at column 0 with no list marker. A card body that follows the charter is read as carrying NO ready line: the append reports success, leaves the 'READY — none yet' sentinel in place, skips the tree-cell re-render, and the scratch-guard then blocks the session's next commit. · reason Two options and both change a governance carrier, which M3 veto 2 reserves to the owner. Either §16 R1 gains an explicit carve-out for a machine-read on-disk record, or manifest-check.sh accepts an optional leading '- ' on the lines it anchors. I will not pick: the charter is the carrier this repo is most careful about, and the fix is one line either way. Observed live this run — it cost 71 minutes and a refused commit.

2026-09-16T12:43:51Z rescope · item add TOOL-cMendedVintage-9 · reason Building uncovered it: manifest-check.sh:128 resolves the session id by reading stdin for the SessionStart hook's JSON, guarded only by '[ -t 0 ]'. That covers the hook (pipe then EOF) and a human at a terminal, but not stdin being an open pipe that never sends EOF — which is what every tool-invoked shell has. --card --write then blocks in sed forever: measured 71 minutes at 4.4s CPU with no children, cleared instantly with '< /dev/null'. Passing --session does not avoid it, because the stdin read runs first and CARD_SID is only the fallback. The skill's own Step 5 prescribes this exact invocation as the card repair, so the documented remedy hangs. Strictly beneficial, no veto tripped (a kit engine, not a governance carrier), and it is a blocker between this run and its own landing.
