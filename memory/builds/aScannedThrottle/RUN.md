# aScannedThrottle - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 51486db048b9d2fa04638a6a7706c1f0581c6cbb
phase: FOLDING
mode: slug
anchor-kind: default-branch
keepalive: 6ade2146
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 49aea26a704537a8299da825b72796bef5953262
anchor-ref: refs/heads/main
base: 49aea26a704537a8299da825b72796bef5953262

## Parked

2026-08-20T22:01:16Z decision · item Should TOOL-aScannedThrottle-1 flip to CLOSED on the strength of the first records-only row in memory/project/trace-waiver.txt, or stay OPEN and keep costing every run an --override build-complete? · reason Options seen, both measured. (1) FLIP: add a trace-waiver.txt row and set the spec CLOSED in ONE commit - drift_report.py restricts its population to TERMINAL specs and turns a leftover waiver row into a suspect of its own, so the two are safe only atomically. Cost: all six existing rows are the other admitted shape (product landed before the id-in-subject convention), so this is the FIRST records-only waiver in the repo. (2) STAY OPEN: build-complete fails on any unit that is neither CLOSED nor WONTDO, so every run carrying this build owes --override build-complete, which the driver itself calls authorizing itself past the one item that means the build is done. REFUSED because option 1 is a gate exemption of a new kind, and the fork rule reserves a change to a gate's waiver registry for the owner. rev-2 of the spec records the route, the atomicity trap and the evidence so the decision costs one command, not a re-derivation. Spec audit F5.
