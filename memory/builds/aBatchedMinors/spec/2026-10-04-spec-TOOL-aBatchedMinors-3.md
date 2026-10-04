# TOOL-aBatchedMinors-3 — check 2 demands one unit per blocker and high, plus one for the minors

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-2 · base 5ba0fc4f · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aBatchedMinors-2-runlog-dc0cf1f9.md](../build/2026-10-04-build-TOOL-aBatchedMinors-2-runlog-dc0cf1f9.md) | journal | TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-4 TOOL-aBatchedMinors-6 |
| [2026-10-04-build-TOOL-aBatchedMinors-3-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aBatchedMinors-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aBatchedMinors-3-1-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aBatchedMinors-3-1-build-brief.md) | journal | — |
| [2026-10-04-review-TOOL-aBatchedMinors-2-closing-diff-round1.md](../reviews/2026-10-04-review-TOOL-aBatchedMinors-2-closing-diff-round1.md) | diff-review | TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-4 |

<!-- /gen:spec-records -->

## 1. Goal

Check 2 of the unattended kit gate demands, per exited subject recording `promote`, ONE unit id the
run's BASE lacked. That floor was a lower bound because a row recorded no finding counts. A closing
review's terminal row now carries them (`TOOL-aBatchedMinors-2`), so for that row the gate can demand
what the ruling owes: one unit per standing blocker and high, plus one for the minors batch.

## 2. Scope (IN)

- **S1** — The check-2 reader in `tools/unattended/check-unattended.sh` reads `highs <n>` and
  `minors <n>` from a review row's reason. A row carrying BOTH is a closing-review row; its owed
  floor is `blockers + highs + (minors > 0 ? 1 : 0)`. A row carrying neither keeps today's floor of
  one. The per-file total is the sum of the per-subject floors, compared against the new non-WONTDO
  ids exactly as today. Observed by AC1 and AC2.
- **S2** — A CONVERGED closing row whose counts stand on anything (`highs + minors > 0`) and which
  records no disposition is read as needing one, so it reaches the existing no-disposition refusal.
  Observed by AC3.
- **S3** — A closing row recording `fold` beside a non-zero `highs + minors` reds through the existing
  fold clause, its message naming that the closing review promotes every finding. Observed by AC4.
- **S4** — The leg's header states what this does NOT check: that the minors went into at most two
  units, or that a promoted unit's mechanism closes its finding — the region records ids, not which
  finding an id closes. Observed by AC5.

## 3. Non-goals (OUT)

- Rows without counts — every spec-audit row and every closing row written before
  `TOOL-aBatchedMinors-2` — keep exactly today's reading. No cutoff, because no historical row
  carries the fields.
- Attributing ids to subjects. The comparison stays per file and counting, as the clause's own
  comment explains.

### Edges

- **hands-off** `TOOL-aBatchedMinors-6` — the closing review's batched minors harden this unit.
- **consumes-from** `TOOL-aBatchedMinors-2` — the row grammar.

## 4. Design

### Evidence

Read at base `5ba0fc4f`. The awk program in check 2 sets `needs[it]` for a NON-CONVERGENT, CEILING or
BOUNDED row and for a graded CONVERGED row carrying a disposition, and adds ONE to `nneed` per
subject recording `promote`. `newids` is the count of non-WONTDO ids in the HEAD units region that
the BASE region lacks. The fold clause `foldbad` fires on `bl[it] > 0` under `FOLD_CUTOFF`.

### Data model

```
owe[it] = (it has counts) ? bl + hi + (mi > 0 ? 1 : 0) : 1      # per exited subject recording promote
nneed  += owe[it]
```

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **Demanding exactly the floor.** Another unit added by `--rescope --act add` for a discovery is a
  legitimate new id, so the region may gain more than the review owes. The floor is a minimum.
- **Applying the per-blocker floor to rows without counts.** Spec-audit rows record no highs, and a
  graded historical record promoting fewer units than blockers would red on an append-only file.

## 5. Production-readiness checklist

- security — the leg reads a tracked record; nothing it reads is executed.
- perf / scale — two `match()` calls per review row inside the existing awk pass; no new process.
- error / empty / loading states — a row with one count and not the other is read as carrying
  neither, and the AC1 arm pins it.
- observability — the failure message names the owed floor and how it was derived.
- testing — each clause observed RED on a staged fixture before it lands.
- migration — none.
- user docs — the verbs entry, in `TOOL-aBatchedMinors-4`.
- risks — a hand-written row with counts and too few ids reds; that is the clause working.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` grades a record whose closing row reads
  `blockers 0 · CONVERGED · highs 1 · minors 3 · disposition promote` over a units region that gained
  one id, it fails check 2 naming a floor of 2; with two ids gained it passes.
  Red when: the reader keeps the floor of one per subject.
- **AC2** — When the row reads `highs 2 · minors 0 · disposition promote` with two ids gained it
  passes, and with one it fails: the minors add nothing when none stood.
  Red when: the minors term adds one unconditionally.
- **AC3** — When the converged closing row carries `highs 0 · minors 2` and no disposition, check 2
  fails naming the missing disposition.
  Red when: a converged row with no disposition is skipped as before.
- **AC4** — When the converged closing row carries `minors 2 · disposition fold`, check 2 fails
  naming the fold.
  Red when: `foldbad` reads only the blocker count.
- **AC5** — When a spec-subject row `blockers 2 · NON-CONVERGENT · disposition promote` grades over
  one new id, the existing arm still passes.
  Red when: a row without counts takes the per-blocker floor.

## 7. Gates

`unattended kit gate` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-unattended.test.sh · a closing row over too few new ids, against the base reader · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from check 2 at base.
- rev-2 · 2026-10-04 · §3 Edges · the hands-off to `TOOL-aBatchedMinors-6`, which consumes this unit; the
  close's hygiene check 12 found the edge one-sided.

## 10. Reuse audit

The seam extended is check 2's existing awk pass and its `needs`, `nneed`, `nomiss` and `foldbad`
clauses, with the `newids` delta unchanged. `python tools/codebase-map/reuse_lookup.py "closing review
disposition promote findings to units by severity"` printed `unscanned layers: .sh` and cannot see it;
it was found by reading the leg. Recall returned the cluster-C record of aProbedUnit's closing review,
which added the CONVERGED-with-disposition read this unit extends.

Recall terms used: closing review disposition promote fold severity BLOCKER HIGH MEDIUM LOW unit rescope CONVERGED
