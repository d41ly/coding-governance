**Serves:** journal DEPL-dGaugedVintage-2

# Acceptance ledger — DEPL-dGaugedVintage-2, the status sweep

**Evidences:** DEPL-dGaugedVintage-2

- AC1 — `grep -c 'SPECCED' memory/backlog/DEPL.md` — no row in that shard leads with SPECCED any
  more. All fifteen `DEPL-dCarriedReceipt-1..15` rows were reconciled against their own spec status
  headers, measured one at a time: every one reads CLOSED, and the build itself reads CLOSED with 15
  units. The single remaining occurrence of the word is prose inside `-2`'s own row.
- AC2 — `memory/backlog/DEPL.md` — `DEPL-aFerriedDossier-1` is CLOSED by citation: `govkit adopt`
  (`DEPL-dCarriedReceipt-13`, spec CLOSED rev-8) writes the receipt an installed tree never had, and
  `WIRE-INTO-PROJECT.md` section 5b is the runbook. That row had outlived its own declared closer.
- AC3 — `memory/backlog/DEPL.md` — S3's answer is YES and is filed as `DEPL-dGaugedVintage-13`: the
  class is cheap to gate because the memory-tree kit already parses both sides, a backlog row's
  status token and a spec's status header. Recorded whether or not it is built, so a decision not to
  gate stays distinguishable from never having asked.
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` — exits 0 after the sweep, with the
  status-vocabulary check green over every edited row.

## What this sweep also closed, and why that matters

This build's OWN eleven rows were left OPEN while ten of its units were CLOSED — the identical defect
one build later, in the unit written to fix it. Ten are now CLOSED against their specs by the same
rule; `-2` closed last, after the sweep it describes; `-12` and `-13` stay OPEN because they are
follow-ups this build filed and did not build.

## What this ledger does not claim

Rows outside `DEPL-dCarriedReceipt-*`, `DEPL-aFerriedDossier-1` and this build's own were not
touched. `DEPL-aFerriedDossier-2` and `-3` stay OPEN: their asks are wider than any unit here.
