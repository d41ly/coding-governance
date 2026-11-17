# TOOL-dDeclaredLoop-32 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-32

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node
`d` (win32), at rev-6 of the spec, by probes of the unit's own code: `review_counts` and `review_state`
sliced out of the driver and called over a scratch run-state file; the driver run in fresh scratch
repositories built by `position.py`'s `write_position_plant` and run through its `run_driver`, as
`budget.py`'s `driver-draws` plant builds them, one per criterion and policy file; check 2's review awk
cut out of `check-unattended.sh` and run over scratch run-state files; the build harness through the
suite's own `run_wf` double, sourced alone with the new arms, against the render and against the base
render; `review_bounds.py`'s two plants by direct CLI; and greps over the carriers and renders.

The budgets were measured with `check-arms.py`'s own readers before the commit: the driver's census
reads 332 PINNED against its raised ceiling of 332 PINNED, the families 1/1, 11/11 and 36/37 PINNED,
and `check-unattended.sh` 266/266 PINNED. Each new function name was put to the lexicon's suggest
verb. The help anchors are the fingerprints `docs_leg.py --fingerprints` prints.

The first dispatch's patch was applied whole and checked against rev-6. One defect in it was fixed
before the commit: `check_fix_pass_open` read `CONVERGED`, `CEILING` and `BOUNDED` as terminal but not
`NON-CONVERGENT`, so the never-greening fix pass took a third pass; the plant's third pass and its
dispatch are refused now.

Owed to the close: every leg the spec's section 7 names, and the RED-first observation of each
`New arm:` line: the driver-suite arms staged against the base driver, the check-2 arms against the
base check, the harness arms against the base harness (their six assertions were run here against the
base render as a probe, where five red and the bare-record negative holds), the `targets` plant
against a `show` of four fields, and `tFixPassLast` against `_RUN_ROW`'s `[a-z]+`.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/review_bounds.py --fixture --plant targets` with every function the unit's pass changed in
`tools/loop/review_bounds.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.
Not observed: the arm in `tools/unattended/unattended.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.
Not observed: the arm in `tools/unattended/check-unattended.test.sh`, a suite arm, left unrun for the owner's
opt-in slow-suite run.
Not observed: the arm in `tools/workflows/unattended-build.test.sh`, a suite arm, left unrun for the owner's
opt-in slow-suite run.
Not observed: the arm in `tools/drift-audit/selftest.py`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-32
- AC1 — `3 3` — the sliced `review_counts` printed `3 3` for `S` and `2` for `T`, and `review_state "3" 3 3` printed `NON-CONVERGENT` with `MAX_ROUNDS=8`.
- AC2 — `round-highs 2` — in a plant repository the slug's round 2 printed `NON-CONVERGENT`, its row read `blockers 1 · round-highs 2 · round-minors 0 · NON-CONVERGENT · highs 3 · minors 0 · to units · disposition promote`, and a third `--review` exited 1 naming the terminal round.
- AC3 — `NON-CONVERGENT` — the slice printed `NON-CONVERGENT`, `CONVERGING`, `CONVERGING` and `BOUNDED` for the four calls, in order.
- AC4 — `loop: budget · target · on-exhausted` — under `rework-budget = 1` round 2 drew `1/1`, its row carried ` · to asks · disposition promote` and its sentence named asks; `budget.py target` at that repository's top level printed `loop: budget · target · on-exhausted`.
- AC5 — `--reds 1` — the second `--fix-pass` printed `NON-CONVERGENT · to units`, the third and a `--dispatch` of the unit each exited 1 naming the terminal pass; under `rework-budget = 0` the second row carried ` · to on-exhausted`.
- AC6 — `_RUN_ROW` — the three copies each counted 1, `PARK_KINDS_OWED` counted 0, and `_RUN_ROW` matched the `fix-pass` row with group one `fix-pass`.
- AC7 — `to asks` — check 2's awk printed the asks floor for the `to asks` exit with no new ask and nothing with one, printed no stall for the falling `round-highs` pair or the flat spec subject `S1`, and printed the stall for the same flat rows on `tRev` and for the two `reds 1` fix passes.
- AC8 — `'specTarget'` — the two `writeRound` slices were byte-identical with `' --round-highs '` before `' --subject '`, and `grep -c "'specTarget'"` over the render printed 1.
- AC9 — `--fix-pass` — each of the five tokens counted at least 1 in both carriers, `unattended.sh --fix-pass ` counted 1 in the Skill template and render, and the render measured 10815 PINNED CR-stripped, its size row.
- AC10 — `exits CONVERGED` — the slice printed `CONVERGED`, `CONVERGING` and `NON-CONVERGENT`; under `until-no-high` the bare round was recorded `CONVERGING`, and under `until-no-blocker` it exited 1 naming `exits CONVERGED`.
- AC11 — `no-fall` — the slice printed `CONVERGING`, `BOUNDED` and `NON-CONVERGENT`; under `rework-budget = 0` the spec subject's terminal row carried ` · to units` and the slug's round-1 exit ` · to asks`.
- AC12 — `held` — `--plant defaults` held on `spec-target=blockers closing-target=highs route-backs=3`, and `--plant targets` held on `spec-target=all closing-target=all route-backs=2`.
- AC13 — `verb:unattended.sh:--fix-pass` — `docs_leg.py --list` named it and `script:tools/loop/budget.py#target` anchored on `help/loop.md`, each once.
