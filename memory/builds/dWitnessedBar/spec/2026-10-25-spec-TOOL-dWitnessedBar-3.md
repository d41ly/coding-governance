# TOOL-dWitnessedBar-3 — attribution deciding what blocks

**Status:** CLOSED · rev-8 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 20 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0341@65d333f3 whole
**Carries:** node:item.test.route
**Carries:** node:record-kind.attribution
**Carries:** node:record-kind.routing
**Carries:** node:policy-key.verdict.blocks
**Carries:** node:policy-key.verdict.red-route

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-a.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-build-TOOL-dWitnessedBar-3-deviation-31.md](../build/2026-10-25-build-TOOL-dWitnessedBar-3-deviation-31.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-26-build-TOOL-dWitnessedBar-3-deviation-32.md](../build/2026-10-26-build-TOOL-dWitnessedBar-3-deviation-32.md) | deviation | — |
| [2026-11-05-build-TOOL-dWitnessedBar-3-deviation-33.md](../build/2026-11-05-build-TOOL-dWitnessedBar-3-deviation-33.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-3-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-3-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-3-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-3-1-builder-return.md) | journal | — |
| [2026-11-20-build-TOOL-dWitnessedBar-3-change-1.md](../build/2026-11-20-build-TOOL-dWitnessedBar-3-change-1.md) | change | — |
| [2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-87.md](../build/2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-87.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-88.md](../build/2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-88.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-89.md](../build/2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-89.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-90.md](../build/2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-90.md) | red-fix | — |
| [2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-91.md](../build/2026-11-20-build-TOOL-dWitnessedBar-3-red-fix-91.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-51 |
| [2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 |
| [2026-10-26-prompt-TOOL-dWitnessedBar-3-1-spec-reviewer.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-3-1-spec-reviewer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dWitnessedBar-3-2-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-3-2-spec-writer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dWitnessedBar-3-1-spec-writer.md](../prompts/2026-11-05-prompt-TOOL-dWitnessedBar-3-1-spec-writer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dWitnessedBar-3-owner-forks.md](../prompts/2026-11-05-prompt-TOOL-dWitnessedBar-3-owner-forks.md) | research | TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-28 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-55 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-3-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-3-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-3-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-3-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-3-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-3-reground-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dWitnessedBar-3-pin-brief.md](../prompts/2026-11-20-prompt-TOOL-dWitnessedBar-3-pin-brief.md) | journal | — |
| [2026-11-20-prompt-TOOL-dWitnessedBar-3-pin-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dWitnessedBar-3-pin-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dWitnessedBar-5-edges-brief.md](../prompts/2026-11-20-prompt-TOOL-dWitnessedBar-5-edges-brief.md) | journal | TOOL-dWitnessedBar-5 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

Turn the bar's report-only attribution into the decision of what blocks. Each red's class (`OWN`,
`INHERITED`, `MIXED`, `CONTENDED`, `DEAD PROBE`) is joined to a block or a pass by `verdict.blocks`,
the pre-push hook and the unattended driver land a red bar only when every red passes, `test.route`
joins every red to one route by its class, and `verdict.red-route` turns the tester's judgment of an
`OWN` or blocking `MIXED` red into a fix pass or a new unit through Design. Today the one blocking
policy is `INHERITED_RED=park|land`, which only knows `INHERITED`; it is retired onto the new key.

## 2. Scope (IN)

- **S1** — The block predicate, `derive_red_blocks <value> <class>` in a new sourced file
  `tools/run-gates/lib-verdict.sh`, printing `block` or `pass` by the table of §4 "### The block
  table" (shared interface I9). An unknown value reads `every-red`, and an empty or unknown class
  blocks. Observed by AC1.
- **S2** — The runner: `GATE_VERDICT_BLOCKS=<value>`, read once and unset as `GATE_INHERITED_RED` is
  today (`tools/run-gates/run-gates.sh@ab6dc6e8:429-431`), replaces it; `run_attribution` sources
  `lib-verdict.sh` and writes the attribution record (`record-kind.attribution`) with a ninth field
  `blocks`, the reason staying last; the `GATE attr` line ends `· blocks` or `· passes`; the summary
  names the value and the blocking count; an absent value is `every-red`, said on the summary. The
  post-merge verifier unsets `GATE_VERDICT_BLOCKS` from its bar's environment as its scrub loop unsets
  `GATE_INHERITED_RED` today (`tools/run-gates/post-merge.sh@ab6dc6e8:40-48`). Observed by AC2.
- **S3** — Self-grading closed: `lib-verdict.sh` joins the KF3 list
  (`tools/run-gates/run-gates.sh@ab6dc6e8:5163`), so a diff against R that edits the table reads every
  red `OWN`. Observed by AC2.
- **S4** — The inherited-green stamp (`tools/run-gates/run-gates.sh@ab6dc6e8:5981-6001`) is written when
  every red row reads `pass` under a handed value, in place of "policy `land` and every red
  `INHERITED`", and records that value as its key `blocks` beside `max_age` (§8 F8); its file name
  `gate-inherited-green` is unchanged. Observed by AC2.
- **S5** — The deciding readers re-pointed from `INHERITED` to the `blocks` field. The hook's
  `read_policy_at` (`.githooks/pre-push#read_policy_at`) reads `verdict.blocks` at R through `policy.py
  get verdict.blocks --rev "$main_remote"`, keeping its read of `INHERITED_RED_MAX_AGE` from the gate
  file at R, and its export block (`.githooks/pre-push@ab6dc6e8:2426-2430`) exports
  `GATE_VERDICT_BLOCKS`. Its `check_inherited_verdict` (`.githooks/pre-push#check_inherited_verdict`)
  reads the run record's `verdict` file, as today, and admits a red bar only when every attribution row
  reads `pass`, attributed against the remote's own sha, one row per failed leg; the landing branch
  after the bar (`.githooks/pre-push@ab6dc6e8:2537-2544`) asks it under every value. The hook's other
  tests of `land` read the value by §8 F8: the doc-only scoping in `classify_docs`
  (`.githooks/pre-push#classify_docs`) and the age export treat every value but `every-red` as they
  treat `land`, and the inherited-green stamp reader (`.githooks/pre-push@ab6dc6e8:1893-1918`) admits a
  stamp only where its `blocks` equals the value read at R. The driver's `read_gate_policy`
  (`tools/unattended/unattended.sh#read_gate_policy`) reads the same value, and `gates-green` hands it
  to its bar as `GATE_VERDICT_BLOCKS` in the bar's environment
  (`tools/unattended/unattended.sh@ab6dc6e8:11989-11991`). `read_gates_record`
  (`tools/unattended/unattended.sh#read_gates_record`) reads field 9: `land` when every row reads
  `pass`, `hold` when every row reads `INHERITED` and one reads `block`, `other` otherwise.
  `write_inherited_asks` (`tools/unattended/unattended.sh#write_inherited_asks`) files its ask for
  every row reading `pass`, its text naming the class. `check_inherited_override` keeps reading the
  class (§8 F7). Observed by AC4.
- **S6** — `test.route`: `python tools/run-gates/verdict_flow.py route --run <run dir>` writes the
  routing record (`record-kind.routing`), `<run dir>/routing`, one row per red joined to one route by
  §4 "### The routes", and prints one `route` line per row; the unattended driver's `gates-green`
  calls it on every red bar it reads. Observed by AC3.
- **S7** — `verdict.red-route`: `python verdict_flow.py judge --run <run dir> --leg <name> --judgment
  <word>` records the tester's judgment on a row routed `attribute`, refusing a word outside the
  `item.test.attribute` row's outcomes (`TOOL-dWitnessedBar-23` S7), and fills its `next` by the
  value: `fix-pass-or-design` sends `code-miss` to `fix-pass` and `spec-wrong` to `new-unit`;
  `always-new-unit` sends both to `new-unit`. Observed by AC5.
- **S8** — `INHERITED_RED` retired, its value carried by an upgrade step: the row
  `govkit/inherited-red-to-verdict-blocks` in `tools/govkit/steps.toml` (TOOL-dSafePassage-1's step
  grammar), whose script maps `park` to `verdict.blocks = "every-red"` and `land` to
  `"own-mixed-contended"` in the target's `.governance/policy.toml` and deletes the line; gov's own
  `.githooks/gate-env.sh` goes through it at landing, and gov's header line documenting the key and its
  policy block's comment go with it, so `policy.py lists --derive legacy-homes` derives no row for the
  key and `policy.py lists --write` drains its row from `memory/project/legacy-homes.txt`. The new step
  id gains its row in `memory/project/landed-steps.txt`, the append-only `landed-steps` population of
  `tools/govkit/registry.toml`. Observed by AC6 and AC7.
  **Readers:** by name: the 16 files AC6's grep lists with -l, DERIVED 2026-11-20 at HEAD ab6dc6e8,
  `.githooks/gate-env.sh`,
  `.githooks/pre-push`, `.githooks/pre-push.test.sh`, `.unattended.conf`, `tools/govkit/govkit.py`
  (`POLICY_KEYS`), `tools/govkit/selftest.py`, `tools/policy/check_policy.py`, `tools/policy/policy.py`,
  `tools/run-gates/post-merge.sh`, `tools/run-gates/run-gates.sh` (as `GATE_INHERITED_RED`),
  `tools/run-gates/run-gates.test.sh`, `tools/unattended/.unattended.conf.example`,
  `tools/unattended/PROTOCOL.template.md`, `tools/unattended/STOPS.template.md`,
  `tools/unattended/unattended.sh` and `tools/unattended/unattended.test.sh`; with them the renders
  `memory/guides/UNATTENDED-STOPS.md` and `memory/guides/UNATTENDED-PROTOCOL.md`, and
  `tools/run-gates/README.md`, which names the policy as `GATE_INHERITED_RED_MAX_AGE` and an exported
  `land`. Two of the 16 joined since the base, `tools/policy/policy.py`'s `GATE_ENV_MARKS` row and
  `tools/policy/check_policy.py`'s legacy fixture, re-pointed by §4 "Migration".
  `memory/DECISIONS.md` names the key in a ruling's prose only, a record outside the population
  · by value: `.githooks/pre-push` `read_policy_at`, `classify_docs`, the inherited-green stamp reader,
  the export block, `check_inherited_verdict` and the landing branch; `tools/unattended/unattended.sh`
  `read_gate_policy`, `read_gates_record`, `write_inherited_asks`, and `gates-green`'s bar environment
  and its MET and hold lines; `tools/run-gates/run-gates.sh` `ATTR_POLICY` and the stamp;
  `tools/govkit/govkit.py`'s check 7h3 predicate built from `POLICY_KEYS`; and
  `tools/policy/policy.py#derive_legacy_homes`, whose gate-file row for the key goes once no line
  assigns, documents or reads it. `tools/unattended/unattended.sh#check_inherited_override` reads the
  class and is unchanged (§8 F7).
- **S9** — The two keys documented: the `verdict.blocks` and `verdict.red-route` rows of
  `tools/policy/catalogue.toml` get their `summary` and `usage`, drained from
  `tools/policy/unsummarised-keys.txt` by `policy.py lists --write`; `help/reference/policy.md` is
  re-rendered by `python tools/playbook/render_playbook.py --reference`, giving each key a section of
  its own, and the mirror `.governance/policy.json` by `policy.py mirror --write` (§8 F10). Observed by
  AC8.

## 3. Non-goals (OUT)

- `INHERITED_RED_MAX_AGE` and the age probe: kept as they are; the age escalates an ask and decides no
  landing.
- The same-tree re-run and the nondeterministic route to `test.flakes`: `TOOL-dWitnessedBar-8` adds
  both to `route` as a row it writes before the class routes.
- The quiet-host re-run of a blocking `CONTENDED` red: `TOOL-dWitnessedBar-30` arms the `quiet-rerun`
  route this unit names.
- Spawning the tester and acting on `next`: the loop's engine runs the item the route names; today's
  stand-ins are the unattended driver's existing fix pass and a new unit added by its `--rescope`.
- An owner exception: PLAY-dOrderedCharter-7 S9's register excuses only a core gate's red whose
  principle and part match an admitted record, read by `core.py exceptions` and by the core gate
  itself, which prints `excepted`; a leg is core when its `enforces` is non-empty (that unit's §4
  Alternatives rejected). No reader of this unit, the hook or the driver reads the register, so the
  `probe-repair` and `fix-unit` routes name an exception as the alternative only for a core-gate leg.
  Under `core.exceptions = owner-only-expiring` no record is admitted until PLAY-dOrderedCharter-15's
  owner-proof check lands (S9 again), and under `none` never.
- The per-tree verdict and its hook reader: `TOOL-dWitnessedBar-4`'s, landed. A red bar's per-tree
  file is never adopted; the landing decision reads the run record's `verdict` file.
- The admission of an override, a hold, a hand-off or an abort over a red the run did not cause:
  `check_inherited_override` keeps reading the class (§8 F7).
- The join between the routing record's route words and the outcomes the `item.test.route` row of
  `tools/loop/loop.toml` declares: §4 "The routes" names it and nothing checks it (§8 F9).

### Edges

- **consumes-from** `TOOL-dWitnessedBar-4` — `gate-verdict`, the verdict record kind the runner writes, whose run-record file `gate-run/<run id>/verdict` the landing decision reads RED beside the attribution record of the same run
- **consumes-from** `TOOL-dWitnessedBar-23` — `gov-tester`, the slot `test.attribute` names, and its closed judgments `code-miss` and `spec-wrong`, which `judge` refuses any other word than
- **hands-off** `TOOL-dWitnessedBar-8` — `verdict.blocks` and the routing record, into which the nondeterministic route to `test.flakes` is written ahead of the class routes
- **hands-off** `TOOL-dWitnessedBar-30` — `verdict.blocks` and the `quiet-rerun` route a blocking `CONTENDED` red takes, which that unit arms
- **hands-off** `TOOL-dWitnessedBar-5` — `tools/run-gates/verdict_flow.py`, the file this unit mints with its `route` and `judge` verbs and its `--fixture` cases, to which unit 5 adds `select`, `select --check` and their fixture cases
- **consumes-from** external — dGroundRules' `policy.py get` (TOOL-dGroundRules-2 S7) and its catalogue rows for `verdict.blocks` and `verdict.red-route`, and TOOL-dSafePassage-1's step rows
- **consumes-from** external — TOOL-dDeclaredLoop-12's `item.test.attribute` row, which `judge` reads through `loop_lib.py items --tag` run as a subprocess, the verb §8 F6's ask adds
- **hands-off** `TOOL-dWitnessedBar-44` — the step script `inherited_red.py`, whose reads and value mapping unit 44 widens to both policy files and every value (id 62)
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 19 and 39: the undeclared path's witness line, and the protocol edit's byte budget, each a scope item of that unit

## 4. Design

### Evidence

- The attribution is report-only (`tools/run-gates/run-gates.sh@ab6dc6e8:20-22`); `run_attribution`
  (`tools/run-gates/run-gates.sh#run_attribution`) writes a nine-field row per red, reason last
  (`tools/run-gates/run-gates.sh@ab6dc6e8:5276-5282`).
- The only blocking policy is `INHERITED_RED=park|land` in `.githooks/gate-env.sh@ab6dc6e8:103-104`,
  parsed at the remote's tip by the hook (`.githooks/pre-push#read_policy_at`) and by the driver
  (`tools/unattended/unattended.sh#read_gate_policy`), an absent key reading `land`, the kit default
  since ruling TOOL-dUnstuckLanding-22. Under `land`, a red bar lands when every red reads
  `INHERITED`; `OWN`, `MIXED`, `CONTENDED` and `DEAD PROBE` block
  (`tools/unattended/unattended.sh#read_gates_record`).
- `own-only`, `own-mixed-contended` and `every-red` are spelled only in the `verdict.blocks` row of
  `tools/policy/catalogue.toml`, and the default `own-only` in the mirror `.governance/policy.json`; no
  code reads either key, and `python tools/policy/policy.py get verdict.blocks` prints `own-only`
  (run at `ab6dc6e8`, 2026-11-20).
- A `DEAD PROBE` is what every red reads when `lib-attribute.sh` is absent
  (`tools/run-gates/run-gates.sh@ab6dc6e8:5152-5153`).
- v2's `[policies]`: `verdict.blocks` values `own-mixed-contended`, `every-red`, `own-only`, default
  `own-only` (v2:1271); `verdict.red-route` values `fix-pass-or-design`, `always-new-unit`, default
  `fix-pass-or-design` (v2:1279). The catalogue rows carry the same values and defaults.
- Since this spec's base, TOOL-dDeclaredLoop-12 declared the `item.test.route` and
  `item.test.attribute` rows of `tools/loop/loop.toml`: the first's outcomes are `nondeterministic`,
  `own`, `contended`, `dead-probe`, `inherited` and `non-blocking`, the second's `code-miss` and
  `spec-wrong`. TOOL-dDeclaredLoop-17 S5 made `--hold --code inherited-red` a caller of
  `check_inherited_override` (`tools/unattended/unattended.sh@ab6dc6e8:7480-7482`).

### The block table

| Class | `own-only` | `own-mixed-contended` | `every-red` |
|---|---|---|---|
| `OWN` | block | block | block |
| `MIXED` | pass | block | block |
| `CONTENDED` | pass | block | block |
| `INHERITED` | pass | pass | block |
| `DEAD PROBE` | block | block | block |
| no row, or an unknown class | block | block | block |

`DEAD PROBE` blocks under every value (§8 F1): it means no comparison was made, so nothing shows the
red is not the run's own. Today's `land` is exactly `own-mixed-contended`, and `park` exactly
`every-red`, which is what the upgrade step of S8 writes.

```bash
# tools/run-gates/lib-verdict.sh — SOURCED, never run; names nothing outside itself
derive_red_blocks() { # value · class -> prints block or pass
  local v=$1 c=$2
  case "$v" in own-only|own-mixed-contended|every-red) ;; *) v=every-red ;; esac
  case "$v:$c" in
    every-red:*) echo block ;;
    *:INHERITED) echo pass ;;
    own-only:MIXED|own-only:CONTENDED) echo pass ;;
    *) echo block ;;
  esac
}
```

### The attribution record

`<run dir>/attribution`, mode 600, one TAB row per red leg, ten fields:
leg · class · inherited · own · R sha · age · owner sha8 · owner id · `blocks` · reason. Field 9 is
inserted before the reason, so every reader that reads fields 1 to 8 positionally
(`.githooks/pre-push#check_inherited_verdict`, `tools/unattended/unattended.sh#read_gates_record`,
`tools/unattended/unattended.sh#write_inherited_asks`,
`tools/unattended/unattended.sh#check_inherited_override`) reads the same bytes it reads today.

The stamp `gate-inherited-green` gains one key, `blocks`, the value it was written under. The hook's
stamp reader compares it with the value it read at R, as it compares `max_age` with the bound it read
there.

### The routes

`verdict_flow.py route` reads `<run dir>/attribution` and `<run dir>/verdict`; a red leg the
attribution does not name is a row of class `-`, which blocks. Its routing record is `<run
dir>/routing`, TAB rows: leg · class · blocks · route · judgment · next, the last two `-` until
`judge` fills them.

| Class | blocks | `route` | `item.test.route` outcome |
|---|---|---|---|
| `OWN`, `MIXED` | block | `attribute`, the tester's `test.attribute` | `own` |
| `CONTENDED` | block | `quiet-rerun` (`TOOL-dWitnessedBar-30`) | `contended` |
| `DEAD PROBE`, `-` | block | `probe-repair`: the probe repaired, or on a core gate an exception record (§3) | `dead-probe` |
| `INHERITED` | block | `fix-unit`: a fix unit through Design, or on a core gate an exception record (§3) | `inherited` |
| any | pass | `ask`, filed by the driver's `write_inherited_asks` | `non-blocking` |

The routes are a closed tuple `ROUTES` in `verdict_flow.py`, and `route` prints one line per row,
`route  <leg>  <class> · <blocks> · <route>`. The last column names the outcome of the
`item.test.route` row of `tools/loop/loop.toml` each route stands for; the record writes the route
word, never the outcome (§8 F9), and the row's sixth outcome, `nondeterministic`, is
`TOOL-dWitnessedBar-8`'s `flakes` route. A kit imports no sibling kit (TOOL-dGroundRules-1 §4;
TOOL-dDeclaredLoop-12 S4), so `judge` reaches both siblings by subprocess, each found through
`resolve_kit_dir`, imported from `leg_factory`, the kit's inline copy under the `resolve_kit_dir`
parity row, as `tools/run-gates/keep_tails.py` imports it: `policy.py get verdict.red-route` for the
value, and for `item.test.attribute`'s outcomes `loop_lib.py items --tag`, the verb §8 F6 asks
dDeclaredLoop for. No verb of `loop_lib.py` prints one item's outcomes: its verbs at `ab6dc6e8` are
`--check`, `--scopes`, `--selftest`, `--fixture --plant` and `--grade-site`
(`tools/loop/loop_lib.py#main`), and `read_outcome_set` (`tools/loop/loop_lib.py#read_outcome_set`)
is a function a sibling may not import. Until that verb lands `judge` exits 2 naming it; a missing
loop kit refuses `judge` with exit 2 naming the kit.

