# TOOL-dDeclaredLoop-66 — the build-order region derives `Parallel` from the group's write sets and edges, never from a shared order alone

**Status:** CLOSED · rev-4 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 38 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-66-deviation-661.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-66-deviation-661.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-66-deviation-662.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-66-deviation-662.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-66-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-66-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-66-deviation-663.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-66-deviation-663.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-66-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-66-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-66-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-66-reground-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-66-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-66-build-brief.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. Each round-1 promotion took
an `order` that put it in a group marked `Parallel: yes` with a unit whose Files touched intersects its
own: specs 38, 39 and 40 all rewrite tools/lib/commit_trailers.py and its copies at order 4. The
build method admits concurrent passes only on disjoint write sets with no dependency either way, and
the column is what says a group is parallel. At this spec's base the build-order render wrote `yes`
for any group of two or more. `TOOL-dGroundRules-25` and `TOOL-dGroundRules-32` have since made the
column a derivation of the group's declared write sets and edges, so the defect is closed in code.
This unit observes that derivation on this build's own regions and closes the finding on the build's
record, writing no product file (§8 F2). It builds at order 38.

## 2. Scope (IN)

- **S1** — The derivation stands as built. `tools/memory-tree/gen_build_index.py#render_order` writes
  each step's cell from `tools/memory-tree/gen_build_index.py#derive_parallel_step`, which answers `no`
  for a step of one unit, `unknown` for a step of two or more in which a member has no Files touched
  sub-head, `no` where one member consumes from another or two members' write sets meet by
  `tools/memory-tree/design_lib.py#check_writes_intersect` over the words of two or more segments, and
  `yes` otherwise. The pass observes it by a direct probe and in two rendered regions, and writes no
  product file. Observed by AC1, AC2, AC4.
- **S2** — One reader each for the sub-head and the edge. `tools/memory-tree/design_lib.py#read_spec_writes`
  is the sub-head read of both `tools/check-spec-tokens.py#extract_files_touched` and
  `tools/memory-tree/gen_build_index.py#parse_spec_text`, and
  `tools/memory-tree/design_lib.py#read_spec_edges` gives `parse_spec_text` its `consumes-from`
  targets, so no caller holds a pattern for the sub-head. Observed by AC3.
- **S3** — Rev-3's four items are each satisfied by the code S1 and S2 name, as §4 "Rev-3 against the
  built code" maps them, so the pass builds none of them. Its readers in
  `tools/memory-tree/tree_lib.py` are the two readers in `tools/memory-tree/design_lib.py`; its cell is
  S1's, which says `unknown` for a member declaring no write set and prints no reason after `no`; and
  its re-render is the branch's regions, which read `no` at steps 4 and 38. Observed by AC2.

## 3. Non-goals (OUT)

- A reason after the cell's `no` or `unknown`, rev-3's `no — <a> and <b> share <path>` form: §8 F2
  keeps it out, and §5 "The sweep" gives the generated rows it would move.
- Renumbering any unit of this build: dispatch is strictly sequential within a shared order, as the
  comment opening "DISPATCH IS STRICTLY SEQUENTIAL" in `tools/workflows/unattended-build.js` states, so
  the groups the finding names never ran concurrently, and the column now says so.
- A red gate over a shared order with intersecting write sets: it would need a dated cutoff key to spare
  landed builds, a public surface no clause of this build names; the derived column carries the fact
  without one.
- Reading the write set a build actually made: the column reads the estimate, as the guards join does.
- `TOOL-dDeclaredLoop-75`'s S24 comment and ask row and its S31 predicate: that unit's, written on the
  `render_order` and `check_writes_intersect` S1 names.

### Edges

- **consumes-from** external — the Parallel derivation TOOL-dGroundRules-25 (S37, S38) and TOOL-dGroundRules-32 (S9, S13) landed, which this unit observes and does not build
- **hands-off** `TOOL-dDeclaredLoop-75` — the ask citation, the symmetric predicate and the re-render population (the round-3 spec audit's ids 18, 34)
- **hands-off** `TOOL-dDeclaredLoop-86` — `render_order`'s Parallel cell, which that unit observes at step 38 (the round-6 spec audit's id 10)

