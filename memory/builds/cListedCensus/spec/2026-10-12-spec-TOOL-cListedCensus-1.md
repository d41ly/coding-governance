# TOOL-cListedCensus-1 — ps-hygiene grades the tracked `.ps1` files, and refuses a population it could not derive

**Status:** INPROGRESS · rev-2 · 2026-10-13 · node c · Tier-2 · base 6e8f8b1d · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-cListedCensus-1-brief.md](../prompts/2026-10-12-prompt-TOOL-cListedCensus-1-brief.md) | research | — |
| [2026-10-13-review-TOOL-cListedCensus-1-implementation-diff-round1.md](../reviews/2026-10-13-review-TOOL-cListedCensus-1-implementation-diff-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/gate-lint/ps-hygiene.py` takes its population from `git ls-files -z`, keeping the `.ps1`
suffix in any case, instead of a walk of the disk. An adopter that parks linked worktrees inside its primary tree then stops getting
reds on files its commit does not hold. A dead probe and an empty population each refuse with exit 2,
the same posture `tools/gate-lint/sh_hygiene.py` already takes.

## 2. Scope (IN)

- **S1** — `scan(root)` lists its files with `git ls-files -z` run with `cwd=root` and no pathspec,
  keeps each distinct entry whose name ends in `.ps1` in any case, grades each one that is a file,
  and returns `(findings, scanned)`. A non-zero git exit raises `OSError`. The walk and its
  `SKIP_DIRS` prune are deleted, because the set existed only to prune the walk. Observed by AC1 and
  AC2.
  **Readers:**
  by name: `tools/gate-lint/ps-hygiene.py` itself, in the walk inside `scan` and the recount inside
  `main`, both deleted with it.
  by value: NO VALUE READERS — no other file compares, counts or derives from the set.
- **S2** — `main` prints an `OSError`, or a `ValueError` from a listing that does not decode, and
  exits 2. It exits 2 with a line saying the run graded NOTHING when no tracked `.ps1` exists. Its
  clean and finding lines count tracked files. Observed by AC1 and AC3.
- **S3** — `--selftest` gains five arms over a scratch git repository, with `GIT_DIR`,
  `GIT_WORK_TREE` and `GIT_INDEX_FILE` held out of the environment for their length.
  `GIT_CEILING_DIRECTORIES` is pinned to the scratch directory, so the not-a-repo arm cannot find a
  parent repository. The arms: a directory that is no repository raises `OSError`, and `main` refuses
  naming the dead listing; a repository whose one tracked `.ps1` is gone from disk, beside an
  untracked one, refuses as empty; a tracked clean file passes as `OK — 1 tracked .ps1 file(s)` while
  a BOM-less non-ASCII copy sits untracked under `.claude/worktrees/x/`; staging that copy reds; a
  tracked BOM-less sub/ü.PS1 reds. Observed by AC1.
- **S4** — The docs say what the scanner now does: `tools/gate-lint/README.md` (usage exit codes,
  "every tracked", the suffix in any case, and the closing paragraph that promised `0 files clean`),
  the kit line in the root `README.md`, the gate-lint bullet in `WIRE-INTO-PROJECT.md`, and the gap
  bullet and command line in `memory/map/features/gate-lint.md`. Observed by AC5.
- **S5** — A gov class record, `memory/gotchas/a-gate-that-walks-the-repo-root-reads-other-worktrees.md`,
  adapted from nc's record of the same name. The gate-lint dossier claims it. Observed by AC4.

## 3. Non-goals (OUT)

- No leg runs `ps-hygiene.py`, and `tools/gate-lint/kit.toml` is unchanged. Gov tracks no `.ps1`, so a
  leg here would refuse on every run. Wiring a leg that adopters with PowerShell receive is a later
  unit.
- `.psm1` and `.psd1` stay out of the population, as they were.
- No fix and no class gate for the other walks the survey names, `tools/codebase-map/map_lib.py` and
  `tools/workflows/check_by_design_parity.py`. The class record lists them.
- No scrub of an inherited `GIT_DIR` in the scanner's own `git ls-files`. `sh_hygiene.py`'s
  `scan_tree` takes the same posture, and a scrub would also drop a hook's `GIT_INDEX_FILE`, which
  names the index a commit is being built from.
- No merge to main and no push without the owner's ask.

### Edges

none

## 4. Design

The population is the index's answer to "which `.ps1` files does this commit hold", read with `cwd`
at the root, so a root below the toplevel lists only its own subtree, with paths relative to it.
The listing takes no pathspec and the suffix is matched case-insensitively: a pathspec glob is
case-sensitive even under `core.ignorecase`, so nc's `-- '*.ps1'` dropped a tracked `Deploy.PS1` that
the walk graded on Windows (closing review H1). No pathspec also means no `GIT_*_PATHSPECS` variable
can narrow it. `-z` keeps a non-ASCII name unquoted. A set drops the repeat entries an unmerged path
gets, one per stage. A listed path absent from disk, an unstaged deletion or a skip-worktree entry,
is skipped and not counted, as in both sibling scanners. The refusals are nc's `bcc6f8a4`; the
module docstring keeps nc's TRACKED, not walked paragraph.

The refusal is two-sided by construction. `OSError` means the probe died, and a `ValueError` from a
listing that does not decode is the same verdict. `scanned == 0` means the probe answered, and its
answer is that nothing here is graded. Both print to stderr and exit 2, and neither is spelled the
same way as a clean tree.

The selftest arms build their fixture under `tempfile.TemporaryDirectory()`. Each arm asserts the
refusal's REASON, not only its exit: the not-a-repo arm catches `OSError` from `scan` and requires
`main`'s output to name the dead listing and not the empty one, and the empty arm asserts
`scanned == 0` with no exception. An arm that saw exit 2 for the wrong reason would otherwise pass.
The untracked arm's fixture is proven live by its control: the same bytes, staged, red.

### Files touched (estimate)

- `tools/gate-lint/ps-hygiene.py`
- `tools/gate-lint/README.md`
- `README.md`
- `WIRE-INTO-PROJECT.md`
- `memory/map/features/gate-lint.md`
- `memory/gotchas/a-gate-that-walks-the-repo-root-reads-other-worktrees.md`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- Adding `.claude` or `worktrees` to `SKIP_DIRS`. That was nc's first fix, `PKG-bStitchedFerry-3`. It
  names one adopter's layout, and a walk still grades every other untracked file.
- A walk filtered through `git check-ignore`. An untracked file that is not ignored, which is what a
  nested worktree is, still passes the filter.
- The pathspec `:(glob,icase)**/*.ps1` (closing review id 1). It is also case-insensitive, but a
  plain listing with a suffix filter is the shape `encoding_posture.py` already takes, and no
  pathspec magic is left for an environment variable to change.

## 5. Production-readiness checklist

- security — N/A: the scanner reads bytes and runs one fixed `git` argv with no shell and no input
  interpolated into it.
- perf / scale — one `git ls-files` replaces a walk of the whole disk tree, worktrees included, so it
  costs less.
- error / empty / loading states — S2's two refusals are the subject of this unit.
- observability — the clean and finding lines print the tracked file count and the root.
- risks — an adopter that wired `ps-hygiene.py . || exit 1` with no tracked `.ps1` goes from green to
  red on its next pull. That is the intended verdict; the README says so.
- testing — S3's five arms, each observed red under a staged break of the line it guards (AC1). The
  dedup and the `ValueError` catch carry no arm: the first needs a conflicted merge and moves only a
  count, and the second needs a non-UTF-8 name or locale this node cannot stage.
- migration — N/A: no stored state. nc retires its carve-out on its own next pull.
- user docs — S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/gate-lint/ps-hygiene.py --selftest` runs, it exits 0 and prints its
  pass line, with the five population arms executed.
  Red when: the population reverts to `root.rglob("*.ps1")`, or the BASE recount returns to `main`
  (the empty and untracked arms red); the `scanned == 0` refusal is removed, or the count moves above
  the on-disk skip (the empty arm reds); the `returncode` check is removed, or `main` turns a dead
  listing into an empty one (the not-a-repo arm reds); a `.claude` prune replaces the listing (the
  control reds); the listing takes `-- '*.ps1'`, the suffix match turns case-sensitive, or `-z` is
  dropped (the sub/ü.PS1 arm reds). Each break is staged once and observed red before this unit
  closes.
- **AC2** — When the BASE scanner and the new one each run with `cwd` at nc's primary tree
  (`C:/projects/incms/main/vendor/nicocares-package`, 11 nested worktrees, 1 tracked `.ps1`), BASE
  exits 1 with every finding under `.claude/worktrees/` and the new one exits 0 on 1 tracked file.
  Red when: the population is a walk.
- **AC3** — When `python tools/gate-lint/ps-hygiene.py .` runs in gov, which tracks no `.ps1`, it
  exits 2 and its stderr says the run graded NOTHING.
  Red when: the zero refusal is removed, which prints `OK — 0` and exits 0.
- **AC4** — When `python tools/memory-tree/gotchas.py --for-paths tools/gate-lint/ps-hygiene.py`
  runs, its checklist names `a-gate-that-walks-the-repo-root-reads-other-worktrees`, and the bar's
  codebase-map and memory-hygiene legs are green over the edited dossier, README and record.
  Red when: the record names no anchor path, or the dossier does not claim it.
- **AC5** — When `git grep -nE 'ps-hygiene|gate-lint/|\.ps1' -- README.md WIRE-INTO-PROJECT.md
  tools/gate-lint/README.md memory/map/features/gate-lint.md` runs, every hit that states the
  scanner's population says tracked files, and every hit that states its verdict on a repository
  with no `.ps1` says exit 2.
  Red when: a hit still promises a clean report or `0 files clean` for an empty population.

## 7. Gates

`recall floor` · `recall floor arms` · `shell-hygiene selftest`

New arm: `tools/gate-lint/ps-hygiene.py` --selftest · covers AC1 · a scratch repository staged per arm, with the guarded line broken once by hand · none

The `--selftest` arms run on no leg: `ps-hygiene.py` is on none. `shell-hygiene selftest` is owed
because its guard is the kit directory, but it runs `sh_hygiene.py`'s suite, and it is held under
`subject = "kit"`. The bar's green therefore does not observe this unit; AC1 to AC3 do.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.
- rev-2 · 2026-10-13 · closing review round 1 folded, all ten items: the listing takes no pathspec
  and matches the suffix in any case, deduplicates, and routes a `ValueError` to exit 2 (H1, L4, L5);
  the header names every exit-2 cause (L1); the selftest gains the sub/ü.PS1 arm, the on-disk skip
  in the empty arm, the dead-listing reason and the clean line's count (H1, L6, L7, L8); the runbook
  bullet and the class record are corrected (M1, L3, L2); S1, S2 and S4 cite criteria that read their
  surface, and AC5 is new (L8); §4's skip rationale is corrected (L6). H1's two sibling instances are
  `TOOL-cListedCensus-2`.

## 10. Reuse audit

The seam is `scan_tree` in `tools/gate-lint/sh_hygiene.py`: the same `git ls-files -z` listing, the
same `OSError` for a dead probe and the same zero-population refusal in `main`. The suffix filter is
`encoding_posture.py`'s shape, made case-insensitive. Its selftest's
scratch-repository block is the shape S3 copies, environment hold included. `reuse_lookup.py` ranked
only name-token neighbours (`git`, `population`, `CensusRefused`) and named no population helper to
call. `tools/gate-lint/encoding_posture.py` carries the same listing, so this is the third copy, and
none is extracted here. Each scanner is a single file run by path that imports no sibling, and an
adopter that carves out one file must be able to take it alone. Extracting a shared listing would
rewrite both siblings, which is OUT. nc's `bcc6f8a4` is the implementation this unit takes.

Recall terms used: "why is ps-hygiene on no leg and how does a gate-lint scanner derive its
population and refuse an empty one" --terms "ps-hygiene gate-lint population git ls-files tracked
refusal empty population graded nothing dead probe leg-wiring sh_hygiene scan_tree adopter"
