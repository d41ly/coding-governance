# aPromptedMandate - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
mode: slug
witness: da574464caf516a2bf16638ae91f080b8f3759d5
phase: SPECCING
branch-sha: b9ebebaae6f776788046980199703c58575d8805
branch-ref: refs/heads/branch/unattended-sessions-kit-extend-2e4038
anchor-kind: run-branch
keepalive: 4add8e66
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 098bebd9876c8f2f61a528b5cc9ac0a6b5d7719a
anchor-ref: refs/heads/main
base: b9ebebaae6f776788046980199703c58575d8805

## Parked

2026-08-18T19:21:25Z decision · item build-complete cannot be met by any build that follows the method: should unit_rows be narrowed to the units table, or is an override the intended escape? · reason unit_rows selects '^| [' across the WHOLE gen:build-index region, but gen_build_index renders TWO tables there - the units and the records. Record rows carry no '| CLOSED |', so nonterminal_units keeps them and the item is unsatisfiable. M4 mandates review records and M8 mandates a closing review, so every conforming build hits it. Measured on builds that already LANDED: aBranchedMandate shows 7 such rows, aStandingWrit 2. Options seen: (a) narrow the selector to the units table - small and correct, but unspecced driver work on DoD evaluation discovered at close; (b) --override build-complete with a reason - the documented escape, but an override absorbing a broken check is what the driver's own comment warns against; (c) leave it and let the owner decide. REFUSED to pick: this is a defect in the authorization/DoD machinery itself, found after the six specced units were built and reviewed, and fixing it silently would be the run editing the rules it is judged by.

2026-08-18T19:34:08Z decision · item the keepalive was reaped while the run is still non-terminal · reason The run is blocked on an owner decision (the build-complete park), not on work. A session-scoped job waking the agent every ten minutes to re-report the same block makes no progress and costs a turn each time; protocol section 5 makes the keepalive an obligation for an ACTIVE run, and this one is waiting on a human. Reaped deliberately, recorded here so the wrap-up does not read it as an orphan. Rearming is one call if the owner resumes the run.

2026-08-18T19:40:53Z decision · item CORRECTION: two keepalives this run recorded as dead were still live, and keepalive-reaped was nearly attested on a false belief · reason This run created three keepalives across two process deaths - e9bd601e, a12754dc, 4add8e66 - and twice asserted in the record that the earlier two died with their processes because the scheduling store is session-scoped. That was FALSE: CronList showed both still registered and firing after the second death. Only 4add8e66 had been reaped, so two orphans were left running while the record said the keepalive was reaped. All three are now cancelled and CronList reports none. What this shows about the kit, not just this run: the driver RECORDS a keepalive id and can never verify it, so keepalive-reaped is an attestation the agent can get wrong in perfect good faith - here by reasoning about process lifetime instead of asking the store. The agent-attested items need a LIST verb to check against, or they are only as true as the agent's model of a subsystem it cannot see.
