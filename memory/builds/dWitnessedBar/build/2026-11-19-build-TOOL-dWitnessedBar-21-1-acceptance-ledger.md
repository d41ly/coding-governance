# TOOL-dWitnessedBar-21 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-21

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-20, by running the unit's own CLI, `fix_keeps.py --keeps` in `tools/unattended/` and each plant of
`fix_keeps.py --fixture`, whose throwaway repository drives a copy of the driver, and by the two greps and
the probe the criteria name. The plants were also run from a scratch copy of the kit whose driver had both
`check_fix_keeps` calls deleted: `writes-test-file`, `commit-test-file` and `unknown-leg` each printed FAIL
there. The new driver-suite arm in `tools/unattended/unattended.test.sh`, the shape refusal called directly
and the five plants, was written and not run: its run and its RED-first observation are owed to the main
loop at the close, with the legs section 7 names.

**Evidences:** TOOL-dWitnessedBar-21
- AC1 — `leg:memory hygiene` — run in `tools/unattended/`, `--keeps 'leg:memory hygiene'` exited 0 printing
  `tools/memory-tree/check-memory-hygiene.sh` alone on stdout (its stderr note `fix-of: tests
  feature.memory-tree-hygiene`); `--keeps 'leg:nope'` exited 2 printing `fix-of: refused · no leg named 'nope'
  in the leg manifest`.
- AC2 — `acceptance-fixture` — the plant printed `--keeps acceptance · exit 0 · tools/fx/fixtures/a.txt`, the
  fixture alone and not `tools/fx/fx.sh`; `--dispatch --fix-of acceptance --writes tools/fx/fixtures/a.txt`
  exited 1 under check 49 naming it, and `--writes tools/fx/fx.sh` exited 0 with one `fix-of` row;
  `fix-of: PASS acceptance-fixture`.
- AC3 — `writes-test-file` — the fixture's `--dispatch … --fix-of 'leg:fx canary' --writes tools/fx/fx.test.sh`
  exited 1 printing `UNATTENDED check 49 FAILED — a fix pass keeps the red check's own files out of its write
  set, so --dispatch refuses tools/fx/fx.test.sh`, the route naming `gov-tester`, `spec-wrong` and
  `feature.fx`, and the run-state file was byte-unchanged; `fix-of: PASS writes-test-file`.
- AC4 — `writes-product` — `--writes tools/fx/fx.sh` exited 0 printing `dispatch declared`, and the fixture's
  `RUN.md` held one `fix-of · item <anchor> ARCH-tFix-1 · reason leg:fx canary` row; `fix-of: PASS
  writes-product`.
- AC5 — `commit-test-file` — after that dispatch, `--check-commit` exited 0 with `tools/fx/fx.sh` staged and 1
  once `tools/fx/fx.test.sh` was staged too, printing check 49 `so --check-commit refuses tools/fx/fx.test.sh`
  with the route; with the calls deleted the same staging met only the undeclared-path widening refusal, which
  names no route; `fix-of: PASS commit-test-file`.
- AC6 — `unknown-leg` — `--fix-of leg:nope` exited 1 printing `--fix-of cannot derive the red check's own
  files … leg:nope · fix-of: refused · no leg named 'nope'`, the run-state file byte-unchanged; `fix-of: PASS
  unknown-leg`.
- AC7 — `grep -n 'fix-of'` — it printed the verbs carrier's paragraph from line 321 of
  `memory/guides/UNATTENDED-VERBS.md`, byte-identical to `tools/unattended/VERBS.template.md`, and the driver's
  header line 23 ending `[--fix-of <red>]`.
- AC8 — `True False` — `grep -c '"fix-of"'` printed 1 for `tools/drift-audit/drift_report.py` and 1 for
  `tools/runlog/model.py`, and the `record` probe printed `True False`.
