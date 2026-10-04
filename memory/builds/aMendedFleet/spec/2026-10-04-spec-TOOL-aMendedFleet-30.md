# TOOL-aMendedFleet-30 — superseded records are labelled in recall output

**Status:** WONTDO · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 30 · retired to aGraftedHelix unit 4, which builds supersession labels in recall output

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-recall/query.py` prints a record a later record superseded exactly as it prints a
current one. The review's point was to label supersession and never demote a partial one. That
mechanism is already owned by the live `aGraftedHelix` build, as its unit 4, on
`origin/branch/helixir-review-gov-adoption-ce32e1`, SPECCED at rev-2 and ratified 2026-10-04. Per the
build brief's rule 7, this unit is specced so the hand-off is visible, and the run retires it to that
unit instead of building a second copy.

## 2. Scope (IN)

- **S1** — the run disposes of this unit: its status becomes `WONTDO` with a reason pointer naming
  aGraftedHelix's unit 4 by paraphrase, since that id is not defined on main. Observed by AC1.

## 3. Non-goals (OUT)

- Any change to `tools/memory-recall/`. aGraftedHelix's unit 4 derives a superseded-by map at index
  time, tags a hit `[superseded by …]` or `[partly superseded by …]`, and moves only a WHOLE-superseded
  hit below a listed successor, which is the review's "label, never demote a partial" rule.
- The two refinements the review attached, which stay with that unit: key each edge by path and line,
  because the review counted 434 ids anchored more than once at `ac65de998`, and backfill the 18
  edges it mined by hand. That unit's map is keyed by id, so the run's wrap-up names both for its
  owner rather than this unit building either.

### Edges

- **hands-off** external — aGraftedHelix's unit 4 builds the labels; this unit builds nothing.

## 6. Acceptance criteria

- **AC1** — When `grep -n "^\*\*Status:\*\*" memory/builds/aMendedFleet/spec/2026-10-04-spec-TOOL-aMendedFleet-30.md`
  runs after the run disposes of this unit, it reads `WONTDO` with a tail naming aGraftedHelix's
  unit 4 as the successor.
  Red when: the header still reads SPECCED, or reads WONTDO with no successor in its tail.

## 8. Open questions

- **F1 — Build supersession labels here, or retire to the live build that owns them?**
  Options: build them in this unit; or retire to aGraftedHelix's unit 4. Building here makes two
  writers of `run_fusion` and `CACHE_VERSION` on two live branches, which the brief's rule 7 exists to
  prevent.
  RESOLVED (agent, 2026-10-04, delegated): retire to that unit, S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; that unit's spec read from its branch at `14e5f2655`.
- rev-2 · 2026-10-04 · §1 status WONTDO: retired to aGraftedHelix unit 4 per the spec brief's rule 7; nothing built here.

## 10. Reuse audit

The seam is aGraftedHelix's unit 4, read with `git show` on its branch: `extract_supersessions` and
`derive_supersession_map` in `tools/memory-recall/extract.py`, and a reorder inside `run_fusion` in
`tools/memory-recall/query.py`. `git grep` over `tools/` at base finds none of those names, so the
seam is in flight rather than shipped. `python tools/codebase-map/reuse_lookup.py "label a
superseded record with its successor in recall output"` returned only `record`-stemmed neighbours in
`tools/runlog/record.py` and `tools/memory-tree/gotchas.py`, none of which labels a hit, so no
shipped seam fits. Recall returned no record of a shipped labeller; its top hits were the floor ask
`TOOL-aWalkedCorpus-2` and a status-flip supersession in node d's dFoldedVerdict build.

Recall terms used: `python tools/memory-recall/query.py "how does recall label a superseded record
and its successor" --terms "supersede superseded successor label recall query run_fusion partial
demote rank retire"`
