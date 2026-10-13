---
slug: dSweptBranches
node: d
opened: 2026-10-13
streams: tooling
roster: TOOL
ids: TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-6
authorized-by: prompt
---

# dSweptBranches — a kit that reconciles a repository's branches and worktrees, and removes only what landed

## The problem this build exists to solve

Owners keep asking agents to clean up branches and worktrees, and every session re-derives the
method by hand. On 2026-10-13 one inCMS session spent hours on 71 local branches, 33 remote
branches and 60 worktrees. It found 60 merged, 9 superseded by later landings, 1 live and 1 closed,
reviewed and never landed, which fixed a live production bug. `git cherry` misses rebased copies,
merge-tree conflict counts mislead, and decision rows rotate into archives. On Windows, worktree
directories survive their removal as skeletons of MSYS links. The owner's prompt is recorded
verbatim under `prompts/`.

## Expected improvements

- One read-only command answers which refs and worktrees are merged, equivalent, superseded, in
  progress, live and unmerged, or undecidable, with the evidence for each row.
- Write mode removes only the three landed verdicts, after a recovery manifest is on disk.
- The Windows removal traps are handled once, in the tool, not rediscovered per session.
- A skill routes "clean up branches" through the tool, and surfaces the live work as decisions.

## Detriments if this is not built

- Each cleanup costs hours of owner and agent time, and repeats the same traps.
- A by-hand pass can delete the one branch that holds unlanded work.
- Worktree skeletons and stale branches accumulate on every node.

## Build-level rules

- Five units, all Tier-2, because each ships in a kit. They are sequenced in roster order and
  authored inline, because units 1 to 4 write one CLI and unit 5 renders its skill. Unit 4 builds
  before unit 3, whose write mode calls its remover.
- Classified at kickoff (M2): all five MISSING, authored in the opening commit.
- Unit 2's predicates are each observed RED against unit 1's stub before they land.
- The relocation engine's `--stragglers` inventory is a different population: refs that still owe a
  backlog relocation. This kit does not consume it, and its README says why.
- Unattended run records are read, never written: `--settle` and `--preflight` own them.
- The side ask about check 21's reading of merges is `TOOL-dSweptBranches-6`, filed, not built.
- No spec audit is declared. The closing diff review is owed.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dSweptBranches-1` | 2 | the census: the kit, the remote ladder, the inventory of worktrees, refs and stash, and a byte-stable report |
| 2 | `TOOL-dSweptBranches-2` | 2 | the verdict ladder: six verdicts over refs and worktree content, each with its evidence |
| 3 | `TOOL-dSweptBranches-4` | 2 | the worktree remover: git first, then `rm -rf`, and a skeleton removed only when it holds no regular file |
| 4 | `TOOL-dSweptBranches-3` | 2 | write mode: a recovery manifest first, then deletes of the three landed verdicts only |
| 5 | `TOOL-dSweptBranches-5` | 2 | the skill: a rendered `/branch-reconcile` that routes cleanup asks through the tool |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 5 unit(s) · node d · opened 2026-10-13 · streams tooling
ids TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSweptBranches-1 — the census: the branch-reconcile kit, its remote ladder, the inventory and a byte-stable report](spec/2026-10-13-spec-TOOL-dSweptBranches-1.md) | 1 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-2 — the verdict ladder: six verdicts over refs and worktree content, each with its evidence](spec/2026-10-13-spec-TOOL-dSweptBranches-2.md) | 2 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-4 — the worktree remover: git first, then `rm -rf`, and a skeleton removed only when it holds no regular file](spec/2026-10-13-spec-TOOL-dSweptBranches-4.md) | 3 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-3 — write mode: a recovery manifest first, then deletes of the three landed verdicts only](spec/2026-10-13-spec-TOOL-dSweptBranches-3.md) | 4 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-5 — the skill: a rendered `/branch-reconcile` that routes cleanup asks through the tool](spec/2026-10-13-spec-TOOL-dSweptBranches-5.md) | 5 | 2 | OPEN | rev-1 | 2026-10-13 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dSweptBranches-1` | no |
| 2 | `TOOL-dSweptBranches-2` | no |
| 3 | `TOOL-dSweptBranches-4` | no |
| 4 | `TOOL-dSweptBranches-3` | no |
| 5 | `TOOL-dSweptBranches-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
