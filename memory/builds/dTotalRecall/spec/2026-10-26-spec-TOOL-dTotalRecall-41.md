# TOOL-dTotalRecall-41 — the ask door refuses a line break or row separator in any value and grades the row it would write, read back

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 14 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 49 at HIGH**, its item **H6**, alone in that item. `TOOL-dTotalRecall-7` S2 has
`gov_record.py new ask` render `--text` verbatim through `render_ask_row`
(`tools/memory-tree/backlog.py:1516-1519`), which joins its parts with `SEP` (`" · "`, `:76`) and
`ARROW` (`" → "`, `:77`) and refuses nothing. The door grades the clause mapping it built from the
`--clause` arguments, not the bytes it writes, and its read-back confirms only that one ask with the
minted id exists. The skeptic re-ran `render_ask_row('EXMP-aFoo-1', '2026-02-01', 'x\n- EXMP-aFoo-2 ·
filed 2026-02-01 · injected', clauses=(('accept', 'y'),))`: it printed two rows, the accept clause on
the injected one. So `--text $'x\n- <id2> · filed …'` with `--clause accept y` passes the `refuse`
default and writes an ask with no acceptance. This unit refuses a line break or a row separator in
every value at the door's argument layer, grades the clauses parsed back from the rendered file, and
asserts the read-back added exactly one row, the minted one. It repairs `TOOL-dTotalRecall-7`.

## 2. Scope (IN)

- **S1** — One value refusal, `check_row_value(label, value)` in `tools/memory-tree/backlog.py`,
  raising `ValueError` naming the label when the value holds a CR, an LF, `SEP` or `ARROW`. The ask
  handler of `tools/memory-tree/gov_record.py` calls it on `--text`, on each `--clause` value and on
  `--pointer` before it mints, so a refused filing mints nothing; the door exits 2 naming the
  argument and writes nothing. Observed by AC1 and AC2.
- **S2** — The grade reads the row the door would write. After rendering, the handler builds the
  would-be `BACKLOG.md` text in memory, parses it with `backlog.parse_file` (`:555`), takes the merged
  clauses of the minted id through `derive_clauses` (`:883`), and grades those with
  `check_ask_acceptable` (`TOOL-dTotalRecall-7` S1). The argument mapping is never graded. Observed by
  AC3.
- **S3** — The read-back counts. The handler compares the asks `parse_file` reads from the would-be
  text against those it reads from the file before the write: exactly one ask is added and its id is
  the minted id, or the door exits 2 naming what it found and writes nothing. After the write it
  parses the file on disk again and asserts the same. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- The acceptance predicate, `asks.acceptance` and the ask row's registry entry: `TOOL-dTotalRecall-7`'s.
- The door's `--field`, `--title`, `--caused-by` and `--edge` values for other kinds: the round-1
  audit's id 50, a MEDIUM, disposed in `TOOL-dTotalRecall-43`.
- The shell ask writer `write_ask_rows` (`tools/unattended/unattended.sh:9980`): it writes rows the
  driver composes itself, and no agent value reaches it unrefused.

### Edges

- **consumes-from** `TOOL-dTotalRecall-7` — the ask handler of `gov_record.py new ask` and its grade
  through `check_ask_acceptable`, which this unit moves onto the parsed row
- **hands-off** `TOOL-dTotalRecall-43` — `check_row_value`, whose line-break half that unit extracts
  into `check_line_break` for the door's other values (the round-1 audit's id 50)
- **hands-off** `TOOL-dTotalRecall-53` — the ask door's write, which that unit makes a compare-and-swap (the round-1 audit of units 36 to 43, id 47)

## 4. Design

### The handler's order, after this unit

1. Parse the arguments; refuse an unknown clause label (`TOOL-dTotalRecall-7` S2).
2. `check_row_value` on every value (S1). Exit 2 on the first refusal.
3. Read `asks.acceptance`, mint the id, render the row.
4. Build the would-be file, parse it, and require one added ask, the minted one (S3).
5. Grade that ask's parsed clauses (S2), then write or refuse by the policy table of
   `TOOL-dTotalRecall-7` §4.
6. Parse the written file and require the same one added ask (S3).

### The refusal

