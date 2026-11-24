# KICK-dKeptSession-18 — acceptance ledger

**Serves:** journal KICK-dKeptSession-18

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32 at
the pass's base `2e61d466f` over the working tree before the commit: by `python loop_table.py check` and
each of the four new plants run alone by direct CLI (`python loop_table.py --fixture --plant <case>` in
the loop kit's directory), by a `python -I -c` probe of `check_transition_tables` with the claim module
made unimportable, and by the greps AC4, AC5 and AC6 state.

Before the first edit the spec's cited code was probed at the base. `tools/loop/loop_table.py` has no
commit since `bfc0a4e47`. `FIRST_MOVES` in `tools/loop/claim.py` maps `new`, `repeat` and `patch` to
their first move, and `claim.py` imports `loop_parents.py`, which imports `loop_table.py` at its top, so
the arm imports the claim inside `check_transition_tables`. The `[dispositions]` set holds `repeat` and
`ask`; the build rows from `none` are B1, B2 and B3 of the loop definition, three (DERIVED, a `tomllib`
read at `2e61d466f`), `new` into planning, `patch` with no disposition into designing and `repeat` into
designing, so the landed units 17, 25 and 61 added no entry row, as §4 says. `check_transition_tables`
has one caller, the module's own `main`. `loop transition tables` has no row in
`tools/run-gates/selftest-budgets.txt` (DERIVED, the grep `^loop transition tables` printed 0 at
`2e61d466f`), so no budget row moves.

How the build reconciled the spec's text with what landed. The spec's S4 reads `PLANTS` as 19 keys at
`bfc0a4e4` and 23 after; an `ast` read of the module at `bfc0a4e47` and an import at `2e61d466f` both
read 18 (DERIVED, `len(PLANTS)`), and the module holds 22 after (DERIVED, `len(PLANTS)` after the
edit): the spec's two figures are each one high, the four plants it adds are the four it names, and
nothing in the design reads the count. The `entry rows` refusals and the line are spelled as S2 and S3
state; the line sits after the route join's `loop: owed` lines and before the stand-in lines, since the
arm runs after the route join.

## Criteria

**Evidences:** KICK-dKeptSession-18
- AC1 — `python loop_table.py check` in the loop kit's directory exited 0 and printed `loop: entry rows · new → planning · patch → designing · repeat → designing` after the `loop: owed` lines; each `to` is the row's, the plants below printing `?` where the row is gone or doubled (DERIVED, that run).
- AC2 — `entry-row-missing` exited 1 printing `loop: refused · entry rows · repeat · forward: no build row from none fires item.entry.claim · claimed`, its line `repeat → ?`; `entry-set-missing` exited 1 printing `loop: refused · entry rows · repeat · forward: no member of [dispositions]` beside the landed check's own "no member" refusal for transition row 3; `entry-row-extra` exited 1 printing `loop: refused · entry rows · ask · backward: build row 53 (item.entry.claim · claimed) fires no first move of FIRST_MOVES`; `entry-row-twice` exited 1 printing `loop: refused · entry rows · repeat · forward: 2 build rows from none fire item.entry.claim · claimed: rows 3, 53` beside the landed "matched by two rows" refusal (DERIVED, those runs). The `python -I -c` probe with `sys.modules['claim'] = None` returned no `entry rows` line and the one refusal `entry rows · FIRST_MOVES unread: import of claim halted; None in sys.modules` (DERIVED, that probe).
- AC3 — `python gen_build_index.py --asks --build dIndexedDesign` in the memory-tree kit printed the `TOOL-dIndexedDesign-19` row, `DEFERRED`, blocker `TOOL-dIndexedDesign-10`, its text opening `THE repeat ROUTE READS A PLAYBOOK BY PATH` (DERIVED, that run); the ask is cited, never edited.
- AC4 — `grep -c 'FIRST_MOVES' loop_table.py` printed 6 and the `sed` range of `check_entry_rows`'s body piped to `grep -cE '"(new|patch|repeat)"'` printed 0 (DERIVED, those commands at observation time).
- AC5 — in `help/`, `grep -c 'entry rows' loop.md` printed 2, `grep -c 'by path' loop.md` printed 1, on the sentence that a `repeat` request names its playbook by path, and `grep -c 'entry-row-twice' loop.md` printed 1; `python tools/govkit/docs_leg.py --fingerprints` printed `6513b6ba` for `script:tools/loop/loop_table.py` and `0011b11d` for its `#check` row, the anchors' own, unmoved (DERIVED, those commands at observation time).
- AC6 — `python -I -c` importing `loop_table` printed 5 for `__doc__.count('entry rows')`, and `grep -c 'entry-row-missing' README.md` in the loop kit's directory printed 1 (DERIVED, those commands at observation time).
- seen-red — `loop transition tables` — red `45016a2c4` — green `45016a2c4` — `entry-row-missing`: a first move with no build row read unchecked
- seen-red — `loop transition tables` — red `45016a2c4` — green `45016a2c4` — `entry-set-missing`: a first move outside the disposition set read unchecked
- seen-red — `loop transition tables` — red `45016a2c4` — green `45016a2c4` — `entry-row-extra`: a build row no first move fires read unchecked
- seen-red — `loop transition tables` — red `45016a2c4` — green `45016a2c4` — `entry-row-twice`: two build rows for one first move read unchecked

## Owed to the close

The `loop transition tables` leg, which runs `check --selftest` and so the new `entry rows` case and the
four plants as cases, and the `docs`, `recall floor`, `recall floor arms`, `lexicon naming predicates`,
`memory hygiene` and `spec tokens` legs §7 names, and the `New arm:` line's RED-first observation against
the base module, are the main loop's at the close.
