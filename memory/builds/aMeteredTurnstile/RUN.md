# aMeteredTurnstile - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 9a9914de69cafa17f6f724495fc8c1207fa3dbab
phase: REVIEWING
branch-sha: 3355837aa7e072de44a7e1d10c8e5e8020c22b15
branch-ref: refs/heads/branch/full-gate-bar-performance-828ae8
mode: slug
anchor-kind: run-branch
keepalive: 2daed484
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 56b945cbb0613b1352dd06221d4d39940db33419
anchor-ref: refs/heads/main
base: 3355837aa7e072de44a7e1d10c8e5e8020c22b15

## Parked

2026-08-19T23:32:21Z decision · item The spec TOOL-aMeteredTurnstile-1 was authored and BUILT in the same attended session, before this mandate existed, so M4's spec audit never preceded its code. · reason Options seen: (a) run the spec audit now, which would be a pre-code pass performed after the code and would record a false ordering; (b) rebuild the unit behind a real audit, which discards working, measured, merged work to satisfy a sequence; (c) park it and let the owner decide whether the unit needs a retroactive design pass. Refused (a) because a spec-audit record dated after the build is the kind of green-by-construction artifact this repo's charter exists to prevent, and refused (b) as disproportionate. The closing M8 diff review DID run and covers the code; what is missing is the pre-code design pass, and only the owner can judge whether that matters for a unit whose deliverable is a measurement.
