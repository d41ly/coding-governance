# TOOL-dSweptBranches-3 — write mode: a recovery manifest first, then deletes of the three landed verdicts only

**Status:** CLOSED · rev-4 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-3-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md) | research | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 |
| [2026-10-13-prompt-TOOL-dSweptBranches-3-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-3-1-build-brief.md) | journal | — |
| [2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 |
| [2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md](../reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round2.md) | diff-review | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 |

<!-- /gen:spec-records -->

## 1. Goal

`branch_reconcile.py --write` removes the worktrees, then the local branches, whose verdict is
`MERGED`, `EQUIVALENT` or `SUPERSEDED`, and `--remote` adds those remote branches in one push. Before
the first deletion it writes a recovery manifest of every tip and worktree `HEAD` under the git common
directory, so every deletion can be undone by hand.

## 2. Scope (IN)

- **S1** — The deletable set is the rows whose verdict is `MERGED`, `EQUIVALENT` or `SUPERSEDED`.
  Every row's action column reads what write mode would do: `remove worktree`, `delete branch`,
  `delete remote branch (--remote)`, or `keep (<why>)`; no action carries the row separator
  ` · `, so a report row parses. The keeps are the default branch, matched by name before the
  verdict is read, the primary worktree, a stash entry, a deletable worktree that contains a kept
  worktree, a branch checked out in a worktree that is kept, and every row outside the deletable
  set. The invoking worktree reads `IN-PROGRESS` by unit 2's S5, so it is outside the set. Observed
  by AC2 and AC5.
- **S2** — The recovery manifest, `<git common dir>/branch-reconcile/recovery-<UTC stamp>.txt`, holds
  one line per local branch, remote branch and stash entry with its sha, and one per worktree with
  its path and `HEAD`. It is written and flushed before any deletion, and its path is printed.
  A manifest that cannot be written refuses the whole run with exit 2. Observed by AC1.
- **S3** — The order: deletable worktrees are removed through unit 4's remover, then
  `git worktree prune` runs, then each deletable local branch is deleted with `git branch -D`. A
  branch still checked out after the removals is kept and reported. Observed by AC1 and AC2.
- **S4** — The remote flag, accepted only beside the write flag, takes the deletable remote
  branches off the remote in ONE push of their names with git's delete option, never the default
  branch. Without the remote flag no remote branch is touched. Observed by AC3.
- **S5** — Each action prints one result line. The exit is 0 when every action succeeded or ended
  busy, 1 when any failed, and 2 on a refusal. Observed by AC4.
- **S6** — The tool never merges, commits, checks out or pushes the default branch. Its only `push`
  is S4's delete. Observed by AC3.

## 3. Non-goals (OUT)

- No deletion of a stash entry, a tag or any ref outside `refs/heads` and the remote's branches.
- No restore verb. The manifest is the restore recipe, read by a person.
- No confirmation prompt. The skill asks the owner, and the CLI's flag is the answer.

### Edges

- **consumes-from** `TOOL-dSweptBranches-2` — the verdicts that define the deletable set.
- **consumes-from** `TOOL-dSweptBranches-4` — the worktree remover S3 calls.
- **hands-off** `TOOL-dSweptBranches-5` — the write flags the skill drives.

## 4. Design

`--write` computes the report exactly as the read-only run does and prints it first, then acts on
the rows. The deletable set is computed once and never re-derived mid-run, so a deletion cannot
change another row's verdict.

The manifest's lines are `branch <name> <sha>`, `remote <remote>/<name> <sha>`,
`stash <index> <sha>` and `worktree <path> <sha|none>`. The stamp is UTC to the second, with a
numeric suffix when one exists already, so two runs in one second never share a file.

The self-test proves the ordering with a trace: the module exposes `WRITE_TRACE`, a list each
mutation appends to BEFORE the act it records, and the arm asserts the manifest entry precedes
the first removal. The remote arm points a bare repository at the fixture and observes which branches remain on it.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`
- `memory/map/features/branch-reconcile.md`

### Alternatives rejected

- One `git push --delete` per branch. Each push runs the remote's hooks and the network round trip,
  and the prompt asks for one.
- A manifest under the working tree. A worktree removal could take it with it, and it would show as
  untracked content.

## 5. Production-readiness checklist

- security — a delete-only write surface, gated by an explicit flag and limited to three verdicts;
  the default branch is excluded by name before any verdict is read.
- perf / scale — one process per deletion, plus one push.
- error / empty / loading states — an empty deletable set writes the manifest and deletes nothing;
  a failed deletion is reported and the rest continue.
- observability — the manifest path and one line per action.
- risks — a deletion of live work. Mitigated by the verdict rules, the manifest and the keeps.
- testing — AC1 to AC4.
- migration — N/A.
- user docs — the kit README's write-mode section.

## 6. Acceptance criteria

- **AC1** — When `branch_reconcile.py --write` runs over the write fixture, the manifest under the
  common directory lists every branch tip and worktree `HEAD`, and `WRITE_TRACE` records it before
  the first removal.
  Red when: the manifest is written after the first deletion, or omits a worktree.
- **AC2** — When `branch_reconcile.py --write` runs over a fixture holding one row of each verdict,
  only the `MERGED`, `EQUIVALENT` and `SUPERSEDED` worktrees and branches are gone; the default
  branch, the `IN-PROGRESS`, `UNMERGED-LIVE` and `UNKNOWN` rows, and every remote branch remain.
  Red when: the deletable set admits another verdict, or the default branch is not excluded.
- **AC3** — When `branch_reconcile.py --write --remote` runs, the bare remote loses exactly the
  deletable branches in one push, and its default branch's tip is unchanged.
  Red when: the push names the default branch or an undeletable branch.
- **AC4** — When one removal is made to fail, `branch_reconcile.py --write` reports it, still
  deletes the other deletable rows, and exits 1; when a removal returns `busy`, it reports it and
  exits 0.
  Red when: the failure aborts the run, the exit is 0 after a failure, or busy counts as one.

- **AC5** — When `branch_reconcile.py --write` runs from a linked worktree, with the primary on
  another branch and a kept worktree nested inside a deletable one, the primary, local `main` and
  both nested worktrees survive, and their rows read `keep (the primary worktree)`,
  `keep (the default branch)` and `keep (contains kept worktree …)`.
  Red when: the containment keep, the primary keep, or both default-branch guards are removed.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 AC2 AC3 AC4 · a write fixture per arm, rebuilt before each, with the guarded line broken once by hand · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-13 · S1 · AC4 · what the build pass settled. The remote action names its flag, the
  default branch is excluded by name in two places, and AC4 takes unit 4's busy half by that spec's
  rev-2. `WRITE_TRACE` records each act before it runs, because a trace appended after the act let a
  manifest written late still read first.
- rev-3 · 2026-10-13 · S1 · AC5 · the closing review's two blockers. B1: a deletable worktree that
  contains a kept worktree is kept, because read_dirt hides the nested one from its container. B2:
  the primary and default-branch keeps get a fixture in which each is the deciding keep. The keep
  reasons move into parentheses, because the action column carried the row separator.
- rev-4 · 2026-10-13 · §4 · AC1 · the closing review's round-1 L2, folded by unit 17: the trace
  is named `WRITE_TRACE`, as the module spells it, and records each act before it runs.

## 10. Reuse audit

No existing seam deletes refs or worktrees by verdict. `remove_scratch_worktree` in
`tools/run-gates/lib-attribute.sh` removes a worktree the runner itself made, with no manifest and no
verdict, and is shell, so it is not reused; unit 4 owns the removal technique. `reuse_lookup.py`
ranked only name-token neighbours for the deletion phrase.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
