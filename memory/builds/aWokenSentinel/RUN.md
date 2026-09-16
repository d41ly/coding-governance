# aWokenSentinel - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b
phase: RUNNING
branch-sha: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b
branch-ref: refs/heads/branch/unattended-kit-keepalive-a29498
mode: prompt
run-branch: refs/heads/branch/unattended-kit-keepalive-a29498
anchor-kind: run-branch
keepalive: f1209d79
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 4cf0944dbdce94714870f26760936bc5edabc64e
anchor-ref: refs/heads/main
base: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b

## Parked

2026-09-16T12:00:05Z rescope · item add TOOL-aWokenSentinel-7 · reason Measured 2026-09-16: the Stop hook's stdin carries session_crons, the cron store no script can reach. keepalive-reaped stops being an attestation (TOOL-aPromptedMandate-11, OPEN since 08-18) and becomes a check against the last stop the hook recorded. Discovered by unit 3's probe; a second mechanism, so its own unit, ordered last.
