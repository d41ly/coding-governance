# TOOL-dTotalRecall-41 — the ask door refuses a line break or row separator in any value and grades the row it would write, read back

**Status:** DEFERRED · rev-3 · 2026-11-22 · node d · Tier-2 · base 462d20f3 · streams tooling · order 14 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-build-TOOL-dTotalRecall-41-deviation-411.md](../build/2026-10-26-build-TOOL-dTotalRecall-41-deviation-411.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-41-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-41-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-prompt-TOOL-dTotalRecall-41-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-41-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-41-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-41-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 49 at HIGH**, its item **H6**, alone in that item. `TOOL-dTotalRecall-7` S2 has
`gov_record.py new ask` render `--text` verbatim through `backlog.py#render_ask_row`, and the `--sev`
reason through `backlog.py#render_sev_row`; both join their parts with `backlog.py#SEP` (`" · "`) and
`#ARROW` (`" → "`) and refuse nothing. The door grades the clause mapping it built from the
`--clause` arguments, not the bytes it writes, and its read-back confirms only one ask with the minted
id and one `SEV` row naming it. Re-run at `e1ae60af8`, `render_ask_row('EXMP-aFoo-1', '2026-02-01',
'x\n- EXMP-aFoo-2 · filed 2026-02-01 · injected', clauses=(('accept', 'y'),))` still prints two rows,
and `parse_file` reads the accept clause on the injected one. So `--text $'x\n- <id2> · filed …'`
with `--clause accept y` passes the `refuse` default and writes an ask with no acceptance. This unit
refuses a line break or a row separator in every value at the door's argument layer, grades the
clauses parsed back from the rendered file, and asserts the read-back added exactly the rows the door
rendered. It repairs `TOOL-dTotalRecall-7`.

## 2. Scope (IN)

Preconditions this unit calls and does not build: the ask handler `write_new_ask` of
`tools/memory-tree/gov_record.py`, its flags, its `SEV` row, its write and restoring read-back
(`TOOL-dTotalRecall-7` S2 and §4 "The door verb", unbuilt at HEAD), and the door's `refused <kind>:
<why>` exit 2 (`TOOL-dTotalRecall-2` §4 "The command", unbuilt).

- **S1** — One value refusal, `check_row_value(label, value)` in `tools/memory-tree/backlog.py`,
  raising `ValueError` naming the label when the value holds a CR, an LF, `SEP` or `ARROW`.
  `write_new_ask` calls it on `--text`, on each `--clause` value, on `--pointer` and on the `--sev`
  reason before it mints, so a refused filing mints nothing; the door exits 2 naming the argument and
  writes nothing. Observed by AC1 and AC2.
- **S2** — The grade reads the row the door would write. After rendering, the handler builds the
  would-be `BACKLOG.md` text in memory, parses it with `backlog.py#parse_file` under the conf's
  `FAMILIES` grammar, takes the minted id's clauses from `backlog.py#derive_clauses` over
  `backlog.py#build_corpus` of that one parse, and grades those with `check_ask_acceptable`
  (`TOOL-dTotalRecall-7` S1). The argument mapping is never graded. Observed by AC3.
- **S3** — The read-back counts. The handler compares the would-be parse against the parse of the file
  before the write: exactly one ask is added, the minted id, and exactly one verb row, the `SEV` row
  naming it, or the door exits 2 naming what it found and writes nothing. After the write it parses
  the file on disk again and asserts the same, a miss taking `TOOL-dTotalRecall-7`'s restore and its
  exit 2. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- The acceptance predicate, `asks.acceptance`, the `SEV` row and the ask row's registry entry:
  `TOOL-dTotalRecall-7`'s.
- The door's `--field`, `--title`, `--caused-by` and `--edge` values for other kinds: the round-1
  audit's id 50, a MEDIUM, disposed in `TOOL-dTotalRecall-43` S37.
- The shell ask writer `tools/unattended/unattended.sh#write_ask_rows`: its callers
  `#write_inherited_asks` and `#write_leg_ask` compose every row from the driver's own values, and
  `#read_ask_back` refuses a row that does not read back as one open ask.

### Edges

- **consumes-from** `TOOL-dTotalRecall-7` — the ask handler of `gov_record.py new ask` and its grade
  through `check_ask_acceptable`, which this unit moves onto the parsed row
- **hands-off** `TOOL-dTotalRecall-43` — `check_row_value`, whose line-break half that unit extracts
  into `check_line_break` for the door's other values (the round-1 audit's id 50)
- **hands-off** `TOOL-dTotalRecall-53` — the ask door's write, which that unit makes a compare-and-swap (the round-1 audit of units 36 to 43, id 47)

## 4. Design

### The handler's order, after this unit

1. Parse the arguments; refuse an unknown clause label or `--sev` level (`TOOL-dTotalRecall-7` S2).
2. `check_row_value` on every value (S1). Exit 2 on the first refusal.
3. Read `asks.acceptance`, mint the id, render the ask row and its `SEV` row.
4. Build the would-be file, the rows placed as the write places them, parse it, and require the one
   added ask and the one added `SEV` row (S3).
5. Grade that ask's parsed clauses (S2), then write or refuse by the policy table of
   `TOOL-dTotalRecall-7` §4.
6. Parse the written file and require the same (S3).

The handler calls `backlog.render_ask_row` through the module, never a `from` import, so the plant of
§7 reaches it by rebinding that one attribute. The before-parse of an absent `BACKLOG.md` holds no ask
and no row. The grammar is the one `record_kinds.py#read_open_asks` compiles from the conf's `FAMILIES`.

