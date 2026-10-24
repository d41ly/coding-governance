# TOOL-dDeclaredLoop-78 — the clean re-merge has three states, and a re-merge that lacks the policy file is graded, never treated as none

**Status:** DEFERRED · rev-5 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 19 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-79 |
| [2026-10-24-build-TOOL-dDeclaredLoop-78-deviation-781.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-78-deviation-781.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-79 |
| [2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-79 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md`)
confirmed finding **id 33 at HIGH**, its item **H3**, alone in that item. `TOOL-dDeclaredLoop-69` takes C
from `TOOL-dDeclaredLoop-59` S2, "blob of merge-tree --write-tree P1 P2, when n == 2, it exits 0 and
parses; else none", and falls to the parent branch, where the parent-equality exemption still applies,
whenever C is none. Neither spec says whether a clean re-merge whose tree lacks the policy path parses or
is none, while 69 §5 compares "a policy file absent at M and at C" as a value. Read as none, it reopens
the path 69 closes: main deletes or empties the policy file, a run branch that never touched it merges
main, the resolution keeps the run branch's bytes, blob(M) equals that parent's, the merge is skipped,
and the old policy keys reach main with no `Gov-Policy:` trailer.

This unit gives C three named states and grades two of them on the C branch. It repairs
`TOOL-dDeclaredLoop-69`.

## 2. Scope (IN)

- **S1** — C has three states in `check_push_range` of `tools/loop/guard.py`. `uncomputable`: an octopus
  merge, a git without `merge-tree --write-tree`, or a re-merge that does not exit 0. `present`: exit 0
  and the printed tree holds the policy path, its blob being C. `absent`: exit 0 and the tree lacks the
  policy path, every key reading absent. A missing path is never `uncomputable`. Observed by AC1, AC2.
- **S2** — `present` and `absent` are graded on 69's C branch: skip only when M's policy blob equals C,
  an absent file at M equalling an `absent` C; otherwise owe each key with `val(M,k) != val(C,k)`, an
  absent key reading as its own value as 59 §4 states. Only `uncomputable` takes 69 S2's parent branch.
  Observed by AC1, AC2, AC3.
- **S3** — A policy blob that does not parse refuses by name, never skips and never raises: at M, at a
  `present` C, or at a parent the `uncomputable` branch reads, the refusal is
  `policy: <merge8> — the policy file does not parse at <M | C | parent <sha8>>: <reason>`.
  Observed by AC4.
- **S4** — The fixture plants `push-merge-resurrect-deleted-policy`, `push-merge-resurrect-emptied-policy`
  and `push-merge-both-absent` join `guard.py --fixture`: main's tip lacks the policy file, or holds it
  with no keys, and a run branch that never touched it merges main keeping its own bytes with no trailer;
  and a merge where neither parent nor M holds the file. Observed by AC1, AC2, AC3.

## 3. Non-goals (OUT)

- A re-merge that exits 1 with the policy path outside its conflicts: `TOOL-dDeclaredLoop-75` S27, which
  widens `present` and `absent` to that exit, as this unit's hands-off bullet to 75 records.
- The pre-filter's cost and its order before C: the audit's ids 7 and 12, batched into
  `TOOL-dDeclaredLoop-79`.
- A bug-class checklist entry that a "value or none" sentinel states which inputs map to none, the
  finding's left-shift: the class is recorded at the close; S4 is this grade's deleted-file fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-69` — the C branch of the merge key grade in `check_push_range` of `tools/loop/guard.py`, whose reference this unit splits into three named states
- **hands-off** `TOOL-dDeclaredLoop-75` — the three states, which S27 widens to a merge-tree exit 1 whose conflicts miss the policy path; its "its blob parses" reads as S3's refusal on a computable C that does not parse, never a fall to the parents
- **hands-off** `TOOL-dDeclaredLoop-79` — the `absent` state, which that unit's pre-filter counts as a value when it compares M with every parent (ids 7, 12)
- **hands-off** `TOOL-dDeclaredLoop-81` — the `uncomputable` state, which that unit narrows to an octopus merge or a probed absence of the feature, every other failed re-merge refusing by name and never taking the parent exemption (the round-5 spec audit's id 28)
- **hands-off** `TOOL-dDeclaredLoop-82` — S4's plant list and AC2, which that unit completes with `push-merge-unparseable-c` and `push-merge-unparseable-parent` and restates to the break AC2 catches (the round-5 spec audit's ids 7, 8, 29)
- **hands-off** `TOOL-dDeclaredLoop-84` — S1's `uncomputable`, S2's parent-branch sentence and §4's grade block, which that unit restates to 81's exit table (the round-6 spec audit's id 7)
- **hands-off** `TOOL-dDeclaredLoop-86` — S3's parse refusal at a parent, which that unit widens to every branch that reads the parents (the round-6 spec audit's id 3)
- **hands-off** `TOOL-dDeclaredLoop-88` — S1's state count and §4's grade block, which that unit restates to five states, a five-way dispatch and a failed-probe line (the round-7 spec audit's ids 2, 5, 20)
- **hands-off** `TOOL-dDeclaredLoop-90` — the H1, S1 and hands-off edge that count C's states, which that unit restates to five (the round-8 spec audit's id 26)

## 4. Design

### Evidence

Probed 2026-10-24 on node `d`, git 2.54.0.windows.1, in a scratch repository under `%TEMP%`: PINNED, that date.

- With `p.toml` deleted on `main` and untouched on `run`, `git merge-tree --write-tree main run` exited 0
  and `git ls-tree` of the printed tree held no `p.toml`: the `absent` state.
- With `p.toml` deleted on `main` and modified on `run`, `git merge-tree --write-tree --name-only main run`
  exited 1, listed `p.toml` among the conflicted paths and printed `CONFLICT (modify/delete)`, leaving
  run's version in the tree: a conflicted blob that parses, so the conflict list and not a parse decides
  computability once 75 S27 admits exit 1.
- 59 §5 already refuses a policy file that does not parse at the merge
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-59.md`, §5 error line).

### The grade, restated

```
for merge M in the range, with parents P1..Pn:
    C = uncomputable                     if n != 2, or merge-tree --write-tree is missing, or it exits != 0
        absent                           if it exits 0 and its tree lacks the policy path
        present(blob)                    if it exits 0 and its tree holds the policy path
    unparseable blob at M, at present C, or at a parent read below -> refuse naming M and the side
    if C is not uncomputable:
        skip when blob(M) == C, absent == absent included
        owed = { k : val(M,k) != val(C,k) }                         # absent C: every key reads absent
    else:                                                            # 69 S2, unchanged
        skip unless blob(M) differs from every blob(Pi)
        owed = { k : val(M,k) != val(Pi,k) for every i }
    owed non-empty and no Gov-Policy trailer naming each key -> refuse naming M and the keys
```

### Files touched (estimate)

- `tools/loop/guard.py`

### Alternatives rejected

- **Reading a missing path as an empty file.** It answers the same keys but makes "absent at M and at C"
  compare an empty blob with no blob, so a merge deleting the file where C keeps it would read equal.
- **Falling back to the parents on an unparseable blob.** A broken file at C would then reopen the parent
  exemption the C branch exists to close.

## 5. Production-readiness checklist

- security — closes a path on which an old policy reaches the default branch untrailered.
- perf / scale — unchanged from 69: the states are read from the one `merge-tree` call 69 already makes.
- error / empty / loading states — S3 refuses on an unparseable blob by name; `absent` and empty are
  graded, never skipped.
- observability — the refusal names the merge, the side and the keys.
- risks — a merge that resurrects a deleted policy file now owes a trailer for every key it brings back;
  that is the defect.
- testing — AC1 to AC4 as fixture plants; the arm under §7, observed at the close.
- migration — none: the rule is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant push-merge-resurrect-deleted-policy` runs a merge whose
  clean re-merge lacks the policy file while M keeps the run branch's bytes, with no trailer, it exits 1
  naming the merge and each key M holds.
  Red when: a missing path reads as `uncomputable`, the parent branch exempts every key and the arm exits 0.
- **AC2** — When `--plant push-merge-resurrect-emptied-policy` runs the same merge with main's file emptied
  to no keys, it exits 1 naming each key M holds.
  Red when: an empty C is skipped as unparseable or none.
- **AC3** — When `--plant push-merge-both-absent` and 69's `push-merge-revert-to-unchanged-side` run, the
  first exits 0 and the second exits 1 naming key `k`.
  Red when: absent at M and at C compares unequal, or the restated grade loses 69's verdict.
- **AC4** — When `--plant push-merge-unparseable-c` makes a computable C whose policy blob does not parse,
  it exits 1 printing `does not parse at C` and no traceback.
  Red when: the arm falls to the parents, skips the merge or raises.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop guard fixtures` leg (`TOOL-dDeclaredLoop-2`) green, which runs
`guard.py --fixture`; the leg is outside the base manifest.

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC4 · the resurrect, both-absent and unparseable-C plants, staged against TOOL-dDeclaredLoop-69's C, which reads a re-merge lacking the file as none · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-4 spec audit's id 33 (HIGH, item H3).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-81 and TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-84 and TOOL-dDeclaredLoop-86, written by the round-6 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 69's grade in `check_push_range` and the single `merge-tree --write-tree` call 59 S2 already
makes; this unit names the states that call's exit and tree already distinguish and mints nothing.
`python tools/codebase-map/reuse_lookup.py "tell an absent file in a tree from a conflicted merge"` ranked
`tree`, `merge` (`tools/memory-tree/merge-rows.py`, `tools/settings-merge.py`), `absent` and
`load_map_tree`, none of which reads a policy path out of a re-merge; `tools/loop/guard.py` is unbuilt at
base, so the seam is 59's and 69's specs.

Recall terms used: merge-tree write-tree clean re-merge policy file absent deleted uncomputable Gov-Policy trailer parent exemption
