# DEPL-cMendedVintage-18 — a withdrawn row whose path did not restore stays in the receipt

**Status:** CLOSED · rev-3 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 29

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-18-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-18-acceptance-ledger.md) | journal | — |
| [2026-09-17-prompt-DEPL-cMendedVintage-18-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-18-2-build-brief.md) | journal | — |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-2` S2 gates the `withdrawn_rows.remove(s["row"])` in `update`'s per-entry
rollback tail together with the `ROLLBACK_FIELDS` revert, on the assumption that no snapshot entry is
also a withdrawn row. `_touching` admits `withdrawn` whenever `--write-withdrawals` is passed, so on
those runs a withdrawn row IS a snapshot entry. `withdrawn_rows` is the DELETE list — the filter
below the write loop strips every row still in it from the receipt — so skipping the removal drops
the row from the receipt entirely for a path the run could not restore. Split the two effects.

*Every site is named by SYMBOL here. rev-1 keyed three of them to line numbers that eight later units
had already moved, and a line-keyed read in code that decides what gets deleted is not a mistake the
reader notices.*

## 2. Scope (IN)

- **S1** The `_left` gate covers the `ROLLBACK_FIELDS` revert ALONE. The `withdrawn_rows.remove`
  moves ABOVE it and runs for every entry that reached the tail, so a row whose path the rollback
  could not return is never deleted from the receipt. One hoisted statement serves the `attributes`
  branch too, which carried its own copy of the same line and sat below the same gate. Observed by
  AC1.
- **S2** A withdrawn-and-unrestored row keeps this run's field values rather than reverting to its
  pre-run ones, matching the landed branch's rule and `DEPL-cMendedVintage-2`'s own invariant that the
  row describes the bytes on disk. For a `withdrawn` verdict those two sets of values are EQUAL over
  every `ROLLBACK_FIELDS` key, because the write loop never touches them — see AC2. Observed by AC2.
- **S3** That path is reported in the order's `NOT restored` block with a sentence stating what is
  true of it — the withdrawal did not complete and the row was kept, with the per-path reason above
  it saying how far the restore got. Observed by AC3.
- **S4** `tools/govkit/selftest.py` gains the invariant one level up: over every arm that exercises a
  rollback, no path may end the run both absent from the receipt's `files[]` and PRESENT IN THE
  TARGET — worktree file or staged index entry, because the reachable case leaves the bytes in the
  index and a worktree-only reading stays green over it. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `_touching` and no change to what `--write-withdrawals` selects. Admitting `withdrawn`
  to the snapshot is correct — a deleted path is exactly what a rollback must be able to undo — and
  narrowing it would trade this defect for an unrestorable deletion.
- No retry of the withdrawal, no second `unlink`, no fallback delete. `DEPL-cMendedVintage-2` §3
  refuses a retry on the restore path and the same argument holds here.
- No change to the landed branch and its `_left_landed`, which already gates its own row
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

`withdrawn_rows` is not a keep-list, it is the delete-list: the filter below the write loop strips
every row still in it from the receipt before serialisation. So `remove(s["row"])` is what SAVES a
row, and gating it behind `_left` inverts its meaning. The sentence in `DEPL-cMendedVintage-2` §2 reads as though the removal
and the revert are two halves of one restoration; they are opposites, and the gate that is right for
one is exactly wrong for the other.

| the run | the revert | the removal from `withdrawn_rows` |
|---|---|---|
| restored every written path | correct: the row goes back to its pre-run values | correct: the row survives |
| could not restore a written path | skipped: the row stays forward | must ALSO run, or the row is deleted while the target still holds those bytes |

### The reachable case, and how it is manufactured

**rev-1's fixture does not reach the branch, measured.** A directory planted at the withdrawn
worktree path is DIRTY against the index, and `DEPL-dCarriedReceipt-12`'s claimed-path guard refuses
the whole run before a byte moves; committing the directory instead takes the blob OUT of the index,
which sends the rollback down its `entry is None` branch, where the unlink is skipped for a
non-file and the path is reported RESTORED. Either way the arm would have graded a rollback that
succeeded. `DEPL-cMendedVintage-2`'s own block says the same thing in its header for its own path.

The technique that reaches it is `DEPL-cMendedVintage-2`'s OTHER one: the kit's own `[check]` runs
between the write and the rollback, so it installs a `required` filter whose smudge command fails and
names the withdrawn path. `git checkout-index -f` then refuses that one path. The withdrawal itself
runs normally — the file is unlinked, the path reaches `deleted` and then `written_paths`, and the
row reaches `withdrawn_rows`.

### What the receipt then says

The row stays, carrying this run's values, describing bytes the target still holds. MEASURED, on the
engine with this unit not landed: the post-run receipt carried no row for the withdrawn path while
`git ls-files` still named it, because the rollback's `update-index` had already re-staged the
pre-run blob before `checkout-index` refused. So the residue is in the INDEX rather than the
worktree — which is why S4's invariant reads both, and why a worktree-only reading of it would have
been an assertion about nothing.

That is the invariant `DEPL-cMendedVintage-2` states and this unit is the second half of: a receipt
that agrees with the tree and re-offers nothing beats a receipt that disagrees, and a receipt with no
row at all for a path the target still holds is the worst of the three — the next `update` cannot
classify it, and `check` reports it as an unclaimed source.

### Inventory

This unit MINTS nothing. It hoists one statement out of a conditional and deletes the duplicate of
it the `attributes` branch carried, adds one order sentence and one suite invariant. It changes no
row's values: rev-1 expected it to, and AC2 records the measurement that says otherwise.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the removal hoisted above the gate and its duplicate deleted, one order sentence |
| `tools/govkit/selftest.py` | one fixture arm and the cross-arm invariant |

### Alternatives rejected

- **Take the row out of `withdrawn_rows` and let the withdrawal stand as recorded.** That records a
  deletion that did not happen: the pre-run blob is staged and the receipt would say gov removed it.
- **Retry the restore instead.** The rollback already tried it and the target's own git refused; a
  second `checkout-index` refuses for the same reason the first did, and §3 refuses a retry outright.
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
- observability — the order's `NOT restored` block names the path, says the withdrawal did not
  complete and says the row was kept, so the state appears in the durable record and not only in the
  run's findings.
- risks — the sharp one is that the removal now runs on a branch where the revert does not, which is
  an asymmetry a later reader will want to re-merge. §4's table is written so it cannot be re-merged
  by mistake, and AC1 fails if it is.
- testing — one fixture, four criteria, plus the cross-arm invariant in S4 which grades every
  existing rollback arm rather than only the new one.
- migration — none; §4 states why.
- user docs — `WIRE-INTO-PROJECT.md`'s maintenance section gains a short paragraph: a withdrawal the
  rollback could not finish undoing keeps its receipt row, because that row is then the only thing
  naming bytes the target still holds.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target carries one withdrawn row, a directory is planted at that
  row's worktree path, and the run is
  `python tools/govkit/govkit.py update --target <fixture> --write --write-withdrawals`
  rolling the kit back, the post-run receipt still carries a row for that path.
  Red when: the removal stays inside the `_left` gate, so the row is dropped from the receipt for a
  file the run neither deleted nor restored.
  fixture: built by this unit from `DEPL-cMendedVintage-2`'s technique — a directory at the worktree
  path the receipt names as a file; this repo keeps no `.governance/` receipt of its own.
- **AC2** — When that run finishes, the kept row's `ROLLBACK_FIELDS` values equal the ones the
  receipt held before the run, which for a `withdrawn` verdict ARE this run's values: the write loop
  appends the row to `withdrawn_rows` and writes none of the six keys. Amended in rev-2 — rev-1 asked
  for this run's values "and not the pre-run ones", which measurement says is a distinction the
  receipt cannot carry. The only key the run adds is `carry`, and `carry` is not in
  `ROLLBACK_FIELDS`, so hoisting the revert out with the removal would produce a byte-identical
  receipt and rev-1's red-when could not fire.
  Red when: the two sets of values diverge at all, which would mean the write loop had started
  writing a withdrawn row's own fields and S2 had become observable after all.
- **AC3** — When the order file from AC1 is read, the path appears under `NOT restored` with a
  sentence saying this run withdrew it, the rollback could not finish putting it back, and the row
  was KEPT rather than dropped.
  Red when: the withdrawn case takes the rewrite branch's sentence, which tells the operator the row
  was left at this run's values when the run's value for a withdrawal was the file's absence.
- **AC4** — When the cross-arm invariant S4 adds runs over every arm that exercises a rollback, no
  path that a rollback order names ends a run both absent from the receipt's `files[]` and present in
  the target — worktree file or staged index entry. Amended in rev-2: rev-1 said "present in the
  worktree", and the reachable case leaves the bytes in the INDEX with no worktree file, so the
  rev-1 wording stayed green over the defect this unit closes. Graded against a target built by the
  unlanded engine, which the predicate reds, and against one built by the landed engine, which it
  passes.
  Red when: the invariant is asserted only on this unit's own fixture, which certifies the arm that
  was written to pass it and says nothing about the ones that already exist.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a `--write-withdrawals` run whose withdrawn path a required
smudge filter keeps `checkout-index` from restoring, asserted to keep the receipt row · no assertion
floor to move.

New arm: `tools/govkit/selftest.py` · the cross-arm receipt-versus-target invariant, discovered from
every rollback order the suite produces rather than listed · no assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-17 · built. Four divergences, all measured. §4's fixture technique replaced: a
  directory at the withdrawn path is refused by the dirty-claimed-path guard, and committing it
  routes the rollback down its `entry is None` branch and restores cleanly — the smudge-filter
  sabotage is what reaches the refusal. S4 and AC4 widened from "present in the worktree" to
  "present in the target", because the reachable case leaves the pre-run blob in the INDEX with no
  worktree file and the rev-1 wording stayed green over it. AC2 amended: a `withdrawn` verdict
  writes none of the six `ROLLBACK_FIELDS` keys, so this run's values and the pre-run ones are equal
  and the revert's placement cannot be read off the receipt. Every line number dropped for its
  symbol. S1 also notes that the hoisted statement retires the `attributes` branch's own copy of it.

- rev-3 · 2026-09-17 · editorial, no criterion moved. AC1's command span WRAPPED across a line
  break, so the criterion offered no whole backticked token on any single line and hygiene check
  23's join arm reported the ledger answer as sharing nothing with it. The span now sits whole on
  its own line and the join resolves. The rule the wrap broke is the one this build has now
  tripped on twice from the other side, in a ledger rather than a spec.

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
