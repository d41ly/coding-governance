# TOOL-dSweptBranches-14 — a merge commit is covered only when it introduces nothing of its own

**Status:** CLOSED · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md](../build/2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md) | journal | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-7 TOOL-dSweptBranches-8 TOOL-dSweptBranches-9 TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13 TOOL-dSweptBranches-15 TOOL-dSweptBranches-16 TOOL-dSweptBranches-17 TOOL-dSweptBranches-19 TOOL-dSweptBranches-20 TOOL-dSweptBranches-21 TOOL-dSweptBranches-23 TOOL-dSweptBranches-24 |
| [2026-10-13-build-TOOL-dSweptBranches-14-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-14-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-14-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-14-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's round 1, H8 (ids 10). A merge on a branch is read for content of its own, and `git cherry`, which skips merges, is trusted only when every merge introduces nothing.

## 2. Scope (IN)

- **S1** — A merge commit is covered only when `git diff-tree --cc -p` prints no hunk for it. check_equivalent trusts `git cherry` only when every merge in `<default>..<tip>` passes the same test. Observed by AC1.

## 3. Non-goals (OUT)

- No change outside the mechanism named above; the other promoted items are their own units.

### Edges

- **consumes-from** `TOOL-dSweptBranches-2` — the code this unit amends.

## 4. Design

The fix is the round's skeptic-judged fix, recorded in the review cited in §10, built as stated
there and observed red before it lands.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`

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

- **AC1** — When a branch holds an evil merge whose sibling commit landed by cherry-pick, `branch_reconcile.py` reads it `UNMERGED-LIVE`, not `EQUIVALENT`.
  Red when: a merge is covered without reading its own diff, or `git cherry` is trusted over merges.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. The seam is derive_coverage and check_equivalent in `tools/branch-reconcile/branch_reconcile.py`, which this build wrote. The fix is the round-1 skeptic's, in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
