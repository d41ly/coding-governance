**Serves:** journal DEPL-dGaugedVintage-13

# Acceptance ledger — DEPL-dGaugedVintage-13, the outliving-row signal

**Evidences:** DEPL-dGaugedVintage-13

- AC1 — `python tools/drift-audit/selftest.py` — a fixture spec at CLOSED whose backlog row reads
  OPEN is counted, and the detail names the id, the row's token and the spec's.
- AC2 — `python tools/drift-audit/selftest.py` — the same spec with a CLOSED row counts 0. Red and
  green over ONE subject, which is what makes the arm an assertion rather than a coincidence.
- AC3 — `python tools/drift-audit/selftest.py` — a CLOSED spec whose id appears in no backlog row is
  not counted: an id can be a unit without ever having been an ask.
- AC4 — `python tools/drift-audit/selftest.py` — the signal reports `live` from the terminal specs it
  actually examined, so a zero means it looked rather than that it could not move.
- AC5 — amended rev-2 — the RED is AC1/AC2's paired arms, not a reverted sweep. Logged in §9.
- AC6 — `python tools/drift-audit/drift_report.py` — exits 0 with
  `backlog_rows_outliving_closed_specs 27 / 376 ok (pin 27, drain it)`.

## What the signal found that nobody asked it to

27 rows across TOOL, PLAY and KICK whose specs read CLOSED while the row reads OPEN or SPECCED —
`TOOL-aBoundedVerdict-22`, `TOOL-aDeclaredCeiling-1..3`, `TOOL-aPromptedMandate-1` among them.
`DEPL-dGaugedVintage-2` swept the DEPL shard by hand and never saw these, because a hand sweep only
covers the shard somebody happened to open.

## What this ledger does not claim

The signal COUNTS; it does not refuse. A row's ask can be legitimately wider than the unit that
partly served it (`DEPL-dGaugedVintage-2` §8 F1), so the 27 are a residue to drain by judgement, not
27 defects. The pin is shrink-only and holds them.