## 4. Design

### Evidence

Read at the branch tip `adbc3ecf5` of `unattended-declared-loop-d56bf0`, from its tree as `git archive`
wrote it:

- `derive_parallel_step` answers as S1 states. Its docstring says `yes` speaks only to the estimates
  and `--dispatch` still decides. `render_order` writes one `| <n> | <ids> | <cell> |` row per `order`
  value and names the units carrying no verb on an `Unordered:` line.
- `parse_spec_text` stores each unit's `writes`, the answer of `read_spec_writes` or None, and its
  `consumes`, the targets `read_spec_edges(text, "consumes-from")` returns.
- `extract_files_touched` takes its words from `read_spec_writes` and keeps its own path and root
  predicates over them. The one other Files touched reader is the driver's awk function
  `tools/unattended/unattended.sh#read_files_touched`, which reads specs at another ref for the
  cross-run overlap check.
- The derivation landed at `b663756ca` (TOOL-dGroundRules-25) and `5412bbecd` (TOOL-dGroundRules-32),
  neither an ancestor of this spec's base `ed497191`, so rev-3's reading of a cell drawn from the
  group's length held when it was written.
- `memory/builds/dDeclaredLoop/README.md` reads `no` at step 4, where specs 38, 39 and 40 each declare
  tools/lib/commit_trailers.py, and at step 38, where `TOOL-dDeclaredLoop-67` shares
  `tools/loop/position.py` with `TOOL-dDeclaredLoop-74`, and `tools/loop/budget.py` and
  `tools/loop/breakpoints.py` with `TOOL-dDeclaredLoop-80`.
- `memory/builds/aTunedCompass/README.md` reads `unknown` at step 2, because `TOOL-aTunedCompass-10`,
  CLOSED, carries no Files touched sub-head.
- Over every build README the region holds 128 `yes`, 1529 `no` and 17 `unknown` rows, in 214 PINNED
  READMEs at `adbc3ecf5`; §5 "The sweep" re-derives them.
- The round-2 probe found 14 shared-order groups and 13 intersecting pairs: PINNED, 2026-10-24.

### The cell, as built

```
group of one                                        -> no
some member has no Files touched sub-head           -> unknown
some member consumes-from another member            -> no
some pair's write sets meet (directory included)    -> no
otherwise                                           -> yes
```

### Rev-3 against the built code

| Rev-3 item | Built as | By |
|---|---|---|
| S1, a sub-head reader in `tools/memory-tree/tree_lib.py` | `read_spec_writes` in `tools/memory-tree/design_lib.py`, read by `extract_files_touched` and `parse_spec_text` | TOOL-dGroundRules-25 S37 |
| S2, an edge reader there | `read_spec_edges` in `tools/memory-tree/design_lib.py` | TOOL-dGroundRules-32 S17 |
| S3, the derived cell | `derive_parallel_step`, with `unknown` for an undeclared write set and no reason text (F2) | TOOL-dGroundRules-25 S37, S38; TOOL-dGroundRules-32 S9, S13 |
| S4, the re-render | every build README's region, derived at the branch tip | both units' passes |

### Files touched (estimate)

- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-66.md`, its status line alone

The pass writes no product file. The driver's `--dispatch --pass` refuses a declaration naming no
`--writes` path (`tools/unattended/unattended.sh#check_verb_flag`, from `VERB_REQUIRES`), so the one
path declared is the file the pass does write; its acceptance ledger and other records are the run's.

### Alternatives rejected

- **Building rev-3's reason text.** §8 F2's option (b): it re-renders every step of two or more for a
  reason a reader can re-derive from the specs, and the finding asked for the derivation alone.
- **A third copy of the sub-head reader.** The reuse rule's second-instance factory is
  `read_spec_writes`; the driver's awk reader lives inside a bash gate and stays there.
- **Renumbering the colliding units.** A spec change to thirteen units of this build for a fact the
  renderer derives, and the next build would collide again.

## 5. Production-readiness checklist

