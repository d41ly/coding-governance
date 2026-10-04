# TOOL-aMendedFleet-45 — reviewers' by-design list comes from one source, the invariant records

**Status:** WONTDO · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 45 · retired to aGraftedHelix unit 3, whose invariants registry is the reviewers' by-design source

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` reads `byDesign` from its caller and falls back to `none
supplied`, and no caller in the tree supplies one, so finders re-report what is intended and
skeptics refute without being shown what is. The review's point was to choose ONE by-design source,
the invariant records the live `aGraftedHelix` build introduces, and to drop the second pipeline the
first wave proposed, a `map_diff --by-design` mode that would restate dossier prose. That mechanism
is owned by aGraftedHelix's unit 3, on `origin/branch/helixir-review-gov-adoption-ce32e1`, SPECCED
at rev-2 and ratified 2026-10-04. Per the build brief's rule 7, this unit is specced so the hand-off
is visible, and the run retires it to that unit instead of building a second copy.

## 2. Scope (IN)

- **S1** — the run disposes of this unit: its status becomes `WONTDO` with a reason pointer naming
  aGraftedHelix's unit 3 by paraphrase, since that id is not defined on main. Observed by AC1.

## 3. Non-goals (OUT)

- Any change to `tools/workflows/` or `tools/memory-tree/gotchas.py`. aGraftedHelix's unit 3 adds an
  `invariant` kind to the gotcha catalogue, prints the invariants a diff touches as a by-design
  block after the bug-class checklist, and makes the harness's `byDesign` take that block, keeping
  a caller's own list under its own label.
- A `map_diff --by-design` mode. It was never built, `git grep -n "by-design" -- tools/codebase-map`
  finds nothing at base, and the review superseded it with the one-source rule; building it here
  would create the second pipeline the point exists to prevent.
- Recording on aGraftedHelix that its invariants are the one by-design source. The review marks
  that an owner act, and this unit does not write into another build's records.

### Edges

- **hands-off** external — aGraftedHelix's unit 3 builds the by-design source; this unit builds
  nothing.

## 6. Acceptance criteria

- **AC1** — When `grep -n "^\*\*Status:\*\*" memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-45.md`
  runs after the run disposes of this unit, it reads `WONTDO` with a tail naming aGraftedHelix's
  unit 3 as the successor.
  Red when: the header still reads SPECCED, or reads WONTDO with no successor in its tail.

## 8. Open questions

- **F1 — Build a by-design source here, or retire to the live build that owns it?**
  Options: build `map_diff --by-design` as the first wave proposed; build the invariant feed here;
  or retire to aGraftedHelix's unit 3. The first is the second pipeline the review rejected; the
  second makes two writers of `tier2-review.template.js` and `gotchas.py` on two live branches,
  which the brief's rule 7 exists to prevent.
  RESOLVED (agent, 2026-10-04, delegated): retire to that unit, S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; that unit's spec read from its branch at `53adda2c5`.
- rev-2 · 2026-10-04 · §1 status WONTDO: retired to aGraftedHelix unit 3 per the spec brief's rule 7; nothing built here.

## 10. Reuse audit

The seam is aGraftedHelix's unit 3, read with `git show` on its branch at `53adda2c5`: an
`invariant` kind in `tools/memory-tree/gotchas.py`, a by-design block printed by `--for-diff`, and a
`byDesign` built from that block in `tools/workflows/tier2-review.template.js`. At base the harness
spells `const byDesign = a.byDesign || 'none supplied'` and no workflow or script passes one, so the
seam is in flight rather than shipped; `git grep` finds `byDesign` assigned only in comments of the
two drift-audit workflows, which are also unfed. `python tools/codebase-map/reuse_lookup.py "feed
the review harness a by-design list of intended behaviour"` ranked `derive_review_exit` and
`derive_review_verdict` in `tools/runlog/model.py`, the `REVIEW-PROTOCOL.md` guide key and
shared-seams prose neighbours, none of which produces a by-design list, so no shipped seam fits; it
printed `unscanned layers: .sh`. Recall returned `TOOL-aSightedSkeptic-1`, which made the skeptic
read the BY DESIGN list the harness is given and supplied no source for it, and the report's row
naming aGraftedHelix's unit 3 as the in-flight source.

Recall terms used: `python tools/memory-recall/query.py "where does the review harness get its
by-design list, and which source owns it" --terms "byDesign by-design tier2-review invariant
gotchas map_diff dossier reviewers skeptic refute"`
