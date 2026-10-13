# TOOL-dSweptBranches-2 — the verdict ladder: six verdicts over refs and worktree content, each with its evidence

**Status:** CLOSED · rev-2 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-2-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md) | research | TOOL-dSweptBranches-1 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 |
| [2026-10-13-prompt-TOOL-dSweptBranches-2-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-2-1-build-brief.md) | journal | — |
| [2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-dSweptBranches-1 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 |
| [2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md](../reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md) | diff-review | TOOL-dSweptBranches-1 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 |

<!-- /gen:spec-records -->

## 1. Goal

`branch_reconcile.py` gives every ref and every worktree exactly one of `MERGED`, `EQUIVALENT`,
`SUPERSEDED`, `IN-PROGRESS`, `UNMERGED-LIVE` or `UNKNOWN`, with the evidence that decided it. The
predicates are the method one inCMS session derived by hand over several hours, including the traps
`git cherry` and merge-tree conflict counts fall into.

## 2. Scope (IN)

- **S1** — The ref ladder, first match wins, for a local branch, a remote branch or a worktree's
  `HEAD`:
  1. `MERGED` — `git merge-base --is-ancestor <tip> <default>`.
  2. `EQUIVALENT` — `git cherry <default> <tip>` lists at least one commit and every line starts `-`.
  3. `SUPERSEDED` — the merge-tree no-op proof of S3, or every unique commit covered by S2.
  4. `IN-PROGRESS` — S4.
  5. `UNMERGED-LIVE` — unique commits remain uncovered and every predicate ran.
  6. `UNKNOWN` — a predicate the outcome depended on could not run, or raised.
  Observed by AC1 to AC8.
- **S2** — A unique commit is one `git rev-list <default>..<tip>` lists. A merge commit among them is
  covered when every parent is an ancestor of the default branch or is itself a unique commit. A
  non-merge commit `git cherry` marks `-` is covered as `patch-id`. Any other non-merge commit is
  covered by the first of four predicates that holds, and the evidence counts each predicate's
  commits:
  - **patch** — a commit in `<merge-base>..<default>` carries the identical subject, and the
    multisets of the two patches' `+` and `-` lines differ by at most `DRIFT_LINES` (4) lines. A
    rebased copy that drifted by a line or two per patch is matched; `git cherry` misses it.
    Observed by AC1.
  - **landing** — the commit's subject names a unit id or a `(<slug>)` scope, and a merge commit in
    `<merge-base>..<default>` whose subject names the same unit or slug touches, in its first-parent
    diff, every file the commit touched. This is the pre-fold or pre-squash variant. Observed by AC2.
  - **records** — every file the commit touched is a run-state file
    (`<memory root>/builds/<slug>/RUN*.md`), and the default branch shows that build landed: its
    `RUN.md` there records phase `LANDED`, or a merge in `<merge-base>..<default>` names the slug.
    Observed by AC3.
  - **rotated** — every file the commit touched is under the memory root, every non-blank line it
    adds is a ROW (its first token, after list or table markup, is a row id), and a row headed by
    each such id exists anywhere under the memory root at the default tip, archives included. A line
    that merely cites an id is content of its own, never a rotated row. Observed by AC4.
- **S3** — The merge-tree no-op proof: `git merge-tree --write-tree <default> <tip>` exits 0 and
  prints the default tip's own tree. It is only ever a positive proof. Its conflict count is never
  read, because a stale, fully landed branch conflicts heavily. A git without `--write-tree` makes it
  a `skipped` line. Observed by AC5.
- **S4** — `IN-PROGRESS` for a ref, from three sources, none of them a host app:
  - a run-state file the tip carries, `<memory root>/builds/<slug>/RUN.md` for a slug the unique
    commits name, whose `phase` fact is not `LANDED` or `ABORTED` and whose `lease-utc` lies within
    the freshness bound;
  - a build README the tip carries, for a slug the unique commits name, whose generated status is
    not `CLOSED` or `WONTDO`, unless the default branch's copy is;
  - a tip committed within the freshness bound, `FRESH_HOURS` (24), which `--fresh-hours` overrides.
  The run records are read as data at the tip and are never written. Observed by AC6.
- **S5** — A worktree's verdict. A worktree is `IN-PROGRESS` when it is the one the tool was invoked
  from, or when its newest activity — its `HEAD` commit, its index and each dirty path's mtime — lies
  within the freshness bound. Otherwise its content is graded first: it is covered when each
  element is covered, and then the worktree takes its `HEAD`'s ref verdict. Elements:
  - an in-progress merge is covered when its `MERGE_HEAD` is an ancestor of the default branch;
  - an untracked file is covered when its blob exists in the default tree, or when every test case
    it declares (`def test_…`, `it("…")`, `test("…")`, `arm "…"`) is found by `git grep -F` at the
    default tip;
  - a staged or unstaged path is covered when its worktree bytes equal the default tree's blob at
    that path, or both are absent;
  - a rebase in progress, or a submodule whose pointer differs from the default tree's gitlink, is
    never covered and makes the worktree `UNKNOWN`.
  Uncovered content makes the worktree `UNMERGED-LIVE`. Observed by AC7.
- **S6** — A stash entry is `SUPERSEDED` when every path its working-tree commit changed already
  holds those bytes at the default tip, else `UNKNOWN`. A stash carrying untracked files is
  `UNKNOWN`. Observed by AC8.
- **S7** — A predicate that raises an `OSError`, `ValueError`, `KeyError` or `IndexError` leaves its
  row `UNKNOWN`, naming the predicate, and adds one `skipped` line. NOT OBSERVED — no
  fixture this node can build makes git fail mid-predicate, and a monkeypatched raise would test the
  wrapper and not git.

## 3. Non-goals (OUT)

- No deletion, which is unit 3.
- No fetch, so a ref is graded against the default branch as this clone last saw it; the skill
  fetches first.
- No reading of an unattended run's liveness through a host process probe. The lease's recorded time
  and the freshness bound decide.
- No similarity measure other than the line-multiset difference.

### Edges

- **consumes-from** `TOOL-dSweptBranches-1` — the inventory, the row shape and the stub seam.
- **hands-off** `TOOL-dSweptBranches-3` — the verdicts write mode deletes by.

## 4. Design

Each predicate is one function returning a decision or "not decided", with an evidence string.
`derive_verdict` walks them in S1's order. A predicate that raises, or one that a missing git
capability prevents, records a `skipped` line once per predicate and leaves the row `UNKNOWN` when
nothing earlier decided it.

The unit and slug names come from `.memory-tree.conf` when present: `MEMORY_ROOT` (default
`memory`) and the id pattern `<FAMILY>-<slug>-<seq>`. A subject names a slug when it carries
`(<slug>)` after its type word, or names a unit id whose slug part is it. A repository with no memory
tree skips the `records`, `rotated` and run-record predicates, announced.

Patches are read once per commit with `git show --format= --no-color --no-ext-diff -U0 <sha>`. The
`+++` and `---` header lines are dropped and the rest count as a multiset. The candidate counterparts
are indexed by subject from one `git log` over `<merge-base>..<default>`.

The self-test's fixtures are one repository per verdict, each built under a temporary directory:
a rebased copy with one and two lines of drift; a pre-fold variant and its later landing merge; a
records-only commit for a landed build; a row rotated into an archive; a detached worktree holding
an in-progress merge whose other side landed; a nested harness worktree; a temp-dir worktree; an
untracked probe whose case landed as a test; a live run lease; and an `UNMERGED-LIVE` branch. Each
arm is written and observed red against unit 1's stub before its predicate is written.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`
- `memory/map/features/branch-reconcile.md`

### Alternatives rejected

- Merge-tree conflict counts as a supersession signal. A stale branch whose every commit landed
  conflicts heavily, so the count separates nothing.
- `git cherry` alone. Its patch ids miss a rebased copy that drifted by a line.
- Reading only the live decision log for a row. A rotated row lives in an archive.

## 5. Production-readiness checklist

- security — read-only; fixed argv lists, no shell, and run records read as data and never executed.
- perf / scale — one `git show` per unique commit and one `git log` per ref. 100 refs with 10 unique
  commits each is about a thousand processes. That is acceptable for an occasional cleanup.
- error / empty / loading states — a skipped predicate is announced and degrades to `UNKNOWN`, never
  to a deletable verdict.
- observability — each row's evidence names the predicate and the counterpart sha.
- risks — a false `SUPERSEDED` is the costly error. Every covering predicate demands evidence on the
  default branch, and the drift bound is small and declared.
- testing — AC1 to AC8, each red against the stub first.
- migration — N/A.
- user docs — the kit README's verdict table.

## 6. Acceptance criteria

- **AC1** — When `branch_reconcile.py` runs over the rebased-copy fixture, the branch reads
  `SUPERSEDED` with evidence counting two commits by `patch`, while `git cherry` lists them `+`.
  Red when: the predicate is the stub, or the drift bound is 0.
- **AC2** — When it runs over the pre-fold fixture, the branch reads `SUPERSEDED` by `landing`,
  naming the landing merge.
  Red when: the predicate is the stub, or a file the commit touched is missing from the merge.
- **AC3** — When it runs over the records-only fixture, the branch reads `SUPERSEDED` by `records`.
  Red when: the predicate is the stub, or the default branch's `RUN.md` is not `LANDED`.
- **AC4** — When it runs over the rotated-row fixture, whose row id exists only under the memory
  root's `archive/`, the branch reads `SUPERSEDED` by `rotated`; a branch whose spec prose cites
  that same id reads `UNMERGED-LIVE`.
  Red when: the predicate is the stub, the search reads only the live log, or an added line that
  only cites an id counts as a row.
- **AC5** — When the merge-tree fixture's branch adds and then reverts a line, it reads `SUPERSEDED`
  by the no-op proof, and a stale landed branch with conflicts never reads `SUPERSEDED` by it.
  Red when: the proof is the stub, or it reads the conflict count.
- **AC6** — When the live-lease fixture's branch carries a `RUN.md` at phase `BUILDING` with a lease
  inside the bound, it reads `IN-PROGRESS`; with the lease outside the bound and an old tip, it does
  not. The `UNMERGED-LIVE` fixture's branch reads `UNMERGED-LIVE`.
  Red when: the predicate is the stub.
- **AC7** — When the detached merge-in-progress worktree, the untracked-probe worktree, the nested
  harness worktree and the temp-dir worktree are graded with a 0-hour freshness bound, the first two
  read their `HEAD`'s verdict because their content is covered, and the other two read their
  `HEAD`'s verdict. An uncovered untracked file reads `UNMERGED-LIVE`. Under the default bound, a
  freshly made worktree reads `IN-PROGRESS`.
  Red when: a content predicate is the stub, or the freshness test is removed.
- **AC8** — When the stash fixture's entry changed a path to bytes the default tip already holds, it
  reads `SUPERSEDED`; a stash with new bytes reads `UNKNOWN`.
  Red when: the predicate is the stub.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · one fixture repository per verdict, each arm observed red against the stub before its predicate · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-13 · S2 · S4 · S6 · S7 · AC4 · what the build pass settled. S2 counts a commit
  `git cherry` marks applied as `patch-id`. The rotated predicate takes rows only: run over gov's own
  tree, the first version called a 250-line spec rewrite `SUPERSEDED` because every id its prose
  cited existed somewhere, and AC4 gains that case as a negative. S4 lets a default-branch copy of a
  build README that is terminal override the tip's. S6 names a stash with untracked files. S7 states
  the raise rule.

## 10. Reuse audit

No existing seam computes these verdicts. `reuse_lookup.py "classify branches and worktrees as
merged or superseded and delete them"` ranked `merge`, `classify` and `branches` as name-token
neighbours only. `build_nonterminal_merged_runs` in `tools/drift-audit/drift_report.py` asks the
reverse question, run records left non-terminal after their build merged, and is not reused. The
run-state facts read here, `phase` and `lease-utc`, are the unattended kit's, written by
`write_lease` in `tools/unattended/unattended.sh`, and the terminal set `LANDED ABORTED` is its
`PHASES_TERMINAL`. The id pattern is the memory-tree kit's `<FAMILY>-<slug>-<seq>`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
