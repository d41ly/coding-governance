# TOOL-dUnstuckLanding-15 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-15

No merge bar and no self-test suite ran in this pass. The two new arms were run ALONE, as the spec's
criteria say: `selftest.py` imported and each arm called on an empty scratch directory under the
user temp directory. They executed 34 and 13 checks with no failure and no skip. Ten staged breaks of
the engine were then run through the same two arms, and nine redded them: the revert clause
off, the attributable test off, the floor off, every record read LEGACY, the controls never
misreading, any fact upholding, an archive counted, a blank cutoff asked, and the slug match off.
The one survivor is an equivalent mutant: removing the witness-behind-base test leaves the verdict
`not-landed (i)` unchanged, because a witness at or behind its base has an empty `base..witness`
and nothing in it is attributable. The selftest suite and the gate legs are owed to the close.

**Evidences:** TOOL-dUnstuckLanding-15
- AC1 — `aborted_work_landed` — at HEAD eaf779cd, base `refs/remotes/origin/main` @ c2ffcf87, the
  report's JSON carries both signals; `aborted_work_landed` is live, value 8, `of` 12, the twelve
  LEGACY ABORTED records, four of them archives listed `landed (archived)`, and every row carries a
  verdict. `discarded_work_landed` reads DEAD, naming the empty post-cutoff population, since gov's
  HANDOFF_CUTOFF is 2026-10-05. The library's own `check_work_landed` and `read_first_commit_date`,
  sourced in bash against the same tip, agreed on all twelve verdicts and dates.
- AC2 — `python tools/drift-audit/drift_report.py --check` — on the arm's fixture, with both signals
  non-zero and `gateable` false, it exited 0.
- AC3 — `test_aborted_work_landed` — the witness-equals-base, foreign-witness and merged-then-reverted
  records read `not-landed (i)`, `not-landed (i)` and `not-landed (iii)`, uncounted; the positive read
  `landed`, counted once. An upheld fact moved it to `settled`; a fact naming another witness left it
  counted; the fact on the foreign record read `fact-not-upheld`; rotated, it read `landed (archived)`
  and the value fell to 0.
- AC4 — `aborted_work_landed` — read against the `unreverted` ref, the tip before the revert, the
  merged-then-reverted record read `landed` and the value rose from 1 to 2.
- AC5 — `discarded_work_landed` — the record first committed after the fixture's cutoff counted there
  and not in `aborted_work_landed`, and an upheld fact did not clear it. With the cutoff blank it read
  LEGACY, counted in `aborted_work_landed` with the note naming the blank key, and
  `discarded_work_landed` read NOT ASKED.
- AC6 — `_WORK_LANDED_CONTROLS` — four landed fact sets read both signals DEAD, the note naming
  `witness-equals-base`; the positive control pointed at reverted work read both DEAD naming
  `merged-not-reverted`; the shipped controls restored read live.
- AC7 — `.unattended.conf` — a fixture with neither it nor a run record read both NOT ASKED; with it
  committed and only a LANDED record, both read DEAD naming the empty ABORTED population.
- AC8 — `test_work_landed_matches_the_driver` — the library was sourced from the path derived from
  this kit's directory; all seven fixture records, the archive and the floored live record among them,
  read the same verdict and date in both, the archive dated 2026-01-10 by its first add and the live
  `RUN.md` floored at 2026-01-20. A verdict flipped by hand read unequal, and the floor turned off
  in the engine redded the arm.
- AC9 — `read_aborted_verdicts` — three ABORTED records cost ten git calls and six cost sixteen: four
  shared and two per record; fifty unrelated commits on the base ref moved neither count.
- AC10 — `grep -c "_work_landed" tools/drift-audit/README.md` — it counted 2, one row per signal, and
  `drift_signals.py` pins `aborted_work_landed` at 8, which the table reads `ok (pin 8, drain it)`.
- AC11 — `--settle` — a mirror of this repository with its `main` set to c2ffcf87, cloned and checked
  out at eaf779cd with this unit's engine copied in: `--settle` on each of the eight listed slugs
  staged `work-landed-at`, one commit took all eight, and `aborted_work_landed` then read 0 of 12,
  each formerly counted row `settled`.
