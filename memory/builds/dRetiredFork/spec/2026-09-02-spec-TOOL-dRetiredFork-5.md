# TOOL-dRetiredFork-5 — four codebase-map selftest arms stop being stamped ok

**Status:** OPEN · rev-2 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

Close the green-by-absence hole inCMS found in gov's own harness and filed as
`ABL-aFerriedToolkit-4`, which gov has not taken. Four guarded arms in
`tools/codebase-map/selftest.py` print an honest "NOT a pass" line when their guard is unmet and are
then stamped `ok` on the next line, so the suite reports coverage it does not have. This is the
class `AGENTS.md` §7 names — a skip that looks like a pass — inside the kit's own proof.

## 2. Scope (IN)

- **S1** — Each guarded arm records a `skipped` outcome instead of `ok`, naming the arm and the
  unmet guard. There are TWO guarded arms, not four: `test_identifier_tokens_corpus_recall`
  (`tools/codebase-map/selftest.py:1165`) and `test_js_probe_against_the_lexicon` (`:1226`). rev-1's
  "four" counted guard EXITS — `:1186`, `:1194`, `:1218` and `:1246` — and the suite's other 24
  `test_*` functions are unconditional.
- **S2** — The suite's summary line reports executed and skipped separately. The refusal predicate
  is that every GUARDED arm skipped is a refusal, not that every arm skipped is — 24 of 26 arms are
  unconditional, so "all skipped" is unreachable and a predicate keyed on it would be dead code the
  moment it landed, which is the could-not-fail shape this unit exists to close.
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
- **AC2** — When BOTH guarded arms are skipped, `python tools/codebase-map/selftest.py` exits
  non-zero naming the vacuity, and the RED is observed by unsetting both guards' preconditions. Observed via `python tools/codebase-map/selftest.py`.
- **AC3** — When every guard is met, the command exits `0` and its executed count is unchanged from
  the pre-change run.
- **AC4** — After the bump, `python tools/codebase-map/gen_map.py --check` and
  `bash tools/check-kit-versions.sh` both exit `0`.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map kit selftest` · `kit version markers` · `testsuite counts (every bar self-test prints one)`.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding H10. rev-1's "four guarded arms" counted guard exits; the suite
  has two guarded arms and 24 unconditional ones, so its "every arm skipped" refusal was unreachable
  and AC2 unobservable. S1, S2 and AC2 are restated against the arm count.
