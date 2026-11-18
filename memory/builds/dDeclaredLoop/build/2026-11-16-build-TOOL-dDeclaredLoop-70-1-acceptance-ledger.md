# TOOL-dDeclaredLoop-70 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-70

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-4 of the spec, over the working tree: the `phase` verb run by direct CLI in scratch work trees built as
the selftest builds them, standing in for the `loop transition tables` leg; the `parent-in-extra-phase`
plant run alone by `--fixture`, standing in for the `loop parent routes` leg; and the `grep` and
`docs_leg.py --fingerprints` probes, standing in for the `docs` leg. The section 5 sweep re-run at the base
of this pass held its design claims: the driver's refusal ceiling stands at unit 52's, the lexicon offender
pin at 1215 PINNED with the one new function leading with `read`, both leg ceilings at 120 PINNED, every
script anchor of `help/loop.md` unchanged; its stale figures are deviation 702.

Owed to the close: every leg section 7 names. Owed RED-first: the `tools/loop/loop_table.py` arm,
its seven PINNED scratch-tree cases and the `DRAFTING` case's `--extra=`, against unit 63's empty default; and the
`tools/loop/loop_parents.py` arm, the `parent-in-extra-phase` case against a parent call passing no tree,
which reds as `loop: unanswered` (deviation 702).

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/loop_parents.py --fixture --plant parent-in-extra-phase` with every function the unit's
pass changed in `tools/loop/loop_parents.py` swapped back to its pre-pass source exited 2, and 0 once
restored: RED observed.
`python tools/loop/loop_parents.py --fixture --plant parent-in-extra-phase` with the parent call passing no
tree exited 2, and 0 once restored: RED observed.
`python tools/loop/loop_table.py check --selftest` with every function the unit's pass changed in
`tools/loop/loop_table.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-70
- AC1 — `phase STAGING · state none · step none · adopter phase` — in a scratch tree whose conf sets `PHASES_EXTRA="STAGING"`, `--from STAGING` printed it, exit 0; `--from REVIEWING --to STAGING` ended `· to STAGING · adopter phase · crosses none`, exit 0; `--from STAGNG` exited 1 printing `refused — phase STAGNG: no row`; `--from STAGING --extra=` exited 1 printing `refused — phase STAGING: no row`.
- AC2 — `route none` — `loop_parents.py --fixture --plant parent-in-extra-phase` from gov's top printed it, exit 0, the tree unchanged; the same plant with the parent call's `tree` dropped printed `loop: unanswered` naming `STAGING`, exit 2.
- AC3 — `driver conf unreadable` — in a scratch tree whose conf holds `exit 3`, `--from STAGING` exited 1 printing `loop: refused · driver conf unreadable: <conf> — exit 3`, and `--from REVIEWING` printed `phase REVIEWING · state designing · step step.design`, exit 0; in a scratch tree with no conf, `--from STAGING` exited 1 printing `refused — phase STAGING: no row`.
- AC4 — `as the driver sources it` — `grep -c` printed 1 PINNED over `help/loop.md`; `read_driver_conf` 3 PINNED over `tools/loop/README.md`; `parent-in-extra-phase` 1 PINNED in each of `help/loop.md` and `tools/loop/README.md`.
- AC5 — `DRAFTING` — owed to the close, since only `check --selftest` observes it; by direct CLI in a scratch tree whose conf sets `PHASES_EXTRA="DRAFTING"`, `--from DRAFTING --extra=` exited 1 printing `refused — phase DRAFTING: no row`, the case's owed reading, while `--from DRAFTING` alone printed `adopter phase`.
