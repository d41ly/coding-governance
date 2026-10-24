# TOOL-dDeclaredLoop-66 — the build-order region derives `Parallel` from the group's write sets and edges, never from a shared order alone

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 38 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-66-deviation-661.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-66-deviation-661.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. Each round-1 promotion took
an `order` that put it in a group marked `Parallel: yes` with a unit whose Files touched intersects its
own: specs 38, 39 and 40 all rewrite `tools/lib/commit_trailers.py` and its copies at order 4, and the
report names ten more pairs, plus spec 49 counting over homes spec 48 defines. BUILD-METHOD M6 admits
concurrent passes only on disjoint write sets with no dependency either way, and the column is what
says a group is parallel. `render_order` (`tools/memory-tree/gen_build_index.py:1716`) writes `yes` for
any group of two or more, so the record states a parallelism the tree's own declarations refute. This
unit makes the column a derivation of those declarations. The defect lands on several units, so this
unit repairs none in particular and builds after every unit (order 38).

## 2. Scope (IN)

- **S1** — `tools/memory-tree/tree_lib.py` gains `read_files_touched(text)`: every backticked word under
  the `### Files touched` sub-head, spelled with or without ` (estimate)`, the body closed at the next
  heading of any depth, in order and without repeats; `None` when the sub-head is absent.
  `tools/check-spec-tokens.py`'s `extract_files_touched` (:530) calls it and keeps its own path
  predicates over the words, so the sub-head is read in one place. Observed by AC1, AC4.
- **S2** — `tree_lib.py` gains `read_edges(text)`: each column-0 `**consumes-from**` and `**hands-off**`
  bullet of the `### Edges` block with its backticked unit id, the grammar
  `tools/memory-tree/check-memory-hygiene.sh:2474` grades. Observed by AC2.
- **S3** — `render_order` writes `yes` for a group only when every pair of members has disjoint write
  sets, a declared directory of two or more segments read as everything under it, and no member's
  `consumes-from` names another member. Otherwise the cell is `no` followed by the first reason in id
  order: `<a> and <b> share <path>`, or `<a> consumes <b>`. A member with no Files touched sub-head makes
  the cell `no — <a> declares no write set`, because disjointness it cannot read is not proven. A group
  of one stays `no`. Observed by AC1, AC2, AC3.
- **S4** — The regions re-render: `gen_build_index.py --write` moves every build README whose group
  S3 does not prove parallel, this build's and `aTunedCompass`'s order 2 among them, and `--check`
  reds a hand-typed `yes` from then on, as it reds any stale generated region. Observed by AC3.

## 3. Non-goals (OUT)

- Renumbering any unit of this build: dispatch is strictly sequential within a shared order
  (`tools/workflows/unattended-build.js:76-81`), so the groups the finding names never ran concurrently,
  and from this unit on the column says so.
- A red gate over a shared order with intersecting write sets: it would need a dated cutoff key to spare
  landed builds, a public surface no clause of this build names; the derived column carries the fact
  without one.
- Reading the write set a build actually made: the column reads the estimate, as the guards join does.

### Edges

none

## 4. Design

### Evidence

- `render_order` writes `{'yes' if len(us) > 1 else 'no'}` (`tools/memory-tree/gen_build_index.py:1732`)
  and reads no field beyond `id` and `order` of each unit.
- A probe over every live spec of the tree on 2026-10-24, importing `extract_files_touched` from
  `tools/check-spec-tokens.py`, found 14 shared-order groups and 13 intersecting pairs: twelve in this
  build and one in `aTunedCompass` (`memory/guides/SESSION-KICKOFF.md` at order 2): PINNED, that date.
- Each unit record carries its spec `path` (`tools/memory-tree/gen_build_index.py:522`), so the renderer
  can read the spec it already parsed the header of.

### The cell

```
group of one                                   -> no
some member has no Files touched sub-head      -> no — <a> declares no write set
some pair shares a path (dir prefix included)  -> no — <a> and <b> share <path>
some member consumes-from another member       -> no — <a> consumes <b>
otherwise                                      -> yes
```

### Rollout

The column's meaning moves from "declared together" to "proven disjoint", in every build at once, at
this unit's `--write`. The README renders it moves are generated regions, so no authored text changes.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/check-spec-tokens.py`

### Alternatives rejected

- **A third copy of the sub-head reader inside the generator.** The reuse rule's second-instance factory
  is S1; the two awk readers in `tools/unattended/unattended.sh:3389` and the hygiene check live inside
  bash gates and stay there.
- **Renumbering the colliding units.** A spec change to thirteen units of this build for a fact the
  renderer can derive, and the next build would collide again.

## 5. Production-readiness checklist

- security — no new surface; a render.
- perf / scale — the renderer reads each ordered spec once more, already in memory from its header read.
- error / empty / loading states — S3's `declares no write set` names the unreadable case.
- observability — each `no` cell names its reason.
- risks — a spec whose estimate under-declares reads disjoint; the estimate is the declaration both the
  guards join and this cell trust, and the closing review reads the real diff.
- testing — AC1 to AC4 as `--selftest` fixtures and a probe; the arm under §7, observed at the close.
- migration — S4's re-render.
- user docs — none: `help/` holds no page on the build-order region.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --selftest` builds a fixture build whose two
  order-2 specs both list one path under Files touched, the rendered row's last cell reads `no` and names
  that path after `share`, and with disjoint lists it reads `yes`.
  Red when: the cell is `yes` for any group of two, as `gen_build_index.py:1732` writes today.
- **AC2** — When the fixture's second spec carries `- **consumes-from**` naming the first, with disjoint
  lists, the row reads `no — ... consumes ...`.
  Red when: a dependency inside a group renders as parallel.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --write` runs over the tree, the
  `gen:build-order` region of `memory/builds/dDeclaredLoop/README.md` reads `no` on its order-4 row, naming
  `commit_trailers.py` or another shared path.
  Red when: the region keeps `yes` over specs 38, 39 and 40.
- **AC4** — When a probe imports `tools/check-spec-tokens.py` and calls `extract_files_touched` on every
  live spec before and after this unit, the two answers are equal.
  Red when: the move of the sub-head read into `tree_lib.py` changes a guards-join input.

## 7. Gates

`build-index selftest` · `memory-hygiene self-test` · `tier2-review self-test` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 · the shared-path, shared-directory and consumes-from fixture groups, staged against the length-only cell · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 1 (HIGH, item H1).

## 10. Reuse audit

The seams are the generator's own `render_order` and the sub-head reader `extract_files_touched`
(`tools/check-spec-tokens.py:530`), lifted into the kit's shared `tree_lib.py` so both read one body;
the edge grammar is the one the hygiene check grades. `python tools/codebase-map/reuse_lookup.py "units
sharing a build order whose write sets intersect"` ranked `write`, `build`, `write_text`, `units`,
`build_commit` and `build_fixture`; none reads a write set, so beyond the two readers named no existing
seam fits.

Recall terms used: build order parallel group Files touched write set disjoint render_order gen_build_index consumes-from M6
