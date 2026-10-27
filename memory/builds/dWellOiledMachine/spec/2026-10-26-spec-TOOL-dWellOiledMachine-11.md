# TOOL-dWellOiledMachine-11 — workspaces by `build.worktree`: the allocator, the commit queue, integration before release, and a sweep that reaps only what it allocated

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 20 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0289@dc7da053 whole
**Carries:** node:record-kind.workspace
**Carries:** node:policy-key.build.worktree

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

Workspaces are neither allocated nor reclaimed: merged worktrees and hundreds of stale temp directories
remain, nothing attributes them, concurrent agents share one scratch directory, and harness passes
share one worktree and meet git's index lock (gap-rt-06, gap-conc-03). The runtime allocates every
workspace by `build.worktree` and records it, commits through one serial queue per build, merges each
unit branch into the build branch before its lease may be released, and sweeps only the workspaces it
allocated (layer-runtime `[isolate]`).

## 2. Scope (IN)

- **S1** — The key's reader. `allocate_workspace` reads `build.worktree` once per call through
  `resolve("build.worktree")` (I31; `tools/policy/policy.py:752`; `tools/policy/catalogue.toml:992`,
  values `per-unit`, `parallel-only`, `shared`, default `shared`). Observed by AC1.
- **S2** — The gov-owned scratch root, `<worktree root>/gov/`, the worktree root being this node's
  `worktree_root` override (`resolve_node_overrides`, `tools/playbook/render_playbook.py:399`) else
  `derive_worktree_root` (`:560`), `<primary>/.claude/worktrees`. Nothing but this unit writes under
  `gov/`, so a hand-made worktree beside it is never this unit's. Observed by AC6.
- **S3** — The allocator, `allocate_workspace(repo, build, unit, lease, parallel)` in the new
  `tools/runtime/workspace.py`, returning the workspace's path. Under `shared`, the build's one worktree
  `<root>/gov/<build>/_build` on the build branch, made on first call. Under `per-unit`, a worktree
  `<root>/gov/<build>/<unit>` on a new branch `gov/<build>/<unit>` started at the build branch's tip,
  never at the default branch. Under `parallel-only`, `per-unit` when `parallel` is true (the unit shares
  its `order` with another unit holding a live lease) and `shared` otherwise. Observed by AC1.
- **S4** — What every workspace gets. A scratch directory per agent,
  `<root>/gov/<build>/<unit>.scratch/<agent id>/`, from `derive_agent_scratch(workspace, agent_id)`,
  outside the tree so no ignore rule is needed. The repository's hooks path: allocation refuses when
  `git -C <workspace> config core.hooksPath` differs from the primary tree's, so no workspace runs
  without the trusted hooks unit 10 installs. A clean start: a fresh workspace whose
  `git status --porcelain` is not empty, line endings included, is reaped and refused with
  `workspace — refused · fresh tree dirty · <n> path(s)`. Observed by AC2.
- **S5** — The record (I20), kind `workspace`: one file
  `<git-common-dir>/gov/workspaces/<build>/<unit>.toml` with `build`, `unit`, `path`, `branch`, `lease`
  (the lease ref, TOOL-dPlacedRequest-1 S1) and `allocated-utc`, written only by
  `write_workspace_record`, node-local and never committed; the kind's row in
  `tools/memory-tree/record-kinds.toml` (TOOL-dTotalRecall-2) names that home. Observed by AC1 and AC6.
- **S6** — The commit queue (I19), `tools/runtime/commit_queue.py`:
  `enqueue_commit(repo, build, workspace, paths, message, act)` holds the build's lock
  `<git-common-dir>/gov/commit-queue/<build>.lock` through unit 12's `hold_lock`, served in arrival
  order by a ticket file per call, and commits `git -C <workspace> commit --only -m <message> -- <paths>`
  under the committer identity `derive_act_identity <act>` prints (TOOL-dWellOiledMachine-39), returning
  the commit's sha. It never stages a path outside `paths`, never takes the lander's marker
  `push-main-active` or any lock `tools/push-main.sh` holds, and pushes nothing: pushing is
  TOOL-dWellOiledMachine-40's under `build.push`, and the `Gov-*` trailers TOOL-dWellOiledMachine-33's.
  Observed by AC3.
- **S7** — Integration before release. `integrate_unit(repo, build, unit)` merges the unit branch into
  the build branch, in the build's worktree and through the commit queue, in declared order: it refuses
  while a unit of the same build with a smaller `order` holds a finished, unmerged branch. It refuses,
  naming the path, a unit branch whose commits touch a shared record, `memory/DECISIONS.md`, an
  authored `BACKLOG.md` or a generated index (BUILD-METHOD M6 clause 3).
  `check_unit_integrated(repo, build_branch, unit_branch)` answers 0 when
  `git merge-base --is-ancestor <unit tip> <build tip>` holds; every lease release of a unit holding a
  workspace calls it first and refuses with `release — refused · <unit branch> holds <n> commit(s)
  <build branch> lacks`. A unit branch pushed from another node is fetched and merged the same way by
  the build's driver, and its holder's release checks the fetched build branch. Observed by AC4 and AC5.
