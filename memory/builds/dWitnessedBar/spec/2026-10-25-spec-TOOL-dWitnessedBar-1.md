# TOOL-dWitnessedBar-1 — gate health measured and the reliability bar

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 23 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0339@8e7bc7ae whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-1-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-1-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-2-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-2-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-3-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-3-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-4-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-4-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |

<!-- /gen:spec-records -->

## 1. Goal

Measure gate health from the flake records and derive the reliability bar `verdict.flakes.entry`'s
`measured` value stands for. Once every leg of the bar has 30 verdicts in the flake records, the
threshold is one more than the 90th percentile, across the bar's legs, of each leg's flakes in its
last ten verdicts; it is re-derived at each gate-health measurement and written to the gate-health
record with the verdicts it came from, which `test.flakes` reads, 2 in 10 holding until the record
holds one. Today nothing measures a flake rate and no catch history is committed (gap-test-10).

## 2. Scope (IN)

- **S1** — The measurement, `measure_gate_health(ctx)` in `tools/drift-audit/drift_report.py`, a
  sibling of `measure_legs_retried_after_timeout` (`:3126`) appended to `SIGNALS` (`:3521`): it reads
  every tracked flake record (`TOOL-dWitnessedBar-8` S3) through PLAY-dOrderedCharter-7 S7's
  `build_records.py read`, counts each bar leg's verdicts and its flakes in its last ten, and reports
  the signal `gate_health` with the derived threshold, the legs armed and the legs short of 30.
  Observed by AC1 and AC3.
- **S2** — The bar's legs: every leg of `tools/gate-legs.json` that the kit hold does not hold, the
  legs a default bar runs (§8 F1); the measurement is armed only when each has at least 30 rows, and
  prints `unarmed` naming each short leg and its count otherwise. Observed by AC3.
- **S3** — The rule: with `c` the list of each bar leg's flakes in its last ten verdicts, sorted
  ascending, `p90 = c[ceil(0.9 × len(c)) − 1]` (nearest rank), and the threshold is `p90 + 1` in 10,
  written `<count>/10`. Observed by AC1 and AC2.
- **S4** — The gate-health record: a record kind `gate-health` of S7's factory, named
  `<date>-build-<unit id>-gate-health-<n>.md`, with required fields `Measured` (`<count>/10`, shared
  interface I12), `Verdicts` (the run ids of every flake record the measurement read) and `Legs`
  (`<armed>/<bar legs>`), written by `python tools/drift-audit/drift_report.py --gate-health --write
  --build <slug> --unit <id>` at each armed measurement and never while unarmed. Observed by AC4.
- **S5** — The measurement's moment: `verdict_flow.py flakes` (`TOOL-dWitnessedBar-8` S4) runs it with
  `--write` for its own build and unit right after writing its flake record, so each new verdict
  re-derives the threshold; a plain drift report reads it and writes nothing. Observed by AC4.
- **S6** — The reader's red case: `verdict_flow.py flakes --check` (`TOOL-dWitnessedBar-8` S7) gains
  the fixture `measured-check`, a planted hold at 2 in 10 made after the record held a higher measured
  threshold. Observed by AC5.

## 3. Non-goals (OUT)

- The flake record, the window, the hold and its check: `TOOL-dWitnessedBar-8`'s. This unit writes
  the record that unit's `measured` reads, and adds one fixture to its check.
- A window other than ten for `measured`: the clause fixes "its last ten verdicts"; a declared
  `<count>/<window>` value of `verdict.flakes.entry` bypasses the measurement entirely.
- A catch field on bug classes or a gate's price (gap-test-10's wider half): the flake records are
  the committed history this measurement needs; pricing a gate is observability's.
