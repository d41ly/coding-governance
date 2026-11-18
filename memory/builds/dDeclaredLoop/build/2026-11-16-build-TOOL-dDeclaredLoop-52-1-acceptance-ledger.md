# TOOL-dDeclaredLoop-52 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-52

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-3 of the spec, over the working tree: the `phase` verb, `check` and the four new plants run alone by
direct CLI, standing in for the `loop transition tables` leg; the `driver-plan` and `driver-close` plants
of `breakpoints.py` run alone, standing in for the `loop breakpoint fixtures` leg; a copy of the loop kit
with no driver beside it; and the `grep`, `awk`, `cmp` and `docs_leg.py --fingerprints` probes the
criteria spell. The section 5 sweep re-run at the base of this pass matched its design claims: the
driver's `PHASES_CORE` line held 13 PINNED members, the census read 342 PINNED before the pass and 343
PINNED after it, the families 1 of 1, 11 of 11 and 36 of 37 PINNED unmoved, and the lexicon offender pin
stays 1215 PINNED, every new name passing `--suggest`. Two sweep facts did not hold as written and one
detail of the hold moved (deviation 523).

Owed to the close: every leg section 7 names. Owed RED-first: the `tools/loop/loop_table.py` arm, its
phase readings and four plants against the base tree; the `tools/loop/breakpoints.py` arm, the
`driver-plan` plant's phase observations against the base driver; and the `tools/unattended/unattended.test.sh`
arm, the `check_phase_gates` refusal text against the base driver.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/loop_table.py check --selftest` with every function the unit's pass changed in
`tools/loop/loop_table.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.
`python tools/loop/breakpoints.py --selftest` with every function the unit's pass changed in
`tools/loop/breakpoints.py` swapped back to its pre-pass source exited 0, and 0 once restored: not reddened by
this break, so not observed.
`python tools/loop/breakpoints.py --fixture --plant driver-plan` with the driver plan move skipping
`check_phase_gates` exited 0, and 0 once restored: not reddened by this break, so not observed.
Not observed: the arm in `tools/unattended/unattended.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-52
- AC1 — `phase --from REVIEWING` — printed `phase REVIEWING · state designing · step step.design`; `--fact halt-code=budget-exhausted` on `ABORTED` printed `state incomplete · step none`, `halt-code=fork-unresolvable` `state withdrawn · step none`; `phase --from DRAFTING` exited 1 printing `refused — phase DRAFTING: no row`.
- AC2 — `hold-code=owner-decision` — with `ending=park-for-owner` beside it `HELD` printed `state parked · step none`; with it alone, and with no fact, `state paused · step none`.
- AC3 — `crosses item.design.exit` — `--from SPECCING --to BUILDING` ended `· to BUILDING · crosses item.design.exit`, `PREFLIGHT` to `SPECCING` `crosses item.plan.exit`, `BUILDING` to `VERIFYING` `crosses item.build.exit`, and `VERIFYING` to `BUILDING` `crosses none`.
- AC4 — `loop: phase join · PHASES_CORE · 13 phase(s)` — `check` exited 0 printing it, 13 PINNED, after `loop: phase map · 15 row(s) · 2 qualified` (PINNED); the plants exited 1, `phase-missing` refusing `the phase REVIEWING of PHASES_CORE has no unqualified phase row`, `phase-stale` `the phase row of DRAFTING names no member of PHASES_CORE`, `phase-shape` a row that `carries both state and step`, and `phase-twice` `two unqualified rows of BUILDING`; a copy of the kit with no driver beside it printed the join `unarmed` and exited 0, its `phase-stale` plant still refusing.
- AC5 — `driver-plan` — the plant printed `held`: under `three-gates` the sourced `check_phase_gates tPos SPECCING BUILDING` exited 1 printing `UNATTENDED check 82 FAILED` and `held at item.design.exit`; `BUILDING VERIFYING` exited 0; after the disposition record of `item.design.exit` the first exited 0 while `check_owner_gates tPos` exited 1 naming `held at item.deploy.mandate`. The `driver-close` plant still printed `held` over the extracted read.
- AC6 — `check_phase_gates` — the `awk` over `verb_phase` printed the call's line directly before `set_fact "$rel" phase`; `grep -c 'read_held_gates'` printed 3 PINNED, its definition and its two calls.
- AC7 — `help/loop.md` — `docs_leg.py --fingerprints` named it for the `phase` verb's usage row; `phase --from` counted 3 over `help/loop.md` and 2 over `tools/loop/README.md`, `[[phase]]` 16 over `tools/loop/loop.toml`, `past a step exit` 1 over the verbs template, and `cmp` of the template and its render exited 0; each count PINNED.
