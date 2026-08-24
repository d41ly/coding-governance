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
