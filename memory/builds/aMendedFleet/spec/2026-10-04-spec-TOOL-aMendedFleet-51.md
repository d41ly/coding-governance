# TOOL-aMendedFleet-51 — report-only drift signals over a pin nobody drains print pinless, and `readme_mechanism_drift` reads live builds only

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 51

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Six report-only drift signals print `over pin` on every run and no ask cites any of them, so the
status column has trained its readers to skip it. Three of the six are drained by other units of
this build. This unit disposes of the other three: a signal that has no pin by design prints
`report only, no pin` instead of a fake `over pin 0`, the backlog watermark whose budget rationale
ended at the switch to builds mode becomes pinless the same way, and `readme_mechanism_drift` stops
grading CLOSED builds, where all of its 31 rows sit except 4, and its pin is re-seeded at what the
narrowed population measures.

## 2. Scope (IN)

- **S1** — PINLESS STATUS. In `tools/drift-audit/drift_report.py`, a signal record whose
  `tolerance` is `None` resolves to a `pin` of `None` unless the project layer's `PINS` declares
  one, and the human table prints `report only, no pin` for such a live record in place of an
  `over pin` or `ok` status. The `--json` output carries `null` for both fields. A gateable record never carries a
  `None` tolerance; the engine asserts that rather than comparing against it. Observed by AC1, AC4.
- **S2** — `build_lexicon_marginal_offense_rate` returns `"tolerance": None` on each of the four
  records it builds itself, which is what its docstring already says it is: no pin, nothing
  raisable. Its not-asked returns go through `_build_not_asked`, whose status line prints before any
  pin is read, and stay as they are. Observed by AC1.
- **S3** — `build_live_backlog_rows` returns `"tolerance": None` on its three return paths, and its
  pin and its ratchet row leave `tools/drift-audit/drift_signals.py`, because under
  `BACKLOG_MODE="builds"` the reading is every live ask, which rises with every ask filed, and the
  shard-rotation floor its watermark guarded no longer exists. Observed by AC1, AC4.
  **Readers:** by name: `tools/drift-audit/drift_report.py` reads the `live_backlog_rows_per_shard`
  key from `ctx.pins` in `build_live_backlog_rows`, and `tools/drift-audit/drift_signals.py` spells
  it in `PINS` and in `RATCHETS`. by value: the human status column of `drift_report.py`, which now
  prints `report only, no pin`; and `ratchet_findings`, which reads the ratchet row and loses it
  with the pin, so no weakening can be reported for a pin that no longer exists.
- **S4** — LIVE BUILDS ONLY. `build_readme_mechanism_drift` grades a build README only when at least
  one spec of that build carries a status token outside `_TERMINAL_STATUSES`, read from the
  `**Status:**` line of the spec text it already reads for the revision log, so no file is read
  twice. Its `of` becomes the count of README files of live builds. Observed by AC2, AC3.
- **S5** — The `readme_mechanism_drift` entry in `PINS` is re-seeded at the value the narrowed
  signal measures at the unit's commit, with the measurement and the narrowing written beside it.
  A lower number is a drain and owes no ratchet marker. Observed by AC2.
- **S6** — The drift-audit README says, beside the signal table, what `report only, no pin` means,
  and the `readme_mechanism_drift` row says it grades live builds only. Observed by AC5.
- **S7** — Self-test arms in `tools/drift-audit/selftest.py`: the `readme_mechanism_drift` fixture
  spec moves from CLOSED to INPROGRESS so its existing arms keep a live build to grade, and one arm
  flips it to CLOSED and asserts zero rows; one arm asserts a record with a `None` tolerance prints
  `report only, no pin` and serialises as `null`. NOT OBSERVED by a criterion here: the suite runs
  once at the close, and the arms are declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- The DEAD-for-N-readings rule. It needs the drift history that unit 48 writes, so it is a second
  mechanism; §8 F1 splits it into a unit the run adds.
- The three other over-pin report-only signals. `backlog_asks_unlabelled` is unit 15's re-armed
  pin, `run_records_nonterminal_but_merged` is unit 47's derived-LANDED fix, and
  `shrink_only_lists_not_shrinking` is unit 57's low-water grading.
