# TOOL-aQuotedBrief-2 — a first preflight refuses a branch carrying commits beyond this build's folder

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base fa68a767 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A run starts on whatever branch its session is on, and nothing in the kit looks at the commits that
branch already carries. Under `ANCHOR_SCOPE="published"` those commits sit below the pinned BASE, so
they fall outside every population the run's checks grade, and they land with the run under its
authorization without passing through the spec loop. This unit refuses a first preflight whose branch
carries a commit, absent from the default branch, that touches anything but this build's folder and
the indexes the kits declare generated. The prompt path tells the run to branch fresh before it
writes the folder, so the refusal is a backstop rather than the usual route.

## 2. Scope (IN)

- **S1** — `verb_preflight` in `tools/unattended/unattended.sh` gains a check between the
  authorization read and the write gate. It lists every commit reachable from `HEAD` and from neither
  the anchor tip `observe_anchor` observed nor the local default branch, with its paths, in one
  `git log --name-only` call. It refuses when any path is outside `<MEMORY_ROOT>/builds/<slug>/` and
  is not covered by an index in the resolved `GENERATED_INDEXES`. The message names the commit and
  the first such path, then prints the recovery of §4. Observed by AC1, AC2 and AC5.
- **S2** — The check binds every authorization mode. On the slug path the README already resolves on
  the default branch, so the branch should carry nothing of its own at all. Observed by AC3.
- **S3** — It runs only at a FIRST preflight: no run-state file for the build exists when preflight
  starts. A re-preflight after a compaction, a waiver re-issue or a rotation's predecessor record is
  not graded, because the commits it would see are the run's own. Observed by AC4.
- **S4** — The prompt path in `tools/unattended/VERBS.template.md` gains an instruction before step 3:
  when the branch carries a commit the default branch does not, switch to a new branch cut from the
  default branch before writing anything; when the tree is dirty, stop and say so. The slug path's
  preflight step names the same refusal, and `tools/unattended/SKILL.template.md` points at both.
  Observed by AC6.

## 3. Non-goals (OUT)

- Moving the commits for the run. The refusal prints the recovery; choosing what to keep is the
  session's or the owner's.
- Commits the run makes after its first preflight. They are the run's own and are graded by the
  checks that read `read_run_commits`.
- Stacked builds. No tracked build README declares a `parent:` today, so a build that needs an
  unlanded predecessor lands the predecessor first.
- A security boundary. A run with shell access can rewrite its branch; the check's header says so.

### Edges

none

## 4. Design

### Evidence

Read at `fa68a767` on 2026-10-09.

- `resolve_base` (`tools/unattended/unattended.sh:2353-2383`) takes the run-branch tip from
  `branch_tip_quiet` when the README does not resolve at the merge-base and the scope is `published`.
  BASE is then a tip the run pushed, so every commit below it, the session's included, is outside
  `read_run_commits` (`tools/unattended/lib-unattended.sh:1167`, `endpoint ^BASE`).
- The landing carry check reads `push-main.sh --carry`, whose `derive_carry_set`
  (`tools/push-main.sh:384-397`) keeps only commits also on the local default branch. A commit that
  exists only on the run's branch is never in that set.
- The unit-set rule is off on the run-branch anchor (`unattended.sh:3399-3402`) and the cross-run
  overlap probe reports without blocking. No other check reads these commits.
- `verb_preflight` (`:6371`) runs `observe_anchor` at `:6487`, the authorization read at `:6540-6543`,
  `check_waiver_scope` at `:6569`, and its write gate at `:6595`. The rotation test opening the verb
  reads the run-state file before any of them.
- `default_branch` (`:2259`) names the default branch from the observation. `GENERATED_INDEXES` is
  resolved at `:656` from the kits' declared rows plus the conf, and `covers` answers whether an
  index path covers a given path (used at `:12396`).
- A new build README's commit carries re-rendered generated indexes, `memory/LIVE.md` and the ledger
  shard among them, because hygiene check 9 runs `gen_build_index.py --check` at pre-commit.

### The predicate

```
git log --format=%h --name-only HEAD --not <anchor tip> [refs/heads/<default>]
```

The local default branch is excluded when it exists, so commits on a local default branch that is
ahead of the remote, already sanctioned by the charter's merge rule, are not counted as carried. This
is a guard against accident, read once: it trusts local refs, which a protocol BASE may not, and it
says so in its header. A merge commit lists no paths; the commits it brings in are listed themselves.

