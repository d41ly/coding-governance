# DEPL-aHalvedInstall-4 — `update` installs a kit whole or not at all across a refused row

**Status:** CLOSED · rev-4 · 2026-10-02 · node a · Tier-2 · base cd90f7fa · streams deployer · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-build-DEPL-aHalvedInstall-4-1-acceptance-ledger.md](../build/2026-10-02-build-DEPL-aHalvedInstall-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-02-prompt-DEPL-aHalvedInstall-4-2-build-brief.md](../prompts/2026-10-02-prompt-DEPL-aHalvedInstall-4-2-build-brief.md) | journal | — |
| [2026-10-02-review-DEPL-aHalvedInstall-1-closing-diff-round1.md](../reviews/2026-10-02-review-DEPL-aHalvedInstall-1-closing-diff-round1.md) | diff-review | DEPL-aHalvedInstall-1 DEPL-aHalvedInstall-2 DEPL-aHalvedInstall-3 |

<!-- /gen:spec-records -->

## 1. Goal

`update` classifies and writes a kit's rows one at a time. A row it refuses — a three-way conflict,
a rename that conflicts, a merge it cannot land — is left at the old vintage while every sibling row
of the same kit lands at the new one, and the kit's `[[regenerate]]` still runs over the mixture.
Observed at an adopter: the review harness's new `check-protocol-parity.test.sh` landed while
`check-verifier-fanout.sh` stayed old behind a conflict, so the render asked the old script for a
flag it does not have. Rollback exists only for a kit whose `[check]` passed before the run and
fails after, and that kit declares `[check] none`. This unit makes a refused row hold its whole kit
back: none of the kit's writes from this run stand, its regenerate does not run, and the run says so.

## 2. Scope (IN)

- **S1** — The write loop of `_cmd_update` in `tools/govkit/govkit.py` records, per row, whether the
  row added a finding, and adds the row's kit to a held set with the row's path. The record is taken
  by comparing the report's problem count before and after the row, so every refusal in the loop is
  covered, including ones added later. Observed by AC1.
- **S2** — The re-render step declines the regenerate of a held kit, printing a `DECLINED` line that
  names the refused rows. A held kit is NOT entered in the render-stale set, so the verify pass's
  declined-red exit cannot claim it. Observed by AC2.
- **S3** — The verify pass rolls a held kit back whatever its check says: before the unmeasured and
  pre-existing-red exits, and through the existing restore loop, so restored bytes, removed
  landings, receipt rows and the rollback order all come from the one mechanism. The order's heading
  and opening sentence, the `verify` line and the finding name the refused rows as the cause instead
  of a check transition. Observed by AC1, AC3 and AC4.
- **S4** — Conflict orders and candidates are written exactly as before, one per refused row.
  Observed by AC5.
- **S6** — Round 1's folds. The fragment-wiring step skips a held kit, like an inert one, and says so
  (M3). The aHI-4 fixtures run with the refused row first AND last in the kit's acted rows, so the
  compare after the loop is exercised (M6). AC5's arm asserts all four candidate files (L1).
  Observed by AC5, AC7 and AC8.
- **S5** — Every kit whose shipped bytes this unit moves is bumped where `govkit epoch` names it;
  govkit itself is not in that population (DEPL-aHalvedInstall-1 rev-2). Observed by AC6.

## 3. Non-goals (OUT)

- **Cross-kit atomicity.** A refused row holds back its own kit only; a green sibling kit's writes
  are correct and stand, the rule the rollback order already states.
- **A row with no kit** — the synthesized lf-pin attributes row — holds back nothing; its own
  refusal is reported as today.
- **Pre-classifying conflicts before the first write.** The three-way runs inside the loop; moving it
  ahead would duplicate the classifier for a result the restore already reaches.

### Edges

- **hands-off** `DEPL-aHalvedInstall-5` — the classification walk's and the landing loop's
  refusals, which this unit's held set does not see; promoted from the closing review's round 1 H1.

## 4. Design

### Evidence

Read at base `cd90f7fa`. Eleven `r.fail` sites in the write loop end a row's processing. The touched
kit set and its pre-write snapshot, `snap_rows`, are taken before the loop for every acted row, so a
held kit always has a baseline and a snapshot. The restore loop sits inside the verify pass's
green-to-red arm, preceded by the `landed-unmeasured` exit, which a `[check] none` kit always takes.

### Data model

```python
_held: dict[str, list[str]] = {}          # kit -> refused row paths, in row order
for a in acted:
    _n0 = len(r.problems)
    ...                                    # the loop body, unchanged
    if len(r.problems) > _n0 and a["row"].get("kit"):
        _held.setdefault(a["row"]["kit"], []).append(a["row"]["path"])
```

