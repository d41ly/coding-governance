# TOOL-dLinkedLibrary-100 — the census's decode walk classifies every helper it calls from another module

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 38 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-100-deviation-1001.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-100-deviation-1001.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 92 to 96
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md`) confirmed
finding **id 27 at HIGH**, report item **H4**. No other id shares the item.

`TOOL-dLinkedLibrary-96` S6 walks 96 S5's readers "and every function they call inside
`adopt_program.py`", and counts a decode only by its spelling. `read_blobs_at`
(`tools/memory-tree/tree_lib.py:328`), which 96 S8 makes the kit's blob reader, decodes strict UTF-8, folds
CR LF and keeps U+FEFF unless called with `raw`, and returns None for a blob that is not UTF-8. A reader
that calls it without `raw` decodes in `tree_lib`, where the walk never looks: AC6 prints "no decode
outside ci_lines" over it, while that reader keeps the BOM that hides a first-line `include:` and drops the
jobs of an `FF` file.

This unit makes the walk treat a call into any other module as what that module's helper does: every
name the walked functions call that `adopt_program.py` imports from outside the standard library must be
classified, `read_blobs_at` without `raw=True` and `read_text` are decodes, and an unclassified helper is
named, deny by default. It repairs `TOOL-dLinkedLibrary-96` and builds one step after it (order 38).

## 2. Scope (IN)

- **S1** — The helper table. `tools/memory-tree/adopt_program.py` holds one table, `IMPORTED_HELPER_KINDS`,
  mapping each name it imports from a module outside the standard library to one kind: `decodes`, a
  helper that turns bytes into text; `bytes`, one that returns bytes undecoded; or `text-only`, one that
  takes text and reads no bytes. `read_text` (`tree_lib.py:383`) is `decodes`; `read_git_output`
  (`tree_lib.py:278`) is `bytes`; `read_blobs_at` is `decodes`, and `bytes` only at a call passing
  `raw=True` as a constant. Observed by AC1 and AC2.
- **S2** — The walk reads the table. Inside 96 S6's walked functions, a call whose target resolves,
  through `adopt_program.py`'s import statements, to a name bound from a module outside the standard
  library is a decode when its kind is `decodes`, and is named `unclassified <name>` when the table holds
  no row for it, whether called by its bare name or as `<module>.<name>`. Both make the structural check
  exit non-zero naming the walked function that makes the call. Observed by AC1 to AC3.
- **S3** — The plants. The structural check 96 AC6 runs holds four planted readers, each a source text
  defining a function named as 96 S5's GitLab reader, walked under `adopt_program.py`'s own imports and
  never a `def` of the module: one calling `read_blobs_at` without `raw`, one calling it with `raw=False`,
  and one calling `read_text`, each named by the walk; and a fourth whose source adds its own `from
  tree_lib import unfenced` line and calls `unfenced`, a name absent from the table, named
  `unclassified`. Observed by AC1.
- **S4** — The record. 96's acceptance ledger carries an amendment line citing this unit, naming the
  table and its kinds as the walk's reach outside `adopt_program.py`. Observed by AC4.

## 3. Non-goals (OUT)

- The standard-library spellings: id 9, `TOOL-dLinkedLibrary-97`'s decode table.
- Walking into another module's source: the table states each helper's kind once, and a helper's own
  behaviour is its own module's to keep.
- A bug-class checklist entry that a walk bounded to one module lists the decoding helpers of the others:
  the report's left-shift, a separate record this unit does not write.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-96` — S6's walk, S8's `raw` keyword and AC6's structural check, which S1 to S3 extend to every helper the walked readers import (id 27)

## 4. Design

### Evidence

- `tools/memory-tree/tree_lib.py:328-367` is `read_blobs_at`: at `:364` it decodes `utf-8`, keeping a
  leading U+FEFF, folds `\r\n`, and at `:365-366` stores None on `UnicodeDecodeError`.