- **S8** — The sweep, `sweep_workspaces(repo)`, run at the node tick. It reaps a directory under
  `<root>/gov/` whose record's lease reads released or expired by TOOL-dPlacedRequest-1's reader, or
  which no record names; and a worktree it allocated only when that worktree is clean and its branch is
  an ancestor of the build branch, reaping it through git's worktree verb and its record with it. It prints one
  `sweep — reaped <path> · <why>` or `sweep — kept <path> · <why>` line per candidate. Observed by AC6.
- **S9** — branch-reconcile leaves leased workspaces alone. `derive_action`
  (`tools/branch-reconcile/branch_reconcile.py:903`) returns `keep (a leased workspace)` for a worktree
  whose path a record under `<git-common-dir>/gov/workspaces/` names, before its verdict is read; the
  kit reads the records as files and imports nothing from the runtime kit. Observed by AC7.
- **S10** — The fixture, `python tools/runtime/workspace.py --fixture --plant <case>`: a bare remote
  and two clones under `%TEMP%` with short names, a planted policy file, a stub lease reader and a stub
  `derive_act_identity`, printing the case's observation, exit 0 when it holds; the leg
  `runtime workspace fixtures` in `tools/gate-legs.json` runs every case. Observed by AC1 to AC6.

## 3. Non-goals (OUT)

- Calling the allocator, the integration and the sweep at their moments: TOOL-dWellOiledMachine-6, the
  supervisor, at each act's launch, each unit's release and each node tick.
- Pushing a build or unit branch: TOOL-dWellOiledMachine-40 (`build.push`) and -60 (the fence).
- Writing `Gov-*` trailers: TOOL-dWellOiledMachine-33. Committing role returns at their witness:
  TOOL-dWellOiledMachine-40.
- Which session or node may hold a unit off the build's node: TOOL-dWellOiledMachine-41
  (`build.unit-holders`); this unit allocates that unit `per-unit` whatever the key says.
- The primary tree's refusal at an act's launch and relative worktree pointers (gap-tool-16):
  TOOL-dWellOiledMachine-37's preflight.
- Ports and databases: only an adopter's isolation pack declares services, and none exists.
- Merged branches and worktrees outside `gov/`: branch-reconcile's, an expansion the core does not
  call.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-12` — `hold_lock`, the waiting file lock the commit queue holds per build
- **consumes-from** `TOOL-dWellOiledMachine-39` — `derive_act_identity`, the committer identity every queued commit is made under
- **hands-off** `TOOL-dWellOiledMachine-33` — `commit_queue`: the queue's message carries the `Gov-*` trailers 33 writes from the act binding
- **hands-off** `TOOL-dWellOiledMachine-40` — `commit_queue`: role returns committed at their witness through `enqueue_commit`, and the build's branch pushed as `build.push` says
- **hands-off** `TOOL-dWellOiledMachine-41` — `commit_queue` and `allocate_workspace`: a unit held off the build's node gets a per-unit workspace and integrates through `integrate_unit`
- **hands-off** `TOOL-dWellOiledMachine-6` — the supervisor calls `allocate_workspace`, `integrate_unit` before each release, and `sweep_workspaces` at the node tick
- **consumes-from** external — the lease ref and its verdict reader (TOOL-dPlacedRequest-1 S1, S2) and the record kind registry (TOOL-dTotalRecall-2)
- **hands-off** `TOOL-dWellOiledMachine-79` — `enqueue_commit` and its ticket queue (findings 9, 39), which the spec audit's minors batch repairs

## 4. Design

### Evidence

Nothing at this base allocates a workspace: the unattended kit only finds a run's existing worktree
(`resolve_holder_worktree`, `tools/unattended/unattended.sh:8756`). The only worktree writers are the
gate runner's detached scratch trees (`add_scratch_worktree`, `remove_scratch_worktree`,
`tools/run-gates/lib-attribute.sh:59`, `:63`), placed by their callers under the common dir. The root
is a render probe (`derive_worktree_root`, `render_playbook.py:560`) whose per-node override is read
only by the node table (`:463`). branch-reconcile reaps by verdict with no notion of a lease
(`derive_action`, `branch_reconcile.py:903`; `remove_worktree`, `:985`). The harness's commit stage is
a shell block a model agent runs (`tools/workflows/unattended-build.template.js:1173-1191`), not a
callable queue. `git merge-base --is-ancestor` is the integration test the unattended kit already uses
(`unattended.sh:2608`).

### Layout under the scratch root

```
<root>/gov/
  fx/_build/              the build's one worktree (shared)
  fx/TOOL-fx-3/           a unit's worktree (per-unit), branch gov/fx/TOOL-fx-3
  fx/TOOL-fx-3.scratch/
    a91c…/                one agent's scratch directory
