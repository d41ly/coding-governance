# TOOL-dWitnessedBar-8 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-8

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed on node d, 2026-11-20, at base `08cdbb708`, by `verdict_flow.py`'s own
fixtures, by the factory's `typed-kinds` plant, by `grep`, `sed` and `bash -n` over the edited files, and
by one probe that sliced `write_leg_ask` out of the driver and ran it over a scratch repository with its
collaborators stubbed. A fixture bar of this pass's runner under `GATE_RERUN=1` was refused by the
role's hook, so AC1's behaviour is owed to the `New arm:` of spec section 7, `run-gates.test.sh` arm 9n,
written and not run: its run, its RED-first observation and the legs of §7 are owed to the main loop at
the close.

**Evidences:** TOOL-dWitnessedBar-8
- AC1 — `runleg "$i" .rerun`: `grep -n` in `tools/run-gates/` names one call site, line 5548, after the
  top-level `run_leg_retry` (5485) and before the top-level `run_attribution` (5558); `bash -n` reads
  the runner clean. The fixture bar's RED verdict, its `<i>.rerun.leg` reading `ok`, the
  `nondeterministic · <leg>` line and the ceiling-fired leg left unre-run are arm 9n's, owed at the close.
- AC2 — `route-flaky`: `python verdict_flow.py --fixture route-flaky` exited 0, routing the planted OWN
  red whose `.rerun.leg` reads `ok` `flakes` and the one whose re-run reads `fail` `attribute`; the
  `route` fixture still routes every class as before.
- AC3 — `flakes-record`: `python verdict_flow.py --fixture flakes-record` exited 0: under `record` it
  wrote one `flake` record with `Run`, `Ended`, `Sha`, `Tree` and `Legs` `3`, rows for the flaky,
  steady and ceiling-retried legs (the retry's rc as the first), none for a leg with no `.leg`, and
  printed `build_records.py read exit 0` with no `malformed` line; under `retry-only` it wrote none.
- AC4 — `flakes-window`: `python verdict_flow.py --fixture flakes-window` exited 0, printing
  `hold  A  2/10  <two record ids>` over eleven planted records, A's oldest flake outside its window
  and nothing for B; with a gate-health record reading `Measured 3/10` and the kind registered in the
  loaded factory's table alone, no hold; with that record and no kind registered, the same `hold` line
  and `2/10` said; with A's ask CLOSED by a commit after its flakes, A's release read after its newest
  row and no hold.
- AC5 — `quarantine-source`: `python verdict_flow.py --fixture quarantine-source` exited 0: the
  working tree's generator read OPEN asks for A and B, and `derive_selection` at R yielded one
  `quarantine` row, `A · quarantine · 2/10, ask ARCH-tFlake-2`.
- AC6 — `quarantine-check`: `python verdict_flow.py --fixture quarantine-check` exited 0: `flakes
  --check` over C's ask exited 1 naming `leg C`, `flaked 1` and `2/10` with a third flake dated after
  the filing held out, and exited 0 once a second flake before the filing was planted. `flakes --check`
  run in this repository exited 0 over 0 held-flaky-leg asks.
- AC7 — `write_leg_ask`: `grep -c 'write_leg_ask' unattended.sh` printed 4, and `sed -n
  '/^write_held_asks()/,/^}/p' unattended.sh | grep -c 'derive_ask_seq'` printed 0. The sliced probe
  filed a flaky ask for `recall floor` beside an OPEN one for `recall floor arms`, reused that one for
  `recall floor arms`, wrote a held suite's rows byte for byte as `write_held_asks` wrote them, and
  printed the DARK rows with `ASKS_CMD` blank. The unattended suite's arms over `write_held_asks` are
  owed at the close.
- AC8 — `typed-kinds`: `python build_records.py --fixture --plant typed-kinds` printed
  `build-records: typed-kinds · flake · memory/builds/tKinds/build/<date>-build-ARCH-tKinds-1-flake-1.md · bound`
  and `PASS typed-kinds — 12 typed kinds bound, --print-bindings printed no A row`.
- AC9 — `help/reference/policy.md`: after `policy.py lists --write` and `render_playbook.py
  --reference`, `grep -cxE 'verdict\.flakes(\.entry)?' tools/policy/unsummarised-keys.txt` printed 0
  and `grep -cE '^## .verdict\.flakes(\.entry)?.$' help/reference/policy.md` printed 2.