### The recovery

```
git switch -c <new-branch> <default>
git checkout <old-branch> -- <MEMORY_ROOT>/builds/<slug>/
```

then re-render the generated indexes, commit, push the branch and preflight again.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_branch_carried` | function | `sh.function`; `python tools/lexicon/lexicon.py --suggest check_branch_carried --as sh.function` answered OK |

The refusal takes the next free driver fail number at build time; the highest at `fa68a767` is 111.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `tools/unattended/VERBS.template.md` · `tools/unattended/SKILL.template.md` · `memory/guides/UNATTENDED-VERBS.md` · `.claude/skills/unattended/SKILL.md` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **Grading `BASE..HEAD` at close.** Under the run-branch anchor BASE is the pushed tip, so the
  carried commits are below it and the range never sees them.
- **Reusing `push-main.sh --carry`.** Its set is built from the local default branch, which is the
  population this check must exclude rather than read.
- **Creating a fresh worktree for the run.** It changes where the session works mid-run and which
  tree the lander runs in; branching in place on a clean tree reaches the same state.

## 5. Production-readiness checklist

- security — narrows what a first preflight admits; grants nothing.
- perf / scale — one `git log` spawn, at a first preflight only.
- error / empty / loading states — an empty listing passes; a missing local default branch drops
  that exclusion and keeps the anchor tip.
- observability — the refusal names the commit, the path and the recovery.
- risks — a session that branched off an unpushed predecessor build is refused until that build
  lands. That is the intended reading of "carried".
- testing — arms in `tools/unattended/unattended.test.sh` over the `readme`, `scope published` and
  `run --preflight` fixtures, run once at VERIFYING.
- migration — none: only a first preflight is graded, so no started run changes verdict.
- user docs — the verbs file's prompt and slug paths.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs on a prompt-mode branch whose build-folder commit sits on a
  commit touching a file outside the build folder, it refuses at the new check naming that commit's
  short sha and the file, and creates no `RUN.md`.
  Red when: the carried commit is admitted, or a run-state file is written first.
- **AC2** — When the only commit beyond the default branch is the build-folder commit with its
  re-rendered `memory/LIVE.md`, `--preflight` prints `preflight OK`.
  Red when: the authorization commit itself is refused for its generated indexes.
- **AC3** — When a slug-mode README resolves on the default branch and the run's branch carries one
  unrelated commit, `--preflight` refuses at the same check.
  Red when: the check grades only the prompt mode.
- **AC4** — When the build's `RUN.md` already exists, the same carried commit is not graded and
  `--preflight` proceeds as it does at BASE.
  Red when: a resumed run is refused on its own commits.
- **AC5** — When the local default branch is ahead of the remote tip and the run's branch is cut
  from it, `--preflight` counts none of the local default's commits.
  Red when: commits already on the local default branch are reported as carried.
- **AC6** — When `grep -n "git switch -c" memory/guides/UNATTENDED-VERBS.md` runs, the prompt path
  tells the run to branch fresh before step 3 and to stop on a dirty tree.
  Red when: the render carries no such instruction.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended skill size` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `check-wiring self-test` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the HEAD driver, which admits any carried commit · none

## 8. Open questions

- **F1 — On a dirty tree at the prompt path, stop or start the run in a fresh worktree?**
  Stopping keeps the session in one tree and makes the owner settle the edits; a fresh worktree lets
  the run start anyway but moves the session and the lander mid-run.
  Recommendation: stop, and say which files are dirty.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "record a self-contained brief of an unattended prompt-mode run, quoting session
context, and refuse unrelated commits on the run branch"` ranked `read_run_commits` in
`tools/unattended/lib-unattended.sh` among its candidates; it reads `endpoint ^BASE` and so cannot
see carried commits, which is the gap. The extended seams are `observe_anchor`, `default_branch`,
the resolved `GENERATED_INDEXES` with `covers`, and the run-state presence test the rotation logic
in `verb_preflight` already makes. `push-main.sh --carry` was probed and rejected in §4.

Recall terms used: `prompt record verbatim authorized-by prompt published anchor branch tip
self-authorization orientation AskUserQuestion owner turn build folder roster` — the same query as
`TOOL-aQuotedBrief-1`, which surfaced `TOOL-dNarrowedAnchor-1` and the second-anchor costs in
`memory/guides/UNATTENDED-PROTOCOL.md` §1.