```python
def check_row_value(label: str, value: str) -> None:
    for bad, name in (("\r", "a carriage return"), ("\n", "a line feed"), (SEP, "the row separator"),
                      (ARROW, "the pointer arrow")):
        if bad in value:
            raise ValueError(f"{label} holds {name}, which would split the row it is written into")
```

The rescope verb refuses the same two classes for its own one-line rows
(`tools/unattended/unattended.sh:13328-13331`), the shape this follows in Python.

### Inventory

Minted: `check_row_value` in `tools/memory-tree/backlog.py`. Naming cell: asked of
`python tools/lexicon/lexicon.py --suggest check_row_value --as py.function` at the pass.

### Files touched (estimate)

- `tools/memory-tree/backlog.py`
- `tools/memory-tree/gov_record.py`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Escape the separators instead of refusing them.** The row grammar has no escape, so an escaped
  value would read back as text no other reader of `BACKLOG.md` decodes.
- **Refuse inside `render_ask_row`.** It is the renderer every row writer shares, the migration's
  included, and a raise there would turn a renderer into a validator for callers that already
  validate; the door is the write boundary the charter's security rule names.

## 5. Production-readiness checklist

- security — the write boundary validates once: every agent-supplied value is refused for a line
  break or a separator before any mint or write, and the grade reads the bytes written.
- perf / scale — two parses of one `BACKLOG.md` per filing.
- error / empty / loading states — each refusal exits 2 naming the argument and leaves the file
  byte-unchanged.
- observability — the refusal names the argument and the character class.
- risks — an ask text that legitimately needs `·`; the door's message names the separator, and the
  author writes the text without it.
- testing — AC1 to AC4 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no page covers the ask door.

## 6. Acceptance criteria

- **AC1** — When `python gov_record.py new ask --build <slug> --text $'x\n- X-a-2 ·
  filed 2026-02-01 · injected' --clause accept y` runs in a scratch clone under `%TEMP%`, it exits 2
  naming `--text`, and `git status --porcelain` is empty.
  Red when: the door renders the text and two rows reach the file.
  fixture: a scratch clone carrying the door and one build folder; the pass makes it.
- **AC2** — When the same command runs with `--text 'x · accept y'` and no `--clause`, it exits 2
  naming `--text` and the row separator; with `--pointer $'a\rb'`, it exits 2 naming `--pointer`.
  Red when: the text's separator lands an accept clause the arguments never carried.
- **AC3** — When a probe drives the handler's grade over a would-be file whose rendered row for the
  minted id carries no `accept` and no `seen` clause, while the argument mapping holds `accept y`, the
  handler refuses under `asks.acceptance = "refuse"` with exit 2.
  Red when: the grade reads the argument mapping, so the refusal does not fire.
- **AC4** — When a probe makes `render_ask_row` return two rows inside the handler, the handler exits
  2 naming two added asks, and the file is byte-unchanged.
  Red when: the read-back only checks that the minted id exists.

## 7. Gates

`memory hygiene` · `build-index selftest` · `backlog migration selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/gov_record.py · covers AC1 AC2 AC3 AC4 · the ask handler's plants `text-newline`, `text-separator`, `pointer-cr`, `graded-args-not-row` and `two-rows-added`, staged by cutting the `check_row_value` calls · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-7`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 49 (HIGH, item H6).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.

## 10. Reuse audit

The seams extended are the backlog grammar's own constants and readers in
`tools/memory-tree/backlog.py`: `SEP` and `ARROW` (`:76-77`), `render_ask_row` (`:1516`), `parse_file`
(`:555`) and `derive_clauses` (`:883`), and `TOOL-dTotalRecall-7`'s ask handler and
`check_ask_acceptable`. No Python value refusal exists to extend: `grep -n newline
tools/memory-tree/backlog.py` finds only the module docstring, and `python
tools/codebase-map/reuse_lookup.py "refuse a newline or separator in a backlog row value before
writing"` ranked name-stem neighbours (`rows`, `write`, `extract_row`) and two process-monitor refusal
classes that read no row. The shell precedent is the rescope verb's field refusal
(`tools/unattended/unattended.sh:13328-13331`).

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
