# dScaffoldedMirror - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 1704b1b44af9f805d0950ddbf69dc2160151cf92
phase: REVIEWING
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

2026-08-24T23:50:03Z review · item dScaffoldedMirror · reason verdict BLOCKED · blockers 1

2026-08-25T01:14:07Z decision · item the charter's read path is 51 B under its declared ceiling, so the next ratified decision record cannot be written · reason Measured 2026-08-25 at round 2: six member files, 133899 B against READ_PATH_CEILING=133950. A DECISIONS.md row costs ~295 B under the 300-char index cap, so recording ANY new ratified decision now reds check 16. The round-2 review found one that is owed: TOOL-dScaffoldedMirror-18 says gov takes the 459-row backfill and lands it, and it did not land — -9 is DEFERRED under the owner's own six-units ruling, so a session reading the decision index first concludes gov holds the backfill. Three options and none is mine to take unattended: (a) raise the ceiling, which is the second raise in one build to absorb that build's own growth and is the exact shape this build exists to remove, and the existing marker says so in as many words; (b) give back ~300 B from the four guides on the read path, which are binding protocols and not something to trim at speed with no owner turn; (c) leave -18 uncorrected, which defers a section-6 obligation for a byte budget. The correction itself is recorded in the build record and in this park, so nothing is lost if the owner picks (b) or (c) later.

2026-08-25T01:24:44Z review · item dScaffoldedMirror · reason verdict BLOCKED · blockers 0 · CONVERGED
