# TOOL-aWindowedPass-5 — acceptance ledger

**Serves:** journal TOOL-aWindowedPass-5

Check 23 fails only the run this tree drives, on one counted write, and `UNDECLARED_WRITE_CEILING`
is retired. The observations are the main loop's, on a slice of `check-unattended.test.sh`: its
prologue plus the check-23 block, the overlap arms and the per-run block through the derived-LANDED
arms, 28 arms at exit 0. Two break runs over the per-run block followed, nine arms each, with the leg
restored byte-identical before commit 7ab7ae53. The real leg over this tree printed no check 22 or
check 23 failure.

**Evidences:** TOOL-aWindowedPass-5
- AC1 — `check-unattended.sh` — the bound-run arm exited 1 and printed the per-run failure naming
  `1 in memory/builds/tRun/RUN.md`; with the comparison staged against 1 instead of zero it printed
  neither.
- AC2 — `check 23 OTHER RUN` — from a detached HEAD the arm printed the OTHER RUN line naming a
  detached HEAD and no check 23 FAILED; with the binding staged to always match it printed FAILED and
  no OTHER RUN line.
- AC3 — `UNDECLARED_WRITE_CEILING="5"` — with that line in the fixture conf, check 22 did not fail and
  the report channel named the key RETIRED; with the retired-key filter staged out, check 22 FAILED.
- AC4 — `TOOL-aWindowedPass-5` — `--emit-ceiling` exited 2 naming this unit; staged to exit 0, the
  exit-code arm failed.
