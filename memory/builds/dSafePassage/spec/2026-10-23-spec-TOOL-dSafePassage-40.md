# TOOL-dSafePassage-40 — the forward walk marks a row `via: witness` only when nothing records that its up ever ran

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-40-deviation-86.md](../build/2026-10-23-build-TOOL-dSafePassage-40-deviation-86.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-39 TOOL-dSafePassage-41 TOOL-dSafePassage-38 TOOL-dSafePassage-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 27 to 35
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`)
confirmed finding **id 29** at HIGH, its item **D-5**. TOOL-dSafePassage-33 S2 has move 1 pass
`via="witness"` whenever the witness holds, with no condition on a prior record. A walk killed after
the up's writes and before move 5 leaves the row `failed` with `interrupted:` (TOOL-dSafePassage-2 S2
move 3), an image written and never staged (move 5 alone stages, TOOL-dSafePassage-2 S11), and a
holding witness, since TOOL-dSafePassage-1 §4 writes the image first and the witness change last. The
re-run's move 1 then records `applied` with `via` `witness`, against TOOL-dSafePassage-33 S1's own
meaning, "its `up` never spawned". If that unstaged image is later lost, a rollback takes the no-image
rule, records `rolled-back` on the down's exit 0 and reports success while the up's writes remain:
the false `rolled-back` TOOL-dSafePassage-33 exists to prevent. This unit is id 29's promotion: the
mark is set only from evidence that no up ran.

## 2. Scope (IN)

- **S1** — The evidence. Move 1 of `run_step_walk` passes `via="witness"` only when the receipt the
  walk received, read before its first write, holds no record for the step, and no before-image
  exists at the row's image path (TOOL-dSafePassage-1 §4 "The before-image"). A row with any prior
  record, `failed` included, or with an image on disk, is recorded `applied` with no `via`.
  Observed by AC1 and AC3.
- **S2** — The plant. The `walk` family of `python3 "tools/govkit/upgrade_steps.py" fixture` gains
  `kill-after-up`: the fixture step's up writes its image, then its file, then its witness change, and
  the fixture kills the walk after the up returns and before move 5. The re-run applies the row at
  move 1. Observed by AC1 and AC2.
- **S3** — The consequence, observed. The `rollback` family gains `kill-after-up-image-lost`: after
  `kill-after-up`'s re-run the image is deleted, and the rollback stops on the row with
  TOOL-dSafePassage-33 S3's failure naming the image path. Observed by AC2.
- **S4** — The docs. The receipt section of `help/upgrade-steps.md`, which names `via`
  (TOOL-dSafePassage-33 S5), says the mark is set only when the receipt held no record of the step and
  no before-image existed. Observed by AC4.

## 3. Non-goals (OUT)

- The writer's carry of the mark across later rewrites: finding 23, `TOOL-dSafePassage-39`.
- Staging the image before move 5. TOOL-dSafePassage-2 S11 stages a step's writes once, after its
  witness holds, and moving that would stage a failed up's partial writes.
- Restoring a lost image, which TOOL-dSafePassage-33 §3 leaves to an operator.

### Edges

- **consumes-from** `TOOL-dSafePassage-33` — move 1's `via` mark and the down's no-image rule it feeds; without them there is no mark to condition
- **consumes-from** `TOOL-dSafePassage-2` — `run_step_walk`, its receipt argument, move 3's `interrupted:` record and the `walk` fixture family; without them there is no prior record to read and no kill to plant

## 4. Design

### The rule

```
move 1, witness holds:
  prior = the walk-start receipt's record for the step, or none
  image = TOOL-dSafePassage-1's image path for the row exists on disk
  via   = "witness" if prior is none and not image else None
  set_step_state(receipt, id, introduced, "applied", via=via)
```

| Walk-start record | Image on disk | Row after move 1 |
|---|---|---|
| none | absent | `applied`, `via` `witness` |
| none | present | `applied`, no `via` |
| `failed`, `interrupted:` or any failure | either | `applied`, no `via` |
| `rolled-back` | either | `applied`, no `via` |

### Inventory

Minted: the plants `kill-after-up` (`walk`) and `kill-after-up-image-lost` (`rollback`). No function,
conf key, gate leg or policy key. No new `raise Refusal` site, so `tools/govkit/refusal_join.py`'s
`BRANCH_PIN` does not move.

### Migration

None: no receipt at the base records a step.

### Rollout

Live at landing. It builds at order 6, after TOOL-dSafePassage-33 (order 5), whose move-1 mark it
conditions. It shares `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with
`TOOL-dSafePassage-39` and TOOL-dSafePassage-26 at order 6, so the build run sequences those passes by
M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Reading only the prior record, not the image.** A receipt lost or reset after an up wrote leaves
  no record and an image on disk; the image is the evidence the up spawned.
- **Reading only the image.** A killed up that died before writing its image leaves a `failed` record
  and no image, and the up still spawned.

## 5. Production-readiness checklist

- security: no new write path; the mark asserts a past event only from evidence of it.
- perf / scale: one file-existence test per row applied by witness.
- error / empty / loading states: a killed walk's re-run records the row without the mark.
- observability: the receipt row shows the mark only where no up is on record.
- risks: a row whose up ran and whose image is later lost cannot roll back by exit alone; it stops,
  as TOOL-dSafePassage-33 §5 prices.
- testing: the two plants and the probe, through §7.
- migration: none.
- user docs: `help/upgrade-steps.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant kill-after-up` runs,
  the killed walk leaves the row `failed` with an `interrupted:` failure, and the re-run records it
  `applied` with no `via`; `--plant witness-holds` still records its row with `via` `witness`.
  Red when: a row whose up ran before a kill is marked as applied by witness alone.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant kill-after-up-image-lost`
  runs, the rollback stops on the row with `witness still holds after down; before-image <path> absent`
  naming the image path, the up's file stays in place, and the run exits 1.
  Red when: the rollback records `rolled-back` while the up's file remains.
- **AC3** — When a `python -c` probe runs `run_step_walk` over a scratch schema-4 receipt holding a
  `failed` record for a step whose witness holds and whose image is absent, the row after the walk is
  `applied` with no `via`; over a receipt with no record and an image present, the same.
  Red when: either kind of evidence is ignored.
- **AC4** — When `git grep -n -e "via" -e "no record" -- help/upgrade-steps.md` runs, the receipt
  section states when the mark is set.
  Red when: the page says the mark means only that the witness held.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the self-test calls `upgrade_steps.py fixture walk` with `kill-after-up` and `fixture rollback` with `kill-after-up-image-lost`, its failing case staged by a move-1 copy that marks every row whose witness holds · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 27 to 35's id 29
  (HIGH, item D-5).

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-2's move 1 and TOOL-dSafePassage-33's mark, both specced and
unbuilt at the base, and TOOL-dSafePassage-1's image path. `python tools/codebase-map/reuse_lookup.py
"carry a row field forward when its writer rewrites the row"` ranked `rows`, `row`, `write` and
`write_text`, name-token matches, so no existing seam fits beyond those specs.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's promoted repairs are placed and sequenced after the unit they repair" --terms "spec audit promoted repair unit order edges hands-off consumes-from minors batch disposal rescope"`
