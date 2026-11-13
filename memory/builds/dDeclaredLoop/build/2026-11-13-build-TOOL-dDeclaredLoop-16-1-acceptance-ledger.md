# TOOL-dDeclaredLoop-16 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-16

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed by the
loop reader's two new plants, by `python -c` probes that import `tools/loop/loop_lib.py` and call the
functions the criteria name, over the working tree and over a scratch copy of the kit, by the record
factory's door and `read` verb over a scratch tree, by its `typed-kinds` plant, and by the `grep`
commands the criteria spell. The pass base is `50b4d1db`.

Owed to the close: the `loop definition` leg, which is the first half of AC1's own command and which
the role's hook refused in this pass; every leg the spec's section 7 names; and the RED-first
observation of its two `New arm:` lines, `tools/loop/loop_lib.py` covering AC1, staged by giving
`ask` twice in the shipped set, and `tools/memory-tree/check-memory-hygiene.test.sh` covering AC6,
staged by the kind in the factory's table and not the reader's tuple. The kit version constants of
the spec's section 5 move at the close, where the epoch legs name them.

**Evidences:** TOOL-dDeclaredLoop-16
- AC1 — `loop: dispositions` — the line is printed by `tools/loop/loop_lib.py#main` from the members
  `check_loop` returns; `python tools/loop/loop_lib.py --check` itself was NOT RUN, being the
  `loop definition` leg's command, owed to the close. Observed in its place: a probe of
  `load_loop` over the kit returned the members `continue amend new patch repeat unit breakpoint ask
  none` in the order of S1, and `check_loop` over the definition with both tables taken out returned
  an empty list. `python tools/loop/loop_lib.py --fixture --plant disposition-unknown` exited 1
  printing `the disposition ask is given twice`.
- AC2 — `resolve_disposition` — a `python -c` probe importing `loop_lib` from `tools/loop` returned
  `ask`, `amend`, `continue` and `new` for `defer`, `attach`, `refuse-as-duplicate` and `new`, and
  raised `LoopError` on `fold`, its message naming the word and the set.
  `python tools/loop/loop_lib.py --fixture --plant disposition-alias` exited 1 printing
  `disposition-alias row 2 (defer) means 'postpone', which is no member of the set`.
- AC3 — `Item is missing` — over a scratch tree holding `memory/builds/tFix/`, the door
  `build_records.py new disposition` with `--channel terminal` wrote
  `2026-11-13-build-TOOL-tFix-1-disposition-1.md` carrying `Item`, `Disposition`, `Channel`,
  `Reason` and `Caused-by`; with `--channel email` it exited 1 printing `Channel email is outside
  mailbox · terminal · prompt`, and the folder held the one record after it; `build_records.py read`
  over that record exited 0, and with its `Item` bullet taken out exited 1 printing `malformed · Item
  is missing`.
- AC4 — `check_disposition_record` — over a scratch copy of `tools/loop` whose definition gained an
  `[[item]]` row `item.build.ratify` declaring `outcomes = ["ratified", "rejected"]` and a row
  `item.entry.place` declaring `outcomes = "dispositions"`, a `python -c` probe returned `True` for
  `ratified` on the first and raised `LoopError` for `continue` on it, naming `item.build.ratify`
  and `ratified rejected`; returned `True` for `continue` on the second and raised for the alias
  word `defer` on it; and returned `None` for an item with no row. Over the shipped kit, which holds
  no item row, the same call returned `None`.
- AC5 — `grep -nE 'REVIEW_DISPOSITIONS|class:|select' tools/loop/README.md` — printed three lines
  of the section "The disposition set", one per vocabulary named as not this set: the review round's
  exit with `REVIEW_DISPOSITIONS`, the per-finding report grammar with `class:`, and triage's
  verdicts with `select`.
- AC6 — `PASS typed-kinds` — `python tools/memory-tree/build_records.py --fixture --plant
  typed-kinds` exited 0, printing a `disposition` line ending `bound` for
  `memory/builds/tKinds/build/2026-11-13-build-ARCH-tKinds-1-disposition-1.md` and its
  `PASS typed-kinds` line; the plant wrote the record through the door's `DOOR_ARGV` row and found
  the door refusing each other door's flag.
- AC7 — `<kind>` — `grep -n 'disposition' tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md`
  printed, in each file, the kind's entry in the closed `<kind>` list and the paragraph
  "Disposition records" with its fields and its door; a `diff` of the two files over that region
  printed nothing.
- AC8 — `grep -nE 'dispositions|new disposition' help/loop.md` — printed the `[dispositions]` table
  of the page's example, the `loop: dispositions` line of the read's output and the
  `build_records.py new disposition` command of the section "The owner's disposition record".

Beside the criteria: the names and refusals the pass added beyond the spec's inventory are recorded
as `2026-11-13-build-TOOL-dDeclaredLoop-16-deviation-163.md`. The usage pin of the `new` row moved
from `d9f4ae09` to `3cae4d5e` in `help/charter.md`, computed by the rule of
`tools/govkit/docs_leg.py#derive_usage_fingerprint` and checked by reproducing the old pin from the
row at the pass base.
