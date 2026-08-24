# dScaffoldedMirror - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 0431c44027fd3aeefe5a9fbee491516252d41a95
phase: BUILDING
branch-sha: 500a5db6b8e056c11bbe1c3cd82a16bc186ada5a
branch-ref: refs/heads/branch/lexicon-kit-overview-00de02
mode: slug
anchor-kind: run-branch
keepalive: 5ba175bf
anchor-url: https://github.com/d41ly/coding-governance
anchor-sha: 9ddcc5c944bdb92456ef031ee5f038842d016587
anchor-ref: refs/heads/main
base: 500a5db6b8e056c11bbe1c3cd82a16bc186ada5a

## Parked

2026-08-24T22:34:24Z decision · item drift-audit's non_terminal_specs_cited_by_product_source is 3 over pin 2 while this build is in flight · reason The two extra citations are TOOL-dScaffoldedMirror-8 and -10, both INPROGRESS, both cited by the code they specify. That is inherent to building: a unit's own source names its own unit id for provenance, per charter section 6, and the id is non-terminal until the unit closes. Options seen: (a) raise the pin, refused because a raisable ceiling is the defect this whole build exists to remove; (b) strip the ids from the comments, which trades provenance for a green signal and would have to be undone at close; (c) park, because BOTH units close inside this build and the count returns to the pin-2 baseline (aBatchedLintel-1, a known standing drain) before anything lands. Taking (c). If either unit ends the build non-terminal, this becomes a real finding rather than a transient one, and the close will say so.
