# dQuietDisk - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: a0ae4dcac415bfab8de7cce5da6423311a25a39e · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: c95ef6216483338ec4c2b9b18817188b74d95d8d
phase: RUNNING
may: none
mode: prompt
run-branch: refs/heads/branch/disk-churn-fixes-40450b
anchor-kind: local
cli-version: 2.1.326
lease-utc: 2026-11-20T10:19:49Z
pid-image: claude.exe
host: compeeto
pid: 18856
session: 0840beea-0651-4dc3-9fe7-f227915b6b42
keepalive: c0718341
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: a0ae4dcac415bfab8de7cce5da6423311a25a39e
anchor-ref: refs/heads/main
base: c95ef6216483338ec4c2b9b18817188b74d95d8d

## Parked

2026-11-20T11:11:30Z rescope · item add TOOL-dQuietDisk-26 · reason TOOL-dQuietDisk-10 F1 resolved (b): check-wiring.sh re-lists the tree per check (1,679 ls-files and 421 check-attr of the suite's 3,786 git processes); one listing per invocation is its own mechanism (M2)

2026-11-20T11:33:40Z decision · item every unit waits for dWitnessedBar's landing (37 of 88 units closed at 2026-11-20 12:00, order 23 of 50 building) · reason options: (a) --hold, refused by its vocabulary: HOLD_CODES_CORE holds host, platform, owner and inherited-red codes and none names a wait on another build; (b) build the non-overlapping units first, refused: only TOOL-dQuietDisk-4's write set avoids dWitnessedBar's diff and it reads unit 1's store, whose files overlap; (c) wait RUNNING on the 10-minute idle-wake, re-ground every spec on the landed tip (unit 19 to the last order), take the B0 readings there, then dispatch by order — taken
