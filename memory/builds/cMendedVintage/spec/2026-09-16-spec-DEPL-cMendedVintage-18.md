# DEPL-cMendedVintage-18 — a withdrawn row whose path did not restore stays in the receipt

**Status:** SPECCED · rev-1 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 27

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-2` S2 gates the `withdrawn_rows.remove(s["row"])` at
`tools/govkit/govkit.py:7666` together with the `ROLLBACK_FIELDS` revert, on the assumption that no
snapshot entry is also a withdrawn row. `_touching` at `tools/govkit/govkit.py:6692` admits
`withdrawn` whenever `--write-withdrawals` is passed, so on those runs a withdrawn row IS a snapshot
entry. `withdrawn_rows` is the DELETE list consumed at `:7818`, so skipping the removal drops the row
from the receipt entirely for a path the run could not restore. Split the two effects.

## 2. Scope (IN)

- **S1** The `_left` gate covers the `ROLLBACK_FIELDS` revert ALONE. The `withdrawn_rows.remove` at
  `tools/govkit/govkit.py:7666` moves outside it and runs whenever the entry reached the tail, so a
  row whose path the rollback could not return is never deleted from the receipt. Observed by AC1.
- **S2** A withdrawn-and-unrestored row keeps this run's field values rather than reverting to its
  pre-run ones, matching the landed branch's rule and `DEPL-cMendedVintage-2`'s own invariant that the
  row describes the bytes on disk. Observed by AC2.
- **S3** That path is reported in the order's `NOT restored` block with a sentence stating what is
  true of it — the withdrawal did not complete, the row was kept, and the file is still there.
  Observed by AC3.
- **S4** `tools/govkit/selftest.py` gains the invariant one level up: over every arm that exercises a
  rollback, no path may end the run both absent from the receipt's `files[]` and present in the
  worktree. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `_touching` and no change to what `--write-withdrawals` selects. Admitting `withdrawn`
  to the snapshot is correct — a deleted path is exactly what a rollback must be able to undo — and
  narrowing it would trade this defect for an unrestorable deletion.
- No retry of the withdrawal, no second `unlink`, no fallback delete. `DEPL-cMendedVintage-2` §3
  refuses a retry on the restore path and the same argument holds here.
- No change to the landed branch at `tools/govkit/govkit.py:7627`, which already gates its own row
  removal on its own predicate. This unit makes the withdrawn branch agree with it rather than
  rewriting either.
- No repair of a receipt already missing a row. Nothing knows which rows those are; the operator's
  repair is a `--re-adopt` with the path pinned.

### Edges

- **consumes-from** `DEPL-cMendedVintage-2` — that unit introduces `_left` and the gate this unit
  splits. Without it there is one unconditional tail and this defect does not exist in the shape
  described here.
- **hands-off** external — nothing else in this build reads `withdrawn_rows`.

## 4. Design

### Why skipping the removal deletes the row

`withdrawn_rows` is not a keep-list, it is the delete-list: `:7818` strips every row still in it from
the receipt before serialisation. So `remove(s["row"])` is what SAVES a row, and gating it behind
`_left` inverts its meaning. The sentence in `DEPL-cMendedVintage-2` §2 reads as though the removal
and the revert are two halves of one restoration; they are opposites, and the gate that is right for
one is exactly wrong for the other.

| the run | the revert | the removal from `withdrawn_rows` |
|---|---|---|
| restored every written path | correct: the row goes back to its pre-run values | correct: the row survives |
| could not restore a written path | skipped: the row stays forward | must ALSO run, or the row is deleted for a file still on disk |

### The reachable case, and how it is manufactured

The fixture technique is `DEPL-cMendedVintage-2`'s own: a directory planted at the worktree path
makes `git checkout-index -f` refuse. The withdrawn arm's own `dp.unlink()` is guarded by
`is_file()`, so a directory is skipped there and still reaches `deleted` and then `written_paths` at
`tools/govkit/govkit.py:7502`. One fixture, both branches, no git mock.

### What the receipt then says

The row stays, carrying this run's values, describing a file that is still in the worktree. That is
the invariant `DEPL-cMendedVintage-2` states and this unit is the second half of: a receipt that
agrees with the tree and re-offers nothing beats a receipt that disagrees, and a receipt with no row
at all for a path that exists is the worst of the three — the next `update` cannot classify it, and
`check` reports it as an unclaimed source.

### Inventory

This unit MINTS nothing. It moves one statement out of a conditional, changes which values a row
keeps on one branch, adds one order sentence and one suite invariant.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the removal hoisted out of the gate, the withdrawn branch's field handling, one order sentence |
| `tools/govkit/selftest.py` | one fixture arm and the cross-arm invariant |

### Alternatives rejected

- **Take the row out of `withdrawn_rows` and let the withdrawal stand as recorded.** That records a
  deletion that did not happen: the file is on disk and the receipt would say gov removed it.
- **Restore the withdrawn path instead.** The path was not withdrawn — the `unlink` was skipped — so
  there is nothing to restore, and `checkout-index` refuses for the same reason it refused the first
  time.
- **Scope withdrawals out of the rollback entirely.** That is the `_touching` narrowing §3 refuses. A
  run that deleted files and then rolled back must be able to bring them back.

### Migration

None. No receipt field or descriptor key changes shape.

### Rollout

Lands directly. The branch is reachable only on a `--write-withdrawals` run whose rollback already
failed, so no ordinary run changes behaviour.

## 5. Production-readiness checklist

- security — the unit strictly reduces what is deleted from the receipt. No new write path.
- perf / scale — no runtime cost; one statement changes position.
- error / empty / loading states — a run with no withdrawn rows never reaches the branch; an entry
  whose every path restored takes the existing revert unchanged.
- observability — the order's `NOT restored` block names the path and says the row was kept, so the
  state appears in the durable record and not only in the run's findings.
- risks — the sharp one is that the removal now runs on a branch where the revert does not, which is
  an asymmetry a later reader will want to re-merge. §4's table is written so it cannot be re-merged
  by mistake, and AC1 fails if it is.
- testing — one fixture, four criteria, plus the cross-arm invariant in S4 which grades every
  existing rollback arm rather than only the new one.
- migration — none; §4 states why.
- user docs — `WIRE-INTO-PROJECT.md`'s maintenance section gains one sentence: a withdrawal that
  could not complete leaves the row, and the file, in place.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target carries one withdrawn row, a directory is planted at that
  row's worktree path, and `python tools/govkit/govkit.py update --target <fixture> --write
  --write-withdrawals` rolls the kit back, the post-run receipt still carries a row for that path.
  Red when: the removal stays inside the `_left` gate, so the row is dropped from the receipt for a
  file the run neither deleted nor restored.
  fixture: built by this unit from `DEPL-cMendedVintage-2`'s technique — a directory at the worktree
  path the receipt names as a file; this repo keeps no `.governance/` receipt of its own.
- **AC2** — When that run finishes, the kept row carries this run's field values and not the pre-run
  ones.
  Red when: the revert is hoisted out with the removal, so the row describes bytes that never came
  back — the defect `DEPL-cMendedVintage-2` exists to close, arriving through the withdrawn branch.
- **AC3** — When the order file from AC1 is read, the path appears under `NOT restored` with a
  sentence saying the withdrawal did not complete and the row was kept.
  Red when: the withdrawn case takes the restore branch's sentence, which tells the operator the
  bytes are this run's when the file was never rewritten.
- **AC4** — When the cross-arm invariant S4 adds runs over every arm that exercises a rollback, no
  path ends a run both absent from the receipt's `files[]` and present in the worktree, and staging
  the shipped gate as written turns it RED.
  Red when: the invariant is asserted only on this unit's own fixture, which certifies the arm that
  was written to pass it and says nothing about the six that already exist.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a `--write-withdrawals` run whose withdrawn path is a directory,
so the rollback cannot restore it, asserted to keep the receipt row · no assertion floor to move.

New arm: `tools/govkit/selftest.py` · the cross-arm receipt-versus-worktree invariant over every arm
that exercises a rollback · no assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "restore a snapshot entry whose kit key no rollback loop
selects"` was the probe for this promoted set and returned no seam; its ranked rows are name-token
neighbours on the stems `kit` and `key` and it named `.sh` as an unscanned layer, so govkit's rollback
pass is the only candidate and it was read from source. The seam this unit extends is the landed
branch at `tools/govkit/govkit.py:7627`, which already separates "may this row be dropped" from "what
values does this row carry" and computes `_left_landed` for the first question only. This unit gives
the withdrawn branch the same separation rather than inventing one. The recall probe returned the
`DEPL-dSealedTally-1` round-1 spec audit, which recorded the per-entry tail at `:6915-6924` running
for every snapshot entry regardless of origin — the same block, one vintage earlier, and the record
that establishes this tail has been got wrong before.

Recall terms used: `--terms "govkit rollback snapshot attributes receipt row kit orphan restore
touched_kits claimed verify outcome regenerate"`, with the question "what decided how govkit rollback
selects snapshot entries by kit and what owns the synthetic attributes row".
