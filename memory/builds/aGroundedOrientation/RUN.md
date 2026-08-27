# aGroundedOrientation - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: e62f6f32ddc0d102f3dba5dfdae64f763cbf90cf
phase: RUNNING
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
