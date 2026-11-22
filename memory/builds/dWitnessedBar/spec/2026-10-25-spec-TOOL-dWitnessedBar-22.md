# TOOL-dWitnessedBar-22 — the `tests=` and `enforces=` edge fields on legs

**Status:** CLOSED · rev-5 · 2026-11-19 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 6 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0360@f873b4dc whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-fix-return.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-11-19-build-TOOL-dWitnessedBar-22-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-22-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-22-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-22-1-builder-return.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-22-deviation-221.md](../build/2026-11-19-build-TOOL-dWitnessedBar-22-deviation-221.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-22-red-fix-26.md](../build/2026-11-19-build-TOOL-dWitnessedBar-22-red-fix-26.md) | red-fix | — |
| [2026-11-19-build-TOOL-dWitnessedBar-22-red-fix-27.md](../build/2026-11-19-build-TOOL-dWitnessedBar-22-red-fix-27.md) | red-fix | — |
| [2026-11-19-build-TOOL-dWitnessedBar-22-red-fix-28.md](../build/2026-11-19-build-TOOL-dWitnessedBar-22-red-fix-28.md) | red-fix | — |
| [2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md](../build/2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-22-2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-22-2-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-22-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-22-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-22-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-22-reground-brief.md) | journal | TOOL-dWitnessedBar-19 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-22-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-22-reground-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-22-spec-fix-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-22-spec-fix-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-54 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

Declare on each leg's own row what the leg tests and which principles or practices it enforces, and
read both as typed edges of the one closed edge set, so the facts "this leg tests that feature" and
"this leg enforces that principle" are declared once, where the leg lives, and every inverse is
derived (night pass, point 4: `night-pass.md:250`). Today no leg carries `tests`, and 51 of the 198
manifest rows carry `enforces` (PINNED 2026-11-19 at `a4cffc2cb`), the key PLAY-dOrderedCharter-7
landed and its meta-check `tools/playbook/core.py` reads, which no edge site reads as an edge; the
feature-to-leg fact lives only in the dossiers' `gate-legs` claims.

## 2. Scope (IN)

- **S1** — The row key `tests` (shared interface I1): a list of tags, each a thing the leg tests.
  Written once at the pass from the dossiers' claims, per §4 "The `tests` values", on each manifest
  row of `tools/gate-legs.json` and on its descriptor `[[gate_leg]]` row; declared there thereafter.
  Observed by AC1.
- **S2** — The row key `enforces`, PLAY-dOrderedCharter-7 S2's, landed: a list of `principle.*` or
  `practice.*` tags. This unit makes it an edge field read at the leg row; the values for every leg
  are TOOL-dWitnessedBar-11's and TOOL-dWitnessedBar-24's to write. Observed by AC3.
- **S3** — `LEG_KEYS` (TOOL-dWitnessedBar-12's one key set) gains `tests`. `enforces` is in both
  `KNOWN` copies of `tools/run-gates/run-gates.test.sh` at `a4cffc2cb`, put there by
  PLAY-dOrderedCharter-50 S1, and in the `LEG_KEYS` value TOOL-dWitnessedBar-12 §4 writes, so it is
  not added twice. Observed by AC2.
- **S4** — The leg-row site of the edge grammar: one adapter `read_leg_edges(text, path)` in
  `tools/playbook/edge_grammar.py`, a site beside PLAY-dOrderedCharter-28 S5's, read by
  `tools/playbook/edge_grammar.py#read_tree_edges` over `tools/gate-legs.json` and by
  `tools/playbook/edge_grammar.py#read_site_edges` for a file named `gate-legs.json`, and named in the
  module docstring's THE SITES paragraph, yielding per row a `tests` edge and an `enforces` edge from
  the row's `tag` to its values, typed and resolved as every site's edges are (§4 "The edge read").
  `tools/playbook/edge_grammar.py#check_edges`, which each caller hands its namespace registry, marks
  two kinds of leg-row target `unarmed`, counted and printed, never red and never resolved: a `tests`
  target in a namespace no registry row holds, and an `enforces` target in the rule-member form
  `practice.<practice>.<rule>`, which `core meta-check` grades (§8 F6, F7). Observed by AC3, AC4
  and AC7.
- **S5** — The both-ways compare in `tools/run-gates/run-gates.gov.test.sh`: a leg whose row
  carries `feature.<f>` in `tests` is claimed by the dossier whose `feature` is `<f>`, and a leg a
  dossier claims carries that dossier's tag in `tests`. The dossiers are read, never edited.
  Observed by AC5.
- **S6** — govkit selfcheck 7h's both-ways join (`tools/govkit/govkit.py#selfcheck`, its `7h`
  block) gains `tests` and `enforces`, presence included: a descriptor row and its manifest row carry
  the same lists. The descriptor-claimed legs whose manifest row carries `enforces` and whose
  descriptor row does not (6, PINNED 2026-11-19 at `a4cffc2cb`, §4 "The `enforces` copies") gain the
  manifest's list on their descriptor row at the pass (§8 F5). Observed by AC6.