### Policy reads

Each key is a row of `tools/policy/catalogue.toml` (dGroundRules-1 S3) read through `policy.py get
<key> --rev <R>` (dGroundRules-2). The hook finds the policy kit through its own `resolve_kit_dir`
(`.githooks/pre-push#resolve_kit_dir`), vetting a copy under the pushing tree with
`check_reviewed_file`, as its floor reader finds the loop kit's `floor.py`; the driver finds it as
`read_spec_audit_switch` does (`tools/unattended/unattended.sh#read_spec_audit_switch`). Both read at
R, so a branch cannot loosen its own landing. Where no policy kit resolves, each reads the catalogue
default `own-only`, v2's, and says so on its policy line; where `policy.py get` exits non-zero or
prints a value outside the three, the read is `every-red`, said on the same line. Gov's value after S8
is `own-mixed-contended`.

The hook's tests of `land` other than the landing decision (§8 F8): `classify_docs` scopes a doc-only
push under every value but `every-red`, because an `INHERITED` red lands under each of them as it did
under `land`; the age bound is exported under the same values; and a stamp is admitted only where its
`blocks` equals the value at R.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/run-gates/lib-verdict.sh` | file | none declared for files |
| `derive_red_blocks` | shell function | `sh.function`, asked at the pass |
| `tools/run-gates/verdict_flow.py` (verbs `route`, `judge`, `--fixture`) | file | none |
| `ROUTES`, the route words `attribute`, `quiet-rerun`, `probe-repair`, `fix-unit`, `ask`, `fix-pass`, `new-unit` | tuple, words | `py.constant`, asked at the pass |
| `GATE_VERDICT_BLOCKS` | env knob | asked at the pass |
| `blocks`, a key of the stamp `gate-inherited-green` | record key | none |
| `govkit/inherited-red-to-verdict-blocks`, `tools/govkit/steps/inherited_red.py` | step row, script | none |

### Migration

The step of S8, under TOOL-dSafePassage-1's contract (before-image, `up`, `down`, `witness`): `up`
reads `INHERITED_RED` from the target's `.githooks/gate-env.sh`, writes `[verdict] blocks` into
`.governance/policy.toml` (`park` to `every-red`, `land` to `own-mixed-contended`; an absent or blank
key writes nothing, so the catalogue default `own-only` applies), and deletes the assignment line;
`down` restores both files from the before-image; `witness` exits 0 when no assignment remains. The
script loads `tools/govkit/steps/conf_to_policy.py` by its path, as `review_rounds.py` does, and takes
the line out with its `render_conf_rest` and writes the key with its `render_policy_bytes`, through
`upgrade_steps.render_policy_text`, the one writer, as `fanout_cap.py` does; that file's `parse_conf`
reads integers only, so the script parses the `park|land` value itself. Gov's row of the key in
`memory/project/legacy-homes.txt`, the shrink-only `legacy-homes` population (TOOL-dWitnessedBar-20),
is drained by `policy.py lists --write` once gov's gate file and both readers no longer name it.

The policy kit's two spellings of the key go with it (§8 F11). The `INHERITED_RED` row of
`GATE_ENV_MARKS` in `tools/policy/policy.py` is deleted: it marks a key of gov's gate file, which
holds none after the pass, and the legacy list is gov's own and graded in no install
(`help/policy.md`, "the list is gov's own"). The legacy fixture of `tools/policy/check_policy.py`,
whose `LEGACY_GATE` text plants the key and whose `drain-merge` case drains it, plants and drains
`INHERITED_RED_MAX_AGE=10` in its place, a key `GATE_ENV_MARKS` still marks `owner-policy` and the
list still sorts last among the gate file's rows, beside the conf row that case drains with it.

### Rollout

Live at landing. An adopter's next `govkit update` runs the step; until then its hook reads the
catalogue default at R, `own-only`, which v2 chose (walk T1) and the step's `land` mapping replaces.
Gov's own `.governance/policy.toml` is a path `tools/policy/guarded-paths.txt` lists, so its change
lands from a live unattended run's branch or the owner (`tools/policy/guard.py`), and the mirror
`.governance/policy.json` is re-rendered by `policy.py mirror --write` in the commit after it.

### Files touched (estimate)

- `tools/run-gates/lib-verdict.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/verdict_flow.py`
- `tools/run-gates/README.md`
- `tools/run-gates/post-merge.sh`
- `tools/run-gates/run-gates.test.sh`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/gate-env.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/STOPS.template.md` and `tools/unattended/PROTOCOL.template.md`, with their renders
  `memory/guides/UNATTENDED-STOPS.md` and `memory/guides/UNATTENDED-PROTOCOL.md`
