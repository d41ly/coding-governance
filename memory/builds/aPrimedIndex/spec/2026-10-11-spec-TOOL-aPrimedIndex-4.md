# TOOL-aPrimedIndex-4 — the lander regenerates the declared outputs over its merged tree and lands them with the merge

**Status:** OPEN · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aPrimedIndex-1.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1.md) | research | TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 |

<!-- /gen:spec-records -->

## 1. Goal

Make the lander, which already writes minted versions over the tree it is about to push, also
regenerate every declared output there, so a landing whose reconcile merge left a `merge=ours` index
stale pushes a fresh tree instead of meeting the bar's refusal.

## 2. Scope (IN)

- **S1** — `--prepare` runs TOOL-aPrimedIndex-2's `--write` over the merged tree after the mint, and
  what it moved enters the prepared merge through the same rewrite the mint uses: same parents, same
  subject. Observed by AC1.
- **S2** — The attended landing runs the same `--write` on every attempt, after its mint commit, and
  commits what moved as its own commit: subject
  `regen: generated outputs onto <remote>/<default> at <sha8>`, plus ` for <unit>` when the pushed
  range attributes one, and a `Pass: none` trailer, the attended mint commit's two rules.
  Observed by AC2.
- **S3** — A `--write` that exits non-zero refuses the landing with the mint refusal's exit shape:
  the branch is left where it was and checked out, and the verb's own output is shown. Observed by
  AC3.
- **S4** — A lander with no `regen.py` beside it, or no usable python, says so in one line and lands
  without it, as `run_minter` does for a missing deployer; the push bar's preflight then grades the
  outputs. Observed by AC4.
- **S5** — The lander's header and the `--prepare` comment block state the regeneration and what it
  does not check. Observed by AC4.

## 3. Non-goals (OUT)

- `--land` regenerates nothing: it pushes the merge `--prepare` already regenerated, and `--prepared`
  answers for exactly that merge.
- No regeneration on a branch push; a branch has no lander.
- No change to the merge-loss check or the mint; the regeneration runs between them.
- No change to `.githooks/pre-push`.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-2` — the `--write` verb, its exit codes and its moved-file
  report.

## 4. Design

### Where it runs

| Path | After | Before | Commit |
|---|---|---|---|
| `--prepare` | `run_minter` | the `git status` that folds the mint into the merge | the rewritten merge |
| attended | the mint commit | the push | its own `regen:` commit |

The regeneration is found the way `run_minter` finds govkit: `resolve_kit_dir` for the run-gates
kit and `regen.py`, then a file test under the toplevel, because the kit can resolve beside the
lander while the tree being landed lacks the file.

### Inventory

One new shell function in `tools/push-main.sh`, `run_regen`, led by `run` from the verb table in
`.lexicon.conf`: execute a process to completion and report its outcome.

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **Fold the attended regeneration into the mint commit.** That commit's subject is read as a mint
  by its own arm and by people; a regeneration is a different act.
- **Regenerate before the reconcile merge.** The merge itself is what leaves the `merge=ours`
  indexes stale, so a regeneration before it misses exactly the case this unit exists for.

## 5. Production-readiness checklist

- security: N/A — the lander already executes the deployer over the same tree; this executes the
  declared generators.
- perf / scale: one `--write` per landing attempt, recorded at build; on node `a` the eleven items
  are minutes, against a push bar measured in hours.
- error / empty / loading states: a failed write refuses with the branch unmoved; nothing moved
  commits nothing.
- observability: the verb's moved-file lines are shown, and the attended commit names what it is.
- risks: a regeneration that rewrites an authored region of a file would land unreviewed; only the
  declared generators run, each of which writes its generated region or file alone.
- testing: lander self-test arms over a clone pushed to a bare remote.
- migration: none.
- user docs: the run-gates kit README names the lander as the verb's second caller.

## 6. Acceptance criteria

- **AC1** — When a branch in a clone pushed to a bare remote commits a one-row removal from
  `memory/gotchas/INDEX.md` and `tools/push-main.sh --prepare` runs, the prepared merge's first
  parent is the advertised tip, its tree carries the restored row, and the tree is clean. Red when:
  the merge carries the stale row, or the regeneration is left uncommitted.
  cost: one full regeneration in a clone, minutes on node `a`.
  fixture: a clone of this repository at HEAD, made by the arm.
- **AC2** — When the attended landing runs in such a clone from `main` with the same stale row and
  the stub bar the suite already uses, a commit whose subject begins `regen: generated outputs onto`
  and carries `Pass: none` precedes the push, and the pushed tip carries the restored row. Red when:
  no such commit lands, or it carries no trailer.
- **AC3** — When the clone's `regen.py` is replaced by one that exits 1, `--prepare` exits non-zero,
  the branch still names its pre-run sha, and the verb's output is on stderr. Red when: a merge is
  kept or the branch moved.
- **AC4** — When the clone has no `regen.py`, `--prepare` prints one line naming the missing
  regeneration and still prepares the merge, and `grep -n "regen" tools/push-main.sh` shows the
  header naming it. Red when: the absence is silent, or it refuses the landing.

## 7. Gates

`install-prefix (shipped surface)` · `line length` · `lexicon naming predicates` · `memory hygiene` · `codebase-map coverage + freshness`

New arm: tools/push-main.test.sh · covers AC1 AC2 AC3 AC4 · a committed one-row removal from the gotchas index, a failing and an absent regen.py · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` led to the lander's own mint seam: `run_minter` in
`tools/push-main.sh` and the `commit-tree` rewrite that folds its output into the prepared merge
(TOOL-aMendedFleet-65). This unit adds a second writer at that seam and reuses its refusal shape and
its unit attribution, `read_mint_unit`.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
