---
slug: cListedCensus
node: c
opened: 2026-10-12
streams: tooling
roster: TOOL
ids: TOOL-cListedCensus-1
---

# cListedCensus — ps-hygiene grades the tracked `.ps1` files, not a walk of the disk

## The problem this build exists to solve

`tools/gate-lint/ps-hygiene.py` builds its population with `root.rglob("*.ps1")`. NicoCares keeps its
linked worktrees inside the primary tree at `.claude/worktrees/<name>/`, untracked, so the scan
graded every sibling checkout. On 2026-10-11 nc's lander went red on 6 findings, all of them in
untracked worktree copies. The red-leg attribution re-ran the leg in a fresh worktree, saw green, and
called the red OWN. nc fixed it locally as `PKG-bIndexedHarrow-1` (nc `bcc6f8a4`). The fix before
that, `PKG-bStitchedFerry-3`, was erased by a govkit pull because it never reached gov.

## Expected improvements

- An adopter's scan grades the files its commit holds, wherever it keeps its worktrees.
- A dead `git ls-files` and an empty population each refuse with exit 2 instead of passing.
- nc's carve-out retires on its next pull rather than being erased by it a third time.

## Detriments if this is not built

- nc's next govkit pull erases its fix again, and its lander reds on other sessions' checkouts.
- Any adopter with nested worktrees gets a red that the attribution misnames as its own.

## Build-level rules

- One unit, Tier 2, at the owner's call at kickoff; no spec audit is declared.
- The reference is nc `bcc6f8a4:scripts/gate-lint/ps-hygiene.py`, taken without its carve-out comment.
- No leg is wired: gov tracks no `.ps1`, so a leg here would refuse on every run.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-cListedCensus-1` | INPROGRESS | the scan's population is `git ls-files -z -- '*.ps1'`; a dead probe and an empty population refuse with exit 2 |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node c · opened 2026-10-12 · streams tooling
ids TOOL-cListedCensus-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cListedCensus-1 — ps-hygiene grades the tracked `.ps1` files, and refuses a population it could not derive](spec/2026-10-12-spec-TOOL-cListedCensus-1.md) | — | 2 | INPROGRESS | rev-1 | 2026-10-12 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-cListedCensus-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
