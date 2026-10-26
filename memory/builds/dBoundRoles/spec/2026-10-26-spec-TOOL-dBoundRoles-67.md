# TOOL-dBoundRoles-67 — unit 65's leftover sweep also selects the observation's worktrees by what they checked out, so a leftover at an unnamed `%TEMP%` path is found

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 38 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-owner-review-stop.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-owner-review-stop.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted specs 65 and 66
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. Id 14 shares the item at HIGH and takes
`TOOL-dBoundRoles-68`. No other id shares it.

Id 1 is the coherence face of the item. Spec 65's S5 and AC4 compare this repository's registered
worktrees only against S2's root, `<TEMP>/dbr63obs`. That root gets its name at order 37. The
observations it guards ran earlier, under a short `%TEMP%` path nobody named: spec 60 at order 33
(its §4 "Where each item lands"), spec 63's S12 at order 35 and spec 64's S18 at order 36. Nothing in
spec 65 re-runs an observation under `dbr63obs`. A worktree leaked at orders 33 to 36 therefore sits
outside the only operand S5 and AC4 read, and AC4 certifies "no leftover" over a directory nobody used.

This unit gives the sweep a second operand that finds those worktrees wherever they sit: the commit
they checked out. It repairs `TOOL-dBoundRoles-65` and builds one step after it (order 38).

## 2. Scope (IN)

- **S1** — The signature. Spec 65's S5 names a second operand for its sweep, the observation's
  signature. An entry of `parse_worktrees` (`tools/branch-reconcile/branch_reconcile.py`) carries the
  signature when its `flags` hold `detached` and its `head` equals the parent of the commit
  `git log -1 --format=%H -S derive_overlay_expected -- tools/govkit/selftest.py` prints, the commit
  spec 63's S12 checks out the parent of. Every observation of orders 33 to 36 checked out that parent,
  so the signature selects their worktrees at `dbr63obs` or at any unnamed path. A signature command
  that prints nothing stops the sweep with a non-zero exit naming the empty signature. An empty
  signature never reads as "no leftover". Observed by AC1 and AC2.
- **S2** — The sweep over this repository. The pass runs S1's selection over this repository's
  `git worktree list --porcelain -z`, beside spec 65's comparison against S2's root. Before anything is
  taken away, it records the signature sha and every entry each operand selected in unit 65's
  AMENDED answer to AC4. Observed by AC2 and AC3.
- **S3** — What the sweep may take away. A signature entry goes to git's forced worktree removal only
  when all three hold. It is not `locked`. It lies under the directory `os.environ["TEMP"]` names, by
  spec 65's S1 comparison. Units 60, 63 and 64, whose passes ran the observation, each carry `CLOSED`
  in their spec status header, so no live pass of this build owns it. A signature entry that fails any
  of the three is recorded and left in place, AC2 stays red naming it, and the pass parks it with the
  reason (BUILD-METHOD M6). Observed by AC2.
- **S4** — Spec 65 follows the sweep. Spec 65's S5 states S1 to S3. Its AC4 names both operands: S1's
  comparison against S2's root and the signature selection, over this repository's porcelain list,
  print nothing. Observed by AC1.
- **S5** — The amendment. The pass bumps spec 65 FIRST, with a §9 line naming this unit
  (BUILD-METHOD M2, READY). Unit 65's ledger answers AC4 on one line, in spec 66's S23 grammar
  `- AC4 — amended rev-<latest> (rev-<a>, ...) — <observation>`, rewriting any earlier answer in
  place. Observed by AC3.

## 3. Non-goals (OUT)

- Id 14's half, the positive control that proves the signature selection sees a planted leftover
  outside the root and the statement that AC4 over `dbr63obs` alone is green by construction. It is
  `TOOL-dBoundRoles-68`'s at the same order. Neither unit reads the other's output. Both spell S1's
  selection in the same words, so no edge joins them.
- The one cleanup rule of report item M5, which settles every entry a pass may take away under the
  root. `TOOL-dBoundRoles-69` states it at order 39 and admits S3's signature entries into it.
- The report's left-shift checklist entry, "a criterion that sweeps for leftovers names the location
  every earlier producer used". No clause of this build names it, and AC2 is this unit's regression.
