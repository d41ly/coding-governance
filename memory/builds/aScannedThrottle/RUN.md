# aScannedThrottle - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 2861ea94c55d3a603deb94e383b46dcff9093480
phase: VERIFYING
mode: slug
anchor-kind: default-branch
keepalive: 6ade2146
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 49aea26a704537a8299da825b72796bef5953262
anchor-ref: refs/heads/main
base: 49aea26a704537a8299da825b72796bef5953262

## Parked

2026-08-20T22:01:16Z decision · item Should TOOL-aScannedThrottle-1 flip to CLOSED on the strength of the first records-only row in memory/project/trace-waiver.txt, or stay OPEN and keep costing every run an --override build-complete? · reason Options seen, both measured. (1) FLIP: add a trace-waiver.txt row and set the spec CLOSED in ONE commit - drift_report.py restricts its population to TERMINAL specs and turns a leftover waiver row into a suspect of its own, so the two are safe only atomically. Cost: all six existing rows are the other admitted shape (product landed before the id-in-subject convention), so this is the FIRST records-only waiver in the repo. (2) STAY OPEN: build-complete fails on any unit that is neither CLOSED nor WONTDO, so every run carrying this build owes --override build-complete, which the driver itself calls authorizing itself past the one item that means the build is done. REFUSED because option 1 is a gate exemption of a new kind, and the fork rule reserves a change to a gate's waiver registry for the owner. rev-2 of the spec records the route, the atomicity trap and the evidence so the decision costs one command, not a re-derivation. Spec audit F5.

2026-08-20T22:31:30Z decision · item CORRECTION to the parked trace-waiver decision above: its premise about the registry's contents was wrong. The decision itself is unchanged. · reason The row above said all six rows in memory/project/trace-waiver.txt are one shape. They are THREE, and the registry's own header states five where the file holds six. Checked at HEAD: four aDrainedSluice rows and one aWireWarden row are pre-cutoff subjects; aWireWarden-1 is additionally a subject-SCOPE waiver, since it names its id in the body; and dSettledRoster-5 is a record-written-after-the-work waiver, landed 2026-08-20, AFTER TRACE_CUTOFF. The load-bearing conclusion survives untouched - none of the six is records-only, so a waiver for TOOL-aScannedThrottle-1 would still be the first of its kind, and that is why the decision is the owner's. Found by the closing diff review, M4. Spec rev-2 carries the corrected premise; this row exists because a parked entry is append-only and the owner reads it here.
