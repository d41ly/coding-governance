---
slug: aPrunedIndex
node: a
opened: 2026-11-25
streams: tooling
roster: TOOL
ids: TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4
spec-audit: 2026-11-25
status: OPEN
---

# aPrunedIndex — the tag check costs what its own worktree's rows cost

## The problem this build exists to solve

The bar leg `tags (the resolver's checks)` timed out at its 420 s ceiling in at least four landing bars on 2026-11-25 and
blocked two sessions' pushes. On a clean index of 270 MB the unmodified check took 85 s. The node's shared index is 12.6 GB:
it stores 35 versions of the citations extractor where the node's worktrees derive 6, and nothing retires the others. Each
read scans every version's rows, each name probe of a build walks them, and each build's sweep walks them again. The
measurements are in `build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md`.

## Expected improvements

- The check's reads, a build's name probes and a build's sweep cost what the reading worktree's own rows cost.
- The leg fits its ceiling on the index as it stands, with no ceiling moved and no verdict changed.
- `--gc` can collect dead versions while worktrees older than the tag registry are checked out.

## Detriments if this is not built

- Every landing on this node waits on a leg that fails at any bar width.
- The index grows by one more full set of rows at each edit of an extractor's import closure.

## Build-level rules

- **Classification (M2)**: four units, all MISSING at open. Unit 1 is Tier-2 (every reader's join), unit 2 Tier-1, unit 3
  Tier-2 (what a build deletes), unit 4 Tier-2 (what `--gc` collects).
- The two live index files are not collected, vacuumed, deleted or opened by this build's code until the owner says so in
  the building session: every measurement runs on a private copy.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py` are not edited; other sessions are landing them.
- No merge and no push without the owner's explicit ask in the building session.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aPrunedIndex-1` | the served rows are read through an index on the extractor version, so a read never walks another version's rows |
| 2 | `TOOL-aPrunedIndex-2` | a build finds an already-named path through a partial index of the `parsed` rows, and reads no parse ledger when it has no blob |
| 3 | `TOOL-aPrunedIndex-3` | a build's and an overlay's sweep deletes only what the trees and dirty rows it drops held |
| 4 | `TOOL-aPrunedIndex-4` | `--gc` skips a worktree whose HEAD holds no tag registry, naming it, and still refuses an unreadable one |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-25 · streams tooling
ids TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
