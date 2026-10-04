# TOOL-aWindowedPass-1 — check 23 counts only a pass whose window overlapped a sibling pass's

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-2 · base 886b089d · streams tooling · order 3 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aWindowedPass-1-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aWindowedPass-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aWindowedPass-1-0-run-mandate.md](../prompts/2026-10-04-prompt-TOOL-aWindowedPass-1-0-run-mandate.md) | journal | — |
| [2026-10-04-prompt-TOOL-aWindowedPass-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aWindowedPass-1-2-build-brief.md) | journal | — |
| [2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md](../reviews/2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-aWindowedPass-2 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 TOOL-aWindowedPass-5 |
| [2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round2.md](../reviews/2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round2.md) | diff-review | TOOL-aWindowedPass-2 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 TOOL-aWindowedPass-5 |

<!-- /gen:spec-records -->

## 1. Goal

A pass's declared write set is the disjointness proof for passes that run AT THE SAME TIME. Check 23
grades every dispatched pass, though 8 of this repo's 397 dispatch groups ever held two. A write
outside the declaration of a pass that ran alone collides with nothing. This unit makes check 23
derive, per run, which passes overlapped another, count only their undeclared writes, and report
the rest without counting them.

## 2. Scope (IN)

- **S1** — A pass's WINDOW runs from its dispatch anchor to its pass commit, else to its unit's next
  anchor, else to HEAD. Two passes of different units OVERLAP when either one's anchor lies inside the other's window:
  at or after its anchor, and not yet reached by its pass commit. Derived inside check 23 from the
  dispatch rows and the pass commits it already computes, positions taken from one topological walk
  of the run's range. Observed by AC1 and AC2.
- **S2** — An undeclared write of a pass that overlapped is counted as today. One of a pass that did
  not is printed as `check 23 SOLO <unit> at <sha> wrote <paths> in <run> — outside its declaration…`,
  the same per-instance text a counted write carries, and is not counted. Observed by AC1, AC2 and AC3.
- **S3** — The check prints, per run, how many passes it graded and how many overlapped, so a run
  where everything was solo says so rather than reading as clean coverage. Observed by AC3.

## 3. Non-goals (OUT)

- Passes in different runs are not compared: a run's declarations are its own disjointness proof.
- Two passes of the same unit at different anchors are one worker's sequence, never an overlap.

### Edges

- **consumes-from** `TOOL-aWindowedPass-2` — the pass commit each window ends at.
- **hands-off** `TOOL-aWindowedPass-5` — what a counted write costs is that unit's.

## 4. Design

The row loop keeps computing `dshit` and the undeclared set as now, but defers the count: each row's
`(anchor, end, unit, undeclared paths)` is stored, and after the run's rows are read the overlap
test runs once over them. Positions come from `git rev-list --topo-order --reverse <base>..HEAD`
read once per run, filtered to the anchors and ends the rows name; an anchor equal to the run's base
sits at position 0. `end` is the pass commit's position, else the unit's next anchor's, else
infinity. Windows are recorded for every row that resolves, graded or not: a pass that never
committed was still running beside whatever was dispatched after it. A run whose base does not
resolve cannot be placed, and every graded pass in it is counted, a single-unit run included — the
verdict before this unit, announced on the report channel.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- **Trusting a `solo` flag `--dispatch` writes.** The run writes its own row; the check would be
  reading the subject's sentence about itself (`inputs-inside-the-subjects-reach`).
- **Pairwise `merge-base --is-ancestor`.** About 3,600 spawns for a 61-group run at 751 ms each on
  node a; one walk and a position map answer the same question.

## 5. Production-readiness checklist

- security — N/A: a read-only gate.
- perf / scale — one `rev-list` per run; the pairwise test is in-memory.
- error / empty / loading states — an anchor outside the walk (an unreachable row) keeps the existing
  skip and is not compared.
- observability — SOLO lines and the per-run overlap count.
- risks — a merge in the run's range makes topological order a total order on a partial one; an
  anchor on a merged side branch is placed by the walk, which can only widen a window.
- testing — fixtures for solo, overlapping and sequential-after-commit passes.
- migration — none; landed and derived-LANDED records are excluded as before.
- user docs — the gate header's exception TWO admits the `SOLO` line and the per-run count. The
  protocol's only check-23 text is the ceiling row, which `TOOL-aWindowedPass-5` retires.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` grades a fixture run whose one pass wrote
  outside its declaration, the output carries `check 23 SOLO` and the pass is not counted.
  Red when: the overlap test is bypassed, so the solo pass is counted.
- **AC2** — When a second pass was dispatched before the first committed, and the first wrote outside
  its declaration, `check-unattended.sh` counts the write.
  Red when: overlap is tested by anchor equality alone, missing a later dispatch inside the window.
- **AC3** — When the second pass was dispatched after the first committed, the first's stray write is
  `SOLO`, and the per-run line prints `0 overlapped`.
  Red when: the window ignores the pass commit and runs to HEAD.

## 7. Gates

`unattended kit gate`

New arm: tools/unattended/check-unattended.test.sh · solo, overlapping and sequential fixtures · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the owner's part (1) and check 23 at base.
- rev-2 · 2026-10-04 · build pass · S1 · §4 · §5 · a window ends at the unit's next anchor when no
  pass commit names it, which is the bound check 23 already grades by; an unresolvable base keeps the
  old verdict, single-unit runs included, so a record nobody can place is never silently relaxed; the
  docs line names the header, since the protocol row is unit 5's. The SOLO line reuses the counted
  write's per-instance text, so one string names a stray write however it is graded; every suite arm
  that asserts a COUNT now dispatches an overlapping sibling first.
- rev-3 · 2026-10-04 · closing review r1 · S1 · §6 · H1 · M7 · every negative check-23 arm now dispatches beside a bound
  sibling, and a self-scan arm reds one that dispatches unbound, since the solo rule had made eight
  of them unable to fail; the unresolvable-base fallback has an arm of its own.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether two dispatched passes overlapped in time"`
ranked name-stem neighbours only and printed `unscanned layers: .sh`. Extended: check 23's row loop,
`pass_commit` and `next_anchor` in `tools/unattended/lib-unattended.sh`, and `check_pass_open` in the
driver, whose "open until its commit overlaps its declaration" rule the window's end restates.

Recall terms used: check 23 undeclared write ceiling dispatch declaration disjointness concurrent pass generated index shrink-only ratchet

The question passed with them: "why does check 23 count undeclared writes against a shrink-only ceiling and how was the dispatch declaration meant to prove disjointness".
