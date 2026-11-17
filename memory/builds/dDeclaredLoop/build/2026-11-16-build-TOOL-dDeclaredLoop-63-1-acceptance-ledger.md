# TOOL-dDeclaredLoop-63 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-63

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-3 of the spec, over the working tree: the `phase` verb run by direct CLI for each adopter-phase case,
standing in for the `loop transition tables` leg; the `driver-plan` plant of `breakpoints.py` run alone,
standing in for the `loop breakpoint fixtures` leg; and the `grep` and `docs_leg.py --fingerprints` probes
the criteria spell, standing in for the `docs` leg. The section 5 sweep re-run at the base of this pass
matched its design claims: the driver's `PHASES_CORE` line held 13 PINNED members, `$(phases)` 1 PINNED
read and `PHASES_EXTRA` 3 PINNED lines; the refusal ceiling stands at unit 52's, and the lexicon offender
pin at 1215 PINNED, no name minted. The registry's rows of this spec read none, and two details of the
arms moved (deviation 632).

Owed to the close: every leg section 7 names, and the sibling-minted `loop breakpoint fixtures`. Owed
RED-first: the `tools/loop/loop_table.py` arm, its five PINNED adopter-phase cases against unit 52's verb, which
takes no `--extra`; and the `tools/loop/breakpoints.py` arm, the `driver-plan` plant's adopter-phase calls
against unit 52's `check_phase_gates`, which passes no `--extra`.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/loop_table.py check --selftest` with every function the unit's pass changed in
`tools/loop/loop_table.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.
`python tools/loop/breakpoints.py --selftest` with every function the unit's pass changed in
`tools/loop/breakpoints.py` swapped back to its pre-pass source exited 0, and 0 once restored: not reddened by
this break, so not observed.

**Evidences:** TOOL-dDeclaredLoop-63
- AC1 — `adopter phase` — `--from STAGING --extra STAGING` printed `phase STAGING · state none · step none · adopter phase`, exit 0; `--from STAGNG --extra STAGING` exited 1 printing `refused — phase STAGNG: no row`; `--from REVIEWING --to STAGING --extra "STAGING QA"` printed `phase REVIEWING · state designing · step step.design · to STAGING · adopter phase · crosses none`; `--from STAGING --to BUILDING --extra STAGING` ended `crosses item.plan.exit item.design.exit`; `--from REVIEWING --extra REVIEWING` printed `phase REVIEWING · state designing · step step.design` with no marker; `--from STAGING` with no `--extra` still exited 1 naming it.
- AC2 — `check_phase_gates tPos REVIEWING STAGING` — the plant printed `held` with its scratch conf setting `PHASES_EXTRA="STAGING"`: that call exited 0, and `check_phase_gates tPos STAGING BUILDING` exited 1 printing `UNATTENDED check 82 FAILED` and `held at item.design.exit`; unit 52's observations printed what they printed.
- AC3 — `--extra` — `docs_leg.py --fingerprints` named `help/loop.md` for `script:tools/loop/loop_table.py#phase`, the anchor re-stamped to its fingerprint; `grep -c -- '--extra'` printed 2 over `help/loop.md` and `grep -c '"--extra="'` 1 over `tools/govkit/usage.toml`, each count PINNED.
