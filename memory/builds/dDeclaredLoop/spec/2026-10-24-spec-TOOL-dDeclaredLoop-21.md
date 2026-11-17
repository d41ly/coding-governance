# TOOL-dDeclaredLoop-21 — the review round bounds as policy keys: review.max-rounds, the design rounds and follow-ups, REVIEW_ROUNDS and RUNAWAY_CEILING retired

**Status:** CLOSED · rev-8 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 26 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0106@90aa01b6 whole
**Carries:** node:policy-key.review.follow-up
**Carries:** node:policy-key.review.design.rounds
**Carries:** node:policy-key.review.design.round-count
**Carries:** node:policy-key.review.max-rounds

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-21-deviation-211.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-21-deviation-211.md) | deviation | — |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-1-reground-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 |
| [2026-11-05-build-TOOL-dDeclaredLoop-21-deviation-212.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-21-deviation-212.md) | deviation | — |
| [2026-11-05-build-TOOL-dDeclaredLoop-21-deviation-213.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-21-deviation-213.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-1-builder-return.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-1-builder-return.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-2-builder-return.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-2-builder-return.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-3-builder-return.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-3-builder-return.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-4-builder-return.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-4-builder-return.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-214.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-214.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-215.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-215.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-216.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-216.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-217.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-217.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-218.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-deviation-218.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-39.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-39.md) | red-fix | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-42.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-42.md) | red-fix | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-43.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-43.md) | red-fix | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-44.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-21-red-fix-44.md) | red-fix | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-21-1-spec-reviewer.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-21-1-spec-reviewer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md) | research | TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-2-spec-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-2-spec-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-3-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-3-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-4-spec-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-4-spec-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-5-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-5-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-6-spec-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-6-spec-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-7-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-7-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-8-spec-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-8-spec-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-9-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-9-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-21-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-21-build-brief.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

Every review loop's bound becomes a policy value the owner sets in one file: `review.max-rounds` bounds
every loop, the closing review's follow-ups included, the design audit's rounds follow
`review.design.rounds` and `review.design.round-count`, and the closing review's follow-ups follow
`review.follow-up`. Today the backstop is a file constant, `RUNAWAY_CEILING="8"`, set inside
`tools/unattended/unattended.sh#load_driver_conf`, the spec bound is a conf key, `REVIEW_ROUNDS`, read in
the same function, and the closing review has no bound but the constant (the stall-and-loop round, P39;
v2:1253-1255).

## 2. Scope (IN)

- **S1** — The one reader of the four keys, `read_review_bounds(root, rev=None)` in the new module
  `tools/loop/review_bounds.py`, each key read through dGroundRules-2's `resolve` (I10), with the
  catalogue defaults until a file sets them: `review.max-rounds` 3, `review.design.rounds` `one`,
  `review.design.round-count` 2, `review.follow-up` `after-high`. It derives two bounds: the spec bound,
  1 under `one`, `review.design.round-count` under `fixed-count`, and `review.max-rounds` under each
  `until-*` value; and the closing bound, 1 under `never` and `review.max-rounds` otherwise. Its CLI,
  `python tools/loop/review_bounds.py show [--rev <rev>]`, prints
  `max-rounds=<n> spec-bound=<n> closing-bound=<n> follow-up=<value>` on one line, and
  `python tools/loop/review_bounds.py --fixture [--plant <case>]` runs S2's plants. Each key reaches
  `resolve` as a string-literal first argument, the call shape
  `tools/policy/check_policy.py#READER_SHAPES` scans, so the policy kit's reader coverage finds a
  reader for each once this build lands. Each verb has a `tools/govkit/usage.toml` row and a usage
  anchor on `help/loop.md` (S10). Observed by AC1, AC3, AC9.
- **S2** — The refusal and its leg. A `review.design.round-count` above `review.max-rounds` is refused
  under `fixed-count`, naming both keys and both values, and a count equal to it is admitted (v2:1254).
  Any value below 1 or outside a key's catalogued values is refused. The refusal lives in the loop kit,
  so it holds with `unattended.sh` absent: `check_review_bounds` runs as an arm of `loop_lib.py --check`,
  the leg `loop definition` (TOOL-dDeclaredLoop-1 S7), over the tree's policy file. Where the policy
  kit does not resolve beside the loop kit, an adopter's legal install, it grades nothing and `--check`
  prints one `loop: review bounds unarmed · <why>` line, as it prints `inputs unarmed`. The module's
  plants run by `python tools/loop/review_bounds.py --fixture`, the new leg `loop review bounds fixtures`
  in `tools/gate-legs.json`. Its row carries `enforces = ["principle.p38"]` (dOrderedCharter-7 S2), the
  tag of the v2 `[enforcement]` row naming this unit's clause `cl-dClosedLoop-0106`, and
  `stage = ["step.test"]`, the key every leg row carries, with chunk `selftests`, subject `kit` and a
  ceiling of 120 PINNED seconds. The leg is gov's own: an `[[exempt_leg]]` row in `tools/govkit/registry.toml`
  and the row `python tools/govkit/govkit.py selfcheck --write` writes into
  `tools/govkit/subject-pins.tsv`, with a comment in `tools/loop/kit.toml` naming the module and its leg,
  as `loop upstream fixtures` is declared. It gains a `tools/run-gates/selftest-budgets.txt` row priced
  from a timed run of its plants, PINNED with date and node by that file's rule, and the claim in
  `memory/map/features/loop.md`, with `python tools/codebase-map/gen_map.py --write` regenerating the
  four files under `memory/map/generated/`. The pending list holds the row
  `principle principle.p38 dGroundRules`, which this pass deletes, as the meta-check reds a pending row
  whose item is now enforced. Observed by AC1, AC2 and AC10.
  **Readers:** by name: `tools/playbook/core-pending.txt`, the pending list that spells `principle.p38`, and `tools/playbook/core.py`, whose `meta-check` verb reads that list and reds a row whose item a leg now enforces
  by value: NO VALUE READERS — a pending row's value is its arming build, which the meta-check prints only in its pending count.
- **S3** — `RUNAWAY_CEILING` retired into `review.max-rounds`. `tools/unattended/unattended.sh#review_state`
  keeps its test order, zero, then non-decrease, then the ceiling, then the bound, with the ceiling read
  as one round past `review.max-rounds` (`n + 1 > max-rounds`), dFairHearing-17's `deriveRoundState`
  order. `tools/unattended/unattended.sh#verb_review` takes the closing bound on the slug subject and the
  spec bound on every other (`tools/unattended/unattended.sh@a47450e4:13215`), each read by
  `load_review_bounds`, or from the driver's four kit defaults where the module or the policy kit does
  not resolve (§4 "How the shell reads it", §8 F9), and its `CEILING` and
  `BOUNDED` exit sentences (`tools/unattended/unattended.sh@a47450e4:13324-13325`) name the key they
  stopped at. The constant's own line and its comment block go out of
  `tools/unattended/unattended.sh#load_driver_conf` (`tools/unattended/unattended.sh@a47450e4:923-931`).
  The parity arm dFairHearing-17 S5 added to `tools/workflows/tier2-review.test.sh`
  (`tools/workflows/tier2-review.test.sh@e7cbf525:3787-3797`) slices the constant's line and takes the
  ceiling as its own variable instead, which the arm sets to each row's limit, so the driver's ceiling
  sits one round past it as dFairHearing-17 §4 "The rule" puts the harness's, and the limit-4 row reads
  `BOUNDED` in both. Observed by AC4, AC11.
  **Readers:** by name: `tools/unattended/unattended.sh` (`load_driver_conf`, `review_state`, `verb_review`), `tools/unattended/check-unattended.sh`, `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.test.sh`, `tools/unattended/runlog-writer.test.sh`, `tools/workflows/tier2-review.test.sh`
  by value: the `ceiling of 8` arms of `tools/unattended/unattended.test.sh` (`tools/unattended/unattended.test.sh@8aae640b:11128` and `tools/unattended/unattended.test.sh@8aae640b:11134`), each re-pointed to `review.max-rounds`'s default of 3, the ceiling read of that suite (`tools/unattended/unattended.test.sh@8aae640b:8657-8659`), and check 2's awk arm in `tools/unattended/check-unattended.sh`, which S6 re-points.
