# TOOL-aCollapsedScan-7 — `repo_root()` takes the walk-up govkit already took for this defect

**Status:** INPROGRESS · rev-2 · 2026-08-26 · node a · Tier-2 · base 3c37a1fb · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-aCollapsedScan-4-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-aCollapsedScan-4-spec-audit-round1.md) | spec-audit | TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-6 |

<!-- /gen:spec-records -->

## 1. Goal

Make the memory-recall kit resolve the repository root correctly when git execs it inside a linked
worktree. Today it does not, so `merge-rows.py` — the row-keyed merge driver git runs for
`memory/DECISIONS.md` and `memory/backlog/*.md` — aborts on every merge of those files in a worktree
and hands the author a conflict instead of a merge.

## 2. Scope (IN)

- **S1** — `recall_conf.repo_root()` resolves by walking UP from `__file__` for `.memory-tree.conf`,
  with no subprocess, exactly as `tools/govkit/govkit.py:83` already does for its own registry and
  for this same measured reason.
- **S2** — `tools/memory-recall/query.py:199`, a second `repo_root()` in the same kit that shells a
  bare `rev-parse` with no `-C` anchor at all, is deleted; its one caller at `query.py:1089` calls
  `recall_conf.repo_root()`. One kit, one answer.
- **S3** — A regression test that resolves the root from inside a LINKED WORKTREE with `GIT_DIR`
  inherited. It must FAIL against the pre-fix function, which is observed before the fix is wired.
- **S4** — `tools/memory-tree/merge-rows.test.sh` gains an end-to-end arm that merges inside a
  linked worktree. Without it the merge-bar leg `row-keyed merge driver replay` cannot reach the
  precondition this defect needs, so it is as blind to the class after the fix as before it.
- **S5** — A backlog row for `tools/drift-audit/drift_report.py:65`, which carries the identical
  defect in a different kit.

## 3. Non-goals (OUT)

- Fixing `tools/drift-audit/drift_report.py:65`. It is a near-verbatim copy of the pre-fix function
  and carries the same defect, verified at source. It is knowingly left: it belongs to a different
  copy-installed kit with its own version marker and its own adopters, git never execs it, and
  folding a second kit's release into this unit is how a fix becomes a migration. S5 files the row.
- Unifying the four `repo_root()` implementations behind one shared function. That is the real class
  fix and it is a unit of its own; §4 names all four so the next reader inherits the map rather than
  re-deriving it.
- Changing `repo_root()`'s anchor from `__file__`. The walk-up strengthens that contract — it removes
  the subprocess that could be steered away from the anchor.
- Any change to `merge-rows.py` itself. Its own root resolution already walks up and is already
  correct; S4 changes its TEST, not it.

## 4. Design

### The failure, reproduced — and its precondition

Git exports `GIT_DIR` to a merge driver. Under an inherited absolute `GIT_DIR` with no
`GIT_WORK_TREE`, `git -C <dir> rev-parse --show-toplevel` reports `<dir>` itself. Measured on node
`a`, 2026-08-26, with a control:

```
control (no GIT_DIR)              -> .../unattended-check-plan-27c557
GIT_DIR set, GIT_WORK_TREE unset  -> .../unattended-check-plan-27c557/tools/memory-recall
```

**The precondition is a LINKED WORKTREE**, and rev-1 stated the failure unconditionally. The spec
audit ran a driver that dumps its environment through two real two-branch merges on git
2.54.0.windows.1: in an ordinary clone `GIT_DIR` is unset and the defect is ABSENT; in a linked
worktree it is set and the defect is PRESENT. That is why S3 and S4 both build worktrees — a fixture
in an ordinary scratch repo cannot fail before the fix, which makes it a test that proves nothing.

`extract.py` resolves `CONF = recall_conf.resolve()` at import, `resolve(None)` calls `repo_root()`,
and the refusal reaching the author is byte-identical to the live one:

```
ConfError: refused: no .memory-tree.conf at .../tools/memory-recall/.memory-tree.conf
```

`merge-rows.py` catches it fail-closed and writes conflict markers, which is correct behaviour over
a broken resolution and is why this cost hand-reconciliation rather than data.

### Inventory — the four root resolvers

Verified at source, 2026-08-26. rev-1 said "the guard belongs in the shared function every caller
routes through", and two of these are not callers of it, so that sentence was false about its own
repo.

| Where | Mechanism | State after this unit |
|---|---|---|
| `tools/memory-recall/recall_conf.py:50` | `-C` + `rev-parse` | S1 — becomes the walk-up |
| `tools/memory-recall/query.py:199` | bare `rev-parse`, no `-C` | S2 — deleted, calls S1's |
| `tools/drift-audit/drift_report.py:65` | copy of the pre-fix function | knowingly left, §3, row in S5 |
| `tools/govkit/govkit.py:83` | walk-up | already correct — the precedent |

### Why the walk-up, and not the environment scrub

rev-1 chose to scrub the inherited git variables and rejected the walk-up on blast radius, citing
"eleven callers". That number was a misread of `reuse_lookup.py`'s fan-in, which is a name-stem
metric across the whole tree; `recall_conf.repo_root` has FOUR call sites outside its own module, in
two files, both already gate-run. With the radius corrected the rejection had no ground left, and
three separate pieces of evidence point the other way:

