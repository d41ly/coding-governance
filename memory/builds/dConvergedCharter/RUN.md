# dConvergedCharter - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
asks-at-landing: PLAY-dConvergedCharter-24=DEFERRED PLAY-dConvergedCharter-25=DEFERRED PLAY-dConvergedCharter-26=DEFERRED PLAY-dConvergedCharter-27=DEFERRED PLAY-dConvergedCharter-28=DEFERRED PLAY-dConvergedCharter-29=DEFERRED PLAY-dConvergedCharter-30=DEFERRED PLAY-dConvergedCharter-31=DEFERRED PLAY-dConvergedCharter-32=DEFERRED PLAY-dConvergedCharter-33=DEFERRED PLAY-dConvergedCharter-34=DEFERRED PLAY-dConvergedCharter-35=DEFERRED PLAY-dConvergedCharter-36=DEFERRED PLAY-dConvergedCharter-37=DEFERRED
units-at-landing: PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18
gates-run: unattended-17938053573705645701-600 fb0dd91f
parked-surfaced: yes, 26 surfaced
keepalive-reaped: yes
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: b2ba51d4f0ec8c886f97d429de1a406131074ca4
phase: LANDING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-dconvergedcharter-51d347
anchor-kind: default-branch
cli-version: 2.1.309
lease-utc: 2026-11-03T21:33:36Z
pid-image: claude.exe
host: compeeto
pid: 29032
session: 782d04e7-a4ed-4756-844e-e9fa31ed9d15
keepalive: 595080b7
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 0d1c1dda4b5656df0a6341dba492ae1f75e8bd61
anchor-ref: refs/heads/main
base: 0d1c1dda4b5656df0a6341dba492ae1f75e8bd61

## Parked

2026-11-04T10:30:39Z rescope · item add PLAY-dConvergedCharter-38 · reason closes 2026-11-04 spec-audit round1 finding 45 (MEDIUM): derive_readers reads the memory root live carriers from the dead-path gate one list

2026-11-04T10:30:44Z rescope · item add PLAY-dConvergedCharter-39 · reason closes 2026-11-04 spec-audit round1 finding 44 (MEDIUM): the renamed gov- Skills claimed in the codebase-map dossiers, a drift-audit dossier added

2026-11-04T11:25:10Z review · item dConvergedCharter-spec-set-r1 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 11 · minors 44 · folded 53 · promoted 2 · disposition promote

2026-11-04T12:20:47Z rescope · item add PLAY-dConvergedCharter-40 · reason closes 2026-11-04 spec-audit PLAY-dConvergedCharter-22 round1 finding 27 (MEDIUM): guide_move.py apply amends an existing unit's help and edge under an edit change record

2026-11-04T12:57:03Z review · item dConvergedCharter-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 9 · minors 31 · folded 39 · promoted 1 · disposition promote

2026-11-04T13:16:28Z rescope · item defer PLAY-dConvergedCharter-1 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:29Z rescope · item defer PLAY-dConvergedCharter-10 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:30Z rescope · item defer PLAY-dConvergedCharter-11 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:31Z rescope · item defer PLAY-dConvergedCharter-12 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:31Z rescope · item defer PLAY-dConvergedCharter-13 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:32Z rescope · item defer PLAY-dConvergedCharter-14 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:33Z rescope · item defer PLAY-dConvergedCharter-15 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:33Z rescope · item defer PLAY-dConvergedCharter-16 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:34Z rescope · item defer PLAY-dConvergedCharter-17 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:35Z rescope · item defer PLAY-dConvergedCharter-18 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:35Z rescope · item defer PLAY-dConvergedCharter-19 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:36Z rescope · item defer PLAY-dConvergedCharter-2 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:37Z rescope · item defer PLAY-dConvergedCharter-20 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:37Z rescope · item defer PLAY-dConvergedCharter-21 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:38Z rescope · item defer PLAY-dConvergedCharter-22 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:39Z rescope · item defer PLAY-dConvergedCharter-23 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:40Z rescope · item defer PLAY-dConvergedCharter-3 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:40Z rescope · item defer PLAY-dConvergedCharter-4 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:41Z rescope · item defer PLAY-dConvergedCharter-5 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:42Z rescope · item defer PLAY-dConvergedCharter-6 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:43Z rescope · item defer PLAY-dConvergedCharter-7 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:43Z rescope · item defer PLAY-dConvergedCharter-8 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:44Z rescope · item defer PLAY-dConvergedCharter-9 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:45Z rescope · item defer PLAY-dConvergedCharter-38 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:45Z rescope · item defer PLAY-dConvergedCharter-39 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T13:16:46Z rescope · item defer PLAY-dConvergedCharter-40 · reason spec run (README rule 1): specced here, the spec audit's chain stopped at round 2 on its own verdict (STOP, own-work), carried forward DEFERRED against PLAY-dConvergedCharter-24 for the build run to build

2026-11-04T15:35:53Z override · item specs-audited · reason the spec-audit chain stopped on its own verdict at round 2 (STOP, own-work), and --chain-verdict names PLAY-dConvergedCharter-40, the round-2 promotion, to close under this override; the build run builds it from its spec as written

2026-11-04T15:35:53Z override · item closing-review-recorded · reason a spec run writes no code, so its diff is specs and records only; the two-round spec-audit chain recorded in the chain record is the review of this spec-only diff, the disposition every chain spec run's close takes (PLAY-dClosedLoop-37)
