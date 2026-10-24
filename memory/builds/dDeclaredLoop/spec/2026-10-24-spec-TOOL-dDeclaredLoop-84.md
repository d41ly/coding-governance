# TOOL-dDeclaredLoop-84 — the specs that restate the clean re-merge's non-zero exits read 81's exit table: 78's states and 82's S27 restatement

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 21 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-84-deviation-841.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-84-deviation-841.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-83-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit.md`)
confirmed finding **id 7 at HIGH**, in its item **H1**. Item H1 also holds id 1, which is its own unit,
`TOOL-dDeclaredLoop-83`. The medium grade of the same defect is item M1, id 18, batched into
`TOOL-dDeclaredLoop-86`.

Id 7's reading: no unit removes the parents-alone fallback for a failed re-merge. 83 removes it from
75 S27. Two more live specs restate the retired rule. `TOOL-dDeclaredLoop-78` S1 makes C `uncomputable`
on "a re-merge that does not exit 0", its §4 grade says "or it exits != 0", and its S2 says "Only
`uncomputable` takes 69 S2's parent branch". `TOOL-dDeclaredLoop-82` S4 restates only S27's exit-1 body,
and 82 AC4 greps only for `its blob parses`, so 82's pass at order 41 can rewrite S27 and bring the
fallback back with nothing to catch it.

This unit restates 78 to 81's exit table and makes 82's S4 and AC4 keep the table. It builds immediately
after 81 and repairs `TOOL-dDeclaredLoop-81`, whose hands-off edges reached 75 and 82 but left 78's
definitions and 82's criterion standing.

## 2. Scope (IN)

- **S1** — 78 S1's `uncomputable` is restated, as a rev bump of 78 with its §9 line: an octopus merge, or
  a git that 81 S1's probe found without `merge-tree --write-tree`. A re-merge exiting 1 is 69 S2's
  conflicted case as 75 S27 widens it. Every other exit is 81 S2's `failed`. `present` and `absent` keep
  exit 0. Observed by AC1, AC2.
- **S2** — 78 S2's last sentence is restated in the same rev bump: `uncomputable`, and an exit 1 whose
  conflicted paths hold the policy path, take 69 S2's parent branch; `failed` never does, as 81 S3
  grades it. Observed by AC1, AC2.
- **S3** — 78 §4's grade block is restated in the same rev bump: its `uncomputable` line drops
  "or it exits != 0" and a `failed` line points at 81 S3. Observed by AC1.
- **S4** — 82 S4 says, as a rev bump of 82 with its §9 line, that its restatement of S27's exit-1 body
  keeps S27's exit table as `TOOL-dDeclaredLoop-83` writes it: every exit other than 0 and 1 is 81's
  `failed`, never a fall to the parents. 82 AC4 gains a second grep in the same rev bump:
  `grep -c "any other exit code grades against the parents alone"` over the 75 spec prints 0.
  Observed by AC3.

## 3. Non-goals (OUT)

- 75 S27's own text: id 1, `TOOL-dDeclaredLoop-83`.
- 59 S3's exit-129 sentence and 81 §4 Evidence's quotation of S27: ids 15 and 18, scope items of
  `TOOL-dDeclaredLoop-86`.
- 78 S3's parse refusal at a parent read by the `failed` or conflicted branch: id 3, a scope item of
  `TOOL-dDeclaredLoop-86`.
- The probe's answers, `supported`, `unsupported` and `probe failed`: id 24, `TOOL-dDeclaredLoop-85`.
  S1 says "a git 81 S1's probe found without the feature" and names no answer, so this unit reads
  nothing 85 writes.
- Any change to `tools/loop/guard.py`: 81 builds the table.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-81` — the exit table of S2 and S3, which S1 to S3 write into 78's states and S4 into 82
- **consumes-from** `TOOL-dDeclaredLoop-78` — S1's three states, S2's parent-branch sentence and §4's grade block, built at order 19, which this unit restates to 81's table
- **hands-off** `TOOL-dDeclaredLoop-82` — S4 and AC4, amended to keep S27's exit table and to grep 75 for the retired fallback, which that unit builds at order 41
- **hands-off** `TOOL-dDeclaredLoop-88` — the restatement of 78's grade, whose dispatch that unit completes, and Files touched (the round-7 spec audit's ids 2, 20, 27)

## 4. Design

### Evidence

Read 2026-10-24 at the worktree tip.

