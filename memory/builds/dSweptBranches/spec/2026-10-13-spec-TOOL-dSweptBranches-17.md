# TOOL-dSweptBranches-17 — the closing review's MEDIUM and LOW items, batched

**Status:** CLOSED · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md](../build/2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md) | journal | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-7 TOOL-dSweptBranches-8 TOOL-dSweptBranches-9 TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13 TOOL-dSweptBranches-14 TOOL-dSweptBranches-15 TOOL-dSweptBranches-16 |
| [2026-10-13-build-TOOL-dSweptBranches-17-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-17-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-17-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-17-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's rounds 1 and 2 as one batch: round 1's M1 to M4 and L1 to L3 (ids 8, 14, 17, 20, 21, 22, 28, 29, 30) and round 2's M1, L1 and L2 (ids 1, 2, 3, 4), per BUILD-METHOD M4's rule that minors become ONE unit.

## 2. Scope (IN)

- **S1** — Round 1 M1: the write fixture gains a `SUPERSEDED` branch with a worktree carrying covered dirty content, and a landed stash. The asserted verdict set is derived from `VERDICT_RANK`, not typed. Observed by AC1.
- **S2** — Round 1 M2: the status read includes ignored paths (`--ignored=matching`), and the evidence names them as `ignored <n>`, saying they go with the worktree. The README says so. Observed by AC2.
- **S3** — Round 1 M3: arm_census's in-process seam check runs inside `seed_environ()`, and an arm with `GOV_REMOTE` set in the outer environment proves the hold-out. Observed by AC3.
- **S4** — Round 1 M4: one skeleton link points at a scratch directory outside the worktree holding a regular file, and the arm asserts that file survives. A failed `os.symlink` records the check as skipped, never as passed. Observed by AC4.
- **S5** — Round 1 L1: with no `.memory-tree.conf` and no memory root at the default tip, the report prints a `skipped —` line naming the records, rotated and run-record predicates. Observed by AC5.
- **S6** — Round 1 L2: spec 3's §4 and AC1 name `WRITE_TRACE`, recorded before each act. NOT OBSERVED — a record edit, which the spec-token checker reads.
- **S7** — Round 1 L3: an uncreatable manifest directory refuses with exit 2, and nothing is deleted. Observed by AC6.
- **S8** — Round 2 M1: the separator check runs over a fixture that holds a stash entry, so every keep spelling is in its population. Observed by AC7.
- **S9** — Round 2 L1 and L2: a row outside the deletable set reads `keep (<verdict>)`, so the README's sentence holds for every keep, and the containment reason names the kept worktree by its row name. Observed by AC7.

## 3. Non-goals (OUT)

- No change outside the mechanism named above; the other promoted items are their own units.

### Edges

- **consumes-from** `TOOL-dSweptBranches-3` — the code this unit amends.

## 4. Design

The fix is the round's skeptic-judged fix, recorded in the review cited in §10, built as stated
there and observed red before it lands.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`
- `memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-3.md`

### Alternatives rejected

- Folding this into another promoted unit: the closing review's exit rule promotes one unit per
  HIGH item, and the MEDIUM and LOW items as one batch.

## 5. Production-readiness checklist

- security — closes the review's finding; the costly error is a false deletable verdict.
- perf / scale — at most a few git calls per row or per commit.
- error / empty / loading states — an undecidable case keeps the row.
- observability — the evidence names what decided the row.
- risks — more rows kept, never more removed.
- testing — each criterion observed red before its fix.
- migration — N/A.
- user docs — the kit README.

## 6. Acceptance criteria

- **AC1** — When `branch_reconcile.py --write` runs over the extended write fixture, the asserted verdict set equals `VERDICT_RANK`, the superseded branch and its worktree are gone, and the stash list is unchanged.
  Red when: `SUPERSEDED` leaves the deletable set or the stash keep is removed.
- **AC2** — When an idle worktree holds an ignored file, `branch_reconcile.py` names `ignored 1` in its evidence.
  Red when: the status read drops `--ignored=matching`.
- **AC3** — When the outer environment exports `GOV_REMOTE=nope`, the census arm still passes.
  Red when: the seam check leaves `seed_environ()`.
- **AC4** — When `remove_worktree` removes a skeleton whose link points at a file outside it, that file survives.
  Red when: the walk follows links.
- **AC5** — When the repository has no memory tree, `branch_reconcile.py` prints the `skipped` line naming it.
  Red when: the announcement is removed.
- **AC6** — When a file occupies the manifest directory's path, `branch_reconcile.py --write` exits 2 and deletes nothing.
  Red when: the directory is created outside the refusal's `try`.
- **AC7** — When `build_rows` runs over a fixture holding every keep, a stash entry included, no action carries ` · `, every keep reads `keep (…)`, and a containment reason names its kept worktree's row name.
  Red when: a keep's reason leaves its parentheses.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. Every item lands in this build's kit. The fixes are the skeptics' sound fixes in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md` and `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
