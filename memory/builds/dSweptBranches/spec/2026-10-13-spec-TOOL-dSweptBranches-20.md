# TOOL-dSweptBranches-20 — gov's range readers audited for a merge read as additions

**Status:** CLOSED · rev-1 · 2026-10-13 · node d · Tier-1 · base 2b852f5f · streams tooling · order 18 · closes TOOL-dSweptBranches-6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-20-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-20-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-build-TOOL-dSweptBranches-20-1-range-reader-audit.md](../build/2026-10-13-build-TOOL-dSweptBranches-20-1-range-reader-audit.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md) | research | TOOL-dSweptBranches-19 TOOL-dSweptBranches-21 |
| [2026-10-13-prompt-TOOL-dSweptBranches-20-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-20-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

inCMS's memory-local check 21 reads a merge of the default branch into a feature branch as adding
every `memory/` file the default branch gained. This unit names every gov site that lists added
files over a range, groups them by the git invocation shape that decides the answer, and observes
each shape over a fixture that merges the default branch into a feature branch.

## 2. Scope (IN)

- **S1** — An audit record under `memory/builds/dSweptBranches/build/` listing each gov site
  outside test suites that reads added files, or per-commit diffs, over a range: its path and line,
  its invocation, its shape and its verdict. Observed by AC1.
- **S2** — A probe, recorded verbatim beside its results in the same record, that builds the
  fixture and runs each shape over it: a feature branch that merges the default branch after the
  default branch added a `memory/` file. Observed by AC2.
- **S3** — A gotcha class for the blind spot, anchored on the range readers the audit names, so the
  checklist selects it for a future edit of one. Observed by AC3.

## 3. Non-goals (OUT)

- No edit of a gov check unless the probe shows one reads the merged-in file as added; a fix would
  then be a unit of its own.
- No edit of inCMS.

### Edges

none

## 4. Design

The answer depends only on the invocation's shape: `git log` without `-m` gives a merge no diff;
`diff-tree` on a merge prints nothing without `-m`, `-c` or `--cc`; a three-dot diff starts at the
merge base, which the merge moves; `-m` diffs a merge against each parent. So one fixture, with each
shape run over it, decides every site that shares it.

### Files touched (estimate)

- `memory/builds/dSweptBranches/build/2026-10-13-build-TOOL-dSweptBranches-20-1-range-reader-audit.md`
- `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- A probe per site: the sites share five shapes, and a site's own surroundings decide nothing about
  whether a merge's files appear.

## 5. Production-readiness checklist

- security — N/A: a read-only audit.
- perf / scale — N/A.
- error / empty / loading states — a site the grep cannot classify is listed as such.
- observability — the record carries its probe and its output.
- risks — a site whose shape is built at run time is missed by a grep; the record says so.
- testing — the probe, recorded with its results.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -E "diff-filter=[A-Z]*A|--name-status|diff-tree"` runs over gov's
  non-test sources, every hit is a row of the audit record.
  Red when: a hit has no row.
- **AC2** — When the recorded probe runs, each shape the record names prints whether the merged-in
  `memory/` file appears, and a shape that sees it is named with its sites.
  Red when: the fixture's merge does not bring the file in, which the probe asserts first.
- **AC3** — When `python tools/memory-tree/gotchas.py --for-paths tools/runlog/model.py` runs, its
  checklist names `a-merge-of-the-default-branch-read-as-additions`.
  Red when: the class names no anchor path.

## 7. Gates

`memory hygiene` · `gotchas selftest` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, at the owner's instruction to build the asks.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for a range-reader audit, so no existing seam
fits. The gotcha form is `memory/gotchas/`'s, and the anchors are the sites the audit finds.

Recall terms used: "does a gov check read a merge of the default branch as adding files" --terms
"merge diff-filter added files range first-parent check 21 memory-local blind spot feature branch"
