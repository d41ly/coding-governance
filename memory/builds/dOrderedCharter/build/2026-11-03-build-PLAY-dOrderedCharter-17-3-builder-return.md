# dOrderedCharter — unit 17's builder returns

**Serves:** journal PLAY-dOrderedCharter-17

Runs wf_dce016de-13e, wf_2c160031-b97 and wf_0821eeef-592, summarized from their returns.

- wf_dce016de-13e returned `DIVERGENCE:`: unit 16's check reported 60 red edges, many no dependency at all. The run
  added PLAY-dOrderedCharter-61 to repair the check, and spec 17 went to rev-4.
- wf_2c160031-b97 returned `DIVERGENCE:`: a flat govkit entry's `optional` part could only match as a literal
  tool-root path, which the install-prefix ban refuses. The run added PLAY-dOrderedCharter-62, and spec 17 went to
  rev-5.
- wf_0821eeef-592 built rev-5 as pass commit `f4d8db192` (34 files): `optional` rows on every core descriptor that
  reaches a non-core kit, flat entries spelling `{prefix}/<file>`; the slot line at the sites S4 to S7 name and in the
  S10 suites; the memory-tree `requires_if` row naming drift-audit replaced by `gen_build_index.py`'s optional row.
- `check_layers.py --list` exits 0: 39 edges, all allowed, 0 red, down from 40 red.
- PLAY-dOrderedCharter-56 closes with this unit; `gen_build_index.py --write` rewrote `memory/backlog/PLAY.md`, outside
  the declared write set, dropping its row.
- `Decided:` trailers: check-install-prefix.sh prints the slot line before its SKIPPED line; run-gates.sh adds its slot
  line beside the govkit-unreachable line; the policy, check-kit-versions, check-wiring.sh and settings-merge sites keep
  their fallbacks as declarations; check-wiring.test.sh's recall arms skip uncounted; check-install-prefix.test.sh exits
  0 with the slot line when no govkit engine is tracked.
- Observed by probe: AC1 to AC5 as the ledger records.
- Owed at the close: AC6 (`check-install-prefix.sh` on a clone without govkit); the run-gates S7 lines under
  `GATE_SELFTESTS=changed`; the §7 legs; RED then GREEN for all seven `New arm:` lines (the unattended suite's arm owed
  with PLAY-dClosedLoop-12 under README rule 8).
