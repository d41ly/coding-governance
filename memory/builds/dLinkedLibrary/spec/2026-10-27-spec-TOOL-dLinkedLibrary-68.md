# TOOL-dLinkedLibrary-68 — `log-diff` reads the decision log's rows and archives through the kit's row grammar

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 29 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-27-build-TOOL-dLinkedLibrary-68-deviation-681.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-68-deviation-681.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 18 at HIGH**, report item **H3**. No other id shares the item. Item M3 (ids 4 and 38) is the
same defect at medium, batched in `TOOL-dLinkedLibrary-74`.

`TOOL-dLinkedLibrary-59` S1 and its §4 table class a removed line `rotated` only when it is "a row `<id>
· …`" whose bytes sit in the literal archive `memory/archive/DECISIONS.<date>.md`. At base 213 lines of
`memory/DECISIONS.md` open `- `, and 72 of them are bold-led, `- **<id>** —` or `- **<id>** -`; the
literal also drops the same-day suffix (`DECISIONS.2026-08-17b.md`) that check 10 admits. Every bold row
`TOOL-dLinkedLibrary-1` S8 rotates then reads `departure`, so 59's AC1 is red on a correct build, and a
builder chasing it restores rotated rows and undoes unit 1. `tools/memory-tree/row_grammar.py` already
exports the row regex and the rotated-archive name.

This unit re-points `derive_log_departures` onto those two readers and plants the bold, suffixed case.
It repairs `TOOL-dLinkedLibrary-59` and builds one step after it (order 29).

## 2. Scope (IN)

- **S1** — The row. `derive_log_departures` (`tools/memory-tree/decision_rubric.py`, 59 S1) reads the id
  of each line the diff shows at base and not now with `row_grammar.derive_row_re(conf)`, `conf` from `row_grammar.load_conf(root)`, so a
  line is a row in either spelling the log holds, and classes it `rotated` on the conditions 59 S1 states.
  No row or id pattern is written in `decision_rubric.py`. Observed by AC1 and AC2.
- **S2** — The archives. The rotated population is every file of the memory root's archive directory
  whose name `row_grammar.build_rotated_re(conf)` matches and whose stem is `DECISIONS`, same-day suffix
  included; the literal `DECISIONS.<date>.md` is not spelled. Observed by AC2.
- **S3** — The plant. The `log-diff` case of `decision_rubric.py --fixture --plant` (59 AC2) gains a tip
  that rotates a `- **<id>** — …` row into a `DECISIONS.<date>b.md` archive with the routing record naming
  the id, and that tip reads `rotated` with 0 departures. Observed by AC2.

## 3. Non-goals (OUT)

- S2's order check, the docstring's classes and the real-tree count: `TOOL-dLinkedLibrary-74`'s items for
  ids 4 and 38.
- The `note` class and the verb's output and exits: `TOOL-dLinkedLibrary-59` S1 and S3, unchanged.
- `row_grammar.py`: read, never edited.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-59` — S1's `derive_log_departures`, its §4 table and AC2's `log-diff` plant, which S1 and S2 re-point onto the row grammar and S3 widens (id 18)
- **hands-off** `TOOL-dLinkedLibrary-74` — the classification's `derive_row_re` read, which unit 74 extends to 59's order check (id 4 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-80` — the row-grammar read of `derive_log_departures` and the `log-diff` plant, which unit 80 completes (ids 24, 39 of the spec audit of units 65 to 74)

## 4. Design

### Evidence

- `tools/memory-tree/row_grammar.py:204-212`: `derive_row_re(conf)`, "the ONE row regex: a dash,
  optional emphasis, then an id of this tree's families", its selftest counting copies of the literal.
- `tools/memory-tree/row_grammar.py:225-240`: `build_rotated_re(conf)`, one fullmatch over `<STEM>.<iso
  date><suffix>.md`, the suffix a same-day disambiguator.
- `tools/memory-tree/row_grammar.py:141`: `load_conf(root)`, which refuses an absent conf rather than
  defaulting.
- `memory/DECISIONS.md` at base: 213 lines opening `- `, 141 in the `<id> · ` form and 72 bold-led
  (figure PINNED, counted at `5fede642` with `grep -c '^- \*\*'` and `grep -c '^- [A-Z]'`).

### Files touched (estimate)

- `tools/memory-tree/decision_rubric.py`: S1 to S3

### Alternatives rejected

- **Widening 59's own predicate to admit emphasis.** It is a second row regex, the copy
  `derive_row_re`'s selftest counts against.
- **Matching archives by `startswith("DECISIONS.")`.** The shape `build_rotated_re`'s comment records
  as admitting a date anywhere after the stem, refused by check 10.

## 5. Production-readiness checklist

- security — read-only, as 59 priced.
- perf / scale — one compiled regex and one directory listing.
- error / empty / loading states — an absent conf raises from `load_conf` and the verb exits 2 naming it,
  59 S3's argument refusal.
- observability — unchanged from 59.
- risks — a row in a spelling the row grammar refuses is a departure, the safe side.
- testing — AC2's plant.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'derive_row_re\|build_rotated_re'` runs over `decision_rubric.py` (its path in
  Files touched) at this pass's tip, it prints a call of each, and no `re.compile` line of the module
  spells a family id or a `DECISIONS` archive name.
  Red when: the module keeps its own row or archive predicate beside the row grammar's.
- **AC2** — When `python decision_rubric.py --fixture --plant log-diff` runs, the tip rotating a bold row
  into a `b`-suffixed archive reads `rotated`, and the output's line for that tip reads `0 departure(s)`.
  Red when: a bold row or a same-day archive reads `departure`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/decision_rubric.py · covers AC2 · the bold-row, `b`-suffixed tip of the `log-diff` plant, the failing case staged by 59's middot-only predicate · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 1 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 18 (HIGH, item
  H3).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.

## 10. Reuse audit

The seams extended are `row_grammar.derive_row_re` and `row_grammar.build_rotated_re`
(`tools/memory-tree/row_grammar.py:204`, :237), the one row regex and the one rotated-archive name the
hygiene checks already share. `python tools/codebase-map/reuse_lookup.py "match a decision log row id
with optional emphasis"` ranked `rows`, `row`, `extract_row`, `match_expr` and `read_id_list`; it missed
both seams, found by reading `row_grammar.py`, and the miss is recorded here as M5 asks.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