- **S4** — `REVIEW_ROUNDS` retired into `review.design.rounds` and `review.design.round-count`, with
  `REVIEW_ROUNDS_DEFAULT` (`tools/unattended/unattended.sh@a47450e4:588`), its `read_bound_key` call, its
  strict-below refusal and the NOTE it prints (`tools/unattended/unattended.sh@a47450e4:932-940`, inside
  `load_driver_conf`). Every line `git grep -n REVIEW_ROUNDS` prints in a by-name reader below is
  re-worded to the policy keys or goes, DERIVED by that command at the pass rather than pinned here.
  BUILD-METHOD M4's chain paragraph, whose "so `REVIEW_ROUNDS` bounds no chain" becomes "so no round
  bound bounds a chain", names no policy key a reader could take for a chain stop. The generated
  `tools/policy/legacy-homes.txt` loses its row `.unattended.conf REVIEW_ROUNDS owner-policy` through
  `python tools/policy/policy.py lists --write`, run after S9, since `lists --check` reds a row no
  home yields; `help/policy.md`'s example row becomes `.unattended.conf GATE_BOUND owner-policy`, a row
  the list keeps. The by-value fixtures split in three. A fixture conf that declares the key only so the
  driver prints no blank-key NOTE and runs no review round loses the line:
  `tools/loop/loop_witness.py#HOLD_CONF`, the conf of `tools/unattended/pass-tree.test.sh`, the conf of
  `tools/unattended/resume-tick.test.sh`, and each conf heredoc and `printf` conf of
  `tools/unattended/unattended.test.sh` whose arm runs no `--review` or records only a round at blockers
  0, which reads `CONVERGED` under any bound. A fixture built by
  `tools/unattended/unattended.test.sh#write_switch_fixture`, which copies the driver and
  `lib-unattended.sh` and no loop kit, loses its `REVIEW_ROUNDS="1"` and nothing else: the three
  `printf` confs of `write_fold_fixture`, the TOOL-dFoldedAudit-14 left-shift block and
  `write_gate_fixture` (`tools/unattended/unattended.test.sh@8aae640b:2655`,
  `tools/unattended/unattended.test.sh@8aae640b:2777` and
  `tools/unattended/unattended.test.sh@8aae640b:3175`). Its driver reads the kit defaults (§8 F9), a
  spec bound of 1, the value the line set, so its 46 `--review` calls need no policy commit and no kit
  copy. A fixture that bounds a review,
  `tools/unattended/unattended.test.sh#mkconf`'s seventh positional, default 7, with its callers, and
  the round-bound arms of `tools/unattended/check-unattended.test.sh` through its `write_rounds_line`,
  is re-pointed to a committed policy file setting `review.design.rounds = "fixed-count"` and
  `review.design.round-count` at the value, with `review.max-rounds` raised to the value where it
  exceeds 3, as S7 maps an adopter's value, since S2 refuses a count above the ceiling. In the driver
  suite that file is the landed one, because `review_bounds.py show` reads the clone's
  `refs/remotes/origin/main` and every arm runs on branch `unit` (§8 F7). The default, `fixed-count` at 7
  with `review.max-rounds` 7, is committed on the fixture's `main` in its base commit, before the push to
  the bare ORIGIN (`tools/unattended/unattended.test.sh@8aae640b:596-617`). No other sub-fixture of that
  suite needs it: the one that pushes its own ORIGIN and runs `--review`
  (`tools/unattended/unattended.test.sh@8aae640b:13825`) records a round at blockers 0. The one arm
  with a value of its own, the spec bound of 1 (`tools/unattended/unattended.test.sh@8aae640b:8799-8832`), lands
  it after its `bcopen` as a commit parented on `$BASE` whose policy file sets `review.design.rounds =
  "one"` with `review.max-rounds` 7, and points only the clone's `refs/remotes/origin/main` at it,
  putting that ref back to `$BASE` before the arm's closing `reset_tree`. The bare ORIGIN's `main`, the
  tip `tools/unattended/unattended.sh#observe_anchor` reads through `ls-remote`, never moves, so the
  merge-base `tools/unattended/unattended.sh#resolve_base` takes, the run's BASE, stays `$BASE`. The arms
  at 9, 8 and 0 (`tools/unattended/unattended.test.sh@8aae640b:11123-11137`) assert the load-time
  refusal this unit retires and go with it: a count equal to the ceiling is admitted (§4 "The bounds"),
  and a count below 1 is the module's refusal, which the leg's plants observe. An arm that read
  the slug subject's `CEILING` at round 8 reads `BOUNDED` at that closing bound, as §4 "The bounds" says.
  The driver suite's default read (`tools/unattended/unattended.test.sh@8aae640b:11113-11119`) reads
  `review_bounds.py show` instead, the copied refusal of `tools/unattended/runlog-writer.test.sh`
  (`tools/unattended/runlog-writer.test.sh@2c1687bc:522-530`) goes with the driver's, and
  `tools/policy/check_policy.py#LEGACY_CONF` plants `GATE_BOUND="3"` where it planted the retired key,
  which changes no expected report, because that fixture seeds its own list. The driver suite gains two
  arms: one landing a refused policy file on the tracking ref, as the bound-1 arm lands its own, whose
  `hit` names the literal of `verb_review`'s new `fail 37` relay (§4 "Budgets and records"); and the
  parity arm of the four kit defaults (§4 "How the shell reads it"), beside TOOL-dFoldedAudit-7's AC5
  arm (`tools/unattended/unattended.test.sh@8aae640b:2596-2606`). Each unattended suite whose assertions
  move takes its `FLOOR_ASSERTIONS` and its region's `FLOOR_SHARD_<n>` by the net delta, counted off the
  diff by region, as TOOL-aSparedSpawn-14 lowered them. Observed by AC5, AC11.
  **Readers:** by name: `tools/unattended/unattended.sh` (`REVIEW_ROUNDS_DEFAULT`, `load_driver_conf`, `verb_review`), `tools/unattended/check-unattended.sh` (`read_rounds_of`, `scan_round_writes`), `tools/unattended/kit.toml`, `.unattended.conf`, `tools/unattended/.unattended.conf.example`, `tools/unattended/lib-unattended.sh`, `tools/unattended/README.md`, `tools/unattended/PROTOCOL.template.md` and its render `memory/guides/UNATTENDED-PROTOCOL.md`, `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md`, `tools/memory-tree/BUILD-METHOD.template.md` and its render `memory/guides/BUILD-METHOD.md`, `tools/workflows/unattended-build.template.js` and its render `tools/workflows/unattended-build.js`, `tools/policy/legacy-homes.txt`, `help/policy.md`
  by value: `tools/unattended/unattended.test.sh` (`mkconf`, its conf heredocs and `printf` confs), `tools/unattended/check-unattended.test.sh` (`write_rounds_line` and the round-bound arms), `tools/unattended/runlog-writer.test.sh`, `tools/unattended/resume-tick.test.sh`, `tools/unattended/pass-tree.test.sh`, `tools/loop/loop_witness.py` (`HOLD_CONF`), `tools/policy/check_policy.py` (`LEGACY_CONF`), each treated as the paragraph above says.
- **S5** — `review.follow-up` on the closing review's subject: `never` gives it one round; `after-high`
  re-arms a follow-up only after a round standing on a blocker or a high, read from the count the
  round records, which TOOL-dDeclaredLoop-32 widens to blockers and highs; `while-finding` is admitted
  and bounded by `review.max-rounds` here, its stopping rule TOOL-dDeclaredLoop-32's, as every
  `until-*` value of `review.design.rounds` is. Observed by AC3.
- **S6** — `tools/unattended/check-unattended.sh` re-pointed. Check 2's ceiling, read today by
  `core_of RUNAWAY_CEILING` (`tools/unattended/check-unattended.sh@f86fd49d:765`), is read from the loop
  kit's `review_bounds.py show`, the module and the policy kit found through the leg's
  `resolve_kit_dir` from `$HERE`, as check 53 finds `loop_lib.py`
  (`tools/unattended/check-unattended.sh@f86fd49d:6768-6771`), never by a typed kit path. Where python,
  the module or the policy kit does not resolve, check 2 reads the driver's four `REVIEW_*_DEFAULT`
  constants by `tools/unattended/check-unattended.sh#core_of`, as it reads `RUNAWAY_CEILING` today, and
  prints one unconditional stdout line naming that source, as its cutoff announcements do; the leg holds
  no copy of a bound. An unreadable value, the module refusing or a default constant `core_of` cannot
  read, refuses as the empty ceiling does today (`tools/unattended/check-unattended.sh@f86fd49d:873-874`),
  that `fail 2` re-worded in place to name the review bounds, and its awk arm
  (`tools/unattended/check-unattended.sh@f86fd49d:998`, compared at
  `tools/unattended/check-unattended.sh@f86fd49d:1071-1072`) compares each subject's rounds with that
  subject's bound, the closing bound on the build slug and the spec bound on every other, its sentence
  naming that bound and its key. It does so in a record first-committed on or after `ROUND_BOUND_CUTOFF`
  or not yet committed, and grades the round count of no record first-committed before it (§8 F6).
  `ROUND_BOUND_CUTOFF` is a driver constant declared after `FOLD_CUTOFF` and `SPEC_COUNTS_CUTOFF`
  (`tools/unattended/unattended.sh@a47450e4:1175` and `tools/unattended/unattended.sh@a47450e4:1185`),
  which no driver line reads, as none reads `FOLD_CUTOFF`; check 2 reads it by `core_of` beside
  `FOLD_CUTOFF`'s read (`tools/unattended/check-unattended.sh@f86fd49d:776`). The date compared is
  `rv_fc`, the record's first-commit date through `--follow`
  (`tools/unattended/check-unattended.sh@f86fd49d:960`), passed to the awk, which tests it as it tests
  `SPEC_COUNTS_CUTOFF`: an empty date, the in-flight record, grades. A cutoff that is no ISO date is
  named into `rv_bad`, as `FOLD_CUTOFF`'s is (`tools/unattended/check-unattended.sh@f86fd49d:880-883`).
  Its value is the day after the newest date
  `git log --all --diff-filter=A --format=%cs -- ":(glob)memory/builds/*/RUN*.md"` prints at the pass,
  PINNED in the constant's comment with that probe, by `FOLD_CUTOFF`'s idiom, strictly past the newest
  record any branch can still write under the old contract
  (`tools/unattended/unattended.sh@a47450e4:1171-1174`). A record a ref first-commits on or after it
  before the landing reds check 2 at the merge, and the close moves the date past it, as `FOLD_CUTOFF`
  was moved. Check 19's round-bound arm
  (`tools/unattended/check-unattended.sh@f86fd49d:3046-3068`), the owner-only round bound, is re-pointed
  and kept: `tools/unattended/check-unattended.sh#read_rounds_of`, called by
  `tools/unattended/check-unattended.sh#scan_round_writes` at each commit and each parent, reads the
  spec bound through `review_bounds.py show --rev`, so a run commit moving the effective bound in
  `.governance/policy.toml` reds as a conf edit does today, and the arm's comment block and failure
  sentence name the policy file. Where the module or the policy kit does not resolve, both sides read
  the driver's `REVIEW_SPEC_BOUND_DEFAULT`, so no commit reads as a move: the driver then reads no policy
  file either. In `tools/unattended/check-unattended.test.sh` the unreadable-ceiling arm
  (`tools/unattended/check-unattended.test.sh@ef109261:1181-1185`) unquotes `REVIEW_MAX_ROUNDS_DEFAULT`
  where it unquoted `RUNAWAY_CEILING`, its tree holding no `review_bounds.py`, and its `hit` takes the
  re-worded literal. The round-bound arms
  (`tools/unattended/check-unattended.test.sh@ef109261:6464-6552`, with `write_rounds_line` and
  `build_round_walk` at `tools/unattended/check-unattended.test.sh@ef109261:841-858`) build their trees with `review_bounds.py` and the policy kit's `policy.py`, `budgets.py` and
  `catalogue.toml` committed in the base commit, write each raise as a policy file, and `MA_ROUNDS`
  takes check 19's re-worded literal. R4 and R5 grade the conf's sourcing grammar, a decoy assignment
  and a zero-padded value, which a TOML file does not have, and go. Observed by AC6.
