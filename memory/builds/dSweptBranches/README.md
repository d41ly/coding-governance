---
slug: dSweptBranches
node: d
opened: 2026-10-13
streams: tooling
roster: TOOL
ids: TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-6 TOOL-dSweptBranches-7 TOOL-dSweptBranches-8 TOOL-dSweptBranches-9 TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13 TOOL-dSweptBranches-14 TOOL-dSweptBranches-15 TOOL-dSweptBranches-16 TOOL-dSweptBranches-17
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
- Closing review: round 1 BLOCKED (2 blockers, 10 HIGH and 7 minor items); the blockers folded into
  unit 3 rev-3; round 2 CLEAN WITH FIXES, CONVERGED. Each HIGH became its own unit, 7 to 16, and
  every MEDIUM and LOW of both rounds unit 17, per M4's exit rule.

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
| 6 | `TOOL-dSweptBranches-7` | 2 | an unread worktree status reads UNKNOWN, never its HEAD's verdict (promoted, H1) |
| 7 | `TOOL-dSweptBranches-8` | 2 | a worktree path is proven this repository's before it is graded or rm -rf'd (promoted, H2) |
| 8 | `TOOL-dSweptBranches-9` | 2 | the patch predicate needs the same files and more shared lines than drift (promoted, H3) |
| 9 | `TOOL-dSweptBranches-10` | 2 | a probe is covered only by a declared case and its body on the default (promoted, H4) |
| 10 | `TOOL-dSweptBranches-11` | 2 | the rotated predicate needs each added row's whole text (promoted, H5) |
| 11 | `TOOL-dSweptBranches-12` | 2 | every name the default goes by is kept, the remote HEAD's included (promoted, H6) |
| 12 | `TOOL-dSweptBranches-13` | 2 | a deletion acts only on the sha it graded (promoted, H7) |
| 13 | `TOOL-dSweptBranches-14` | 2 | a merge is covered only when it introduces nothing of its own (promoted, H8) |
| 14 | `TOOL-dSweptBranches-15` | 2 | submodule content makes its worktree UNKNOWN (promoted, H9) |
| 15 | `TOOL-dSweptBranches-16` | 2 | tracked edits in an idle worktree are graded by a fixture (promoted, H10) |
| 16 | `TOOL-dSweptBranches-17` | 2 | the closing review's MEDIUM and LOW items, batched (promoted) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 16 unit(s) · node d · opened 2026-10-13 · streams tooling
ids TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-6 TOOL-dSweptBranches-7 TOOL-dSweptBranches-8 TOOL-dSweptBranches-9 TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13
ids TOOL-dSweptBranches-14 TOOL-dSweptBranches-15 TOOL-dSweptBranches-16 TOOL-dSweptBranches-17

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSweptBranches-1 — the census: the branch-reconcile kit, its remote ladder, the inventory and a byte-stable report](spec/2026-10-13-spec-TOOL-dSweptBranches-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-2 — the verdict ladder: six verdicts over refs and worktree content, each with its evidence](spec/2026-10-13-spec-TOOL-dSweptBranches-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-13 |
| [TOOL-dSweptBranches-4 — the worktree remover: git first, then `rm -rf`, and a skeleton removed only when it holds no regular file](spec/2026-10-13-spec-TOOL-dSweptBranches-4.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-13 |
| [TOOL-dSweptBranches-3 — write mode: a recovery manifest first, then deletes of the three landed verdicts only](spec/2026-10-13-spec-TOOL-dSweptBranches-3.md) | 4 | 2 | CLOSED | rev-3 | 2026-10-13 |
| [TOOL-dSweptBranches-5 — the skill: a rendered `/branch-reconcile` that routes cleanup asks through the tool](spec/2026-10-13-spec-TOOL-dSweptBranches-5.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-7 — a worktree whose status was never read reads UNKNOWN, never its HEAD's verdict](spec/2026-10-13-spec-TOOL-dSweptBranches-7.md) | 6 | 2 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-8 — a registered worktree path holding another repository is never graded as the worktree, and rm -rf reaches only a proven worktree](spec/2026-10-13-spec-TOOL-dSweptBranches-8.md) | 7 | 2 | CLOSED | rev-2 | 2026-10-13 |
| [TOOL-dSweptBranches-9 — the patch predicate matches only a copy that shares more lines than it drifts, on the same files](spec/2026-10-13-spec-TOOL-dSweptBranches-9.md) | 8 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-10 — an untracked probe is covered only when its cases are declared on the default branch and its body exists there](spec/2026-10-13-spec-TOOL-dSweptBranches-10.md) | 9 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-11 — the rotated predicate requires each added row's whole text on the default branch](spec/2026-10-13-spec-TOOL-dSweptBranches-11.md) | 10 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-12 — every name the default branch goes by is kept, the remote's own HEAD branch included](spec/2026-10-13-spec-TOOL-dSweptBranches-12.md) | 11 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-13 — a deletion acts only on the sha it graded](spec/2026-10-13-spec-TOOL-dSweptBranches-13.md) | 12 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-14 — a merge commit is covered only when it introduces nothing of its own](spec/2026-10-13-spec-TOOL-dSweptBranches-14.md) | 13 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-15 — a submodule with uncommitted content makes its worktree UNKNOWN](spec/2026-10-13-spec-TOOL-dSweptBranches-15.md) | 14 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-16 — tracked edits in an idle worktree are graded by a fixture](spec/2026-10-13-spec-TOOL-dSweptBranches-16.md) | 15 | 2 | OPEN | rev-1 | 2026-10-13 |
| [TOOL-dSweptBranches-17 — the closing review's MEDIUM and LOW items, batched](spec/2026-10-13-spec-TOOL-dSweptBranches-17.md) | 16 | 2 | OPEN | rev-1 | 2026-10-13 |
<!-- /gen:build-units -->

Records: 17 bound to this build, across 4 record folder(s).

Ids no record names: TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13 TOOL-dSweptBranches-14 TOOL-dSweptBranches-15 TOOL-dSweptBranches-16 TOOL-dSweptBranches-17 TOOL-dSweptBranches-9.

Ids no `spec-audit` record has ever named: TOOL-dSweptBranches-1 TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13 TOOL-dSweptBranches-14 TOOL-dSweptBranches-15 TOOL-dSweptBranches-16 TOOL-dSweptBranches-17 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3
TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-7 TOOL-dSweptBranches-8 TOOL-dSweptBranches-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dSweptBranches-1` | no |
| 2 | `TOOL-dSweptBranches-2` | no |
| 3 | `TOOL-dSweptBranches-4` | no |
| 4 | `TOOL-dSweptBranches-3` | no |
| 5 | `TOOL-dSweptBranches-5` | no |
| 6 | `TOOL-dSweptBranches-7` | no |
| 7 | `TOOL-dSweptBranches-8` | no |
| 8 | `TOOL-dSweptBranches-9` | no |
| 9 | `TOOL-dSweptBranches-10` | no |
| 10 | `TOOL-dSweptBranches-11` | no |
| 11 | `TOOL-dSweptBranches-12` | no |
| 12 | `TOOL-dSweptBranches-13` | no |
| 13 | `TOOL-dSweptBranches-14` | no |
| 14 | `TOOL-dSweptBranches-15` | no |
| 15 | `TOOL-dSweptBranches-16` | no |
| 16 | `TOOL-dSweptBranches-17` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
