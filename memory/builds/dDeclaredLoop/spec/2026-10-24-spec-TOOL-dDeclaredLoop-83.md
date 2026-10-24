# TOOL-dDeclaredLoop-83 — 75 S27 states 81's exit table, so no merge-tree exit but 0 and 1 falls to the parents

**Status:** OPEN · rev-3 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 21 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-83-deviation-831.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-83-deviation-831.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md`)
confirmed finding **id 1 at HIGH**, in its item **H1**. Item H1 also holds id 7, which is its own unit,
`TOOL-dDeclaredLoop-84`. The medium grade of the same defect is item M1, id 18, batched into
`TOOL-dDeclaredLoop-86`.

`TOOL-dDeclaredLoop-81` S2 makes every re-merge exit other than 0 and 1 its `failed` state, refused
untrailered and never a fall to the parents. `TOOL-dDeclaredLoop-75` S27 still ends "any other exit code
grades against the parents alone with 59 S3's printed line" (75 §2 S27). 75's own consumes-from edge to
81 in its §3 states the narrowing, so 75's scope body and its edge give opposite answers. 75 builds at
order 39, after 81 at order 20, and a builder who follows S27 puts exit 128 back on the parent exemption:
the untrailered unrelated-history fail-open 81 closes.

This unit rewrites S27's fallback clause to 81's exit table, and makes 75's own AC27 observe the table at
75's pass. It builds immediately after 81 and repairs `TOOL-dDeclaredLoop-81`, whose hands-off to 75
left S27's fallback standing.

## 2. Scope (IN)

- **S1** — 75 S27's last clause is replaced, as a rev bump of 75 with its §9 line. The new clause: a
  merge-tree exit other than 0 and 1 is 81 S2's `failed` state, graded by 81 S3 and refused untrailered,
  never a fall to the parents. Only 81's `uncomputable` C, an octopus merge or a probed absence of the
  feature, grades against the parents with 59 S3's printed line. S27's exit-1 body, "its blob parses"
  included, is left as written, because `TOOL-dDeclaredLoop-82` S4 restates that body by that phrase.
  Observed by AC1, AC2.
- **S2** — 75 AC27 gains a second observation in the same rev bump: at 75's pass,
  `--plant push-merge-tree-fatal` of `guard.py --fixture` (81 S5) still exits 1 printing
  `the clean re-merge failed: 128`. 75's New arm line for `tools/loop/guard.py` names the plant beside
  `push-merge-conflict-elsewhere`. Observed by AC3.

## 3. Non-goals (OUT)

- 78's three states and 82's restatement of S27's exit-1 body, which restate the same retired rule
  elsewhere: id 7, `TOOL-dDeclaredLoop-84`.
- 59 S3's exit-129 sentence and 81 §4 Evidence's quotation of S27: ids 15 and 18, scope items of
  `TOOL-dDeclaredLoop-86`.
- Any change to `tools/loop/guard.py`: 81 builds the exit table, and S2 only makes 75's pass re-observe it.
- The report's left-shift, a spec-lint check that a spec retiring a rule by quoting a sibling sentence
  bumps that sibling: the class is `memory/gotchas/amendment-leaves-its-other-half-standing.md`, already
  recorded, and AC1 is this instance's grep.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-81` — the exit table of S2 and S3, every exit other than 0 and 1 the `failed` state, which S1 writes into 75 S27
- **hands-off** `TOOL-dDeclaredLoop-75` — S27's fallback clause restated to 81's exit table and AC27 re-observing `push-merge-tree-fatal`, which that unit builds at order 39
- **hands-off** `TOOL-dDeclaredLoop-88` — S1's parent rows, §4's S27 table, its Evidence pins and Files touched, which that unit completes, re-anchors and widens (the round-7 spec audit's ids 1, 15, 27)
- **hands-off** `TOOL-dDeclaredLoop-90` — S1, which that unit reads for the policy path, and §3's state count, which it restates to five (the round-8 spec audit's ids 5, 26)

## 4. Design

### Evidence

Read 2026-10-24 at the worktree tip.

