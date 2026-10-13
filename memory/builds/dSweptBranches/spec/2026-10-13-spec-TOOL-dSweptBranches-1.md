# TOOL-dSweptBranches-1 — the census: the branch-reconcile kit, its remote ladder, the inventory and a byte-stable report

**Status:** OPEN · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md) | research | TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 |

<!-- /gen:spec-records -->

## 1. Goal

A new kit, `tools/branch-reconcile/`, ships a read-only CLI that lists every worktree, local branch,
remote branch and stash entry of the repository it runs in, with each worktree's location kind and
dirty state, as one report that is byte-identical across two runs over an unchanged repository.
Every row's verdict is `UNKNOWN` in this unit, from a stub that unit 2 replaces.

## 2. Scope (IN)

- **S1** — `branch_reconcile.py` resolves the remote and the default branch with the canonical
  `remote_ladder_py` block from `tools/lib/resolve_remote.py`, inlined byte-identically. An empty
  branch from the ladder falls back to `main`, then `master`, whichever exists on the remote or
  locally. The default ref is `refs/remotes/<remote>/<branch>` when it resolves, else
  `refs/heads/<branch>`, announced. A ladder refusal, a directory that is no repository, and a
  default branch that resolves nowhere each exit 2 with the reason. The tool fetches nothing.
  Observed by AC3.
