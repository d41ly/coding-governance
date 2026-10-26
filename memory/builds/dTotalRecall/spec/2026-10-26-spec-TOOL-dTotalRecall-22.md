# TOOL-dTotalRecall-22 — each edge type's cardinality declared per source and per target, mirrored in the kind registry, and checked over the merged tree after every merge

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 10 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0233@50683b2a whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-7 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-25 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-22-deviation-221.md](../build/2026-10-26-build-TOOL-dTotalRecall-22-deviation-221.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-3 TOOL-dTotalRecall-2 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

Every edge type declares how many edges of it one source may carry and how many one target may
receive, and a check counts both over the merged tree after every merge, so two records superseding
one decision on separate branches, which git merges clean, are red on the merged tree (gap-mem-42;
`night-pass-two.md:237-240`, `:269-270`, probe D). Today the only per-target rule in the tree is the
as-built view's one-head-per-clause rule (`tools/memory-tree/asbuilt_view.py:322-366`), and the planned
edge gates count per source only ("a second edge line of one type", `memory-plan.md:366`).

## 2. Scope (IN)

- **S1** — A `cardinality = { per-source = "<n|many>", per-target = "<n|many>" }` key on every
  declared `[[edge]]` row of `tools/playbook/edges.toml` (I10), its values per §4 "The bounds". A
  declared row without it, or with a value that is not a positive integer or `many`, is red in the
  registry's own parse. Observed by AC1.
- **S2** — The mirror in the kind registry: the `cardinality` column of `tools/memory-tree/record-kinds.toml`
  (I1), on each `[[record-kind]]` row whose kind's records declare an edge of a bounded type, holds that
  type's bounds, and `check_edge_cardinality --registry` reds an entry that differs from `edges.toml`
  or names an unregistered type. Observed by AC2.
- **S3** — The counter, `count_edge_cardinality(edges, bounds)` in `tools/memory-tree/design_lib.py`,
  beside `derive_pin_hash` (PLAY-dOrderedCharter-24 S7), generalised from `resolve_clause_rows`' head
  rule: it groups edges by `(type, source)` and by `(type, target)` and returns one violation per group
  past its bound, naming the type, the end, the bound and every member. Observed by AC3.
- **S4** — `resolve_clause_rows` (`tools/memory-tree/asbuilt_view.py:322`) computes its "two or more
  heads" case through `count_edge_cardinality`, over the derived head relation with per-target bound
  1, its finding text and its verdicts unchanged; its no-head (cycle) case stays its own. Observed by
  AC4.
- **S5** — The check, `check_edge_cardinality(root)` in `tools/playbook/edge_grammar.py`, and its CLI
  `edge_grammar.py --cardinality`: every declared edge of the tree's file sites, read by the parser's
  site adapters (PLAY-dOrderedCharter-28 S5) and by `gen_build_index.py --print-relations`
  (TOOL-dTotalRecall-6) for the README site, targets normalised by PLAY-dOrderedCharter-19's resolver
  so two address forms of one node count once, counted by `count_edge_cardinality`; exit 1 with one
  line per violation, exit 0 with a line naming the edge and type counts read. Observed by AC5 and AC6.
- **S6** — The leg `edge cardinality (per source and per target, over the merged tree)` in
  `tools/gate-legs.json`, argv `python {prefix}/playbook/edge_grammar.py --cardinality`, `"pack":
  "tags"`, so the bar runs it before a push and `tools/run-gates/post-merge.sh` runs it on every landed
  sha, which `tools/push-main.sh:445-455` starts after every landing. Observed by AC7.

## 3. Non-goals (OUT)

- The edge types, their `from` and `to`, the grammar and the parser: PLAY-dOrderedCharter-24's and
  -28's; this unit adds one key to their rows and one verb to their module.
- Commit trailers as a counted site: a commit is not in the merged tree, and none of the bounded types
  of §4 is declared by a trailer.
- Prose supersession in records written before typed edges: it is no edge, and nothing counts it.
- The relation keys and their inversion: TOOL-dTotalRecall-6's; this unit counts their edges.
- Bounds for types the design states nothing about: those rows declare `many` on both ends, written,
  never defaulted.

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record-kinds.toml`, whose `cardinality` column this unit
  adds after `purpose`
- **consumes-from** `TOOL-dTotalRecall-6` — `depends-on` and the README-site types, read from
  `--print-relations`, whose per-target counts the check takes
- **consumes-from** external — PLAY-dOrderedCharter-24 S1's and -28 S1's `edges.toml` rows and S3/S5's
  parser and site adapters in `tools/playbook/edge_grammar.py`; PLAY-dOrderedCharter-19 S6's address
  resolver; PLAY-dOrderedCharter-19 S12's `pack` key in `tools/gate-legs.json`
- **hands-off** `TOOL-dTotalRecall-39` — `edge_grammar.py --cardinality`, which that unit's AC3 runs over a bulleted cause (the round-1 audit's id 23)
- **hands-off** `TOOL-dTotalRecall-43` — `--cardinality` with memory-tree absent, the `design_lib` reach and the leg's meta-gate rows, which that unit changes for the round-1 audit's ids 20, 40 and 63

## 4. Design

### The bounds

| Type | `per-source` | `per-target` | Why |
|---|---|---|---|
| `supersedes` | `many` | `1` | one node is superseded by one successor; probe D's merge (`night-pass-two.md:237-240`) |
| `caused-by` | `1` | `many` | a record has one cause; `deviation_join.py:247-248` already refuses a `**Caused-by:**` that is not one id |
| every other declared type | `many` | `many` | the design states no bound |

The derived `cites` row carries no key: a derived type is never declared, so nothing counts it.

### The mirror

A record kind's row mirrors the bounds of each bounded type its records declare, read from its
schema's edge fields. At this unit's pass those are the kinds whose schema names `**Caused-by:**` or
`**Supersedes:**` (the deviation record, `deviation_join.py:145-147`, and any kind unit 1 registers
with either); the pass derives the list from the registry and records it in its commit's `Decided:`
trailer.

```toml
[[record-kind]]
name = "deviation"
# ... unit 1's and unit 16's columns ...
cardinality = { caused-by = { per-source = "1", per-target = "many" }, supersedes = { per-source = "many", per-target = "1" } }
```

### The count

```python
count_edge_cardinality(edges, bounds) -> list[Violation]
# edges:  iterable of (type, source, target, where)   where = "<path>:<line>"
# bounds: {type: (per_source, per_target)}            "many" or an int
# Violation(type, end, node, bound, members)          end is "source" or "target"
```

Pure, no I/O, and the one implementation both callers use: `resolve_clause_rows` passes the edges
`(head, member, clause)` for each member no other member supersedes, with bound per-target 1, and
maps a violation to its existing `unordered amends of <clause>` finding; `check_edge_cardinality`
passes every declared edge with the registry's bounds. The playbook kit reaches `design_lib.py`
through its `resolve_kit_dir` copy, as it reaches `derive_pin_hash`.

### The check

Population: the files tracked at `HEAD` of the tree the check runs in, so on a merge commit it is the
merged tree. Sites read: a record's header lines, a record section's `**Edges:**` lines, an
instruction unit's `edges` list, a `gov:note` `refs=` segment and a spec's `**Carries:**` line, each
by its PLAY-dOrderedCharter-28 S5 adapter, and the README relations by `--print-relations`. A target
is normalised to the node the resolver returns, so `PLAY-dX-3` and its tag count as one; an edge whose
target does not resolve is counted under its written form. Output lines:

```
cardinality: supersedes per-target 1 exceeded at PLAY-xDec-1 by memory/builds/xA/build/…:7, memory/builds/xB/build/…:7
cardinality: read <n> edges of <k> types; <v> violations
```

### Inventory

Minted: the `cardinality` key on `[[edge]]` rows and the `cardinality` column on `[[record-kind]]`
rows; `count_edge_cardinality`, `Violation`, `check_edge_cardinality`; the flags `--cardinality` and
`--registry` of `edge_grammar.py`; the leg `edge cardinality (per source and per target, over the
merged tree)`. Naming cells: the two functions are asked of the lexicon's `--suggest` under `--as
py.function` at the pass.

### Migration

None. Today's tree declares no `**Edges:**` line and no README relation beyond `parents:`, so the
check's first run reads only header edges, and no record carries two `**Caused-by:**` lines (PINNED,
measured 2026-10-26 at `fb872a37e` by `git grep -c` over `memory/`; AC6 re-derives it).

### Files touched (estimate)

- `tools/playbook/edges.toml`
- `tools/playbook/edge_grammar.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/record-kinds.toml`
- `tools/gate-legs.json`

### Alternatives rejected

- **Declare cardinality only in the kind registry.** The types live in `edges.toml`; bounds kept apart
  from their types would let a type be registered with none. The registry mirrors them under a parity
  arm (S2).
- **Copy `resolve_clause_rows`' rule into the new check.** Two per-target counters would drift; the
  brief and the reuse rule both ask for the generalisation.
- **A dedicated post-merge hook.** `post-merge.sh` already runs the whole bar on every landed sha, so
  a leg is checked there with no second mechanism.

## 5. Production-readiness checklist

- security — no write path; read-only over tracked files and the registry.
- perf / scale — one pass over the edges the site adapters already parse; the count is linear.
- error / empty / loading states — an empty population prints its zero counts and exits 0, said on
  the line rather than silent; an unregistered type is the registry parse's red, not this check's.
- observability — every violation names the type, the end, the bound and each member's path and line.
- risks — a supersession written in prose is invisible to the count; only typed edges are graded.
- testing — AC1 to AC7 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — none under `help/`: no page describes edge types; the atlas, TOOL-dTotalRecall-26's,
  renders the registry.

## 6. Acceptance criteria

- **AC1** — When a probe reads `edges.toml` with `tomllib`, every row whose `status` is `declared`
  carries `cardinality` with both ends, `supersedes` reads `per-target = "1"` and `caused-by` reads
  `per-source = "1"`; with the key cut from one row in a scratch clone, `edge_grammar.py --list` exits
  non-zero naming that row.
  Red when: a declared row parses with no bound.
- **AC2** — When `edge_grammar.py --cardinality --registry` runs at the pass tip it exits 0; with the
  `deviation` row's `supersedes` entry changed to `per-target = "many"` in a scratch clone, it exits 1
  naming `deviation`, `supersedes` and both values.
  Red when: the mirror is not compared, so the registry can disagree with `edges.toml`.
- **AC3** — When a probe calls `count_edge_cardinality` with two edges `("supersedes", "A", "D", …)`
  and `("supersedes", "B", "D", …)` and bound `(many, 1)`, it returns one violation at target `D`
  naming both members; with bound `(many, many)` it returns none.
  Red when: the count groups by source only.
- **AC4** — When `asbuilt_view.py` runs its plant arms at the pass tip, the two-heads plant still
  prints its `unordered amends of` finding with the same text as at base `462d20f3`, and a probe that
  stubs `count_edge_cardinality` to return nothing makes that finding disappear.
  Red when: `resolve_clause_rows` keeps a private copy of the head count.
- **AC5** — When `git merge` joins two branches of a fixture repository under `%TEMP%/<short>`, each
  adding one record whose section carries `**Edges:** supersedes=PLAY-xDec-1` against a tree defining
  that decision, the merge is clean, `edge_grammar.py --cardinality` exits 0 on each branch alone, and
  exits 1 on the merge commit naming `PLAY-xDec-1` and both records.
  Red when: the per-target count is absent, so the merged tree passes.
- **AC6** — When `edge_grammar.py --cardinality` runs at the pass tip, it exits 0 and its last line
  names the edges and types it read, the edge count above zero.
  Red when: the population is empty and the zero is read as a pass, or today's tree reds.
  figure: the counts are DERIVED at each run.
- **AC7** — When a probe reads `tools/gate-legs.json`, one row named `edge cardinality (per source and
  per target, over the merged tree)` carries an argv ending in `edge_grammar.py --cardinality` and
  `"pack": "tags"`.
  Red when: the check is not in the bar, so the post-merge run never reaches it.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `playbook render wiring` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `memory hygiene`

New arm: tools/playbook/edge_grammar.py · covers AC1 AC2 AC3 AC5 · its `--fixture --plant` cases gain `cardinality-merge` (the two-branch supersession merged clean), `cardinality-missing` (a declared row with no key) and `cardinality-mirror` (a registry entry that differs), staged by dropping the per-target group · none
New arm: tools/memory-tree/asbuilt_view.py · covers AC4 · its plant arms keep the two-heads finding through the shared counter, staged by stubbing the counter · none
New arm: tools/gate-legs.json · covers AC6 AC7 · the new leg itself, observed red on the AC5 merge fixture and green at the tip · none

## 8. Open questions

- **F1 — Where is cardinality declared: the kind registry, as the clause says, or the edge rows, where
  the types live?** Options: (a) on each `edges.toml` row, mirrored in the kind registry under a parity
  arm; (b) in the kind registry alone; (c) on the edge rows alone. (b) separates a type from its bound;
  (c) fails the clause's "in the kind registry". RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the brief's I10, the registry mirror checked both ways by S2; the new required key on the parent's
  row is deviation 221 (`2026-10-26-build-TOOL-dTotalRecall-22-deviation-221.md`). widens: none ·
  relaxes: none
- **F2 — Which types are bounded?** Options: (a) every declared type with a bound the records state,
  `many` written elsewhere; (b) a guessed bound per type. (b) invents rules no record states, and each
  invented bound reds legitimate records. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1: probe D
  states `supersedes` per target (`night-pass-two.md:237-240`) and the deviation grammar states
  `caused-by` per source (`deviation_join.py:247-248`). widens: none · relaxes: none
- **F3 — The brief's I5 spells a section's edge line `**Edges:** <type> <target>`, and
  PLAY-dOrderedCharter-24 S2 spells it `**Edges:** type=target[,target]`.** Options: (a) read edges
  only through the parent's parser, so this unit spells no grammar and its fixtures use the parser's;
  (b) parse I5's spelling here. (b) is a second edge parser. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, PLAY-dOrderedCharter-24 S2 is the grammar's spec; the disagreement is named in this
  unit's return for the I5 owner, TOOL-dTotalRecall-19. widens: none · relaxes: none
- **F4 — Is "after every merge" a new hook?** Options: (a) a leg in the bar, which `post-merge.sh` runs
  on every landed sha; (b) a dedicated post-merge script. (b) is a second post-merge mechanism.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, tie-broken by reuse of `post-merge.sh`.
  widens: none · relaxes: none
- **F5 — The parents are specced and not built.** `edges.toml`, `edge_grammar.py`, the resolver and
  the `pack` key are DEFERRED at `462d20f3`. RESOLVED (agent, 2026-10-26, delegated): this spec calls
  them as their specs name them, and the build run re-grounds on the landed code, rung 1 (the brief's
  chain rule). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 22, the brief's shared interfaces I1 and
  I10, scout A's row for cl-0233, and the head rule read at `fb872a37e`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-39, TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam extended is `resolve_clause_rows` (`tools/memory-tree/asbuilt_view.py:322`), whose
one-head-per-clause rule is the tree's only per-target count, generalised into `count_edge_cardinality`
beside `derive_pin_hash` in `tools/memory-tree/design_lib.py`, the module the playbook kit already
reaches; the check extends PLAY-dOrderedCharter-24/28's `edge_grammar.py`, and the "after every merge"
point is the bar `tools/run-gates/post-merge.sh` runs (started by `tools/push-main.sh:445-455`). The
lookup, `python tools/codebase-map/reuse_lookup.py "count edges per target and refuse two records superseding one node"`,
ranked `counts`, `read_records`, `render_record` and `check_records` and did not list
`resolve_clause_rows`, which scout A's row found. The recall probe returned scout A's row, the brief's
I10 and dOrderedCharter's edge-registry scout; scout A's lines held at `fb872a37e`.

Recall terms used: `python tools/memory-recall/query.py "how is an edge type's cardinality checked per target after a merge" --terms "cardinality per-target per-source supersedes merged tree post-merge probe D resolve_clause_rows head edges.toml"`
