# PLAY-dOrderedCharter-47 — a record written on a branch that never held the positional check is graded print-only, by its adding commit's ancestry

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 10 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-47-deviation-471.md](../build/2026-10-24-build-PLAY-dOrderedCharter-47-deviation-471.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 81 at HIGH**, its item **H8**. `PLAY-dOrderedCharter-26` seeds the file:line list
once from this build's tree (S2), and S3's `shrink-only` reds any reference in the tree that is not on
the list. S4's print-only rule for `memory/builds/` covers only unresolved symbol and pinned forms,
not S3's list check. Sixteen unattended run branches were in flight when the audit ran. Each one that
merges the default branch after unit 26 lands brings in records it wrote before the check existed,
some pinned at its BASE, and the `tags` leg reds on citations the branch cannot edit; the only remedy
offered, `pin`, rewrites them. This is the class `memory/gotchas/a-merged-in-check-can-refuse-a-pinned-record.md`
names. This unit grandfathers by authorship rather than by a tree snapshot: a citation in a build
record whose adding commit does not descend from the commit that brought the check in is printed and
never red. It repairs unit 26 and is built right after it.

## 2. Scope (IN)

- **S1** — The landing commit. `positional.py` derives `L`, the commit that added
  `tools/playbook/positional.py` to this repository (the oldest add, through
  `tree_lib.read_adding_commits`), once per run. With no such commit, the module is staged and not
  yet landed, and every record is graded as S3 grades it today. Observed by AC1.
- **S2** — The descendants. One `git rev-list --ancestry-path L..HEAD`, plus `L` itself, is the set of
  commits that hold the check. A record under `memory/builds/` whose adding commit, read through
  `tree_lib.read_adding_commits` over `memory/builds/**`, is outside that set was written on a branch
  that never held the check. Observed by AC1 and AC2.
- **S3** — The verdict. In such a record, every unlisted file:line reference S3 would red is printed
  as `positional — grandfathered: <path> <ref> (added in <sha8>, before the check)` and leaves the exit
  unchanged; references in every other file keep unit 26 S3's verdict under each `tags.positional`
  value. This extends unit 26 S4's `memory/builds/` print-only rule to S3's list check for exactly the
  records the check could not have reached when they were written. Observed by AC2 and AC3.
- **S4** — The probe, as a plant through unit 19's fixture, `python tools/playbook/gov_tag.py --fixture
  --plant positional-forked-before`: a scratch repository whose branch forks before the commit that
  adds `positional.py`, writes a record under `memory/builds/<slug>/build/` citing `x.py:1`, and is
  merged after that commit; the leg's arm then exits 0 printing the grandfathered line. A second
  record written after the merge and citing `x.py:2` is red. Observed by AC2.

## 3. Non-goals (OUT)

- The reference forms, the list, the `pin` and `shrink` verbs and the other `tags.positional` values:
  unit 26's.
- The directive producers that tell a writer to cite path and line: `PLAY-dOrderedCharter-48`.
- Grandfathering live text outside `memory/builds/`: a file there can be edited to clear a red, which
  is what the check asks.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-26` — `positional.py`, its list check and its plants, whose verdict S3 narrows for records written before the check; without them there is nothing to grandfather

## 4. Design

### Evidence

Read at `ce13efbe`; the seam is unit 26's design. Unit 26 S2 seeds once and refuses a re-seed; S3's
`shrink-only` reds "a reference in the tree and not on the list"; S4's print-only clause sits under
"Resolution of the two stable forms" and names "Unresolved", which a bare file:line citation is not.
`tree_lib.read_adding_commits` (`tools/memory-tree/tree_lib.py:302`) returns `{path: sha}`, the oldest
commit that added each path, from one `git log --diff-filter=A` over one pathspec, and is the kit's
one adding-commit reader (TOOL-dTrueNorth-20 S32). The audit counted 16 branches with
`git branch -a | grep -c unattended` (finding 81's evidence, PINNED 2026-10-23).

### Why ancestry and not a date or a snapshot

A date is wrong on a branch whose clock or rebase moves it. A snapshot of the list at landing, the
current S2, is wrong for every branch forked earlier, which is the finding. Ancestry is the property
itself: a commit that descends from `L` was made in a tree holding the check, and one that does not,
was not. `--ancestry-path` keeps a side branch forked before `L` and merged after it outside the set,
which `L..HEAD` alone would not.

### Inventory

Minted: the line prefix `positional — grandfathered:`, the plant `positional-forked-before`, and the
private derivations of `L` and its descendant set in `positional.py`. Naming cells: `lexicon naming
predicates` grades the Python names.

### Files touched (estimate)

- `tools/playbook/positional.py`
- `tools/playbook/gov_tag.py` (the plant)

### Rollout

Live at landing, order 10, after unit 26 at order 9. `PLAY-dOrderedCharter-48` shares order 10 and
also writes `tools/playbook/positional.py`, and unit 25 shares it and writes `tools/playbook/gov_tag.py`,
so the dispatch sequences the three rather than running them together (M6).

### Alternatives rejected

- **S4's print-only rule for every file under `memory/builds/`**, the review's second fix: a spec or
  record written after the check landed would then never be graded, which `PLAY-dOrderedCharter-48`'s
  finding needs graded.
- **Re-seeding the list at each merge**: a seed is the list's whole definition, and unit 26 S2 refuses
  a second one for that reason.

## 5. Production-readiness checklist

- security: no new surface; the rule reads history and narrows a verdict to print-only for records
  nobody can edit.
- perf / scale: one `git log --diff-filter=A` over `memory/builds/**` and one `git rev-list` per run,
  both DERIVED and timed at the pass against the leg's ceiling.
- error / empty / loading states: no `L` (module not yet committed) grades every record; a failed git
  call is an `OSError` naming it, as `read_adding_commits` raises, and exits 2.
- observability: each grandfathered reference is printed with its adding commit.
- risks: a record deleted and re-added after `L` is graded from its new add, the oldest add kept by
  the reader being the original; stated in the module's docstring.
- testing: AC1 to AC3; S4 is a plant under unit 19's selftest arm.
- migration: none.
- user docs: unit 26's paragraph in `tools/playbook/README.md` gains one sentence on the rule.

## 6. Acceptance criteria

- **AC1** — When a probe calls the derivation over this repository after the unit lands, `L` is the
  commit `git -C tools/playbook log --diff-filter=A --format=%H -- positional.py | tail -1` prints, and
  every spec of this build dated 2026-10-23 is outside the descendant set.
  Red when: `L` is read from a date or a typed sha, or the set includes commits made before `L`.
- **AC2** — When `python gov_tag.py --fixture --plant positional-forked-before` runs,
  the record written before the fork's merge prints `positional — grandfathered:` naming `x.py:1` and
  the arm exits 0; the record written after the merge reds naming `x.py:2`.
  Red when: the pre-fork record reds, or the post-merge record is grandfathered.
- **AC3** — When the same plant moves the pre-fork record to `notes.md` under the fixture's `tools` directory, outside
  `memory/builds/`, the arm reds naming `x.py:1`.
  Red when: grandfathering reaches live text.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC2 AC3 · the playbook-render selftest runs `positional-forked-before`, its failing case staged by grading the pre-fork record under unit 26's base rule · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 26's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What grandfathers a record.** Options: (a) its adding commit's ancestry against the commit
  that added the check; (b) print-only for all of `memory/builds/`; (c) the adding commit's date. (b)
  stops grading every new record, and (c) trusts a clock. RESOLVED (agent, 2026-10-24, delegated):
  (a), rung 3. widens: none · relaxes: unit 26 S3's red, for a build record whose adding commit does
  not descend from the check's landing

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 81 (HIGH, item H8).

## 10. Reuse audit

The seam extended is unit 26's list check in `tools/playbook/positional.py` (its S3), and the history
read reuses `tree_lib.read_adding_commits` (`tools/memory-tree/tree_lib.py:302`), the kit's one
adding-commit reader, rather than a second `git log`. `python tools/codebase-map/reuse_lookup.py
"which commit added a record and whether it descends from a given commit"` ranked `records`
(`tools/memory-tree/gotchas.py`), `build_commit` and `read_records` by name stem and did not rank
`read_adding_commits`, which was found by reading `tree_lib.py`; the probe disagrees with source on
which reader is the seam. The recall query returned the gotcha this class is
filed under and TOOL-dSweptBranches-6, which records that a merge must not read as adding every file
the default branch gained; `read_adding_commits` walks no merge diff, so it holds that property.

Recall terms used: `python tools/memory-recall/query.py "how is a merged-in check kept from refusing a record pinned at base on another branch" --terms "a-merged-in-check-can-refuse-a-pinned-record grandfather adding commit shrink-only frozen record branch"`
