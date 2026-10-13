# TOOL-dSweptBranches-4 — the worktree remover: git first, then `rm -rf`, and a skeleton removed only when it holds no regular file

**Status:** OPEN · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md) | research | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-5 |

<!-- /gen:spec-records -->

## 1. Goal

`remove_worktree` in `branch_reconcile.py` removes a linked worktree on Windows and POSIX alike,
through the failures one inCMS session measured on 2026-10-13: a git removal that fails on deep
`node_modules`, a directory that survives as an empty skeleton of MSYS links, Windows deleters that
refuse those links, and a directory a desktop session holds as its working directory.

## 2. Scope (IN)

- **S1** — `git worktree remove --force --force <path>` first. On a non-zero exit, GNU `rm -rf
  <path>` and then `git worktree prune`. Observed by AC1.
- **S2** — When the directory survives a clean removal, it is a skeleton candidate. A walk with
  `os.scandir` that follows no link and no junction counts the regular files beneath it, and a
  reparse point never counts. Zero regular files: `rm -rf <path>`. Any regular file: the directory is
  kept and the row reports the count. Observed by AC2 and AC3.
- **S3** — No link is resolved. No `readlink` is spawned, and the walk asks only `is_dir` and
  `is_file` with `follow_symlinks=False`. Observed by AC2.
- **S4** — An `rm` that fails with `Device or resource busy` is reported as `busy`, a result and not a
  failure. Any other `rm` failure is a failure. Observed by AC4.
- **S5** — `rm` is found on `PATH`. When none is found, the fallback and the skeleton step report a
  `skipped` line and the row fails, rather than reaching for `cmd rmdir` or .NET, which refuse MSYS
  links. Observed by AC5.

## 3. Non-goals (OUT)

- No removal of the primary worktree. Unit 3 never hands it here.
- No use of `cmd rmdir /s /q`, PowerShell `Remove-Item` or .NET `Directory.Delete`.
- No killing of a process that holds a directory.

### Edges

- **hands-off** `TOOL-dSweptBranches-3` — the remover write mode calls.

## 4. Design

`remove_worktree(root, path) -> (result, detail)` where the result is `removed`, `busy`, `kept` or
`failed`. The walk is iterative over `os.scandir` with `follow_symlinks=False` on every test. On
Windows a junction or a symlink reports `is_dir(follow_symlinks=False)` as false. The entry's
`stat(follow_symlinks=False).st_file_attributes` is read there and checked for
`FILE_ATTRIBUTE_REPARSE_POINT`, so a reparse point is never descended or counted. The walk stops at
the first regular file, because the answer is binary.

The `busy` match reads `rm`'s stderr for `Device or resource busy` or `EBUSY`, and the error text is
kept in the detail. The self-test drives the fallback by replacing the git removal with one that
fails, through the module seam, and builds a skeleton of empty directories and dangling links where
this node can create links; where it cannot, that arm prints a skip line.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`
- `memory/map/features/branch-reconcile.md`

### Alternatives rejected

- `shutil.rmtree`. Whether it follows a junction depends on the Python version, and the inCMS run
  observed only GNU `rm -rf` removing the MSYS link skeletons.
- Resolving each link before deleting it. One spawned `readlink` per link timed out at 600 s over
  40 directories.

## 5. Production-readiness checklist

- security — `rm -rf` runs on a path the inventory read from `git worktree list`, never on the primary
  and never on a path the skeleton check found a regular file under.
- perf / scale — the walk stops at the first regular file; an empty skeleton is a directory walk.
- error / empty / loading states — S4 and S5.
- observability — the result and its detail on the action line.
- risks — deleting a directory that still holds work. S2's zero-file assertion guards the skeleton
  path, and the git removal guards the first path.
- testing — AC1 to AC5.
- migration — N/A.
- user docs — the kit README's Windows removal section.

## 6. Acceptance criteria

- **AC1** — When the git removal is made to fail, `remove_worktree` removes the directory with
  `rm -rf` and `git worktree list` no longer names it.
  Red when: the fallback is removed.
- **AC2** — When a removed worktree leaves a skeleton of empty directories and dangling links,
  `remove_worktree` removes it and reports `removed`, and no `readlink` process is spawned.
  Red when: the skeleton step is removed, or the walk follows a link.
- **AC3** — When the skeleton holds one regular file, `remove_worktree` keeps it and reports
  `kept · 1 regular file`.
  Red when: the zero-file assertion is removed.
- **AC4** — When `rm` reports `Device or resource busy`, `remove_worktree` returns `busy` and write
  mode's exit is not 1 for it.
  Red when: busy is classed as a failure.
- **AC5** — When `rm` is absent from `PATH`, `remove_worktree` reports a skip naming `rm` and fails
  the row.
  Red when: it falls back to another deleter.

## 7. Gates

`codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 AC2 AC3 AC4 AC5 · a linked worktree per arm, with the removal seam replaced where the arm needs a failure · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`remove_scratch_worktree` in `tools/run-gates/lib-attribute.sh` removes a worktree with
`git worktree remove --force` and no fallback. It is shell and handles only a directory the runner
made, so it is not reused. `reuse_lookup.py` returned no directory remover that walks without
following links.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
