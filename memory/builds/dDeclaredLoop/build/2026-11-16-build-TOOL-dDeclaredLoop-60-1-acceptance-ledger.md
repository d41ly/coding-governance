# TOOL-dDeclaredLoop-60 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-60

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node
`d` (win32), at rev-4 of the spec, by probes of the unit's own code: the two new plants of `budget.py`
and the four plants that write a run-state file, `unrecorded`, `patch-trailer-only`, `pre-spec` and
`trailer-only`, each run alone by direct CLI in its own scratch repository, each printing `held`. No
function is minted, so the lexicon pin does not move; no shell file is edited, so the driver's census and
its family counts do not move. The help anchors through `docs_leg.py --fingerprints` read unchanged for
the four `script:tools/loop/budget.py` rows, whose usage rows this pass does not write.

The `loop budget fixtures` row is re-priced from the direct readings, as deviation 604 PINNED records.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of the `New
arm:` line, the `draws-survive-rotation` and `patch-archived` plants staged against the base's reader,
`ROTATED` reading `RUN.LANDED.*.md` and the suffixed population every live `RUN.md` alone.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/budget.py --fixture --plant draws-survive-rotation` with every function the unit's pass
changed in `tools/loop/budget.py` swapped back to its pre-pass source exited 0, and 0 once restored: not
reddened by this break, so not observed.
`python tools/loop/budget.py --fixture --plant patch-archived` with every function the unit's pass changed in
`tools/loop/budget.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.
`python tools/loop/budget.py --fixture --plant draws-survive-rotation` with `ROTATED` reading only landed
run-state files and the suffixed population the live files alone exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-60
- AC1 — `open 3/6` — `--fixture --plant draws-survive-rotation` drew twice, moved the record to `RUN.ABORTED.0000aaaa.md`, planted a fresh `RUN.md` and drew a third time, printed `3/6` on that draw, `budget_state` answered `open 3/6`, the fresh `RUN.md` held no `budget · ` row, and the plant printed `held`; figures PINNED at the default `4+2` over one unit.
- AC3 — `unfrozen 1/4` — `--fixture --plant patch-archived` drew `patch:tFixPatch` into the run-state file of `tFixPatch` suffixed ` · budget tFix`, moved it to `RUN.ABORTED.0000bbbb.md` and planted a fresh one; `budget_state` answered `unfrozen 1/4` for `tFix` and `unfrozen 0/4` for `tFixPatch`, and the plant printed `held`; figures PINNED at the default base.
- AC4 — `RUN.<phase>.<blob8>.md` — `grep -n "RUN.<phase>.<blob8>.md" help/loop.md tools/loop/budget.py` found the help sentence of S5 and the docstring's rows paragraph.