- **S7** — The upgrade step (I25). An `[[upgrade]]` row `unattended/review-rounds-to-policy` in
  `tools/unattended/kit.toml`, shaped as the `agent-cap/fanout-cap-to-agents-in-flight` row of
  `tools/hooks/kit.toml`: `up`, `down` and `witness` argv on its program
  `tools/govkit/steps/review_rounds.py`, `surfaces = ["conf-key:.unattended.conf#REVIEW_ROUNDS"]` and
  `needs-target`. On dSafePassage-1's step kind, up reads an adopter's effective `REVIEW_ROUNDS`,
  writes nothing for 1, which is the catalogue default `one`, and for N above 1 writes
  `review.design.rounds = "fixed-count"` and `review.design.round-count = N`, adding
  `review.max-rounds = N` when N exceeds 3 so the adopter's bound reads the same; then it deletes the
  conf line. Down restores both files byte-identical. Witness exits 0 when no `REVIEW_ROUNDS`
  assignment is left in the conf. Each of the three verbs has a `tools/govkit/usage.toml` row and a
  usage anchor on `help/upgrade-steps.md`, beside `fanout_cap.py`'s three, and its arms join
  dSafePassage-1's in `tools/govkit/selftest.py`. Observed by AC7, AC9.
  **Readers:** by name: in an adopter's tree the line is read only by its installed copy of this kit, the same files S4 re-points in this unit, so the release that ships the step ships no reader of it: `tools/unattended/unattended.sh` (`load_driver_conf`), `tools/unattended/check-unattended.sh` (`read_rounds_of`), `tools/unattended/kit.toml` and `tools/unattended/.unattended.conf.example`; S4 carries the full list, and gov's own line, in `.unattended.conf`, is S9's
  by value: the adopter's N, read today by `verb_review`'s bound in `tools/unattended/unattended.sh` and by check 19 through `read_rounds_of` in `tools/unattended/check-unattended.sh`, each reading `review.design.round-count` after S4 and S6, the key the step writes N into.
- **S8** — The shared step, extracted at this second instance (I25): the move of one conf key into
  policy keys and back, `tools/govkit/steps/conf_to_policy.py`, generalised by conf file and key from
  `tools/govkit/steps/fanout_cap.py`'s `parse_conf`, `render_conf_rest`, `check_committed` and
  `render_policy_bytes`, its policy text written through `upgrade_steps.render_policy_text`. S7's
  `review_rounds.py` is its one caller here and loads it by path, as `fanout_cap.py` loads
  `upgrade_steps.py`, since the runner's `-I` leaves a program's own directory off `sys.path`.
  `fanout_cap.py` stays byte-identical: it is the program of the landed row
  `agent-cap/fanout-cap-to-agents-in-flight`, and `tools/govkit/upgrade_steps.py#check_frozen` reds any
  byte a landed argv's program moves (§8 F8). Its move onto the module belongs to a later step row whose program calls the module in the
  landed row's place, owed as a backlog row the close writes. Every new function name in `review_bounds.py`, `conf_to_policy.py` and
  `review_rounds.py` opens with a verb of `.lexicon.conf`'s table, and each new `raise Refusal` site of
  the two step files is reached by S7's `tools/govkit/selftest.py` arm. Observed by
  AC7, AC8.
- **S9** — Gov migrated first: S7's up runs on gov's own tree in this unit's commit, and gov's
  `REVIEW_ROUNDS="1"` in `.unattended.conf` maps to the default, so the step leaves no line and writes
  no policy key; S4's regeneration of `tools/policy/legacy-homes.txt` follows it. Observed by AC5, AC7.
- **S10** — The page `help/loop.md` (TOOL-dDeclaredLoop-1 S7) gains a section on the review bounds:
  the four keys, the two derived bounds, that a count equal to `review.max-rounds` is admitted and
  raising any of them is the owner's, and the usage anchors of `review_bounds.py show` and
  `review_bounds.py --fixture`. The page `help/upgrade-steps.md` gains the step's section with its
  three anchors, each anchor's fingerprint as `python tools/govkit/docs_leg.py --fingerprints` prints
  it. Observed by AC9.

## 3. Non-goals (OUT)

- No stopping rule for an `until-*` or `while-*` value and no blocker-and-high count:
  TOOL-dDeclaredLoop-32's convergence routing. No disposal of a terminal round's findings: a
  closing-review follow-up's and a fix pass's are TOOL-dDeclaredLoop-32's; a spec audit's are
  BUILD-METHOD M4's spec-audit rule's, applied through TOOL-dDeclaredLoop-20's `item.review.dispose` row.
- No `review.trigger` refusal and no disposal: TOOL-dDeclaredLoop-20's items read the bound.
- No catalogue row: dGroundRules-1 S3 writes one per v2 row, and dGroundRules-11 gives the loop bounds
  `direction = "raise-loosens"`, which makes raising each the owner's.
- No write to `.governance/policy.toml` by an agent: gov's own value maps to the default, so the step
  writes none here, and an adopter's step runs under govkit's update.
- No run of the unattended kit's own suites at the close: README rule 8 waives them for this landing,
  so the by-value fixture edits are made and their clean reading is owed with PLAY-dClosedLoop-13.
- No `help/` page on the unattended conf: none exists, and the loop page carries the keys.

### Edges

- **hands-off** `TOOL-dDeclaredLoop-32` — `review.max-rounds`, with the spec and closing bounds, which the convergence routing stops `until-*` and `while-*` loops against
- **hands-off** `TOOL-dDeclaredLoop-20` — `review.max-rounds`, the bound `review.trigger` refuses another round past
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 9, 39, 44, 63, each a scope item of that unit

## 4. Design

### The bounds

| Subject | Bound | Ceiling (`CEILING` past it) |
|---|---|---|
| the closing review (the build slug) | 1 under `never`, else `review.max-rounds` | `review.max-rounds` |
| a spec audit (any other subject) | 1, `review.design.round-count` or `review.max-rounds`, by `review.design.rounds` | `review.max-rounds` |

`review_state` then reads, for round `r = n + 1`: `CONVERGED` at count 0; `NON-CONVERGENT` when the
count did not fall; `CEILING` when `r > max-rounds`; `BOUNDED` when `r >= bound`; `CONVERGING`
otherwise. The non-decrease reading applies to the closing review's subject: a spec audit passes
`no-fall` (TOOL-dDeclaredLoop-32 S3) and ends at its target or its bound, `CONVERGED`, `BOUNDED` or
`CEILING`, never `NON-CONVERGENT`. A bound equal to the ceiling is reached as `BOUNDED`, the equality S2
admits; today the ceiling's `>=` test in `tools/unattended/unattended.sh#review_state` fires first, which
is why `load_driver_conf` refuses equality.

### How the shell reads it

One driver function, `load_review_bounds`, called by `tools/unattended/unattended.sh#verb_review` alone
(§8 F10), sets `MAX_ROUNDS`, `SPEC_BOUND`, `CLOSING_BOUND` and `FOLLOW_UP`. It finds the module through
`tools/unattended/unattended.sh#resolve_position_engine` with the script name `review_bounds.py`, as
`--rescope --flow` finds `adapt.py`, and the policy kit by `resolve_kit_dir "$PE_PY" policy policy.py
"$KIT_DIR"`, the probe `tools/unattended/unattended.sh#read_spec_audit_switch` makes. Where python, the
module or the policy kit does not resolve, it takes the four values from file constants and prints one
NOTE on stderr naming them (§8 F9). Otherwise it runs `"$PE_PY" "$PE_PATH" show` and splits the one line
on spaces; a non-zero exit, or a line that is not the four fields, returns 1 with the module's first
line, and `verb_review` fails 37 relaying it. Nothing is sourced. The load-time refusal leaves
`load_driver_conf` for this one function, so a driver verb that reads no review bound starts no python.

