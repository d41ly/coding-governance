# TOOL-dWitnessedBar-4 — the runner-written verdict per tree, the pre-push hook reading it, and the tree Test verifies

**Status:** CLOSED · rev-5 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 17 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0342@a3fc832c whole
**Carries:** node:item.test.merge
**Carries:** node:item.test.verdict
**Carries:** node:item.test.exit
**Carries:** node:record-kind.verdict
**Carries:** node:policy-key.verdict.tree

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-4-deviation-41.md](../build/2026-10-25-build-TOOL-dWitnessedBar-4-deviation-41.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-4-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-4-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-4-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-4-1-builder-return.md) | journal | — |
| [2026-11-20-build-TOOL-dWitnessedBar-4-deviation-42.md](../build/2026-11-20-build-TOOL-dWitnessedBar-4-deviation-42.md) | deviation | — |
| [2026-11-20-build-TOOL-dWitnessedBar-4-red-fix-74.md](../build/2026-11-20-build-TOOL-dWitnessedBar-4-red-fix-74.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-4-red-fix-75.md](../build/2026-11-20-build-TOOL-dWitnessedBar-4-red-fix-75.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-4-red-fix-76.md](../build/2026-11-20-build-TOOL-dWitnessedBar-4-red-fix-76.md) | red-fix | — |
| [2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md](../build/2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-55 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-4-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-4-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-4-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-4-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-4-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-4-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The per-tree green the push boundary adopts is written by whoever ran a bar: the pre-push hook
(`write_bar_green`, `.githooks/pre-push@176f5913:2488`), the unattended driver's close
(`tools/unattended/unattended.sh#write_bar_green`) and the post-merge verifier
(`tools/run-gates/post-merge.sh#write_bar_green`), three copies of one grammar, none of them the runner that
judged the legs. The runner writes only a per-run record and a per-sha stamp (gap-test-02, gap-test-05;
flow-steps' `hook-actor-kind` amend: `test.verdict` is the runner, whose record the hook reads). This
unit makes the runner write one verdict per tree hash, has the hook read it in place of the three
writers, gives the Test step's merge its policy `verdict.tree`, and records the verified tree at
`test.exit`.

## 2. Scope (IN)

- **S1** — The run record names its tree. The runner's `$RUNDIR/verdict` block
  (`tools/run-gates/run-gates.sh@4e410b10:5733-5758`) gains `tree`, the tree hash of `HEAD` when the run started
  clean, `-` otherwise (I8). Observed by AC1.
- **S2** — The per-tree verdict. At the end of every run whose tree was clean at its start and did not
  move, the runner writes `<common-dir>/gate-verdict/<tree hash>` for a full run and
  `<common-dir>/gate-verdict/<tree hash>.scoped` for a scoped one, GREEN or RED, through
  `derive_temp_path` and a rename, in the grammar of §4 "The record" (I8, `record-kind.verdict`).
  Observed by AC1, AC2 and AC3.
- **S3** — The hook reads it. `.githooks/pre-push`'s bar-record candidates
  (`.githooks/pre-push@176f5913:1598-1617`), `check_bar_record`, `check_bar_base` and the bar branch
  of the cover pass's `check_cover_record` (`.githooks/pre-push@176f5913:2190-2235`) read the pushed
  tree's `gate-verdict/<tree hash>` and `.scoped` file through `read_bar_file`, adopting one only when
  it reads `verdict GREEN` and passes the predicates the runner's own stamp passes in
  `check_green_record` (`.githooks/pre-push@176f5913:1653`) and, for its reuse pair,
  `check_green_reuse` (`.githooks/pre-push@176f5913:1749`). Observed by AC4 and AC5.
- **S4** — The three hand-written per-tree records leave. The hook's `write_bar_green` and its call
  (`.githooks/pre-push@176f5913:2611-2629`), the driver's copy and the post-merge verifier's copy are
  deleted; each of those bars runs the runner, which now writes the record. The call's declines go
  with it: the floor's advisory red (TOOL-dDeclaredLoop-2 S14, landed since the base) is a bar whose
  runner record reads RED, which the hook never adopts; the declared STUB runs no runner; the
  doc-only and inherited-base declines are unit 40's, on the runner's write rule. Observed by AC6.
  **Readers:** by name: `.githooks/pre-push`, `.githooks/pre-push.test.sh`,
  `.githooks/pre-push.runlog.test.sh`, `tools/unattended/unattended.sh`,
  `tools/unattended/unattended.test.sh`, `tools/run-gates/post-merge.sh`,
  `tools/run-gates/run-gates.evidence.test.sh` and `tools/run-gates/README.md`, every tracked file
  outside the memory tree that spells `write_bar_green` or `gate-bar-green`, by a git grep at the base,
  re-derived at HEAD d6fb6ef4 on 2026-11-20 as the same files, by the same git grep
  · by value: `check_bar_record`, `check_bar_base` and `check_cover_record` in `.githooks/pre-push`,
  which compare a record's `sha`, `tree`, `kind`, `base` and `bar`, re-pointed by S3; `tools/unattended/unattended.sh`'s gates-green
  check, which reads the record it wrote.
- **S5** — `verdict.tree`. `tools/push-main.sh --prepare`, the actor of `test.merge`, reads
  `verdict.tree` through `policy.py get` (TOOL-dGroundRules-2), its kit found by
  `resolve_lander_kit policy policy.py` (`tools/push-main.sh#resolve_lander_kit`, every lander stage's
  one kit resolution), the catalogue default `prepared-merge` where either cannot run
  (TOOL-dGroundRules-3): under `prepared-merge` it merges the run's branch onto the advertised tip as
  today (`tools/push-main.sh#cmd_prepare`); under `build-tip` it makes no merge and pins the branch tip.
  Either way it prints one witness line naming the value, the SHA and its tree hash. `--land`
  (`tools/push-main.sh#cmd_land`) pushes only a prepared merge (`check_prepared_merge`) and re-prepares
  through `cmd_prepare` on a race, so under `build-tip` it makes the landing merge itself, through the
  merge path `--prepare` takes under `prepared-merge`, when HEAD carries none, and its race path takes
  that merge path too (F4). Observed by AC7.
- **S6** — `test.exit`'s verified tree. `TRANSITION_FIELDS` (TOOL-dDeclaredLoop-3,
  `tools/loop/loop_transition.py#TRANSITION_FIELDS`) gains `tree`, a field `record` takes as
  `--field tree=<hash>`, and the move `write_transition` records at `item.test.exit` (outcome
  `recorded`, `testing -> deploying` in `tools/loop/loop.toml`) refuses unless its `tree` names a full
  `gate-verdict/<tree hash>` reading `verdict GREEN` for the tree `verdict.tree` selects. Observed by
  AC8.
- **S7** — The key's catalogue row. `verdict.tree`'s row of `tools/policy/catalogue.toml`
  (TOOL-dGroundRules-1 S3) gets its `summary` and `usage`, drained from
  `tools/policy/unsummarised-keys.txt` by `policy.py lists --write`; no row is added. The rendered
  `help/reference/policy.md`, which lists a row lacking either field under its unsummarised heading,
  is re-rendered by `python tools/playbook/render_playbook.py --reference`, giving the key a section of
  its own. Observed by AC9.
- **S8** — The kit page. `tools/run-gates/README.md` states the verdict record kind, its two files, the
  keys this unit writes and the rule that keys are additive. NOT OBSERVED — prose, read by the closing
  review.

## 3. Non-goals (OUT)

- `run_id` and `cause` in the verdict and the kept output tail: unit 25's. `held.<n>` is unit 5's and
  `warn.<k>` unit 29's; each joins this record as an additive key.
- The per-sha `gate-full-green` stamp and its readers: unchanged; it certifies one SHA under stricter
  preconditions and the push boundary's predicate 9 reads it.
- Which reds block, and how a red routes: units 3 and 8.
- The remote and peer-node backends that carry the same tree key: unit 6's.
- The lease record `test.exit` writes onto once dPlacedRequest lands the lease kind; until then the
  transition record carries the tree, as flow-steps.md:365 says.
- The `[[item]]` rows for `item.test.merge`, `item.test.verdict` and `item.test.exit`: TOOL-dDeclaredLoop-12
  transcribed them into `tools/loop/loop.toml` since this spec's base, their actors
  `command:test.merge`, `command:test.verdict` and `command:test.exit` naming the commands this unit
  makes real; this unit edits none of them.
- The unattended kit's own self-test suites: waived for this build's landing (README rule), so their
  arms over the deleted writer are amended citing that rule, not observed here.

### Edges

- **hands-off** `TOOL-dWitnessedBar-25` — `gate-verdict`, the per-tree verdict file and the run record's verdict block, into which unit 25 writes `run_id`, `cause` and `tail.<n>`
- **hands-off** `TOOL-dWitnessedBar-3` — `gate-verdict`, the runner-written per-tree verdict whose RED the landing decision reads beside the run's attribution
- **hands-off** `TOOL-dWitnessedBar-6` — `gate-verdict`, the per-tree verdict `local-hook`'s reader reads and the peer and remote backends key by the same tree
- **hands-off** `TOOL-dWitnessedBar-2` — `gate-verdict`, the per-tree verdict a bypass record reads to tell a killed hook after a green bar from a push no bar judged
- **consumes-from** external — dGroundRules' catalogue row and reader for `verdict.tree` (TOOL-dGroundRules-1, -2, -3); dDeclaredLoop's `TRANSITION_FIELDS` and transition writer (TOOL-dDeclaredLoop-3)
- **hands-off** `TOOL-dWitnessedBar-40` — the per-tree record's write rule and `check_bar_record`, into which unit 40 carries the docs-mode and inherited-base declines and the `reused` pair (round-1 spec audit id 18)
- **hands-off** `TOOL-dWitnessedBar-41` — the per-tree record and the hook's adoption of it, which unit 41 gives the `selection` keys and their re-derivation at R (id 59)
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 13 and 48: `run_id` written once on the per-tree record, and the per-tree directory's retention across worktrees, each a scope item of that unit
- **hands-off** `TOOL-dWitnessedBar-56` — the per-tree record and unit 4's AC4 adopt plant, which the verdict-boundary minors batch amends with the keys units 40 and 41 make required (id 3)

## 4. Design

### The record

`record-kind.verdict` is two files of one grammar, `<key>TAB<value>` lines, keys in runlog's grammar
(`tools/runlog/README.md:22`: an all-digit suffix is an index), written by the runner alone and read
by key, so a key added later is additive and changes no reader:

| File | Written | Keys this unit writes |
|---|---|---|
| `<git-dir>/gate-run/<run id>/verdict` | every run, last, as today | today's keys plus `tree` |
| `<common-dir>/gate-verdict/<tree hash>` and `.scoped` | every run that started clean and did not move | `tree`, `sha`, `verdict`, `kind` (`full` or `scoped`), `base`, `manifest`, `manifest_blob`, `fingerprint`, `selftests`, `run_id`, `stamped`, `by` (`runner`) |

`kind` is `full` when `GATE_FULL=1` ignored every guard and `scoped` otherwise, `base` the resolved
`BASE` a scoped run diffed against (`tools/run-gates/run-gates.sh@4e410b10:557-569`). The common dir is
resolved once, as the `.shared` stamp resolves it (`RG_COMMON_RAW`, asked at
`tools/run-gates/run-gates.sh@4e410b10:118-122` and read at
`tools/run-gates/run-gates.sh@4e410b10:5824-5839`), so every worktree of a clone
reads one directory, and a full record never overwrites a scoped one or the reverse: two slots per
tree, the two-slot rule the hook adopted (TOOL-aFrugalTurnstile-11 S1). The last run of a tree in a
slot wins, GREEN or RED, because the record is what the latest bar said about that tree.

### What the hook adopts

Today the hook's candidates are six files in two slot families, each written by a bar and checked for
the hook's own bar command (`bar`, `bar_paths`). The runner's record names the manifest it ran instead
of a command, so the hook adopts it as it adopts the runner's stamp: same manifest path and blob as
the bar it would run, no cache reuse, `selftests` covering what this push needs. A wrapper bar that is
not the runner finds no record for its own command and runs: that costs a saving, never a verdict,
which is the rule the deleted writers stated for every decline.

### `verdict.tree` and the two items

| Item | Actor | Under `prepared-merge` | Under `build-tip` |
|---|---|---|---|
| `item.test.merge` | `push-main.sh --prepare` | merges the branch onto the advertised tip | pins the tip, no merge |
| `item.test.verdict` | `run-gates.sh`, on that tree | writes `gate-verdict/<tree>` for the merge's tree | for the tip's tree |
| `item.test.exit` | the transition writer at `testing -> deploying` | `tree` = the merge's tree, refused without its GREEN | `tree` = the tip's tree |

The witness line is `push-main: test.merge <value> <sha8> tree <tree hash>`. Under `build-tip`,
`--land` makes the landing merge when HEAD carries none (F4) and the hook still gates the pushed tree;
the value decides which tree Test verifies, never whether the boundary runs.

### Inventory

Minted: the run-record key `tree`; the files `gate-verdict/<tree hash>` and `.scoped` with the keys
above; the `TRANSITION_FIELDS` member `tree`; the witness line. Deleted: three functions named
`write_bar_green` and the `gate-bar-green` slot files. Naming cells: each is asked of `python
tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

A clone's existing `gate-bar-green*` files are left on disk and read by nothing; the first runner run
of a tree writes its record, so the first push after landing may run a bar it would have adopted.

### Rollout

Live at landing; the hook, the driver and the post-merge verifier change in one commit with the runner.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/post-merge.sh`
- `tools/run-gates/README.md`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/loop/loop_transition.py`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `help/reference/policy.md`

### Alternatives rejected

- **Keep the hook's writer and add the runner's beside it**: two writers of one fact, the defect this
  clause names.
- **Fold `gate-full-green` into the per-tree record**: a wider change than the clause, its readers
  spread over push-main and the driver, and its preconditions stricter than a per-tree verdict's.

## 5. Production-readiness checklist

- security — the files live in the git common dir, outside the tree, written by rename as the stamps
  are; a hand-planted record passes only the predicates the runner's stamp already passes.
- perf / scale — one small file per tree and slot; a lookup is one path, where the hook read six.
- error / empty / loading states — a run that started dirty or moved writes no per-tree record and
  says so on one line; a missing record means the hook runs the bar.
- observability — the runner prints the path it wrote; `--prepare` prints the witness line.
- risks — the first push after landing may re-run a bar (§4 Migration).
- testing — fixtures on scratch clones; the suite arms in §7 are observed RED then GREEN by the main
  loop at the close.
- migration — none to run; stale files are ignored.
- user docs — `tools/run-gates/README.md` (S8) and `help/reference/policy.md`, re-rendered with
  `verdict.tree`'s section (S7). `help/policy.md`'s floor row says a red read as advisory writes no
  green record, which stays true: the runner's record of that bar reads RED.

## 6. Acceptance criteria

- **AC1** — When the runner makes a full run, every guard ignored, over a fixture manifest
  (`GATE_LEGS=<fixture>`, the runner's manifest knob at `tools/run-gates/run-gates.sh@4e410b10:415`)
  holding one passing leg in a clean scratch clone,
  `<common-dir>/gate-verdict/<tree>` exists for `git rev-parse HEAD^{tree}` and reads `verdict GREEN`,
  `kind full`, `by runner`, and the run's `verdict` file holds the same `tree`.
  Red when: the record is written under the git dir of a linked worktree, or keyed by the SHA.
- **AC2** — When the same fixture's leg fails, the per-tree record reads `verdict RED`; when the run
  starts with an untracked file planted, no per-tree record is written and the run prints why.
  Red when: a dirty start writes a record for a tree nobody tested.
- **AC3** — When a scoped run, guards honoured, follows a full GREEN of the same tree, the
  `<common-dir>/gate-verdict/<tree>.scoped` file holds the scoped record and the full file still
  reads `kind full`.
  Red when: the scoped run overwrites the full record its base depends on.
- **AC4** — When `.githooks/pre-push` runs over a scratch clone whose pushed tree carries a full GREEN
  per-tree record from the same manifest, it adopts it and runs no bar, printing the record's path.
  Red when: the hook ignores the runner's record and runs the bar.
- **AC5** — When the record for that tree reads `verdict RED`, or names another manifest, or carries a
  non-zero `reused_cache`, the hook runs the bar.
  Red when: any of the three is adopted.
- **AC6** — When `git grep -c 'write_bar_green' -- .githooks tools` runs on the built tree, it prints
  nothing.
  Red when: a writer of the hand-written record survives beside the runner's.
- **AC7** — When `bash push-main.sh --prepare --slug x` runs on a scratch run branch under
  `verdict.tree = "build-tip"`, `HEAD` is unchanged and the witness line names `build-tip`, the tip and
  its tree; under `prepared-merge` it names the merge it made. When `--land` then runs on that pinned
  branch under `build-tip` over the suite's fixture remote, the remote's default branch holds a merge
  whose first parent is the advertised tip and whose second is the pinned tip.
  Red when: `build-tip` still merges at `--prepare`, so Test verifies a tree the value excluded, or
  `--land` refuses the pinned tip for want of a prepared merge.
- **AC8** — When the transition writer is asked for `testing -> deploying` at `item.test.exit`
  (`loop_transition.py record --from testing --item item.test.exit --outcome recorded`) with a
  `--field tree=<hash>` whose full per-tree record is missing or RED, it exits 1 naming the tree; with
  a GREEN record it writes the transition carrying `tree=<hash>`.
  Red when: the exit records a tree no GREEN verdict covers.
- **AC9** — When `python policy.py get verdict.tree` runs on the built tree, it prints `prepared-merge`,
  and `grep -cx 'verdict.tree' unsummarised-keys.txt` under `tools/policy/` prints 0, and
  `grep -c '^## .verdict\.tree.$' help/reference/policy.md` prints 1.
  Red when: the row keeps an empty `summary` or `usage`, or the reference page still lists the key as
  unsummarised.

## 7. Gates

`measure-legs selftest` · `pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `push-main self-test` · `run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `memory hygiene` · `scratch-guard self-test` · `routed-commits selftest` · `tier2-review self-test` · `policy fixtures` · `policy check` · `loop transition record` · `help reference pages`

The guards join's broad `.githooks/`, `tools/` and `tools/run-gates/` guards are excluded by the
checker's floor; the bar at the close runs them all. The unattended kit's suites are waived for this
build's landing (README rule). `policy check`, `loop transition record` and `help reference pages`,
none in the manifest at this spec's base, carry no guard and run on every bar: they read S7's row,
S6's field and S7's render.

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 · a dirty start and a scoped-after-full pair staged on a scratch clone · none
New arm: .githooks/pre-push.test.sh · covers AC4 AC5 · a per-tree record planted RED, then from another manifest, then GREEN · none
New arm: tools/push-main.test.sh · covers AC7 · `verdict.tree` planted as `build-tip` on a scratch run branch, then `--land` over the suite's fixture remote · none

## 8. Open questions

- **F1 — Does the runner write a per-tree record for a RED run?** Options: (a) every run that started
  clean and did not move, GREEN or RED; (b) GREEN only, as the deleted writers did. (b) leaves unit 3's
  landing decision, which reads the RED of the same run, with nothing per tree, and flow-steps.md:358
  names "the runner-written verdict per tree hash, each red classed". RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 1, flow-steps.md:358. widens: none · relaxes: none
- **F2 — Do the driver's and the post-merge verifier's copies leave with the hook's?** Options: (a) all
  three, since each of those bars runs the runner, which now writes the record; (b) the hook's only,
  the clause's words. (b) leaves two writers of a record nothing reads once the hook reads the
  runner's, which the charter's `[yagni]` deletes rather than disables. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Does `build-tip` stop `--prepare` merging?** Options: (a) yes, `--prepare` pins the tip and
  `--land` merges; (b) `--prepare` always merges and `build-tip` only changes which tree the exit
  records. (b) runs Test's bar on a tree the value excludes. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 1, flow-steps.md:356, "Under `build-tip`, it pins the build's tip". widens: none ·
  relaxes: none
- **F4 — Under `build-tip`, what makes the landing merge?** `--land` pushes only a merge
  `check_prepared_merge` finds on HEAD's first-parent line and re-prepares through `cmd_prepare` on a
  race (`tools/push-main.sh#cmd_land`), so a tip F3 pinned is refused, and §4's rule that the landing
  still merges had no actor. flow-steps.md:437 has `deploy.land` push "HEAD of the prepared merge" and
  names no actor under `build-tip`. Options: (a) `--land`, under `build-tip` and with no prepared
  merge on HEAD, takes `--prepare`'s merge path before its push, and its race path takes that path
  too; (b) a new `--prepare` flag making the landing merge after Test, a public surface (M3 veto 2);
  (c) `--prepare` under `build-tip` also writes the merge to a side ref `--land` pushes, a new write
  surface (M3 veto 3). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3, the one survivor of the
  vetoes, and it keeps AC7 and §4's rule. widens: none, since `--land` already merges on its race
  path · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 4, the brief's I8, scout A's row for
  cl-0342, flow-steps.md:356-365 and the `hook-actor-kind` amend, and the three writers at `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-40, TOOL-dWitnessedBar-41, TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, promoted by the round-1 spec audit of units 40 to 51; nothing else
  moved.
- rev-4 · 2026-11-19 · §7 · the leg line gains `scratch-guard self-test`, `routed-commits selftest`,
  `tier2-review self-test` and `policy fixtures`, whose manifest guards hold the §4 paths
  `tools/unattended/unattended.sh` and `tools/policy/catalogue.toml`, per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief; nothing else moved.
- rev-5 · 2026-11-20 · §1 · S3 S4 S5 S6 S7 · §3 · §4 · §5 · AC1 AC7 AC8 AC9 · §7 · §8 F4 · §10 ·
  re-grounded at `d6fb6ef4` per brief 2026-11-19-prompt-TOOL-dWitnessedBar-4-reground-brief: moved
  hook and runner lines blob-pinned, the rest cited as `path#symbol`; S3 names the cover pass and
  `check_green_reuse`; S4 names the floor's advisory-red decline the call gained; S5 reads through
  `resolve_lander_kit` and F4 gives `--land` the landing merge under `build-tip`; S7 re-renders
  `help/reference/policy.md`; AC1's manifest is `GATE_LEGS`; Files touched gains that page and
  `tools/unattended/unattended.test.sh`; the leg line gains `policy check`, `loop transition record`
  and `help reference pages`, landed since the base.

## 10. Reuse audit

The seams extended are the runner's `$RUNDIR/verdict` block and its `.shared` common-dir placement
(`tools/run-gates/run-gates.sh@4e410b10:5733-5839`), the hook's `read_bar_file` and runner-stamp
predicates (`.githooks/pre-push@176f5913:1618-1653`), `tools/push-main.sh#cmd_prepare` with its kit
resolution `tools/push-main.sh#resolve_lander_kit`, and dDeclaredLoop's
`tools/loop/loop_transition.py#TRANSITION_FIELDS`. The lookup below, re-run at `d6fb6ef4`, ranks the
same generic stems. `python tools/codebase-map/reuse_lookup.py "record the bar's verdict for a tree
hash so the push boundary can adopt it"` ranked generic stems (`tree` in a selftest, `records` in
`tools/memory-tree/gotchas.py`, runlog's `write_record`) and named none of the three writers, which
`git grep -c 'write_bar_green'` found. The recall probe returned TOOL-aFrugalTurnstile-2's brief, the
design origin of the hook's writer, scout A's row and the sibling specs of units 2, 3 and 6 that read
`gate-verdict/<tree hash>`; their spelling agrees with this unit's.

Recall terms used: `python tools/memory-recall/query.py "how does the pre-push hook read a runner-written verdict keyed by tree hash" --terms "gate-verdict tree hash runner verdict pre-push write_bar_green gate-bar-green prepared-merge build-tip verdict.tree test.exit"`
