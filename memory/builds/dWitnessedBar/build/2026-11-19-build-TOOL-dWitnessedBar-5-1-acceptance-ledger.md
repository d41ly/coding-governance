# TOOL-dWitnessedBar-5 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-5

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed on node d, 2026-11-20, by greps over the built tree, by `verdict_flow.py
--fixture` over this pass's file, by `python -c` calls into `leg_factory.py`, and by two scratch
probes that extracted the runner's hold block, `report_one` and the hook's admission and export
blocks and ran them over planted arrays and a planted repository at `%TEMP%/v5h`. Each count below
also read at `c9b50206`, where it read the red, and `verdict_flow.py` at `c9b50206` refused every
new fixture name with its usage line. The three `New arm:` lines of spec section 7 were written and
not run: their runs, their RED-first observations and the section 7 legs are owed to the main loop at (DERIVED from the builder's probe)
the close. The resumed pass, at base `30160e0c`, re-ran every grep and every `--fixture` below green,
the runner's extracted hold block over a planted selection, and the `check_declarations` probes.

**Evidences:** TOOL-dWitnessedBar-5
- AC1 — `grep -c '= selftests \]' run-gates.sh` — printed 1 and `grep -c 'derive_hold_source'
  run-gates.sh` printed 5, the definition and four calls (the hold site, the `changed` selection, the
  last-run writer and `report_one`); the first printed 3 at `c9b50206`.
- AC2 — `python verdict_flow.py --fixture selection-rows` — printed the file's two rows, the one
  refusal `holds ghost leg, which the manifest lacks, ignored`, and a `kit` row refused as outside
  `quarantine level`; exit 0. The runner's own block, extracted, held the quarantined and the `level`
  leg, refused the unknown and the `kit` row on stderr, ran the `kit` row's repo leg, and copied the
  file byte-equal into the run record as `selection`. The `run-gates canary` arm is owed at the close.
- AC3 — `grep -c "printf 'GATE held  " run-gates.sh` — printed 1 and `grep -c "(self-test,"
  run-gates.sh` printed 0; each printed 2 at `c9b50206`. The extracted `report_one` printed
  `(quarantine, flaked 2 of 10)`, `(level e2e, outside tests.landing-levels unit integration)`,
  `(kit, set GATE_SELFTESTS=1 to run)` and `(kit, unchanged since abc12345)`.
- AC4 — `python verdict_flow.py --fixture held-keys` — read `held.1` to `held.3` as leg, source and
  result, refused `maybe` naming `outside unrun ok fail`, and refused a count of 3 over two keys;
  exit 0. The extracted `report_one` wrote `held 4` and `held.1` to `held.4`, one per held leg.
- AC5 — `python verdict_flow.py --fixture select` — held `slow suite` as `level` at R, held it again
  with the levels swapped in the working tree alone, admitted the derived selection and exited 1 on
  one adding `fast suite`, naming it; exit 0. The hook's extracted admission block read rc 0 on a
  derived selection and RED naming the added row otherwise.
- AC6 — `python verdict_flow.py --fixture held-policy` — `push-selected` printed `export
  GATE_SELFTESTS=changed` for an unset pusher value and none for `1`, `on-demand` none, and
  `peer-or-cadence` exited 2 naming the value with no `HELD_CI_WORKFLOW` at R and 0 with one; exit 0.
  The hook's extracted export block exported `changed` under `push-selected` alone.
- AC7 — `python leg_factory.py --conform` — its count line read `legs: 219 declared · 81 claimed ·
  138 exempt · 69 enforces-pending · 101 held · 36 unguarded`, 101 the manifest's held rows, with no
  `held guard` finding; it exits 1 on one `name` finding, `encoding posture (an entry point writes
  stdout as UTF-8)`, which is not this unit's: that leg and the `name` arm are unchanged since
  `c9b50206`, so its exit 0 is owed to whoever renames the leg. `check_declarations` named `held
  guard` on a planted held declaration with neither, with `unguarded_why = ""`, and with a guard in
  every form beside a reason, and was silent on a guard alone, on a reason alone, and on a split guard
  beside a reason (deviation 52); the adopter form `run_conform_adopter` over this tree printed no
  `held guard` finding, `15 held · 6 unguarded`, its two other findings unchanged since base. `grep -nE '[0-9]+/[0-9]+ legs passed' README.md`
  printed nothing; it printed line 100 at `c9b50206`. The scratch-clone run and the `--selftest` arm
  are owed at the close.
- AC8 — `grep -cx 'verdict\.held' tools/policy/unsummarised-keys.txt` — printed 0 and `grep -cE '^##
  .verdict\.held.$' help/reference/policy.md` printed 1; they printed 1 and 0 at `c9b50206`.
- AC9 — `grep -E '^BAR_INERT_KNOBS=' .githooks/pre-push.test.sh | grep -cw GATE_SELECTION` — printed
  1 and `grep -cw GATE_SELECTION .githooks/pre-push` printed 0; the first printed 0 at `c9b50206`.
  The suite's `check_knob_classes`, extracted, printed nothing over the built runner.