The four constants are the line `show` prints under the catalogue defaults, declared after
`SPEC_AUDIT_CHAIN_CEILING_DEFAULT` (`tools/unattended/unattended.sh@a47450e4:1186-1192`):
`REVIEW_MAX_ROUNDS_DEFAULT="3"`, `REVIEW_SPEC_BOUND_DEFAULT="1"`, `REVIEW_CLOSING_BOUND_DEFAULT="3"` and
`REVIEW_FOLLOW_UP_DEFAULT="after-high"`. They hold the derived values and not the four keys' defaults,
so the derivation of S1 stays the module's alone. I10's no-shell-copy rule admits these four, as it
admits the `SPEC_AUDIT_*_DEFAULT` three, because a copy-installed kit cannot read a kit that is not
there; no shell copy of the policy parse or of the derivation is added. Double-quoted, so check 2 reads
them by `core_of`. A parity arm in the driver suite holds them equal to `show` over a fixture with no
policy file, as TOOL-dFoldedAudit-7's AC5 arm holds the switch defaults to the catalogue's. The NOTE
reads `unattended: NOTE - the loop kit's review_bounds.py or the policy kit it reads does not resolve
beside this kit, so the review bounds take the kit defaults: ` and the four `<field>=<value>` pairs. It
never spells `no policy kit resolves`, which the fold fixture's AC8 arm asserts absent from a
`--review` that reads no switch (`tools/unattended/unattended.test.sh@8aae640b:2710`). It adds no census
site: it is an `echo` and a `return 0`.

### Migration

The upgrade step of S7, run by govkit's update over an adopter. A conf line left after the step is
an unknown key once `kit.toml` drops it from `optional_keys`, which govkit's conf check names.

### Rollout

Live at landing. Gov's spec bound stays 1; the closing review's backstop moves from 8 rounds to 3,
v2:1255's default, and a round past 3 now reads `CEILING`.

### What this does not check

The leg `loop review bounds fixtures` checks the module's derivation and refusal over its plants, and
`check_review_bounds` checks the tree's own policy file. Neither checks that the driver or check 2
reads the bound it prints, which AC4 and AC6 observe in the waived unattended suites, nor that a
round's recorded counts are true, nor that an owner's raise was the owner's, which check 19 grades
only over a run's own commits.

Check 2 grades the round count of a record first-committed on or after `ROUND_BOUND_CUTOFF`, or not
yet committed, against its subject's bound. A record first-committed before it, written under the
retired backstop of 8, is graded by check 2's other clauses alone, the stalled-loop arm among them, and
its round count by nothing: the driver of its day stopped it at 8, and the record is append-only. A
pre-cutoff record a run still appends to after the landing has its rounds bounded by the driver's
`review_state`, not by check 2. A graded record is read against the bounds the tree's landed policy
file sets now, not those at its own BASE, so an owner lowering a bound reds a graded record that ran to
the higher one; reading each record's BASE was §8 F6's option (b).

The four `REVIEW_*_DEFAULT` constants equal the catalogue's derivation only through the driver suite's
parity arm, which README rule 8 waives for this landing, so until PLAY-dClosedLoop-13 nothing run at
the bar holds them to a catalogue row that moves. `step-rows-frozen` freezes `review_rounds.py`'s
bytes once its row lands and not `conf_to_policy.py`'s, which it imports, as it freezes no
`upgrade_steps.py` byte that every step program imports.

### Files touched (estimate)

- `tools/loop/review_bounds.py` (new)
- `tools/loop/loop_lib.py`: `--check` calling `check_review_bounds`
- `tools/loop/kit.toml`: the comment naming the module and its leg
- `tools/loop/loop_witness.py`: the line out of `HOLD_CONF`
- `tools/gate-legs.json`: the leg `loop review bounds fixtures`, its `enforces` holding `principle.p38` and its `stage`
- `tools/govkit/registry.toml`: the leg's `[[exempt_leg]]` row
- `tools/govkit/subject-pins.tsv`: the leg's row, written by govkit's `selfcheck --write` (S2)
- `tools/govkit/usage.toml`: the rows of `review_bounds.py` and `review_bounds.py#show`, and of `review_rounds.py#up`, `#witness` and `#down`
- `tools/govkit/selftest.py`: the arms of AC7, reaching every new `raise Refusal` site of S8
- `tools/run-gates/selftest-budgets.txt`: the leg's row
- `tools/playbook/core-pending.txt`: the row of `principle.p38`
- `tools/policy/check_policy.py`: `LEGACY_CONF`
- `tools/policy/legacy-homes.txt`: regenerated by the policy kit's `lists --write` (S4)
- `help/loop.md`: the section of S10 and the two anchors
- `help/upgrade-steps.md`: the step's section and its three anchors
- `help/policy.md`: the example row
- `tools/unattended/unattended.sh`: with the constant `ROUND_BOUND_CUTOFF` and its comment (S6, §8 F6),
  and the four `REVIEW_*_DEFAULT` constants with their comment (§8 F9)
- `tools/unattended/check-unattended.sh`: with check 2's `ROUND_BOUND_CUTOFF` read and its cutoff in the
  awk (S6, §8 F6), and its kit-defaults read and announcement (S6, §8 F9)
- `tools/unattended/kit.toml`
- `tools/unattended/.unattended.conf.example`
- `.unattended.conf`
- `tools/unattended/lib-unattended.sh`: the comment naming the key's `read_bound_key` call
- `tools/unattended/README.md`
- `tools/unattended/PROTOCOL.template.md` and its render `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md`
- `tools/memory-tree/BUILD-METHOD.template.md` and its render `memory/guides/BUILD-METHOD.md`
- `tools/workflows/unattended-build.template.js` and its render `tools/workflows/unattended-build.js`
- `tools/govkit/steps/conf_to_policy.py` (new), `tools/govkit/steps/review_rounds.py` (new);
  `tools/govkit/steps/fanout_cap.py` is not touched (S8, §8 F8)
- `tools/unattended/unattended.test.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/resume-tick.test.sh`, `tools/unattended/runlog-writer.test.sh`,
  `tools/unattended/pass-tree.test.sh`; in `tools/unattended/unattended.test.sh`, the fixture's policy
  file committed on `main` before the ORIGIN push, the bound-1 arm's tracking-ref commit, the relay
  and parity arms, and the three `write_switch_fixture` `printf` lines (S4, §8 F7, §8 F9); in
  `tools/unattended/check-unattended.test.sh`, the arms S6 names; the floors of each (S4)
- `tools/workflows/tier2-review.test.sh`: dFairHearing-17's parity arm
- `memory/map/features/loop.md`: the leg's claim
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`: regenerated by the codebase-map kit's `--write` (S2)
- `memory/guides/SESSION-KICKOFF.md`: the manifest's `last-audit` re-stamp, since its `watch:` line
  names `tools/gate-legs.json`, `.unattended.conf`, `.memory-tree.conf` and `memory/guides/BUILD-METHOD.md`
- `.memory-tree.conf`: the driver's `REFUSAL_CEILINGS` token and its comment line (§4 "Budgets and
  records")
- `memory/project/positional-refs.txt`: the row of that token's driver count, re-pointed 326 -> 327

### Budgets and records

- `REFUSAL_CEILINGS` in `.memory-tree.conf` prices the driver and `tools/unattended/check-unattended.sh`,
  and the leg `harness arms (fail branches armed or pinned)` on §7's line observes both (§8 F5).
  - The driver: its census, read through `tools/memory-tree/check-arms.py`'s `branches` and
    `scan_refusal_sites`, is 326 PINNED (second builder return, base `8a3bd0c8`, 2026-11-16), at its
    ceiling of 326. The refusal this unit retires from `load_driver_conf` is an `echo` and `exit 2`,
    which neither `tools/memory-tree/check-arms.py#FAIL_RE` nor its `EXIT_RE` and `STATUS_RE` count,
    so retiring it lowers nothing, and `verb_review`'s one new `fail 37` branch relaying the module's refusal makes
    the census 327. The ceiling rises 326 -> 327 PINNED, under the row `TOOL-dDeclaredLoop-21` of
    `memory/DECISIONS.md`, landed by the run ahead of the pass. The kit-defaults path of §8 F9 is an
    `echo` and a `return 0` and adds no site, and §8 F10 leaves `verb_preflight` without a call; a
    second new site is a divergence, not a larger raise. The relay reads
    `fail 37 "the review bounds do not read, so this round cannot be bounded and nothing is recorded: $_rb_why"`,
    and the driver suite's relay arm (S4) `hit`s that literal, which arms it for the leg.
  - The token: the driver's entry in `REFUSAL_CEILINGS` keeps its path and takes count 327, the pass's
    date and decision `TOOL-dDeclaredLoop-21`, one space still separating it from the leg's entry. Above
    the line, after TOOL-dDeclaredLoop-28's, the pass adds the comment line:
    `# TOOL-dDeclaredLoop-21 RAISED the driver 326 -> 327, the census, under decision TOOL-dDeclaredLoop-21 (ER:388): verb_review's one fail 37 relay of the review-bounds module's refusal; the conf-load refusal it retires was an echo the census never counted.`
  - The positional row: `memory/project/positional-refs.txt`'s row pairing `.memory-tree.conf` with the
    driver's path and count 326 is re-pointed in place to 327, as d0ce2bc2 re-pointed it from 325 for
    TOOL-dDeclaredLoop-28, since `positional.py shrink` drops a stale row and never adds one.
  - The families: `tools/unattended/unattended.families.txt` stays as the return measured it,
    missing-run-state 1 of 1, required-flag 11 of 11 and field-shape 36 of 37 PINNED; the new
    message spells none of its three patterns, so it holds no `requires --`.
  - The leg: `tools/unattended/check-unattended.sh` stays at 266 PINNED, its ceiling: S6 re-words
    check 2's unreadable-ceiling `fail 2` in place and adds no branch to check 19, and its
    `ROUND_BOUND_CUTOFF` reading feeds `rv_bad`, whose one `fail 2`
    (`tools/unattended/check-unattended.sh@f86fd49d:1267`) already stands, so it adds no `fail` site.
  - After §8 F6 to F10 the counts are unchanged: `ROUND_BOUND_CUTOFF` and the four kit defaults are
    assignments, the NOTE and check 2's announcement are `echo`s, check 2's kit-defaults read is a
    `core_of` call, and the fixtures' policy commits are suite lines. The census after the change is
    the driver at 327 of a ceiling raised to 327, `tools/unattended/check-unattended.sh` at 266 of 266,
    and the families at 1 of 1, 11 of 11 and 36 of 37, each PINNED to the return's measurement at
    `12e930f8` plus this unit's one relay.
  - Armed: check 2's re-worded `fail 2` by the re-pointed arm at
    `tools/unattended/check-unattended.test.sh@ef109261:1185`, and check 19's re-worded `fail 19` by
    `MA_ROUNDS`'s `hit`s (S6). Each arm text is read statically by the leg, so the waiver of the suites'
    runs does not waive their arming.
  - TOOL-dDeclaredLoop-30's raise by two then starts from 327, as the decision row records.
