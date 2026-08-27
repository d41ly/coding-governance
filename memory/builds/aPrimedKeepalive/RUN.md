# aPrimedKeepalive - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: b944720cb81d1626e53712f484790aa0a7f2e5f4
phase: REVIEWING
branch-sha: 0e92aaa9ec0006c285eb96b26a0d851a1d496b75
branch-ref: refs/heads/branch/unattended-keepalive-orientation-493b93
mode: prompt
anchor-kind: run-branch
keepalive: 8191840b
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b4e1d5be879bc8868529fb57c15657e271c39113
anchor-ref: refs/heads/main
base: 0e92aaa9ec0006c285eb96b26a0d851a1d496b75

## Parked

2026-08-27T11:55:19Z rescope · item add TOOL-aPrimedKeepalive-7 · reason Observed while verifying unit 3 AC6: the DRIVER's check_single_live refuses --preflight with 2 live records, so dTieredTribunal at LANDING blocks the next run on this repo even after unit 4 fixes the LEG. Unit 4's section 3 named this a non-goal on a reading of the code that is false. Strictly beneficial by protocol section 11: measured, nothing gets worse, no veto tripped.

2026-08-27T12:20:29Z review · item aPrimedKeepalive-specs · reason verdict BLOCKED · blockers 4

2026-08-27T12:56:03Z review · item aPrimedKeepalive-specs · reason verdict BLOCKED · blockers 1

2026-08-27T13:31:47Z review · item aPrimedKeepalive-specs · reason verdict BLOCKED · blockers 2 · NON-CONVERGENT

2026-08-27T13:32:12Z rescope · item add TOOL-aPrimedKeepalive-8 · reason PROMOTED from spec-audit round 3, NON-CONVERGENT: SKILL.template.md:35 asserts a resumed keepalive is dead before it starts while :589 of the same file calls that intuition MEASURED FALSE, 554 lines apart, with the false half in the section every path reads first. Same defect at README.md:176.

2026-08-27T13:32:16Z rescope · item add TOOL-aPrimedKeepalive-9 · reason PROMOTED from spec-audit round 3, NON-CONVERGENT: every acceptance criterion a fold ADDED is unevidenced in the ledger — unit 1 AC8/AC9, unit 2 AC9, unit 4 AC6, unit 6 AC5 — while unit 7's fold-added AC6 is evidenced, so it is an omission rather than a convention. Hygiene check 23 reds the push boundary the moment those units flip to CLOSED.

2026-08-27T15:13:54Z review · item aPrimedKeepalive · reason verdict BLOCKED · blockers 2
