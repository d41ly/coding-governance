# aClosedDocket - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes, 0 surfaced
keepalive-reaped: yes
witness: 217d1ddcb8562a77d18e683ff8c0cafab78d4213
phase: BUILDING
branch-sha: 733552e11d36e93836767b6478fec3607a99aca4
branch-ref: refs/heads/branch/aclosed-docket
mode: prompt
anchor-kind: run-branch
keepalive: 75d57778
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 7dae5ce9dccef35c30df1fb5f4623133db4f1a46
anchor-ref: refs/heads/main
base: 733552e11d36e93836767b6478fec3607a99aca4

## Parked

2026-08-31T12:19:59Z review · item spec-set · reason verdict BLOCKED · blockers 3

2026-08-31T12:53:51Z review · item spec-set · reason verdict BLOCKED · blockers 4 · NON-CONVERGENT

2026-08-31T12:54:10Z rescope · item add TOOL-aClosedDocket-4 · reason Round-2 blocker B2, promoted at the NON-CONVERGENT exit. M2 states verbatim that a separate document, gate, adopter or generated artifact is a separate unit with its own id and spec; rev-2 of unit 1 had put the M4 sentence, check-unattended.sh clause 3 and a new driver-written fact under one id. The gate half and the driver fact split out here, leaving unit 1 as the document change alone. This is promotion in its literal sense: the blocker needs a MECHANISM the build did not have, which is a second unit.

2026-08-31T13:00:12Z dispatch · item 217d1ddc TOOL-aClosedDocket-3 · reason tools/unattended/unattended.test.sh

2026-08-31T13:21:54Z review · item TOOL-aClosedDocket-4 · reason verdict BLOCKED · blockers 1
