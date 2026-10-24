# TOOL-dDeclaredLoop-59 — a merge owes a policy trailer only for a key its result sets that no parent and no clean re-merge set

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 17 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-59-deviation-591.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-59-deviation-591.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 17 at HIGH**, its item **H2**, alone in that item. `TOOL-dDeclaredLoop-44` S2
grades a merge by `git diff-tree --cc -r --name-only <merge>` and says that list holds a path only when
the resolution edited it. It does not: a clean auto-merge in which each side changed a different line
of the file lists the path too, while the `--cc` patch prints no hunk. So a run branch changing one key
of the policy file and a main changing another owe a `Gov-Policy:` trailer on the merge, which
push-main's `--prepare` cannot write (it commits a fixed message, `tools/push-main.sh:880-881`), and
the landing wedges, the failure `TOOL-dDeclaredLoop-44` exists to prevent. This unit takes the report's
fix. It repairs `TOOL-dDeclaredLoop-44`.

## 2. Scope (IN)

- **S1** — The merge grade is by key, never by path list. For a merge whose policy file's blob differs
  from every parent's (the `--cc --name-only` list, kept only as the cheap pre-filter), the arm parses
  the file at the merge, at each parent and at the clean re-merge of the parents, and owes a trailer for
  exactly the keys whose value at the merge equals neither any parent's value nor the clean re-merge's
  value. This supersedes `TOOL-dDeclaredLoop-44` S2's "the list holds the file" condition and its §4
  Evidence bullet on `--cc`. Observed by AC1, AC2.
- **S2** — The clean re-merge is git's own: `git merge-tree --write-tree <p1> <p2>` and the policy blob
  of the tree it prints. When it exits 1 (a conflict) the conflicted blob does not parse and the
  clean-merge leg is skipped for that merge, so every key that matches no parent is the resolution's own
  and is owed. Observed by AC2, AC3.
- **S3** — Where the clean re-merge cannot be computed — an octopus merge, or a git without
  `merge-tree --write-tree` (it exits 129) — the arm grades against the parents alone and prints
  `policy: <merge> graded against its parents only — <reason>`, never refusing for the missing leg.
  Observed by AC4.
- **S4** — The fixture case `push-merge-both-sides-clean` joins `guard.py --fixture`: both sides edit
  different keys and the merge is clean. Observed by AC1.

## 3. Non-goals (OUT)

- The non-merge rule and the all-zero base: `TOOL-dDeclaredLoop-44` S1 and S3, the latter's first-push
  case the audit's id 61, batched into `TOOL-dDeclaredLoop-67`.
- push-main writing trailers onto its merge: the lander's message is fixed by design, and with S1 a
  clean landing merge owes none.
- A checklist entry that every git plumbing claim carries a scratch probe, the finding's left-shift:
  the class is recorded at the close; S4 is this rule's clean-merge fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-44` — the push-range merge rule in `check_push_range` of `tools/loop/guard.py`, whose merge grade this unit restates by key
- **hands-off** `TOOL-dDeclaredLoop-67` — the merge key grade, which that unit's first-push walk applies to each merge it finds (the round-2 spec audit's id 61)

## 4. Design

### Evidence

- Probed 2026-10-24 on node `d`, git 2.54.0.windows.1: a scratch repository where `side` changed line 1
  of a ten-line `p.toml` and `main` changed line 10, merged with `--no-ff`, printed the merge sha and
  `p.toml` for `git diff-tree --cc -r --name-only HEAD`, and only the sha for `git diff-tree --cc -r
  HEAD`. `git merge-tree --write-tree HEAD^1 HEAD^2` printed a tree whose `p.toml` blob equalled the
  merge's: PINNED, that date.
- `--prepare` merges with `git merge --no-ff` and a fixed `msg=` (`tools/push-main.sh:880-881`).

### The grade

```
for merge M in the range, with parents P1..Pn:
    skip unless blob(M) differs from every blob(Pi)          # the --cc name-only pre-filter
    C = blob of merge-tree --write-tree P1 P2, when n == 2, it exits 0 and parses; else none
    owed = { k : val(M,k) != val(Pi,k) for every i, and (C is none or val(M,k) != val(C,k)) }
    owed non-empty and no Gov-Policy trailer naming each key -> refuse naming M and the keys
```

An absent key reads as its own value, so a key the resolution deletes is graded like one it sets.

### Files touched (estimate)

- `tools/loop/guard.py`

### Alternatives rejected

- **Hunks of the `--cc` patch.** git's combined diff hides a hunk where the result matches one parent
  line by line, which is right for most edits, but a multi-line value changed in two places by the two
  sides is a hunk with no resolution edit; the key read with the clean re-merge has no such case.
- **Keys against the parents alone.** The same two-sided multi-line value equals neither parent after a
  clean merge and would be owed; S3 keeps it only as the fallback.

## 5. Production-readiness checklist

- security — the resolution edit still owes its trailer, so `floor.record-changes` is not bypassed.
- perf / scale — one `merge-tree` per merge that touched the file, a handful per landing.
- error / empty / loading states — a policy file that does not parse at the merge is a refusal naming
  the merge, as an unparsable file at a non-merge commit is in `TOOL-dDeclaredLoop-44`.
- observability — S3's line names each merge graded without the clean leg.
- risks — `merge-tree --write-tree` re-computes the merge base itself; a criss-cross history picks a
  virtual base, which is the same answer `git merge` gave the lander.
- testing — AC1 to AC4 as fixture plants; the arm under §7, observed at the close.
- migration — none.
- user docs — none beyond `help/policy.md`, `TOOL-dDeclaredLoop-2` S13's.

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant push-merge-both-sides-clean` runs a range whose
  merge took one side's change to key `a` and the other's to key `j` with no resolution edit, it exits 0.
  Red when: the path list is the grade, so the clean merge owes a trailer and the arm exits 1.
- **AC2** — When `--plant push-merge-resolution-edit` runs a merge whose result sets a key to a value
  neither parent nor the clean re-merge holds, with no `Gov-Policy:` trailer, it exits 1 naming the
  merge and that key.
  Red when: the key comparison takes the clean re-merge's conflicted blob as a value.
- **AC3** — When `--plant push-merge-conflict-pick` resolves a conflicting key by taking one side's
  value, it exits 0.
  Red when: a conflicted re-merge makes every key owed.
- **AC4** — When `--plant push-merge-octopus` grades a three-parent merge that changed no key beyond its
  parents, it exits 0 and prints `graded against its parents only`.
  Red when: the missing clean leg refuses the merge.

## 7. Gates

`measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 AC4 · the four merge plants, staged against the path-list grade `TOOL-dDeclaredLoop-44` S2 specified · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 17 (HIGH, item H2).

## 10. Reuse audit

The seams are git's own merge, `git merge-tree --write-tree`, and the policy reader
`TOOL-dDeclaredLoop-2` gives `tools/loop/guard.py`; no merge is re-implemented here. `python
tools/codebase-map/reuse_lookup.py "grade a merge commit by what a clean re-merge would produce"` ranked
`merge` (`tools/memory-tree/merge-rows.py`, `tools/settings-merge.py`), `build_commit` and
`pass_commit`; the two `merge` functions merge row files and settings, neither grades a commit, so no
existing seam fits beyond git's.

Recall terms used: policy merge diff-tree cc clean auto-merge merge-tree write-tree Gov-Policy resolution key push-main prepare
