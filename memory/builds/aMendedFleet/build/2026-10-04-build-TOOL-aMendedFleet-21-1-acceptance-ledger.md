# TOOL-aMendedFleet-21 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-21

**Evidences:** TOOL-aMendedFleet-21
- AC1 — `python tools/drift-audit/drift_report.py --json` on the live tree — the `cutoff_keys_armed` row read value 29, of 29, tolerance 29, gateable true, live true; the AC1 `git ls-files` count printed 29 at the same tree; 45 s wall
- AC2 — `python tools/drift-audit/drift_report.py --check` in a `git clone --local` under `%TEMP%/c21` carrying this unit's files, with `--base-ref HEAD` — after one armed `_CUTOFF` line was appended to `.memory-tree.conf`, stderr named `cutoff_keys_armed = 30 (pin 29)`; after `STREAMS_CUTOFF` was then blanked, no stderr line named it and the row read `ok (pin 29, drain it)`
- AC3 — `drift_report.py --check` in that clone — the `PINS` entry raised 29 to 30 with no comment printed `RATCHET WEAKENED` naming `cutoff_keys_armed moved 29 -> 30` in `tools/drift-audit/drift_signals.py`; with a `# 29 -> 30` comment line above it, no ratchet finding
- AC4 — `drift_report.py --json` in that clone with the `PINS` entry deleted — the `cutoff_keys_armed` row read gateable false with the detail opening `no budget declared: add a PINS entry`; `--check` printed no stderr finding naming it, only its table row as report-only
- AC5 — `grep -n "cutoff_keys_armed" tools/drift-audit/README.md tools/drift-audit/drift_signals.template.py` — the README's signal table row, the "Armed cutoff keys are a budget" paragraph naming the three routes and that the signal cannot tell the third from the first two, and the template's commented `PINS` and `RATCHETS` lines
- AC6 — `drift_report.py --json` in that clone with every `_CUTOFF` assignment line deleted from every tracked root conf — the `cutoff_keys_armed` row read live false, value 0, of 0; `--check` printed `cutoff_keys_armed is DEAD — gateable`

## The new selftest arm

- `test_cutoff_keys_armed` in `tools/drift-audit/selftest.py`, run alone through a one-arm slice:
  five checks green. RED on a staged break dropping `build_cutoff_keys_armed` from `SIGNALS`: all
  five failed; restored and green. `CHECK_FLOOR` moved 284 -> 289 for the five.

## Owed at the close

- The `drift-audit selftest` leg runs the whole suite; only the new arm ran here.
- `memory/map/generated/symbols.json` was regenerated in this pass by `gen_map.py --write`; the
  codebase-map coverage and freshness legs are the close's.
- The lexicon leg grades the three new definitions; `lexicon.py --suggest --as py.function` answered
  OK for each, and the leg itself is the close's.
- `drift-audit records` on the bar: the clone's `--check` also named
  `non_terminal_specs_cited_by_product_source` at 4 over pin 2. This unit's own id drops out of it
  once this commit closes the spec; the remainder predates this unit.