### The refusal

```python
def check_row_value(label: str, value: str) -> None:
    for bad, name in (("\r", "a carriage return"), ("\n", "a line feed"), (SEP, "the row separator"),
                      (ARROW, "the pointer arrow")):
        if bad in value:
            raise ValueError(f"{label} holds {name}, which would split the row it is written into")
```

The rescope verb refuses a newline and the separator for its own one-line rows
(`tools/unattended/unattended.sh#verb_rescope`), the shape this follows in Python.

### Inventory

Minted: `check_row_value` in `tools/memory-tree/backlog.py`; the `ask-door` plant's cases of §7.
Naming cell: `python tools/lexicon/lexicon.py --suggest check_row_value --as py.function` printed `OK`
on 2026-11-22.

### Files touched (estimate)

- `tools/memory-tree/backlog.py`
- `tools/memory-tree/gov_record.py`
- `tools/memory-tree/build_records.py` (the `ask-door` plant's cases)
- `tools/memory-tree/check-memory-hygiene.test.sh` (the `ask-door` hit's comment names this unit's
  criteria; its assertion count is unchanged)
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

- **AC1** — When `python gov_record.py new ask --build <slug> --text $'x\n- X-a-2 · filed 2026-02-01 ·
  injected' --sev LOW w --clause accept y` runs in a scratch clone under `%TEMP%`, it exits 2 naming
  `--text`, and `git status --porcelain` is empty.
  Red when: the door renders the text and two rows reach the file.
  fixture: the `ask-door` plant's scratch clone (`TOOL-dTotalRecall-7` §7); the pass makes it.
- **AC2** — When the same command runs with `--text 'x · accept y'` and no `--clause`, it exits 2
  naming `--text` and the row separator; with `--pointer $'a\rb'`, it exits 2 naming `--pointer`; and
  with `--text x --sev LOW $'w\n- SEV · X-a-1 · HIGH · z'`, it exits 2 naming `--sev`.
  Red when: the text's separator lands an accept clause the arguments never carried.
- **AC3** — When a child Python rebinds `backlog.render_ask_row` to drop its `clauses`, then runs
  `gov_record.py`'s main with `new ask --build <slug> --text x --sev LOW w --clause accept y` in the
  clone under the default `refuse`, it exits 2 naming `asks.acceptance`, and `git status --porcelain`
  is empty.
  Red when: the grade reads the argument mapping, so the refusal does not fire.
- **AC4** — When the child Python rebinds `backlog.render_ask_row` to return its row and a second
  ask row, and runs the AC3 command, it exits 2 naming two added asks, and the file is byte-unchanged.
  Red when: the read-back only checks that the minted id exists.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `backlog migration selftest` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `memory-recall kit selftest` · `policy fixtures` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 AC3 AC4 · the `build_records.py --fixture --plant ask-door` case gains the cases `text-newline`, `text-separator`, `pointer-cr`, `sev-newline`, `graded-args-not-row` and `two-rows-added`, under its one `build-records: PASS ask-door` hit, staged by cutting the `check_row_value` calls, grading the argument mapping and cutting the count, in turn · none

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
- rev-3 · 2026-11-22 · §1 · §2 · §3 · §4 · AC1 to AC4 · §7 · §10 · per
  `2026-11-22-prompt-TOOL-dTotalRecall-41-reground-brief`, re-grounded at `e1ae60af8`: line cites
  become `path#symbol`; `TOOL-dTotalRecall-7` rev-5's door requires `--sev <LEVEL> <why>` and writes a
  `SEV` row, so S1 refuses the reason too, S3 counts the `SEV` row and every criterion's command passes
  `--sev`; the grade's corpus is `build_corpus` of the one parse; the arm moves from `gov_record.py`,
  which no leg runs, to unit 7's `ask-door` plant in `check-memory-hygiene.test.sh`; the leg line gains
  `memory-hygiene self-test`, `drift-audit selftest`, `memory-recall kit selftest` and `policy
  fixtures`.

## 10. Reuse audit

The seams extended are the backlog grammar's own constants and readers in
`tools/memory-tree/backlog.py`: `#SEP`, `#ARROW`, `#render_ask_row`, `#render_sev_row`,
`#parse_file`, `#build_corpus` and `#derive_clauses`, and `TOOL-dTotalRecall-7`'s `write_new_ask`,
`check_ask_acceptable` and `ask-door` plant. No Python row-value refusal exists to extend:
`grep -n newline tools/memory-tree/backlog.py` finds only `#parse_file`'s docstring, and the nearest
test, `tools/memory-tree/build_records.py#write_record`'s inline CR and LF check, guards a record's
field grammar beside `FORGED_FIELD`, never the row separators; `TOOL-dTotalRecall-43` S37 extracts the
shared line-break half. `tools/roles/handoff.py#render_shape_line` folds a separator instead, the
alternative §4 rejects. At `e1ae60af8`, `python tools/codebase-map/reuse_lookup.py "refuse a newline
or separator in a backlog row value before writing"` ranks name-stem neighbours (`rows`, `write`,
`write_record`, `extract_row`), none a refusal of a row value. The shell precedent is
`tools/unattended/unattended.sh#verb_rescope`'s field refusal, beside `#check_step_fields`.

Recall terms used: `python tools/memory-recall/query.py "how is a line break or row separator refused in a value written into a one-line row" --terms "newline carriage return separator forge row park rescope refuse value one line render_ask_row"`