- 75 §2 S27 reads: "The clean re-merge C is taken from `git merge-tree --write-tree`'s first output line
  on exit 0 or exit 1, and used when the policy path is not among the conflicted paths and its blob
  parses; any other exit code grades against the parents alone with 59 S3's printed line"
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`, lines 151-153).
- 75 §3's consumes-from edge to 81 reads "every other exit is the failed state, refused untrailered and
  never a fall to the parents" (same file, line 213).
- 75 AC27 runs only `push-merge-conflict-elsewhere` (same file, lines 389-392), and its New arm line
  names only that plant (line 430).
- 81 S2 and its §4 grade map `rc` other than 0 and 1 to `failed`, and 81 S5 defines
  `push-merge-tree-fatal` with `run_merge_tree` answering 128
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md`, §2, §4).
- 82 S4 replaces S27's "its blob parses" with present, absent or refused, and 82 AC4 greps that phrase
  to 0 over 75 (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md`, §2 S4, §6
  AC4). S1 keeps the phrase so 82's edit still has its target.

### S27 after this unit

```
exit 0 or 1, policy path not conflicted, its blob parses -> C from the first output line   (82 S4 restates this body)
exit other than 0 and 1                                 -> 81 S2 `failed`, graded by 81 S3, refused untrailered
octopus merge, or a probed absence of the feature       -> 81 `uncomputable`: parents, 59 S3's printed line
```

### Files touched (estimate)

- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`

### Alternatives rejected

- **Leaving S27 alone and relying on 81's plants.** The plants catch a literal rebuild only after the code
  is written, and the text keeps contradicting the code for the next change: the finding's consequence.
- **Rewriting S27 whole, the exit-1 body included.** That is 82 S4's edit, by the phrase it greps; doing it
  here moves 82's target and makes two units own one sentence.
- **Moving 75 to an order before 81.** 75 S27 widens 81's states, so 75 depends on 81; the order is right
  and the text is wrong.

## 5. Production-readiness checklist

- security — closes the text route by which exit 128 regains the parent exemption at 75's pass.
- perf / scale — N/A — a spec text change and one more plant run at 75's pass, seconds.
- error / empty / loading states — N/A — no new state; S27 points at 81's `failed`.
- observability — S2 makes 75's pass print `the clean re-merge failed: 128` from 81's plant.
- risks — 82 S4 edits the same scope item at order 41; S1 keeps 82's phrase, and AC2 checks it.
- testing — AC1 to AC3 as greps over the 75 spec; 81's plant is observed at 75's pass by 75 AC27.
- migration — none: 75 is unbuilt.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `grep -c "any other exit code grades against the parents alone"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-75.md`, it prints 0.
  Red when: S27 still sends exits other than 0 and 1 to the parents.
- **AC2** — When `awk '/^- \*\*S27\*\*/,/^- \*\*S28\*\*/'` over the 75 spec is piped to
  `grep -c "never a fall to the parents"`, it prints at least 1, and at this pass the same range piped to
  `grep -c "its blob parses"` prints 1.
  Red when: S27 names no `failed` route, or the rewrite removed the phrase 82 S4 replaces.
  fixture: the second half holds at this pass only; 82 S4 removes the phrase at order 41, by design.
- **AC3** — When `awk '/^- \*\*AC27\*\*/,/^- \*\*AC28\*\*/'` over the 75 spec is piped to
  `grep -c "push-merge-tree-fatal"`, it prints at least 1, and `grep -c "^New arm: tools/loop/guard.py.*push-merge-tree-fatal"`
  over the same file prints 1.
  Red when: 75's pass is never asked to re-observe exit 128 after it widens exit 1.

## 7. Gates

`recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass writes one spec and no code. 75's own pass keeps the sibling-minted `loop guard fixtures` leg
(`TOOL-dDeclaredLoop-2`) green, which runs `guard.py --fixture`; the leg is outside the base manifest.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which half of H1's fix is id 1's, and which is id 7's?** Both ids are one defect, and each takes
  a unit. (a) id 1 rewrites 75 S27, the sentence its coherence lens found contradicting 75's own edge;
  id 7 restates the other specs that carry the retired rule, 78 and 82. (b) one unit does both, the other
  only a criterion. (b) leaves one unit with no mechanism. (a) gives two disjoint write sets at one order.
  RESOLVED (agent, 2026-10-24, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-6 spec audit's id 1 (HIGH, item H1, shared
  with id 7).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-90, written by the round-8 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 75 S27 itself, amended in place as a rev bump; no new spec text duplicates 81's table, which
S1 points at. The class is `memory/gotchas/amendment-leaves-its-other-half-standing.md`, whose fixture is
a grep-0 criterion over the sibling, which AC1 is.
`python tools/codebase-map/reuse_lookup.py "amend a sibling spec scope item so a retired rule has no stale reader"`
ranked `read`, `read_text`, `scope` and `read_spec_revisions` (`tools/memory-tree/design_lib.py`), none of
which edits or checks a sibling spec, so no existing seam fits beyond the spec itself. The memory-recall
query returned the gotcha above and `TOOL-dTieredTribunal-24`, an open ask for mechanical arms for the
class, which this unit does not build.

Recall terms used: amendment other half standing sibling spec stale clause rev bump grep-0 criterion retired rule
