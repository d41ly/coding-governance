**Serves:** journal DEPL-dGaugedVintage-9

# Acceptance ledger — DEPL-dGaugedVintage-9, the version delta

**Evidences:** DEPL-dGaugedVintage-9

- AC1 — `python tools/govkit/selftest.py` — with every row's `version` set to `STALE-SENTINEL`,
  `update --write` refreshes it, and the refreshed value is the constant's source line. `sha256` and
  `commit` move with it, so the three stay one fact.
- AC2 — `git show HEAD:tools/govkit/govkit.py` — RED OBSERVED. The same three arms run against the
  pre-fix engine: two FAIL with the stored value still reading `["STALE-SENTINEL", "STALE-SENTINEL"]`
  while `sha256` and `commit` moved. That is aTetheredConvoy round-3 F6, reproduced.
- AC3 — `python tools/govkit/govkit.py update --target C:/projects/incms/main` — a level entry is
  printed as `level`, not omitted: five of fifteen read level against the live adopter.
- AC4 — `python tools/govkit/govkit.py update --target C:/projects/incms/main` — `gate-lint` and
  `push-main` report `none declared — no comparison is possible`, and `(govkit)` reports the gov-side
  `unresolvable`. None is collapsed into level.
- AC5 — amended rev-3 — the absent-key state is implemented and reported as "this receipt predates
  the version field", but no receipt in reach carries a row without the key, so it is UNOBSERVED.
  Recorded rather than claimed.
- AC6 — `git status --short` — empty in the target after a read-only run; the report is printed
  before the `if not write` return and writes nothing.

## What this ledger does not claim

The comparison is EQUALITY on an extracted version number, never ordering: it says stored and gov
differ, not which is newer. A row refreshed before S1 landed reads as whatever it stores and may be
stale — §8 F3 records why detecting that needs a schema bump this unit did not take.

## The report reproduces the inbound audit's headline mechanically

Against the live adopter it prints `drift-audit DIFFERS — stored 1.7, gov has 1.8` and
`unattended DIFFERS — stored 1.12, gov has 1.14`. Those are exactly the two kits the inCMS document
identified by hand as having a genuine upstream release, and `memory-tree 2.50 → 2.52` is the kit it
called unpinnable. One command, no lenses.