- security — no new surface; the pass reads.
- perf / scale — nothing moves; the render's cost is the built derivation's.
- error / empty / loading states — a member with no Files touched sub-head reads `unknown` (AC4), and
  a step of one reads `no`.
- observability — each cell reads `yes`, `no` or `unknown`; why a `no` stands is re-derived from the
  specs and not printed (F2).
- risks — an estimate that under-declares reads disjoint, as it does for the guards join, and the
  closing review reads the real diff. A one-segment root declares nothing, so two units meeting only
  there read `yes`.
- testing — AC1 probes `derive_parallel_step` directly and AC2 to AC4 read the tree; no arm is added,
  since the selftest's five Parallel arms stand.
- migration — none; no stored data changes shape.
- user docs — none: `help/` holds no page on the build-order region.

### The sweep

Read at the branch tip `adbc3ecf5`; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| this spec's Files touched, three product paths to its own spec path | `derive_parallel_step` over step 38; `--dispatch --pass`'s declared set; the driver's `read_files_touched` for the cross-run overlap; the spec-token checker's guard join through `extract_files_touched` | step 38 reads `no` either way, from the pairs 67 with 74 and 67 with 80, as a probe of `derive_parallel_step` over the four specs showed with 66's set emptied, and 67's declared spec directory also holds 66's spec; the declaration names one path, which `check_verb_flag` asks for; the cross-run check meets the path only where another ref changes this spec; the path trips the guards of `recall floor` and `recall floor arms`, which the §7 leg line names |
| the §7 leg line, six legs to five, and its `New arm:` line, which is gone | the spec-token checker's leg join and its `covers` grade; the close's RED and GREEN observation of a declared arm | the five named legs are in the manifest; no arm is declared, so the close owes no RED observation |
| rev-3's planned `tree_lib.py` readers and its cell change | none: neither was built, no symbol is minted, and the generator, the token checker and `tools/memory-tree/tree_lib.py` keep their bytes | nothing reads an unbuilt name; the driver's `read_files_touched` is a separate bash function and is not touched |
| the Edges block, its stray `none` line taken out and an external `consumes-from` added | the hygiene edge-shape and reciprocity arms; `read_spec_edges` for `parse_spec_text` and for the token checker's hands-off join | both hands-off bullets keep their bytes, so 75's and 86's reciprocal `consumes-from` lines still meet; `external` is no member id, so step 38's cell does not move |
| this spec's line citations | `memory/project/positional-refs.txt`, its 9 PINNED rows for this spec, under `positional (the citation check alone)` | this revision cites symbols and paths only, so the commit landing it runs `python tools/playbook/positional.py shrink` |
| the criteria, re-pointed at the built code | the acceptance ledger at the close; the token checker's witness, `ac-order` and `bar` joins | AC1 to AC4 ascend, each carries a backticked command and a `Red when:`, and none spells the runner |
| sibling specs naming this unit | `TOOL-dDeclaredLoop-75` S24, S31 and its Edges; `TOOL-dDeclaredLoop-79` S16 and AC16, on 75's ask row; `TOOL-dDeclaredLoop-82` S14 and AC14 at step 39; `TOOL-dDeclaredLoop-86` S14 and AC14 at step 38 | steps 38 and 39 already read `no`; `render_order` and `check_writes_intersect` are the functions those specs name, written by the two dGroundRules units; each re-grounds its author attribution and its stale fixture note at its own pass |
| the build's records | deviation `2026-10-24-build-TOOL-dDeclaredLoop-66-deviation-662`, which records rev-2 and rev-3 past the audited rev-1, and the README's `TOOL-dDeclaredLoop-66@rev-1` audited-revision entry | this re-ground is recorded as the run records its siblings' re-grounds; no record is written by this spec |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:memory/builds/dDeclaredLoop/README.md" | grep -E "^\| (4|38|39) \| .TOOL-dDeclaredLoop-[0-9]+., "
git show "$B:memory/builds/aTunedCompass/README.md" | grep -E "^\| 2 \| .TOOL-aTunedCompass-10"
git grep -c -e 'read_spec_writes(text)' "$B" -- tools/check-spec-tokens.py tools/memory-tree/gen_build_index.py   # 1 and 1
git grep -c -e 'FILES_TOUCHED_HEAD' "$B" -- tools                                    # design_lib.py alone, 2
git grep -h -E '^\| [0-9]+ \| .*\| (yes|no|unknown) \|$' "$B" -- 'memory/builds/*/README.md' | awk -F'|' '{print $(NF-1)}' | sort | uniq -c   # DERIVED
git grep -l -e 'gen:build-order -->' "$B" -- 'memory/builds/*/README.md' | wc -l      # DERIVED
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-66.md'   # 9
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED, since no name is
  minted.
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead.
- The refusal ceilings and families: `tools/memory-tree/check-arms.py#scan_refusal_sites` reads tracked
  `*.sh` files, and this unit edits none. `REFUSAL_CEILINGS` in `.memory-tree.conf` keeps the driver
  at 343 PINNED and `tools/unattended/check-unattended.sh` at 266 PINNED, and
  `tools/unattended/unattended.families.txt` does not move.
