# dFramedEntrypoint - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 56c58eac7f452eedc9c178653096775df101c5f7
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
