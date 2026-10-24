# TOOL-dSafePassage-19 — a rollback past the schema step stamps schema 3 with no `steps`, finishes its record, and converges after a kill

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-19-deviation-65.md](../build/2026-10-23-build-TOOL-dSafePassage-19-deviation-65.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 TOOL-dSafePassage-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 52** at HIGH, merged with id 2 into its item **D-3**. TOOL-dSafePassage-4's §4
"Migration" (lines 173-174) says only that a rollback to before `govkit/receipt-schema-4` "ends with
that step's down", and no spec says how that run's last record is written, or what its stamp and
record hold, once the down has rewritten the receipt. The run ends as an error after it mutated the
tree, with the record and the stamp unspecified, so TOOL-dSafePassage-5's `down` case and its rollback
from a killed state cannot pass. This unit is id 52's promotion, the run's half of D-3: what
`update --rollback --write` does after a reverse walk whose last down lowered the receipt.
`TOOL-dSafePassage-18`, id 2's promotion, keeps the walk itself from writing the row.

## 2. Scope (IN)

- **S1** — The re-read drops what the disk dropped. TOOL-dSafePassage-2's post-spawn re-read of
  `schema` and `steps` takes a key the receipt on disk no longer holds out of the in-memory receipt,
  so a `steps` list the down removed is not written back by any later write of the run. Observed by
  AC1.
- **S2** — The stamp. After the write loop of a `--rollback --write` run whose reverse walk ended
  below schema 4, the stamp sets `gov_commit` to `--to`, keeps `schema` 3 (TOOL-dSafePassage-3 S5's
  `max(schema, 3)`) and writes no `steps` key, asking `test_steps_recordable` and adding nothing the
  predicate rejects. Observed by AC1.
- **S3** — The record. `write_rollback_record` (TOOL-dSafePassage-4 S6) names each down from the
  verdict list `TOOL-dSafePassage-18` returns, the schema step `rolled-back` among them, and finishes
  with `gov_commit: moved to <to8>`. Observed by AC1.
- **S4** — A kill after the schema step's down and before the stamp. The receipt then reads schema 3,
  no `steps`, `gov_commit` unmoved, and the record reads `not finished`. A re-run of the same
  `update --rollback --to <rev> --write` passes `check_rollback_vintage`, finds every reverse row
  recorded nowhere and witness-probes each (TOOL-dSafePassage-4 S4 move 1), skips those whose witness
  does not hold, moves the file rows, stamps and finishes the record, converging to the bytes of an
  uninterrupted run. Observed by AC2.

## 3. Non-goals (OUT)

- The reverse walk's own records: `TOOL-dSafePassage-18`.
- How a down is judged reverted, which the fixture's synthetic rows decide by their witnesses:
  `TOOL-dSafePassage-17`.
- The release-0 rollback itself, which TOOL-dSafePassage-5's `upgrade-walk` leg observes.

### Edges

- **consumes-from** `TOOL-dSafePassage-2` — the post-spawn re-read of the receipt, which S1 changes for a key the disk no longer holds; without it the run would write the dropped list back
- **consumes-from** `TOOL-dSafePassage-4` — `update --rollback`, `check_rollback_vintage`, the stamp under `--rollback`, `write_rollback_record` and the `rollback-update` fixture family; without them there is no run to finish
- **consumes-from** `TOOL-dSafePassage-16` — the predicate the stamp asks before it writes; without it the stamp would copy the writer's schema test
- **consumes-from** `TOOL-dSafePassage-18` — the verdict list the record is written from; without it the record cannot name a row the receipt no longer holds
- **hands-off** `TOOL-dSafePassage-5` — the rollback of the release-0 tree to release-0's digest, from a whole walk and from a killed one
- **hands-off** `TOOL-dSafePassage-35` — the minors batch of the round-1 audit of units 15 to 26, which adds the shipped-shape plant of the kill-before-stamp re-run and reads its second downs

## 4. Design

### Data model

The receipt a clean rollback to before the schema step leaves:

```json
{"schema": 3, "gov_source": "...", "gov_commit": "<--to>", "kits": ["..."], "files": ["..."]}
```

The record's last lines for that run:

```
down govkit/receipt-schema-4: rolled-back
files: wrote <n> · moved <n> · deleted <n> · withheld <n> · conflicts <n>
gov_commit: moved to <to8>
```

### Inventory

Minted: the `rollback-update` plants `schema-step` and `schema-step-kill-before-stamp`. No function,
conf key, gate leg or policy key.

### Migration

None.

### Rollout

Live at landing, reached only through `--rollback`. It builds at order 3, after TOOL-dSafePassage-2,
TOOL-dSafePassage-4 and `TOOL-dSafePassage-16` (order 2), and within order 3 after
`TOOL-dSafePassage-18`, whose verdict list it reads.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **The stamp writes `"steps": []` back.** A schema-3 receipt with the field is the foreign shape
  TOOL-dSafePassage-3's down normalises away, and the rollback would not be byte-identical with
  release-0, which TOOL-dSafePassage-5 asserts.
- **A receipt field recording the rollback.** TOOL-dSafePassage-4 §8 F1 refused it: the schema step's
  down removes any such field.

## 5. Production-readiness checklist

- security: no new write path; the stamp writes the keys it writes today, `steps` excepted.
- perf / scale: unchanged.
- error / empty / loading states: a killed run leaves a `not finished` record and a schema-3 receipt
  the re-run converges from.
- observability: the record names the schema step's down and the stamp's move.
- risks: a re-run whose witnesses misread a row as applied would down it again; downs tolerate their
  own absent state (TOOL-dSafePassage-4 S4), and `TOOL-dSafePassage-17` covers the witnesses that
  cannot be falsified.
- testing: the two plants, through the arm of §7.
- migration: none.
- user docs: N/A — the "Rolling back" section TOOL-dSafePassage-4 writes covers the record and the
  stamp.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant schema-step`
  runs, a scratch gov's `govkit.py update --target <t> --rollback --to A --write`, over a target
  installed at A at schema 3 and updated to B through the schema step, exits 0; the receipt reads
  `"schema": 3`, no `steps` key and `gov_commit` = A; and `update-reverted-<from8>-<to8>.md` names
  `down govkit/receipt-schema-4: rolled-back` and `gov_commit: moved to`.
  Red when: the run raises `Refusal` after the down, the receipt keeps a `steps` key, or the record
  is not finished.
- **AC2** — When the same family runs with `--plant schema-step-kill-before-stamp`, the fixture kills
  the run after the schema step's down and before the stamp; the receipt reads schema 3 with
  `gov_commit` unmoved and the record `not finished`, and the re-run exits 0 with the receipt and the
  record bytes, its times aside, equal to AC1's.
  Red when: the re-run refuses, downs a row a second time, or leaves `gov_commit` unmoved.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the self-test calls `upgrade_steps.py fixture rollback-update` with the plants `schema-step` and `schema-step-kill-before-stamp`, its failing case staged by a re-read that keeps a key the disk dropped · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 52 (HIGH, item
  D-3, shared with id 2).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-35`; no other section moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-4's rollback run (its S5, S6 and §4 "The order of one
rollback run") and TOOL-dSafePassage-2's post-spawn re-read (its S3), with the predicate of
`TOOL-dSafePassage-16`. `python tools/codebase-map/reuse_lookup.py "skip persisting a progress row
when the receipt schema is too old to hold it"` ranked `rows`, `row`, `skip` and `extract_row`,
name-token matches, so no existing seam fits beyond those specs; the stamp's own site is
`tools/govkit/govkit.py:12407` at the base, the line TOOL-dSafePassage-3 S5 caps.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
