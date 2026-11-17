# TOOL-dDeclaredLoop-54 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-54

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-4 of the spec, over the working tree: `loop_table.py check` and its two new plants run by direct CLI,
standing in for the `loop transition tables` leg; `termination.py check` and the `unit-dead-end`,
`dead-end` and `empty-states` plants run by direct CLI, standing in for the `loop termination` leg; and
the `grep` and `docs_leg.py --fingerprints` probes the criteria spell, standing in for the `docs` leg. The
section 5 sweep re-run at the base of this pass matched its design claims: `read_transition_rows`,
`derive_from_states`, `check_transition_tables` and the termination module read as rev-4 cites them, the
lexicon offender pin stood at 1215 PINNED with `read_terminal_set` printing `OK` by `--suggest`, the
refusal ceilings were unmoved and no shell script was edited. The plant grader dropped the composition
parameter its `dead-end` entry alone read (deviation 542).

Owed to the close: every leg section 7 names. Owed RED-first: the `tools/loop/loop_table.py` arm, its two
new plants and the `terminal unit` case against the base reader; and the `tools/loop/termination.py` arm,
the `unit-dead-end` plant against the build-only set and the `dead-end` plant's exact `terminal` findings
against feature and unit sets filled with the build's list. Both staged breaks were probed in memory by
patching the composition's sets, and each plant closed `MISSED`, exit 1; the close's observation on the
staged files stands owed.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/termination.py --fixture --plant unit-dead-end` with every function the unit's pass changed
in `tools/loop/termination.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED
observed.
`python tools/loop/loop_table.py check --selftest` with every function the unit's pass changed in
`tools/loop/loop_table.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-54
- AC1 — `['build', 'feature', 'unit']` — the `python -c` probe printed it, then the build's `terminal` list, `['deployed']` and `['deployed']`; `python loop_table.py check` exited 0 printing `loop: terminal unit · deployed` and no `loop: table unit-terminal` line.
- AC2 — `unit-terminal-from` — the plant exited 1 printing `loop: refused · ` naming `leaves deployed, a terminal`; `--plant level-no-terminal` exited 1 naming `the level unit declares no terminal set`.
- AC3 — `unit-dead-end` — `python termination.py check` exited 0 with no `unchecked` line and no feature or unit finding; the plant exited 0 printing `loop: termination · terminal · unit reviewed`, then `loop: fixture · unit-dead-end · check exit 1`, closing `loop: fixture · unit-dead-end · held`; `--plant dead-end` exited 0 closing `held`, its one `terminal` finding `build stuck`.
- AC4 — `no terminal set` — `grep -c` printed a count above zero over `help/loop.md` for `unit-terminal`, `level-no-terminal` and `unit-dead-end`, and zero over that page and `tools/loop/termination.py` for `no terminal set`; `docs_leg.py --fingerprints` named the anchors the page already carries.