## 3. Non-goals (OUT)

- The `enforces` key's creation and its meta-check: PLAY-dOrderedCharter-7 S2 and S3. The value
  "every leg declaring the principles it enforces" is TOOL-dWitnessedBar-11's; the portability
  pack's values are TOOL-dWitnessedBar-24's.
- The edge registry, the parser and the resolver: PLAY-dOrderedCharter-24, -28 and -19. The tag
  index resolving the rule-member form a practice row's `rules` admit is the ask §8 F6 names.
- The dossiers' `[claims] gate-legs` lists and the `feature` namespace: the map's and dTotalRecall's.
  This unit compares against them and edits none; making the dossier side derived from `tests` is
  the ask named in §8 F2.
- Carrying `tests` or `enforces` into an adopter's manifest: neither travels (§8 F4), so
  `LEG_KEY_FLOORS` gains no row for them.
- Reading a leg's own files from its `tests` edge: TOOL-dWitnessedBar-21's (shared interface I15).

### Edges

- **consumes-from** `TOOL-dWitnessedBar-12` — `tag`, the leg's address every edge this unit reads
  starts from, its `leg.<owner>.<name>` member the form a `tests` target and an `enforces` row's leg
  are spelled in, and `LEG_KEYS`, where the key is admitted
- **hands-off** `TOOL-dWitnessedBar-11` — `enforces`, the edge field the leg factory emits from each
  pack's declaration and whose values for every leg it writes
- **hands-off** `TOOL-dWitnessedBar-24` — `enforces`, the field its portability legs fill with
  `practice.portable.*` tags
- **hands-off** `TOOL-dWitnessedBar-21` — `tests`, the edge a leg's own files are read through
- **consumes-from** external — PLAY-dOrderedCharter-7 S2 (the `enforces` key),
  PLAY-dOrderedCharter-24 (the `tests` and `enforces` edge rows) and -28 S5 (the site table)
- **hands-off** external — dTotalRecall: registering the `feature` namespace, which arms the
  `tests` edges' resolution, and deriving the dossiers' `gate-legs` claims from them
- **hands-off** external — dOrderedCharter: the tag index resolving a practice row's rule members,
  after which the leg-row mark on them is deleted (§8 F6)
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 12 and 41: `fix_keeps.py` keeping no `tests` target, and the row hash dropping the `tests` and `enforces` keys, each a scope item of that unit

## 4. Design

### The `tests` values

At `a4cffc2cb`, 180 of the 198 legs are claimed by exactly one of the 33 dossiers (PINNED 2026-11-19)
under `memory/map/features/`, in its `[claims] gate-legs` list, none by two, and 18 by none (PINNED
2026-11-19, by a probe over each dossier's first fenced TOML, the fence
`tools/codebase-map/map_lib.py#parse_dossier` reads). Of the 18, 17 (PINNED 2026-11-19) are map
debt in `memory/map/baseline.toml`. The last, `run-gates evidence`, is claimed by
`memory/map/FOUNDATION.md`, which sits outside `memory/map/features/` and titles itself "the shared
substrate (not a feature)", so it is outside the population. Of the 27 descriptors carrying
`[[gate_leg]]` rows (PINNED 2026-11-19), 4 declare only unclaimed legs and carry none of the
`enforces` copies below: `tools/drift-audit/kit.toml`, `tools/govkit/entries/check-wiring.kit.toml`,
`tools/govkit/entries/kickoff-manifest.kit.toml` and `tools/govkit/entries/settings-merge.kit.toml`,
which the pass leaves unchanged. Each claimed leg's row gains `"tests": ["feature.<f>"]`, `<f>`
the claiming dossier's `feature` value. An unclaimed leg carries no `tests` key: a value the rule
cannot derive is not guessed.

The key is declared at the leg from then on. A new leg states its own `tests`; a dossier that claims
it must agree, which S5 checks until dTotalRecall derives the claim from the edge.

### The edge read