- `.unattended.conf`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/steps.toml`
- `tools/govkit/steps/inherited_red.py`
- `.governance/policy.toml`
- `.governance/policy.json`: the mirror, re-rendered by `policy.py mirror --write`
- `tools/policy/policy.py`: the `GATE_ENV_MARKS` row (§8 F11)
- `tools/policy/check_policy.py`: the legacy fixture's planted key (§8 F11)
- `tools/policy/catalogue.toml`: the two rows' `summary` and `usage` (S9)
- `tools/policy/unsummarised-keys.txt`: drained by `policy.py lists --write` (S9)
- `help/reference/policy.md`: re-rendered by `render_playbook.py --reference` (S9)
- `memory/project/legacy-homes.txt`: the key's row drained by `policy.py lists --write`
- `memory/project/landed-steps.txt`: the new step id's row
- `memory/guides/SESSION-KICKOFF.md`: its `watch:` line holds `tools/run-gates/run-gates.sh` and
  `.unattended.conf`, so its `last-audit` is re-stamped

### Alternatives rejected

- **The table inside `lib-attribute.sh`.** That file states it decides no verdict and is shared with
  the self-test runner's baseline; the decision is policy and gets its own file.
- **A byte-identical copy of the table in the hook.** The hook reads the runner's `blocks` field, and
  KF3 already makes an edited grader read every red `OWN`; a second copy is a second fact.
- **Keeping `INHERITED_RED` beside `verdict.blocks`.** Two keys deciding one landing disagree the first
  time an adopter sets both.
- **A step whose up proposes the policy key and writes only the gate file**, the shape of
  `tools/govkit/steps/review_rounds.py` (TOOL-dDeclaredLoop-56 S40). Its up refuses until the owner
  sets the key, while the readers this unit re-points read the key from landing on: an adopter that
  declared `park` reads `own-only` in that window, and an `INHERITED` or `MIXED` red lands where it
  parked. It also fails AC7 as written.

## 5. Production-readiness checklist

- security — deny by default: an unknown value reads `every-red`, an unattributed or `DEAD PROBE` red
  blocks, the policy is read at R and never from the pushed tree, a stamp written under one value is
  refused at a boundary reading another, and `lib-verdict.sh` is graded by KF3 like the classifier.
- perf / scale — one `case` per red leg; `route` reads two run-dir files.
- error / empty / loading states — no attribution record reads every red `-`, which blocks; a refused
  policy read reads `every-red`, said on the hook's line; `judge` on a row not routed `attribute`, or
  with the loop kit or its read verb absent, exits 2 naming which.
- observability — the `GATE attr` line, the summary's blocking count and the routing record.
- risks — v2's default `own-only` lets a `MIXED` red land on an adopter that never set
  `INHERITED_RED`; the step maps a declared `land` to `own-mixed-contended`, gov's value, and the
  `ask` route files every passing red.
- testing — the probes of §6; the suite arms of §7 at the close.
- migration — the step of S8, reversible by its `down`.
- user docs — `help/reference/policy.md` lists both keys and gains a section for each from S9's
  `summary` and `usage`; no other help page names the inherited-red policy, and `help/loop.md`'s
  inherited-red hold stays true under §8 F7. The run-gates README's attribution section and the
  unattended templates are updated in place.

## 6. Acceptance criteria

- **AC1** — When
  `bash -c 'KITDIR=tools/run-gates; . "$KITDIR/lib-verdict.sh"; for v in own-only own-mixed-contended every-red bogus; do for c in OWN MIXED CONTENDED INHERITED "DEAD PROBE" -; do printf "%s " "$(derive_red_blocks "$v" "$c")"; done; echo; done'`
  runs at the root, it prints the four rows of §4's table, the `bogus` row equal to
  `every-red`'s.
  Red when: `MIXED` passes under `own-mixed-contended`, or `DEAD PROBE` passes under any value.
- **AC2** — When the runner's attribution pass runs over the fixture bar of §7's `run-gates canary`
  arm, its record's rows carry ten fields with `blocks` ninth, and an edit of `lib-verdict.sh`
  against R reads every red `OWN` with the KF3 reason; observed by
  `grep -c 'lib-verdict.sh' run-gates.sh` in `tools/run-gates/` printing at least 2 (the source line
  and the KF3 list) at the pass.
  Red when: the KF3 list omits the file, so a branch editing the table grades itself.
- **AC3** — When `python verdict_flow.py --fixture route` runs in `tools/run-gates/`, over a planted
  run dir whose attribution holds one row of each class under `own-only`, it prints `attribute` for
  `OWN`, `ask` for `MIXED`, `CONTENDED` and `INHERITED`, and `probe-repair` for `DEAD PROBE`, and
  the routing record holds one row per red leg the verdict counts.
  Red when: a passing `MIXED` routes to `attribute`, or a red the attribution omits gets no row.
- **AC4** — When
  `bash -c 'eval "$(sed -n "/^check_inherited_verdict()/,/^}/p" .githooks/pre-push)"; main_remote=$1; check_inherited_verdict "$2"; echo "rc $? $PP_NOT"' _ <sha> <run dir>`
  runs over a planted RED run dir whose rows all read `pass`, it prints `rc 0`; with one row reading
  `block` it prints `rc 1` naming that leg.
  Red when: the predicate still tests the class for `INHERITED`, so an all-`pass` `MIXED` bar under
  `own-only` is refused.
  fixture: two run dirs under the scratch path, each a `verdict` and an `attribution` file.
- **AC5** — When `python verdict_flow.py --fixture red-route` runs, under `fix-pass-or-design` it
  prints `code-miss -> fix-pass` and `spec-wrong -> new-unit`, under `always-new-unit` both
  `-> new-unit`, and `judge --judgment maybe` exits 2 naming the outcome set, the fixture's `here`
  holding a stub loop kit that answers `items --tag`; with no loop kit, and with one whose `loop_lib.py`
  lacks the verb, `judge` exits 2 naming the kit or the verb; and
  `git grep -nwE '(import|from) (loop_lib|policy)' -- tools/run-gates` prints nothing.
  Red when: `judge` accepts a word outside `item.test.attribute`'s outcomes, or imports a sibling kit.
- **AC6** — When `git grep -nwE "(GATE_)?INHERITED_RED" -- .githooks tools .unattended.conf` runs
  after the pass, it prints only lines of the step's own row and script, `inherited_red.py`, and the
  run-gates README's migration note; at `ab6dc6e8` it lists 16 files (DERIVED 2026-11-20 by the same
  grep with `-l`).
  Red when: a reader still parses or exports the retired key, or the policy kit still marks or plants
  it.
- **AC7** — When `python inherited_red.py up <target>` runs beside the step row's script, over a
  fixture target whose `.githooks/gate-env.sh` holds `INHERITED_RED=park`, the target's policy file
  `policy.toml` holds `blocks = "every-red"` under `[verdict]` and the line is gone; `down` restores
  both files byte for byte; with `land` it writes `own-mixed-contended`.
  Red when: an absent key writes a value, or `down` leaves a byte changed.
- **AC8** — When `python policy.py get verdict.blocks` runs in `tools/policy/` on the built tree, it
  prints `own-mixed-contended`; `grep -cxE 'verdict\.(blocks|red-route)' unsummarised-keys.txt` there
  prints 0; and `grep -cE '^## .verdict\.(blocks|red-route).$' help/reference/policy.md` at the root
  prints 2.
  Red when: either row keeps an empty `summary` or `usage`, or the reference page still lists a key
  as unsummarised.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `pre-push self-test` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `scratch-guard self-test` · `routed-commits selftest` · `tier2-review self-test` · `policy fixtures` · `policy check` · `build-index selftest` · `gotchas selftest` · `memory-recall kit selftest` · `recall floor` · `kickoff-manifest ratchet` · `ratchet (both ways)` · `step-rows-frozen` · `step-gate`

`build-index selftest`, `gotchas selftest` and `memory-recall kit selftest` guard
`tools/policy/policy.py`; `recall floor` guards `memory/`, which holds the two renders, the two
ledgers and the kickoff manifest this unit re-stamps. `kickoff-manifest ratchet`, `ratchet (both
ways)`, `step-rows-frozen` and `step-gate` carry no guard and grade, on every bar, the stamp, the
`landed-steps` row and the new step row.

New arm: tools/run-gates/run-gates.test.sh · covers AC2 · a fixture bar with one red leg attributed INHERITED under `GATE_VERDICT_BLOCKS` every-red, its row reading `block` and no stamp written, the same bar under own-only writing a stamp whose `blocks` reads own-only, then a staged edit of `lib-verdict.sh` against R reading the red OWN by KF3 · none
New arm: .githooks/pre-push.test.sh · covers AC4 · a planted push whose bar is red on one MIXED leg, refused under own-mixed-contended and admitted under own-only, the value read at R, and a planted inherited-green stamp whose `blocks` differs from the value at R refused · none

The unattended suite's `INHERITED_RED` arms are re-pointed at the pass, and its verdict is waived for
this landing by the README's self-test waiver rule, its clean reading owed with PLAY-dClosedLoop-16.

## 8. Open questions

- **F1 — Does a `DEAD PROBE` red ever pass?** Options: (a) it blocks under every value; (b) it blocks
  under `every-red` only, by the value names; (c) it blocks under `every-red` and
  `own-mixed-contended`. (b) and (c) let every red land under `own-only` the moment
  `lib-attribute.sh` is missing, because every red then reads `DEAD PROBE`: a widened write surface
  (veto 3). RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the only survivor of veto 3; stricter
  than layer-flow's "DEAD PROBE route by `verdict.blocks`", so recorded as deviation 31. widens: none ·
  relaxes: none
- **F2 — Where is the block decided, and does the hook re-decide it?** Options: (a) the runner writes
  `blocks`, the hook reads it, and `lib-verdict.sh` joins KF3; (b) a byte-identical copy in the hook
  under a parity row, recomputed from the class; (c) the hook alone. (b) is a second fact; (c) leaves
  the driver and the routing to re-implement it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3,
  one fact and the existing self-grading guard. widens: none · relaxes: none
- **F3 — What does a declared `INHERITED_RED` become?** Options: (a) a step mapping `land` to
  `own-mixed-contended` and `park` to `every-red`; (b) dropping the key so v2's default applies; (c)
  keeping both keys. (b) silently loosens every repository that declared `land`; (c) is two facts.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the charter's `[core]` "with defaults and an
  upgrade step". widens: none · relaxes: none
- **F4 — How does the hook read the new key?** Options: (a) `policy.py get verdict.blocks --rev
  "$main_remote"`; (b) a `read_policy_key` parse of `.governance/policy.toml` text. (b) parses TOML with
  a `KEY=value` parser, which dGroundRules-2 S8 keeps to `KEY=value` files. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 1, dGroundRules-8's reader shape for a hook. widens: none ·
  relaxes: none
- **F5 — Which hash does the `**Carries:**` line pin?** Deviation `2026-10-25-build-TOOL-dWitnessedBar-3-deviation-31` amends
  cl-dClosedLoop-0341's text, so the as-built view hashes it `65d333f3` where the baseline hashed `0f53eec5`.
  RESOLVED (agent, 2026-10-25, delegated): rung 1, the line pins `cl-dClosedLoop-0341@65d333f3`, the view's hash,
  moved by deviation 31. widens: none · relaxes: none
- **F6 — How does `judge` read `item.test.attribute`'s outcomes, when `loop_lib.py` has no read verb?**
  A kit imports no sibling kit (TOOL-dDeclaredLoop-12 S4), and `read_items` is a function that
  `loop_lib.py` offers only to its own `--check` and `--fixture` (its AC1, AC2). Options: (a) an ask to
  dDeclaredLoop: `loop_lib.py` gains `items --tag <tag>`, printing the row's `outcomes` one per line
  and exiting 2 on an unknown tag, run by `judge` as a subprocess; (b) a declared `requires_if` row on
  `tools/run-gates/kit.toml` naming `loop`, `judge` importing `read_items` in process, which the rule
  admits only as a declaration `govkit selfcheck` grades and that installs nothing, the shape of
  `tools/memory-tree/kit.toml:8`; (c) `judge` parsing `loop.toml` itself, a second reader of one row.
  (a) keeps the call in the shape dDeclaredLoop uses for its own sibling reads (its S4 and §8 F5); its
  cost is a wait, since live `judge` exits 2 until the ask lands. (b) needs no parent change but makes
  run-gates the one in-process consumer of a module its owner runs by subprocess; (c) is a second fact.
  Recommendation (a). RESOLVED (owner, 2026-11-05): (a) an `items --tag` ask to dDeclaredLoop. The
  ask this build run files in `memory/builds/dDeclaredLoop/BACKLOG.md` is "TOOL-dDeclaredLoop-12:
  `loop_lib.py items --tag <tag>` prints the item row's `outcomes`, one per line".
- **F7 — Does `check_inherited_override` read the `blocks` field?** Since the base,
  `--hold --code inherited-red` calls it (TOOL-dDeclaredLoop-17 S5,
  `tools/unattended/unattended.sh@ab6dc6e8:7480-7482`), and that hold is the state in which every red
  is `INHERITED` and blocks. Options: (a) it keeps reading the class, admitting the override, the
  hold, the hand-off and the abort only over an all-`INHERITED` red, whatever `verdict.blocks` says;
  (b) it reads `pass` on every row, as rev-6's S5 had it; (c) the hold reads the class and the other
  three verbs read `pass`. (b) refuses the hold in the one state `gates-green` prints its hold line
  for, every red `INHERITED` and one blocking, since a blocking row never reads `pass`, so the printed
  hold could never be taken. (c) splits one admission into two rules. The four verbs ask whether the
  red is the run's own, a class question, and none of them lands a red. Recommendation (a). RESOLVED
  (agent, 2026-11-20, delegated): (a), by M3, the most feature-rich: (b) loses the hold, and (c)
  carries one more rule for no verb it serves. widens: none · relaxes: none
- **F8 — How do the hook's other tests of `land` read the new value?** `classify_docs` scopes a
  doc-only push only under `land`, the age bound is exported only under `land`, and the
  inherited-green stamp is read only under `land` (`.githooks/pre-push@ab6dc6e8:1893-1918`). Options:
  (a) the first two read every value but `every-red` as `land`, and the stamp records its `blocks`
  value and is admitted only where that equals the value at R; (b) as (a), but a stamp is admitted
  wherever the value at R is not `every-red`; (c) the stamp retired. (b) admits a stamp written under
  a handed `own-only` at a boundary whose R reads `own-mixed-contended`, so a `MIXED` red that
  boundary blocks selects the scoped gate: a widened write surface (veto 3). (c) fails S4 as written
  (veto 1) and costs every push from a git dir whose default branch holds an inherited red a FULL bar.
  Recommendation (a). RESOLVED (agent, 2026-11-20, delegated): (a), by M3, the only survivor; the
  `every-red` mapping is the step's `park`. widens: none · relaxes: none
- **F9 — Does the routing record write this unit's route words or the `item.test.route` row's
  outcomes?** The row of `tools/loop/loop.toml`, declared since the base, names its outcomes `own`,
  `contended`, `dead-probe`, `inherited`, `non-blocking` and `nondeterministic`. Options: (a) the
  record writes this unit's route words, and §4's table names the outcome each stands for; (b) it
  writes the row's outcomes; (c) this unit renames the row's outcomes to its route words. (b) fails
  AC3 as written and the `quiet-rerun` and `flakes` words units 30 and 8 consume (veto 1). (c) edits the
  loop definition's outcome set, its `routes` keys and the transition keyed `inherited`, which the
  tree does not force and the re-ground that raised this fork may not take on (its brief's
  non-goals). The cost of (a): nothing checks the join between the record and the row, a follow-up
  for the unit that arms the row's witness. Recommendation (a). RESOLVED (agent, 2026-11-20,
  delegated): (a), by M3, the survivor once (b) fails veto 1 and (c) leaves this re-ground's scope.
  widens: none · relaxes: none
- **F10 — Does this unit document the two keys it makes live?** `help/reference/policy.md`, rendered
  since the base, lists `verdict.blocks` and `verdict.red-route` bare, because their catalogue rows
  carry no `summary` or `usage`. Options: (a) both rows gain the two fields, drained from
  `tools/policy/unsummarised-keys.txt`, the page and the mirror re-rendered, as
  `TOOL-dWitnessedBar-4` S7 did for `verdict.tree`; (b) none. (b) leaves the keys an adopter now sets
  undocumented on the page that lists every key, against the charter's `[docs]`. Recommendation (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), by M3, the option satisfying the charter's `[docs]`
  rule. widens: none · relaxes: none
- **F11 — What becomes of the policy kit's two spellings of the key?** `GATE_ENV_MARKS` in
  `tools/policy/policy.py` marks it and `tools/policy/check_policy.py`'s legacy fixture plants and
  drains it, both landed since the base. Options: (a) delete the mark and re-point the fixture to
  `INHERITED_RED_MAX_AGE`, a key still marked; (b) keep both, AC6 naming them. (b) keeps a mark for a
  key no graded tree can hold once gov's gate file drops it, since the legacy list is graded in gov's
  tree alone, against the charter's `[yagni]` "delete rather than disable". Recommendation (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), by M3, tie-broken by the charter's `[yagni]`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 3, the brief's I9 and owned-node table,
  scout A's row for cl-0341, flow-steps' `test.route` and `test.attribute` rows, and the runner, hook
  and driver read at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-44, TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; the `**Carries:**` line re-pinned to `65d333f3`, deviation 31's amended text, with §8 F5; nothing else moved.
- rev-3 · 2026-10-26 · §3 · §3 Edges · §4 The routes · §5 · AC5 · §8 F6 · re-grounded on the cross-check
  record `2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck`, rows 4 and 6: the owner exception
  narrowed to a core gate's red matched by principle and part, none admitted under
  `owner-only-expiring` until PLAY-dOrderedCharter-15's check lands; `judge` reaches the loop and
  policy kits by subprocess, with F6 open for the loop read verb.
- rev-4 · 2026-11-05 · §3 Edges · §4 The routes · AC5 · §8 F6 · F6 RESOLVED (owner) to (a), by the
  brief `2026-11-05-prompt-TOOL-dWitnessedBar-3-1-spec-writer`: `judge` runs `loop_lib.py items
  --tag`, the ask this build run files in dDeclaredLoop's `BACKLOG.md`; nothing else moved.
- rev-5 · 2026-11-19 · §7 · AC1 · the leg line gains `scratch-guard self-test`, `routed-commits selftest`,
  `tier2-review self-test` and `policy fixtures`, whose manifest guards hold the §4 paths
  `tools/unattended/unattended.sh`, `tools/policy/legacy-homes.txt` and `tools/govkit/govkit.py`; and AC1,
  run from the root, sources the new library through `$KITDIR` as `tools/run-gates/run-gates.sh@7c21a741:5097` sources its own, in
  place of the bare name, which resolved against the working directory; per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-17-spec-tokens-brief; nothing else moved.
- rev-6 · 2026-11-20 · §3 Edges · the Edges block gains the hands-off bullet mirroring
  TOOL-dWitnessedBar-5's consumes-from edge for `verdict_flow.py`, per brief
  2026-11-20-prompt-TOOL-dWitnessedBar-5-edges-brief; nothing else moved.
- rev-7 · 2026-11-20 · S2 S3 S4 S5 S8 S9 · §3 · §3 Edges · §4 · §5 · AC6 AC8 · §7 · §8 F7 to F11 · §10 ·
  re-grounded at `ab6dc6e8` per brief 2026-11-19-prompt-TOOL-dWitnessedBar-3-reground-brief: runner,
  hook and driver citations moved to symbols or blob pins; the hook's doc-only scoping, stamp reader,
  export and landing branch joined S5's readers, the stamp gaining `blocks` (F8);
  `check_inherited_override` keeps the class, since `--hold --code inherited-red` calls it (F7); the
  routes name the `item.test.route` row's outcomes without writing them (F9); the reader population
  re-derived at 16 files (DERIVED 2026-11-20), the policy kit's mark and fixture re-pointed (F11); the legacy list
  moved to `memory/project/legacy-homes.txt`; the step reuses `conf_to_policy.py`; `judge` imports
  `resolve_kit_dir` from `leg_factory`; S9 documents both keys (F10); Files touched gains the mirror,
  the policy kit, the two ledgers and the kickoff manifest, the leg line their legs.
- rev-8 · 2026-11-20 · §9 · rev-7's line pins the reader count it re-derived as DERIVED, per brief
  2026-11-20-prompt-TOOL-dWitnessedBar-3-pin-brief; nothing else moved.

## 10. Reuse audit

The seam extended is the runner's attribution pass, `run_attribution` and `derive_attribution`
(`tools/run-gates/run-gates.sh#run_attribution`, `tools/run-gates/run-gates.sh#derive_attribution`),
whose record already carries each red's class, and the two deciding readers that already consume it,
the hook's `check_inherited_verdict` and the driver's `read_gates_record`; the policy read is
dGroundRules' `policy.py get`, reached as the hook's floor reader and the driver's
`read_spec_audit_switch` already reach a sibling kit. The upgrade step extends
`tools/govkit/steps/conf_to_policy.py`, the shared part of a step moving a conf key into policy keys,
extracted at that kind's second instance; `judge` imports `resolve_kit_dir` from `leg_factory` as
`keep_tails.py` does. `python tools/codebase-map/reuse_lookup.py "decide which red legs block a
landing from their attribution class"`, re-run at `ab6dc6e8` on 2026-11-20, ranked the `leg` and
`legs` stems, `derive_attribution`, `check_landed_facts_due` and `read_attribution_tokens`
(`tools/unattended/lib-unattended.sh#read_attribution_tokens`), which reads commit subjects and
trailers, not the attribution record, so it is no seam here; no existing table maps a class to a
block, so `lib-verdict.sh` is new. The recall probe, re-run the same day, returned scout A's row, this
spec, the ask TOOL-dWitnessedBar-36, deviation 31, the brief's unit row, section 13 of
`memory/guides/UNATTENDED-STOPS.md` (the render of `STOPS.template.md`, a by-name reader already
listed) and TOOL-dUnstuckLanding-11, which accepts on adopters declaring `INHERITED_RED=land`, which
this unit retires; TOOL-dWitnessedBar-36 carries that ask to its owner. Scout A cites the base:
its row at `tools/run-gates/run-gates.sh@cdfbd1cf:5064` is the `printf` at
`tools/run-gates/run-gates.sh@cdfbd1cf:5066-5068`, and its `check_inherited_verdict` at
`.githooks/pre-push@cdfbd1cf:2230`; both moved to the symbols this spec cites.

Recall terms used: `python tools/memory-recall/query.py "how does the bar's red attribution decide what blocks a landing" --terms "attribution OWN INHERITED MIXED CONTENDED DEAD PROBE verdict.blocks INHERITED_RED land park test.route"`