<git-common-dir>/gov/workspaces/fx/TOOL-fx-3.toml
<git-common-dir>/gov/commit-queue/fx.lock
```

### The queue, one commit

```
hold_lock(fx.lock) → take the lowest ticket → env $(derive_act_identity <act>)
git -C <workspace> commit --only -m <message> -- <paths> → sha → drop the ticket → release
```

Two parallel passes under `shared` stage disjoint write sets (M6) and reach git's index one at a time,
which is what removes the index-lock collisions of gap-conc-03.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `allocate_workspace`, `derive_agent_scratch`, `write_workspace_record`, `integrate_unit`, `check_unit_integrated`, `sweep_workspaces` | python functions | `tools/runtime/workspace.py` |
| `enqueue_commit` | python function | `tools/runtime/commit_queue.py` |
| `<root>/gov/`, `gov/<build>/<unit>` | scratch root, branch namespace | S2, S3 |
| `workspace` | record kind row | `tools/memory-tree/record-kinds.toml` |
| `keep (a leased workspace)` | branch-reconcile action | `branch_reconcile.py` |
| `workspace —`, `release — refused`, `sweep —` | output lines | S4, S7, S8 |
| `runtime workspace fixtures` | gate leg | `tools/gate-legs.json` |

### Files touched (estimate)

- `tools/runtime/workspace.py` (new)
- `tools/runtime/commit_queue.py` (new)
- `tools/runtime/kit.toml`
- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/memory-tree/record-kinds.toml`
- `tools/gate-legs.json`

### Alternatives rejected

- **Reusing branch-reconcile's remover for the sweep.** branch-reconcile is an expansion, and the
  runtime is core: the core depends on nothing it does not ship (layer-runtime `[isolate]`).
- **The workspace record as a tracked file.** It would ride the build branch, and a shared record never
  rides a unit branch; the record is node-local state, as acts and session bindings are.
- **A unit branch started at the default branch.** The unit would lack the build's earlier passes; the
  per-unit route branched from the build tip is the one TOOL-dUnstalledConvoy-7 measured and cleared.

## 5. Production-readiness checklist

- security — writes only under the gov scratch root, the common dir's `gov/` and the build's own
  branches; never the primary tree, never the lander's locks; refuses a workspace without the trusted
  hooks path.
- perf / scale — one `git worktree add` per unit under `per-unit`; the queue holds a lock for one
  commit at a time; the sweep is one pass over `gov/`.
- error / empty / loading states — a dirty fresh tree, a hooks-path mismatch, an out-of-order merge and
  a shared-record path each refuse naming their cause; an unreadable lease keeps the workspace.