- `memory/guides/BUILD-METHOD.md` measures 30709 PINNED bytes against its 30720 cap in
  `tools/template-size-limits.txt`, 11 spare. S4's M4 rewording is exactly two substitutions, in the
  template and its render: the BLOCKED-verdict paragraph's `REVIEW_ROUNDS` becomes
  `review.design.rounds`, so "A SPEC subject takes `review.design.rounds` rounds (protocol §8)", +7
  bytes; and the chain paragraph's "so `REVIEW_ROUNDS` bounds no chain" becomes "so no round bound
  bounds a chain", -2 bytes. The render
  lands at 30714 PINNED, 6 under the cap; any other M4 wording is a divergence.
- `memory/guides/UNATTENDED-PROTOCOL.md` sits at its no-headroom row of 68130. Its section 8 row for
  `REVIEW_ROUNDS` goes whole, because check 22 joins that table's first cells to the example conf's keys
  in both directions and the example loses the key; the render shrinks, the row stays, since a lowering
  is the owner's.
- The loop, unattended, govkit, policy and workflows kits' versions are owed at the lander, as
  `kit epoch (shipped bytes move, the version moves)` prints.
- This revision turns the spec's file-and-line code citations into symbol citations and blob-pinned
  lines, so the commit landing it runs `python tools/playbook/positional.py shrink`, which takes their
  rows out of `memory/project/positional-refs.txt` before `positional (the citation check alone)` reds
  them stale.

### Alternatives rejected

- **Keep the equality refusal.** v2:1254 holds the count "at or below" the ceiling, and the clause asks
  a count equal to it admitted.
- **Map `REVIEW_ROUNDS` straight onto `review.design.round-count`.** The count is read only under
  `fixed-count` (v2:1254), so a moved value under the default `one` would change nothing an adopter set.
- **A third copied step program.** dSafePassage-1 S6 and S7 already move conf files into policy keys;
  the [reuse] rule extracts the shared step here.
- **A `[[gate_leg]]` row for the new leg in `tools/loop/kit.toml`.** The leg's subject is the module
  itself, so it has no job in a tree that copy-installs the kit, the owner's 2026-08-23 ruling for a
  kit's self-test, and every loop fixtures leg is gov's `[[exempt_leg]]` for that reason, as the
  registry row of `loop upstream fixtures` records.
- **One policy file per fixture at the catalogue defaults.** The driver suite's review arms run at a
  bound of 7 so that no arm but the bounded ones stops early; moving them to a spec bound of 1 would
  rewrite every arm's expected exit instead of its conf.

## 5. Production-readiness checklist

- security — the policy file is read, never written by an agent; raising any bound stays the owner's
  under dGroundRules-6's guard and dGroundRules-11's direction.
- perf / scale — one python start per `--review`, one per check 2 run, and one per commit and parent
  check 19 reads; none where the module does not resolve.
- error / empty / loading states — an unreadable or out-of-range value refuses by key; an absent file
  reads the catalogue defaults; an absent module or policy kit reads the driver's four kit defaults,
  announced.
- observability — `show` prints every derived bound; the exit sentences name the key they stopped at.
- risks — a closing review that ran past 3 rounds before now stops at `CEILING` sooner; v2 chose 3.
- testing — direct probes of `review_bounds.py`, the driver and the leg in scratch repositories; the
  suite arms in §7, the unattended ones waived for this landing.
- migration — the step of S7; gov's own value maps to the default.
- user docs — `help/loop.md` gains the bounds' section, `help/upgrade-steps.md` the step's, and
  `help/policy.md` a kept example row; the unattended README, protocol and verbs reference are
  re-worded.

### The sweep

Every name the body changes or removes, its callers, readers, fixtures, suite arms, pinned contracts
and test populations, read at the branch tip `12e930f8`. Counts are PINNED to that commit; the
commands below re-derive them, and a builder re-runs them at its base.