- Help anchors and usage rows: no verb and no flag is added, and no `tools/govkit/usage.toml` row moves.
- Subject pins, epoch delegates, upgrade rows, size caps and the kickoff watch list: no leg is added;
  no file `check-verdict-epoch.sh` delegates to is edited; no data changes shape, so no `[[upgrade]]`
  row is owed; the README slot ceilings in `tools/memory-tree/build-readme-slot-limits.txt` read
  authored slices alone and no authored README slot is written; no path on the `watch:` line of
  `memory/guides/SESSION-KICKOFF.md` is edited; no shipped byte moves, so no kit version is owed.

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'                  # "1215"
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'               # 343 and 266
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
```

### Dependency

The derivation is TOOL-dGroundRules-25's and TOOL-dGroundRules-32's, both CLOSED and landed on main and
on the branch. No committed spec at orders 34 to 38 edits `gen_build_index.py`, `design_lib.py` or
`check-spec-tokens.py`: a probe of every live spec's Files touched through `read_spec_writes` found
`tools/memory-tree/` paths only in `TOOL-dDeclaredLoop-67` (`routed_commits.py`) and
`TOOL-dDeclaredLoop-68` (`HYGIENE.template.md`) at those orders. `TOOL-dDeclaredLoop-33` (order 34,
committed rev-7, rev-8 coming), `TOOL-dDeclaredLoop-52` and `TOOL-dDeclaredLoop-53` (order 34, built),
`TOOL-dDeclaredLoop-54`, `-55`, `-63` and `-64` (order 35), `TOOL-dDeclaredLoop-56`, `-70`, `-71` and
`-72` (order 36), and `TOOL-dDeclaredLoop-65`, `-68` and `-76` (order 37) each change the loop kit, the
driver or other kit files, which can move step 38's or step 39's members only by their Files touched;
step 38 reads `no` through 67's shares, which 67 owns. At order 38, `TOOL-dDeclaredLoop-67`, `-74` and
`-80` build beside this unit, which writes only its own spec, a file inside the spec directory 67
declares; dispatch is sequential, so the two never write it at once. `TOOL-dDeclaredLoop-75` (order 39),
`-82` (order 41) and `-86` (order 42) read this unit's name, as the sweep says.
`TOOL-dDeclaredLoop-34` is deferred against ask TOOL-dDeclaredLoop-113 and `TOOL-dDeclaredLoop-33`'s
numeric direction against ask TOOL-dDeclaredLoop-114; neither touches the render. Every code claim was
read at the branch tip; the reuse probe and the spec-token checker ran on this spec's worktree at
`179486e8f`, cut from main, whose `gen_build_index.py`, `design_lib.py` and `check-spec-tokens.py`
carry the same derivation and readers.

## 6. Acceptance criteria

- **AC1** — When a probe run in `tools/memory-tree/` imports `gen_build_index` and calls
  `derive_parallel_step` on steps of `{"id", "writes", "consumes"}` units, it answers `no` for one unit;
  `no` for two units declaring one common two-segment path; `no` where one declares a two-segment
  directory over the other's path; `yes` for disjoint paths; `no` where the second consumes from the
  first over disjoint paths; and `unknown` where the second's writes are None.
  Red when: a step sharing a path, nesting one in a declared directory or holding a `consumes-from`
  edge reads `yes`, as a cell drawn from the group's length alone does.
- **AC2** — When `grep -E "^\| (4|38) \| .TOOL-dDeclaredLoop-[0-9]+., " memory/builds/dDeclaredLoop/README.md`
  runs at the pass, it prints two rows, each ending `| no |`.
  Red when: step 4 reads `yes` over specs 38, 39 and 40, which all declare tools/lib/commit_trailers.py.
- **AC3** — When `grep -c "read_spec_writes(text)" tools/check-spec-tokens.py tools/memory-tree/gen_build_index.py`
  runs, it prints 1 for each file, and `grep -c FILES_TOUCHED_HEAD` over
  `tools/memory-tree/design_lib.py`, `tools/check-spec-tokens.py` and
  `tools/memory-tree/gen_build_index.py` prints 2, 0 and 0.
  Red when: a caller holds its own pattern for the sub-head, so two readers can disagree on a spec.
- **AC4** — When `grep -E "^\| 2 \| .TOOL-aTunedCompass-10" memory/builds/aTunedCompass/README.md` runs,
  it prints one row, ending `| unknown |`.
  Red when: a step holding a member with no Files touched sub-head reads `yes`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `build-index selftest` · `recall floor` · `recall floor arms`

This unit adds and moves no arm. The generator's selftest already holds five Parallel arms, landed by
TOOL-dGroundRules-25 and TOOL-dGroundRules-32, which the `build-index selftest` leg runs; AC1 is the
pass's direct probe of the same function.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — What does this unit build, now that the derivation has landed?** TOOL-dGroundRules-25 and
  TOOL-dGroundRules-32 built rev-3's readers, cell and re-render, all but the reason text after `no`,
  and with `unknown` where rev-3 wrote `no — <a> declares no write set`. Options: (a) build nothing,
  and close on observing the built derivation over this build's regions, declaring the spec's own file
  as the pass's one write; (b) build the reason text,
  `no — <a> and <b> share <path>`, `no — <a> consumes <b>` and `unknown — <a> declares no write set`,
  in `derive_parallel_step`, with selftest arms and a re-render of every build README's steps of two or
  more; (c) take the unit to WONTDO, superseded by the two dGroundRules units. (b) re-renders every
  step of two or more across 214 PINNED READMEs for a reason a reader can re-derive from the specs,
  which the finding did not ask for; (c) changes the unit's status, which this re-ground keeps.
  Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), under the run's mandate, per the
  brief `2026-11-16-prompt-TOOL-dDeclaredLoop-66-1-spec-writer`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-4 · 2026-11-16 · §1 to §10 · S1 to S3 · AC1 to AC4 · §8 F2 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `adbc3ecf5`, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-66-1-spec-writer`: TOOL-dGroundRules-25 and TOOL-dGroundRules-32
  built rev-3's readers, cell and re-render after this spec's base, so by F2 the unit writes no product
  file, its Files touched names its own spec for the dispatch's one required path, and its criteria
  observe the built derivation; the Edges block takes out its stray `none` and gains the external
  `consumes-from`; citations by symbol; the sweep.

## 10. Reuse audit

The seams are the built ones: `tools/memory-tree/gen_build_index.py#derive_parallel_step`, which
`render_order` calls, and `tools/memory-tree/design_lib.py#read_spec_writes`, which the generator and
`extract_files_touched` share. `python tools/codebase-map/reuse_lookup.py "units sharing a build order
whose write sets intersect"` and `python tools/codebase-map/reuse_lookup.py "derive parallel step from
disjoint write sets"`, run on the worktree at `179486e8f`, ranked `write`, `write_text`, `build`,
`units`, `step` and `write_commit` by fan-in, none of which reads a write set; reading `render_order`
found the seam.
This unit extends neither, because both already do what it asked.

Recall terms used: build order parallel step group Files touched write set disjoint render_order derive_parallel_step consumes-from
