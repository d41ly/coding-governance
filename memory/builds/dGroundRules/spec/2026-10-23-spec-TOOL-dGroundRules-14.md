# TOOL-dGroundRules-14 — the landing replay: the mirror a prepared merge carries is fresh at that merge

**Status:** CLOSED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-14-deviation-2.md](../build/2026-10-23-build-TOOL-dGroundRules-14-deviation-2.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-14-deviation-66.md](../build/2026-10-23-build-TOOL-dGroundRules-14-deviation-66.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-14-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-14-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-14-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-14-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-16 TOOL-dGroundRules-65 TOOL-dGroundRules-19 TOOL-dGroundRules-15 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-20 TOOL-dGroundRules-21 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`)
exited BOUNDED with finding **id 31 at BLOCKER**, which shares item **B1** with id 1
(`TOOL-dGroundRules-65`). This unit is id 31's promotion. It repairs `TOOL-dGroundRules-5` and builds
at order 4, one step after that unit.

Id 31 is B1 seen from the landing: `--prepare` regenerates the mirror at the merge and then folds it
into a new commit with `commit-tree` (`tools/push-main.sh:911`, `:921`), and the bar runs
`regen.py --check` before its first leg (`tools/run-gates/run-gates.sh:1449-1458`). As specified, the
mirror is stale at the commit that lands, so the bar reds after every landing and no criterion of
`TOOL-dGroundRules-5` replays the lander. `TOOL-dGroundRules-65` fixes the render; this unit is the
arm that replays the landing's shape every bar, plus the one-off observation of the real lander
the review asked for, so the class cannot return through a later reason, field or regen order.

## 2. Scope (IN)

- **S1** — The case `mirror-landed-merge` in `CASES` of `tools/policy/check_policy.py`, replaying
  the lander's order in its temporary repository: a branch commit changing the policy file, a
  `git merge --no-ff` of it onto `main`, `policy.py mirror --write` over the merged tree, the
  rewrite `git commit-tree "$(git write-tree)" -p <main> -p <branch>`, and `main` moved to the
  rewrite in the fixture's bare remote. At the rewrite it asserts three outcomes: `mirror --check`
  exits 0, `arm_mirror_parity` reports no finding, and `node policy-mirror.js get <key> --explain`
  reads the mirror FRESH, its reason not opening `mirror stale at`. Observed by AC1.
- **S2** — The case is armed by a staged break, not by a planted file: the close stages the render
  to spell its revision in a reason, and the case reds naming the stale key. Observed by AC2.
- **S3** — The lander, observed once. In a scratch clone of the built tree with a bare remote,
  `bash tools/push-main.sh --prepare` runs over a branch that changes `.governance/policy.toml`, and
  `python tools/run-gates/regen.py --check` on the prepared merge exits 0. Observed by AC3.

## 3. Non-goals (OUT)

- The render's fix itself: `TOOL-dGroundRules-65`, id 1's promotion, owns `rev_phrase` and the
  helper's fill. This unit adds no code to `tools/policy/policy.py`.
- Changing `tools/push-main.sh` or `tools/run-gates/regen.py`: the landing's order is correct; the
  defect was the render's.
- A suite that runs the real lander every bar. `--prepare` needs a clone, a remote and the whole
  kit set; the case replays its four git steps instead, and S3 observes the real one once.

### Edges

- **consumes-from** `TOOL-dGroundRules-5` — `mirror --write` and `--check`, `arm_mirror_parity`, `readPolicy` with its CLI, and the fixture's bare remote, which the replay drives
- **consumes-from** `TOOL-dGroundRules-65` — the render invariant this replay asserts green; without it the case is red on a correct replay
- **hands-off** `TOOL-dGroundRules-25` — the lander observation and `mirror-landed-merge`, which that unit moves into the lander's own suite with `--slug` and the success line asserted (findings 18, 12, 30)

## 4. Design

### Evidence

- `--prepare` order: `git merge --no-ff "$oldb"` (`tools/push-main.sh:881`), `run_minter`, then
  `run_regen` (`:911`), then, when the tree moved, `git add -A` and
  `git commit-tree "$(git write-tree)" -p "$R" -p "$oldb"` (`:921`). The rewrite's parents are the
  merge's.
- `run-gates.sh` runs `"$PYBIN" "$KITDIR/regen.py" --check` before the first leg and exits 2 on a
  non-zero answer (`tools/run-gates/run-gates.sh:1449-1458`).
- `TOOL-dGroundRules-5` §4 "The arms and the cases" builds every case's repository from unit 1's
  fixture with a bare remote whose `main` is the landed revision, so the replay reuses that
  repository and adds one branch.

### The case

| Step | Act in the case's repository | What the lander does there |
|---|---|---|
| 1 | commit `budgets.enforce = "refuse"` on branch `b` | the branch being landed |
| 2 | `git checkout --detach main` then `git merge --no-ff b` | `tools/push-main.sh:876-881` |
| 3 | `python <kit>/policy.py mirror --write` | `run_regen`, `:911` |
| 4 | `git add -A`, then `git commit-tree "$(git write-tree)" -p main -p b`, `git update-ref HEAD` | `:919-921` |
| 5 | push the rewrite to the bare remote as `main` | the landing's push |

Then `mirror --check`, `arm_mirror_parity` over the repository, and the helper's `get
budgets.enforce --explain` each run at the rewrite. The case prints
`policy-fixture: mirror-landed-merge · fresh at the rewrite` or `· WRONG` with the failed outcome.
It is an outcome case, as `TOOL-dGroundRules-5`'s `mirror-worktree-loosened` is: green on a correct
build, and RED only on its staged break.

### The observation of the real lander

S3 is a probe, run once by this unit's pass: a scratch clone under `%TEMP%`, short-named, of the
built tree; a bare repository as its remote holding `main`; a branch committing one policy-file
change; `bash tools/push-main.sh --prepare` on it; then `regen.py --check` at the prepared HEAD.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `mirror-landed-merge` | `CASES` entry | `tools/policy/check_policy.py` |

### Files touched (estimate)

- `tools/policy/check_policy.py`

### Alternatives rejected

- **A permanent case running `push-main.sh --prepare`.** It needs a remote, the minter and every
  generated output's kit in the fixture; the four git steps are the part of the lander the mirror
  depends on, and S3 observes the rest once.
- **Folding this arm into `TOOL-dGroundRules-65`'s case.** That case rewrites one commit; a landing
  is a two-parent merge rendered after the merge and read by the helper through a remote, and the
  method makes a separate gate a separate unit.

## 5. Production-readiness checklist

- security — N/A: a test case over a temporary repository; no shipped behaviour changes.
- perf / scale — one more case of about eight git calls and one `node` call in `--fixture`.
- error / empty / loading states — a step that fails prints the step and `WRONG`, never a pass.
- observability — the case names the outcome that failed: the check, the parity arm or the helper.
- risks — the replay drifts from the lander if `--prepare`'s order changes; S3 is the one-off that
  compares them, and the case's table cites the lander's lines so a reader can re-check.
- testing — the case under `--fixture`, with AC1 to AC3.
- migration — none.
- user docs — N/A: no user act changes.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py` and `policy.py`, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `python check_policy.py --fixture mirror-landed-merge` runs on the built tree, it
  prints `policy-fixture: mirror-landed-merge · fresh at the rewrite` and no `WRONG`.
  Red when: the mirror rendered at the merge is stale at its rewrite, the parity arm finds it, or
  the helper reads it as stale.
- **AC2** — When the reason builder for a file value in `policy.py` is staged to format its own
  sha8 in place of `read.rev_phrase` and the same `--fixture mirror-landed-merge` runs, it prints
  `WRONG` naming `budgets.enforce`; restored, it prints no `WRONG`.
  Red when: the case passes with the render spelling its revision, so it cannot see the class.
- **AC3** — When `bash tools/push-main.sh --prepare` runs in a scratch clone of the built tree over
  a branch changing the policy file, then `python tools/run-gates/regen.py --check` runs at the
  prepared HEAD, the second exits 0 and names no stale output.
  Red when: the prepared merge carries a mirror its own check calls stale.
  cost: a clone of the repository and one `--prepare`, a minute or two.
  fixture: the clone and its bare remote under `%TEMP%`, short-named; the tree holds none today.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the case; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture mirror-landed-merge`) · covers AC1 AC2 · the render staged to spell its revision's sha8 in a file value's reason · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 31 (BLOCKER, item B1) of the round-1
  spec audit, from the review's left-shift gate and `tools/push-main.sh` read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-25`, the reciprocal of each
  promotion of the round-1 spec audit of units 13 to 21 that repairs this unit; no scope moved.
- rev-3 · 2026-10-23 · §1 §3 §4 · TOOL-dGroundRules-13 renamed TOOL-dGroundRules-65 by the owner's ruling, the id a landed dSafePassage ask holds; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dGroundRules-5`'s case fixture, a temporary repository with a bare remote
whose `main` is the landed revision, which this case drives through the lander's four git steps.
`python tools/codebase-map/reuse_lookup.py "replay the lander merge rewrite with commit-tree and
check a generated output fresh"` ranked name stems only (`tree`, `check`, `merge`, `build_commit`);
`build_commit` (`tools/unattended/lib-unattended.sh`) builds a run's commit and replays no landing,
so no existing seam fits the replay itself. Read against source, `tools/push-main.sh:876-921` is the
order the table copies. The recall probe returned `DEPL-aPrimedIndex-1`, `TOOL-aPrimedIndex-1` and
`TOOL-aPrimedIndex-4`, which put regeneration into the prepared merge; they agree with source.

Recall terms used: `python tools/memory-recall/query.py "how does a generated output stay fresh
across the lander's commit-tree rewrite" --terms "generated output regen commit-tree prepare merge
stale preflight mirror sha8 landing"`