- `govkit.py:83` already took the walk-up for this exact defect and its docstring names the merge
  driver in a linked worktree as the motivating case. The walk-up is this repo's established answer,
  not a novel alternative.
- A scrub is a DENYLIST that has to be maintained. `.githooks/pre-push:25` already pins eight names
  for this purpose under `TOOL-dScrubbedConduit-1`, and rev-1's list had five. The walk-up inherits
  nothing, so there is no list.
- Every real caller resolves a tree that has `.memory-tree.conf` at its root by contract — `resolve()`
  demands it there — so the walk-up and the git root are the same directory by construction. The
  three `selftest.py` call sites and `check-recall.py:302` all resolve the REAL repo; the scratch
  roots the selftests build are passed explicitly to `resolve(root)` and never reach `repo_root()`.

### Files touched (estimate)

`tools/memory-recall/recall_conf.py` · `tools/memory-recall/query.py` ·
`tools/memory-recall/selftest.py` · `tools/memory-tree/merge-rows.test.sh` · two kit-version markers
· `memory/backlog/TOOL.md`.

## 5. Production-readiness checklist

- security — N/A. Removing a subprocess narrows what the resolution can be steered by.
- perf / scale — the resolution itself gets cheaper: a filesystem walk replaces a `git` exec, on a
  function every module in the kit calls at import. But the kit-version bump feeds
  `recall_conf.Conf.digest()`, which keys cache freshness, so it invalidates every warm recall cache
  and costs one full re-index on the next query — the cost that function's own docstring prices.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the walk-up raises when no ancestor holds the conf, which is the
  same state the `ConfError` already described; the refusal text is unchanged, so the symptom
  recorded in the backlog row stays greppable.
- observability — unchanged wording, deliberately.
- risks — a caller wanting the GIT root of a tree with no `.memory-tree.conf` above the kit would
  change behaviour. None exists: `resolve()` requires the conf at the root it is handed.
- testing + left-shift gates — S3 is the function-level regression, S4 is the class-level one on the
  merge bar. Both are observed RED before the fix.
- migration / rollback — a two-function revert.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — When `recall_conf.repo_root()` is called from inside a linked worktree with `GIT_DIR`
  inherited, it returns the repository root, proven by a test that FAILS against the pre-fix
  function and passes after.
- **AC2** — When `grep -n "def repo_root" tools/memory-recall/*.py` runs, exactly one definition
  remains in the kit.
- **AC3** — When `bash tools/memory-tree/merge-rows.test.sh` runs, it passes AND its new
  linked-worktree arm is observed RED against the pre-fix `recall_conf.py`.
- **AC4** — When a merge that conflicts `memory/backlog/TOOL.md` is replayed inside this worktree,
  `merge-rows.sh` completes with no `ConfError` and no conflict markers.
- **AC5** — When `python tools/memory-recall/selftest.py` and `python tools/memory-recall/check-recall.py`
  run, they pass.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs, the bar is green.

## 7. Gates

`memory hygiene` · `row-keyed merge driver replay` · `row-grammar selftest` · the memory-recall kit
legs · the full bar. S4 strengthens an existing leg rather than adding one.

## 8. Open questions

- **F1 — walk-up, or scrub the inherited git environment?** RESOLVED (agent, 2026-08-26, delegated):
  the walk-up. rev-1 resolved this the other way on a blast-radius figure that turned out to be a
  fan-in misread; §4 carries the corrected radius, the govkit precedent and the denylist argument.
  This is a re-decision on evidence, not a reversal on taste.
- **F2 — fold `drift_report.py:65` in as well?** RESOLVED (agent, 2026-08-26, delegated): no, and
  §3 states the reason rather than leaving it as an omission. S5 files the row so the identical
  defect is recorded rather than merely known.
- **F3 — unify all four resolvers?** RESOLVED (agent, 2026-08-26, delegated): out of scope. It is
  the class fix and it crosses three kits' release boundaries; §4's table is what a later unit
  starts from.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, written after the failure was reproduced with a control.
- rev-2 · 2026-08-26 · folded the round-1 spec audit. F1 RE-DECIDED to the walk-up on three pieces
  of evidence rev-1 did not have: `govkit.py:83` had already taken it for this exact defect and says
  so, the "eleven callers" blast radius was a fan-in misread (four call sites, two files), and a
  scrub is a denylist `.githooks/pre-push` already pins at eight names. Added the linked-worktree
  PRECONDITION and S4, without which the merge-bar leg cannot reach the class. Added S2 (a second
  resolver in the same kit) and S5, corrected the four-resolver inventory, and priced the cache
  invalidation the version bump causes.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve the repository root for a kit invoked by git"`
ranks `recall_conf.resolve` (fan-in 26) and `recall_conf.repo_root` (fan-in 11) first, and rev-1
took that second figure as a call-site count. It is a name-stem metric across the tree; the real
count is four call sites in two files, which is what re-opened F1.

The seam this unit extends is `recall_conf.repo_root`, and the MECHANISM it adopts is
`tools/govkit/govkit.py:83`'s — the walk-up, already written in this repo for this defect, with the
merge driver in a linked worktree named in its docstring. §4's table records all four resolvers so
the next unit does not re-derive them. Recall terms used: `duplicate id backlog shard decision log
hygiene check merge driver row-keyed conflict ceiling budget gate leg check-30 population liveness`.
