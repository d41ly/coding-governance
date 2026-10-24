# TOOL-dDeclaredLoop-69 — a merge whose clean re-merge is computable is graded against that re-merge alone

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 18 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-69-deviation-691.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-69-deviation-691.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 2 at HIGH**, its item **H2**, alone in that item. `TOOL-dDeclaredLoop-59` S1 and
its §4 grade exempt every key whose value at the merge equals some parent's value, even when the clean
re-merge C is computable. A resolution that sets a cleanly mergeable key back to the value of the parent
that never changed it differs from C and owes nothing: main moves key `k` from 1 to 2, a run branch that
never touched `k` merges main and resolves `k` back to 1, and a policy change lands on main with no
`Gov-Policy:` trailer. 59 §5's claim that the resolution edit still owes its trailer is false on that path.

This unit takes the skeptic's corrected fix: where C is computable it is the whole reference, and the
parent-equality exemption survives only where C is not. It repairs `TOOL-dDeclaredLoop-59`.

## 2. Scope (IN)

- **S1** — Where C is computable, the pre-filter is `blob(M) != blob(C)` and the owed set is exactly the
  keys with `val(M, k) != val(C, k)`; no parent's value exempts a key. This supersedes 59 S1's "equals
  neither any parent's value nor the clean re-merge's value" on that branch. Observed by AC1, AC2.
- **S2** — Where C is not computable, 59 S2's conflicted re-merge and 59 S3's octopus or missing
  `merge-tree --write-tree` cases, the grade is 59's unchanged: the "differs from every parent"
  pre-filter, the parent-equality exemption and 59 S3's printed line. Observed by AC3.
- **S3** — The fixture cases `push-merge-revert-to-unchanged-side` join `guard.py --fixture` in two
  variants: the run branch touching the policy file at another key, and the run branch not touching it
  at all. Both merges resolve `k` to the unchanged side's value with no trailer, and both exit 1 naming
  the merge and `k`. Observed by AC1.
- **S4** — 59's own plants keep their verdicts under S1: the both-sides-clean merge equals C and owes
  nothing, and the resolution edit differs from C at the key it sets. Observed by AC2.

## 3. Non-goals (OUT)

- When C is computable after a conflict elsewhere: the audit's id 41, batched into
  `TOOL-dDeclaredLoop-75`, which widens the computable case this unit grades.
- The non-merge rule and the first-push walk: `TOOL-dDeclaredLoop-44` and `TOOL-dDeclaredLoop-67`,
  unchanged; the walk applies whatever grade `check_push_range` holds.
- A checklist entry that a merge-grading rule's fixtures include a revert to the stale side, the
  finding's left-shift: the class is recorded at the close; S3 is this rule's fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-59` — the merge key grade in `check_push_range` of `tools/loop/guard.py`, whose computable branch this unit restates against the clean re-merge alone
- **hands-off** `TOOL-dDeclaredLoop-75` — the computable branch, which that unit widens to a merge-tree exit 1 whose conflicts miss the policy file (id 41)
- **hands-off** `TOOL-dDeclaredLoop-78` — the C branch, whose reference that unit splits into three named states so a clean re-merge lacking the policy file is graded (the round-4 spec audit's id 33)
- **hands-off** `TOOL-dDeclaredLoop-79` — the grade's pre-filter and stated cost, which that unit restates to skip only a merge whose policy blob equals every parent's (ids 7, 12); this pass keeps the sibling-minted `loop guard fixtures` leg green (id 3)

## 4. Design

### Evidence

- 59 §4's pseudo-code owes `{ k : val(M,k) != val(Pi,k) for every i, and (C is none or val(M,k) !=
  val(C,k)) }` (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-59.md`, §4 The
  grade), so a key equal to any parent is exempt on both branches.
- `git merge-tree --write-tree <p1> <p2>` prints the clean tree's id on its first line; the blob of the
  policy path in that tree is C, as 59 S2 specifies: probe recorded in 59 §4, PINNED 2026-10-24.

### The grade, restated

```
for merge M in the range, with parents P1..Pn:
    C = 59 S2's clean re-merge blob, or none
    if C is not none:
        skip unless blob(M) != C
        owed = { k : val(M,k) != val(C,k) }
    else:                                                    # 59 S2 and S3, unchanged
        skip unless blob(M) differs from every blob(Pi)
        owed = { k : val(M,k) != val(Pi,k) for every i }
    owed non-empty and no Gov-Policy trailer naming each key -> refuse naming M and the keys
```

An absent key reads as its own value on both branches, as 59 §4 states.

### Files touched (estimate)

- `tools/loop/guard.py`

### Alternatives rejected

- **Keeping the parent exemption and adding a revert special case.** It enumerates one bad resolution
  where the clean re-merge already defines every good one.
- **Dropping the parent branch altogether.** With no C, a resolution that takes one side's conflicting
  value would be owed, which 59 AC3 rightly passes.

## 5. Production-readiness checklist

- security — closes a path on which a policy change reaches the default branch untrailered.
- perf / scale — unchanged: C is already computed per two-parent merge by 59 S2.
- error / empty / loading states — a policy file absent at M and at C is equal and owes nothing.
- observability — the refusal names the merge and each owed key, as 59 prints it.
- risks — a merge that hand-edits a key back to the stale side now refuses; that is the defect.
- testing — AC1 to AC3 as fixture plants; the arm under §7, observed at the close.
- migration — none: the rule is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant push-merge-revert-to-unchanged-side` runs each of
  its two variants, each exits 1 naming the merge and key `k`.
  Red when: the parent-equality exemption still applies where C is computable, so both exit 0.
- **AC2** — When `--plant push-merge-both-sides-clean` and `--plant push-merge-resolution-edit` run, the
  first exits 0 and the second exits 1 naming its key.
  Red when: the restated grade changes a verdict 59 fixed.
- **AC3** — When `--plant push-merge-octopus` and `--plant push-merge-conflict-pick` run, both exit 0,
  and the octopus run prints `graded against its parents only`.
  Red when: the fallback branch loses its parent exemption.

## 7. Gates

`measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 · the two revert variants beside 59's four plants, staged against TOOL-dDeclaredLoop-59's grade, which exempts a key equal to any parent · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 2 (HIGH, item H2).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-78 and TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 59's own grade in `check_push_range` and the clean re-merge it already computes; this unit
changes which reference the computable branch compares against and mints nothing.
`python tools/codebase-map/reuse_lookup.py "grade a merge commit against its clean re-merge"` ranked
`merge` (`tools/memory-tree/merge-rows.py`, `tools/settings-merge.py`) and `build_commit`, row and settings
mergers that grade no policy key; `tools/loop/guard.py` is unbuilt at base, so the seam is 59's spec.

Recall terms used: merge-tree write-tree clean re-merge policy key grade Gov-Policy trailer parent exemption push range