- Sampling `readme_mechanism_drift`'s precision and retiring it below about 0.5, which the source
  synthesis suggests. Four rows are too few to measure today; a follow-up can.
- A per-signal "owner action" field. The source synthesis lists it under "do not build".
- Any change to what a gateable signal does, or to `--check` and `--offenders`.
- Bumping the drift-audit kit version. Many units of this build move the kit; the bump is owed once,
  at the close.

### Edges

- **hands-off** `TOOL-aMendedFleet-15` — the `backlog_asks_unlabelled` pin, the fourth over-pin
  report-only signal, which that unit re-arms.
- **hands-off** external — the DEAD-for-N rule, which §8 F1 moves to a unit the run adds.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `fee9f62b`, whose bytes under `tools/` equal base `7af5f564`'s.

- `python tools/drift-audit/drift_report.py` printed six report-only signals over their pin:
  `lexicon_marginal_offense_rate` 552 over pin 0, `shrink_only_lists_not_shrinking` 2 over 0,
  `live_backlog_rows_per_shard` 457 over 454, `readme_mechanism_drift` 31 over 19,
  `backlog_asks_unlabelled` 452 over 0 and `run_records_nonterminal_but_merged` 13 over 5. PINNED,
  measured 2026-10-04.
- Of the 31 `readme_mechanism_drift` rows, 27 sit in 12 builds whose every spec is CLOSED or WONTDO.
  The other 4 sit in `dScaffoldedMirror` (one DEFERRED spec) and `dScriptedRepeat` (one SPECCED
  spec), both listed in `memory/LIVE.md`. A scratch probe joined the detail rows to each build's
  spec status headers. PINNED, measured 2026-10-04; the source synthesis predicted 4.
- `build_lexicon_marginal_offense_rate` sets `"tolerance": 0` on all four return paths, and its
  docstring says the rate has no pin and nothing raisable.
- The renderer in `main` compares a report-only `value` against `pin` and prints
  `over pin <pin> (report only)` when it is larger, and `pin` falls back to `tolerance`.

### Disposition per over-pin signal

| Signal | Disposition | Owner |
|---|---|---|
| `lexicon_marginal_offense_rate` | pinless status, as its docstring states | this unit, S2 |
| `live_backlog_rows_per_shard` | pinless; its pin and ratchet row go | this unit, S3 |
| `readme_mechanism_drift` | live builds only, pin re-seeded | this unit, S4 and S5 |
| `backlog_asks_unlabelled` | shrink-only pin re-armed | unit 15 |
| `run_records_nonterminal_but_merged` | derived-LANDED rule | unit 47 |
| `shrink_only_lists_not_shrinking` | graded against its low-water mark | unit 57 |

### Inventory

No new definition. `report only, no pin` is a status string, not an identifier.

### Rollout

