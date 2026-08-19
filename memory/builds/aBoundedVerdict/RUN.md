# aBoundedVerdict - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 2dd297dfd0a76e7f672ad85b8fc6fbfd22c06258
phase: BUILDING
anchor-kind: default-branch
keepalive: e7a1f734
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: b482cdca6466a56d77d96f7726a566ece19bacc9
anchor-ref: refs/heads/main
base: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a

## Parked

2026-08-19T07:06:41Z decision · item the closing review's base, now that the run has merged origin/main · reason M8 says review from the run's PINNED BASE; the pin (098bebd9) now predates a merge that brought in an entire landed build (aPacedTurnstile, ~25 commits). A literal BASE..HEAD would review another node's landed work as if this run wrote it. Options seen: the literal pin, per M8; the merge-base with the reconciled main, which is this run's actual diff; or a two-part review. Taking the merge-base sha and recording it here rather than silently reinterpreting a binding instruction.

2026-08-19T07:52:51Z decision · item S8 retires the authored roster wholesale, which makes build-complete's missing-units term a tautology · reason Verified: roster_ids read from the GENERATED region is a subset of spec_ids by construction, because that region is rendered from specs that exist. So missing_units is empty always and --plan can never report a planned-but-unspecced unit. The authored pair was the ONLY carrier of that question. Options seen: accept the loss and drop the term; keep the authored pair for the missing-units question alone; invent a third declaration. Taking the middle one on the conservative reading - authorization, presence and terminality move to the generated region, and the authored pair is NARROWED to the one question only it can answer rather than retired. Spec S8 says retired and is now wrong; correcting it. Owner may prefer dropping the term outright.

2026-08-19T08:25:14Z decision · item gates-green is unreachable for this run: another node's run is live at LANDING and cannot be terminated by me · reason Leg check 7 reds on two non-terminal run-state files: mine and aPacedTurnstile's, which arrived with the merge from main at 6f598a1. Their run overrode build-complete, then could not land because the primary tree's main was ahead by three commits of a different mid-flight build, so it parked 'Who lands this, and when?' at phase LANDING. LANDING is NOT in PHASES_TERMINAL, so their record is live forever and check 7 counts it against every later run. Options seen: --override gates-green, which this repo's own aBranchedMandate commit refuses on the record as spending the one machine check between an unattended run and an unverified landing, for a red that is someone else's; --landed or --abort on their record, which is not mine to write and is the instinct their own backlog row warns against; or escalate. Escalating: the fix is outside this mandate's authority, which is exactly the gate-red-out-of-scope case.
