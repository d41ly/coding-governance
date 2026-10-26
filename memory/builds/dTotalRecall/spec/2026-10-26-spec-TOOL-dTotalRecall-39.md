# TOOL-dTotalRecall-39 — one record-header edge reader: the edge grammar's header site binds `tree_lib.read_header_edges` and defines none of its own

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 17 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 23 at HIGH**, its item **H4**, alone in that item. `TOOL-dTotalRecall-19` S1
mints `read_header_edges(path, text)` in `tools/memory-tree/tree_lib.py`, reading the bare
`**Caused-by:**` form and the bulleted `- **Caused-by:**` form 666 landed records carry.
PLAY-dOrderedCharter-28 S5 already specs a header-site adapter in `tools/playbook/edge_grammar.py`, and
its Inventory names that adapter `read_header_edges` too
(`memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md:59-63`, `:173`), reading
the bare form only. Two functions of one name would read different cause edges from one record, so
`edge_grammar.py --check`, `TOOL-dTotalRecall-22`'s cardinality count and `record_causes.py --check`
would disagree. This unit makes `tree_lib.read_header_edges` the one reader: the edge grammar's header
site binds it by import and defines no function of that name. It repairs `TOOL-dTotalRecall-19`.

## 2. Scope (IN)

- **S1** — The header site of `tools/playbook/edge_grammar.py` binds `read_header_edges` from
  `tree_lib`, reached by the route PLAY-dOrderedCharter-28 S5's header site already takes to
  `tree_lib.read_bindings` (`tools/memory-tree/tree_lib.py:471`), and the module defines no function
  of that name. Every caller of the header site in `edge_grammar.py`, the `--check` walk and
  `TOOL-dTotalRecall-22`'s `check_edge_cardinality` among them, keeps calling the same name.
  Observed by AC1.
- **S2** — The one reader's contract is `TOOL-dTotalRecall-19` S1's: the column-0 bare form within
  `BIND_HEAD_LINES` for an untyped record, and the factory's `- **Key:**` form for a typed one, each
  returned as the same `(type, target)` edge. Both the edge check and the causes check read a
  bulleted `- **Caused-by:** X` as the edge `caused-by=X`. Observed by AC2.
- **S3** — The departure. This unit departs from PLAY-dOrderedCharter-28 S5 and its Inventory, which
  mint the adapter inside `edge_grammar.py`; the build run records it as a deviation of this unit by the
  README's departures rule. NOT OBSERVED by a criterion: the deviation record is graded by the
  departures report at the close.

## 3. Non-goals (OUT)

- The header grammar, the cause refusal and the causes check: `TOOL-dTotalRecall-19`'s.
- The edge grammar's other site adapters, its parser and its check: PLAY-dOrderedCharter-28's.
- A gate refusing any function name defined in two kits. Inline copies of `tools/lib/` blocks are
  sanctioned duplicates, so such a gate needs a parity-row exemption this build does not own; this
  unit closes the instance and its AC1 identity check holds it.

### Edges

- **consumes-from** `TOOL-dTotalRecall-19` — `tree_lib.read_header_edges`, the one header reader the
  edge grammar's header site binds
- **consumes-from** `TOOL-dTotalRecall-22` — `edge_grammar.py --cardinality`, the count AC3 runs over
  a bulleted cause to observe that it reads the same edge
- **hands-off** external — the deviation from PLAY-dOrderedCharter-28 S5 and its Inventory, recorded
  by the build run under the README's departures rule
- **hands-off** `TOOL-dTotalRecall-53` — the edge grammar's header binding, which that unit observes or asks for and whose refusal it collects (the round-1 audit of units 36 to 43, ids 6, 18, 38 and 45)

## 4. Design

### The binding

```python
# tools/playbook/edge_grammar.py, the header site
tree_lib = load_sibling("memory-tree", "tree_lib.py")   # the route 28 S5 takes to read_bindings
read_header_edges = tree_lib.read_header_edges           # one definition, in tree_lib.py
```