The selftest fixture for `readme_mechanism_drift` writes a CLOSED spec, so S4 alone would empty
every arm that grades it; S7 moves the fixture to INPROGRESS in the same commit. Unit 15 also writes
`PINS` and is ordered first; this unit rebases onto it.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`

### Alternatives rejected

- **Re-seed `live_backlog_rows_per_shard` at 457.** That is a raise earned by nothing, the move the
  ratchet row exists to make visible, and the next filed ask puts it over again.
- **Delete `live_backlog_rows_per_shard`.** The live ask count is still worth printing, and
  `TOOL-aRelaxedShard-4` records it as report-only on purpose; only its pin outlived its reason.
- **Read build liveness from `memory/LIVE.md`.** That is a generated file in another kit; the spec
  status lines are already in hand and `_TERMINAL_STATUSES` already sits in this file.

## 5. Production-readiness checklist

- security — N/A: no new input, no write path; the same files are read.
- perf / scale — no new read; S4 parses a line of text the builder already holds.
- error / empty / loading states — a build with no spec is not live and contributes nothing, as it
  did before; liveness of `readme_mechanism_drift` keeps its existing formula.
- observability — the status column stops printing a red-looking word nobody acts on, so an
  `over pin` that remains means something.
- risks — a CLOSED build whose README still names a revised mechanism is no longer reported; that
  record is frozen and the review found no row there worth acting on.
- testing — AC1 to AC5 here; the arms in S7.
- migration — N/A: report output only; nothing stored changes.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs at the worktree root, the rows for
  `lexicon_marginal_offense_rate` and `live_backlog_rows_per_shard` print `report only, no pin`.
  Red when: either still prints `over pin`.
- **AC2** — When `python tools/drift-audit/drift_report.py --json` runs, every
  `readme_mechanism_drift` detail row names a `build` that has a row in `memory/LIVE.md`, and the
  record's `value` is at most its `tolerance`, which equals the `PINS` entry in
  `tools/drift-audit/drift_signals.py`.
  Red when: a row names a build whose every spec is CLOSED or WONTDO.
  figure: DERIVED at observation time; the §4 probe read 4 rows.
- **AC3** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path, the one
  non-terminal spec status of `dScaffoldedMirror` is edited to CLOSED and
  `python tools/drift-audit/drift_report.py --json` runs, the `readme_mechanism_drift` value falls by
  the number of rows that build carried and no row names it.
  Red when: the CLOSED build's row is still reported.
- **AC4** — When `python tools/drift-audit/drift_report.py --json` runs, the two pinless records
  carry `"tolerance": null` and `"pin": null`, and `grep -c "live_backlog_rows_per_shard"
  tools/drift-audit/drift_signals.py` reports 0.
  Red when: a pinless record serialises a number, or the dropped pin is still declared.
- **AC5** — When `grep -n "report only, no pin" tools/drift-audit/README.md` runs, it hits the
  paragraph beside the signal table.
  Red when: the engine prints a status the README does not explain.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · the readme-drift fixture spec flipped to CLOSED reads zero rows, and a record with a `None` tolerance prints `report only, no pin` and serialises `null` · `CHECK_FLOOR` moves by the checks the arms add

## 8. Open questions

- **F1** — Is the rule that a report-only signal DEAD for N readings is retired or filed part of
  this mechanism?
  Options: build it here; split it out. It reads consecutive readings, which exist only once unit
  48's drift history does, and it acts on DEAD records rather than on over-pin ones.
  RESOLVED (agent, 2026-10-04, delegated): split — the DEAD-for-N rule moves to a new unit the run
  adds, after unit 48.
- **F2** — What happens to `live_backlog_rows_per_shard`, the one over-pin signal no unit drains?
  Options: re-seed at 457; delete the signal; keep it and make it pinless. Re-seeding is a silent
  raise; deleting loses a count `TOOL-aRelaxedShard-4` kept on purpose; the watermark's reason, a
  shard rotation floor, does not exist under builds mode.
  RESOLVED (agent, 2026-10-04, delegated): pinless, per S3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's items [#54], [#61] and [#62], and a probe
  of the drift report and the readme-drift rows at base.

## 10. Reuse audit

The seams extended are the renderer in `main` of `tools/drift-audit/drift_report.py`, the
`tolerance`-to-`pin` fallback beside it, `build_readme_mechanism_drift`'s own spec read, and
`_TERMINAL_STATUSES` in the same file. `python tools/codebase-map/reuse_lookup.py "print a
report-only drift signal without a pin label and restrict a signal to live builds"` returned only
name-stem neighbours such as `report` in the drift-audit selftest and `render_report` in two other
kits, none of which renders a drift status, so no existing seam fits outside the engine itself; the
scan names `.sh` as unscanned, and no shell file renders this table. Recall returned
`TOOL-aRelaxedShard-4`, which records the backlog count as report-only on purpose,
`TOOL-dScriptedRepeat-14`, the ask that shipped `readme_mechanism_drift` at 31 rows, and
`TOOL-aNumeralWarden-3`, why a pin raise needs a marker. Where the report and the tree disagree:
none on the counts; the report's six over-pin signals and 31-of-31 CLOSED rows were re-measured as
six and 27 of 31.

Recall terms used: `python tools/memory-recall/query.py "which report-only drift signals sit over
their pin and what should happen to them" --terms "drift-audit report-only over pin
readme_mechanism_drift lexicon_marginal_offense_rate live_backlog_rows_per_shard PINS RATCHETS
demote retire"`
