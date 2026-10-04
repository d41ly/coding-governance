# TOOL-aWindowedPass-1 — acceptance ledger

**Serves:** journal TOOL-aWindowedPass-1

Check 23 places each dispatch row's window on one topological walk of the run's range and counts an
undeclared write only when the pass's window overlapped another unit's. The observations below are
the main loop's, on a slice of `check-unattended.test.sh`: its prologue plus the check-23 block, the
generated-render arms and the new overlap arms, 32 arms at exit 0. The breaks were staged in the leg
with the overlap test bypassed, so every graded pass counted, and the leg was restored byte-identical
before commit c5582706. The real leg over this tree printed `graded 2 pass(es), 0 overlapped` for
this build and no check-23 failure.

**Evidences:** TOOL-aWindowedPass-1
- AC1 — `check 23 SOLO` — the solo-pass arm printed `check 23 SOLO ARCH-tRun-1 at` and no check 23
  FAILED; with the overlap test bypassed it printed FAILED and no SOLO line.
- AC2 — `check-unattended.sh` — the later-anchor sibling arm printed check 23 FAILED and no SOLO line;
  it held under the bypass too, as its red-when names anchor equality, not the bypass.
- AC3 — `0 overlapped` — the sequential arm printed `graded 2 pass(es), 0 overlapped a sibling` and a
  SOLO line; with the overlap test bypassed both were missing and check 23 FAILED appeared.