`load_sibling` stands for whatever route the landed `edge_grammar.py` uses to reach `tree_lib`; if it
reaches it by a direct import, the binding is that import. The pass re-grounds on the landed module and
bumps this spec's rev first where its spelling differs.

### Why tree_lib holds it

The records live in the memory tree, the binding reader `read_bindings` and the `BIND_HEAD_LINES`
window are in `tree_lib.py` already, and the typed factory's field grammar `deviation_join.FIELD`
(`tools/memory-tree/deviation_join.py:145`) is a memory-tree constant. The edge grammar reads records
through memory-tree's code at every other header field, so the cause and maker fields follow.

### Inventory

Minted: nothing; one binding in `edge_grammar.py`.

### Files touched (estimate)

- `tools/playbook/edge_grammar.py`
- `tools/memory-tree/record_causes.py` (its fixture gains the `bulleted-cause` plant)

### Alternatives rejected

- **Extend PLAY-dOrderedCharter-28's adapter to admit `- ` and keep both functions.** Two definitions
  of one rule still drift on the next change, which is the finding.
- **Make `edge_grammar.py` the one reader and re-point `record_causes.py` to it.** The memory-tree kit
  would then import the playbook kit for its own records, the boundary the batch's id 11 settles the
  other way.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — unchanged: one reader where two were.
- error / empty / loading states — the reader's refusal of a second line of one key is
  `TOOL-dTotalRecall-19` S1's, now raised at both sites.
- observability — unchanged.
- risks — the playbook kit installed without memory-tree; the header site already depends on
  `tree_lib.read_bindings`, so the route's absence is refused as it is today.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `edge_grammar` from `tools/playbook/` and `tree_lib` from
  `tools/memory-tree/`, `edge_grammar.read_header_edges is tree_lib.read_header_edges` prints `True`,
  and `git grep -n "def read_header_edges" -- tools` prints one line, in `tree_lib.py`.
  Red when: `edge_grammar.py` keeps its own definition.
- **AC2** — When `python record_causes.py --fixture --plant bulleted-cause` builds a
  fixture record carrying `- **Caused-by:** TOOL-tFix-1`, `record_causes.py --check` over it names no
  causeless record, and `python edge_grammar.py --check` over the same fixture names no
  finding and lists the edge `caused-by=TOOL-tFix-1`.
  Red when: either check reads the bulleted line as absent.
  fixture: the scratch repository `record_causes.py --fixture` builds under the system temp directory.
- **AC3** — When `python edge_grammar.py --cardinality` runs over the AC2 fixture with a
  second record carrying `- **Caused-by:** TOOL-tFix-1` and `**Caused-by:** TOOL-tFix-2` both, it names
  that record as over `caused-by`'s per-source bound of `1`.
  Red when: the count reads only the bare line, so the record reads as one cause.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/record_causes.py · covers AC2 · the fixture plant `bulleted-cause` read by both checks, staged by the edge grammar's header site reading the bare form only · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which module holds the one reader?** Options: (a) `tree_lib.py`, `TOOL-dTotalRecall-19`'s, the
  edge grammar binding it; (b) `edge_grammar.py`, PLAY-dOrderedCharter-28's, `record_causes.py`
  importing it. (b) has the memory-tree kit import the playbook kit to read its own records.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, tie-broken by reuse of the seam the header
  site already calls, `tree_lib.read_bindings`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 23 (HIGH, item H4).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-19`'s `tree_lib.read_header_edges`, extended to a second caller, and
the route PLAY-dOrderedCharter-28 S5 already takes from the edge grammar's header site to
`tree_lib.read_bindings` (`tools/memory-tree/tree_lib.py:471`). `git grep -n "read_header_edges"`
over the tree prints only the two specs at base, so neither definition exists yet and nothing landed
moves. `python tools/codebase-map/reuse_lookup.py "read a record header edge line Caused-by"` ranked
name-stem neighbours and no header reader.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
