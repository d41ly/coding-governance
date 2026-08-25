# dScaffoldedMirror - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
parked-surfaced: yes
keepalive-reaped: yes
witness: ea49714abdf92a14f856e392cb208ab34a2b331b
phase: LANDED
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

2026-08-25T01:59:01Z override · item build-complete · reason Six units are DEFERRED by the OWNER's own ruling, not by this run's judgement. TOOL-dScaffoldedMirror-16..19 recorded four rulings on 2026-08-24, and the fifth was the scope: six units now, with -9 as a seventh gated on evidence, against the agent's proposed thirteen. The owner's instruction was to commit all fourteen specs and apply the cuts as status flips, which is why -4, -9, -11, -12, -13 and -15 sit DEFERRED with rev-1 specs rather than deleted -- each is a real unit somebody can pick up, and its spec is the handover. -9's own gate has since been read twice: the fresh-file marginal offense rate is 4.2%, under the 5% bar its kill rule names, so the evidence that would unpark it is currently pointing the other way. The build's stated goal -- make the naming gate useful rather than a mirror of the code it grades -- is met and demonstrated: the owner's six deliberately-bad names now all fail where all six passed green, and VERB_OFFENDER_PIN fell 463 -> 384 across the build and never rose once.

2026-08-25T02:02:17Z decision · item the landing is a Tier-2 concurrent integration nobody scoped: main gained 20 commits from dFramedEntrypoint during this run · reason Observed 2026-08-25 at the landing, after --close reached LANDING and the bar was 85/85 green on this branch's own tip. origin/main moved 9ddcc5c9 -> 60ba1d60 while this run was building. merge-base is still 9ddcc5c9; 42 commits mine, 20 theirs, and git merge-tree reports 126 conflicted paths. The good news is that tools/lexicon/ is UNTOUCHED on main, so the kit work is orthogonal and nothing about this build's subject is contested. The collision is entirely in the memory tree: dFramedEntrypoint changed the build README slot contract, which rewrote every build README in the tree, and both sides moved .memory-tree.conf, DECISIONS.md, HYGIENE.md, TEMPLATE-SPEC.md, backlog/TOOL.md and .gitattributes. One collision is already known to be wrong rather than merely conflicting: main carries KIT_MEMORY_TREE_VERSION 2.40 and this branch bumped 2.30 -> 2.31 to clear its own verdict-epoch leg, so that bump must be discarded in favour of main's and the epoch check re-run against the merged tree. Charter section 8 makes a cross-stream merge Tier-2 on its own account, and section B records the 2026-08-21 precedent where exactly this shape put four merge-bar legs red on a merged tree with none red on either parent. The mandate authorized landing THIS build; it did not anticipate integrating another node's, and a run cannot review its own merge into somebody else's work with no owner turn. Branch pushed at 15263bd8 so nothing is stranded.
