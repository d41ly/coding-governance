**Serves:** journal TOOL-dWitnessedBar-8

# TOOL-dWitnessedBar-8 — builder return 2 (run `wf_b6ee5899-0be`), committed 5944dcc3cb203ef0a97ce1aceb964195f6b9d71a

## Why

TOOL-dWitnessedBar-8 is built from spec rev-7 and committed in pass commit 5944dcc3c, which carries `Pass: TOOL-dWitnessedBar-8` and sets the spec status to CLOSED. A second commit, 2e15cfa04 (`Pass: none`), re-renders .governance/policy.json. It comes after the pass because the mirror refuses a catalogue that is not committed, which is how unit 25 did it. Before writing anything I checked every claim the spec makes about the code against HEAD (paths, symbols, blob-pinned lines, the `.leg` row fields, the verdict's `tree`/`run_id`/`ended` keys, ASKS_CMD, read_row_commit, add_scratch_worktree, BAR_INERT_KNOBS, the catalogue rows, the HYGIENE kind list, and the kickoff manifest's watch line). All of them held, so there was no divergence to report.

## Summary

The unit is built and committed; AC1's fixture-bar behaviour and every gate in §7 are still owed to the main loop at the close.

**Commits** (base 531336dcb5a5a599bdaa025da5f611f1ea912eab):
- Pass commit 5944dcc3cb203ef0a97ce1aceb964195f6b9d71a. It sets the spec to CLOSED and includes RUN.md, the acceptance ledger memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-8-1-acceptance-ledger.md, and deviation record memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-8-deviation-82.md (number 81 was already taken). It also includes what `gen_build_index.py --write` and `gen_map.py --write` rewrote, and the kickoff manifest re-stamped at base.
- Follow-up commit 2e15cfa04fa4761e7d956c9feff66a23d0dcb4d2 (`Pass: none`): the .governance/policy.json mirror.
- No path outside the dispatched write set was written. help/reference/drive.md and units.md were already modified before this pass (line endings only) and were left unstaged.

**What changed:**
- **tools/run-gates/run-gates.sh:** under `GATE_RERUN=1` (read once, then unset), each red leg runs once more into `.rerun` files, after the serial retry and the sample and before `run_attribution`. Legs whose ceiling fired are skipped, and nothing re-runs if the wall fired. The re-run writes no gate-logs file and prints `nondeterministic · <leg>` when the leg goes green.
- **tools/run-gates/verdict_flow.py:**
  - `route` sends a leg to `flakes` when its re-run reads ok.
  - New `flakes` verb writes the flake record through `keep_tails.load_factory` and `write_record`, and prints the `hold` lines.
  - New `flakes --check`.
  - New `quarantine` row source in SELECT_SOURCES, read at R in a scratch worktree.
  - `read_conf_at` is extracted from `read_held_runner`.
  - Five new fixtures, and the `--build`/`--unit` rules in `main`.
- **tools/memory-tree:** build_records.py gets the `flake` kind, and `read` now falls through to `read_record` for kinds with no reader of their own. tree_lib.py adds `flake` to TYPED_RECORD_KINDS. HYGIENE.template.md and memory/HYGIENE.md now list twelve typed kinds.
- **tools/unattended/unattended.sh:**
  - New `write_leg_ask`; `write_held_asks` now files through it and no longer calls `derive_ask_seq` itself.
  - New `run_leg_records`, extracted from `write_leg_tails`.
  - `gates-green` sets `GATE_RERUN=1` and runs `flakes` right after `run_verdict_route`, filing one MED held-flaky-leg ask per `hold` line.
  - `write_ask_rows` leaves out "red at" when it is given no sha.
- **Other files:** `GATE_RERUN` added to BAR_INERT_KNOBS (.githooks/pre-push.test.sh) with its reason. Summary and usage added for `verdict.flakes` and `verdict.flakes.entry`, then unsummarised-keys.txt and help/reference/policy.md re-rendered. The run-gates README is updated. Canary arm 9n is written and the floor raised 461 to 465.

