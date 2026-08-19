# aPromptedMandate - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
mode: slug
witness: 5f9efdb05c3386a32e0ed436d762fb94bb58b872
phase: LANDED
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
keepalive-reaped: yes
parked-surfaced: yes

2026-08-19T01:40:14Z decision · item the primary tree carries 46 unpushed commits from TWO other builds, one of which deliberately refused to land — may this run's landing push carry them? · reason push-main refuses everywhere but the primary tree. That tree is on main and clean, so the lander WOULD succeed - while carrying 46 commits this run did not author: aDeclaredBound (20) and aPacedTurnstile (22), plus 3 merges. aPacedTurnstile's own final commit says in terms: 'the run cannot land, and the reason is outside its authority' - it stopped at LANDING for this same reason and filed TOOL-aPacedTurnstile-15 (gates-green runs the bar on the RUN's tip, never on what the landing push would actually carry). Pushing main would therefore land a build that DECIDED it must not land, under this build's mandate: outward-facing, irreversible, every gate green, and no verb in the kit saying a word. Options seen: (a) push main and carry all 46 - refused, it spends another build's landing decision; (b) raw-push only this build's commits - refused, bypassing the lander discards the whole bar the authorization leaned on, and the lander is mandated for that reason; (c) stop at LANDING, which is the TRUE state - built, reviewed, DoD-evaluated with no overrides, branch pushed and durable at origin/branch/unattended-sessions-kit-extend-2e4038 - and hand the decision to the owner. REFUSED to pick between (a) and (b): the owner authorized landing THIS build, and neither of us knew the primary tree held two other builds' work when that was said.

2026-08-19T11:35:00Z abort · item aPromptedMandate · reason This run merged into local main and stopped at LANDING without marking itself; its merge IS reachable from main, but nothing was ever pushed, so the run landed nothing. LANDED is not available and would not be true — the driver's own check 15 refuses a LANDED claim whose witness is not an ancestor of the tip the remote advertises, and it refused this exact edit when it was attempted. ABORTED is the same terminal state this fleet's aFusedCharter run took for the same reason on the same day. Set by the aFusedCharter session on the owner's explicit instruction, as part of landing main; that session did NOT perform this run and attests nothing about its Definition of Done. The work itself is unaffected and reaches the remote with this push.

2026-08-19T19:04:01Z decision · item aPromptedMandate · reason phase set from ABORTED to LANDED BY HAND, on the owner's explicit instruction given after they were shown that the kit refuses this transition. Both `--landed` and `--phase` refused with check 26 (a finished record is not something to move, re-open or re-pin), and memory/guides/UNATTENDED-PROTOCOL.md states that a run already terminal cannot be moved at all. This edit therefore bypasses check 26 deliberately; it is the owner's call and not the kit's, and it is recorded here rather than left to be inferred from a diff. Set by the aFusedCharter session, which did NOT perform this run and attests NOTHING about its Definition of Done. The LANDED claim rests on the owner's judgment plus a single verified fact: this record's witness 5f9efdb0 is an ancestor of the remote tip 033b454, so the work it names is on the branch the remote calls its default. The abort note above is superseded on that point only; its statement that this run itself pushed nothing remains true.
