# aFusedCharter - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: ac158844225c03d2216fd3b82ecd128d5cad3701
phase: BUILDING
branch-sha: bd6dd7f6a4aad362b47591f79386aab75f7ba448
branch-ref: refs/heads/branch/governance-template-convergence-91c2c6
anchor-kind: run-branch
keepalive: e04576b5
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a
anchor-ref: refs/heads/main
base: bd6dd7f6a4aad362b47591f79386aab75f7ba448

## Parked

2026-08-18T12:32:10Z decision · item The full bar has not completed a green run in this session · reason It exceeds 10 minutes on node a against 4139 stale scratch dirs in TMPDIR, which is the documented environment trap; every leg this pass touches was run individually and is green, but the authoritative full run is owed before landing and no run in this session produced one. Options seen: keep retrying inside a single tool call (rejected, it exceeds the wall-clock limit), run it detached across turns (the resumption's job), or land without it (refused).

2026-08-18T12:45:49Z decision · item DEPL-aFusedCharter-1 landed in slices and three scope items are unbuilt · reason S1c's duplicate-id predicate for govkit selfcheck, S5's fifth column in marker-contract.test.sh, and the kit's own test are specced and not yet written. Options seen: hold the commit until the unit is whole (rejected — a stalled run would then leave nothing on disk for the next one to resume from), or commit the working engine and name the residue (taken). The engine is proven by effect on a fixture and every gate it currently trips is green.