- Observability's Maintain detectors (layer-flow names "gate health" one): the cadence that would run
  this measurement on a schedule is dTendedCadence's, the hand-over being that it calls the same
  `--gate-health --write`.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-8` — `record-kind.flake`, the records whose rows this measurement counts, and the `flakes` verb and `flakes --check` it hooks into
- **consumes-from** external — PLAY-dOrderedCharter-7 S7's record factory, where the `gate-health` kind is registered

## 4. Design

### Evidence

- `measure_legs_retried_after_timeout` (`drift_report.py:3126-3170`) reads every run record's
  `verdict` under every git dir of the clone and returns one signal dict with `value`, `of`,
  `gateable`, `live` and a `detail` list; `SIGNALS` (`:3521-3538`) runs each per report.
- Run records are kept five per git dir and never committed; the flake records of
  `TOOL-dWitnessedBar-8` are committed, one per Test-step verdict, a row per executed leg.
- The manifest holds 142 legs at `cdfbd1cf`, and the kit hold (subject `kit` or chunk `selftests`)
  holds the self-test class, which runs only on request (`tools/run-gates/run-gates.sh:3129`).
  PINNED, measured 2026-10-25; the measurement re-derives both from the manifest it reads.
- v2's `verdict.flakes.entry` row: `measured` holds at 2 in 10 until every leg of the bar has 30
  verdicts in the flake records, then at the threshold this unit derives (v2:1274).

### The signal

```python
def measure_gate_health(ctx) -> dict:
    """`gate_health`: the reliability bar derived from the flake records, or `unarmed` naming each
    bar leg short of 30 verdicts."""
    # rows: {leg: [(ended, first_rc, rerun_rc), ...]} from every tracked *-flake-*.md
    # bar:  manifest legs whose row the kit hold does not hold
    # armed  <=> every leg of bar has len(rows[leg]) >= 30
    # flakes(leg) = count of first != 0 and rerun == 0 in its newest ten rows
    # value = p90(sorted(flakes(leg) for leg in bar)) + 1
```

It returns `{"signal": "gate_health", "value": <count or None>, "of": <bar legs>, "armed":
<legs at 30>, "gateable": False, "live": <armed>, "detail": [<per-leg verdicts and flakes>]}`, with
`value` None and a `why` naming the short legs while unarmed, so a report never reads an unarmed
measurement as a zero.

### The record

```
# gate-health record — <slug>

**Serves:** gate-health <unit id>

- **Measured:** <count>/10
- **Verdicts:** <run id> <run id> …
- **Legs:** <armed>/<bar legs>
```

`TOOL-dWitnessedBar-8` reads the newest record by date and `<n>` and takes `Measured`. Each armed
measurement writes one, so the record in force at any date is the newest one dated on or before it,
which is what `flakes --check` reads for a hold's filing date.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `measure_gate_health` | function | `py.function`, asked at the pass |
| `gate_health` | drift signal | none |
| `--gate-health`, `--write`, `--build`, `--unit` | drift CLI flags | none |
| `gate-health` | record kind of S7's factory | none |
| `measured-check` | fixture case of `flakes --check` | none |

### Migration

Additive. Until every bar leg has 30 verdicts the signal reads `unarmed` and no record is written,
so `test.flakes` holds at 2 in 10, as v2 states.

### Rollout

Live at landing; it arms itself on the thirtieth Test-step verdict of the slowest bar leg.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/README.md`
- `tools/drift-audit/selftest.py`
- `tools/memory-tree/build_records.py`
- `tools/run-gates/verdict_flow.py`

### Alternatives rejected

- **A run-gates verb for the measurement.** The bar would read committed records under the memory
  root on its own path; drift already measures the bar's records and is the named sibling.
- **Writing only when the value changes.** The clause writes the threshold "with the verdicts it came
  from", and those change at every measurement.

## 5. Production-readiness checklist

- security — read-only over committed records, one write through the record factory into the
  calling build's folder.
- perf / scale — one pass over every flake record per measurement; one small file per Test-step
  verdict, so linear in Test steps.
- error / empty / loading states — no flake records, or a bar leg short of 30, reads `unarmed` with
  the short legs named, never a value; a malformed record is reported by the factory's reader and
  skipped, said in `detail`.
- observability — the `gate_health` signal on every drift report, and the record's `Verdicts`.
- risks — the measurement arms late where a guarded bar leg rarely runs; `unarmed` names it, so the
  wait is visible rather than silent.
- testing — the fixtures of §6; the drift suite's arm of §7 at the close.
- migration — additive, as §4 says.
- user docs — none owed under `help/`: no help page describes drift signals; the drift README's
  signal table gains the row.

## 6. Acceptance criteria

- **AC1** — When `python drift_report.py --gate-health --fixture differs` runs in
  `tools/drift-audit/`, over planted flake records of ten bar legs with 30 verdicts each whose
  flakes in their last ten are eight 0s and two 3s, it prints `measured 4/10` and names the 30 run
  ids it read.
  Red when: the percentile is taken over all rows rather than per leg, or the threshold is the
  percentile without the one added.
  figure: 4/10 is DERIVED from the fixture by S3's rule.