A `continue` inside the body skips a trailing statement, so the count for a row is compared at the
TOP of the next iteration, and once more after the loop, rather than at the body's foot.

### Rollout

A run with no refused row behaves exactly as at base. A run with one now prints `HELD BACK` for that
kit, restores its other rows, and fails as it already did.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Rolling back only kits declaring `[check] none`.** A kit with a check that stays green over a
  half-install would keep it; the check is not what decides consistency.
- **Writing nothing until every row is classified clean.** The three-way result is computed inside
  the loop and the restore already exists; a second pass is a second implementation of both.

## 5. Production-readiness checklist

- security — the restore loop's containment check applies unchanged.
- perf / scale — one integer comparison per row.
- error / empty / loading states — a held kit with nothing written restores nothing and says so, the
  existing `(nothing to restore…)` line.
- observability — the order, the verify line and the finding each name the refused rows.
- risks — selftest arms written for the old half-install may now see a rollback; the owed suite run
  at VERIFYING is where they surface.
- testing — a fixture kit with one conflicting row, one clean stale row and a regenerate.
- migration — none: a receipt row restored is the pre-run row.
- user docs — N/A: `update`'s output is self-describing.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py update --target <fixture> --write` runs over a kit
  whose update conflicts on one row and cleanly changes another, the clean row's bytes and receipt
  row are back at the old vintage and the output carries `HELD BACK`.
  Red when: the held set is not consulted in the verify pass, so the clean row keeps gov's new bytes.
  fixture: built by the selftest arm in a temp dir; the kit declares `[check] none`.
- **AC2** — When that run's kit declares a `[[regenerate]]`, the output carries `DECLINED` for it
  naming the conflicting row, and the regenerate's output file is unchanged.
  Red when: the decline is missing, so the argv runs over the mixture.
- **AC3** — When the fixture kit declares a `[check]` that stays green, the clean row is still
  restored.
  Red when: the forced rollback sits after the transition test.
- **AC4** — When `update-rollback-demo.md` is read after AC1's run, it names the conflicting row as
  the cause and lists the clean row as restored.
  Red when: the order keeps its check-transition sentence for a held kit.
- **AC5** — When that run's `.governance/outbox` is read, the conflict order and its four candidate files for the
  conflicting row exist as before.
  Red when: the forced rollback deletes the outbox entries.
- **AC6** — When `python tools/govkit/govkit.py epoch` runs at the build's version commit, it prints
  no `FAILED` line.
  Red when: a kit whose shipped set moved keeps its version.

- **AC7** — When a held kit's update lands a changed hook fragment, `.claude/settings.json` is
  byte-identical after the run and the output names the fragment as not wired, with the hold.
  Red when: `_fr_skip` omits the held set.
- **AC8** — When the conflicting row sorts after every other acted row of its kit, `HELD BACK`, the
  declined regenerate and the restored clean row hold as in AC1 and AC2.
  Red when: the compare after the write loop is deleted.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · a fixture kit with one conflicting and one clean row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft, from the owner's third observation and `_cmd_update` at base.
- rev-4 · 2026-10-02 · §3 Edges · the hands-off to unit 5 that unit 5's consumes-from names; hygiene
  check 12 joins the pair and redded the close's bar without it.
- rev-3 · 2026-10-02 · S6 · AC7 · AC8 · folded round 1's M3, M6 and L1; AC5 now names all four files.
- rev-2 · 2026-10-02 · build pass · §4 Data model · S5 · AC6 · the per-row count is compared at the
  top of the next iteration instead of moving the 350-line body into a local function, which would
  have rebound a dozen of its names; S5 and AC6 follow unit 1's rev-2, since `epoch` does not grade
  govkit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "install a kit all or nothing when one row conflicts"`
ranked name-stem neighbours only (`classify_row`, `build_owned_row`). The seams extended are the
verify pass's restore loop and its `snap_rows` snapshot from DEPL-aRepatriatedFork-17 and
DEPL-dSealedTally-1, and the re-render step's decline list from DEPL-cMendedVintage-1. The recall
probe returned DEPL-dRatifiedSeam-2, which deferred landed sources outside rollback and was closed
by DEPL-dSealedTally-1; no record covers a refused row holding back its siblings.

Recall terms used: govkit update conflict rollback regenerate rendered vintage stale partial install hole discharge absent key

The question passed with them: "why does govkit update leave a kit half-installed when one row conflicts, and why does a renderer change roll back a kit".