- **S2** — The inventory. Worktrees come from `git worktree list --porcelain -z`. Each worktree is
  given one location kind: `primary`, `nested` (under `<primary>/.claude/worktrees/`), `temp` (under
  the system temp directory), `sibling` (its parent is the primary's parent) or `elsewhere`. Its
  flags are `detached`, `prunable`, `locked` and `bare`. Local branches come from `refs/heads`,
  remote branches from `refs/remotes/<remote>` without its `HEAD`, and stash entries from
  `git stash list`. Observed by AC1.
- **S3** — Each worktree's dirty state, from `git status --porcelain=v2 -z --untracked-files=all`:
  staged, unstaged, untracked and unmerged counts, an in-progress merge (`MERGE_HEAD`) or rebase
  (`rebase-merge` or `rebase-apply`), and submodule-pointer drift. An untracked path that is
  another inventoried worktree, or contains one, is not counted. A prunable worktree's state is not
  read, and the row says so. Observed by AC1 and AC4.
- **S4** — The report. A header line names the remote, the default branch, its tip and the counts.
  A `skipped — <predicate> · <why>` line names every predicate that could not run. Then one row per
  item: `<VERDICT> · <kind> · <name> · <tip12> · <tip date> · age <n>d · <action> · <evidence>`.
  The age is whole days from the tip's commit date to the default tip's, so the report reads no
  clock. Rows sort by verdict rank, then kind, then name. Observed by AC1 and AC2.
- **S5** — The verdict seam: one function per verdict predicate, each a stub returning "not decided"
  in this unit, and a ladder that reads them in order and falls to `UNKNOWN` with the evidence
  `no predicate decided`. Unit 2 replaces the stubs. Observed by AC5.
- **S6** — The kit's carriers: `kit.toml`, `README.md`, the `govkit` registry entry, the
  `branch-reconcile selftest` leg in `tools/gate-legs.json` with its subject pin, budget row and
  exempt row, the codebase-map dossier, and the kit lines in the root `README.md`,
  `WIRE-INTO-PROJECT.md` and `.claude/rules/product.md`. The README states why the relocation
  engine's `--stragglers` inventory is a different population. Observed by AC6.

## 3. Non-goals (OUT)

- No verdict other than `UNKNOWN`, which is unit 2. No write mode, which is unit 3. No directory
  removal, which is unit 4. No skill, which is unit 5.
- No fetch. The skill fetches before it runs the tool.
- No JSON or TSV output: the skill reads the text report.
- No consumption of `migrate_backlog.py --stragglers`.

### Edges

- **hands-off** `TOOL-dSweptBranches-2` — the stub predicates and the ladder's order.
- **hands-off** `TOOL-dSweptBranches-3` — the inventory and the rows write mode acts on.

## 4. Design

One module, `branch_reconcile.py`, stdlib only, run by path. `read_inventory(root)` returns the
worktrees, refs and stash entries as plain records. `derive_verdict(row)` walks the predicate list in
ladder order. `render_report(inventory, rows)` produces the lines, and `main` prints them.

The row name of a worktree is its path relative to the primary when it sits under it, else its
absolute path, forward-slashed. The primary's untracked count excludes any untracked path at or
above another worktree's path: a nested harness worktree is a directory the primary's status lists
as untracked, and counting it would make every primary read dirty (the gotcha class
`a-gate-that-walks-the-repo-root-reads-other-worktrees`).

Determinism: every list is sorted, the age is relative to the default tip and not to the clock, and
no line carries a time of day. Every `git` call runs with `-C <path>`, `encoding="utf-8"` and
`errors="replace"`, and none passes through a shell.

The self-test, `selftest.py`, builds its fixtures under a temporary directory with `GIT_DIR`,
`GIT_WORK_TREE` and `GIT_INDEX_FILE` held out of the environment and `GIT_CEILING_DIRECTORIES`
pinned. The census fixture is a bare remote named `upstream`, a clone, and one worktree of each
location kind, plus a detached one, a prunable one, a stash entry and a submodule.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`
- `tools/branch-reconcile/kit.toml`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/gate-legs.json`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/features/branch-reconcile.md`
- `README.md`
- `WIRE-INTO-PROJECT.md`
- `.claude/rules/product.md`

### Alternatives rejected

- A shell CLI. The patch comparison and the inventory joins are data work, and every peer kit of
  this shape, runlog and drift-audit, is Python.
- Ages relative to the clock. Two runs a second apart across midnight would differ.

## 5. Production-readiness checklist

- security — read-only; fixed `git` argv lists with no shell, and no input interpolated into one.
- perf / scale — a fixed number of `git` calls per worktree and per ref. 60 worktrees and 100 refs
  is a few hundred processes.
- error / empty / loading states — S1's three refusals exit 2; an empty stash and a repository with
  no linked worktree each render with zero rows of that kind.
- observability — the header counts and the `skipped` lines.
- risks — a misread location kind only changes a label in this unit.
- testing — AC1 to AC5, each staged red once.
- migration — N/A: a new kit, no stored state.
- user docs — the kit README and the runbook line, S6.

## 6. Acceptance criteria

- **AC1** — When `branch_reconcile.py` runs over the self-test's census fixture, its
  report lists a `primary`, a `nested`, a `sibling`, a `temp` and a detached and a prunable worktree,
  each local and `upstream` branch, and the stash entry, with the staged, unstaged, untracked,
  merge-in-progress and submodule-drift counts the fixture placed.
  Red when: a kind test is inverted, or the status parser drops a field.
- **AC2** — When the selftest runs `branch_reconcile.py` twice over the unchanged fixture, the two
  stdouts are byte-identical.
  Red when: a list goes unsorted or the age reads the clock.
- **AC3** — When the selftest sets `GOV_REMOTE` to a name that is no remote, or adds a second remote
  with none configured, `branch_reconcile.py` exits 2 and names `GOV_REMOTE`; with `upstream` as the
  only remote it resolves `upstream/main`.
  Red when: the ladder is replaced by a literal `origin`.
- **AC4** — When the primary's status lists the nested worktree's directory as untracked, the
  primary's untracked count in `branch_reconcile.py`'s report is 0.
  Red when: the exclusion is removed.
- **AC5** — When every predicate is the stub, every row reads `UNKNOWN` with
  `no predicate decided` in `branch_reconcile.py`'s report.
  Red when: the ladder defaults to any other verdict.
- **AC6** — When `python tools/govkit/govkit.py selfcheck` and `bash tools/check-kit-versions.sh`
  run, both exit 0 with the kit registered, and `python tools/codebase-map/gen_map.py --check` is
  green over the new dossier.
  Red when: the descriptor or the registry entry is missing.

## 7. Gates

`govkit selfcheck` · `kit version markers` · `codebase-map coverage + freshness` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `govkit selftest` · `lexicon naming predicates` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 AC2 AC3 AC4 AC5 · a fixture repository built per arm, with the guarded line broken once by hand · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

The seam is `resolve_remote` in `tools/lib/resolve_remote.py`, the canonical `remote_ladder_py`
block, inlined byte-identically as `tools/drift-audit/drift_report.py` does; the parity arm in
`tools/lib/resolve-python.test.sh` finds the copy by its marker. The kit shape is the runlog kit's:
`tools/runlog/kit.toml`, its withheld self-test and its registry rows. `reuse_lookup.py` ranked only
name-token neighbours (`merge`, `classify`, `add_scratch_worktree`) and no inventory of worktrees or
refs. The relocation engine's `cmd_stragglers` in `tools/memory-tree/migrate_backlog.py` lists refs
that carry unaccounted backlog row changes, a narrower population asking a different question, so
it is not consumed.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
