# dFramedEntrypoint - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 94b6195f32d1ee7c1c5e12ddca4bd05ca315f79d
phase: BUILDING
branch-sha: 470bb09ba977030f5c651c55e813bc6e5bd53b03
branch-ref: refs/heads/branch/build-readme-governance-e1c044
mode: slug
anchor-kind: run-branch
keepalive: 60f2b088
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 9ddcc5c944bdb92456ef031ee5f038842d016587
anchor-ref: refs/heads/main
base: 470bb09ba977030f5c651c55e813bc6e5bd53b03

## Parked

2026-08-24T20:05:52Z decision · item Should the authored roster:units marker pair become MANDATORY and gated, or should its reader, the --plan MISSING report and build-complete term 3 all be deleted together? · reason Options seen: (a) make the pair mandatory and gate its presence, which turns build-complete term 3 into a real check and closes TOOL-aPacedTurnstile-14; (b) delete roster_ids, missing_units and term 3, accepting the loss of the only structure in the kit that can name a planned unit with no spec. Refused because the pair is live on 10 of 61 builds and has never once reported a missing unit, term 3 is overridable and passes vacuously on 51 of 61, and pointing roster_ids at the generated region was already tried and reverted inside TOOL-aBoundedVerdict-11 as a tautology. Both options are defensible and the choice changes what a Definition-of-Done item MEANS, which is outside this build's stated goal of constraining the README's authored half.

2026-08-24T20:05:57Z review · item dFramedEntrypoint-specs · reason verdict BLOCKED · blockers 1

2026-08-24T20:05:59Z review · item dFramedEntrypoint-specs · reason verdict BLOCKED · blockers 0 · CONVERGED

2026-08-24T20:28:25Z decision · item memory/guides/BUILD-METHOD.md is 2 lines over its own declared budget at this build's BASE, and no gate enforces the pair. · reason Measured 313 lines and 23868 B at 470bb09b against M1's stated cap of 310 lines and 24 KB. The byte half is fine; the line half was already breached before this build touched the file, and M1's own text says exceeding it silently was the one option not taken - so it was exceeded silently anyway, by an earlier build, because nothing checks it. This unit's edits took it 313 to 312, a net reduction of one line, so the run did not cause it and has not worsened it. Options seen: (a) trim two lines of method prose belonging to other builds, (b) raise the cap, (c) add a gate. All three are changes to a governance carrier, which M3's veto 2 puts outside the delegated resolver authority, and the file's own M1 names its budget as an owner call twice over. Refused for that reason rather than for cost.

2026-08-24T20:38:25Z decision · item After the roster sorts by build order, the unattended driver's --plan and --status disagree about which unit is next. · reason Observed live at this unit's build: --status reads the generated units region, which TOOL-dFramedEntrypoint-4 now renders in order-then-id sequence, and names unit 4; --plan sorts tracked specs by id and names unit 2. Both were consistent before, because the region was rendered in path order and path order matched id order closely enough. Options seen: (a) sort --plan by the same key, which means the driver reads the order verb and couples a second kit to this build's grammar; (b) have --plan read the rendered region rather than re-deriving from specs, which is the shape check_authorization already uses; (c) leave them divergent and document that --status is the build order and --plan is the id order. Refused because the fix belongs to tools/unattended/, which is a different kit with its own contract, and spec 4's non-goals do not reach it. Not urgent: neither verb is wrong about STATUS, only about which unit it volunteers first.

2026-08-24T20:57:23Z decision · item The lexicon naming leg is RED at this build's BASE on a clean tree, and its guard hid that. · reason Measured: git stash to a clean tree, then python tools/lexicon/lexicon.py exits 1 with 435 P1 verb violations, the first three in tools/codebase-map/map_lib.py. Nothing in this build caused it and this build cannot see when it started, because the leg is GUARDED on tools/, skills/session-kickoff/, .githooks/ and .claude/ - so it runs only when one of those moves, and a red can sit in it for the length of any build that does not touch them. That is the guarded-legs-hide-latent-failures class this repo already records as a gotcha. Options seen: (a) fix 435 violations, which is a build of its own and touches another kit's source; (b) pin the offenders in the lexicon's own waiver registry, which is a judgement about another kit's naming that this build has no standing to make; (c) report it and leave it. Refused because it is outside this build's stated goal and belongs to whoever owns the naming table. Worth knowing separately: this is the second guarded leg this build found holding something nobody had seen.

2026-08-24T21:12:39Z decision · item tools/dead-path-waivers.txt is keyed on <path>:<line>, so any insertion above a waived hit unpins it. · reason Hit live in this build: unit 3 added four comment lines to tools/memory-tree/check-memory-hygiene.sh, which moved a waived STATUS.md mention from line 550 to 554, and the leg redded with a stale-row message that names the new location but not the cause. Re-keyed by hand and green again. This repo has ALREADY recorded that this keying is wrong, in another file: tools/memory-tree/adopt-memory-tree.sh says of method-carriers.txt, 'Keyed on PATH alone, never <path>:<line> - that keying is what unpinned install-prefix-waivers.txt.' So the lesson exists and dead-path-waivers.txt did not receive it. Options seen: (a) re-key it on path alone, which loses the ability to waive one mention in a file with several; (b) key it on the surrounding line's TEXT, which survives insertion but not rewording; (c) leave it and pay a re-key per insertion. Refused because it is another kit's registry and this build has no standing to change its grammar, and because (a) and (b) trade different failures rather than removing one.
