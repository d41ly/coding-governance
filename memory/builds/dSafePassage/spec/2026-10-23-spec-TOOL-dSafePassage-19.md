# TOOL-dSafePassage-19 — a rollback past the schema step stamps schema 3 with no `steps`, finishes its record, and converges after a kill

**Status:** CLOSED · rev-4 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-19-deviation-65.md](../build/2026-10-23-build-TOOL-dSafePassage-19-deviation-65.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-19-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-19-ledger.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-19-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-19-1-spec-writer.md) | research | — |
| [2026-10-26-prompt-TOOL-dSafePassage-19-2-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-19-2-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-19-3-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-19-3-spec-writer.md) | research | — |
| [2026-10-26-prompt-TOOL-dSafePassage-19-4-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-19-4-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-19-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-19-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 TOOL-dSafePassage-26 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

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

S1, S2's outcome and S3 already hold at HEAD, by TOOL-dSafePassage-4 (commit `264862061`) and
TOOL-dSafePassage-18, so this unit builds the two `rollback-update` plants, their `schema.block-after`
trigger, the `[dSP-19]` self-test rows that run them, and its acceptance ledger.

## 2. Scope (IN)

- **S1** — The re-read keeps no key the disk no longer holds. TOOL-dSafePassage-2's post-spawn re-read of
  `schema` and `steps` takes a key the receipt on disk no longer holds out of the in-memory receipt,
  so a `steps` list the down took out is not written back by any later write of the run. It holds at
  HEAD: `run_step_reread` pops each of `schema` and `steps` the disk lacks
  (`tools/govkit/upgrade_steps.py:985-989`). Observed by AC1.
- **S2** — The stamp. After the write loop of a `--rollback --write` run whose reverse walk ended
  below schema 4, the stamp sets `gov_commit` to `--to` (`tools/govkit/govkit.py:12723`) and keeps
  the schema the downs left, 3, since the rollback branch reads `receipt.get("schema", schema)` and
  never raises it (TOOL-dSafePassage-4 S5, `tools/govkit/govkit.py:12688-12689`). It adds no key and
  asks no predicate: the `steps` the schema step's down took out stays out because S1's re-read
  took it out of the in-memory receipt the stamp writes (`tools/govkit/govkit.py:12726`). It holds
  at HEAD. Observed by AC1.
- **S3** — The record. `write_rollback_record` (TOOL-dSafePassage-4 S6) names each down from the
  verdict list `TOOL-dSafePassage-18` returns, the schema step `rolled-back` among them, and finishes
  with `gov_commit: moved to <to8>`. It holds at HEAD. Observed by AC1.
- **S4** — A kill after the schema step's down has written schema 3 and before the write loop moves a
  file row. The receipt then reads schema 3, no `steps`, `gov_commit` unmoved, and the record reads
  `not finished` with no `down` line, since `write_rollback_record` rewrites it only when the run
  returns (TOOL-dSafePassage-4 S6, `tools/govkit/govkit.py:10443-10461` and `:12679-12732`). A re-run of the same
  `update --rollback --to <rev> --write` passes `check_rollback_vintage`, finds every reverse row
  recorded nowhere and witness-probes each (TOOL-dSafePassage-4 S4 move 1). None holds: each row the
  killed run downed went out with `steps`, each other row's down took away what its witness reads,
  and the schema step's witness exits 1 at schema 3 (`tools/govkit/steps/receipt_schema_4.py:71-75`).
  So `run_reverse_walk` returns every row `skipped (nothing applied)`
  (`tools/govkit/upgrade_steps.py:1143-1147`) and downs nothing. The run then moves the file rows,
  stamps and finishes the record. It converges on an uninterrupted run in the receipt's bytes, the
  target's bytes and the record's finished shape, and its `down` lines read
  `skipped (nothing applied)` where the uninterrupted run's read `rolled-back`, since no verdict of
  the killed run survives the kill. Observed by AC2.

## 3. Non-goals (OUT)

- The reverse walk's own records: `TOOL-dSafePassage-18`.
- How a down is judged reverted, which the fixture's synthetic rows decide by their witnesses:
  `TOOL-dSafePassage-17`.
- The release-0 rollback itself, which TOOL-dSafePassage-5's `upgrade-walk` leg observes.

### Edges

- **consumes-from** `TOOL-dSafePassage-2` — the post-spawn re-read of the receipt, which drops a key the disk no longer holds (S1); without it the run would write the dropped list back
- **consumes-from** `TOOL-dSafePassage-4` — `update --rollback`, `check_rollback_vintage`, the stamp under `--rollback`, `write_rollback_record` and the `rollback-update` fixture family; without them there is no run to finish
- **consumes-from** `TOOL-dSafePassage-16` — the predicate the reverse walk asks after each down, whose false answer at schema 3 leaves no row for the stamp to carry; this unit adds no call of it, and without it the walk would refuse at the writer
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

Minted, all fixture or self-test names: the `rollback-update` plants `schema-step` and
`schema-step-kill-before-stamp`, added to `ROLLBACK_UPDATE_PLANTS`
(`tools/govkit/upgrade_steps.py:1715`); the `schema.block-after` trigger, a branch of the
`os.replace` entry of `FIXTURE_SCHEMA_STEP_PLANTS` (`tools/govkit/upgrade_steps.py:1746-1759`) that
blocks the schema step's down after its rename, as `fx.py`'s `<slug>.block-after` blocks after its
first file; and the `[dSP-19]` tag on this unit's rows of `check_step_rollback`
(`tools/govkit/selftest.py:3558`). That function tags every plant starting `schema-step` `dSP-18`
(`tools/govkit/selftest.py:3611`), so the two rows are tagged `dSP-19` explicitly. No product
function, conf key, gate leg or policy key.

### Migration

None.

### Rollout

No product behaviour changes: S1 to S3 are live at HEAD, reached only through `--rollback`, and this
unit lands the plants and rows that observe them. It builds at order 3, after TOOL-dSafePassage-2,
TOOL-dSafePassage-4 and `TOOL-dSafePassage-16` (order 2), and within order 3 after
`TOOL-dSafePassage-18`, whose verdict list the record is written from.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py` — the two plants in `run_rollback_update_fixture`, which builds
  its gov with `schema3=True` for them, and the `schema.block-after` trigger
- `tools/govkit/selftest.py` — the `[dSP-19]` rows
- `memory/builds/dSafePassage/build/2026-10-26-build-TOOL-dSafePassage-19-ledger.md` — the
  acceptance ledger

### Alternatives rejected

- **The stamp writes `"steps": []` back.** A schema-3 receipt with the field is the foreign shape
  TOOL-dSafePassage-3's down normalises away, and the rollback would not be byte-identical with
  release-0, which TOOL-dSafePassage-5 asserts.
- **A receipt field recording the rollback.** TOOL-dSafePassage-4 §8 F1 refused it: the schema step's
  down removes any such field.
- **The stamp asks `test_steps_recordable` (rev-3's S2).** Each answer at the stamp breaks one
  section. Dropping `steps` where the predicate rejects would remove the stale list a broken re-read
  kept, so §7's staged break could never turn the arm red (charter [gate]). Refusing there is a
  refusal no section names. And the outcome is already HEAD's without the call.

## 5. Production-readiness checklist

- security: no new write path and no product change; the stamp is HEAD's.
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
- **AC2** — When the same family runs with `--plant schema-step-kill-before-stamp`, the fixture
  installs two targets from one scratch gov (`build_update_gov` takes several target names,
  `tools/govkit/upgrade_steps.py:2197-2205`), so both receipts name the same commits. It rolls the
  twin back uninterrupted, as AC1 does. It kills the other target's run after the schema step's down
  has written schema 3 and before the write loop moves a file row. The killed receipt reads schema 3,
  no `steps` and `gov_commit` unmoved, and the record reads `not finished` with no `down` line. The
  re-run exits 0, and these three things match the twin: (1) the receipt's bytes are equal, `carry`
  included; (2) the target's bytes are equal on every path outside `.git/` and `.governance/outbox/`;
  (3) the record has the finished shape: `finished` and no `not finished`, the twin's `files:` line,
  and `gov_commit: moved to <to8>`. Its `down` lines read `down fx/s1: skipped (nothing applied)`,
  then `down govkit/receipt-schema-4: skipped (nothing applied)`, where the twin's read `rolled-back`.
  That is because both rows went out with `steps` and neither witness still holds, so the re-run
  downs neither (S4). `carry` needs no exclusion here, unlike TOOL-dSafePassage-15 rev-2's AC4. The
  killed run moved no file row, so the re-run's write loop meets the same target bytes as the twin's,
  and it recomputes `carry` from them rather than reading it back (DEPL-dCarriedReceipt-9 S2,
  `tools/govkit/govkit.py:10164-10172`).
  Red when: the re-run refuses, downs a row a second time, leaves `gov_commit` unmoved or the record
  `not finished`, differs from the twin in the receipt's or the target's bytes, or prints a `down`
  line other than the two `skipped (nothing applied)` lines.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the self-test calls `upgrade_steps.py fixture rollback-update` with the plants `schema-step` and `schema-step-kill-before-stamp`, its failing case staged by a re-read that keeps a key the disk dropped · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 52 (HIGH, item
  D-3, shared with id 2).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-35`; no other section moved.
- rev-3 · 2026-10-26 · S4 · AC2 · the builder's DIVERGENCE hand-back (`wf_7efb05c8-043`): after the
  kill, the re-run skips both reverse rows, so its record's `down` lines can never equal AC1's
  `rolled-back`. AC2 now compares the receipt's bytes, the target's bytes and the record's finished
  shape against an uninterrupted twin from the same scratch gov. It requires the two
  `skipped (nothing applied)` lines and says why. The kill is placed before the write loop moves a
  file row, which is the builder's reading, so `carry` is compared too. By
  `2026-10-26-prompt-TOOL-dSafePassage-19-1-spec-writer.md`.
- rev-4 · 2026-10-26 · S1 · S2 · S3 · §1 · §3 · §4 · §5 · §10 · S2 asks no predicate. The stamp adds
  no key, and S1's re-read keeps the dropped `steps` out, so §7's staged break can still turn the arm
  red. §1 states that S1, S2's outcome and S3 hold at HEAD. §4's Inventory and Files touched shrink to
  the two plants, their `schema.block-after` trigger, the `[dSP-19]` rows and the ledger, and
  `govkit.py` leaves the estimate. The stamp's schema is cited as TOOL-dSafePassage-4 S5's
  `receipt.get("schema", schema)`, not TOOL-dSafePassage-3 S5's `max(schema, 3)`. The
  TOOL-dSafePassage-16 edge is reworded. By `2026-10-26-prompt-TOOL-dSafePassage-19-4-spec-writer.md`.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-4's `rollback-update` fixture family
(`run_rollback_update_fixture`), with `build_update_gov`'s `schema3` gov and the schema step's
fixture plants of TOOL-dSafePassage-15 (`FIXTURE_SCHEMA_STEP_PLANTS`), and TOOL-dSafePassage-4's
`check_step_rollback` self-test arm. The behaviour observed is TOOL-dSafePassage-4's rollback run
(its S5, S6 and §4 "The order of one rollback run") and TOOL-dSafePassage-2's post-spawn re-read
(its S3). `python tools/codebase-map/reuse_lookup.py "skip persisting a progress row
when the receipt schema is too old to hold it"` ranked `rows`, `row`, `skip` and `extract_row`,
name-token matches, so no existing seam fits beyond those specs. The stamp's own site is
`tools/govkit/govkit.py:12688-12689` at HEAD, the rollback branch TOOL-dSafePassage-4 S5 wrote.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