**Checks that ran** (fixtures and probes of this unit's own code, not gates):
- **AC2–AC6:** the five `verdict_flow.py --fixture` cases all exit 0. Those fixtures stand in for nothing in §7, since no leg runs them. The existing route, red-route, selection-rows, held-keys, select and held-policy fixtures still exit 0.
- **AC8:** `build_records.py --fixture --plant typed-kinds` reports `flake` as bound and PASS with 12 kinds (stands in for the memory-hygiene self-test re-run).
- **AC7:** `grep -c` gives 4 and the `derive_ask_seq` sed check gives 0. A probe that sliced `write_leg_ask` out of the driver and ran it with stubs showed: no reuse across `recall floor` / `recall floor arms`, reuse on an exact match, the held-suite rows byte-identical to before, and the DARK path printing what it would file (stands in for the waived unattended-suite arms).
- **AC9:** the two greps give 0 and 2 (stands in for policy check and help reference pages).
- **AC1:** the grep shows a single `runleg "$i" .rerun` call site at line 5548, between `run_leg_retry` (5485) and `run_attribution` (5558). `bash -n` passes on run-gates.sh, run-gates.test.sh, unattended.sh and pre-push.test.sh.
- **H49 knob classes:** a re-implementation of `check_knob_classes` reports nothing unclassified and nothing stale (stands in for the pre-push self-test arm).
- **Naming lexicon:** run in full, OK, offenders at the 1417 pin. Every new name was checked with `--suggest` and came back OK.
- **`flakes --check` in this repository:** exits 0 over 0 asks in 5.6 s.

**Refused, not worked around:** the role hook blocked a fixture bar of run-gates.sh under GATE_RERUN=1 ("a role agent runs no gate", row G2). That means AC1's behaviour is not observed here: a red bar, `<i>.rerun.leg` reading ok, the `nondeterministic` line, and a ceiling-fired leg not re-run.

**Owed to the main loop at the close:**
- New arm `tools/run-gates/run-gates.test.sh` arm 9n (covers AC1): its run and its RED-first observation.
- All of §7: run-gates canary, run-gates evidence, measure-legs selftest, unattended kit gate, memory hygiene, kit/dogfood doc parity, recall floor, recall floor arms, spec tokens, scratch-guard self-test, tier2-review self-test, policy fixtures, pre-push self-test (H49 class), memory-hygiene self-test, policy check, help reference pages, routed-commits selftest, kickoff-manifest ratchet.
- The unattended suite's arms over `write_held_asks` (h9 slices `write_held_asks` alone, so it now also needs `write_leg_ask` sliced). §7 says their verdict is waived for this landing.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` ran after both commits. For the pass commit it selected 66 classes plus the 6 universal ones; what I acted on:
- **Runner knob classified:** `GATE_RERUN` is in BAR_INERT_KNOBS and unset in the runner, so a nested bar never inherits it.
- **Floor raised:** the canary floor now counts the four new arm-9n assertions.
- **No fixture passes by finding nothing:** each new fixture has a case that would read negative.
- **No `GIT_*` leaks into the ask generator:** the generator subprocess runs with every `GIT_*` variable stripped.

The mirror commit selected only the 6 universal classes. Two residuals are named, not fixed:
- **ASKS_CMD has two readers:** `verdict_flow` parses it from the conf with Python, while the driver sources the conf in shell. This is the spec's own design; the two agree for the present literal value.
- **No idempotence key:** a manual second `flakes` run over the same run dir would write a second record. The driver can't do this, because each bar gets a fresh run id.

Deviation 82 records what the spec left open: a walled bar re-runs nothing; a sampled leg prints `nondeterministic` only once; `flakes --check` uses a declared entry value as its threshold; the read-back line carries no sha for a flaky-leg ask; views are now rendered once per filed ask. (DERIVED from the builder's probe)