- A shipped sweep. The selection is a criterion probe's, run by this pass. No shipped code reads the
  signature.

### Edges

- **consumes-from** `TOOL-dBoundRoles-65` — S1's comparison, S2's root, S5 and AC4, which S2 runs beside and S4 restates (id 1 of the round-1 audit of units 65 and 66)
- **consumes-from** `TOOL-dBoundRoles-63` — S12's commit, whose parent every observation checked out and S1 takes as the signature (id 1)
- **hands-off** `TOOL-dBoundRoles-69` — S3's take-away of signature entries, which unit 69's one cleanup rule admits by name (id 12 of the same audit)

## 4. Design

### The selection

```python
import os, subprocess, sys
sys.path.insert(0, "tools/branch-reconcile")
import branch_reconcile as br

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()

def signature():
    c = git("log", "-1", "--format=%H", "-S", "derive_overlay_expected", "--", "tools/govkit/selftest.py")
    if not c:
        sys.exit("sweep: the signature command printed nothing; refusing to read an empty signature as clean")
    return git("rev-parse", c + "^")

def signed(text, sig):
    return [w for w in br.parse_worktrees(text) if "detached" in w["flags"] and w["head"] == sig]
```

The block shows the design's shape. The pass fits it to spec 65's comparison, and S3 filters the
selected entries before any is taken away. `head` and `flags` are fields `parse_worktrees` already
returns. The selection reads no path at all, so it cannot depend on how `%TEMP%` was spelled when the
worktree was made.

### Why the signature is specific

The commit is the one that took `derive_overlay_expected` out of `tools/govkit/selftest.py`, and spec
63's S12 requires its subject to name `TOOL-dBoundRoles-19`. Its parent is a fixed sha. A worktree
detached at that sha is the observation's, or a hand-made checkout of the same old tree. S3's three
conditions keep a take-away to the first kind: `TEMP` is where the observation put it, `locked` is how
a human pins a worktree, and the `CLOSED` headers prove the observing passes are over.

### Evidence

Read at base `462d20f3` on 2026-10-26; HEAD equals base for every code file cited here:

- `tools/branch-reconcile/branch_reconcile.py:188-212` is `parse_worktrees`. It keeps `HEAD` as
  `head` (`:204-205`) and `detached`, `locked` and `prunable` in `flags` (`:208-209`). `:165-172` are
  `derive_key` and `check_under`, the comparison spec 65's S1 adopts.
- Spec 63's S12, lines 83-89, names the commit command and says the worktree is checked out at its
  parent "under a short `%TEMP%` path". Spec 64's S18, lines 116-121, keeps "a short `%TEMP%` prefix".
  Spec 60's §4 "Where each item lands", line 212, extracts "under `%TEMP%`, short-pathed".
- `git grep -n derive_overlay_expected -- tools` prints nothing at base: unit 54 adds the function at
  order 6 and unit 19 takes it out at order 24. So the signature command prints nothing on today's
  tree, and S1's stop is what keeps a sweep run before order 24 from passing.
- `git worktree list --porcelain` prints 30 `worktree` lines and one `detached` entry, none under
  `%TEMP%`. The detached entry's `head` is not a parent of a unit-19 commit, which does not exist yet.
- `tools/workflows/unattended-unit.js:314-318` has each unit pass set its spec header to `CLOSED` in
  its own commit, so S3's third condition is readable from the tree at order 38.

### Inventory

Minted: none. The signature is a sha read at the pass, not an identifier.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 38, after unit 65 at order 37. `TOOL-dBoundRoles-68` holds order 38 and also
writes spec 65 and unit 65's ledger. The declared write sets intersect, so `--dispatch` refuses the
second pass while the first is open (M6 clause 1). Each unit amends a different criterion of spec 65,
AC4 here and a new AC6 there, so neither rewrites the other's ledger line.

### Files touched (estimate)

- the spec of TOOL-dBoundRoles-65, a rev bump (S4, S5), named here for the dispatch write set
- the acceptance ledgers of unit 65 and this unit, the AMENDED AC4 answer and the pre-sweep record,
  named here for the dispatch write set
- no tracked file otherwise: S3 takes away worktree registrations under `.git/worktrees`, which git
  owns

### Alternatives rejected