| Changed or removed | Population at `12e930f8` | What keeps it green |
|---|---|---|
| `RUNAWAY_CEILING` | 23 PINNED lines in 6 files under `tools/`, and the gotcha record that cites it | S3 and S6 re-point every line; the tier2-review parity arm and the driver suite's `review_state` slice set `MAX_ROUNDS` themselves; the record keeps its text |
| `REVIEW_ROUNDS`, `REVIEW_ROUNDS_DEFAULT` | 73 lines in 20 PINNED files under AC5's pathspec, 8 of them the default; outside it `help/policy.md`, three renders under `memory/guides/`, and two append-only records | S4's derived rule and AC5; the renders regenerate; `memory/DECISIONS.md` and `memory/backlog/TOOL.md` keep their text |
| `review_state` | its one caller `verb_review`; the driver suite's slice arms; the tier2-review parity arm | the default third argument becomes `MAX_ROUNDS`, which each slicing arm sets (S3, AC4) |
| `verb_review` | 85 `--review` lines in the driver suite: 46 on `write_switch_fixture` trees, one sub-fixture round at blockers 0, the rest the main fixture's; one in `tools/unattended/runlog-writer.test.sh`, at blockers 0 | the switch trees read the kit defaults, spec bound 1 as their deleted line set (§8 F9); the main fixture reads its policy on `main` (§8 F7); a blockers-0 round reads `CONVERGED` under any bound |
| `verb_preflight` | `tools/loop/loop_witness.py#check_hold_plant` runs the real driver's `--preflight` in a scratch repository | untouched (§8 F10), so the `loop computed witness` leg sees no new line |
| `load_driver_conf` | TOOL-dFoldedAudit-7's arm that the loader calls no switch reader (`tools/unattended/unattended.test.sh@8aae640b:2540-2547`) | `load_review_bounds` is called by `verb_review` alone, never the loader |
| the NOTE of §8 F9 | the switch trees' `run_fold` output, stderr joined; the `miss` on `no policy kit resolves beside this kit` at `tools/unattended/unattended.test.sh@8aae640b:2710` | the NOTE never spells that phrase; `run_chain` drops stderr |
| check 2's ceiling read and its `fail 2` | the checker suite's trees from `reset_tree` and `tools/unattended/check-unattended.test.sh#ma_init`, each holding the loop kit's three files from `seed_loop_kit` and no `review_bounds.py` | they read the driver's kit defaults by `core_of`; the unreadable-ceiling arm is re-pointed (S6) |
| check 19, `read_rounds_of`, `scan_round_writes` | 11 `MA_ROUNDS` lines and `write_rounds_line` in `tools/unattended/check-unattended.test.sh`, arms R1 to R5 and the round-walk arms | those trees commit the module and the policy kit, raises become policy files, R4 and R5 go (S6) |
| `tools/govkit/steps/fanout_cap.py` | the landed row `agent-cap/fanout-cap-to-agents-in-flight` in `tools/hooks/kit.toml`; its three usage rows and anchors; its 7 `govkit refusal join` sites | byte-identical (§8 F8, AC8) |
| `conf_to_policy.py`, `review_rounds.py` | `tools/govkit/refusal_join.py#population`, every tracked `.py` under the govkit kit; `BRANCH_PIN` 335 and `FILE_PIN` 4, both floors; `VERB_OFFENDER_PIN` 1209 and the `sh.function.conv` pin 6 in `.lexicon.conf`; 114 tracked files carrying the inlined `resolve_kit_dir` marker | each new `raise Refusal` site reached by S7's selftest arm; the floors are only exceeded; every new name opens with a declared verb; an inlined resolver copy is byte-identical; `conf_to_policy.py` shows no page command, so the `docs` leg owes it no usage row |
| the `[[upgrade]]` row `unattended/review-rounds-to-policy` | `step-rows-frozen` over the landed rows at the merge-base | absent there, so unlanded until this build lands; frozen after |
| `optional_keys`, the example conf's block, the protocol's key row | check 22's two-way join of the protocol's section 8 to the example conf, and its one-way join of the project conf | all three go together, and S9 deletes gov's line; `RETIRED_CONF_KEYS` gains nothing, because an adopter's line goes with the step |
| `tools/policy/legacy-homes.txt` | `tools/policy/policy.py#derive_legacy_homes`, the keys of every root `.*.conf` | S9's deletion drops the row and `lists --write` regenerates it, a shrink |
| `tools/loop/loop_witness.py#HOLD_CONF` | the `loop computed witness` leg | the line goes; no reader is left |
| `tools/policy/check_policy.py#LEGACY_CONF` | the `policy fixtures` leg | it plants `GATE_BOUND="3"` and seeds its own list |
| `loop_lib.py --check` | the `loop definition` leg over gov's tree; no consumer parses its lines outside the loop kit | the policy kit resolves in gov's tree; an adopter without it reads the unarmed line (S2) |
| subject pins | `tools/govkit/subject-pins.tsv`, one row per leg | the new leg's row alone, written by `selfcheck --write` |
| verdict-epoch delegates | the `DELEGATES` list of `check-verdict-epoch.sh` | none is touched, so no bump is owed |
| census and family ceilings | §4 "Budgets and records" | 327 of 327, 266 of 266, 1, 11 and 36 of 1, 11 and 37 |
| size caps | `memory/guides/BUILD-METHOD.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, the live-spec class row | 30714 of 30720; a shrink under 68130; this spec reads over the class row as a `BUDGET WARN` under gov's `budgets.enforce = "warn"` |
| policy reader coverage | the four keys, owner `dDeclaredLoop` | graded once the build lands, each spelled as a literal `resolve` argument (S1) |
| suite floors | `FLOOR_ASSERTIONS` 3348 in the driver suite and 1152 in the checker suite, with their shard floors | each moves by the suite's net delta, counted off the diff by region (S4) |

```
git grep -n RUNAWAY_CEILING -- tools | wc -l                        # 23
git grep -l RUNAWAY_CEILING -- tools | wc -l                        # 6
git grep -n REVIEW_ROUNDS -- tools .unattended.conf | wc -l         # 73
git grep -l REVIEW_ROUNDS -- tools .unattended.conf | wc -l         # 20
git grep -n REVIEW_ROUNDS_DEFAULT -- tools | wc -l                  # 8
grep -c -- '--review' tools/unattended/unattended.test.sh            # 85
grep -c 'run_fold --' tools/unattended/unattended.test.sh            # 42
grep -c 'run_chain --review' tools/unattended/unattended.test.sh     # 4
grep -c MA_ROUNDS tools/unattended/check-unattended.test.sh          # 11
git grep -l '>>> resolve_kit_dir' -- tools | wc -l                  # 114
```

## 6. Acceptance criteria

- **AC1** — When `python review_bounds.py show --rev HEAD` runs in a scratch repository whose committed
  policy file sets `review.design.rounds = "fixed-count"`, `review.design.round-count = 4` and
  `review.max-rounds = 3`, it exits 2 naming `review.design.round-count`, 4 and 3; with the count set to
  3 it exits 0 and prints `spec-bound=3`.
  Red when: the comparison keeps the driver's strict-below form, so a count equal to the ceiling is
  refused.
- **AC2** — When the same planted policy file is committed in a scratch clone of the tree from which
  `tools/unattended/unattended.sh` has been deleted, `python review_bounds.py show --rev HEAD`, run in the
  clone's loop kit, still exits 2 naming `review.design.round-count`.
  Red when: the bound is read out of the driver, so deleting it silences the refusal.
  fixture: the clone sits under `%TEMP%/rbclone`, a short path, since the scratch path is too long for
  a clone on Windows.
- **AC3** — When `python review_bounds.py show --rev HEAD` reads policy files setting each of
  `review.follow-up` = `never`, `after-high` and `while-finding`, it prints `closing-bound=1`, `3` and
  `3`; and with no policy file it prints `max-rounds=3 spec-bound=1 closing-bound=3 follow-up=after-high`.
  Red when: `never` reads the ceiling, so a closing review the owner set to one round runs follow-ups.
- **AC4** — When `review_state` is sliced out of `tools/unattended/unattended.sh` and called with
  `MAX_ROUNDS=3` over prior counts `5 4` and a count of `3` with bound 3, it prints `BOUNDED`, and over
  `5 4 3` and `2` it prints `CEILING`; `grep -c RUNAWAY_CEILING tools/unattended/unattended.sh` prints 0.
  Red when: the ceiling is tested as `r >= max-rounds`, so the bound equal to it reads `CEILING`.
- **AC5** — When `git grep -n REVIEW_ROUNDS -- tools .unattended.conf` runs at this unit's commit, it
  prints only lines of the step's program `review_rounds.py`, its `[[upgrade]]` row in
  `tools/unattended/kit.toml` and its arms in govkit's self-test, the places the retired key's name is
  still read or planted, and `grep -c REVIEW_ROUNDS help/policy.md` prints 0.
  Red when: a by-value fixture such as `HOLD_CONF` in `tools/loop/loop_witness.py` still writes the
  line, or `tools/policy/legacy-homes.txt` still lists it, so a suite or a list grades a key no reader
  reads.
  figure: DERIVED, the grep's own output at the commit.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs in a scratch repository whose run's
  own commit raises `review.design.round-count` in the policy file, the module and the policy kit
  committed beside the copy, it fails check 19 naming the commit. With `review_bounds.py` absent from
  the scratch tree it prints the line naming the driver's kit defaults as check 2's source and fails no
  check on that account; with `REVIEW_MAX_ROUNDS_DEFAULT` unquoted in the copied driver as well, it fails
  check 2 naming the unread review bounds. In a scratch repository holding a record committed under
  `GIT_COMMITTER_DATE` before
  `ROUND_BOUND_CUTOFF` whose spec subject records 4 review rounds, check 2 names no round count for it;
  the same rows in an uncommitted record, whose empty first-commit date grades, fail check 2 naming the
  subject, its 4 rounds and its spec bound of 1.
  Red when: check 19 still reads `.unattended.conf`, so the raise in the policy file passes; or check 2
  compares every record with its subject's bound, so the pre-cutoff record reds; or check 2 refuses an
  absent module, so every install without the policy kit reds.
- **AC7** — When `python review_rounds.py up` runs over three scratch targets whose conf holds
  `REVIEW_ROUNDS="1"`, `"2"` and `"5"`, the first gains no policy key, the second gains
  `review.design.rounds = "fixed-count"` and `review.design.round-count = 2`, the third those with 5
  and `review.max-rounds = 5`, each conf losing the line, and `witness` exits 0 on each; `down`
  restores each pair byte-identical, after which `witness` exits 1 on the second and third.
  Red when: N above 3 is written without raising `review.max-rounds`, so the adopter's own bound is
  refused after the step.
- **AC8** — When `git rev-parse` reads `tools/govkit/steps/fanout_cap.py` at the merge-base of this
  unit's commit with `origin/main` and at the commit, it prints one blob id twice; and, run in the
  steps folder, `grep -n "def parse_conf\|def render_conf_rest\|def check_committed" review_rounds.py`
  prints nothing, while `grep -n conf_to_policy review_rounds.py` prints its load.
  Red when: the landed step's program moves a byte, which `step-rows-frozen` reds, or the shared part is
  copied into `review_rounds.py` and the module holds no caller's code.
- **AC9** — When `grep -n "review.max-rounds" loop.md` runs over the help page at this unit's commit, it
  finds the section naming the four keys and the admitted equality;
  `grep -o "usage: script:[^ ]*review_bounds.py[#a-z]*" help/loop.md` prints two anchors, the bare
  script's and `#show`, and `grep -o "usage: script:[^ ]*review_rounds.py#[a-z]*" help/upgrade-steps.md`
  prints three, `#up`, `#witness` and `#down`, one anchor per row S1 and S7 add to
  `tools/govkit/usage.toml`.
  Red when: the keys move into the policy file and no page says where an owner sets the bound, or a new
  verb has a usage row and no anchor, which the `docs` leg reds.
- **AC10** — When `python -m json.tool gate-legs.json` runs in the tools folder, the row named
  `loop review bounds fixtures` carries `enforces` holding `principle.p38` and `stage` holding
  `step.test`; `grep -c "principle.p38" tools/playbook/core-pending.txt` prints 0;
  `grep -c "loop review bounds fixtures"` prints 1 over each of `tools/run-gates/selftest-budgets.txt`,
  `tools/govkit/registry.toml` and `memory/map/features/loop.md`; and
  `python tools/playbook/core.py meta-check` on this unit's pass exits 0, naming neither that leg nor a
  stale pending row.
  Red when: the leg carries no `enforces`, which dOrderedCharter-7 S3's meta-check reds, or the
  pending row stays, which it reds stale.
