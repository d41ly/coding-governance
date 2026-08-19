# aBoundedVerdict - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 60afa42dfaf8c6a43547d4a0f69c73b6fa8bb072
phase: RUNNING
anchor-kind: default-branch
keepalive: e7a1f734
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b482cdca6466a56d77d96f7726a566ece19bacc9
anchor-ref: refs/heads/main
base: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a

## Parked

2026-08-19T07:06:41Z decision · item the closing review's base, now that the run has merged origin/main · reason M8 says review from the run's PINNED BASE; the pin (098bebd9) now predates a merge that brought in an entire landed build (aPacedTurnstile, ~25 commits). A literal BASE..HEAD would review another node's landed work as if this run wrote it. Options seen: the literal pin, per M8; the merge-base with the reconciled main, which is this run's actual diff; or a two-part review. Taking the merge-base sha and recording it here rather than silently reinterpreting a binding instruction.