- `tree_lib.py:383-387` is `read_text`, which opens a path in binary, decodes `utf-8` and folds `\r\n`.
- `tree_lib.py:278-299` is `read_git_output`, which returns `done.stdout` as bytes.
- 96 S6 (`2026-10-27-spec-TOOL-dLinkedLibrary-96.md`, S6) bounds the walk to `adopt_program.py` and
  lists no call into another module; 96 S8 seats `ci_lines` on `read_blobs_at` with `raw`.
- `tools/memory-tree/adopt_program.py` is absent at base, so its imports are the builder's; S2's deny
  by default is what keeps the table complete.

### Rollout

Order 38, one step after `TOOL-dLinkedLibrary-96`. This unit and `TOOL-dLinkedLibrary-97` both write the
walk in `adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences those passes. If the pass adds a
function, it re-renders the generated map with `python tools/codebase-map/gen_map.py --write` where its
`--check` exits 1, then runs `python tools/lexicon/lexicon.py`, in the pass commit; a function it adds is
named after `python3 tools/lexicon/lexicon.py --suggest <name>`.

### Inventory

S1 mints the module constant `IMPORTED_HELPER_KINDS` and its three kind values `decodes`, `bytes` and
`text-only`.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S3
- `memory/builds/dLinkedLibrary/build/`: S4's amendment line
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **Adding `read_blobs_at` and `read_text` to the spelling list.** It fixes two instances and leaves the
  next imported decoder unseen; S2's unclassified name closes the class.
- **Following each call into `tree_lib.py`'s source.** The walk would need a second module's import graph
  and would still miss a helper reached through a variable; one stated kind per helper is checkable.

## 5. Production-readiness checklist

- security — closes a reader decoding through a shared helper, which keeps a BOM or drops a non-UTF-8
  file's jobs while the walk reads clean; deny by default on an unclassified helper.
- perf / scale — one table lookup per call in the walked functions.
- error / empty / loading states — an unclassified helper exits non-zero naming it and its caller.
- observability — the walk names the helper, its kind and the calling reader.
- risks — a helper whose kind is misstated passes; the table is one reviewed constant beside the walk.
- testing — AC1 to AC4 by the fixture, a scratch copy and a ledger grep.
- migration — none: the walk runs at fixture time.
- user docs — none under `help/`: the fixture is a developer surface.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs its structural check, it
  names each of S3's first three planted readers as a decode and the fourth as `unclassified unfenced`,
  and over the real module prints no decode outside `ci_lines` and no unclassified name.
  Red when: a `read_blobs_at` call without `raw=True` or a `read_text` call passes the walk.
- **AC2** — When a scratch copy of `adopt_program.py` whose GitLab reader takes its text from
  `read_blobs_at` without `raw` runs the same check by `python -I`, it exits non-zero naming that reader.
  Red when: the walk prints no decode over a reader decoding in `tree_lib`.
- **AC3** — When a scratch copy that imports a new helper from `tree_lib` and calls it inside a walked
  reader, with no row in `IMPORTED_HELPER_KINDS`, runs the check, it exits non-zero printing
  `unclassified` and the helper's name.
  Red when: an imported helper the table does not classify passes as no decode.
- **AC4** — When `grep 'TOOL-dLinkedLibrary-100'` runs over 96's acceptance ledger, it prints the line
  naming `IMPORTED_HELPER_KINDS` as the walk's reach outside `adopt_program.py`.
  Red when: 96's ledger certifies a walk bounded to one module.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 · the structural check's three `tree_lib` decoding plants and its unclassified-helper plant, the failing case staged by a reader calling `read_blobs_at` without `raw` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 92 to 96, id 27 (HIGH, item
  H4).

## 10. Reuse audit

The seam extended is 96 S6's walk in `tools/memory-tree/adopt_program.py`, with `tree_lib.py`'s own
helpers classified rather than re-implemented. `python tools/codebase-map/reuse_lookup.py "classify an
imported helper as a decoding reader"` ranked `read`, `read_text`, `read_conf` and `read_journal`; each is
a reader, none a classifier of readers, so no existing seam fits beyond the walk being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census walk prove no decode outside ci_lines" --terms "census ci_lines decode walk read_blobs_at raw tree_lib helper imported deny-by-default structural"`
