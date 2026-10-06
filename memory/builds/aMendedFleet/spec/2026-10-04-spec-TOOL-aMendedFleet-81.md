# TOOL-aMendedFleet-81 — the month shards carry only what never changes after their month

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 81

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

The month shards under `memory/ledger/` claim to be frozen once their month passes, and they are not:
a build's status and id count are re-rendered into an old shard whenever they move. This unit renders
each shard from the three inputs a build cannot change after its month, so the frozen claim becomes
true. Split from `TOOL-aMendedFleet-22` at that spec's F1, under this build's one-mechanism rule.

## 2. Scope (IN)

- **S1** — `render_shards` in `tools/memory-tree/gen_build_index.py` renders each month shard's
  table as Build, Node and Opened, the three inputs a build cannot change after its month, and the
  shard's "Frozen once the month passes" sentence stays as written because it becomes true. The
  Status, Streams and Ids (n) columns are no longer rendered there; `memory/LIVE.md` keeps all of
  them. Observed by AC1 and AC2.
  **Readers:** by name: `tools/memory-tree/gen_build_index.py` alone spells the shard's header row,
  in `render_shards` and in its own self-test arms.
  by value: `tools/workflows/drift-audit-state.js` points its work-state lens at the shards and
  `memory/LIVE.md` for which builds are non-terminal, and `memory/LIVE.md` still lists every build
  holding a non-terminal unit with its status; `tools/memory-tree/check-memory-hygiene.sh` measures
  each shard against the index-file caps, and every row gets shorter.

## 3. Non-goals (OUT)

- The merge attribute on the shards, which `TOOL-aMendedFleet-22` adds.
- `memory/LIVE.md`'s columns, which units 12 and 13 change.
- The `HYGIENE.md` line saying a month shard freezes when its month passes. S1 makes it true, so the
  carrier needs no edit.

## 4. Design

### Evidence

- The month shards change after their month. `git log -p` over `memory/ledger/` shows the Status
  cell flipped a month late in each closed month: `aWireWarden` in the July shard at `60e2e8f99`,
  `aClosedDocket` in the August shard at `4289f1b40`, and `aRepatriatedFork` twice in the September
  shard on 2026-10-02. At `38524b752` that row's id count also moved from 58 to 60. Read by the
  writer of `TOOL-aMendedFleet-22` at base `7af5f564`.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `memory/ledger/`

### Alternatives rejected

- **Dropping only the Status column, as the report proposed.** The id count moved a month late too,
  so the shard would still not be frozen.
- **Keeping Streams with a reworded claim.** A build's `streams:` front matter can gain a discipline
  mid-build, so the claim would carry an exception and the carrier line a half-truth.

## 5. Production-readiness checklist

- security — N/A: a renderer change over data already in the tree.
- perf / scale — shorter rows; no new pass.
- error / empty / loading states — unchanged: an empty month renders as today.
- observability — check 9 still byte-compares every shard to a fresh render.
- risks — a reader that took a status from a shard now reads it from `memory/LIVE.md`; S1's
  Readers clause names the only such reader.
- testing — one generator self-test arm.
- migration — the next `--write` re-renders every shard once to the new columns.
- user docs — none; the frozen sentence already describes the result.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` has run on the unit's branch,
  the table header of `memory/ledger/2026-09.md` reads Build, Node and Opened, and
  `gen_build_index.py --check` exits 0.
  Red when: a shard still renders a Status, Streams or Ids column.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm renders one
  fixture build's month shard, flips a unit from SPECCED to CLOSED, adds a unit, renders again, and
  finds the two shards byte-identical.
  Red when: the second render differs, which is the frozen claim failing.
  cost: the generator's whole self-test, about ninety seconds on node a.

## 7. Gates

`memory hygiene` · `build-index selftest` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py --selftest · a shard rendered before and after a status flip and an added unit, staged red by restoring the Status column · none

## 8. Open questions

- **F1 — Which columns does a month shard keep?**
  Options: drop Status alone; keep Streams under a reworded claim; keep only Build, Node and Opened.
  §4's alternatives record why the first two leave the shard changing after its month.
  RESOLVED (agent, 2026-10-04, delegated): Build, Node and Opened.

## 9. Revision log

- rev-1 · 2026-10-04 · split from `TOOL-aMendedFleet-22` rev-1 at its F1; S1, AC1, AC2 and F1 are
  that spec's S4, AC5, AC6 and F2, unchanged.

## 10. Reuse audit

The seam extended is `render_shards` in `tools/memory-tree/gen_build_index.py`, the function that
already renders every shard. No new renderer is written.
`python tools/codebase-map/reuse_lookup.py "render the month ledger shard table"` ranked twenty-odd
`render_*` functions by name stem and did NOT name `render_shards`; a grep for `def render_shards`
finds it at `tools/memory-tree/gen_build_index.py`, the one renderer of the shard. The probe's miss
is the name-stem ranking wave 1 measured, not a missing seam. Recall, run by the writer of
`TOOL-aMendedFleet-22` with the terms below, named `TOOL-aMendedLedger-1`, which made the shards
generated.

Recall terms used: `python tools/memory-recall/query.py "how should a merge handle the generated LIVE.md and ledger shards, and was a merge driver for them declined" --terms "merge=ours merge=rows generated view LIVE.md ledger shard regenerate driver gitattributes check 9 stale render conflict"`
