# TOOL-dSweptBranches-16 — tracked edits in an idle worktree are graded by a fixture

**Status:** CLOSED · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md](../build/2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md) | journal | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-7 TOOL-dSweptBranches-8 TOOL-dSweptBranches-9 TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13 TOOL-dSweptBranches-14 TOOL-dSweptBranches-15 TOOL-dSweptBranches-17 TOOL-dSweptBranches-19 TOOL-dSweptBranches-20 TOOL-dSweptBranches-21 TOOL-dSweptBranches-23 TOOL-dSweptBranches-24 |
| [2026-10-13-build-TOOL-dSweptBranches-16-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-16-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-16-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-16-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's round 1, H10 (ids 19). arm_content grades staged and unstaged tracked edits, so the uncovered-change branch of check_worktree is observed.

## 2. Scope (IN)

- **S1** — arm_content gains an idle worktree with a staged and an unstaged edit to new bytes, which reads `UNMERGED-LIVE` naming `changed <path>`, and one whose edit restores the default's bytes, which takes its `HEAD`'s verdict. Observed by AC1.

## 3. Non-goals (OUT)

- No change outside the mechanism named above; the other promoted items are their own units.

### Edges

- **consumes-from** `TOOL-dSweptBranches-2` — the code this unit amends.

## 4. Design

The fix is the round's skeptic-judged fix, recorded in the review cited in §10, built as stated
there and observed red before it lands.

### Files touched (estimate)

- `tools/branch-reconcile/selftest.py`

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

- **AC1** — When an idle worktree carries staged and unstaged edits to new bytes, `branch_reconcile.py` reads it `UNMERGED-LIVE` naming `changed`; an edit restoring the default's bytes reads its `HEAD`'s verdict.
  Red when: an uncovered changed path is appended as covered.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. The seam is arm_content in `tools/branch-reconcile/branch_reconcile.py`, which this build wrote. The fix is the round-1 skeptic's, in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
