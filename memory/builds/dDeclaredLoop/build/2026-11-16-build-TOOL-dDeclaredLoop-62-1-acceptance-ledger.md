# TOOL-dDeclaredLoop-62 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-62

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node
`d` (win32), at rev-4 of the spec, by probes of the unit's own code: `.gitattributes` read with `sed`
and `git check-attr`, and the `budget.py` plants run alone by direct CLI in their own scratch
repositories, the stagings applied in memory by a `python` probe that replaced `write_budget_rows` or
`read_git` for one run and left the file untouched. No function is minted, so the lexicon pin does not
move; no shell file is edited, so the driver's census and its family counts do not move. The help
anchors through `docs_leg.py --fingerprints` read unchanged for the four `script:tools/loop/budget.py`
rows.

The `loop budget fixtures` row is re-priced from the direct readings, as deviation 624 PINNED records.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of the `New
arm:` line, the `parallel-append-uneven` plant and the append-only check staged by a fixture attribute
answering `unspecified`, a write that doubles a row, and a write that puts rows ahead of the record's
lines.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant parallel-append-uneven` with the fixture's merge attribute
answering unspecified exited 1, and 0 once restored: RED observed.
`python tools/loop/budget.py --fixture --plant parallel-append-uneven` with a write that doubles each row
exited 1, and 0 once restored: RED observed.
`python tools/loop/budget.py --fixture --plant parallel-append-uneven` with a write that puts the rows ahead
of the record's lines exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-62
- AC1 — `merge=rows` — the `sed` range from the `instructions.lock` line to the transition line holds `merge=rows`, `147 of` and `draw id` once each in its comment lines, and `git check-attr merge` on `2026-11-16-build-TOOL-dDeclaredLoop-1-transition-1.md` in `memory/builds/dDeclaredLoop/build/` answered `merge: union`.
- AC2 — `unfrozen 3/4` — `--fixture --plant parallel-append-uneven` read the attribute `union`, merged `side` at exit 0, printed three draw rows `TOOL-tFix-1 · 1/4`, `TOOL-tFix-2 · 1/4` and `TOOL-tFix-3 · 2/4`, each with its own draw id, `budget_state` answered `unfrozen 3/4`, and the plant printed `held`; staged with `check-attr` answering `unspecified` it printed `MISSED` naming the conflicted merge, and staged with a row doubled it printed `MISSED` naming the three distinct rows; figures PINNED at the default `4+2` base.
- AC3 — `MISSED` — staged with `write_budget_rows` putting its rows ahead of the record's lines, the plant printed `MISSED` naming each draw, `TOOL-tFix-1` on main and `TOOL-tFix-2` and `TOOL-tFix-3` on side, as having rewritten the record; unstaged it printed `held`, and `--plant parallel-append` with the same check on its two draws printed `held`.
