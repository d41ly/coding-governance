# Acceptance ledger — DEPL-dRetiredFork-4

**Serves:** journal DEPL-dRetiredFork-4

Tier-1 · node d · 2026-09-03

## Acceptance criteria

**Evidences:** DEPL-dRetiredFork-4

- AC1 — MET — `git_pathspec` feeds the pathspec over stdin, and the arm builds a **40,500-byte**
  pathspec (500 names) and observes the command succeed with all 500 paths reaching git
- AC2 — MET for the class this unit owns, NOT as a general restructure. `git_pathspec` REFUSES an
  empty path list rather than running, because git then reads no pathspec at all and operates on the
  whole tree — the difference between `add -- <nothing>` and `add -A`. A general "refuse before the
  write loop for any reason" is not built and is not claimed
- AC2b — MET — a grep for a derived population passed as argv returns ZERO. The five converted sites
  are named below, and the one deliberately NOT converted is named too
- AC3 — MET — `python tools/govkit/selftest.py` reports all arms held with the S3 arm added
- AC4 — MET — `python tools/govkit/govkit.py selfcheck` exits 0

## The RED half fired on this host, not in theory

```
ok   [-4] S3 the fixture pathspec really exceeds the 32 KiB command line   (40,500 bytes)
ok   [-4] S3 a >32 KiB pathspec over STDIN succeeds
ok   [-4] S3 ...and every path in it actually reached git                  (500 of 500)
ok   [-4] S3 ...where the SAME list through argv still dies
```

The arm carries a skip branch for a platform whose command line is larger, which announces itself
rather than passing quietly — but it was not needed here. Both halves are live on node `d`.

## The class, enumerated — AC2b

Five sites concatenated a derived population into a git argv, and all five now go over stdin:

| site | call | population |
|---|---|---|
| `:4349` | `add --` | `staged` — grows with the install |
| `:4512` | `diff --name-only HEAD --` | `lf_paths` — **the reported crash** |
| `:4521` | `add --renormalize --` | `lf_paths` |
| `:4525` | `ls-files --eol --` | `lf_paths` |
| `:6416` | `rm -q --ignore-unmatch --` | `deleted` — update's withdrawals |

**`index_read` is NOT in the class**, and is named so the enumeration is complete rather than
convenient: it already chunks at 400 paths, which is a different mitigation for the same bound.

rev-1 fixed only the reported call site; rev-2 added AC2b because a unit whose scope item states the
class rule and whose criteria observe one instance can pass with the class still open. Four of these
five were invisible to the crash report.

## The fix removes the bound rather than raising it

`--pathspec-from-file=-` with `--pathspec-file-nul`. A chunking loop would leave the same class open
at a larger size, and the failure would then be rarer and harder to attribute — worse than a bound
you can name.

NUL-separated because a path may contain any byte but NUL; the newline form would split a path whose
name contains a newline into two pathspecs matching nothing, which is a silent wrong answer where
this one is at least loud.

## Two declarations the change made stale, and the gate caught both

Adding a function that spawns reds until `SHELL_EXEC_SITES` declares it — expected, and added as
`gov`, since no target value reaches the argv it builds.

The second was the interesting one. `_cmd_update` held a row for exactly ONE shape — the BinOp
`git rm ... + deleted` the census cannot destructure — and converting that call made the row stale.
The table asserts in BOTH directions, so it redded on "declared but no longer spawning", and a
paired map in the selftest redded the same way when only one side was removed.

That is the declared-population discipline doing precisely what it exists for: a stale row cannot
quietly widen the surface it was written to narrow.