```python
read_leg_edges(text, path) -> list[dict]
# {"path": "tools/gate-legs.json", "line": <the row's "tag" line>, "type": "tests",
#  "targets": ["feature.branch-reconcile"], "site": "leg", "source": "leg.gov.branch-reconcile-selftest"}
# {"path": "tools/gate-legs.json", "line": <the row's "tag" line>, "type": "enforces",
#  "targets": ["principle.p16"], "site": "leg", "source": "leg.roles.roles-catalogue"}
```

Both rows are the tags TOOL-dWitnessedBar-12's §4 rule yields at `a4cffc2cb`: `branch-reconcile
selftest` is a registry `[[exempt_leg]]` leg, so its owner segment is `gov`, and `roles catalogue` is
the roles kit's.

The adapter takes the manifest's text and its tree-relative path, the shape of the other text
sites' adapters (`tools/playbook/edge_grammar.py#read_section_edges`,
`tools/playbook/edge_grammar.py#read_unit_edges`), and reads no registry (§8 F7). It parses the
text as JSON and yields, for each row and each of `tests` and `enforces` the row carries non-empty,
one edge dict, the shape `check_edges` and `run_resolve` read from every site: `path` the
manifest's path; `line` the 1-based line of the first match of `"tag"`, optional blanks, `:`,
optional blanks and the row's tag as a JSON string, which holds in the manifest's one-member-per-line
layout and in a one-line fixture manifest alike; `type` the key; `targets` its list in row order;
`site` the word `leg`; and `source` the row's `tag` (TOOL-dWitnessedBar-12), the field
`read_unit_edges` names a unit row's source by. A row is keyed by its `tag` and never by its `name`.
Its edges pass through `tools/playbook/edge_grammar.py#check_site_targets`, as the header and
work-order adapters' do, so a malformed value is an `EdgeRefusal` line naming the manifest, the line
and the key; a text that does not parse as JSON, a key that is not a list of strings, and a row
carrying either key with no `tag` are refusal lines of the same `EdgeRefusal`, which
`read_tree_edges` gathers as it gathers every site's.

`tools/playbook/edge_grammar.py#read_tree_edges` reads the adapter for the one tracked path
`tools/playbook/instruction_units.py#derive_tool_rel` names for `gate-legs.json`
(`tools/gate-legs.json` in gov), beside its other sites. `tools/playbook/edge_grammar.py#read_site_edges`,
the `--parse` and plant entry, reads it for a path whose file name is `gate-legs.json`, ahead of its
non-Markdown branch. `check_edges` and `run_resolve` then type and resolve each yielded edge, the
checks of PLAY-dOrderedCharter-28 S8 run by the leg `edges (every declared edge parses, is registered
and resolves)`.

### The leg-row marks

`tools/playbook/edge_grammar.py#check_edges` is handed the namespace rows by each of its callers:
`run_check`, `run_parse`, `tools/playbook/tag_bundle.py#run_edge_arm` and the checks of
`tools/playbook/instructions_edit.py`. On an edge whose `site` is `leg`, it appends two kinds of
target to the edge's `unarmed` list and passes them. That list is the mark its id branch already
writes for an id no registered class holds, and `tools/playbook/edge_grammar.py#run_resolve` counts
a target on it as unarmed and never resolves it, the contract `run_edge_arm` states beside its
`target-resolves` arm. The two kinds:

- **a `tests` target whose namespace no registry row holds.** The `tests` row admits any target
  (PLAY-dOrderedCharter-24: `tests`, any to any), but a namespace word not yet registered "admits
  nothing until its build registers it", and `check_edges` otherwise reds it. Until dTotalRecall
  registers `feature`, every `feature.*` value is this case, and S5's compare holds the claim
  meanwhile.
