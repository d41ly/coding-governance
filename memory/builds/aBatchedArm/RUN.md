# aBatchedArm - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
halt-code: scope-approval-needed
parked-surfaced: yes, 1 surfaced
keepalive-reaped: yes
witness: c777c7898b74f2bada5f87d31634b80bb44a2bf5
phase: ABORTED
branch-sha: e9ed269bc7ae7a7a5453156eff5431abf7280bcc
branch-ref: refs/heads/branch/unattended-checks-performance-a37d8d
mode: prompt
anchor-kind: run-branch
keepalive: c2b564d8
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: fdd754bf62d1833361350ab7cb0b0f393027d99a
anchor-ref: refs/heads/main
base: e9ed269bc7ae7a7a5453156eff5431abf7280bcc

## Parked

2026-09-10T10:55:53Z review · item TOOL-aBatchedArm-1 · reason verdict BLOCKED · blockers 3

2026-09-10T10:58:32Z rescope · item add TOOL-aBatchedArm-2 · reason spec-audit round 1 named one structural group linter as the left-shift for five of its six findings. It grades the LINKAGE between a group's emitted set and its miss/same arms, which TOOL-aBatchedArm-1 states as a rule and cannot enforce per group. A separate mechanism under M2, so a unit rather than a scope item.

2026-09-10T11:30:16Z review · item TOOL-aBatchedArm-1 · reason verdict BLOCKED · blockers 13 · NON-CONVERGENT · disposition fold

2026-09-10T11:31:16Z rescope · item add TOOL-aBatchedArm-3 · reason Round 2 killed the admissibility rule: only 6 of 29 check numbers carry a single branch (16 carries 34, 28 carries 31), so a fired check number witnesses one of up to 34 branches and cannot witness the one a miss control is about. Excluding miss and same arms as TOOL-dScriptedRepeat-15 S3 requires leaves 95 blocks carrying 136 solo invocations, which is 36 minutes before any batch runs. MEASURED: batching alone reaches 40 to 44 minutes unsharded and misses the 20-minute goal at every group size. Raising SHARD_ARITY from 2 to 8 reaches about 10 minutes with no new mechanism and no unsound oracle, is already owner-ruled 2026-08-29 under TOOL-aGradedDoorway-7 S2, and carries assertion-count identity as its control. Adopted under protocol section 11 rather than parked: it makes the measured observable strictly better, makes nothing worse, and trips no M3 veto.

2026-09-10T12:12:44Z review · item TOOL-aBatchedArm-3 · reason verdict BLOCKED · blockers 8

2026-09-10T12:13:27Z decision · item The 20-minute target is not reachable inside this build's declared scope. Which way should it widen: change the shared runner tools/run-gates/run-selftests.sh, give this kit its own parallel shard runner in tools/unattended/run-unattended-gates.sh, or lower the target? · reason THREE UNITS, THREE BLOCKED AUDITS, ALL ON MEASURED GROUNDS. Batching (TOOL-aBatchedArm-1) measures 40 to 44 minutes because TOOL-dScriptedRepeat-15 S3 forbids batching the 128 control assertions, leaving 95 blocks carrying 136 solo invocations. Its linter (TOOL-aBatchedArm-2) depends on it. Sharding (TOOL-aBatchedArm-3) is blocked three ways, each verified in the tree by me and not taken on the lens's word: (1) eight budget rows CANNOT BE DECLARED - run-selftests.sh:357-361 word-splits argv and feeds every slash-bearing token to git ls-files --error-unmatch, so a --shard 1/8 token reds the always-on budget-row leg, and --shard=1/8 is refused by the suite's own parser, so no escape spelling exists; (2) the consumer is SERIAL - run-unattended-gates.sh:263 calls run-selftests.sh with no flag and run-selftests.sh:296 sets OUTER=1 except under --sweep, which withholds every cost verdict, so the mode that would show 20 minutes grades no cost and the mode that grades cost gets no speed-up; (3) my zero-cross-region-variable measurement READ THE WRONG CARRIER - the coupling is git REF state, and check-unattended.test.sh:1277-1293 already hand-replays it for the two-way split, saying an eight-way one would owe seven more such replays, all unbudgeted. OPTIONS SEEN. (a) Make run-selftests.sh pool in its default mode and make its row checker slash-tolerant. Reaches the goal and touches a shared runner that grades 61 suites, which is M3 veto 2 and an owner turn. (b) Give this kit its own bounded shard runner inside run-unattended-gates.sh, which is in scope and avoids veto 2, but re-splits the self-test budget ownership that TOOL-aQuenchedHarness-4 deliberately centralised, and needs its own spec and audit. (c) Lower or re-declare the target. WHY I REFUSED. Option (a) trips veto 2 and M3 says a fork whose only survivor trips a veto is parked exactly as if nothing survived. Option (b) is mine to take but reverses a recorded centralisation decision, which is a scope call rather than a design one. Option (c) is never a run's to make.

2026-09-10T12:15:02Z abort · item aBatchedArm · reason The 20-minute target is unreachable inside this build's declared scope, and every way out needs an owner scope decision this run may not take. Three units, four spec audits, all BLOCKED on measured grounds. Batching measures 40 to 44 minutes because TOOL-dScriptedRepeat-15 S3 forbids batching the 128 control assertions. Sharding cannot be declared at all: run-selftests.sh:357-361 reds any slash-bearing argv token so a --shard 1/8 row fails the always-on budget leg, the consumer runs serial (OUTER=1 except under --sweep, which withholds cost verdicts), and the region coupling is git REF state which check-unattended.test.sh:1277 already hand-replays once and an eight-way split would owe seven more. WHAT I REFUSED TO DECIDE: whether to change tools/run-gates/run-selftests.sh, a shared runner grading 61 suites, which is M3 veto 2 and an owner turn; or to give this kit its own shard runner in run-unattended-gates.sh, which is in scope but reverses TOOL-aQuenchedHarness-4's deliberate centralisation of self-test budgets; or to lower the target, which is never a run's call. The full question and options are the parked entry. WHAT THIS RUN DID LAND, on the branch and not merged: a repaired fixture defect (0f89c5c4) whose DISPOSITION_CUTOFF announcement had silently redded 14 arms across both shards, and the regression that repair introduced (105f777a), both verified by before-and-after FAIL-set diffs on frozen clones. Three specs are written, folded and audited; none is built.
