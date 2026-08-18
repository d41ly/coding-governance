# aDeclaredBound - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 5709a6382a56a1d0a5511b8281273f206133f903
phase: ABORTED
branch-sha: 75a664fbeedf0e9b41bbde56194d14ee37bc018d
branch-ref: refs/heads/branch/adeclaredbound-unattended
anchor-kind: run-branch
keepalive: 99a615b5
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a
anchor-ref: refs/heads/main
base: 75a664fbeedf0e9b41bbde56194d14ee37bc018d
keepalive-reaped: yes
parked-surfaced: yes

## Parked

2026-08-18T10:39:26Z decision · item Which unit owns unit 5's S2/S2b/S3, given the ratified predicate cannot be satisfied at unit 5's own landing commit? · reason Options seen: (a) unit 5 asserts the pointer-SHAPE half only and unit 4 adds the reads-it half in the commit that makes the hook read the conf; (b) S2/S2b/S3 move wholesale into unit 4 and unit 5 lands digit-free prose only; (c) reverse the README order so unit 4 lands first, which reopens the window unit 5 exists to close. REFUSED because all three differ in WHAT EACH UNIT BUILDS, and M3 reserves a fork whose options differ in what gets built to the owner. The ratified choice itself is not in question -- only which unit carries it.

2026-08-18T10:39:34Z decision · item The two-round review cap is spent and the verdict is still BLOCKED. What is the disposition? · reason Options seen: (a) fold round 2's fixes and build anyway, which ships specs no round has called clean and is what M4's floor forbids; (b) park the build here and hand the owner both blockers; (c) the owner grants a third round, which only they can do since TOOL-aBoundedVerdict-1 makes the cap a driver constant owned by the owner for unattended runs. REFUSED (a) because building unreviewed specs is the failure M4 exists to prevent, and (c) because granting a third round is the owner's to grant. Taking (b). Note for the record: TOOL-aBoundedVerdict-1 identified M4's MISSING BLOCKED disposition as the loop's real engine, and that gap is still open -- this run is the first to reach the cap with a live BLOCKED verdict and had no ratified rule to follow.

2026-08-18T10:40:08Z abort · item aDeclaredBound · reason Two spec-audit rounds spent under TOOL-aBoundedVerdict-1's cap, both BLOCKED, and neither live blocker is mine to resolve. The first is a SCOPE question -- which unit owns unit 5's S2/S2b/S3, since the ratified predicate cannot be satisfied at unit 5's own landing commit -- and M3 reserves a fork whose options differ in what gets built to the owner. The second is my own defect: the gate measurement I published does not contain the pattern it reported, and AC1 pins the build to a figure no documented pattern reproduces; the record now carries an appended correction. No code was written and nothing was merged or pushed beyond the run branch the owner authorised.