- **an `enforces` target of the rule-member form `practice.<practice>.<rule>`**, a `practice.*` tag
  of three segments. `tools/playbook/practices.toml` admits that form only as a row's `rules` entry,
  since `tools/playbook/instruction_units.py#read_practice_catalogue` refuses a row tag outside
  `practice.<seg>`. The tag index holds no row for it, so `resolve_edge` would red it, and
  `tools/playbook/core.py#run_meta_check` already joins it to the catalogue's rules both ways, a
  rule-member tag no row declares being red there. It is that check's verdict, run by the leg `core
  meta-check`, and this one adds none, as `run_resolve` leaves a `serves` target to check 21. 13
  targets on 8 legs are this form (PINNED 2026-11-19 at `4b1d8cec6`, the first builder's return).

Every other leg-row target is graded as any site's is: an `enforces` target outside `unit`,
`practice` and `principle`, and a two-segment `practice.*` or a `principle.*` tag the index does not
hold, stay red. A target of either kind at any other site stays red too.

One function, `derive_leg_unarmed(edges) -> list[str]` in `tools/playbook/edge_grammar.py`, counts
the marks on the leg-row edges and returns a line per non-zero kind, which `run_check` and
`run_parse` print:

```text
edges: leg rows · <n> tests target(s) unarmed until their namespace is registered
edges: leg rows · <n> enforces target(s) unarmed, practice rules core meta-check grades
```

`run_check`'s `edges: targets` line counts both kinds among its `unarmed`. The module docstring's
"What it does not check" sentence names both marks.

`enforces` follows the leg-row grammar of PLAY-dOrderedCharter-7 S2: its targets are `principle.*`
and `practice.*`. The `enforces` row of `tools/playbook/edges.toml` reads
`to = ["unit", "practice", "principle"]` at `a4cffc2cb`, so §8 F1's ask has landed and the pass
widens no row.

`tools/playbook/tag_bundle.py#read_bundle_rows` reads the same edges, so a bundle of a principle or
two-segment practice tag lists the manifest among its `enforced-by` rows; no plant pins that row.

### The `enforces` copies

The 6 descriptor-claimed legs whose manifest row carries `enforces` at `a4cffc2cb` (PINNED
2026-11-19, by joining each descriptor `[[gate_leg]]` name to its manifest row): `shell hygiene (a
location probe asked from a moved directory)` and `shell hygiene (a fixed-name temp renamed into
place)` in `tools/gate-lint/kit.toml`, `roles catalogue` in `tools/roles/kit.toml`, `policy check` in
`tools/policy/kit.toml`, and `loop definition` and `loop transition tables` in `tools/loop/kit.toml`.
No descriptor row carries `enforces`. Each of them gains its manifest row's list verbatim, so S6's
join holds presence included; no value is written that the manifest does not already hold. The
emitter, `tools/govkit/govkit.py#write_gate_legs`, copies named keys into a target's row and names
neither `tests` nor `enforces`, so neither travels (§8 F4).

### Inventory

Minted: the row key `tests` and its values (180, PINNED 2026-11-19, §4), `read_leg_edges`, the site
word `leg`, the two leg-row marks in `check_edges`, `derive_leg_unarmed`, the gov canary's compare
arm, the `LEG_KEYS` entry, the 7h join of both keys, and the leg-row plants of §7's edge-grammar arm
(`leg-resolved`, `leg-unregistered`, `leg-rule-member`). Naming cells: `read_leg_edges` and
`derive_leg_unarmed` are asked of the lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

