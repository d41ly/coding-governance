# TOOL-dSafePassage-27 — the prepared landing's one untracked snapshot, taken before the walk, serves the regeneration's refusal too

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-27-deviation-73.md](../build/2026-10-23-build-TOOL-dSafePassage-27-deviation-73.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 1** at HIGH, merged with id 35 into its item **D-1**. TOOL-dSafePassage-8 S4
runs `run_gov_first` after the mint and before the regeneration, and TOOL-dSafePassage-25's §4 block
discards its snapshot `gfsnap` as soon as the walk passes. The regeneration stage then takes its own
snapshot (`tools/push-main.sh:910`), which already holds the walk's receipt, before-images and
outbox orders. A regeneration refusal (`:911-916`) runs `git reset -q --hard`, which restores tracked
files only, and `remove_new_untracked "$rgsnap"`, which cleans only the paths that snapshot lacks
(`:784-793`). So the walk's files survive the refusal, and the next `--prepare`'s `git add -A`
(`:918`) folds them into the merge. This unit is id 1's promotion: the prepared path takes ONE
snapshot, before the walk, and both of its untracked-creating stages clean against it on refusal.
Id 35's promotion, `TOOL-dSafePassage-28`, gates every later refusal as a class.

## 2. Scope (IN)

- **S1** — One snapshot. In `cmd_prepare`, the snapshot TOOL-dSafePassage-25 takes into `gfsnap`
  before `run_gov_first` stays alive past a passing walk. The regeneration stage of `cmd_prepare`
  takes no snapshot of its own: its refusal runs `git reset -q --hard "$t"`, then
  `remove_new_untracked "$gfsnap"`, then `rm -f "$gfsnap"`, checks the branch out and exits 1, as
  today. Every untracked path made after the snapshot, by the walk or by the regeneration, is
  therefore cleaned. Observed by AC1.
- **S2** — The lifetime. `rm -f "$gfsnap"` runs on the gov-first refusal, on the regeneration
  refusal, and once after `run_regen` passes, so no path of `cmd_prepare` leaves the temporary file
  behind and none reaches a later stage holding it. Observed by AC1 and AC3.
- **S3** — The fixture. TOOL-dSafePassage-8's `--prepare` fixture, with the walk passing and a
  committed `regen.py` that exits 1, as `tools/push-main.test.sh` arm 30 plants one (`:993-1009`),
  asserts that `git status --porcelain` names no path after the refusal, and that the retried
  `--prepare` without the plant builds a merge holding no before-image or order from the refused
  run. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The attended landing. TOOL-dSafePassage-8 S4 commits gov first there as its own commit before the
  regeneration, so a regeneration refusal on that path meets the walk's files tracked, and its own
  snapshot at `tools/push-main.sh:1100` is taken after that commit.
- The refusals after the regeneration, which run on files `git add -A` already staged: the class arm
  of `TOOL-dSafePassage-28`.
- A shared snapshot helper, its write guard and the stale comment above `remove_new_untracked`:
  findings 25 and 36, the minors batch `TOOL-dSafePassage-35`.

### Edges

- **consumes-from** `TOOL-dSafePassage-25` — the gov-first snapshot and its refusal shape in `cmd_prepare`; without them there is no snapshot taken before the walk to keep alive
- **hands-off** `TOOL-dSafePassage-28` — the class arm over every refusal of the prepared path after the walk, of which the regeneration refusal fixed here is the first
- **hands-off** `TOOL-dSafePassage-35` — the snapshot helper and its write guard, which this unit's one snapshot site keeps as an inline line

## 4. Design

### The prepared path after this unit

```bash
gfsnap=$(mktemp) && git ls-files --others --exclude-standard -z 2>/dev/null | LC_ALL=C sort -z > "$gfsnap"
if ! run_gov_first "$R" "$oldb"; then
  git reset -q --hard "$t" >/dev/null 2>&1 || true
  remove_new_untracked "$gfsnap"; rm -f "$gfsnap"
  git checkout "$branch" >/dev/null 2>&1 || true
  echo "push-main: the steps this landing introduces could not be run on gov first (named above). ..." >&2
  return 1
fi
if ! run_regen; then
  git reset -q --hard "$t" >/dev/null 2>&1 || true
  remove_new_untracked "$gfsnap"; rm -f "$gfsnap"
  git checkout "$branch" >/dev/null 2>&1 || true
  echo "push-main: the generated outputs this landing owes could not be regenerated (named above). ..." >&2
  return 1
fi
rm -f "$gfsnap"
```

The refusal lines keep today's text in full; the block elides them. The arguments of
`run_gov_first` are TOOL-dSafePassage-8's.

### Why the earlier snapshot is safe to clean against

Between the snapshot and the regeneration only `run_gov_first` runs, and every untracked path it
makes is one this landing must not keep on refusal. The tree the snapshot is taken on is the mint's:
`run_minter` writes version carriers, which are tracked, so the snapshot holds exactly the untracked
set the operator had before the landing, and cleaning against it keeps every one of those paths.

### Inventory

Minted: nothing. The local `rgsnap` of `cmd_prepare` is no longer assigned there; the attended
path's `rgsnap` at `tools/push-main.sh:1100` is unchanged. No function, conf key, gate leg or policy
key.

### Migration

None.

### Rollout

Live at landing. It builds at order 5, after TOOL-dSafePassage-25 (order 4), whose block it edits.

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/push-main.test.sh`

### Alternatives rejected

- **Clean against both snapshots.** The earlier one is a subset of the later, so the second compare
  adds nothing and keeps a second temporary file alive.
- **Take the regeneration's snapshot before `run_gov_first`.** That is this unit's shape spelled as
  two variables holding one value.
- **Stage the walk's files before the regeneration.** The merge is rewritten once, after the
  regeneration, so staging earlier only moves the leak into the index.

## 5. Production-readiness checklist

- security: no new write; a refusal cleans only paths created after the snapshot.
- perf / scale: one `ls-files` per landing, one fewer than TOOL-dSafePassage-25 leaves.
- error / empty / loading states: a snapshot that cannot be written is finding 36, carried by
  `TOOL-dSafePassage-35`; this unit keeps TOOL-dSafePassage-25's line as written.
- observability: both refusal lines are unchanged.
- risks: a regeneration that writes an untracked file the operator also created after the snapshot
  would clean it; the window is the landing's own run, during which the tree is the lander's.
- testing: the `tools/push-main.test.sh` arm of §7.
- migration: none.
- user docs: N/A — TOOL-dSafePassage-8 §5 records that no `help/` page covers the lander.

## 6. Acceptance criteria

- **AC1** — When `bash tools/push-main.sh --prepare --slug fx` runs in TOOL-dSafePassage-8's AC5
  fixture with the walk passing and a committed `regen.py` that exits 1, it exits 1 naming the
  regeneration, leaves the branch at its old sha, and `git status --porcelain` in the fixture prints
  nothing.
  Red when: the walk's receipt, a before-image or an order is left untracked after the regeneration
  refuses.
  fixture: a scratch clone under `%TEMP%`, built as `build_regen_fixture` builds one
  (`tools/push-main.test.sh:934`), with TOOL-dSafePassage-8's step plant.
- **AC2** — When the same command runs again in that fixture with the failing `regen.py` reverted,
  it exits 0, and `git ls-tree -r --name-only HEAD -- .governance/steps .governance/outbox` in the
  prepared merge names no file the refused run made.
  Red when: a leftover of the refused run is folded into the retried merge.
- **AC3** — When `git grep -n -e "gfsnap" -e "rgsnap" -- tools/push-main.sh` runs after the pass,
  `cmd_prepare` shows `gfsnap` at its one assignment and in both refusal branches, and `rgsnap`
  appears only in the attended path.
  Red when: `cmd_prepare` still takes a second snapshot after the walk.

## 7. Gates

`push-main self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/push-main.test.sh · covers AC1 AC2 · the gov-first fixture landing with the walk passing and a failing regeneration asserts a clean status after the refusal and a clean merge after the retry, its failing case staged by a lander copy whose regeneration refusal cleans against a snapshot taken after the walk · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 1 (HIGH, item D-1, shared with id 35).

## 10. Reuse audit

The seam extended is the lander's refusal pair in `cmd_prepare`: TOOL-dSafePassage-25's gov-first
snapshot and the regeneration refusal (`tools/push-main.sh:908-916`) with its helper
`remove_new_untracked` (`:784-793`), whose snapshot this unit takes once instead of twice.
`python tools/codebase-map/reuse_lookup.py "clean the untracked files a refused lander stage made
after an earlier stage passed"` ranked `CensusRefused`, `ScopeRefused` and `corpus_files`,
name-token matches; the map ranks no function of `tools/push-main.sh` for the phrase, while the source holds the exact precedent, so the hits and the
source disagree there, as TOOL-dSafePassage-25 §10 recorded.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