- **AC11** — When `--review` runs a spec subject's first round at `--blockers 3` in a scratch repository
  holding only copies of `unattended.sh` and `lib-unattended.sh` under `u/` and a run record, the tree
  `write_fold_fixture` builds, its output names `exits BOUNDED`, and its stderr carries the NOTE naming
  `spec-bound=1` and not the text `no policy kit resolves`. In the same tree with the policy kit copied
  beside the driver and no loop kit, the same NOTE prints. In the main repository,
  `grep -c '^REVIEW_[A-Z_]*_DEFAULT="' tools/unattended/unattended.sh` prints 4, and
  `python review_bounds.py show`, the loop kit's module run in a scratch repository with no policy
  file, prints the four values those lines hold.
  Red when: an absent module refuses, so every `write_switch_fixture` arm fails 37; or the constants
  hold the keys' defaults and the shell derives the bounds, a second copy of S1's derivation.

## 7. Gates

`unattended kit gate` · `loop definition` · `loop computed witness` · `loop stage coverage` · `core meta-check` · `playbook render selftest` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `step-rows-frozen` · `docs` · `help page commands` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `every held leg is budgeted, every budget row resolves` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `routed-commits selftest` · `harness arms (fail branches armed or pinned)` · `build-method size` · `unattended protocol size` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `positional (the citation check alone)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/review_bounds.py · covers AC1 AC2 AC3 · the `loop review bounds fixtures` leg's plants, its failing case staged by a count above the ceiling read with the strict-below form · none
New arm: tools/govkit/selftest.py · covers AC7 · a step tree with no `review_rounds.py` and no `conf_to_policy.py` · none
New arm: tools/unattended/unattended.test.sh and tools/unattended/check-unattended.test.sh · covers AC4 AC6 AC11 · the base driver's `RUNAWAY_CEILING`, conf-keyed check 19 and no kit defaults · waived for this build's landing by README rule 8, so their clean reading is owed with PLAY-dClosedLoop-13

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `tools/memory-tree/tree_lib.py#STATUS_TOKENS`. Observation, 2026-10-24:
  `DRAFT` is not in the tuple. Liveness: the tuple would list it if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-24, delegated): `OPEN`.
- **F2 — Where does the round-count refusal live, so it holds with `unattended.sh` deleted?** Options:
  (a) the loop kit's `review_bounds.py`, called by the driver and run as an arm of the loop kit's
  check; (b) `check-unattended.sh`, reading the policy file; (c) a new catalogue field in dGroundRules'
  schema. (b) cannot run without the driver it reads fifteen sets from; (c) re-specs a parent's
  contract. RESOLVED (agent, 2026-10-24, delegated): (a), by rung 3.
  widens: none · relaxes: none
- **F3 — What does an `until-*` or `while-*` value bound here?** Options: (a) `review.max-rounds`, its
  stopping rule TOOL-dDeclaredLoop-32's; (b) refuse those values until that unit lands. Both units build
  in one run, and v2:1255 bounds every loop by the key. RESOLVED (agent, 2026-10-24, delegated): (a),
  by rung 1.
- **F4 — Editing `tools/memory-tree/BUILD-METHOD.template.md` M4 and the unattended protocol's conf
  table changes governance carriers; does the build's grant cover it?** The clause retires
  `REVIEW_ROUNDS` with its readers derived and each re-pointed, and both carriers read it by name.
  RESOLVED (agent, 2026-10-24, delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the REVIEW_ROUNDS mentions in tools/memory-tree/BUILD-METHOD.template.md, tools/unattended/PROTOCOL.template.md and their renders re-worded to the policy keys, M4's chain paragraph to name none
- **F5 — How does `verb_review` refuse an unreadable or refused review bound?** The driver's refusal
  census stands at its ceiling, 326 PINNED, and the conf-load refusal this unit retires is an `echo`
  and `exit 2` the census never counted. Options: (a) keep `verb_review`'s `fail 37` relay of the
  module's refusal, one new census site, the ceiling rising 326 -> 327 under a decision row the run
  lands before the pass, as TOOL-dDeclaredLoop-28 raised it 325 -> 326; (b) keep the census flat, the
  refusal an echo with a non-`fail` exit, the shape of the one it replaces, which no arm of
  `harness arms (fail branches armed or pinned)` grades. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a), by M3's ratify rule, the option that grades the refusal and leaves no
  follow-up; the row `TOOL-dDeclaredLoop-21` in `memory/DECISIONS.md` landed ahead of the pass, and
  §4 "Budgets and records" states the raise, its token, comment line and positional row.
  widens: none · relaxes: none
- **F6 — How does check 2 grade a record written under the retired backstop of 8?** Check 2 reads
  every tracked `RUN*.md`, and its one `fail 2` takes every subject past its limit. The third builder
  return measured, with check 2's own subject split over the tracked records at `c28d4e5f`, 69 subjects
  over their subject's bound after this unit and 4 over `review.max-rounds` alone, all in append-only
  records no verb rewrites, so the `unattended kit gate` would red at the close. Options: (a) grandfather
  by the record's first-commit date, `rv_fc` (`tools/unattended/check-unattended.sh@f86fd49d:960`), the
  idiom check 2 applies to `FOLD_CUTOFF` and `SPEC_COUNTS_CUTOFF`, with a new driver constant
  `ROUND_BOUND_CUTOFF`; (b) read each record's bound at its own BASE, as
  `tools/unattended/lib-unattended.sh#read_fold_cutoff` does, a
  record before the keys reading the retired 8: a python start per record, a record naming no base
  unreadable, and a BASE with no policy file reads the catalogue's 3, so it still needs (a)'s date for
  the 4; (c) keep a named historical backstop of 8 for the corpus and compare per-subject bounds only on
  the uncommitted in-flight record, which grades a run's record by its bound only until its first commit
  and keeps 8 as a value no driver reads. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated):
  (a), by M3's ratify rule: no option trips a veto, and (a) grades every record begun after the landing
  by its subject's bound, which (c) gives up at a record's first commit, with none of (b)'s unreadable
  bases; it reuses the seam check 2 already applies to two cutoffs. S6 states the constant's home, value
  and reading; §4 "What this does not check" and AC6 state how a pre-cutoff record is graded.
  widens: none · relaxes: check 2's round count over a record first-committed before `ROUND_BOUND_CUTOFF`, which the retired 8 graded
- **F7 — How does the driver suite's per-arm round bound reach `review_bounds.py show`, which reads the
  landed revision?** With no `--rev`, `show` reads `refs/remotes/<remote>/<branch>` through
  `tools/policy/policy.py#resolve` and `tools/policy/policy.py#derive_landed_revision`. The suite pushes
  `main` to its bare ORIGIN once (`tools/unattended/unattended.test.sh@8aae640b:617`) and every arm
  works on branch `unit`, so a policy file an arm commits there is never read, and the arms would run at
  the catalogue defaults (third builder return). Options: (a) seed the default `fixed-count` 7 and
  `review.max-rounds` 7 policy on the fixture's `main` before the ORIGIN push, a per-arm value landing
  without moving the anchor; (b) the driver calls `show --rev HEAD`, a change to §4 "How the shell reads
  it". Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), by M3's ratify rule: (b) is
  discarded by veto 3, since a bound read at HEAD lets a run's own commit loosen the bound it runs
  under, a write surface the landed read keeps the owner's; (a) keeps §4's reader and leaves no
  follow-up. S4 states the seed and how the one per-arm value, the bound of 1, lands on the clone's
  tracking ref while the advertised anchor stays.
  widens: none · relaxes: none
- **F8 — How does S8 extract the shared step when its first instance is a landed step's program?**
  `tools/govkit/steps/fanout_cap.py` is the `up`, `down` and `witness` program of the row
  `agent-cap/fanout-cap-to-agents-in-flight`, introduced by `29ccb0652` (TOOL-dSafePassage-1) and on
  main, and
  `tools/govkit/upgrade_steps.py#check_frozen` reds any byte that program moves between the merge-base
  and HEAD, so rev-7's re-pointing reds `step-rows-frozen` (fourth builder return). Options: (a)
  `fanout_cap.py` stays byte-identical, `conf_to_policy.py` has `review_rounds.py` as its one caller,
  and AC8 drops its import clause, the second caller left to a later step row; (b) re-point the fanout
  move through a new step row that retires the landed one to it, as the frozen-row rule asks; (c) an
  owner ruling exempting this edit. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a),
  the run's pick: (c) is no delegated resolver's, because the frozen-row contract is the step kind's,
  and (b) is a second mechanism in this unit against the build method's M2. S8 and AC8 state it.
  widens: none · relaxes: AC8's import clause; the move of `fanout_cap.py` onto the module, owed as a backlog row the close writes
