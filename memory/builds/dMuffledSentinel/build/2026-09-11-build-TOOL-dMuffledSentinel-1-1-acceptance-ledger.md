# Acceptance ledger — TOOL-dMuffledSentinel-1

**Serves:** journal TOOL-dMuffledSentinel-1

Tier-1 · node d · 2026-09-11

## Where it was found

In inCMS, whose vendored copy of this engine sits unwired beside a forked hygiene gate. Its forked
`gen_build_index.py` had no `--print-bindings`, and `python scripts/gen_build_index.py --print-bindings`
exited 2 with a one-line usage message. Over its 1531 records, check 21 printed only the
`RECORD_UNBOUND_PIN is undeclared` branch. Once the fork gained the mode, the same check named 1485
records with no conformant Serves line, 7 undefined ids and 46 unqualified names. None of those
could have surfaced before.

## The criteria

**Evidences:** TOOL-dMuffledSentinel-1

- AC1 — MET, OBSERVED — the exit-2 stub arm in `tools/memory-tree/check-memory-hygiene.test.sh`
  passes, and the fixture's no-Serves record stays unnamed in the same run, which shows the stub
  was what check 21 read.
- AC2 — MET, OBSERVED — the exit-0 stub, printing a `--check`-shaped summary and no `N` row, is
  refused by the same branch.
- AC3 — MET, OBSERVED — the healthy fixture's run carries no refusal line.
- AC4 — MET, OBSERVED BY STAGED BREAK — with the engine restored to `75b85708` and the new suite
  kept, the suite exits 1 on exactly two lines, both `check 21 did not report: the bindings parse
  did not complete`, one per stub. Every other arm passed. With the fix back it is
  `PASS (374 assertions)`.
- AC5 — MET — `check-arms.py --check` exits 0, and `--report` lists check 21 branch 1 at line 842
  as ARMED.
- AC6 — MET — `check-verdict-epoch.sh 75b85708` reports the range clean once the engine change and
  the 2.69 bump are committed together; before the commit it could only report the base.

## Residue

- **`pass-order history` reds on this unit, and that is true.** The spec was written after the code
  and both landed in `a3b4ca1e`, so at its parent `75b85708` no spec for the id exists. The leg only
  saw it once the unit went CLOSED. It is neither waived nor rewritten into a spec-first order: the
  waiver registry exists for units already landed, and a reordered branch would state an authoring
  order that did not happen. Whether to land it under a waiver is the owner's decision.
- The same full bar reds `python resolver` on `tools/run-gates/run-gates.evidence.test.sh:643`, which
  is on `origin/main` since `d4c05068` and blocks any push until someone fixes it.
- The inCMS copy of the engine keeps the swallow until its next pull, which that repo tracks as
  `ABL-dMuffledSentinel-1`.