- 78 S1: "`uncomputable`: an octopus merge, a git without `merge-tree --write-tree`, or a re-merge that
  does not exit 0"; 78 S2: "Only `uncomputable` takes 69 S2's parent branch"; 78 §4: "C = uncomputable
  if n != 2, or merge-tree --write-tree is missing, or it exits != 0"
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md`, §2, §4).
- 81 S2 makes exit 1 the conflicted case and every other non-zero outcome `failed`, and 81 S3 grades
  `failed` without the exemption (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-81.md`, §2).
- 82 S4 restates "its blob parses" and 82 AC4 greps only that phrase over the 75 spec
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md`, §2 S4, §6 AC4).
- 78 is order 19, 81 order 20, 83 and this unit order 21, 75 order 39 and 82 order 41, read from each
  status header.

### 78's grade after this unit

```
C = uncomputable    if n != 2, or 81 S1's probe found no merge-tree --write-tree     # never run
    absent | present(blob)   if it exits 0                                            # 78 S1
    conflicted               if it exits 1                                            # 69 S2, widened by 75 S27
    failed(rc, line)         otherwise                                                # 81 S2, graded by 81 S3
```

### Files touched (estimate)

- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md`

### Alternatives rejected

- **A §9 note on 78 only, as H1's fix words it.** A note beside an unchanged S1 leaves the definition
  reading "does not exit 0", which is the sentence a reader cites; the definition itself moves.
- **Amending 82 S4 to rewrite S27 whole.** S27 is 83's to restate; 82 keeps its exit-1 body edit and
  gains the check that it kept the rest.

## 5. Production-readiness checklist

- security — closes the two remaining spec routes by which a failed re-merge regains the parent
  exemption.
- perf / scale — N/A — spec text only.
- error / empty / loading states — N/A — no new state; 78 points at 81's `failed`.
- observability — N/A — no printed line changes.
- risks — 78 is built at order 19, before this unit; its code is 81's by order 20, so the restatement
  brings the text to the code and moves no verdict.
- testing — AC1 to AC3 as greps over the 78 and 82 specs.
- migration — none: every reader is unbuilt.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `grep -c "does not exit 0\|exits != 0\|Only .uncomputable. takes"` runs over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-78.md`, it prints 0.
  Red when: any of 78's three restatements still routes every non-zero exit to `uncomputable`.
- **AC2** — When `awk '/^- \*\*S1\*\*/,/^- \*\*S3\*\*/'` over the 78 spec is piped to `grep -c "failed"`,
  it prints at least 2, and piped to `grep -c "TOOL-dDeclaredLoop-81\|81 S"` it prints at least 1.
  Red when: S1 and S2 name no `failed` state or no source for it.
- **AC3** — When `awk '/^- \*\*AC4\*\*/,/^- \*\*AC5\*\*/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-82.md` is piped to
  `grep -c "any other exit code grades against the parents alone"`, it prints 1, and the S4 range
  `awk '/^- \*\*S4\*\*/,/^- \*\*S5\*\*/'` piped to `grep -c "never a fall to the parents"` prints at least 1.
  Red when: 82's pass can restate S27 with nothing checking that the fallback stays gone.

## 7. Gates

`recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass writes two specs and no code, so no loop leg is tripped.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which half of H1's fix is id 7's?** As `TOOL-dDeclaredLoop-83` §8 F2 records: id 1 takes 75 S27,
  and id 7 takes the other live restatements of the retired rule, 78 and 82, the ones its grounding lens
  named. RESOLVED (agent, 2026-10-24, delegated): 78 S1, S2 and §4, and 82 S4 and AC4.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-6 spec audit's id 7 (HIGH, item H1, shared
  with id 1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-88, written by the round-7 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are 78's and 82's own scope items, amended in place as rev bumps that point at 81's table and
copy none of it. The class is `memory/gotchas/amendment-leaves-its-other-half-standing.md`.
`python tools/codebase-map/reuse_lookup.py "amend a sibling spec scope item so a retired rule has no stale reader"`
ranked `read`, `read_text`, `scope` and `read_spec_revisions` (`tools/memory-tree/design_lib.py`), none
an editor or checker of sibling specs, so no existing seam fits beyond the specs themselves. The recall
query returned the gotcha above and the round-6 report's H1.

Recall terms used: amendment other half standing sibling spec stale clause rev bump grep-0 criterion retired rule
