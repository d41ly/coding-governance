# Acceptance ledger — the common dir's shared files take a second concurrent writer

**Serves:** journal TOOL-aPairedSlots-7

Observed on node a on 2026-10-12. The run-log suite's new arm `TWO` was run alone from a copy
(`RGRL_ARMS=TWO`) over the changed runner: 6 assertions, no failure. Run twice over the runner as it
stood before this unit, it read RED both times. The drift self-test's new arm was run from a harness
that executes the arm's own source against the changed and then the previous `drift_report.py`.

**Evidences:** TOOL-aPairedSlots-7
- AC1 — `gates.log` — three concurrent writers running the runner's own append statement 60 times
  each with 20000-byte lines left 180 whole three-field lines; through the previous `printf >>`
  statement they left 170 and then 156 whole of 180.
- AC3 — `gate-full-green.shared` — two stamping processes staged under two different names, and after
  25 concurrent stamps each the shared file held one whole stamp with no staging file left; with the
  previous fixed staging name both processes staged under one name. A torn stamp was not reproduced
  on the previous runner in either run.
- AC4 — `write_drift_history` — with a second writer run inside the first writer's open of an absent
  history, the file held exactly one header and both rows; the previous writer left two headers.
