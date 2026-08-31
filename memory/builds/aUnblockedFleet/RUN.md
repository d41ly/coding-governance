# aUnblockedFleet - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 6b76b5fc00c3404585a1e7b0e9f309f32b91b9fd
phase: BUILDING
branch-sha: 117de044094bc7ac729358edfc24541ba3a1486a
branch-ref: refs/heads/branch/unattended-builds-blocking-640d0d
mode: prompt
anchor-kind: run-branch
keepalive: 6a6fb940
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 396cd9db154f1621db5cb4cde72b93470b2f690c
anchor-ref: refs/heads/main
base: 117de044094bc7ac729358edfc24541ba3a1486a

## Parked

2026-08-30T23:55:59Z review · item spec-set · reason verdict BLOCKED · blockers 3

2026-08-30T23:58:31Z rescope · item add TOOL-aUnblockedFleet-6 · reason spec audit round 1 blocker B1: the merge bar's repo-wide turnstile (run-gates.sh:415-441, GATE_TURNSTILE default 1, keyed on git-common-dir) serializes two concurrent --close bars in one clone, and the queue wait sits INSIDE the run's declared GATE_BOUND=3600 while TS_MAXWAIT derives to >=7200s. Removing the two run-state checks alone therefore moves the wedge from STARTING to CLOSING rather than removing it.

2026-08-31T02:48:50Z review · item spec-set · reason verdict BLOCKED · blockers 3 · NON-CONVERGENT

2026-08-31T02:49:23Z rescope · item retire TOOL-aUnblockedFleet-6 · reason spec-audit round 2 refuted all three of its mechanisms, each verified against source: S5 names <git-common-dir>/gate-queue-status but run-gates.sh:686 writes $gd, which is git rev-parse --git-dir and therefore PER-WORKTREE, so on the sibling-worktree layout this build exists for the driver would stat a path nothing writes; :692 deletes that file on both exits from the wait loop, before the bar runs, so the state S5 reports is unreachable; and the GATE_BOUND/4 derivation gives a 900s queue bound against a measured 1560s bar, so a queued close NEVER acquires and always runs contended, which is exactly what this spec's own section 3 rejected GATE_TURNSTILE=0 for. The loop is NON-CONVERGENT at 3 blockers both rounds, so a corrected design cannot be re-reviewed, and M3's rule is no survivors means PARK rather than the least-bad option. The PROBLEM is real and stays on the record as a parked decision and a backlog row.

2026-08-31T02:49:39Z decision · item The merge bar's repo-wide turnstile can still make two concurrent unattended CLOSES contend, and the fix needs an owner turn this run could not take. · reason OPTIONS SEEN. (1) Bound the turnstile queue wait inside GATE_BOUND: specced as unit 6, refuted by spec-audit round 2 on three verified mechanisms — the queue-status path is per-worktree not per-common-dir, the file is deleted before the bar can be killed, and GATE_BOUND/4 at 900s against a 1560s bar means the queued close never acquires and always runs contended, which is disabling the turnstile by another name. (2) Raise GATE_BOUND to absorb queue time: rejected, it is a HANG detector sized by TOOL-aBoundedCeiling-6 after a 3h19m hang and absorbing contention restores that blindness. (3) The property actually needed, which round 2 named and this run did not have a reviewed design for: GATE_BOUND minus the queue bound must exceed a CONTENDED bar, not an uncontended one, and nobody has measured a contended bar on this fleet. WHY REFUSED. The review loop is NON-CONVERGENT at 3 blockers in both rounds, so M4 forbids re-reviewing a corrected design, and building an unreviewed design whose three core mechanisms were each refuted is worse than not building it. M3's rule at that point is park, never the least-bad option. WHAT SHIPPED INSTEAD. Units 1 to 5, which remove the START-time block the owner asked about. The close-time contention is a pre-existing property of run-gates.sh that those units make REACHABLE rather than create, it is strictly narrower than what they remove — a close is a moment, a live run is the whole build — and it is filed as a backlog row carrying both rounds' evidence.

2026-08-31T13:01:50Z decision · item The closing diff review is SINGLE-ROUND by owner instruction, so any blocker it confirms is folded without a review of the fix. · reason Owner instruction 2026-08-31: no tier-2 review after the one now running. BUILD-METHOD M8 requires 'fix every blocker, then re-review the FIX, not the diff again', and that second pass will not happen. WHAT THAT COSTS: a fold is unreviewed by definition, so a blocker fixed badly, or a fix that introduces a new defect, lands unobserved by anything except the merge bar. The bar catches what the bar catches -- structure, arms, parity, drift -- and a review exists precisely for what it cannot. WHAT REDUCES THE EXPOSURE: this build already ran TWO full spec-audit rounds over the same code before a line of it was written, every finding from both was verified against source by hand rather than taken on trust, and the driver half is evidenced by a passing suite plus two staged breaks observed RED. WHAT DOES NOT: the leg self-test suite was skipped by a separate instruction, so four acceptance criteria are already unmet, and the closing review was the remaining independent check over that same code. The two skips compound rather than overlap.
