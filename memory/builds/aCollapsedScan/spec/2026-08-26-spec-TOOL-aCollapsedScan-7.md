# TOOL-aCollapsedScan-7 — `repo_root()` scrubs the inherited git environment before it asks git

**Status:** INPROGRESS · rev-1 · 2026-08-26 · node a · Tier-2 · base 3c37a1fb · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make the memory-recall kit resolve the repository root correctly when it is invoked from inside a
git subprocess environment. Today it does not, so `merge-rows.py` — the row-keyed merge driver git
execs for `memory/DECISIONS.md` and `memory/backlog/*.md` — aborts on every merge of those files and
hands the author a conflict instead of a merge.

## 2. Scope (IN)

- **S1** — `recall_conf.repo_root()` runs its `git rev-parse --show-toplevel` with the inherited
  git environment variables removed from the child's environment, so the `-C <kit dir>` anchor it
  documents is the only thing deciding the answer.
- **S2** — A regression test that reproduces the failure: with `GIT_DIR` set and `GIT_WORK_TREE`
  unset, `repo_root()` returns the repository root and not the kit directory. It must fail against
  the current function, which is observed before the fix is wired.
- **S3** — The kit-version marker bumped where the kits this touches declare one, so an adopter can
  tell a fixed copy from a broken one.

## 3. Non-goals (OUT)

- Changing `repo_root()`'s anchor from `__file__` to anything else. Its docstring states why the
  anchor is the file and not the cwd, and this unit strengthens that contract rather than replacing
  it.
- Replacing the `rev-parse` with the conf walk-up that `merge-rows.py:_anchor_root()` uses. That
  walk-up is correct for its caller, which wants the conf's directory; `repo_root()` has eleven
  callers and answers a different question. Changing what it MEANS to fix where it is CALLED is the
  larger blast radius, and §4 records the test that separated the two.
- Any change to `merge-rows.py`. The defect is not there — its own root resolution is already
  correct and its comment already documents why `rev-parse` cannot be trusted at that call site.
- Auditing the other ten callers of `repo_root()` for the same environment. None of them is invoked
  by git, and widening the unit to prove that would be a survey rather than a fix.

## 4. Design

### The failure, reproduced

Git invokes a merge driver with `GIT_DIR` set and `GIT_WORK_TREE` unset. Under that environment
`git -C <dir> rev-parse --show-toplevel` reports `<dir>` itself, because with `GIT_DIR` set and no
work tree named, git treats the current directory as the work tree root. Measured on node `a`,
2026-08-26, with a control:

```
control (no GIT_DIR)              -> .../unattended-check-plan-27c557
GIT_DIR set, GIT_WORK_TREE unset  -> .../unattended-check-plan-27c557/tools/memory-recall
```

`extract.py` resolves `CONF = recall_conf.resolve()` at import, `resolve(None)` calls `repo_root()`,
and the refusal that reaches the author is byte-identical to the one seen in the live merges:

```
ConfError: refused: no .memory-tree.conf at .../tools/memory-recall/.memory-tree.conf
```

`merge-rows.py` catches it fail-closed and writes conflict markers, which is correct behaviour over
a broken resolution and is why this cost nothing but hand-reconciliation.

### Data model

None. One subprocess call gains an explicit environment.

### Migration

None. The function's return value changes only in the environment where it was wrong.

### Alternatives rejected

- **The conf walk-up from `__file__`**, as `merge-rows.py:_anchor_root()` does. It needs no
  subprocess and cannot be fooled by any environment, which makes it the more robust mechanism in
  isolation. Rejected on blast radius: `repo_root()` has fan-in 11 and answers "the git root", while
  the walk-up answers "the nearest ancestor holding the conf". Those coincide in this repo and are
  not the same question, and eleven callers is too many to re-decide inside a fix.
- **Scrubbing the environment in `merge-rows.py` before the deferred import.** It fixes the one
  caller that is broken today and leaves the defect in place for the next kit git ever execs. The
  guard belongs in the shared function every caller routes through.

### Files touched (estimate)

`tools/memory-recall/recall_conf.py` and its test file. A kit-version marker.

## 5. Production-readiness checklist

- security — N/A. Removing inherited variables from a child environment narrows what the subprocess
  can be steered by; it widens nothing.
- perf / scale — unchanged. Same one subprocess.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the `ConfError` path is unchanged and still fires when the conf
  is genuinely absent; only the wrong root that provoked it spuriously is removed.
- observability — the refusal text is unchanged, which matters: the recorded symptom in
  `TOOL-aCollapsedScan-7`'s backlog row stays greppable against the fixed code.
- risks — a caller that deliberately set `GIT_DIR` to steer this function would change behaviour.
  None exists: the function's docstring says it anchors on the file, so any such caller was already
  relying on a contradiction.
- testing + left-shift gates — S2 is the regression test, and the class is left-shifted as the
  gotcha `inputs-inside-the-subjects-reach` already names.
- migration / rollback — a single-function revert.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — When `repo_root()` runs with `GIT_DIR` set and `GIT_WORK_TREE` unset, it returns the
  repository root, proven by a test that FAILS against the pre-fix function and passes after.
- **AC2** — When a merge that conflicts `memory/backlog/TOOL.md` is replayed, `merge-rows.sh`
  completes without a `ConfError` and without conflict markers, observed on a real conflicting pair.
- **AC3** — When `bash tools/memory-tree/merge-rows.test.sh` runs, it passes.
- **AC4** — When `python tools/memory-recall/check-recall.py` and the recall kit's own tests run,
  they pass.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs, the bar is green.

## 7. Gates

`memory hygiene` · `row-keyed merge driver replay` · `row-grammar selftest` · the memory-recall kit
legs · the full bar. The new regression test rides the recall kit's existing suite rather than
adding a leg, because a leg per function is how a manifest stops being readable.

## 8. Open questions

- **F1 — scrub which variables?** `GIT_DIR` alone is the one measured to cause this.
  RESOLVED (agent, 2026-08-26, delegated): scrub the whole `GIT_*` family that redirects a
  repository — `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_COMMON_DIR`,
  `GIT_OBJECT_DIRECTORY`. Scrubbing only the variable whose failure was observed leaves the same
  defect reachable through its siblings, which is the fix-the-instance-not-the-class shape the
  charter names.
- **F2 — should `merge-rows.py` also stop depending on import-time resolution?** RESOLVED (agent,
  2026-08-26, delegated): out of scope, and recorded as an observation rather than a defect. The
  import-time `CONF` in `extract.py` is what turns a bad root into an exception at import, which is
  what made this diagnosable at all.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, written after the failure was reproduced with a control.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve the repository root for a kit invoked by git"`
ranks `recall_conf.resolve` (fan-in 26, SEAM) and `recall_conf.repo_root` (fan-in 11, SEAM) first.
That IS the seam and this unit extends it rather than adding a second root resolver beside it — the
kit already has two answers to "where is the root", `repo_root()` and `merge-rows.py:_anchor_root()`,
and a third would be the `two-answers-to-one-question` class the checklist selected for these paths.
Recall terms used: `duplicate id backlog shard decision log hygiene check merge driver row-keyed
conflict ceiling budget gate leg check-30 population liveness`.
