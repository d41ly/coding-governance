# aGroundedOrientation - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes, 3 surfaced
keepalive-reaped: yes
witness: ded172527621226aed8f4b9f3dcf78234ac084e2
phase: LANDED
landed-anchor: remote
landed-anchor-source: reconstructed 2026-08-27 by hand, not by the verb, following the precedent commit 7cf96591. `--landed` flipped this record to LANDED and THEN failed leg check 34 on a stale lander marker, leaving a terminal phase with no anchor kind; re-running it now refuses with check 26 because the record is finished, so no verb can write these keys. VERIFIED before writing: `git merge-base --is-ancestor ded17252 origin/main` is true, so the witness genuinely reached the remote default branch and `remote` is the true kind, not the convenient one.
unpushed-at-landing: 29
branch-sha: e62f6f32ddc0d102f3dba5dfdae64f763cbf90cf
branch-ref: refs/heads/branch/unattended-prompt-cg-toolkits-831d35
mode: prompt
anchor-kind: run-branch
keepalive: c25e22fa
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b4e1d5be879bc8868529fb57c15657e271c39113
anchor-ref: refs/heads/main
base: e62f6f32ddc0d102f3dba5dfdae64f763cbf90cf

## Parked

2026-08-27T11:30:07Z review · item 2026-08-27-review-TOOL-aGroundedOrientation-1-spec-audit-round1 · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-27T12:00:49Z rescope · item add TOOL-aGroundedOrientation-1 · reason The generated units region at the pinned BASE e62f6f32 held only TOOL-aGroundedOrientation-3, because units 1 and 2 had no spec yet and that region is RENDERED from specs. The authored roster table named all three from the first commit. Their specs were authored after preflight, so the region caught up and the driver correctly saw the executed roster grow. This is the defect this build exists to fix, occurring to the build itself: had orientation run its probes before step 3, all three specs would have existed at BASE.

2026-08-27T12:00:56Z rescope · item add TOOL-aGroundedOrientation-2 · reason The generated units region at the pinned BASE e62f6f32 held only TOOL-aGroundedOrientation-3, because units 1 and 2 had no spec yet and that region is RENDERED from specs. The authored roster table named all three from the first commit. Their specs were authored after preflight, so the region caught up and the driver correctly saw the executed roster grow. This is the defect this build exists to fix, occurring to the build itself: had orientation run its probes before step 3, all three specs would have existed at BASE.

2026-08-27T12:03:17Z decision · item dTieredTribunal's run-state file is non-terminal on main (phase LANDING), so UNATTENDED check 7 reds the bar for every subsequent run, including this one. Who finalizes it? · reason Node d closed that build and merged it — b4e1d5be IS its landing merge — but never ran --landed, so the record stopped at LANDING, which is not terminal. The kit's own Skill warns of exactly this: until the --landed record is committed, every later run counts yours as live and the bar reds on the second one. Options seen: (1) run --landed dTieredTribunal myself — ATTEMPTED and REFUSED, check 32, because the verb evaluates the CURRENT HEAD and that record names no branch-ref to fall back to, so it would compare my unlanded work against remote main; (2) hand-edit that record's phase — refused, it forges another node's run record and the whole point of a witnessed phase is that it is not assertable by a third party; (3) park it. Chose 3. This blocks THIS run's landing, not any of its units: the gates-green DoD item will need an override naming this, or node d re-runs --landed and commits the record. Not fixable inside this mandate's scope.

2026-08-27T13:38:34Z decision · item RESOLVED by owner, 2026-08-27: the check-7 LANDING red is not this run's to fix and clears at push-main. · reason Owner ruling in response to the parked question above. The dTieredTribunal run-state file sitting at phase LANDING on main reds UNATTENDED check 7 for every later run; the owner states it clears on push-main and instructed this run to proceed. This run therefore does NOT treat check 7 as a landing blocker and does NOT forge another node's record. Recorded here because a ruling that lives only in a transcript is a ruling nobody can audit, and because the earlier parked entry would otherwise read as still-open at wrap-up.

2026-08-27T17:58:37Z decision · item memory/guides/SESSION-KICKOFF.md is EFFECTIVELY FULL — 2 bytes under its 25600 cap after this merge. The next session that hits a trap cannot record it without evicting someone else's entry. Raise the cap, split the file, or accept that §B stops accreting? · reason Measured across three merges today. Before this run: 25118. After my trap entry: 25584, 16 bytes headroom, which I flagged then as a signal rather than a healthy state. After merging main, which added a GATE_BOUND bullet of its own: 26064, i.e. 464 OVER. Two nodes grew one hard-capped file in one afternoon. Options seen: (1) prune a dated correction — CHECKED, neither prune-when condition holds; 75e0e5c0 is gov dropping its own GATE_SELFTESTS, not the second-kit adoption that entry waits for; (2) remove another node's entry — refused, not mine to delete; (3) drop my own. Chose 3, and it is defensible beyond arithmetic: my entry documented a 963 s pre-commit leg, and the fix landing in this same merge makes it 54 s, so its primary fact is obsolete on arrival. The surviving half — a timed-out commit orphans its hook tree — is preserved in TOOL-aGroundedOrientation-3's spec and in this run's commit messages. What is NOT solved is the structural point: a document whose job is front-loading traps has no room to front-load the next one.

2026-08-27T18:46:45Z review · item aGroundedOrientation · reason verdict BLOCKED · blockers 2

2026-08-27T18:47:02Z review · item aGroundedOrientation · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED

2026-08-27T18:47:42Z override · item gates-green · reason Owner instructed 'merge to main without gates' on 2026-08-27, so the bar was not run for this landing and the pre-commit hook was bypassed on five commits, each recorded in its own message. Two reds this build created were found by the closing review and FIXED and pushed anyway (b0b1cb31): check 9's last-body-change threshold and check 5's stamp. One red remains on main and is NOT this build's: check-arms on the stale pin at memory/project/unarmed-branches.txt:42, verified green at BASE and red at f1be0b49 in its own worktree, with an empty diff on that file across this build's range.
