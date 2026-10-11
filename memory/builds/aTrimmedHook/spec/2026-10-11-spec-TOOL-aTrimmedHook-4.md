# TOOL-aTrimmedHook-4 — the staged classifier reads the index the hook was handed

**Status:** SPECCED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing review's H1. `check_staged_render` reads the staged set and the index blobs with
`_build_git_env()`, which drops `GIT_INDEX_FILE`, while the hygiene shell that calls it reads the
index it inherits. Under `git commit -a`, `git commit <paths>` or `git commit -i`, git hands the
pre-commit hook a temporary index, so in an adopter whose hook does not unset that variable the
classifier reads the stale `.git/index` and prints a false SKIPPED. This unit makes the classifier
read the index the hook was handed, so both readers answer about one index.

## 2. Scope (IN)

- **S1 — one index for both readers.** In `tools/memory-tree/gen_build_index.py`,
  `check_staged_render` runs its two git calls with `_build_git_env()` plus `GIT_INDEX_FILE` carried
  through from the process environment when it is set. Every other git call in the module keeps the
  scrubbed environment. Observed by AC1 and AC2.
- **S2 — the arm.** `test_staged_render` gains an arm that writes a structural edit into a temporary
  index with `GIT_INDEX_FILE`, leaves `.git/index` holding nothing staged, sets the variable for the
  call, and expects a render owed. Observed by AC1.

## 3. Non-goals (OUT)

- **N1** — gov's own `.githooks/pre-commit` unsets `GIT_INDEX_FILE` before the legs run, so under
  `commit -a` both readers there read `.git/index`. That is pre-existing and unchanged; it is the
  hook's choice, not the classifier's.
- **N2** — no change to `_build_git_env()` or `_GIT_ENV_LEAKS`, which every other mode relies on.
- **N3** — the adopter pre-commit snippets in the kit README and `WIRE-INTO-PROJECT.md` are not
  edited.

### Edges

none

## 4. Design

`_GIT_ENV_LEAKS` exists because a generator started from a hook inherits pointers to a different
tree. `GIT_INDEX_FILE` is the exception for this one function: the staged set IS the index the hook
holds, and the hygiene shell, which decides that the classifier runs at all, reads that same index
through its own `git diff --cached`. Carrying the variable makes the two readers agree. The value is
used as git exports it; git exports an absolute path to hooks, and a relative one resolves against
the repository root, which is the cwd of both the hook and this call.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`

### Rollout

Order 3. Units 5 and 7 also write this file and follow it.

### Alternatives rejected

- **The shell passes its name-status list on stdin.** The shell then becomes the one reader of the
  staged set, but the classifier still reads blobs through `:<path>`, which needs the same index, so
  the variable is owed anyway; the stdin channel would add a second interface for no gain.

## 5. Production-readiness checklist

- security — N/A — the variable names an index of the same repository, which the shell already reads.
- perf / scale — N/A — no extra process.
- error / empty / loading states — an unset variable is the default index, as before.
- observability — N/A — the skip line is unchanged.
- risks — a stray `GIT_INDEX_FILE` outside a hook now steers the classifier as it already steers the
  shell's `git diff --cached`, so the two still agree.
- testing — AC1 is a `--selftest` arm; AC2 reads the source.
- migration — none.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `gen_build_index.py --selftest` runs, the arm that stages a build README edit only
  into a temporary index named by `GIT_INDEX_FILE` sees a render owed; with the variable dropped from
  the classifier's environment, the same arm sees a skip, which is the arm observed RED.
  Red when: the arm sees a skip with the variable carried.
  cost: one fixture repo; seconds.
- **AC2** — When `grep -n GIT_INDEX_FILE tools/memory-tree/gen_build_index.py` runs, the hits are the
  leak list entry and the carry inside `check_staged_render`, and no other function reads the variable.
  Red when: another function reads it.

## 7. Gates

`build-index selftest` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: tools/memory-tree/gen_build_index.py test_staged_render · covers AC1 · `GIT_INDEX_FILE` dropped from the classifier's environment · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, promoted from the closing review's H1.

## 10. Reuse audit

The seam is `_build_git_env()` in `tools/memory-tree/gen_build_index.py`, extended at its one
staged caller rather than changed for all. `python tools/codebase-map/reuse_lookup.py "read the index
a git hook was handed"` returned only name-stem matches. Recall named the hook environment scrub,
`TOOL-dScrubbedConduit-1`, which is why every other caller keeps the scrubbed environment.

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
