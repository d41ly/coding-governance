# TOOL-dTotalRecall-45 — the three id readers outside unit 38's table parse through the grammar, each site held gone by file and line

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 35 at HIGH**. It shares item **H1** with id 1, which `TOOL-dTotalRecall-44`
closes. Unit 38's AC3 greps three kits for one quote style only, so it certifies readers it never
reads. Three id readers outside its table still split, each read at base `462d20f3`:

- `tools/branch-reconcile/branch_reconcile.py:520`, `derive_names`, adds `i.split("-")[1]` for each id
  `ID_RE.findall` returns from a commit subject;
- `tools/memory-tree/row_grammar.py:1116`, `scan_records`, keys each row's `slug` as `rid.split("-")[1]`;
- `tools/memory-tree/gen_build_index.py:8576`, `render_spec_skeleton`, writes the node as
  `spec_id.split('-')[1][0]`, single-quoted, which AC3's `"-"` pattern misses.

Under the hyphenated `in-slug` flip the first two answer `d2026` for `TOOL-d2026-10-26ClosedLoop-3`. The
third still answers `d`, because a slug's first character is its node whatever follows it, but it is a
split the census lists and no parse holds it. This unit re-points the three and holds every split id reader gone by file and line, in both quote styles, over
the whole tool root. It repairs `TOOL-dTotalRecall-38`.

## 2. Scope (IN)

- **S1** — `derive_names` in `tools/branch-reconcile/branch_reconcile.py` takes each id's slug from
  `parse_id_parts`, reached as `TOOL-dTotalRecall-5` §4 "The readers" routes a kit that does not require
  memory-tree: its `resolve_kit_dir` copy, and where memory-tree does not resolve, the legacy shape
  with its one stderr line. An id the grammar refuses adds no slug. Observed by AC1.
- **S2** — `render_spec_skeleton` in `tools/memory-tree/gen_build_index.py` writes the node as the first
  character of `parse_id_parts(spec_id, root)`'s slug. Observed by AC2.
- **S3** — `scan_records` in `tools/memory-tree/row_grammar.py` keys a row's `slug` from
  `parse_id_parts`, and a row id the grammar refuses keeps `""`. Observed by AC3.
- **S4** — The site assertion. The pass records, in its commit's `Decided:` trailer, the thirteen
  split sites of unit 38's §1 and this unit's §1 by file and line at base. Observed by AC4.

## 3. Non-goals (OUT)

- The ten readers of unit 38's table: `TOOL-dTotalRecall-38`'s.
- The census predicate: `TOOL-dTotalRecall-44`'s.
- The family readers `tools/memory-tree/gen_build_index.py:3793` and `tools/memory-tree/backlog.py:1683`.
  Each takes index 0, which a hyphen in the slug cannot move, so each stays as it is.
- `branch_reconcile.py`'s own `ID_RE`, whose slug class admits no hyphen: unit 5's re-point owns it.

### Edges

- **consumes-from** `TOOL-dTotalRecall-38` — `parse_id_parts` in `id_grammar.py` and the re-point routes
  its §4 table uses, which the three readers here take
- **hands-off** `TOOL-dTotalRecall-53` — the three further re-pointed readers, which that unit holds to their base answers for the flat and node-scoped eras (ids 2 and 23)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts`, landed at step 8; without it the three readers of §4 raise `IndexError` at this pass (the round-1 audit of units 44 to 53, id 2)
- **hands-off** `TOOL-dTotalRecall-60` — `render_spec_skeleton`'s re-point and AC2, whose signature, refusal, fixture and flipped command that unit settles (the round-1 audit of units 44 to 53, ids 2, 10, 16, 17, 29 and 42)

## 4. Design

### The three readers

| Site | Today | After |
|---|---|---|
| `branch_reconcile.py:520` | `{i.split("-")[1] for i in list(names)}` | the slug of `parse_id_parts(i, root)`, skipped on `ValueError` |
| `gen_build_index.py:8576` | `spec_id.split('-')[1][0]` | `parse_id_parts(spec_id, root)[1][0]` |
| `row_grammar.py:1116` | `rid.split("-")[1]` | `parse_id_parts(rid, root)[1]`, `""` on `ValueError` |

`derive_names` takes a commit subject and no root today; it gains the repository root the module
already resolves for its conf read (`branch_reconcile.py:415-418`), so its callers pass one more value.

### Inventory

Minted: none.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/row_grammar.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Keep the splits and assert only by grep.** The grep is the assertion; the readers still answer
  `d2026` under the flip until they parse through the grammar.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one cached regex per root.
- error / empty / loading states — an id the grammar refuses yields no slug or `""`, as each caller
  answers a malformed id today.
- observability — none new.
- risks — `derive_names` gains a parameter; every caller is in its own module and is changed with it.
- testing — AC1 to AC4 by the pass; the arm of §7 at the close.
- migration — none: the default grammar gives the same slug for every unhyphenated id.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe calls `derive_names` from `branch_reconcile.py` with the subject
  `TOOL-d2026-10-26ClosedLoop-3 fix` in the flipped clone `TOOL-dTotalRecall-5` §4 "The flips" makes,
  the slug `d2026-10-26ClosedLoop` is in its answer.
  Red when: the answer holds `d2026`.
  fixture: the flipped scratch clone; the pass makes it under the run's scratch directory.
- **AC2** — When `python gen_build_index.py --new-spec TOOL-d2026-10-26ClosedLoop-3` runs in the same
  clone, the written header reads `node d`, as it does at base.
  Red when: the re-point moves the node, or reads it from anything but the parsed slug.
- **AC3** — When a `python -c` probe runs `scan_records` from `row_grammar.py` over the clone holding
  one row `TOOL-d2026-10-26ClosedLoop-3`, that row's `slug` is `d2026-10-26ClosedLoop`.
  Red when: the slug is `d2026`.
- **AC4** — When `git grep -nE "\.split\(['\"]-['\"]\)" -- tools` runs at the pass tip, its output
  holds none of the thirteen sites S4 records, each matched by file and by the line's text.
  Red when: any one of them still splits, in either quote style.

## 7. Gates

`branch-reconcile selftest` · `build-index selftest` · `row-grammar selftest` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `memory hygiene` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/row_grammar.py · covers AC3 · a hyphenated-slug row in the row-grammar selftest, staged by restoring the split · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-5`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 35
  (HIGH, item H1 shared with id 1).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-54, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `parse_id_parts` in `tools/memory-tree/id_grammar.py` (`TOOL-dTotalRecall-38` S1),
each reader reaching it by the route `TOOL-dTotalRecall-5` §4 "The readers" gives its kit; no second
parser is written. `python tools/codebase-map/reuse_lookup.py "take the slug out of a unit id"` ranked
name-stem neighbours (`parse`, `slug`) and no id parser at base, which is the parser unit 38 mints.

Recall terms used: `python tools/memory-recall/query.py "which readers split a unit id on a hyphen and break under a hyphenated slug" --terms "split hyphen slug reader census id_grammar readers flip-probe parse_id_parts kept predicate"`
