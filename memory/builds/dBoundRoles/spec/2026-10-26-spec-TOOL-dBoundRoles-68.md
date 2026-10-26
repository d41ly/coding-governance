# TOOL-dBoundRoles-68 — unit 65's AC4 says it is green by construction over `dbr63obs` alone, and a positive control proves the signature selection sees a leftover outside that root

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 38 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-owner-review-stop.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-owner-review-stop.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-67 TOOL-dBoundRoles-69 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted specs 65 and 66
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md`)
confirmed finding **id 14 at HIGH**, report item **H1**. Id 1 shares the item at HIGH and takes
`TOOL-dBoundRoles-67`. No other id shares it.

Id 14 is the blast-radius face of the item. A worktree leaked by a failed import at orders 33 to 36
sits outside spec 65's operand `<TEMP>/dbr63obs`, so spec 65's AC4 prints nothing and certifies "no
leftover" over exactly the runs that could have leaked. The skeptic re-ran the check: AC4 is green on
today's tree by construction, because no observation has ever run under that root. Spec 65 says none
of this, and nothing proves that a selection able to find those worktrees can fail.

This unit writes the by-construction fact beside AC4 and adds the positive control: in a scratch
repository, the signature selection reports a detached worktree planted outside any `dbr63obs` root,
rejects its look-alikes, and refuses an empty signature. It repairs `TOOL-dBoundRoles-65` and builds
one step after it (order 38).

## 2. Scope (IN)

- **S1** — What AC4 does not see. Spec 65 gains a scope item, S7. Over `dbr63obs` alone AC4 is green
  on the tree at `462d20f3` by construction, because no observation has run under that root. The
  observations of orders 33 to 36 ran under an unnamed short `%TEMP%` path. The signature selection is
  what covers them, and AC6 is its positive control. Observed by AC1.
- **S2** — The control's repository. The pass makes a scratch repository under `%TEMP%/dbr68c`,
  short-pathed. Commit c1 adds `f.txt` holding the token `dbr68tok`, and commit c2 takes the token out,
  so `git log -1 --format=%H -S dbr68tok -- f.txt` prints c2 and the signature is c1. That is the shape
  of spec 63's S12 commit, which takes `derive_overlay_expected` out. Under `%TEMP%/dbr68c/o` the
  pass adds three worktrees: `1` detached at c1, `2` detached at c2, and `3` on a new branch at c1. It
  also makes the empty directory `%TEMP%/dbr68c/dbr63obs`. Observed by AC2.
- **S3** — The control's readings. The signature selection is the same predicate in the same words as
  `TOOL-dBoundRoles-67`'s S1: an entry of `parse_worktrees` whose `flags` hold `detached` and whose
  `head` equals the parent of the commit the `git log -1 -S` command prints. Over the scratch
  repository's porcelain list it reports exactly `o/1`. Spec 65's S1 comparison against the empty
  `dbr63obs` reports nothing over the same list, which is the vacuity this unit names. After git's
  forced worktree removal has taken `o/1` away, the selection reports nothing. With the token
  `dbr68none`, which no commit touched, the selection exits non-zero naming the empty signature and
  reports no entry. The control runs inside its own repository, so it neither sees nor touches this
  repository's worktrees, and the scratch directory is cleared after. Observed by AC2.
- **S4** — Spec 65 gains AC6, stating S3's four readings with S2 as its fixture. Observed by AC1 and
  AC3.
- **S5** — The amendment. The pass bumps spec 65 FIRST, with a §9 line naming this unit
  (BUILD-METHOD M2, READY). Unit 65's ledger answers AC6 on one line, in spec 66's S23 grammar
  `- AC6 — amended rev-<latest> (rev-<a>, ...) — <observation>`. Observed by AC3.

## 3. Non-goals (OUT)

- Id 1's half, the sweep over this repository with its take-away rule and AC4's second operand. It is
  `TOOL-dBoundRoles-67`'s at the same order. Neither unit reads the other's output. S3 spells the
  predicate in the words 67's S1 uses, so no edge joins them.
- The one cleanup rule of report item M5. `TOOL-dBoundRoles-69` states it at order 39.
- The report's left-shift checklist entry, "a criterion that sweeps for leftovers ... states whether it
  is green by construction on the current tree". No clause of this build names it, and S1 is this
  unit's instance of it.
- A shared control helper. The control is a probe of this pass, as spec 65's S4 control is.

### Edges

- **consumes-from** `TOOL-dBoundRoles-65` — S1's comparison, S2's root and AC4, which S1 qualifies and S3 runs over an empty root (id 14 of the round-1 audit of units 65 and 66)
- **consumes-from** `TOOL-dBoundRoles-63` — S12's commit, a `-S` commit that takes a token out, whose shape S2's scratch commits copy (id 14)

## 4. Design

### The control

```bash
R="$(cygpath -m "$TEMP")/dbr68c"; mkdir -p "$R/r" "$R/dbr63obs"
git -C "$R/r" init -q
# c1 adds f.txt holding dbr68tok; c2 takes the token out
git -C "$R/r" worktree add --detach "$R/o/1" "$c1"
git -C "$R/r" worktree add --detach "$R/o/2" "$c2"
git -C "$R/r" worktree add -b side "$R/o/3" "$c1"
```

The readings run `parse_worktrees` over `git -C "$R/r" worktree list --porcelain -z`. Worktree `2`
fails the `head` half, and worktree `3` fails the `detached` half, so each is a should-not-match case.
The empty `dbr63obs` makes the root comparison's silence visible beside the selection's report. The
block shows the design's shape; the pass fits it to S3's readings.

### Evidence

Read at base `462d20f3` on 2026-10-26; HEAD equals base for every code file cited here:

- Measured in a scratch repository under `%TEMP%` built as S2 says. The selection reported
  `C:/Users/d41ly/AppData/Local/Temp/d68p/o/1` only. The root comparison against the empty
  `dbr63obs` reported nothing. `git log -1 --format=%H -S dbr68none` printed an empty string. After
  `git worktree remove --force` on `o/1`, three worktrees stayed registered: the main one, `o/2` and
  `o/3`.
- `tools/branch-reconcile/branch_reconcile.py:188-212` is `parse_worktrees`, keeping `head`
  (`:204-205`) and the `detached` flag (`:208-209`).
- Spec 65's AC4, lines 201-204, compares against `<TEMP>/dbr63obs` only. Its S4, lines 54-60, is the
  control this one is modelled on.
- `git worktree list --porcelain` of this repository names no path under `%TEMP%`, and no observation
  has run, so AC4 over `dbr63obs` prints nothing today whatever the tree holds.

### Inventory

Minted: none. `dbr68c`, `dbr68tok` and `dbr68none` are scratch names, not identifiers.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 38, after unit 65 at order 37. `TOOL-dBoundRoles-67` holds order 38 and also
writes spec 65 and unit 65's ledger. The declared write sets intersect, so `--dispatch` refuses the
second pass while the first is open (M6 clause 1). This unit adds S7 and AC6 to spec 65 and amends no
criterion 67 amends, so neither rewrites the other's ledger line.

### Files touched (estimate)

- the spec of TOOL-dBoundRoles-65, a rev bump (S1, S4, S5), named here for the dispatch write set
- the acceptance ledgers of unit 65 and this unit, the AC6 answer and the control's readings, named
  here for the dispatch write set

### Alternatives rejected

- **Staging a real failed observation in this repository.** It needs unit 19's commit and an import
  that fails on purpose, and spec 66's AC8 already stages that failure. The question here is whether
  the selection can see a worktree outside the root, which a scratch repository answers without
  touching this one.
- **Only the by-construction sentence.** It names the gap and proves nothing can close it. The control
  is what can fail.
- **Planting the leftover under `dbr63obs`.** The root comparison would report it too, so the control
  would not tell the two operands apart.

## 5. Production-readiness checklist

- security — no new write path. The control writes only its own scratch repository under
  `%TEMP%/dbr68c` and clears it after.
- perf / scale — one scratch repository, two commits, three worktrees, four readings.
- error / empty / loading states — the empty-signature reading is a staged case of its own and must
  exit non-zero.
- observability — unit 65's ledger records the four readings.
- risks — a scratch path long enough to fail a worktree checkout on Windows. `dbr68c` sits directly
  under `%TEMP%`, as spec 65's `dbr65c` does.
- testing — AC1 by an extraction probe, AC2 by the scratch control, AC3 by a ledger probe. No suite
  arm.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe extracts spec 65's S7 and AC6 bullets, joins their lines and
  collapses their whitespace, S7 names `dbr63obs`, `462d20f3`, "by construction" and orders 33 to 36.
  AC6 names `dbr68c`, `detached` and the empty-signature refusal. Spec 65's §9 holds a line naming
  `TOOL-dBoundRoles-68`.
  Red when: AC4's silence over an empty root still reads as coverage of the earlier observations.
- **AC2** — When the pass runs S3's control over the scratch repository's
  `git worktree list --porcelain -z`, the selection prints exactly the `o/1` path, the comparison
  against the empty `dbr63obs` prints nothing, the selection prints nothing after
  `git worktree remove --force` takes `o/1` away, and the `dbr68none` run exits non-zero naming the
  empty signature.
  Red when: the selection misses a signature worktree outside the root, selects a branch or
  other-commit worktree, or reads an empty signature as clean.
  fixture: a scratch repository under `%TEMP%/dbr68c`, short-pathed and cleared after; the tree holds
  none today.
- **AC3** — When a `python -c` probe reads unit 65's `**Evidences:**` block, exactly one line answers
  AC6 and `LEDGER` of `tools/memory-tree/deviation_join.py:163` matches it. The spec-65 revision whose
  §9 line names `TOOL-dBoundRoles-68` is the revision `LEDGER` captures, or one inside the
  parenthesised list after it.
  Red when: a second line answers AC6, or the line names no revision of this unit.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

No suite arm moves. S3's control is a write probe, so the pass runs it and records its readings.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 65 carries no
  clause, so veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 65 and 66, id 14
  (HIGH, item H1, shared with id 1), on the report's fix, which the skeptic judged sound.

## 10. Reuse audit

The seams are `tools/branch-reconcile/branch_reconcile.py`'s `parse_worktrees` and the scratch-control
shape of spec 65's S4, extended rather than rebuilt. `python tools/codebase-map/reuse_lookup.py "find leftover git worktrees by their checked-out commit wherever they sit"`
ranked `git`, `check`, `build_commit`, `run_git` and `add_scratch_worktree`. None is a positive control
for a worktree selection, so no existing seam fits beyond those named. The recall query's hits include
spec 65's own S4 control and `TOOL-dSweptBranches-1`, which defines the porcelain flags the selection
reads.

Recall terms used: `python tools/memory-recall/query.py "how is a leftover scratch worktree found and removed safely without touching another session's" --terms "worktree porcelain detached HEAD signature leftover sweep prunable locked forced removal temp root"`
