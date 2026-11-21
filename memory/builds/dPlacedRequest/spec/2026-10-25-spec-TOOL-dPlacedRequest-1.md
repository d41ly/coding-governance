# TOOL-dPlacedRequest-1 — one lease grammar for builds, units and cadence runs, with an epoch, run claims migrated onto it, and its verbs and four policy keys

**Status:** CLOSED · rev-9 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 3 · advances TOOL-dPlacedRequest-22 · closes TOOL-dPlacedRequest-67

**Carries:** cl-dClosedLoop-0120@5d655f07 whole
**Carries:** node:record-kind.lease
**Carries:** node:policy-key.leases
**Carries:** node:policy-key.leases.granularity
**Carries:** node:policy-key.leases.renewal
**Carries:** node:policy-key.leases.overlap
**Carries:** node:policy-key.leases.offline

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-departures-spec.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-departures-spec.md) | journal | — |
| [2026-10-25-build-TOOL-dPlacedRequest-1-deviation-11.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-deviation-11.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md) | research | TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-crosscheck-returns.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-crosscheck-returns.md) | research | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-deviation-12.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-deviation-12.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-reground-returns.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-reground-returns.md) | research | — |
| [2026-11-05-build-TOOL-dPlacedRequest-1-crosscheck-returns.md](../build/2026-11-05-build-TOOL-dPlacedRequest-1-crosscheck-returns.md) | research | TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5 |
| [2026-11-05-build-TOOL-dPlacedRequest-1-parents-crosscheck.md](../build/2026-11-05-build-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5 |
| [2026-11-05-build-TOOL-dPlacedRequest-1-reground-returns.md](../build/2026-11-05-build-TOOL-dPlacedRequest-1-reground-returns.md) | research | TOOL-dPlacedRequest-5 |
| [2026-11-19-build-TOOL-dPlacedRequest-1-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dPlacedRequest-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dPlacedRequest-1-design-notes.md](../build/2026-11-19-build-TOOL-dPlacedRequest-1-design-notes.md) | research | — |
| [2026-11-19-build-TOOL-dPlacedRequest-1-red-fix-5.md](../build/2026-11-19-build-TOOL-dPlacedRequest-1-red-fix-5.md) | red-fix | — |
| [2026-11-19-build-TOOL-dPlacedRequest-1-red-fix-6.md](../build/2026-11-19-build-TOOL-dPlacedRequest-1-red-fix-6.md) | red-fix | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-departures-build.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-departures-build.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-deviation-642.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-deviation-642.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-deviation-643.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-deviation-643.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-deviation-644.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-deviation-644.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-deviation-645.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-deviation-645.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-red-fix-46.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-red-fix-46.md) | red-fix | — |
| [2026-11-21-build-TOOL-dPlacedRequest-1-red-fix-47.md](../build/2026-11-21-build-TOOL-dPlacedRequest-1-red-fix-47.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-1-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-1-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-10-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-10-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-11-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-11-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-12-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-12-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-2-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-2-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-3-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-3-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-4-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-4-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-5-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-5-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-6-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-6-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-7-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-7-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-8-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-8-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-9-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-9-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-owner-review-until-no-high.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-owner-review-until-no-high.md) | research | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-34 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-26-prompt-TOOL-dPlacedRequest-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dPlacedRequest-1-parents-reground.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-34 |
| [2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 |
| [2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-reground.md](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-reground.md) | research | TOOL-dPlacedRequest-5 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-1-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-1-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dPlacedRequest-1-asks-adopt-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-1-asks-adopt-brief.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-20 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

One lease mechanism serves every holder: a build, a unit of a build, and a cadence run, each a ref
on the remote written by compare-and-swap, each carrying an epoch that rises at every take-over, and
the unattended run claim migrated onto it so one mechanism remains (coordination.md:79-101). Today
only runs are claimed (`refs/gov/runs/<slug>`, `tools/unattended/unattended.sh:2087`); a claim names a
user, not a fleet tag (`:2410`), carries no epoch, covers no unit (gap-conc-01, gap-conc-02); overlap is
a probe that "always returns 0" (`check_cross_run_overlap`, `:3409`); and an unreachable remote is only
announced (`:2141-2149`).

## 2. Scope (IN)

- **S1** — The grammar (I5): `refs/gov/leases/<slug>/build`, `refs/gov/leases/<slug>/unit/<id>` and
  `refs/gov/leases/run/<cadence>/<period>`, built only by `derive_lease_ref <kind> <name> [<sub>]`,
  each segment held by `check_lease_segment` to a legal one-segment ref name. `<cadence>` takes any
  legal segment here; `TOOL-dPlacedRequest-18` narrows it to the tag grammar (I7). Observed by AC1.
- **S2** — The record (I6), `record-kind.lease`: the commit `TOOL-dPlacedRequest-11`'s
  `build_gov_commit` builds, parented on the tip read, its message `gov-claim <tail>` (the ref after
  `refs/gov/leases/`), a blank line, today's eight keys (`unattended.sh:2411-2412`) and `epoch`,
  `kind`, `fleet-tag`, `renews`, `witness`, `offer`, `offer-deadline` and `last-fetch`, the last three
  `-` until `TOOL-dPlacedRequest-16` and `TOOL-dPlacedRequest-20` fill them. `read_claims` (`:2118`)
  stays the one parser, validating the header, `slug`, a positive `epoch` and `kind` against the ref,
  and `CLAIM_ROWS` grows from eleven TAB fields to eighteen. Observed by AC1 and AC2.
- **S3** — The epoch: a create writes 1; a take or an announced take of a foreign lease writes the
  read epoch plus one; every other write keeps it. A record with no `epoch` reads 0. Observed by AC2.
- **S4** — The migration of run claims (I24): the driver's claim is the build lease
  `refs/gov/leases/<slug>/build`. `read_claims` fetches `refs/gov/leases/*` and the legacy
  `refs/gov/runs/*` in one bounded fetch, the lease row winning for a slug with both. The first write
  to a slug holding only a legacy claim parents the lease on the legacy tip at epoch 1, the legacy ref
  left in place. `RUN_CLAIMS` (`:671-676`) stays the dark-landing switch for every lease read and write.
  Observed by AC3.
- **S5** — The verbs: `unattended.sh --lease acquire|renew|release|take-over <kind> <name> [<sub>]`,
  with `--witness <sha>` on `renew` and `--as landed|aborted|withdrawn` on `release`. Each reads the
  remote's leases, derives its row through `check_claim_writable`'s table, which gains a `lease` mode
  (S6), writes through `write_gov_ref`, and prints one line: `lease — <tail> · <act> · epoch <n>`, or
  `lease refused — <cause> · <tail> · <holder>` with one cause word of I9 and exit 1, or `lease not
  written — <why>` with exit 2. `withdrawn` joins `landed` and `aborted` as a terminal status.
  `--lease` is declared on `VERBS_INLINE` with a header usage line, so check 26 of the unattended kit
  gate requires a `--lease` row in `tools/unattended/VERBS.template.md` and an `unattended.sh --lease`
  line in `tools/unattended/SKILL.template.md`. The skill render's size row has no headroom, so it is
  raised on its four terms by this unit's own figure, from the row `TOOL-dPlacedRequest-13` leaves.
  The usage line is the `docs` leg's member `verb:unattended.sh:--lease`
  (`tools/govkit/step_gate.py#VERB_SOURCES`), anchored in `help/loop.md` beside `--claims`. Observed by AC1, AC2, AC9, AC10 and AC13.
- **S6** — The `lease` mode, a column of `CLAIM_MODES` (`:2220`): a lease is `mine` when its
  `fleet-tag` and `session` are this node's and this harness's; `acquire` creates on none, renews on
  mine, and refuses `live-holder` on foreign live or held (naming `take-over` when stale) and
  `tombstone` on foreign terminal; `take-over` takes foreign stale, announced, and refuses the rest as
  `acquire` does. A lost compare-and-swap is `epoch-fence`. The full table is in the design record.
  The GH19 arm's `GC_CELLS` gains one `lease` row per `CLAIM_READS` class, typing its `acquire`
  cell. Observed by AC2, AC9 and AC19.
- **S7** — `leases.granularity` (`build-and-unit`, `build`, `unit`; default `build-and-unit`): `build`
  refuses `--lease acquire unit` and `unit` refuses `--lease acquire build`, each with exit 2 naming the
  key and its value; the driver's run claim is a build lease under every value. Observed by AC5.
- **S8** — `leases.renewal` (`progress`, `activity`, `fixed`, `none`; default `progress`) sets each
  write's `renews` and `witness`. Under `progress` a write renews only on a witness: a commit that
  resolves, records a transition of this build on the channel `transitions.record` selects
  (TOOL-dDeclaredLoop-3 S4, S7) and differs from the record's `witness`; any other write, a beat
  included, writes `renews: no`. `activity` renews on every write, `fixed` only at acquisition, and
  `none` writes `renews: -`, a lease `TOOL-dPlacedRequest-17` never expires. A declared wait also
  witnesses (§8 F9): a `--witness` naming a `question` mail commit to the build, `open` and inside its
  deadline by `check_mail_deadline`, renews even when it equals the record's `witness`, and once
  `expired` or answered renews nothing. `check_lease_witness <slug> <sha>` is the one witness check,
  its order of tests in the design record (§4). The record's `witness`, the differs test and the
  mailbox match all use the full sha `git rev-parse --verify --quiet <sha>^{commit}` prints, never
  the argument as typed. Observed by AC4, AC11 and AC12.
- **S9** — `leases.overlap` (`kit-dirs`, `files`, `builds`; default `kit-dirs`) and `leases` (`warn`,
  `refuse`; default `warn`) replace the probe's constant 0, as the design record's "The overlap
  reduction" states (§4). It runs at `--lease acquire` and where the driver calls it today (`:7492`).
  Under `warn` it prints and returns 0. Under `refuse` a finding returns 1 and the acquisition is refused `overlap`, and every
  UNAVAILABLE exit of the probe returns 1 too, refused `overlap` naming that line's cause: a probe that
  cannot run admits nothing. Observed by AC6 and AC14.
- **S10** — `leases.offline` (`warn`, `refuse`, `follow-leases`; default `warn`) when the read cannot
  reach the remote: `warn` builds the lease commit on the cached tip, records it in
  `<git-common-dir>/gov-queue.log` and prints `queued`; `refuse` refuses `offline`; `follow-leases`
  lets a renew of a held lease print `follow-leases` and write nothing, and refuses every acquisition
  and take-over `offline`. The queue holds one TAB line per write: ref, cached tip, commit,
  `queued-utc`. `--lease flush` and every later successful read push each line through `write_gov_ref`
  on its recorded tip, oldest first: rc 0 and rc 1 resolve the line, rc 1 printing `yield` with a
  `lease-yielded` health event, and rc 2 keeps it. `add_gov_queue` and `write_gov_queue` serve every later
  compare-and-swap writer of this build. No value creates a ref while offline. Observed by AC7.
- **S11** — Fleet identity and uniqueness: `resolve_fleet_tag` asks the playbook kit's one fleet
  reader, `read_fleet` (`tools/playbook/render_playbook.py:347`), through a new `--fleet-tag --user
  <u> --host <h>` flag, for the row matching this node; a node with none is refused with exit 2 naming
  `fleet.toml` before any write. `CLAIM_ROWS`' field 1 is the lease's name (`<slug>` for a build
  lease) and field 2 its `fleet-tag`; a legacy `refs/gov/runs/*` record, which has no such key, keeps
  its `node` there. `print_claims` still prints fields 1 to 5 without `--with-key`, and the header's
  `--claims [--with-key]` usage line (`tools/unattended/unattended.sh@875eaadf:43`) and the verbs
  guide's `--claims` row name the column `node or fleet tag`. `derive_claim_keys`
  (`tools/unattended/unattended.sh#derive_claim_keys`), the `--with-key` reader, keys a legacy row over
  `refs/gov/runs/<slug>@<sha>` and a lease row over `refs/gov/leases/<tail>@<sha>`, built by
  `derive_lease_ref`, its `runstate=` read from the row's `slug`, `?` for a cadence lease. A build lease create is a slug's remote
  uniqueness check: of two nodes creating one, one wins and one reads `epoch-fence`. Observed by AC8,
  AC9, AC15 and AC18.
- **S12** — The four keys and `leases` are read once per process each by `read_lease_policy`, built on
  `read_spec_audit_switch`'s pattern (`tools/unattended/unattended.sh#read_spec_audit_switch`): the
  policy kit found by `resolve_kit_dir`, a closed `case` over the five keys, and one literal
  `"$py" "$d/policy.py" get <key>` line per key, which `check_policy.py`'s reader coverage counts. It
  copies the seam's rule too: only an unresolved policy kit reads the default, with one NOTE naming
  the key; a refused `get`, an invalid file included, returns 1 and `run_lease_verb` prints `lease not
  written — <key> refused`, exits 2 and writes nothing. The rows are dGroundRules-1 S3's. Observed by AC4, AC5, AC16
  and AC17.
- **S13** — The stops guide's section 7 (`tools/unattended/STOPS.template.md:187-245`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) states the grammar, the record, the epoch, the `lease` column,
  the verbs, the four keys and the refusal causes `[rules]` routes. Observed by AC10.

## 3. Non-goals (OUT)

- No expiry by a declared clock: the age stays the reader's clock against `beat-utc` (`:2177-2186`)
  until `TOOL-dPlacedRequest-17`.
- No hand-over, tombstone, queued-claim age or prune: `TOOL-dPlacedRequest-16`'s.
- No offer: `offer` and `offer-deadline` are `-` until `TOOL-dPlacedRequest-20`.
- No step-checklist caller: later builds' items call S5's verbs; `entry.claim`'s lease is
  `TOOL-dPlacedRequest-21`'s.
- No mailbox notice of an overlap or a take-over: dKeptSession's.
- No record-kind factory: dConvergedCharter's registers `record-kind.lease` from S2's grammar.
- No ask-id mint: other compare-and-swap mints apply `leases.offline` through S10's queue functions
  when they land.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref` and `build_gov_commit`, through which every lease write lands parented on the tip read
- **hands-off** `TOOL-dPlacedRequest-17` — `refs/gov/leases/<slug>/build` and the `renews` and `witness` fields, whose expiry the observer clock judges
- **hands-off** `TOOL-dPlacedRequest-16` — `refs/gov/leases/<slug>/build`, the `epoch` and the `last-fetch` field, which the hand-over, the tombstone and the queued-claim age rule extend
- **hands-off** `TOOL-dPlacedRequest-20` — `refs/gov/leases/<slug>/build`, the `epoch` and the `offer` fields, which acquisition with an offer extends
- **hands-off** `TOOL-dPlacedRequest-18` — `refs/gov/leases/<slug>/build` and `derive_lease_ref`, whose cadence segment that unit narrows to the tag grammar
- **hands-off** `TOOL-dPlacedRequest-15` — `refs/gov/leases/<slug>/build`, the lease tip the fenced effect push carries a beat on
- **hands-off** `TOOL-dPlacedRequest-19` — `refs/gov/leases/<slug>/build`, the grammar a request record's lease is acquired by, and the offline queue it applies
- **hands-off** `TOOL-dPlacedRequest-21` — `refs/gov/leases/<slug>/build` and the refusal causes, which `entry.claim` routes, and the offline queue it applies
- **hands-off** `TOOL-dPlacedRequest-4` — `refs/gov/leases/<slug>/build`, the lease `placement.check` reads for `continue` and `amend`
- **hands-off** external — dKeptSession's presets, which cannot set `leases` beside a `leases.*` key (TOOL-dGroundRules-1 §8 F5), and its mailbox's overlap and take-over notices
- **consumes-from** external — dKeptSession, a child build: `read_mailbox` (KICK-dKeptSession-5 S6, S7) and `check_mail_deadline` (KICK-dKeptSession-24 S3, S5), which arm the question witness (§8 F9)
- **hands-off** external — KICK-dKeptSession-25 S4's beat, which passes a question's commit as `--witness` and re-plants AC11 on real mail
- **hands-off** `TOOL-dPlacedRequest-23` — `run_lease_verb` and `leases.offline`'s offline branch, which that unit keeps out of every strict claim read
- **hands-off** `TOOL-dPlacedRequest-24` — `add_gov_queue`, `write_gov_queue` and `gov-queue.log`, which that unit puts under a node lock and makes idempotent
- **hands-off** `TOOL-dPlacedRequest-25` — the lease writer's `renews` decision, which that unit derives so a write opening a tenure renews, and S8's question witness, its third verdict
- **hands-off** `TOOL-dPlacedRequest-26` — the record's `epoch` and `renews` keys, which mark the tenure that unit's walk stops at
- **hands-off** `TOOL-dPlacedRequest-29` — the record's `epoch`, `fleet-tag` and `session` and the `lease` mode, which decide that unit's same-holder re-fence
- **hands-off** `TOOL-dPlacedRequest-32` — the `lease` mode's `mine` test and the `--lease` verbs, which that unit closes to an absent session
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-40` — `--lease flush`, which that unit exempts from the id-less refusal so a sessionless flush drains the queue
- **hands-off** `TOOL-dPlacedRequest-41` — the offline branch and `acquire` renewing on `mine`, which that unit rebases and dedupes
- **hands-off** `TOOL-dPlacedRequest-42` — the offline branch's empty-tip create, which that unit routes through `read_feed_lease_tip`
- **hands-off** `TOOL-dPlacedRequest-43` — the queue line's tip field and `resolve_fleet_tag`, which that unit's items encode and align

## 4. Design

The record's worked example, the `lease` mode's full table, the witness under `progress` and the
question witness's order of tests, the policy reads, the overlap reduction, the migration, the
rollout and the alternatives rejected are in the design record
`memory/builds/dPlacedRequest/build/2026-11-19-build-TOOL-dPlacedRequest-1-design-notes.md`, moved
there to hold this spec under the 49152-byte ceiling (48574 bytes at rev-8, PINNED 2026-11-19);
`TOOL-dPlacedRequest-43` S22 cuts it over 48128 after each render.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_lease_ref` | shell function | `derive`, OK |
| `check_lease_segment` | shell function | `check`, OK |
| `resolve_fleet_tag` | shell function | `resolve`, OK |
| `read_lease_policy` | shell function | `read`, OK |
| `check_lease_witness` | shell function | `check`, OK |
| `run_lease_verb`, the verb's body | shell function | `run`, OK |
| `add_gov_queue`, `write_gov_queue` | shell functions | `add` and `write`, OK |
| `--lease`, `--lease flush` | driver verbs | none |
| `--fleet-tag` | render_playbook.py flag | none |
| `gov-queue.log` | node-local file | none |
| `lease-yielded` | health event | none |
| `lease` | `CLAIM_MODES` member | graded by leg check 52 |
| `withdrawn` | claim status value | none |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: every item but S11's flag and S13's guide; the kit version is
  minted by the lander (TOOL-aMendedFleet-65; TOOL-dPlacedRequest-34 S59)
- `tools/unattended/lib-unattended.sh`: `resolve_fleet_tag` beside `resolve_index_generator` (`:188`),
  through the same `resolve_kit_dir` call
- `tools/unattended/unattended.test.sh`: the lease arms, `GC_CELLS`' `lease` rows, and the claim
  fixtures moved to the lease ref
- `tools/unattended/STOPS.template.md`: section 7
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/unattended/VERBS.template.md`: the `--lease` row, and the `--claims` row's column name
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `tools/unattended/SKILL.template.md`: an `unattended.sh --lease` line in the fenced verb list
- `.claude/skills/unattended/SKILL.md`: its render
- `tools/template-size-limits.txt`: the `.claude/skills/unattended/SKILL.md` row, raised (S5)
- `memory/DECISIONS.md`: the raise's row, its term 4
- `tools/playbook/render_playbook.py`: the `--fleet-tag` flag over `read_fleet`
- `skills/session-kickoff/manifest-check.sh`: `derive_claims_line`, the `claims —` cell reading
  `--claims --with-key`'s six fields, unchanged in shape
- `skills/session-kickoff/manifest-check.test.sh`: a lease row beside `seed_claim`'s legacy row, and
  TOOL-dDeclaredLoop-8 AC8's field-6 arm (`skills/session-kickoff/manifest-check.test.sh@3eaf707d:2066`)
- `help/loop.md`: the `--lease` usage anchor (S5)
- `memory/map/generated/`: `gen_map.py --write` in this unit's pass, for the functions it mints;
  `TOOL-dPlacedRequest-34` S38 only re-checks
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

## 5. Production-readiness checklist

- security — every write is a compare-and-swap on the tip read; the record names a fleet tag and a
  session, never a credential; a node outside the fleet writes nothing.
- perf / scale — one bounded fetch and one `awk` pass per read, as today; one `get` per key.
- error / empty / loading states — a refusal names one cause and the holder; an unanswered read
  follows `leases.offline`; an absent policy kit prints a NOTE and the default, and a refused key
  refuses the verb, writing nothing.
- observability — every verb prints one line naming the tail, the act and the epoch; a take-over and a
  yield append a health event.
- risks — under `progress` a run lease renews only on a recorded transition, which nothing records
  until dWellOiledMachine lands, so a run with none reads stale once unit 17 judges expiry (§8 F5).
- testing — the probes of §6, and the suite arms of §7.
- migration — lazy, per slug, at its next write.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7, the verbs guide's `--lease` row and
  `help/loop.md`'s `--lease` anchor, beside the driver's other verbs.

## 6. Acceptance criteria

- **AC1** — When `--lease acquire build tFix`, `--lease acquire unit tFix TOOL-tFix-2` and `--lease
  acquire run maintain 2026-10` run in a fixture clone, the origin holds the three refs S1 names, each
  message opening `gov-claim <tail>` with `epoch: 1`, its `kind` and `fleet-tag: a`; `--lease acquire
  build 'a b'` exits 2 and writes nothing.
  Red when: a ref is built outside `derive_lease_ref`, or an illegal segment reaches a push.
  fixture: a scratch clone with a bare origin whose `HEAD` is set, the kit's example conf with
  `RUN_CLAIMS=on`, and `USERNAME=daily-agent`.
- **AC2** — When session `s2` runs `--lease take-over build tFix` over a planted stale lease, the origin's
  lease reads `epoch: 2` and its parent is the planted tip; `--lease acquire build tFix` by `s3` then
  exits 1 printing `lease refused — live-holder`.
  Red when: a take-over keeps the epoch, or a live lease is acquired.
- **AC3** — When the fixture origin holds only a legacy `refs/gov/runs/tFix` claim, `--claims` prints
  one five-field row for `tFix`; after the run's next holder write, `refs/gov/leases/tFix/build` reads
  `epoch: 1` parented on the legacy tip, the legacy ref is unchanged, and `--claims` prints one row.
  Red when: both rows print, the legacy ref moves, or the lease starts a new chain.
- **AC4** — When no policy file exists and `--lease renew build tFix` runs without `--witness`, the
  record reads `renews: no`; with `--witness` naming a commit carrying `Gov-Transition: … build=tFix`,
  `renews: yes` and that `witness`; the same witness again, `renews: no`; a witness recording no
  transition of `tFix` exits 2. With `transitions.record` planted `["log"]`, a witness that added
  `tFix`'s `-transition-1.md`, no trailer, reads `renews: yes`. With `leases.renewal` planted
  `activity`, `fixed` and `none`, a renew without a witness reads `yes`, `no` and `-`. A renew with
  the transition witness's 7-character prefix, after a renew with its full sha, reads `renews: no` and
  `witness: <full sha>`.
  Red when: a beat alone renews under the default `progress`, a planted value is not read, a
  log-only transition never renews, or a short sha is stored or compared as typed.
- **AC5** — When `leases.granularity` is planted `build`, `--lease acquire unit tFix TOOL-tFix-2` exits
  2 naming `leases.granularity`; planted `unit`, `--lease acquire build tFix` exits 2; under the default
  both write.
  Red when: a planted value admits the level it excludes.
- **AC6** — When the fixture origin holds a branch whose spec declares one script in a planted scratch
  kit directory under the tools root and this build's spec declares a second there, `--lease acquire
  build tFix` prints an `overlap` finding under the default `kit-dirs` and none under planted `files`;
  with `leases` planted `refuse` it exits 1 printing `lease refused — overlap`; with the path made
  equal and `builds` planted, one finding names the branch. A second branch touching only
  `memory/builds/<its own slug>/` draws no `kit-dirs` finding.
  Red when: the probe returns 0 under `refuse`, a granularity value is not applied, or two build
  folders join on `memory`.
- **AC7** — When the origin is renamed away and `--lease acquire build tOff` runs, it exits 0 printing
  `queued`, `gov-queue.log` holds one line and `git for-each-ref refs/gov/leases` lists nothing new;
  restored, `--lease flush` creates the ref and empties the queue, or after a conflicting write prints
  `yield`. Under planted `refuse` the offline acquire exits 1 printing `offline`; under
  `follow-leases` a held lease's renew prints `follow-leases` and an acquire exits 1.
  Red when: an offline call writes a ref, or a queued write overwrites a conflicting one.
- **AC8** — When `USERNAME` names no `fleet.toml` row, `--lease acquire build tFix` exits 2 naming
  `fleet.toml` and the origin is unchanged; with `daily-agent`, `--claims` prints `a` in the node column.
  Red when: a node with no tag writes a lease, or the row names a user.
- **AC9** — When two clones whose caches both read no lease run `--lease acquire build tNew` one after
  the other without a fetch between, the first exits 0 and the second exits 1 printing `epoch-fence`.
  Red when: both report a create.
- **AC10** — When `grep -n 'refs/gov/leases/<slug>/build\|--lease\|leases.renewal\|epoch-fence'` runs over
  `STOPS.template.md`, each is found in section 7, and AC1's `--claims` rows hold five TAB fields.
  Red when: the guide omits the grammar or the verbs, or the row shape changes.
- **AC11** — When the AC4 fixture plants `Q=$(git commit-tree -m question "$(git rev-parse
  'HEAD^{tree}')")`, a commit with no transition, exports by `export -f` a stub `read_mailbox` printing
  one `question` row to `tFix`, state `open`, commit `$Q`, and a stub `check_mail_deadline`, and runs
  `--lease renew build tFix --witness "$Q"` twice, both records read `renews: yes` and `witness: $Q`.
  With the row `expired`, the renew exits 0 with `renews: no` and the prior `witness`. With no stub it
  exits 2. With a row naming a 40-hex sha the clone lacks, as `--witness`, it exits 2, writing nothing.
  Red when: a held question renews once only, an expired one renews, one renews with dKeptSession's
  functions absent, or an unresolvable sha passes.
  fixture: the stubs stand in for KICK-dKeptSession-5's and KICK-dKeptSession-24's functions.
- **AC12** — When the AC11 stub `read_mailbox` prints the row `open` on its first call and `expired`
  after, and `check_lease_witness tFix "$Q"` then `--lease renew build tFix --witness "$Q"` run, the
  probe prints `question` and exits 0, and the renew exits 0 with `renews: no`. A bounded probe
  outside the waived suite sources `unattended.sh` with the stubs and prints AC11's two `renews` lines.
  Red when: the renew exits 2 and the beat writes no record, or the direct probe prints no
  `renews: yes`.
- **AC13** — When `grep -c -- '^- `--lease` — ' tools/unattended/VERBS.template.md`,
  `grep -c 'unattended.sh --lease ' tools/unattended/SKILL.template.md` and
  `grep -c '^#   unattended.sh --lease' tools/unattended/unattended.sh` and
  `grep -c 'usage: verb:unattended.sh:--lease ' help/loop.md` run, each prints at least 1, and
  `tr -d '\r' < .claude/skills/unattended/SKILL.md | wc -c` prints at most the figure
  `awk -F'\t' '$1==".claude/skills/unattended/SKILL.md"{print $2}' tools/template-size-limits.txt`
  prints.
  Red when: a carrier check 26 or the `docs` leg joins lacks the verb, or the skill render is over
  its row.
- **AC14** — When the AC6 clone's `refs/remotes/origin/HEAD` is deleted and `leases` planted `refuse`,
  `--lease acquire build tFix` exits 1 printing `lease refused — overlap` and the UNAVAILABLE cause,
  writing no lease; under `warn` it exits 0 printing the UNAVAILABLE line.
  Red when: a probe that cannot run admits the lease under `refuse`, or prints `NOT blocked` there.
- **AC15** — When the AC3 fixture origin holds a legacy `refs/gov/runs/tOld` claim whose `node` is
  `n1` and a lease `refs/gov/leases/tFix/build` whose `fleet-tag` is `a`, `--claims` prints field 2 as
  `n1` for `tOld` and `a` for `tFix`, five fields each.
  Red when: a legacy row prints an empty or shifted field 2.
- **AC16** — When `python -c "import sys; sys.path.insert(0, sys.argv[1]); import check_policy; k = check_policy.scan_reader_keys(sys.argv[2]); print(sorted(x for x in k if x.split('.')[0] == 'leases'))" tools/policy .`
  runs at the repository root over the built tree, the four `leases.*` keys of S7 to S10 are among
  what it prints, and each `leases` key a `case` arm of the `read_lease_policy` cut names has its own
  literal `get` line there, so it holds as units 17 and 20 add keys.
  Red when: a key is passed to `get` in a variable, which reader coverage reads as unread.
- **AC17** — When a fixture plants a `.governance/policy.toml` setting `leases` to `refuse` above a
  line that does not parse, `--lease acquire build tFix` exits 2 printing `lease not written` and the
  refused key, the origin unchanged; with the policy kit hidden, it prints one NOTE and reads the
  default.
  Red when: an invalid policy file reads the catalogue default, so `refuse` reads `warn` and writes.
- **AC18** — When the AC15 fixture runs `--claims --with-key`, the `tFix` row prints six fields, its
  sixth equal to `claims.py key` over `refs/gov/leases/tFix/build@<sha>`, and `tOld`'s keyed over
  `refs/gov/runs/tOld@<sha>`.
  Red when: a lease row is keyed over the runs namespace.
- **AC19** — When a probe compares `CLAIM_READS` by `CLAIM_MODES` in `unattended.sh` with the cells
  `GC_CELLS` types, by `comm -3` as the GH19 arm does, it prints nothing; `CLAIM_MODES` names
  `lease`.
  Red when: a class has no typed `lease` cell.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `unattended skill size` · `check-wiring self-test` · `manifest-check self-test` · `scratch-guard self-test` · `playbook render selftest` · `govkit acceptance matrix` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `routed-commits selftest` · `govkit selftest` · `govkit refusal join` · `tier2-review self-test` · `policy fixtures` · `docs` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC14 AC17 AC19 · the `GC_CELLS` `lease` rows and the lease arms, staged by planting each policy value, cutting the epoch increment and unsetting the tracking HEAD under `refuse` · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count · waived by README rule 8, its clean reading owed with PLAY-dClosedLoop-14; AC12's direct probe observes it at landing
New arm: tools/playbook/render_playbook.py · covers AC8 · the `--fleet-tag` flag's selftest case, staged by a user no row names · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC15 AC18 · a lease row seeded beside `seed_claim`'s legacy row, staged by a reader printing the `fleet-tag` key alone and by a key derived over the runs namespace · none

## 8. Open questions

Each fork's options and the reasons each lost are in the design record (§4), moved there whole; the
picks and their marks stay here.

- **FACT-QUESTION · F1 — Is the brief's status token `DRAFT` legal?** Probe: `STATUS_TOKENS` at
  `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: the tuple lacks `DRAFT`. Liveness: the
  tuple would show `DRAFT` if the vocabulary held it. RESOLVED (agent, 2026-10-25,
  delegated): `OPEN`, rung 2.
- **F2 — Does the migration retire `RUN_CLAIMS`?** RESOLVED (agent, 2026-10-25, delegated): (a), keep
  it as the switch every lease read and write sits behind, rung 3. widens: none · relaxes: none
- **F3 — How do run claims migrate?** RESOLVED (agent, 2026-10-25, delegated): (a), lazily, the reader
  reading both namespaces and the first write parenting the lease on the legacy tip, rung 3.
  widens: none · relaxes: none
- **F4 — Which lease does a run hold under `leases.granularity: unit`?** RESOLVED (agent, 2026-10-25,
  delegated): (a), the build lease always, the key governing the checklists' acquisitions, rung 3.
  widens: none · relaxes: none
- **F5 — What witnesses progress for a run lease before any caller records a transition?** RESOLVED
  (agent, 2026-10-26, delegated): (a), only a recorded transition of the build, rung 1,
  TOOL-dDeclaredLoop-3 S4 and S7 at `783f1ad3a`; its risk is in §5. widens: none · relaxes: none
- **F6 — What do `fixed` and `none` mean, which v2 names without defining?** RESOLVED (agent,
  2026-10-25, delegated): `fixed` renews only at acquisition; `none` never expires; rung 3.
  widens: none · relaxes: none
- **F7 — How do the three `leases.overlap` values reduce a path?** RESOLVED (agent, 2026-10-25,
  delegated): as the design record's "The overlap reduction" states (§4), rung 3. widens: none · relaxes: none
- **F8 — How does the bash driver read a log-only transition, when `read_transitions` is a Python
  function with no verb?** RESOLVED (agent, 2026-10-26, delegated): (a), the driver reads the selected
  channel with two `git` calls, held to TOOL-dDeclaredLoop-3's source table by AC4's `["log"]` plant,
  rung 3. widens: none · relaxes: none
- **F9 — The question witness (S8) rests on dKeptSession, a child build landing after this unit; how
  is it built here?** RESOLVED (agent, 2026-11-19, delegated): (a), the branch built here, armed only
  when `declare -F` finds `read_mailbox` and `check_mail_deadline`, observed on exported stubs (AC11)
  and inert until dKeptSession lands, rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 1, scout A row 1 and Shared interfaces 1,
  4 and 8, coordination.md:79-101, v2:1157-1162 and flow-steps:53-60.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: AC6 describes the overlap fixture's two planted
  scripts in prose, so no untracked path reads as a repository path; §3 gains the hands-off to
  TOOL-dPlacedRequest-4 that unit's consumes-from names.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-23,
  hands-off TOOL-dPlacedRequest-24, hands-off TOOL-dPlacedRequest-25, hands-off
  TOOL-dPlacedRequest-26, hands-off TOOL-dPlacedRequest-29, hands-off TOOL-dPlacedRequest-32,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirrors
  hands-off TOOL-dPlacedRequest-40, hands-off TOOL-dPlacedRequest-41, hands-off
  TOOL-dPlacedRequest-42, hands-off TOOL-dPlacedRequest-43.
- rev-5 · 2026-10-26 · §2 S8 · §4 The witness under `progress` · §6 AC4 · §8 F5, F8 · re-grounded on
  dDeclaredLoop at `783f1ad3a` by the cross-check record
  `build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`, row 2: the witness is a
  recorded transition on the channel `transitions.record` makes the source, the log record where
  `trailer` is not selected.
- rev-6 · 2026-11-19 · §2 S8 · §3 Edges · §4 The witness under `progress`, The question witness,
  Inventory · §6 AC11 · §7 · §8 F9 · §10 · adopts ask TOOL-dPlacedRequest-67 per the brief
  `2026-11-19-prompt-TOOL-dPlacedRequest-1-1-spec-writer`: an open `question` to the build inside its
  deadline witnesses a renewal (F9 resolved (a)); §7 gains the two legs the spec-token guard join names.
- rev-7 · 2026-11-19 · §2 S8 · §3 Edges · §4 The question witness, Files touched · §6 AC11, AC12 · §7 ·
  §10 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`: findings 1 and 23 (item H1), the hands-off to TOOL-dPlacedRequest-25 names the
  question-witness branch; finding 24 (H6), the kit version is the lander's to mint; finding 4 (M3), the
  unattended.test.sh arm cites README rule 8 and AC12 adds a direct probe; finding 11 (M5), the check
  resolves the sha after the mailbox fetch and before it classifies, and AC11 plants `Q`; finding 12
  (L3), a question closed between the probe and the renew answers `question-closed` and writes
  `renews: no`; finding 14 (L5), §10 quotes where the probe found `check_mail_deadline`.
- rev-8 · 2026-11-19 · §2 S2, S5, S6, S8, S9, S11, S12 · §3 · §4 · §5 · §6 AC6, AC13 to AC16 · §7 · §8 ·
  §10 · folds `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 26 (H2), `kit-dirs`
  reduces kit and skill paths only, AC6's build folders must not join; finding 27 (H3), the acquire's
  anchor and slug are named and an UNAVAILABLE probe refuses under `refuse` (AC14); finding 16 (M4),
  `read_lease_policy` copies `read_spec_audit_switch` (AC16); finding 18 (M6), `--lease`'s check-26
  carriers and the skill row's raise (AC13); finding 22 (M10), a legacy row keeps `node` in field 2
  (AC15); finding 24 (L10), §4's long sections and §8's option analyses moved to the design record.
- rev-9 · 2026-11-19 · §2 · §4 · §5 · §6 · §7 · §8 · §10 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: findings 10 (H1), 7 (M3), 15 (M6), 16 (M7),
  17 (M8), 22 (M10), 4 (L1) and 14 (L5); §4's policy reads and overlap reduction moved to the design
  record.

## 10. Reuse audit

The policy reader's seam is `read_spec_audit_switch` (`tools/unattended/unattended.sh#read_spec_audit_switch`),
whose literal `get` lines S12 copies. The seam extended is the run-claim block,
`tools/unattended/unattended.sh:2070-2462`: `read_claims` (`:2118`) stays the one reader,
`check_claim_writable`'s table (`:2243`) gains the `lease` column, and writes go through
`TOOL-dPlacedRequest-11`'s `write_gov_ref`; the overlap's and the fleet tag's seams are S9's and S11's.
`python tools/codebase-map/reuse_lookup.py "lease a build or unit on the remote with an epoch and take
over"` ranked `build_commit`, `units`, `build_fixture` and `resolveLease` (the run-state lease on the
run's own branch); none writes a remote ref, so the claim block is the seam. `python
tools/memory-recall/query.py "how are run claims written and how would they migrate to leases"`
returned scout A's rows 1 and 6, the brief's unit rows and coordination.md:54, the design record
naming where scout A disagreed with source. `git grep -l check_mail_deadline` at `6e9c6062` finds it
in no file under tools/ or skills/.

Recall terms used: lease epoch take-over refs/gov/leases run claim migrate fleet tag overlap offline renewal progress
