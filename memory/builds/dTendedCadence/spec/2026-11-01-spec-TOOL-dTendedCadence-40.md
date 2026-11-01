# TOOL-dTendedCadence-40 — the `dead-path carriers` leg judges its served-text record as gateable, while the report's copy stays report-only

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 11 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 14 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH (re-graded from medium by the skeptic), item H5. Unit 7 S2 builds the `dead_paths_in_served_text`
record with `gateable` false, "so `drift_report.py --check` gates nothing of it" (spec-7 :56-57),
while S3 calls the same record "its one gateable signal at bound 0, so the exit is 1". Unit 18's
`run_signal_leg` returns 1 only "when a gateable record is over or dead" (spec-18 S1). Built as S2
says, the kept merge-bar leg `dead-path carriers (deleted files still named)` can never red. This unit
states the split: the leg judges the record as gateable, and the copy `SIGNALS` emits stays
report-only.

## 2. Scope (IN)

- **S1** — The leg's record. `python dead_pointers.py --leg` in `tools/drift-audit/dead_pointers.py`
  hands `run_signal_leg` the served-text record with `gateable` set true, a copy built at the call,
  `dict(record, gateable=True)`; the auto-memory record is handed as `measure` returns it, report-only.
  Observed by AC1 and AC2.
- **S2** — The report's record. `measure_dead_text_pointers` keeps returning `gateable` false, so the
  `SIGNALS` entry `drift_report.py --check` reads gates nothing of it, and the one gate on served text
  stays the kept leg. Observed by AC3.
- **S3** — Unit 7 S2's sentence is read with S1 and S2 as the split it states: false in the report,
  true in the leg. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- `run_signal_leg` itself: TOOL-dTendedCadence-18 S1, unchanged.
- A selftest arm over every `run_signal_leg` caller requiring exit 1 on one planted offender: the
  report's left-shift gate, a class gate over units 15, 18 and this one's callers and a separate
  mechanism; it is not built here.

### Edges

- **consumes-from** `TOOL-dTendedCadence-7` — `dead_pointers.py`, its `--leg` mode and `measure_dead_text_pointers`, whose record this unit hands the leg factory as gateable

## 4. Design

### Evidence

- Spec-7 S2 (:56-57) sets `gateable` false; S3 relies on it gateable; S4 keeps the leg's name, its
  `reads`, `chunk`, `subject` and `ceiling` (`tools/gate-legs.json:1367-1377`) with argv
  `dead_pointers.py --leg`.
- Spec-18 S1: `run_signal_leg` exits 1 only on a gateable record over or dead.

### Inventory

Minted: nothing.

### Files touched (estimate)

- `tools/drift-audit/dead_pointers.py`: S1, S2
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **Mark the `SIGNALS` copy gateable.** Then `drift_report.py --check` gates the record inside
  `drift-audit records` as well, and one carrier reds two legs.

## 5. Production-readiness checklist

- security — N/A — no write path; the leg reads the tree.
- perf / scale — N/A — one dict copy per leg run.
- error / empty / loading states — a `not asked` population under `--leg` stays unit 7 S3's exit 2;
  a dead probe exits 1 as a gateable dead record does.
- observability — the leg's line is `run_signal_leg`'s, unchanged.
- risks — the copy and the original differ by one field; S2's criterion pins the original.
- testing — the criteria of §6.
- migration — N/A — the module is new in this build.
- user docs — N/A — the leg is gov-only.

## 6. Acceptance criteria

- **AC1** — When `python dead_pointers.py --leg` runs in a fixture holding one served-text carrier
  that names a deleted file, it prints the record `over` and exits 1.
  Red when: the leg exits 0 on a standing carrier.
- **AC2** — When the carrier is removed from the fixture, `python dead_pointers.py --leg` exits 0;
  with a planted stale waiver row it exits 1.
  Red when: a clean fixture reds, or a stale waiver passes.
- **AC3** — When `python drift_report.py --check` runs over the AC1 fixture, its
  `dead_paths_in_served_text` line reads `(report only)` and that record sets no exit.
  Red when: the report's copy gates.

## 7. Gates

`drift-audit selftest` · `dead-path carriers (deleted files still named)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 · one planted carrier, its removal and a stale waiver, staged against a leg handed the report-only record · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 14 (HIGH, item H5) of the round-1 spec
  audit.

## 10. Reuse audit

The seam extended is unit 7's `dead_pointers.py --leg` and unit 18's `run_signal_leg`, called
unchanged. `python tools/codebase-map/reuse_lookup.py "validate a record key at the write boundary so
no key becomes a path"` and the other set probes named no gateable-flag seam; neither module exists at
base, so no existing seam fits beyond those two units' own.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
