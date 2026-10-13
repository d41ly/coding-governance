# TOOL-dSweptBranches-10 — an untracked probe is covered only when its cases are declared on the default branch and its body exists there

**Status:** CLOSED · rev-2 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-10-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-10-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-10-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-10-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's round 1, H4 (ids 3, 13). An untracked test file counts as landed only when each case it declares is DECLARED on the default branch in the same form and every non-blank line of it exists in a file that declares one.

## 2. Scope (IN)

- **S1** — An untracked probe is covered only when it declares test cases and every non-blank line of it, stripped, exists in a default-branch file that names one of those cases. The line declaring each case is itself a probe line, so the body check requires the declaration, whole, without a separate anchor; the name only narrows which files are read. Observed by AC1.

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

- **AC1** — When the default branch holds only a longer name with the probe's name as a prefix, or the name only in prose, or the declaration under another body, `branch_reconcile.py` reads the probe's worktree `UNMERGED-LIVE`; the landed probe still reads covered.
  Red when: the body check is removed and a name hit alone covers the probe.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.
- rev-2 · 2026-10-13 · S1 · AC1 · the declaration-form ERE is dropped: a staged break replacing it with a bare name match stayed green, because the declaring line is one of the probe's own lines and the body check already demands it whole. The positive fixture's default test now carries the probe's body.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. The seam is check_worktree in `tools/branch-reconcile/branch_reconcile.py`, which this build wrote. The fix is the round-1 skeptic's, in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