Additive. No adopter row changes; no name-keyed file moves.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/README.md`
- `tools/playbook/edge_grammar.py` (the adapter, its two dispatch branches, the leg-row marks in
  `check_edges`, `derive_leg_unarmed` and its two printers, the docstring, and the three leg plants;
  no tag-index file, §8 F6)
- `tools/playbook/adopt-playbook.sh` (the plant rows of §7's edge-grammar arm)
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- 23 of the 27 descriptors carrying `[[gate_leg]]` rows (PINNED 2026-11-19 at `a4cffc2cb`, the
  27 as TOOL-dWitnessedBar-12 lists them), each holding a dossier-claimed leg or one of §4's
  `enforces` copies: `tools/branch-reconcile/kit.toml`, `tools/codebase-map/kit.toml`,
  `tools/gate-lint/kit.toml`, `tools/lexicon/kit.toml`, `tools/loop/kit.toml`,
  `tools/memory-recall/kit.toml`, `tools/memory-tree/kit.toml`, `tools/playbook/kit.toml`,
  `tools/policy/kit.toml`, `tools/process-monitor/kit.toml`, `tools/roles/kit.toml`,
  `tools/run-gates/kit.toml`, `tools/runlog/kit.toml`, `tools/unattended/kit.toml`,
  `tools/workflows/kit.toml`, `tools/govkit/entries/check-agent-cap-restatement.kit.toml`,
  `tools/govkit/entries/check-install-prefix.kit.toml`,
  `tools/govkit/entries/check-kit-versions.kit.toml`,
  `tools/govkit/entries/check-line-length.kit.toml`,
  `tools/govkit/entries/check-microformats.kit.toml`,
  `tools/govkit/entries/check-placeholders.kit.toml`,
  `tools/govkit/entries/check-testsuite-counts.kit.toml`, `tools/govkit/entries/push-main.kit.toml`;
  the other 4 are named in §4 "The `tests` values"

### Alternatives rejected

- **`tests` targets as `kit.<id>` tags.** The owner kit is already the tag's second segment, so the
  value would restate the tag; the feature a leg tests is the fact the dossiers hold.
- **Declare on both sides with no compare.** Two spellings of one fact with no gate is what the
  night pass's point 4 forbids.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one pass over the manifest's rows and the dossiers' fences (198 and 33, PINNED
  2026-11-19 at `a4cffc2cb`, §4).
- error / empty / loading states — a `tests` target in an unregistered namespace and a rule-member
  `enforces` target each print their `edges: leg rows` count; a malformed manifest value is a refusal
  line naming the manifest, its line and the key; a compare miss names the leg, the dossier and the
  side that disagrees.
- observability — the edges check's summary carries the leg-row site's edge counts in its `by site`
  line, and its `unarmed` count includes both leg-row marks, split by the `edges: leg rows` lines.
- risks — 180 `tests` edges (PINNED, §4) stay unresolved until dTotalRecall registers `feature`;
  the compare arm is what holds them meanwhile. The rule-member `enforces` targets (13, PINNED
  2026-11-19 at `4b1d8cec6`) stay unresolved by the edges check until the tag index resolves the
  member form; `core meta-check` is what holds them meanwhile.
- testing — AC1 to AC7 by a pass; the arms of §7 at the close.
- migration — additive.
- user docs — none under `help/`; `tools/run-gates/README.md` names `tests` beside `tag` at the pass.

## 6. Acceptance criteria

- **AC1** — When a probe reads `tools/gate-legs.json` after the pass, every leg a dossier under
  `memory/map/features/` claims carries `tests` equal to `["feature.<f>"]` for its claiming dossier,
  and no other leg carries the key, `run-gates evidence` included.
  Red when: a value is guessed for an unclaimed leg, or a claimed leg's value names another feature.
  figure: 180 and 18 are PINNED 2026-11-19 at `a4cffc2cb`; the probe re-derives both from the
  dossiers under `memory/map/features/`.
- **AC2** — When the canary's key-set arm runs over a fixture manifest row carrying `tests` and
  `enforces`, it passes; with `tests` cut from `LEG_KEYS`, it fails.
  Red when: the manifest carries a key the canary does not admit.
- **AC3** — When `read_leg_edges` is called on a fixture manifest text holding one row with tag
  `leg.x.y`, name `x y`, `"tests": ["layer.memory"]` and `"enforces": ["practice.land"]`, it returns
  two dicts, one per key, each with `site` `leg`, `source` `leg.x.y` and `line` the row's `"tag"`
  line; and the plant `leg-resolved`, that text as a `gate-legs.json` site over the edge grammar's
  resolve fixture, whose registry and index declare both tags, prints each target `resolved` and
  exits 0.
  Red when: an edge is keyed by `name`, a key yields no edge, or either target is not resolved.
  command: `python tools/playbook/edge_grammar.py --fixture --plant leg-resolved`, and a
  `python -c` probe printing `read_leg_edges` over the same text.
- **AC4** — When the plant `leg-unregistered` parses a fixture manifest whose one row's `tests` holds
  `feature.x`, against the shipped namespace registry, which holds no `feature` row, `check_edges`
  returns no red, the target sits on its edge's `unarmed` list, the line
  `edges: leg rows · 1 tests target(s) unarmed until their namespace is registered` is printed
  (1 DERIVED: the plant's one target), and the run exits 0.
  Red when: the target is red or reported resolved before dTotalRecall registers the namespace.
  command: `python tools/playbook/edge_grammar.py --fixture --plant leg-unregistered`.
- **AC5** — When the gov canary's compare arm runs over a copy of the manifest with one claimed
  leg's `tests` emptied, it names that leg and its dossier; with a dossier's claim added for a leg
  whose `tests` does not name it, it names that pair too.
  Red when: the compare reads one direction only.
- **AC6** — When `govkit.py selfcheck` runs over a fixture whose descriptor row's `enforces`
  differs from its manifest row's, check 7h names the leg and both lists.
  Red when: the descriptor and the manifest disagree unseen.
- **AC7** — When the plant `leg-rule-member` resolves, over the edge grammar's resolve fixture, a
  fixture manifest whose one row's `enforces` holds `practice.land` and `practice.land.paths`,
  `practice.land` prints `resolved`, `practice.land.paths` sits on its edge's `unarmed` list and is
  never resolved, the line
  `edges: leg rows · 1 enforces target(s) unarmed, practice rules core meta-check grades` is printed
  (1 DERIVED: the plant's one rule-member target), and the run exits 0.
  Red when: the rule-member target reds the check, or the two-segment `practice.land` is marked
  rather than resolved.
  command: `python tools/playbook/edge_grammar.py --fixture --plant leg-rule-member`.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `playbook render selftest` · `policy fixtures` · `measure-legs selftest` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `branch-reconcile selftest` · `lexicon selftest` · `pre-push run-log line` · `review-join self-test` · `run-gates run-log line` · `runlog selftest` · `shell-hygiene selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `hook destinations self-test` · `scratch-guard self-test` · `routed-commits selftest` · `edges (every declared edge parses, is registered and resolves)` · `core meta-check` · `tags bundle selftest` · `instruction units selftest` · `instruction edits selftest` · `memory hygiene`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC5 · the `tests`-to-claims compare, staged by one claimed leg's `tests` emptied · that suite's arm count
