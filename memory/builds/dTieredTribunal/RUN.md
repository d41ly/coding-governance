# dTieredTribunal - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: da9e4cd28072501cd4fe87a81db36c01b9a80f9e
phase: SPECCING
mode: slug
anchor-kind: default-branch
keepalive: 91052d0a
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: da9e4cd28072501cd4fe87a81db36c01b9a80f9e
anchor-ref: refs/heads/main
base: da9e4cd28072501cd4fe87a81db36c01b9a80f9e

## Parked

2026-08-25T23:03:44Z decision · item Which proposal set becomes this build's units — and specifically, does P1 (a subject descriptor on tier2-review.js) get built, which requires editing BUILD-METHOD.md M4? · reason The research record ranks P1/P2/P12 RECOMMENDED and the build README says the owner narrows before anything is specced; the invocation said 'spec the build and execute' without naming a set. P1 is the build's own goal, but landing it makes M4's 'Not the harness' rule FALSE, and this build's README rule 3 puts BUILD-METHOD M4/M8 and REVIEW-PROTOCOL.md in scope as PROPOSALS, not as edits. So P1 without a rule edit ships a capability M4 still forbids (dead by construction), and P1 with one breaches the build's own stated rule. Options seen: (a) build P1 + P6's rule edits, breaching README rule 3; (b) build P1 alone, leaving M4 stating something false; (c) build P9 (the record-shape hygiene gate), which the research names as the substitute 'worth doing alone if P1 is declined' and which needs no rule edit; (d) park P1 and P9 together as one owner turn and build only what needs no governance-carrier edit. Refused (a) and (b) because both breach a stated constraint, and M3's veto 2 makes a governance-carrier change an owner turn that the mandate's delegation does not reach. Refused (c) alone because substituting P9 for a parked P1 pre-empts the owner's call on the stronger mechanism. Proceeding on (d).
