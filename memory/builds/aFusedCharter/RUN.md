# aFusedCharter - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: e1919b284f0eb6fe70cd5961269ea44117cdfda5
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

2026-08-18T15:21:21Z decision · item PLAY-aFusedCharter-3 is started but not landed, and gov's deploy.toml is written outside the repo · reason S1 through S3 must land in ONE commit — a tree with the rendered region added and the authored gate-suite section still present states the bar twice, and the wiring leg reds on a descriptor with no region. The descriptor is written and held at ~/.gov-hold/deploy.toml with every answer filled and verified to render clean. What remains is the 26 KB admission cut over the gate-suite section, which is a substantial authored edit. Options seen: land the region alone (rejected, it reds the bar and states the bar twice), commit the descriptor alone (rejected for the same red), or hold both for one whole pass (taken).

2026-08-18T15:36:28Z decision · item TOOL-aFusedCharter-2's self-test has not been observed passing end to end · reason Every arm that has reported is ok and none has failed, but this node has degraded to where 14 invocations of a git-rooted gate exceed the tool timeout, so no single run has printed its PASS line. Options seen: commit the harness on partial evidence (refused — a gate is not landed until its failing case has been observed, and that rule does not weaken because the machine is slow), reduce the arm count to fit the clock (refused — the arms ARE the coverage), or run it detached and commit on its verdict (taken, in flight).