New arm: tools/playbook/adopt-playbook.sh · covers AC3 AC4 AC7 · three plants of `edge_grammar.py --fixture` run as rows of the edge grammar's plant table: `leg-unregistered` a parse plant, its site written as `gate-legs.json`, and `leg-resolved` and `leg-rule-member` resolve plants whose site is named `gate-legs.json`; staged by `check_edges` marking no leg-row target, which reds `leg-unregistered` and `leg-rule-member` · none
New arm: tools/govkit/selftest.py · covers AC6 · 7h's `tests` and `enforces` join, staged by one descriptor list changed · none

## 8. Open questions

- **F1 — Which targets does `enforces` admit on a leg row?** PLAY-dOrderedCharter-7 S2 admits
  `principle.*` and `practice.*`; PLAY-dOrderedCharter-24's edge row admits `unit` or `practice`.
  Options: (a) follow -7 S2, the leg-row grammar, and widen -24's row `to` to admit `principle`;
  (b) follow -24 and drop `principle.*` from legs; (c) a second edge type for legs. (b) breaks
  -7 S3's meta-check, which joins principles to legs through `enforces`, and the clause of unit 11
  ("every leg declaring the principles it enforces"); (c) adds a type to the closed set.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the brief's direction; the ask for
  PLAY-dOrderedCharter-24's row is named in this unit's return, and the pass widens the row only
  where the ask has not landed. widens: none · relaxes: none. At `a4cffc2cb` the row's `to` admits
  `principle` (§4 "The edge read"), so the pass widens nothing.
- **F2 — Where is `tests` declared, given the dossiers already claim legs?** Options: (a) the leg
  row, values derived once from the claims, a both-ways compare until the map derives its side;
  (b) the dossiers only, the edge derived from them; (c) both, with no compare. The clause and night
  pass point 4 put a leg's edges in "a leg's fields"; (b) keeps the fact away from its site; (c) is
  two spellings with no gate. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, the night pass's
  "declared once, where the fact lives"; the ask that dTotalRecall derive the dossiers' `gate-legs`
  claims from `tests` is named in this unit's return. widens: none · relaxes: none
- **F3 — Shared interface I15 reads "the targets of its `tests` edge" as a leg's own files; is a
  `tests` target the leg's own test file or the thing it tests?** Options: (a) the thing tested, the
  direction PLAY-dOrderedCharter-24's `tests` row and its text form (`tests=kit.y,kit.z`) give;
  (b) the leg's own suites. Under (a), excluding `tests` targets from a fix pass's allowance would
  fence the product code the pass must fix; under (b), the edge points the wrong way for every
  other site. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, -24's row; the reading of I15 is
  named in this unit's return for TOOL-dWitnessedBar-21's writer, whose own files are the argv's
  files and the gate script. widens: none · relaxes: none
