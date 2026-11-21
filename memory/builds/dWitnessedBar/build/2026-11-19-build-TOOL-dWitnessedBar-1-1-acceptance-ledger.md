# TOOL-dWitnessedBar-1 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-1

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-20, by running the unit's own CLIs over their scratch fixtures: `drift_report.py --gate-health
--fixture <case>` in `tools/drift-audit/`, `verdict_flow.py --fixture <case>` in `tools/run-gates/`,
`build_records.py --fixture --plant typed-kinds` in `tools/memory-tree/`, and `drift_report.py
--gate-health` over this tree. The new drift arm `test_gate_health` in `tools/drift-audit/selftest.py`
(CHECK_FLOOR 486 -> 494, counted) runs the same four cases and was not run: its run and its RED-first
observation are owed to the main loop at the close, with the legs section 7 names.

**Evidences:** TOOL-dWitnessedBar-1
- AC1 — `measured 4/10` — `--fixture differs` exited 0 printing `drift-report: gate-health measured 4/10 ·
  legs 10/10 · verdicts fx-00 … fx-29`, the thirty run ids, over ten bar legs whose newest ten hold eight
  at no flake and two at three, two of the eight flaked five times in the twenty before. Over every row,
  or over all thirty per leg, the same planted set reads otherwise; the RED of the arm is owed at the close.
- AC2 — `measured 1/10` — `--fixture lower` exited 0 printing `measured 1/10 · legs 10/10`; and
  `verdict_flow.py --fixture flakes-window` printed, under a planted `Measured` of 1/10, `hold  A  2/10` and
  `hold  B  1/10`, B's one flake in its last ten, and exited `fixture flakes-window ok`.
- AC3 — `unarmed` — `--fixture short` exited 0 printing `drift-report: gate-health unarmed · leg 03 29/30`
  with `--write`, no gate-health record written, and neither the `kit` leg nor the `selftests` leg named.
  Over this tree `--gate-health` printed `unarmed` naming all 118 bar legs at `0/30`.
- AC4 — `--gate-health --write --build` — `--fixture write` exited 0: the armed `--write` wrote
  `<date>-build-ARCH-tHealth-1-gate-health-1.md`, which `build_records.py read` passed (exit 0, `Measured:
  4/10`, `Verdicts`, `Legs: 10/10`); `--with gate-legs.json` exited 2 writing nothing; one row deleted, the
  same command printed `unarmed` and wrote nothing; `--with` naming an unstaged thirtieth verdict armed it.
  `verdict_flow.py --fixture flakes-record` printed the stub drift kit's argv `--gate-health --write --build
  tFlake --unit ARCH-tFlake-1 --with memory/builds/tFlake/build/…-flake-1.md` under `record`, and no stub
  line under `retry-only`.
- AC5 — `flaked 2` — `verdict_flow.py --fixture measured-check` exited 0: a `Measured` of `3/10` dated
  2026-01-20, before the ask filed 2026-02-01, made `flakes --check` exit 1 naming `leg D`, `flaked 2` and
  `3/10`; dated 2026-02-10, after the ask, it exited 0 at 2/10.
- AC6 — `build-records: PASS typed-kinds` — the plant printed `PASS typed-kinds — 13 typed kinds bound,
  --print-bindings printed no A row`, the `gate-health` record read `bound`; `grep -n 'gate-health'
  memory/HYGIENE.md` named line 681 of the closed kind list.
- AC7 — `read_flake_body` — the grep names `build_records.read_flake_body` and `derive_flaked` called in
  `verdict_flow.py` (lines 690, 784, 879) and `br.read_flake_body` and `br.derive_flaked` in
  `drift_report.py`; the `count("\t") == 2` grep over both files names nothing (exit 1).
- AC8 — `hold  A  2/10` — `--fixture flakes-window` exited `ok`: `hold  A  2/10` with no gate-health record,
  none at a planted `Measured` of 3/10, the same `hold` line with the kind out of the loaded table and the
  kind back in it after, and no hold once A's ask closed after its flakes.
