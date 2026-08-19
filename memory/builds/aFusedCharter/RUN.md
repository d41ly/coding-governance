# aFusedCharter - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 6bd71de83e92df00bea8be05c5eb31b3814808a8
phase: LANDED
branch-sha: bd6dd7f6a4aad362b47591f79386aab75f7ba448
branch-ref: refs/heads/branch/governance-template-convergence-91c2c6
anchor-kind: run-branch
keepalive: e04576b5
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a
anchor-ref: refs/heads/main
base: bd6dd7f6a4aad362b47591f79386aab75f7ba448

keepalive-reaped: yes
parked-surfaced: yes

## Parked

2026-08-18T12:32:10Z decision · item The full bar has not completed a green run in this session · reason It exceeds 10 minutes on node a against 4139 stale scratch dirs in TMPDIR, which is the documented environment trap; every leg this pass touches was run individually and is green, but the authoritative full run is owed before landing and no run in this session produced one. Options seen: keep retrying inside a single tool call (rejected, it exceeds the wall-clock limit), run it detached across turns (the resumption's job), or land without it (refused).

2026-08-18T12:45:49Z decision · item DEPL-aFusedCharter-1 landed in slices and three scope items are unbuilt · reason S1c's duplicate-id predicate for govkit selfcheck, S5's fifth column in marker-contract.test.sh, and the kit's own test are specced and not yet written. Options seen: hold the commit until the unit is whole (rejected — a stalled run would then leave nothing on disk for the next one to resume from), or commit the working engine and name the residue (taken). The engine is proven by effect on a fixture and every gate it currently trips is green.

2026-08-18T15:21:21Z decision · item PLAY-aFusedCharter-3 is started but not landed, and gov's deploy.toml is written outside the repo · reason S1 through S3 must land in ONE commit — a tree with the rendered region added and the authored gate-suite section still present states the bar twice, and the wiring leg reds on a descriptor with no region. The descriptor is written and held at ~/.gov-hold/deploy.toml with every answer filled and verified to render clean. What remains is the 26 KB admission cut over the gate-suite section, which is a substantial authored edit. Options seen: land the region alone (rejected, it reds the bar and states the bar twice), commit the descriptor alone (rejected for the same red), or hold both for one whole pass (taken).

2026-08-18T15:36:28Z decision · item TOOL-aFusedCharter-2's self-test has not been observed passing end to end · reason Every arm that has reported is ok and none has failed, but this node has degraded to where 14 invocations of a git-rooted gate exceed the tool timeout, so no single run has printed its PASS line. Options seen: commit the harness on partial evidence (refused — a gate is not landed until its failing case has been observed, and that rule does not weaken because the machine is slow), reduce the arm count to fit the clock (refused — the arms ARE the coverage), or run it detached and commit on its verdict (taken, in flight).

2026-08-18T16:58:28Z decision · item Orphaned gate-leg processes from earlier killed bar runs are still live and competing with the current one · reason Processes are still executing against the scratch dirs of bars 4 and 5, which died on the cygwin fork failure; four orphan scratch dirs hold 64-69 entries each. That is why every leg is slow and why two runs exceeded the tool clock. Options seen: blanket-kill matching processes (REFUSED — the charter's own rule is to kill a target by identity and never blanket-kill every process of a runtime, and I cannot prove every match is mine), delete the scratch dirs (refused while live processes hold them), or let the current run finish slowly and leave the cleanup to the owner (taken). The stale-TMPDIR trap in the charter documents the disk half of this; the live-orphan half is not yet recorded anywhere and is worth a gotcha.

2026-08-18T18:00:23Z decision · item The M8 closing diff review has zero coverage after five runs, and the build is held open rather than closed · reason Twenty lens attempts across five workflow runs, every one dead on API 529 Overloaded, so nothing has read the cumulative bd6dd7f..HEAD diff. M8 makes that review mandatory before a build closes. The owner directed a retry each time and the last direction was to retry again, which was done and failed identically. Options seen and their costs: close with the DoD item overridden (available and visible in this file, but it lands a 53-file diff no adversarial pass has read); substitute a self-review (not zero coverage, but I would be reviewing my own work and it is not what M8 requires); hold the build open at BUILDING with everything committed (TAKEN — nothing is lost, all seven units are built and each was verified against its own gates as it landed, and the review costs only a retry once the API recovers). Resume with: Workflow scriptPath tools/workflows/tier2-review.js, resumeFromRunId wf_c6bc1036-ec2. No lens has ever completed, so nothing is cached and a recovery shows immediately.

2026-08-19T01:37:58Z decision · item The merge to main is reconciled but NOT completed: it surfaces 5 govkit selftest failures neither parent has · reason main moved to bba7422 while this build ran, adding a run-gates kit. Two conflicts reconciled additively and verified: the waiver file keeps main's run-gates row and drops the hooks row this build made stale, and govkit selftest's arm combines each side's operand (write|seed 3 from here, ORDER 4 from main). playbook-parity and govkit selfcheck both green after that. But govkit selftest then reports 5 INTEGRATION failures that neither parent had alone, starting with 'the playbook entry lands its one file' landing nothing — most likely the playbook_path answer the renderer now requires is not supplied by the selftest's own fixture. Options seen: complete the merge red (REFUSED — a conflict-free merge is not a passing merge, and the post-merge gate is the rule this build spent a day honouring), leave the primary tree half-merged (refused — worse than either end state), or abort and hand a clean primary tree plus an intact pushed branch to the next session (TAKEN). Nothing is lost: the branch is pushed, phase is LANDING, DoD is met with no overrides, and the reconcile is a ten-minute redo with the answers recorded here.

2026-08-19T08:34:53Z abort · item aFusedCharter · reason This run reconciled the merge to main and then aborted it red rather than complete it, handing a clean primary tree and an intact pushed branch to the next session; that session completed the merge at 056331b and the seven specs closed at a3ec54d, so this run itself landed nothing and its record is terminal. LANDED is not available and would not be true: the merge sits on local main only, so the witness is an ancestor of no tip the remote advertises, and the driver's own --landed verb refuses on exactly that test.

2026-08-19T19:04:01Z decision · item aFusedCharter · reason phase set from ABORTED to LANDED BY HAND, on the owner's explicit instruction given after they were shown that the kit refuses this transition. Both `--landed` and `--phase` refused with check 26 (a finished record is not something to move, re-open or re-pin), and memory/guides/UNATTENDED-PROTOCOL.md states that a run already terminal cannot be moved at all. This edit therefore bypasses check 26 deliberately; it is the owner's call and not the kit's, and it is recorded here rather than left to be inferred from a diff. What is independently verifiable for THIS run: it reached LANDING with its Definition of Done met at 7d80591, and its witness 6bd71de8 is an ancestor of the remote tip 033b454, so check 15's witness test passes on the merits rather than by construction. The abort note above is superseded on one point only -- the merge no longer sits on local main alone, it reached origin at 033b454.
