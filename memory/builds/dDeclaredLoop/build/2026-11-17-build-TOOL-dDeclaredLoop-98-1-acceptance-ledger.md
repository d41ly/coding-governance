# TOOL-dDeclaredLoop-98 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-98

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-2 of the spec, over the working tree, by the first dispatch, which started from the base
`6d0b2a447`. The `conf-read-forms` plant of `budget.py`, run alone by `--fixture --plant`, stands in for the
`loop budget fixtures` leg's run of that plant; the `no-own-conf-read` plants of `budget.py` and
`breakpoints.py`, each run alone, stand in for that leg's and the `loop breakpoint fixtures` leg's runs of
them, and both printed `held`. The AC3 probe, run by `python -I`, stands in for nothing a leg runs. Each
staged break was observed in a scratch copy of the loop, lib and memory-tree kit folders outside the tree.

The sweep re-run at the base held every design claim: the branch holds one PINNED `import loop_lib` statement,
inside the tree_lib rows; `budget.py` holds 29 PINNED definitions before and after; the callers of
`derive_conf_reads` are eight PINNED call sites in `budget.py` and one in `breakpoints.py`; the lexicon
offender pin reads 1215 PINNED; the shared records are the two the spec names; the kickoff manifest's
watch line names no path under the loop kit; the positional registry holds no row for this spec; no help
page and no loop README line names `conf-read-forms`; the loop kit holds no families file. The pass mints
no function, shell file, shared record or watched kickoff path, so no deviation is recorded.

Owed to the close: every leg section 7 names, the `loop budget fixtures` leg among them, and the RED-first
observation of the `New arm:` line covering AC1 and AC2, the declared readers seen row staged with the
rule's callee set restored to the literal pair and with an empty tuple.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant conf-read-forms` with the reader-call callee set restored to
the literal pair exited 1, and 0 once restored: RED observed.
`python tools/loop/budget.py --fixture --plant conf-read-forms` with an empty `CONF_READERS` exited 1, and 0
once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-98
- AC1 — `declared readers seen · 9/9 calls answered · read_design_conf, read_driver_conf, parse_conf` — the plant in `tools/loop/` exited 0 printing that line and `held`, PINNED 2026-11-17; the row absent, no such line prints, the red case the staged breaks under AC2 stand beside.
- AC2 — `declared reader not answered: read_design_conf as loop_lib.read_design_conf` — with the copy's rule matching the literal pair the plant printed `6/9 calls answered` and exited 1, its `MISSED` line naming that miss, `as ll.read_design_conf` and `as r0`; with the copy's tuple empty it printed `0/0 calls answered` and exited 1, its `MISSED` line holding `CONF_READERS is empty` beside the aliased-reader row's miss, PINNED 2026-11-17.
- AC3 — `True []` — the spec's probe in `tools/loop/` printed exactly that; with the copy's row typing its own three-name tuple it printed `False` and the three names, PINNED 2026-11-17.
