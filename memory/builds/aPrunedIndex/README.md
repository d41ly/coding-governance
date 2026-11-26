---
slug: aPrunedIndex
node: a
opened: 2026-11-25
streams: tooling
roster: TOOL
ids: TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-20 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 TOOL-aPrunedIndex-24 TOOL-aPrunedIndex-25 TOOL-aPrunedIndex-26
spec-audit: 2026-11-25
---

# aPrunedIndex — the tag check costs what its own worktree's rows cost

## The problem this build exists to solve

The bar leg `tags (the resolver's checks)` timed out at its 420 s ceiling in at least four landing bars on 2026-11-25 and (PINNED, 2026-11-25)
blocked two sessions' pushes. On a clean index of 270 MB the unmodified check took 85 s. The node's shared index is 12.6 GB: (PINNED, 2026-11-25)
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
  the building session (said 2026-11-25, for after the closing review): every measurement runs on a private copy.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py` are not edited; other sessions are landing them.
- No merge and no push without the owner's explicit ask in the building session.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aPrunedIndex-1` | the served rows are read through an index on the extractor version, so a read never walks another version's rows |
| 2 | `TOOL-aPrunedIndex-2` | a build finds an already-named path through a partial index of the `parsed` rows, and reads no parse ledger when it has no blob |
| 3 | `TOOL-aPrunedIndex-3` | a build's sweep deletes only what the trees and the gone worktrees' dirty rows it drops held; a replaced edit's rows wait for `--gc` |
| 4 | `TOOL-aPrunedIndex-4` | `--gc` skips a worktree whose HEAD holds no tag registry, naming it, and still refuses an unreadable one |
| 5 | `TOOL-aPrunedIndex-10` | the closing review's four lows, batched (M4): the README's sweep cost stated as its ceiling, the lambda-bound plant helper a named `def`, and two `gc-predates` steps whose HEAD git cannot read |
| 6 | `TOOL-aPrunedIndex-17` | the five tag plants this build added hold the git answers that cannot change while they run, so they spawn fewer git processes; whether `tags bundle selftest` then fits its ceiling under load is AC8's reading at the close, and the remainder is handed to a pool unit (closing review round 2, id 1) |
| 7 | `TOOL-aPrunedIndex-20` | `tags bundle selftest` runs its plants on a bounded pool of workers with output in row order, so the leg's wall is near its slowest plant (unit 17's hand-off) |
| 8 | `TOOL-aPrunedIndex-24` | the held-answer rules get arms `tags bundle selftest` runs: the key table and the never-store-a-failure rule, and `HELD_FLAGS` loses its dead `"--"` (closing review round 3, items 1, 4, 5) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 8 unit(s) · node a · opened 2026-11-25 · streams tooling
ids TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14
ids TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-20 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 TOOL-aPrunedIndex-24 TOOL-aPrunedIndex-25 TOOL-aPrunedIndex-26

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPrunedIndex-1 — a read of the served rows starts from the reading worktree's own extractor versions](spec/2026-11-25-spec-TOOL-aPrunedIndex-1.md) | 1 | 2 | CLOSED | rev-4 | 2026-11-26 |
| [TOOL-aPrunedIndex-2 — a build finds an already-named path through a partial index, and reads no parse ledger without a blob](spec/2026-11-25-spec-TOOL-aPrunedIndex-2.md) | 2 | 1 | CLOSED | rev-4 | 2026-11-26 |
| [TOOL-aPrunedIndex-3 — a build's sweep touches only the rows that the trees and gone worktrees' edits it lets go of held](spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md) | 3 | 2 | CLOSED | rev-4 | 2026-11-26 |
| [TOOL-aPrunedIndex-4 — `--gc` skips a worktree that predates the tag registry, and still refuses one it cannot read](spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md) | 4 | 2 | CLOSED | rev-4 | 2026-11-26 |
| [TOOL-aPrunedIndex-10 — the closing review's four lows: the sweep's cost stated as its ceiling, a named plant helper, and two steps whose HEAD git cannot read](spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md) | 5 | 1 | CLOSED | rev-2 | 2026-11-26 |
| [TOOL-aPrunedIndex-17 — the five tag plants hold the git answers that cannot change while they run](spec/2026-11-26-spec-TOOL-aPrunedIndex-17.md) | 6 | 2 | CLOSED | rev-4 | 2026-11-26 |
| [TOOL-aPrunedIndex-20 — the tag plants of `tags bundle selftest` run on a bounded pool, graded in row order](spec/2026-11-26-spec-TOOL-aPrunedIndex-20.md) | 7 | 1 | CLOSED | rev-2 | 2026-11-26 |
| [TOOL-aPrunedIndex-24 — the held-answer rules get a `held-key` plant that `tags bundle selftest` runs](spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md) | 8 | 1 | CLOSED | rev-2 | 2026-11-26 |
<!-- /gen:build-units -->

Records: 32 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 8 of 8 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPrunedIndex-1` | no |
| 2 | `TOOL-aPrunedIndex-2` | no |
| 3 | `TOOL-aPrunedIndex-3` | no |
| 4 | `TOOL-aPrunedIndex-4` | no |
| 5 | `TOOL-aPrunedIndex-10` | no |
| 6 | `TOOL-aPrunedIndex-17` | no |
| 7 | `TOOL-aPrunedIndex-20` | no |
| 8 | `TOOL-aPrunedIndex-24` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
