# TOOL-dDeclaredLoop-44 — the policy push arm grades a merge on its combined diff, and a new branch against the remote default tip

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 16 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-44-deviation-441.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-44-deviation-441.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 50 at HIGH**, its item **H16**, alone in that item. `TOOL-dDeclaredLoop-2` S6
grades "every commit in the range whose diff changes `.governance/policy.toml`" and never defines a
merge's diff, nor the all-zero base of a new branch. The lander's `--prepare` merges the run branch onto
the advertised tip with `git merge --no-ff` (`tools/push-main.sh:881`), and a reconcile by hand,
which `--prepare` tells the operator to do on a conflict (:885-886), can edit the policy file inside the
merge. Diffed against its first parent, a prepared merge carrying another build's trailered change is
refused, wedging the landing; with merges skipped, a resolution edit passes with no trailer and bypasses
`floor.record-changes`. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-2`.

## 2. Scope (IN)

- **S1** — The range is every commit `git rev-list <base>..<tip>` names, merges included.
  A non-merge commit is graded on its diff against its one parent, as `TOOL-dDeclaredLoop-2` S6 says.
  Observed by AC1.
- **S2** — A merge commit is graded on its combined diff, `git diff-tree --cc -r --name-only <merge>`,
  which lists a path only when the merge's result differs from every parent: a change no parent carries,
  the resolution's own edit. Where that list holds `.governance/policy.toml`, the merge must carry a
  `Gov-Policy:` trailer naming each key whose value differs from its first parent's, and is refused
  naming the merge and the key otherwise. A change one parent's commit brought is graded on that commit,
  never on the merge. Observed by AC1, AC2.
- **S3** — An all-zero old sha, a new ref, takes as its base the remote default branch's tracking tip,
  resolved by the remote ladder `resolve_remote.py` carries (the `remote_ladder_py` block), and refuses
  naming the ref when no tracking tip resolves, never grading an unbounded history. Observed by AC3.
- **S4** — The fixture cases `push-merge-carries-trailered` and `push-merge-resolution-edit` join
  `guard.py --fixture`, and `push-new-branch` with an all-zero old sha. Observed by AC1, AC2, AC3.

## 3. Non-goals (OUT)

- The trailer's grammar, its reader and the change record: `TOOL-dDeclaredLoop-2` and `-23`.
- A shared fixture pair for every push-range check in the repository, the finding's left-shift: S4's
  cases are this arm's; the class is recorded at the close.
- Policy changes on a branch other than the default: the arm runs from `.githooks/pre-push` on the
  pushes that hook grades, unchanged.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-2` — `check_push_range` in `tools/loop/guard.py` and its `--push-range` call from `.githooks/pre-push`, whose range rule this unit completes
- **hands-off** `TOOL-dDeclaredLoop-59` — the merge grade, which that unit restates by key against the parents and the clean re-merge (the round-2 spec audit's id 17)
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 44 and 61: this pass keeps the loop guard fixtures leg green, and the first push to an empty remote is a scope item of that unit

## 4. Design

### Evidence

- `--prepare` merges with `git merge --no-ff "$oldb"` onto the advertised tip and aborts on a conflict,
  telling the operator to reconcile on the branch by `git merge`, resolve and commit
  (`tools/push-main.sh:876-886`); that hand merge is where a resolution can edit the policy file.
- `git diff-tree --cc` prints only paths whose merge result differs from all parents, git's own
  definition of a combined diff, so a change taken whole from one side is not listed.
- The remote ladder is canonical at `tools/lib/resolve_remote.py` and carried inline under the
  `remote_ladder_py` parity row (`tools/lib/resolve-python.test.sh:182`).

### The rule

| Commit | Diff graded | Trailer owed |
|---|---|---|
| non-merge changing the file | against its parent | on that commit |
| merge whose combined diff lists the file | the resolution's own edit | on the merge, keys against its first parent |
| merge whose combined diff omits the file | none | none: each parent's commit carries its own |
| new ref (all-zero old sha) | `<remote default tip>..<tip>` | per the rows above |

### Files touched (estimate)

- `tools/loop/guard.py`

### Alternatives rejected

- **Diffing a merge against its first parent.** It refuses a prepared merge for a change another build's
  trailered commit brought, which is the wedge.
- **Skipping merges, as `git log` does by default.** A resolution edit then lands untrailered.

## 5. Production-readiness checklist

- security — closes a bypass of `floor.record-changes` through a merge resolution.
- perf / scale — one `diff-tree --cc` per merge in the range, a handful per landing.
- error / empty / loading states — a new ref with no tracking tip refuses by name; an empty range grades
  nothing and says so.
- observability — a refusal names the merge, the key and that the edit is the resolution's own.
- risks — an octopus merge is graded by the same combined diff, git's rule for any parent count.
- testing — AC1 to AC3 as fixture cases; the arm under §7, observed at the close.
- migration — none.
- user docs — none beyond `help/policy.md`, which `TOOL-dDeclaredLoop-2` S13 owns.

## 6. Acceptance criteria

- **AC1** — When `python guard.py --fixture --plant push-merge-carries-trailered` runs a
  range whose merge takes a side carrying a trailered policy change, it exits 0.
  Red when: the merge is diffed against its first parent and refused for lacking a trailer.
- **AC2** — When `--plant push-merge-resolution-edit` runs a merge whose resolution sets a policy key
  neither parent set, with no `Gov-Policy:` trailer, it exits 1 naming the merge and the key.
  Red when: merges are skipped, so the resolution's edit passes.
- **AC3** — When `--plant push-new-branch` passes an all-zero old sha, the arm grades only the commits
  past the fixture remote's default tip, and with no tracking ref it exits 2 naming the ref.
  Red when: the all-zero base walks the whole history, grading every commit ever made.

## 7. Gates

`measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/guard.py · covers AC1 AC2 AC3 · the three push cases, staged against the first-parent diff the base arm would take · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 50 (HIGH, item H16).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-59 and TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are git's combined diff and the `remote_ladder_py` block (`tools/lib/resolve_remote.py`), which
names the remote default tip for every probe that asks which ref landed. `python
tools/codebase-map/reuse_lookup.py "commits in a push range whose diff changes a path including merges"`
ranked `merge`, `changed`, `build_commit` and `check_lease_only_diff`; none grades a merge by its combined
diff, so the rule is this arm's own.

Recall terms used: push range merge combined diff diff-tree cc resolution Gov-Policy all-zero base remote ladder
