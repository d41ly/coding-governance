# TOOL-dRetiredFork-5 — four codebase-map selftest arms stop being stamped ok

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close the green-by-absence hole inCMS found in gov's own harness and filed as
`ABL-aFerriedToolkit-4`, which gov has not taken. Four guarded arms in
`tools/codebase-map/selftest.py` print an honest "NOT a pass" line when their guard is unmet and are
then stamped `ok` on the next line, so the suite reports coverage it does not have. This is the
class `AGENTS.md` §7 names — a skip that looks like a pass — inside the kit's own proof.

## 2. Scope (IN)

- **S1** — Each of the four guarded arms records a `skipped` outcome instead of `ok`, naming the arm
  and the unmet guard.
- **S2** — The suite's summary line reports executed and skipped separately, and a run whose skip
  count equals its arm count REFUSES rather than passing.
- **S3** — Absorb the `encoding="utf-8"` fix on the corpus-recall `subprocess.run` that inCMS
  carries as its `KIT_CODEBASE_MAP_SELFTEST_DELTA`, if gov HEAD still lacks it. Verify before
  editing: the sibling fix in `drift_report.py` landed at `TOOL-aGradedDoorway-3`, and this row may
  already be stale.
- **S4** — Bump `KIT_CODEBASE_MAP_VERSION` with its paired markers, and run
  `python tools/codebase-map/gen_map.py --write` in the same landing, because the version rides
  `inventories.json`, `MAP.md` and `symbols.json` and the freshness gate byte-compares them.

## 3. Non-goals (OUT)

- Making the four guards satisfiable. Whether the guarded arms CAN run in gov's tree is a separate
  question; this unit makes the report honest, not the coverage complete.

## 6. Acceptance criteria

- **AC1** — When a guard is unmet, `python tools/codebase-map/selftest.py` prints that arm as
  `skipped` with the guard named, and no `ok` line for it.
- **AC2** — When every arm is skipped, the same command exits non-zero naming the vacuity. Observed via `python tools/codebase-map/selftest.py`.
- **AC3** — When every guard is met, the command exits `0` and its executed count is unchanged from
  the pre-change run.
- **AC4** — After the bump, `python tools/codebase-map/gen_map.py --check` and
  `bash tools/check-kit-versions.sh` both exit `0`.

## 7. Gates

`codebase-map freshness` · `codebase-map selftest` · `kit versions` · `testsuite counts`.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