- observability — one line per allocation refusal, per release refusal and per sweep candidate.
- risks — `git worktree remove` can fail on deep trees on Windows (branch-reconcile's measured traps);
  the sweep keeps what it cannot reap and says so, and the next tick retries.
- testing — the fixture plants of AC1 to AC6, branch-reconcile's arm for AC7, and §7's arms.
- migration — none: existing hand-made worktrees sit outside `gov/` and are never this unit's.
- user docs — `tools/runtime/README.md` (I1) gains the workspace layout and the queue.

## 6. Acceptance criteria

The fixture is a bare remote and clones A and B under `%TEMP%` with short names, a build `fx` with units
`TOOL-fx-1` and `TOOL-fx-2` at `order 1` and `TOOL-fx-3` at `order 2`, a planted policy file and a stub
lease reader.

- **AC1** — When `python workspace.py --fixture --plant values` allocates `TOOL-fx-1` and `TOOL-fx-2`
  under each value of `build.worktree`, `shared` returns `_build` for both, `per-unit` returns two
  worktrees on `gov/fx/TOOL-fx-1` and `gov/fx/TOOL-fx-2` started at the build branch's tip while the
  default branch sits elsewhere, and `parallel-only` returns per-unit for the two order-1 units and
  `_build` for `TOOL-fx-3`; each allocation leaves its record.
  Red when: a unit branch starts at the default branch, or a value allocates the wrong shape.
- **AC2** — When `python workspace.py --fixture --plant workspace` allocates with two agent ids, two
  distinct scratch directories exist outside the tree; a planted `core.hooksPath` mismatch refuses the
  allocation; and a planted `.gitattributes` that dirties a fresh checkout prints
  `workspace — refused · fresh tree dirty` and leaves no worktree.
  Red when: two agents share a scratch directory, or a dirty fresh tree is handed out.
- **AC3** — When `python workspace.py --fixture --plant queue` runs twenty pairs of concurrent
  `enqueue_commit` calls of disjoint paths in the `_build` worktree, every call returns a sha, no call
  meets `index.lock`, each commit holds only its own paths and a `gov-act` committer, and no file named
  `push-main-active` is touched.
  Red when: a commit carries another call's path, or an index-lock error is seen, as a planted queue
  without the lock shows.
- **AC4** — When `python workspace.py --fixture --plant integrate` finishes `TOOL-fx-3` before
  `TOOL-fx-1`, `integrate_unit` for `TOOL-fx-3` refuses naming `TOOL-fx-1`; a release of `TOOL-fx-1`
  before its merge prints `release — refused`; and a unit branch touching `memory/DECISIONS.md` is
  refused naming that path.
  Red when: a unit merges out of order, a lease releases with unmerged commits, or a shared record
  rides a unit branch.
- **AC5** — When `python workspace.py --fixture --plant second-node` has clone B take `TOOL-fx-2` under
  `shared`, commit on its unit branch and push it, clone A's driver merges it from the remote and pushes
  the build branch, and B's release passes only after B fetches that build branch.
  Red when: B releases before the merge reaches the fetched build branch, or B pushes to the build
  branch itself.
- **AC6** — When `python workspace.py --fixture --plant sweep` plants a released lease's workspace, a
  live lease's, an unrecorded directory under `gov/`, a clean merged worktree, a dirty one and a
  hand-made worktree under `.claude/worktrees/`, `sweep_workspaces` reaps the first, third and fourth,
  keeps the live and the dirty ones with a `sweep — kept` line, and never names the hand-made one.
  Red when: a leased, dirty or hand-made workspace is reaped.
- **AC7** — When `python branch_reconcile.py` reports in a fixture repo over a merged worktree a record under
  `gov/workspaces/` names, its action reads `keep (a leased workspace)`, and without the record it reads
  `remove worktree`.
  Red when: branch-reconcile reaps a leased workspace.

## 7. Gates

`branch-reconcile selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `memory hygiene`

New arm: tools/runtime/workspace.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · each plant staged against an allocator branching from the default branch, a queue without its lock, a release without the ancestry check and a sweep without the lease read, in turn · none
New arm: tools/branch-reconcile/selftest.py · covers AC7 · a merged worktree named by a workspace record, staged by the base `derive_action` · none

## 8. Open questions

- **F1 — Where is the workspace record kept?** (a) Node-local under `<git-common-dir>/gov/workspaces/`;
  (b) a tracked record in the build folder. (b) rides a branch, and the integration step refuses shared
  records on a unit branch. Rung 1, layer-runtime `[isolate]`, "shared records never ride a unit
  branch". RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — How is the sweep kept off hand-made worktrees?** (a) A gov-owned subroot `gov/` under the
  worktree root; (b) a marker file in each allocated tree. (b) puts an untracked file in every tree,
  which dirties it. Rung 1, the layer's "lease-marked directories under a gov-owned scratch root".
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F3 — What lock serialises the queue?** (a) Unit 12's `hold_lock`, its second caller; (b) the gate
  runner's turnstile, a counting semaphore that TOOL-dWellOiledMachine-9 extracts. The queue needs one
  holder at a time in arrival order, which a waiting exclusive lock and a ticket file give; (b) would
  extract another unit's mechanism early. Rung 3, the charter's reuse rule. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-79.

## 10. Reuse audit

The seams extended are the worktree root probe and its node override (`render_playbook.py:560`,
`:399`), the ancestry test (`git merge-base --is-ancestor`, as `unattended.sh:2608` uses it), unit 12's
`hold_lock`, unit 39's `derive_act_identity`, and branch-reconcile's action table (`derive_action`,
`branch_reconcile.py:903`) for the exclusion. No existing seam fits the allocator or the queue:
`python tools/codebase-map/reuse_lookup.py "allocate a worktree per unit lease, merge it before release
and sweep stale workspaces"` ranked `merge` (the row merge driver and the settings merge),
`add_scratch_worktree` and `resolveLease`; the scratch-worktree pair adds a detached tree with no branch
and no record, and `resolveLease` reads the unattended run lease, not a unit lease. Scout C's row cites
`check_holder_worktree` at `unattended.sh:9117` as using `--is-ancestor`; at this base that function
calls no ancestry test, and the uses are at `:1524`, `:2608` and `:2764`. Its other lines,
`lib-attribute.sh:59`, `:63`, `render_playbook.py:560`, `:463` and `branch_reconcile.py:336`, `:716`,
`:887`, `:935`, hold.

Recall terms used: `python tools/memory-recall/query.py "how are worktrees allocated and reclaimed for
parallel units" --terms "build.worktree worktree per-unit shared parallel-only commit queue integration
sweep branch-reconcile scratch root lease"`