- **F4 — Do `tests` and `enforces` travel into an adopter's manifest?** Options: (a) no: both name
  gov-side registries (gov's dossiers, its principle rows), and an adopter's legs arrive through
  their overlay (TOOL-dWitnessedBar-28); (b) yes, behind a `LEG_KEY_FLOORS` row each. (b) ships
  edges whose targets an adopter's registry may not hold. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3. widens: none · relaxes: none
- **F5 — What does 7h's `enforces` join do with a leg whose manifest row carries `enforces` and
  whose descriptor row does not?** At `a4cffc2cb` six descriptor-claimed legs are that case (§4 "The
  `enforces` copies"), since PLAY-dOrderedCharter-7 wrote the key on the manifest alone. Options:
  (a) the pass copies each manifest list onto its descriptor row, and the join grades presence as
  S6 states; (b) the join compares only where the descriptor declares the key, as 7h's `reads` and
  `ceiling` arms do; (c) `enforces` leaves the join. (b) leaves a list on one side alone unseen,
  which AC6's "the descriptor and the manifest disagree unseen" refuses; (c) drops half of S6.
  (a) writes no value the manifest does not hold, so S2's values stay units 11's and 24's, and the
  emitter names neither key, so F4 holds. RESOLVED (agent, 2026-11-19, delegated): (a), the most
  feature-rich survivor, meeting S6 and AC6 with no veto tripped and no question left open; per
  brief 2026-11-19-prompt-TOOL-dWitnessedBar-22-reground-brief. widens: none · relaxes: none
- **F6 — What does the leg-row site do with an `enforces` target of the rule-member form
  `practice.<practice>.<rule>`?** At `4b1d8cec6` 13 targets on 8 legs are that form (PINNED
  2026-11-19, the first builder's return). `tools/playbook/practices.toml` admits it as a row's
  `rules` entry and `tools/playbook/core.py#run_meta_check` joins it, but the tag index resolves it to
  no row, so the `edges` leg would red each one once the site is read. Options: (a) the tag index
  learns the member form; (b) the leg-row site counts them `unarmed`, with AC7 and its plant;
  (c) units 11 and 24 respell the values. (a) changes the resolver, a §3 non-goal
  (PLAY-dOrderedCharter-19's) and a second mechanism (M2), and would add rows that the leg `tags (the
  resolver's checks)` grades; (c) writes values §3 gives to units 11 and 24, and the bare
  `practice.<practice>` spelling leaves each rule unenforced, which the meta-check's rule join reds.
  Veto 1 discards (a) and (c). RESOLVED (agent, 2026-11-19, delegated): (b), the one survivor,
  meeting AC7 while `core meta-check` keeps its verdict on each target; the ask that the tag index
  resolve the member form, after which the mark is deleted, is named in this unit's return for the
  dOrderedCharter chain; per brief 2026-11-19-prompt-TOOL-dWitnessedBar-22-spec-fix-brief.
  widens: none · relaxes: none, since the edges check reads no leg row before this unit
- **F7 — Where is a leg-row target marked `unarmed`, given the adapter sees no registry?** Options:
  (a) the adapter takes the registered namespace words, `read_leg_edges(text, path, registered)`,
  and `read_tree_edges` and `read_site_edges` read a registry to pass to it; (b) the adapter reads
  no registry, and `check_edges`, which each caller already hands its namespace rows, marks the
  leg-row targets on the edge's `unarmed` list, the list its id branch writes and `run_resolve`
  skips. (a) has `read_tree_edges` read a registry its callers already read, and may read a
  different one: `tools/playbook/tag_bundle.py#run_edge_arm` passes its own. That is one fact read
  twice, and a site filtering its own output before the check sees it. RESOLVED (agent, 2026-11-19,
  delegated): (b), the most feature-rich survivor, both marks in the one function that holds the
  registry, no new parameter and no veto tripped; per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-22-spec-fix-brief. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 22, the brief's shared interfaces I1,
  I2 and I15, scout B's row for cl-0360, night pass point 4, PLAY-dOrderedCharter-7, -24 and -28,
  and the dossiers and manifest read at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-19 · §7 · the leg line drops `agent-instructions self-test`, which
  PLAY-dOrderedCharter-31 retired from `tools/gate-legs.json` with its kit, whose registry `[[retired]]`
  successor `playbook-render` is tested by `playbook render selftest`, already on the line; it gains
  `policy fixtures`, whose manifest guard holds the §4 path `tools/gate-legs.json`; per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief; nothing else moved.
- rev-4 · 2026-11-19 · §1 §2 §4 §5 §6 §7 §8 §10 · S2 S3 S4 S6 · AC1 · F1 F5 · re-grounded at
  `a4cffc2cb` per brief 2026-11-19-prompt-TOOL-dWitnessedBar-22-reground-brief: the claim counts
  are re-pinned (PINNED, §4), with `memory/map/FOUNDATION.md`'s claim named outside the population;
  `enforces` has landed on manifest rows and in both `KNOWN` copies, so S3 adds `tests` alone; the
  `enforces` row of `edges.toml` admits `principle`, so F1's widen is moot and the file leaves Files
  touched; descriptor-claimed legs carry `enforces` on the manifest alone (PINNED, §4), which F5
  settles by copying the lists to their descriptor rows; the sites are wired in
  `read_tree_edges`, the closed PLAY-dOrderedCharter-28 holding no site table to extend, and the
  edge-grammar arm moves to `adopt-playbook.sh`'s plant rows, where the plants run; the worked edges
  use the tags unit 12's rule yields; Files touched names the descriptors the pass edits, the
  retired agent-instructions descriptor gone and the loop and policy ones added, with the README
  and `adopt-playbook.sh`; the leg line gains `hook destinations self-test`, `scratch-guard
  self-test`, `routed-commits selftest` and the `edges` leg, and drops `drift-audit selftest`,
  whose descriptor the pass leaves unchanged; citations re-pinned as `path#symbol`.
- rev-5 · 2026-11-19 · §2 §3 §4 §5 §6 §7 §8 §10 · S4 · AC3 AC4 AC7 · F6 F7 · settles the first
  builder's divergence per brief 2026-11-19-prompt-TOOL-dWitnessedBar-22-spec-fix-brief: the
  rule-member `enforces` targets the tag index does not resolve are marked `unarmed` at the leg site
  and left to `core meta-check` (F6, AC7 and its plant); the marks live in `check_edges`, which holds
  the registry, so `read_leg_edges(text, path)` reads none, and its edge-dict shape is named (F7);
  AC3's targets are respelled to two tags the resolve fixture declares; the plants are three, named;
  §3 gains the tag-index ask; the leg line gains `core meta-check`, `tags bundle selftest`,
  `instruction units selftest` and `instruction edits selftest`, whose code reads `check_edges` or
  `read_tree_edges` or grades the rule members; Files touched gains no file.

## 10. Reuse audit

The seams extended are PLAY-dOrderedCharter-7 S2's `enforces` key, read by `tools/playbook/core.py`'s
meta-check, PLAY-dOrderedCharter-24's edge rows in `tools/playbook/edges.toml` and parser, and -28
S5's site adapters, gathered by `tools/playbook/edge_grammar.py#read_tree_edges`, all CLOSED and
landed when re-verified at `a4cffc2cb`; within the last, `check_edges`' `unarmed` mark, which its id
branch writes and `run_resolve` skips and counts, extended to the leg site rather than a second
withholding path, and `check_site_targets`, the target grammar the header and work-order adapters
answer to (re-read at `4b1d8cec6`); TOOL-dWitnessedBar-12's `LEG_KEYS` and leg tags, landed at
`6b3f271c6`;
govkit selfcheck 7h (`tools/govkit/govkit.py#selfcheck`, its `7h` block), whose `doc_reads`, `impure`
and `stage` arms are the presence-included joins S6 copies; and the dossiers' `[claims] gate-legs`
lists, parsed by `tools/codebase-map/map_lib.py#parse_dossier` and joined to the manifest's leg names,
which `tools/codebase-map/map_extractors.py#_gate_legs` extracts, by
`tools/codebase-map/map_lib.py#claimant_index`. The lookup
`python tools/codebase-map/reuse_lookup.py "declare which feature a gate leg tests"` with the words
`and which principles it enforces` appended ranked generic `leg`, `legs` and `declares` stems and
named no seam, as expected with neither key built. One disagreement with scout B: it gives the
dossiers' leg claims as front matter `gate-legs = [...]`; at `cdfbd1cf` they sit in each dossier's
fenced TOML under `[claims]`, 122 legs claimed once and 20 unclaimed, and at `a4cffc2cb` 180 and 18
(PINNED, §4). The recall probe returned scout B's row and the brief's settle-in-§8 instruction; none
disagreed with source otherwise. At rev-5 the lookup
`python tools/codebase-map/reuse_lookup.py "mark an edge target unarmed so the edge check does not red it"`
ranked generic `check` and `note` stems and named no seam beyond `check_edges`' mark; the second
recall probe below returned the first builder's return, scout B's row and the build backlog's
`enforces` row, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "how is an edge target counted unarmed rather than red" --terms "unarmed check_edges run_resolve rule member practice rules enforces tag index resolve"`, and `python tools/memory-recall/query.py "how are the tests and enforces edges declared on a gate leg row" --terms "tests enforces edge field leg row gate-legs.json dossier gate-legs claims principle practice edge grammar"`