- **The report's first fix for id 1, judged UNSOUND by its skeptic.** The skeptic's corrected fix is
  S1 to S3.
- **A location sweep over all of `%TEMP%`.** Other sessions' fixture clones and worktrees sit there
  (spec 65 §4 "Alternatives rejected"), so a location alone cannot say which entry is the
  observation's.
- **Re-running the observation under `dbr63obs` and sweeping only that root.** It proves the new root
  is clean, and says nothing about the worktrees orders 33 to 36 may already have leaked.
- **Taking away every signature entry, wherever it sits.** A detached checkout of the same sha that a
  human made outside `TEMP`, or locked, is not this build's to take away.

## 5. Production-readiness checklist

- security — no shipped write path. The pass hands git's forced worktree removal only an entry that
  carries the signature, is not locked, lies under `TEMP`, and whose observing passes are `CLOSED`.
  Anything else is recorded and parked.
- perf / scale — one `git log -S` over one file's history, one porcelain read, one sha compare per
  entry.
- error / empty / loading states — an empty signature exits non-zero naming it. A failing `git` call
  raises from `check=True`, so an empty porcelain is never read as clean.
- observability — unit 65's ledger records the signature sha and both operands' selections before
  any take-away.
- risks — a hand-made detached checkout of the same sha under `TEMP` would be taken away. It holds a
  tree from before order 24, and the parent sha is printed first, so the record shows what went.
- testing — AC1 by an extraction probe, AC2 by the sweep over this repository, AC3 by a ledger probe.
  The selection's positive control is `TOOL-dBoundRoles-68`'s AC2. No suite arm.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe extracts spec 65's S5 and AC4 bullets, joins their lines and
  collapses their whitespace, S5 names `detached`, `derive_overlay_expected`, the parent, `locked`,
  `TEMP`, the `CLOSED` headers of units 60, 63 and 64, and the stop on an empty signature. AC4 names
  `dbr63obs` and the signature both. Spec 65's §9 holds a line naming `TOOL-dBoundRoles-67`.
  Red when: AC4 names one operand only, so a leftover at an unnamed `%TEMP%` path passes it.
- **AC2** — When the pass's sweep runs over this repository's `git worktree list --porcelain -z` after
  S3's take-away, it prints a 40-hex signature sha and selects no entry by either operand.
  Red when: a worktree detached at the signature stays registered outside `dbr63obs`, or the signature
  resolves empty and the sweep prints nothing.
  figure: DERIVED at observation time.
- **AC3** — When a `python -c` probe reads unit 65's `**Evidences:**` block, exactly one line answers
  AC4 and `LEDGER` of `tools/memory-tree/deviation_join.py:163` matches it. The spec-65 revision whose
  §9 line names `TOOL-dBoundRoles-67` is the revision `LEDGER` captures, or one inside the
  parenthesised list after it. The line holds the signature sha and the pre-sweep selections.
  Red when: a second line answers AC4, this unit's revision is missing from the line, or the line
  records no pre-sweep selection.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

No suite arm moves. The sweep is a probe of this pass, and it records its readings.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 65 carries no
  clause, so veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 65 and 66, id 1
  (HIGH, item H1, shared with id 14), on the skeptic's corrected fix.

## 10. Reuse audit

The seam is `tools/branch-reconcile/branch_reconcile.py`'s `parse_worktrees`, whose `head` and
`flags` fields the selection reads, beside the `derive_key` and `check_under` comparison spec 65
already adopts. `python tools/codebase-map/reuse_lookup.py "find leftover git worktrees by their checked-out commit wherever they sit"`
ranked `git`, `check`, `build_commit`, `run_git` and `add_scratch_worktree`. None selects worktrees by
their checked-out commit, so no existing seam fits beyond `parse_worktrees`. The recall query's hits
include the H1 fix itself, `TOOL-dSweptBranches-1`, which defines the porcelain flags this reads, and
`TOOL-dSweptBranches-8`, whose take-away reaches only a proven worktree, the rule S3 follows.

Recall terms used: `python tools/memory-recall/query.py "how is a leftover scratch worktree found and removed safely without touching another session's" --terms "worktree porcelain detached HEAD signature leftover sweep prunable locked forced removal temp root"`
