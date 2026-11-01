# TOOL-dTendedCadence-43 — the red leg reads the newest committed period record, each record names its run kind, and `on-finding` writes the clean record that clears a standing one

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 8 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 40 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H8. Unit 15's leg counts the `over-pin:` lines of the newest committed maintenance record
of any run (spec-15 S4, :74-84). An event run reads only its event's rows yet writes a record
(spec-6:26-27, spec-8 S5), so one `default-branch-red` run greens the leg while period offenders
stand; and under `maintain.record-when: on-finding` a clean run writes nothing (spec-6 S6, :85-87),
so the leg stays red after the offenders clear. This unit makes each record name its run kind,
derived from its key, points the leg at the newest period record, and has `on-finding` write the
clean record that replaces a standing one.

## 2. Scope (IN)

- **S1** — The run kind. Each row of `RECORD_KEY_FAMILIES` (TOOL-dTendedCadence-35) carries its run
  kind: `daily`, `weekly` and `session` are `period`, `event` is `event`, `node` is `node`.
  Observed by AC1.
- **S2** — The field. `render_maintenance_record` writes a fourth `fields` line, `**Run:** <kind>`,
  after `**Read:**`, derived from the key's family and never passed by a caller; the
  `maintenance-record` row of `tools/memory-tree/record-kinds.toml` (unit 6 S8) names four fields, so
  the kind's `fields` form grades it. Observed by AC1.
- **S3** — The reader. `read_newest_record(root, run=None)` (unit 6 S7) takes an optional run kind:
  given one, it returns the newest committed record, by unit 15 F3's rule, whose `**Run:**` line
  equals it, and a record with no `**Run:**` line matches no kind. `python maintenance.py newest
  [--run <kind>]` is the same call. Observed by AC2.
- **S4** — The leg. `check_breach_record` (unit 15 S4) reads `read_newest_record(root, run="period")`;
  its dead-probe line names the kind, `no committed period maintenance-record under <home>`.
  Observed by AC3.
- **S5** — The clean record. Under `on-finding`, a run with no finding still writes its record when
  the newest committed record of its own run kind carries one or more `over-pin:` lines, and prints
  `maintenance — <key> · on-finding, clears <n> standing over-pin line(s)`. Observed by AC4.

## 3. Non-goals (OUT)

- Which readings reach an `over-pin:` line: TOOL-dTendedCadence-37.
- The node pass's records: under `every-node` they carry no `held` route (unit 16 S8), and the leg
  reads only `period`.
- A filter by line content (`carrying=`): id 28, TOOL-dTendedCadence-48.

### Edges

- **consumes-from** `TOOL-dTendedCadence-15` — `check_breach_record`, the leg this unit points at the period record
- **consumes-from** `TOOL-dTendedCadence-6` — `render_maintenance_record`, `read_newest_record`, `read_record_when` and the `maintenance-record` row, which this unit gives a run kind
- **consumes-from** `TOOL-dTendedCadence-35` — `RECORD_KEY_FAMILIES`, whose rows carry the run kind S1 adds
- **hands-off** `TOOL-dTendedCadence-39` — the run kind on each family and `read_newest_record`'s `run=` filter, which that unit's `security` family and base read take
- **hands-off** `TOOL-dTendedCadence-55` — `check_breach_record`'s period read and the clean-record rule, which that unit widens to each node's newest record (review id 2)
- **hands-off** `TOOL-dTendedCadence-59` — the leg's event records and the Files touched, which the minors batch repairs (review ids 38, 49)

## 4. Design

### Evidence

- Spec-6 §4 gives the record three `fields` lines, `**Key:**`, `**Base:**`, `**Read:**`, in that
  order, and `read_newest_record` returns the newest by unit 15 F3's rule.
- Spec-15 S4 reads that record "of any kind" and exits 1 above 0 lines; F3 settles "newest" as the
  newest first-parent commit of `HEAD` touching the home.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `**Run:**` | `fields` line of `maintenance-record` | none |
| `period`, `event`, `node` | run kinds | none |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S2, S3, S5
- `tools/drift-audit/maintain_file.py`: S4
- `tools/memory-tree/record-kinds.toml`: S2's row
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **A `--run` argument on `maintenance.py write`.** The caller would type a fact the key already
  determines, two spellings of one value.
- **The leg reads the newest record of each kind and sums.** An event record's lines are a subset read
  of the period's offenders, so summing double counts them.

## 5. Production-readiness checklist

- security — N/A — the write boundary is unchanged; one more line derived from an already-validated
  key.
- perf / scale — S3's filter walks the home's first-parent history once per call, the walk the
  unfiltered reader already does; S5 adds one such read per clean `on-finding` run.
- error / empty / loading states — no committed period record is the leg's dead probe, exit 1.
- observability — S5's line says why a clean run wrote.
- risks — records written before this unit carry no `**Run:**` line and match no kind; none is
  committed at base.
- testing — the criteria of §6.
- migration — N/A — the home is new in this build.
- user docs — `help/maintain.md`'s section "When a reading breaches its pin" says the leg reads the
  newest period record.

## 6. Acceptance criteria

- **AC1** — When `python maintenance.py write` runs with `--key 2026-11-01`, then
  `default-branch-red.0123456789ab`, then `2026-11-01.node-a`, each record's `**Run:**` line reads
  `period`, `event` and `node` in turn, fourth among its fields.
  Red when: a record names no kind, or a kind its key does not derive.
- **AC2** — When a scratch worktree commits a period record and then an event record, `python
  maintenance.py newest --run period` prints the period record's path and `newest` with no `--run`
  prints the event record's.
  Red when: the filter returns a record of another kind.
- **AC3** — When the same worktree's period record carries one `over-pin:` line and the later event
  record none, `python maintain_file.py leg` under `maintain.on-breach = "red-leg"` exits 1.
  Red when: a newer event record greens the leg while a period offender stands.
- **AC4** — When `on-finding` is planted and the newest committed period record carries one
  `over-pin:` line, a clean period run writes its record with no `over-pin:` line; once that record is
  committed, `python maintain_file.py leg` exits 0.
  Red when: the clean run writes nothing, so the leg stays red after the offender clears.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The registry's own leg, `record-kinds` (TOOL-dTotalRecall-1 S3), grades S2's row once that build
lands; it is not in the manifest at base, so it is named here in prose.

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 AC4 · committed period and event records in a scratch worktree and a clean `on-finding` run, staged against the reader of any kind · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 40 (HIGH, item H8) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (units 55 and 59); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are unit 6's `read_newest_record` and `render_maintenance_record`, unit 15's
`check_breach_record` and unit 35's family table, which gains a column rather than a second table.
`python tools/codebase-map/reuse_lookup.py "file a records-only intake so a written record is
committed and landed"` ranked `records`, `extract_records` and `read_records`
(`tools/memory-tree/deviation_join.py`, `tools/runlog/extract.py`), readers of other record kinds with
no run-kind filter, so no existing seam fits beyond unit 6's reader.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