- **F9 — What does the driver read where `review_bounds.py`, or the policy kit it reads, does not
  resolve beside it?** `tools/unattended/kit.toml` requires the loop kit and neither kit requires the
  policy kit, so an install with no policy kit is legal; and the driver suite's 46 `--review` calls on
  `tools/unattended/unattended.test.sh#write_switch_fixture` trees run with no loop kit, no remote and a
  bound of 1 (fourth builder return). Options: (a) read four kit defaults with a NOTE, as
  `tools/unattended/unattended.sh#read_spec_audit_switch` does with its `SPEC_AUDIT_*_DEFAULT`
  constants, §4's no-shell-copy wording admitting the four; (b) refuse, and every such fixture copies
  the loop and policy kits. Recommendation: (a). RESOLVED (agent, 2026-11-16, delegated): (a), the run's
  pick: it reuses the driver's one seam for an absent policy kit, the switch trees read spec bound 1
  with their `REVIEW_ROUNDS` line deleted and no other edit, and it adds no census site, the driver
  staying at 327. Check 2 and check 19 read the same constants by `core_of` where the module does not
  resolve, so the leg grades a record by the bounds its driver ran under. §4 "How the shell reads it",
  S3, S4, S6 and AC11 state it.
  widens: none · relaxes: §4's no-shell-copy rule, which admits the four `REVIEW_*_DEFAULT` constants
- **F10 — Does `verb_preflight` read the review bounds?** Rev-7 had it call `load_review_bounds` and
  named no behaviour on a refusal there, while §4 "Budgets and records" admits one new census site, the
  relay of `verb_review`. Found by this revision's sweep: `tools/loop/loop_witness.py#check_hold_plant`
  runs the real driver's `--preflight`. Options: (a) `verb_review` alone calls it; (b) preflight relays
  a refusal through a new `fail`, a second census site and a raise to 328 the run's decision row does
  not cover; (c) preflight prints a refusal and continues, a refusal no arm grades. Recommendation:
  (a). RESOLVED (agent, 2026-11-16, delegated): (a), by M3's ratify rule: (b) trips the census
  ceiling's veto, (c) leaves an ungraded refusal, and (a) leaves no follow-up, since the `loop
  definition` leg refuses the same policy file at the bar before a run reads it. §4 "How the shell
  reads it" states it.
  widens: none · relaxes: the policy file's refusal at `--preflight`, which rev-7 placed there

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 21, v2:1236 and :1253-1255, scout C's
  row and conflicts 1 to 5, dSafePassage-1 S6 and S7 and dFairHearing-17, read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-11-05 · S2 · §4 Files touched · AC10 · TOOL-dDeclaredLoop-56 §8 F5 (a), per the brief
  `2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade`: the leg `loop review bounds fixtures`
  carries `principle.p38`, its clause's `[enforcement]` row; its own pass writes it, so the core
  meta-check never reds the leg.
- rev-4 · 2026-11-05 · §3 · §4 The bounds · S3 · S4 · F4 · the parity arm sets its ceiling variable to
  each row's limit; the second `REVIEW_ROUNDS` reader, M4's chain paragraph, listed and re-worded to name no
  key; the non-decrease reading kept to the closing review, a spec audit taking `no-fall`; a spec audit's
  disposal named as M4's spec-audit rule's through TOOL-dDeclaredLoop-20's dispose row; the `roundLimit`
  claim dropped from the non-goal and the edge, by the brief
  prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md
- rev-5 · 2026-11-16 · §1 · S1 · S2 · S3 · S4 · S6 · S7 · S9 · S10 · §4 · AC5 · AC7 · AC9 · AC10 · §7 · F1 · §10 ·
  the six findings of the first builder return,
  build/2026-11-16-build-TOOL-dDeclaredLoop-21-1-builder-return.md, re-grounded at `131629c6`:
  S4 and AC5 gain the readers `tools/loop/loop_witness.py`, `tools/unattended/pass-tree.test.sh`,
  `tools/policy/check_policy.py` and `tools/policy/legacy-homes.txt`, regenerated by its generator, and
  `help/policy.md`'s example row, with the by-value fixtures split into lines deleted and confs raised
  to a ceiling S2 admits; Files touched gains `tools/govkit/selftest.py`, the usage rows and help
  anchors of `review_bounds.py` and the step's three verbs, on `help/loop.md` and
  `help/upgrade-steps.md`, and the new leg's companions, its `stage` key, `[[exempt_leg]]` row, subject
  pin, budget row, dossier claim, the four generated map files and the manifest re-stamp; §7's line
  gains `scratch-guard self-test`, `playbook render selftest`, `policy fixtures` and the legs those
  companions owe; S2's Readers name the tracked `meta-check` and pending list, and the row's deletion
  is unconditional; S7 gains the step kind's `witness`; every moved line number is a symbol citation or
  a blob-pinned line.
- rev-6 · 2026-11-16 · §4 Budgets and records · §4 Files touched · §7 · F5 · the divergence of the second
  builder return, build/2026-11-16-build-TOOL-dDeclaredLoop-21-2-builder-return.md: `verb_review`'s
  `fail 37` kept and the driver's ceiling raised 326 -> 327 under decision `TOOL-dDeclaredLoop-21`,
  with the conf token, its comment line and its positional row in Files touched, and the M4 rewording
  worded to fit the 11 PINNED bytes `BUILD-METHOD.md` has left; §7's line gains `transition-audit arms` and
  `straggler-guard arms`, the legs whose guard holds `.memory-tree.conf`.
- rev-7 · 2026-11-16 · S4 · S6 · §4 What this does not check · §4 Budgets and records · §4 Files touched ·
  AC6 · F6 · F7 · §10 · the divergence of the third builder return,
  build/2026-11-16-build-TOOL-dDeclaredLoop-21-3-builder-return.md, re-grounded at `c28d4e5f`: check 2
  grades a record's round count from `ROUND_BOUND_CUTOFF` by its first-commit date and a pre-cutoff
  record's by nothing; the driver suite's default policy is committed on the fixture's `main` before
  the ORIGIN push, the bound-1 arm landing its value on the tracking ref alone, and the 9, 8 and 0
  arms going with the retired refusal; the census and families unchanged.
- rev-8 · 2026-11-16 · S1 · S2 · S3 · S4 · S6 · S8 · §4 How the shell reads it · §4 What this does not
  check · §4 Files touched · §4 Budgets and records · section 5 · AC6 · AC8 · AC11 · §7 · F8 · F9 · F10 ·
  §10 · the divergence of the fourth builder return,
  build/2026-11-16-build-TOOL-dDeclaredLoop-21-4-builder-return.md, re-grounded at `12e930f8`:
  `fanout_cap.py` stays byte-identical and `conf_to_policy.py` has `review_rounds.py` as its one caller;
  where the module or the policy kit does not resolve, the driver and check 2 read four kit defaults,
  the switch fixtures losing their line alone; `verb_preflight` reads no bound; section 5 carries the
  sweep; the census stays 327, 266 and the families.

## 10. Reuse audit

The seams extended are the driver's round predicate `tools/unattended/unattended.sh#review_state` and
its caller `tools/unattended/unattended.sh#verb_review`, the leg's ceiling read (`core_of` at
`tools/unattended/check-unattended.sh@f86fd49d:765`) and check 19's
`tools/unattended/check-unattended.sh#read_rounds_of`, and dSafePassage-1's step kind with its first
conf-to-policy program, `tools/govkit/steps/fanout_cap.py`, whose shared part S8 extracts. At rev-7
check 2's first-commit cutoff idiom, `rv_fc` with `FOLD_CUTOFF` and `SPEC_COUNTS_CUTOFF`, is the seam
`ROUND_BOUND_CUTOFF` extends, and the driver suite's base commit before its ORIGIN push is the seam the
fixture's policy file joins. At rev-8 the driver's absent-policy-kit seam,
`tools/unattended/unattended.sh#read_spec_audit_switch` with its `SPEC_AUDIT_*_DEFAULT` constants, is
the one the four kit defaults extend, `tools/unattended/unattended.sh#resolve_position_engine` the
seam that finds the module, and check 53's `resolve_kit_dir` read the seam check 2 finds it through.
`fanout_cap.py` is no longer a seam this unit edits: its frozen bytes are read, not moved.
`python tools/codebase-map/reuse_lookup.py "move a conf round bound into a policy key with an upgrade step"`
ranked name stems (`key`, `load_conf`, `parse_conf`, `step` in `tools/govkit/govkit.py`) and found no
upgrade-step code at base. At rev-5's re-grounding, `131629c6`, the step kind is built:
`tools/govkit/upgrade_steps.py` is tracked and `fanout_cap.py` loads it, and the other step programs
under `tools/govkit/steps/` move a schema, a floor or the charter's adopter rules, none a conf key into
a policy key, so `fanout_cap.py` stays the one prior instance and S8 extracts at the second. The new
leg's companions follow the `loop upstream fixtures` leg's, TOOL-dDeclaredLoop-29. `python
tools/memory-recall/query.py` returned scout C's row, the packet's clause and aWokenSentinel's
measurement that `REVIEW_ROUNDS` bounds one subject while promotions mint fresh ones
(`memory/builds/aWokenSentinel/BACKLOG.md:5`), the cascade TOOL-dDeclaredLoop-30's budget closes. Scout
C's eleven by-value fixtures were read at base; the tree has since gained more, so S4 derives them with
`git grep` at the pass rather than listing lines, and the gotcha
`memory/gotchas/retirement-inventory-misses-readers-by-value.md` is the class that rule answers.

Recall terms used: REVIEW_ROUNDS RUNAWAY_CEILING review.max-rounds round bound BOUNDED CEILING review_state upgrade step policy key legacy-homes exempt_leg kit default no policy kit resolves frozen step
