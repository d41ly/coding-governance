# TOOL-dTotalRecall-39 — one record-header edge reader: the edge grammar's header site calls `tree_lib.read_header_edges` and defines none of its own

**Status:** DEFERRED · rev-3 · 2026-11-22 · node d · Tier-2 · base 462d20f3 · streams tooling · order 17 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-build-TOOL-dTotalRecall-39-deviation-391.md](../build/2026-10-26-build-TOOL-dTotalRecall-39-deviation-391.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-39-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-39-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-prompt-TOOL-dTotalRecall-39-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-39-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-39-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-39-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 23 at HIGH**, its item **H4**, alone in that item. PLAY-dOrderedCharter-28 S5 landed
a header adapter, `tools/playbook/edge_grammar.py#read_header_edges`, reading the column-0
`**Caused-by:**` and `**Made-by:**` lines through `edge_grammar.py#HEADER_RE` only. `TOOL-dTotalRecall-19`
S1 mints a second `read_header_edges(text, path, binding=None)` in `tools/memory-tree/tree_lib.py`, with
that adapter's signature and return, which also reads a typed record's bulleted `- **Caused-by:**` field.
2,761 tracked files under `memory/` carry that field (DERIVED 2026-11-22 at `ed5a7d523`, `git grep -l -E
'^- \*\*Caused-by:\*\*' -- memory | wc -l`), and the landed adapter reads none of them. Two functions of
one name would read different cause edges from one record, so `edge_grammar.py --check`,
`TOOL-dTotalRecall-22`'s cardinality count and `record_causes.py --check` would disagree. This unit makes
`tree_lib.read_header_edges` the one reader: the edge grammar's header site calls it and defines no
reader of its own. It repairs `TOOL-dTotalRecall-19`.

## 2. Scope (IN)

Preconditions this unit calls and does not build: `tree_lib.read_header_edges` and
`tools/memory-tree/record_causes.py` with its `--fixture --plant <case>` (`TOOL-dTotalRecall-19` S1, S8,
S12), and the route `gen_build_index.py#load_edge_grammar` by which that script reaches the playbook kit.

- **S1** — `tools/playbook/edge_grammar.py` loses `read_header_edges` and `HEADER_RE`, its only reader,
  and gains the site adapter `check_header_edges(text, path, binding=None)`. It calls
  `tree_lib.read_header_edges` on the module `tag_index.py#load_memory_tree` returns at call time, the
  route every other memory-tree read of the module takes, and returns
  `edge_grammar.py#check_site_targets` over its edges, so a header target still answers to the one target
  grammar. Its two callers, `edge_grammar.py#read_tree_edges` (the walk `--check` and `--cardinality`
  read) and `edge_grammar.py#read_site_edges` (`--parse`), call it in the adapter's place. Observed by AC1
  and AC4.
- **S2** — The one reader's contract is `TOOL-dTotalRecall-19` S1's: the column-0 bare form within
  `tree_lib.py#BIND_HEAD_LINES` for an untyped record, and the factory's `- **Key:**` form for a record a
  typed kind's grammar names. Both the causes check and the edge walk read a typed record's bulleted
  `- **Caused-by:** X` as the edge `caused-by` to `X`. Observed by AC2.
- **S3** — The reader's `ValueError` on a second line of one key is re-raised by `check_header_edges` as
  an `edge_grammar.py#EdgeRefusal` whose second line carries the reader's message, the shape
  `read_tree_edges` collects per record and `edge_grammar.py#run_parse` prints, so the walk goes on past
  the record and reads no edge of that key from it. Observed by AC3.
- **S4** — The `caused-by` row of `tools/playbook/edges.toml` moves from `pin = "none"` to
  `pin = "clause"` (§8 F4), so a cause pinned to a clause revision is legal and resolves by
  `design_lib.py#derive_clause_hash`. Observed by AC5.
- **S5** — The docs follow: the module docstring's sites paragraph and `tools/playbook/README.md` name
  `check_header_edges` over `tree_lib.read_header_edges` and admit a pinned clause id on `caused-by`;
  `help/tags.md` gives `caused-by` pin `clause` in its type table and its pinned-forms paragraph, and
  names a typed record's `- **Caused-by:**` field under "Where edges are read". Observed by AC5 for the
  help row; the prose is NOT OBSERVED by a criterion and is read by the diff review.
- **S6** — The departure. This unit retires PLAY-dOrderedCharter-28 S5's landed adapter and departs from
  its Inventory; the build run records it as a deviation of this unit by the README's departures rule.
  NOT OBSERVED by a criterion: the deviation record is graded by the departures report at the close.

## 3. Non-goals (OUT)

- The header grammar, the reader's refusal and the causes check: `TOOL-dTotalRecall-19`'s.
- The edge grammar's other site adapters, its parser and its check: PLAY-dOrderedCharter-28's.
- Printing a refused header line from `--cardinality`, which counts it today: `TOOL-dTotalRecall-53` S12.
- Rewriting a landed record: none is rewritten; S4 admits the three pinned causes of §4 as written.
- A gate refusing any function name defined in two kits. Inline copies of `tools/lib/` blocks are
  sanctioned duplicates, so such a gate needs a parity-row exemption this build does not own; this
  unit closes the instance and its AC1 check holds it.

### Edges

- **consumes-from** `TOOL-dTotalRecall-19` — `tree_lib.read_header_edges`, the one header reader the
  edge grammar's header site binds
- **consumes-from** `TOOL-dTotalRecall-22` — `edge_grammar.py --cardinality`, whose count reads the
  walk AC3 observes over a record carrying two bulleted causes
- **hands-off** external — the deviation from PLAY-dOrderedCharter-28 S5 and its Inventory, recorded
  by the build run under the README's departures rule
- **hands-off** `TOOL-dTotalRecall-53` — the edge grammar's header binding, which that unit observes or asks for and whose refusal it collects (the round-1 audit of units 36 to 43, ids 6, 18, 38 and 45)

## 4. Design

### The site adapter

```python
# tools/playbook/edge_grammar.py, replacing read_header_edges and HEADER_RE
def check_header_edges(text, path, binding=None) -> list[dict]:
    """A record header's edges, read by memory-tree's one reader and graded by the one target grammar."""
    tree_lib, _ = ti.load_memory_tree()
    try:
        edges = tree_lib.read_header_edges(text, path, binding)
    except ValueError as exc:
        raise EdgeRefusal(f"edges: {path}: 1 header line(s) refused:\n  {exc}") from None
    return check_site_targets(edges, path)
```

The module holds no name `read_header_edges`, so nothing can call a stale copy, and the attribute is
looked up per call, so a probe that wraps `tree_lib.read_header_edges` (`TOOL-dTotalRecall-53` AC17)
wraps the function the walk reaches. `EdgeRefusal` subclasses `ValueError`, and `check_site_targets`
raises it outside the `try`, so its message is never wrapped twice. `read_tree_edges` keeps each refusal
line after the first (`str(exc).splitlines()[1:]`), which is why the reader's message sits on line two.

### What the walk newly reads

The landed adapter reads no bulleted field, so after S1 the edge walk reads typed records' causes it
never read, 2,742 of them (DERIVED 2026-11-22 at `ed5a7d523`: the `git grep -n -E '^- \*\*Caused-by:\*\*' -- memory`
lines whose file name ends `-<kind>-<n>.md` for a kind of `tree_lib.py#TYPED_RECORD_KINDS`). Graded by
`edge_grammar.py#check_edges` and resolved by `#run_resolve` against that HEAD, three are red and none is
unresolved (DERIVED 2026-11-22, the same probe): the deviation records of TOOL-dFurnishedOrders-19 and
of DEPL-dShippedRelease-12 and -21, each caused by a clause id pinned to its revision, the first
`cl-dClosedLoop-0210@c44de500`, which `caused-by`'s `pin = "none"` refuses. Under `pin = "clause"` the
same probe grades all three green and resolves them. No typed record carries two bulleted causes, and
no untyped one two column-0 cause lines outside a fence (DERIVED 2026-11-22, `git grep -c` of each form
over `memory`), so S3's refusal reds no landed record.

### Why tree_lib holds it

The records live in the memory tree; `tree_lib.py#read_bindings`, `#BIND_RE` and `#BIND_HEAD_LINES`,
which the landed adapter already reads, are there; and the typed factory's field grammar is
`build_records.py#FIELD`, a memory-tree constant. The memory-tree kit reading its own records through
the playbook kit is the boundary the batch's id 11 settles the other way (§8 F2).

### Inventory

Minted: `check_header_edges` in `edge_grammar.py`, asked of the lexicon's `--suggest` under
`--as py.function` (it leads with `check`, a declared verb); the plants `bulleted-cause` and
`bulleted-twice` of `record_causes.py --fixture`. Retired: `edge_grammar.py#read_header_edges` and
`#HEADER_RE`.

### Files touched (estimate)

- `tools/playbook/edge_grammar.py`
- `tools/playbook/edges.toml` (the `caused-by` row's `pin`)
- `tools/playbook/README.md`
- `help/tags.md`
- `tools/memory-tree/record_causes.py` (the two plants)
- `tools/memory-tree/check-memory-hygiene.test.sh` (the arm of §7)

### Alternatives rejected

- **Bind `read_header_edges = tree_lib.read_header_edges` at import.** It loads memory-tree when the
  module loads, and a wrap of the reader after import misses the alias (§8 F3).
- **Extend the landed adapter to admit `- ` and keep both functions.** Two definitions of one rule still
  drift on the next change, which is the finding.
- **Make `edge_grammar.py` the one reader and re-point `record_causes.py` to it.** The memory-tree kit
  would then import the playbook kit for its own records (§8 F2).

## 5. Production-readiness checklist

- security — no new surface; S4 admits one more target form on one row, graded and resolved as
  `carries-clause`'s is.
- perf / scale — one reader where two were; the edge walk reads and resolves the typed causes of §4
  once per run.
- error / empty / loading states — the reader's refusal of a second line of one key is
  `TOOL-dTotalRecall-19` S1's, collected per record at the walk (S3) and printed by `--parse`.
- observability — unchanged: a refusal is an `edges: refused` line of `--check`.
- risks — the playbook-render kit `requires` memory-tree (`tools/playbook/kit.toml`), and an absent one
  is the `TagError` `tag_index.py#load_memory_tree` raises today, on which `edge_grammar.py#main` exits 2.
- testing — AC1 to AC5 by the pass; the arm of §7 at the close.
- migration — none: no record is rewritten.
- user docs — `help/tags.md` (S5).

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe puts `tools/playbook/` on `sys.path`, imports `edge_grammar`,
  replaces `tree_lib.read_header_edges` with a counting wrapper and calls
  `edge_grammar.check_header_edges("**Caused-by:** TOOL-tFix-1\n", "x.md")`, it prints
  `hasattr(edge_grammar, "read_header_edges")` and `hasattr(edge_grammar, "HEADER_RE")` as `False`
  and the wrapper's count as `1`; `git grep -n "def read_header_edges" -- tools` prints one line, in
  `tools/memory-tree/tree_lib.py`.
  Red when: `edge_grammar.py` keeps its own reader, or binds the reader at import.
- **AC2** — When `python record_causes.py --fixture --plant bulleted-cause` runs from
  `tools/memory-tree/`, its scratch repository holds one typed deviation record whose only cause is
  `- **Caused-by:** TOOL-tFix-1`; the plant runs `check_causes` and the edge grammar's `read_tree_edges`
  over that root, prints `0 causeless` and the record's `caused-by` edge to `TOOL-tFix-1`, and exits 0.
  Red when: either check reads the bulleted line as absent.
  fixture: the scratch repository `record_causes.py --fixture` builds under the system temp directory.
- **AC3** — When the plant `bulleted-twice` writes a typed record carrying two `- **Caused-by:**`
  fields, `read_tree_edges` over its root returns no `caused-by` edge of that record and one refusal
  naming it and both lines, and the plant exits 0. `run_check` and `check_edge_cardinality` take their
  edges and refusals from that walk.
  Red when: the `ValueError` escapes the walk, the refusal list is empty, or the record reads as edges.
  fixture: the scratch repository of AC2's plant table.
- **AC4** — When `python tools/playbook/edge_grammar.py --parse <file>` reads a scratch file named
  `2026-11-22-build-TOOL-tFix-1-deviation-1.md` whose field is `- **Caused-by:** a,b`, it exits 1 naming
  `caused-by` and `'a,b'` as matching no address form; over one named `bare.md` carrying
  `**Caused-by:** TOOL-tFix-1` it exits 0 and prints its `caused-by · TOOL-tFix-1` row.
  Red when: the target grammar leaves the header site with the landed adapter.
  fixture: two scratch files under `%TEMP%`, written by the pass.
- **AC5** — When `python tools/playbook/edge_grammar.py --parse` reads
  `memory/builds/dFurnishedOrders/build/2026-10-26-build-TOOL-dFurnishedOrders-19-deviation-191.md`,
  it prints its `caused-by · cl-dClosedLoop-0210@c44de500` row and no `pins a target` line, and exits 0;
  `--list` prints `caused-by` with `pin clause`, and `grep -n '^| .caused-by.' help/tags.md` prints a
  row ending `| clause |`.
  Red when: the row keeps `pin = "none"`, so the three pinned causes of §4 red the edge check.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 · the plants `bulleted-cause` and `bulleted-twice` read by both checks, staged by the landed header adapter reading the column-0 form only · none

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
- **F3 — The landed adapter graded its targets and raised `EdgeRefusal`; the tree_lib reader can do
  neither. How does the header site bind it?** Options: (a) a site adapter `check_header_edges` reaching
  the reader per call, mapping its `ValueError` and grading targets; (b) a module-level alias bound at
  import, each caller wrapping it; (c) the alias alone. (c) drops the target grading AC4 observes and
  lets the reader's `ValueError` abort the walk, which `read_tree_edges` catches only as `EdgeRefusal`;
  (b) loads memory-tree at import and hides a wrapped reader from `TOOL-dTotalRecall-53` AC17.
  RESOLVED (agent, 2026-11-22, delegated): (a), the most feature-rich survivor, meeting AC1 to AC4 and
  reusing the call-time route `tag_index.py#load_memory_tree`. widens: none · relaxes: none
- **F4 — The bound reader reads three landed deviation records' clause-pinned causes, which
  `caused-by`'s `pin = "none"` reds. Which gives?** Options: (a) the row's `pin` becomes `clause`;
  (b) rewrite the three records' causes unpinned; (c) a waiver for the three. (b) rewrites landed
  records, which §3 and `TOOL-dTotalRecall-19` §3 refuse, and drops the revision the cause names; (c)
  is a mechanism this unit does not otherwise need. RESOLVED (agent, 2026-11-22, delegated): (a), the
  option meeting AC5 with no new mechanism, grading the pin as `carries-clause`'s is.
  widens: none · relaxes: caused-by's pin, from none to clause

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 23 (HIGH, item H4).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.
- rev-3 · 2026-11-22 · §1 · §2 S1 to S6 · §3 · §4 · §5 · §6 AC1 to AC5 · §7 · §8 F3, F4 added · §10 · per
  `2026-11-22-prompt-TOOL-dTotalRecall-39-reground-brief`: the re-ground on HEAD `ed5a7d523`. The
  landed adapter `edge_grammar.py#read_header_edges` is retired for a site adapter `check_header_edges`
  calling unit 19's reader per call, keeping its target grading and mapping its refusal per record; the
  `caused-by` row admits a clause pin, for the three landed pinned causes the binding newly reads; the
  arm moves to `check-memory-hygiene.test.sh`, unit 19's; the leg line gains `policy fixtures`.

## 10. Reuse audit

The seam is `TOOL-dTotalRecall-19`'s `tree_lib.read_header_edges`, extended to a second caller and
reached by `tools/playbook/tag_index.py#load_memory_tree`, the route the landed adapter already takes to
`tree_lib.py#read_bindings`, `#BIND_RE` and `#unfenced_lines`. The landed `edge_grammar.py#check_site_targets`
and `#EdgeRefusal` keep the site's grading and refusal, and `record_causes.py --fixture`'s plant table
takes the two plants. `git grep -n "read_header_edges" -- tools` at `ed5a7d523` prints the landed
definition, its two callers in `edge_grammar.py` and one `tools/playbook/README.md` line, so nothing
outside the playbook kit calls it. `python tools/codebase-map/reuse_lookup.py "read a record header
Caused-by edge typed field"` ranked name-stem neighbours (`read_text`, `read`, `records`) and no header
reader.

Recall terms used: `python tools/codebase-map/reuse_lookup.py "read a record header Caused-by edge typed field"`;
`python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