- **AC2** — When `python drift_report.py --gate-health --fixture lower` runs, over records where
  nine legs never flaked and one flaked once in its last ten, it prints `measured 1/10`, and
  `verdict_flow.py --fixture flakes-window` (`TOOL-dWitnessedBar-8` AC4) run over the same records
  with that record holds the one-flake leg, which 2 in 10 would not hold.
  Red when: the leg is not held, so `test.flakes` still reads 2 in 10 beside a measured record.
- **AC3** — When `python drift_report.py --gate-health --fixture short` runs, over records where one
  bar leg has 29 verdicts, it prints `unarmed` naming that leg and `29/30`, and writes no record; a
  leg the kit hold holds, with no row at all, is not named.
  Red when: an unarmed measurement prints a value, or a held kit leg keeps it unarmed forever.
- **AC4** — When `python drift_report.py --gate-health --write --build <slug> --unit <id>` runs in a
  fixture repository holding armed records, it writes one `<date>-build-<id>-gate-health-1.md` whose
  `Measured`, `Verdicts` and `Legs` fields `build_records.py read` reports well formed; run again
  unarmed, it writes nothing; and `grep -n 'gate-health' verdict_flow.py` in `tools/run-gates/`
  names the call `flakes` makes after its record.
  Red when: an unarmed run writes a record, or `flakes` never triggers the measurement.
- **AC5** — When `python verdict_flow.py flakes --check` runs over the `measured-check` fixture, a
  gate-health record reading `3/10` dated before an OPEN held-flaky-leg ask whose leg had 2 flakes
  in its window, it exits 1 naming the leg, `2` and `3/10`; with the record dated after the ask it
  exits 0.
  Red when: a `test.flakes` that holds at 2 in 10 once the record holds a measured threshold passes
  the check (the clause's planted red).

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `run-gates canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 · `test_gate_health` over the three planted record sets, the short set staged by deleting one row of one leg · `CHECK_FLOOR` raised by the arm's counted checks

## 8. Open questions

- **F1 — Which legs are "every leg of the bar"?** Options: (a) the manifest legs the kit hold does
  not hold; (b) every manifest leg; (c) every leg the flake records name. (b) never arms where the
  self-test class runs only on request, an unmovable probe; (c) arms on one leg and reads a bar of
  one. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3: the legs a default bar runs, the only
  option that both arms and covers the bar; a held kit leg that executes still adds rows and flakes.
  widens: none · relaxes: none
- **FACT-QUESTION · F2 — Which percentile method?** Probe: the clause's text and v2:1274, read
  2026-10-25. Observation: both say "the 90th percentile, across the bar's legs" and name no method.
  Liveness: a method named in either would be quoted here. RESOLVED (agent, 2026-10-25, delegated):
  nearest rank, the one method whose value is always a count some leg actually has, rung 2. widens:
  none · relaxes: none
- **F3 — Where does the measurement live?** Options: (a) a drift signal with a `--gate-health` verb;
  (b) a run-gates verb; (c) inside `verdict_flow.py`. (b) and (c) put a report over committed records
  on the bar's path; the clause and scout A name drift's sibling. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 1, the brief's unit row. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 1, the brief's I12, scout A's row for
  cl-0339, v2's `verdict.flakes.entry` row, and the drift report read at base `cdfbd1cf`.

## 10. Reuse audit

The seam extended is drift's per-signal measurement, `measure_legs_retried_after_timeout`
(`tools/drift-audit/drift_report.py:3126`) and the `SIGNALS` list (`:3521`), whose dict shape the new
signal returns; the records are read and written through PLAY-dOrderedCharter-7 S7's factory. `python
tools/codebase-map/reuse_lookup.py "measure each leg's flake rate across verdict records and derive a
threshold"` ranked `measure_typed_counts` (`tools/codebase-map/map_lib.py`, a map count), the
deviation and runlog record readers, and generic `leg` stems; none derives a rate from per-leg rows,
so the measurement is new code in the named sibling's shape. The recall probe returned scout A's row
for this unit, which agrees with source on `:3126`, the brief's rows for this unit and
`TOOL-dWitnessedBar-8`, and the night-pass instrument that wrote the clause's text into v2; none names a
percentile method, which §8 F2 records.

Recall terms used: `python tools/memory-recall/query.py "how is gate health measured and the flake entry threshold derived" --terms "gate health measured threshold flake record percentile verdicts drift signal verdict.flakes.entry test.flakes"`
