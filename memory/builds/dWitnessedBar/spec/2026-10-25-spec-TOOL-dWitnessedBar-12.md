# TOOL-dWitnessedBar-12 — the `leg`, `check` and `pack` tag namespaces, and a `tag` on every leg

**Status:** CLOSED · rev-8 · 2026-11-19 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 5 · advances TOOL-dWitnessedBar-31

**Carries:** cl-dClosedLoop-0350@37beff65 whole
**Carries:** node:tag-namespace.leg
**Carries:** node:tag-namespace.check
**Carries:** node:tag-namespace.pack

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-reuse-scout-b.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-28 |
| [2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-spec-stage-returns.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-26-build-TOOL-dWitnessedBar-12-deviation-121.md](../build/2026-10-26-build-TOOL-dWitnessedBar-12-deviation-121.md) | deviation | — |
| [2026-11-05-build-TOOL-dWitnessedBar-12-deviation-122.md](../build/2026-11-05-build-TOOL-dWitnessedBar-12-deviation-122.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-12-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-12-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-12-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-12-1-builder-return.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-12-red-fix-23.md](../build/2026-11-19-build-TOOL-dWitnessedBar-12-red-fix-23.md) | red-fix | — |
| [2026-11-19-build-TOOL-dWitnessedBar-12-red-fix-24.md](../build/2026-11-19-build-TOOL-dWitnessedBar-12-red-fix-24.md) | red-fix | — |
| [2026-11-19-build-TOOL-dWitnessedBar-12-red-fix-25.md](../build/2026-11-19-build-TOOL-dWitnessedBar-12-red-fix-25.md) | red-fix | — |
| [2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md](../build/2026-11-21-build-TOOL-dWitnessedBar-1-runlog-5a748574.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 TOOL-dWitnessedBar-109 TOOL-dWitnessedBar-110 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-spec-fix-brief.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 |
| [2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-56 |
| [2026-11-05-prompt-TOOL-dWitnessedBar-3-owner-forks.md](../prompts/2026-11-05-prompt-TOOL-dWitnessedBar-3-owner-forks.md) | research | TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-28 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-12-2-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-12-2-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-12-3-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-12-3-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-12-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-12-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-12-pin-fix-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-12-pin-fix-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-12-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-12-reground-brief.md) | journal | TOOL-dWitnessedBar-61 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-12-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-12-reground-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-12-spec-fix-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-12-spec-fix-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-54 |
| [2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-28 |
| [2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md) | diff-review | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

Give every gate leg a `tag` in the `leg` namespace beside its free-text `name`, which stays the join
key of every file keyed by leg, and register the `leg`, `check` and `pack` namespaces with their
extractors, so a leg, a check and a pack can be addressed, selected and shape-checked like every
other tagged thing. 139 of 140 leg names failed the tag shape (systems.md:270) when the systems
record measured them, and no leg carries a tag today: `grep -c '"tag"' tools/gate-legs.json` prints
0 (PINNED 2026-11-19 at `a30a26466`).

## 2. Scope (IN)

- **S1** — A `tag` on each of the 198 rows of `tools/gate-legs.json` (PINNED 2026-11-19 at `a30a26466`)
  and on each of the 70 `[[gate_leg]]` rows in the 27 kit descriptors that carry one (PINNED
  2026-11-19 at `a30a26466` by §8 F4's probe), by the rule of §4 "The tag rule". Observed by AC1.
- **S2** — Three `[[namespace]]` rows in `tools/playbook/namespaces.toml`, each carrying every field
  of `REGISTRY_FIELDS` (`tools/playbook/tag_index.py#REGISTRY_FIELDS`), per §4 "The three rows".
  Observed by AC2.
- **S3** — Three extractors in `tools/playbook/tag_index.py`: `extract_leg` (one member per
  manifest row's `tag`), `extract_pack` (one member `pack.<word>` per distinct `pack` value on the
  manifest's rows) and `extract_check` (one member `check.<kit>.<id>` per `[[numbered_check]]` row
  of a kit descriptor, §8 F8). `extract_check` is the second extractor minting `<ns>.<kit id>.<key>`
  from a descriptor table, so the body of `tools/playbook/tag_index.py#extract_command` becomes one
  factory, `derive_kit_rows(text, ns, table)`, which both call, and `ROW_TAG_KEYS` gains
  `"numbered_check": "id"`. Observed by AC3 and AC4.
- **S4** — The leg row key set, today a literal spelled twice in `tools/run-gates/run-gates.test.sh`
  (the arm at `tools/run-gates/run-gates.test.sh@20bb181a3abe:409` and `keyset_probe` at
  `tools/run-gates/run-gates.test.sh@20bb181a3abe:830`), becomes one constant `LEG_KEYS` that both
  arms read, and `tag` joins it. `tools/run-gates/owed_rows.py#read_known_copies` reads `LEG_KEYS` in
  place of the `KNOWN` copies, and its refusal of two copies that disagree, with its self-test case
  "two KNOWN copies that differ", is deleted, since one constant cannot disagree with itself. Every
  later unit adding a row key adds it there once. Observed by AC5.
  **Readers:** by name: `tools/run-gates/run-gates.test.sh`, which spells `KNOWN` in both copies and
  in the comments of each key's control pair; `tools/run-gates/owed_rows.py`, which spells `KNOWN` in
  `read_known_copies`, its refusals, its owed row, its self-test cases and its help text.
  by value: `tools/run-gates/owed_rows.py#read_known_copies`, the one reader that compares the
  copies and derives the owed key rows from them, which reads `LEG_KEYS` after the pass.
- **S5** — `LEG_KEY_FLOORS` in `tools/govkit/govkit.py`, beside the `*_FLOOR_RUN_GATES` constants,
  four (PINNED 2026-11-19 at `a30a26466`): `SUBJECT_`, `DOC_READS_`, `CEILING_` and
  `STAGE_FLOOR_RUN_GATES`. It is one table from row key to the run-gates version whose canary
  admits it, `tag` its first entry. The emitter, `tools/govkit/govkit.py#write_gate_legs`, carries a descriptor's `tag`
  into a target's row only at or above that floor, through
  `tools/govkit/govkit.py#check_target_reads_subject`'s `floor` argument. Observed by AC6.
- **S6** — govkit selfcheck 7h's both-ways join (`tools/govkit/govkit.py#selfcheck`, its `7h` block)
  gains `tag`: a descriptor row and its manifest row carry the same tag. Observed by AC7.
- **S7** — The gov canary `tools/run-gates/run-gates.gov.test.sh` asserts every row of gov's own
  manifest carries a `tag` in the `leg` namespace and no two rows share one. It is the one check
  that reds a duplicated leg tag (§8 F10). Observed by AC1.
- **S8** — The fixture plants, on PLAY-dOrderedCharter-19 S13's
  `gov_tag.py --fixture --plant <case>`: `leg-rows`, `pack-rows` and `check-rows`, each a row of the
  playbook-render selftest's `run_plant_rows` heredoc in `tools/playbook/adopt-playbook.sh`.
  Observed by AC3 and AC4.
- **S9** — `help/tags.md`'s namespace table gains the `leg`, `pack` and `check` rows, and its
  sentence counting the registered namespaces reads the registry's count after the pass. Observed by
  AC2.

## 3. Non-goals (OUT)

- The tag grammar, `namespaces.toml`, the index, the shape check and the join factory:
  PLAY-dOrderedCharter-19's and -10's, landed in `tools/playbook/tag_index.py` and
  `tools/playbook/gov_tag.py`, called here and never re-specced. The namespace-word rule of
  `tools/playbook/tag_index.py#derive_tag_fault` and its twin `tools/lexicon/lexicon.py#check_tag_name`
  is TOOL-dDeclaredLoop-18 S10's and is not narrowed here (§8 F9).
- The `pack` row key itself: PLAY-dOrderedCharter-19 S12's, landed, which this unit's extractor
  reads.
- Moving any file keyed by leg name onto the tag. `tools/run-gates/ceiling-evidence.txt`,
  `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/windows-only-legs.txt`, `silenced_legs`
  and `tools/roles/house/policy.toml`'s `[gates]` stay keyed by `name` (systems.md:265-271).
- Declaring `[[numbered_check]]` rows for any kit's numbered checks. The namespace reads `unarmed`
  until a kit declares one (§8 F2); the two checks numbered 23 (final-questions.md:312) are its first
  candidates.
- The descriptors' existing `[check]` table, govkit's per-kit verifier (`argv` or `none`), which
  every descriptor declares and selfcheck 7j2 requires; this unit adds no key to it (§8 F8).
- The leg factory that generates the manifest: TOOL-dWitnessedBar-11. Until it lands, the tag is
  written in the manifest and the descriptors, and 7h joins the two.
- A repository's own legs' `leg.adopter.<name>` rows: TOOL-dWitnessedBar-28's.
- A rename or retirement of a leg tag. No write path owns it: PLAY-dOrderedCharter-15's write verbs
  take `--manifest <kit id>|overlay` over instruction manifests, and its change record's `Unit` field
  is an instruction unit's tag (its S2, S7 and `WRITE_VERBS`), so no path of that unit writes
  `tools/gate-legs.json`. Per §8 F5 the path goes to that unit's `new change` door, by the ask this
  build run files in dOrderedCharter's `BACKLOG.md`. PLAY-dOrderedCharter-15 S9's
  `extract_change_records` is named here only as the reader that turns a recorded end of a tag into
  its retired index row.

### Edges

- **hands-off** `TOOL-dWitnessedBar-22` — `tag`, the `leg.<owner>.<name>` member a `tests` edge's
  target and an `enforces` row's leg are addressed by
- **hands-off** `TOOL-dWitnessedBar-19` — `tag`, the row key `purpose` is added beside in `LEG_KEYS`
  and `LEG_KEY_FLOORS`
- **hands-off** `TOOL-dWitnessedBar-11` — `tag`, which the leg factory emits from each pack's
  declaration and its conformance gate grades
- **hands-off** `TOOL-dWitnessedBar-14` — `tag`, the `pack.ratchet` member its legs' `pack` value
  yields
- **hands-off** `TOOL-dWitnessedBar-24` — `tag`, the `pack.portability` member its legs' `pack`
  value yields
- **hands-off** `TOOL-dWitnessedBar-28` — `tag`, the `leg` namespace a repository's
  `leg.adopter.<name>` rows join and the `pack.adopter` member
- **consumes-from** external — PLAY-dOrderedCharter-19 S1, S2, S4, S12 and S13 and
  PLAY-dOrderedCharter-10 S3: the grammar, the registry, the index, the `pack` key, the fixture and
  the shape check this unit registers into
- **hands-off** `TOOL-dWitnessedBar-51` — the round-1 minors ids 15, 16 and 41: `LEG_KEYS`' readers through the `level` and `precommit` keys, the tag rule re-derived for units 24 and 9, and the row hash dropping declarative keys, each a scope item of that unit

## 4. Design

### The tag rule

`tag = "leg.<owner>.<name>"`, where `<owner>` is the `id` of the kit descriptor whose
`[[gate_leg]]` row declares the leg, or `gov` for a leg `tools/govkit/registry.toml` exempts, and
`<name>` is the leg's `name` lower-cased, each run of characters outside `[a-z0-9]` folded to one
hyphen and the ends trimmed. Where a descriptor's `id` is a namespace word of
`tools/playbook/namespaces.toml` at the pass, `<owner>` is that id with `-kit` appended (§8 F9). A
tag over `tools/playbook/tag_index.py#TAG_MAX_BYTES` (64) bytes is cut at its last hyphen within it.
Applied at `a30a26466` the rule yields 198 tags (PINNED 2026-11-19 by §8 F4's probe):
70 under a descriptor's id and 128 under `gov` (PINNED 2026-11-19 at `a30a26466`), 6 cut (PINNED
2026-11-19 at `a30a26466`), no two equal, every one matching `seg := [a-z0-9][a-z0-9-]*`, and one
owner, the policy kit's `policy`, a namespace word, so its leg reads `leg.policy-kit.policy-check`.

The rule runs once, at the pass, to write the tags. After that a tag is the leg's declared identity
and is not re-derived when its `name` changes; a rename of the tag has no owned write path until
the `new change` door accepts a `leg.*` tag (§3, §8 F5). A new leg is given its tag by the same rule, which the gov canary's
shape and uniqueness arm and 7h hold it to.

### The three rows

```toml
# tools/playbook/namespaces.toml, after its 15 rows (PINNED 2026-11-19 at a30a26466:
# PLAY-dOrderedCharter-10's ten and dDeclaredLoop's five)
[[namespace]]
ns = "leg"
owner = "dWitnessedBar"
layer = "layer.flow"
source = "each row's tag in {prefix}/gate-legs.json"
extractor = "tag_index:extract_leg"
role = "selects"
purpose-source = "{prefix}/gate-legs.json"
join-armed-by = "dWitnessedBar"

[[namespace]]
ns = "pack"
owner = "dWitnessedBar"
layer = "layer.flow"
source = "each distinct pack value of the rows of {prefix}/gate-legs.json, pack.<word> each"
extractor = "tag_index:extract_pack"
role = "selects"
purpose-source = "{prefix}/gate-legs.json"
join-armed-by = "dWitnessedBar"

[[namespace]]
ns = "check"
owner = "dWitnessedBar"
layer = "layer.distribution"
source = "each [[numbered_check]] row's id in a tracked kit.toml or *.kit.toml descriptor, check.<id>.<check id> each"
extractor = "tag_index:extract_check"
role = "describes"
purpose-source = "{prefix}/govkit/registry.toml"
join-armed-by = "dWitnessedBar"
```

| `ns` | Members at landing |
|---|---|
| `leg` | 198, DERIVED from the manifest's rows |
| `pack` | `pack.tags` alone, DERIVED from the 6 rows carrying `"pack": "tags"` (PINNED 2026-11-19 at `a30a26466`); `ratchet`, `portability` and `adopter` join as their units land |
| `check` | none: `tags: unarmed check` |

`leg` and `pack` select: a later instruction unit's or a test selection's scope names them. Each
`purpose-source` is path-only (§8 F6), as the `kind`, `kit`, `repo`, `step`, `item`, `scenario`, `policy`
and `command` rows' are. `leg` and `pack` sit in `layer.flow`, whose definition names the verdict engine;
`check` sits in `layer.distribution` with `kit` and `command`, the rows minted from descriptors
(§8 F7). A `[[numbered_check]]` row holds `id` (one segment) and `leg` (the name of the leg that runs
it), so `check.memory-tree.23` and `check.unattended.23` can be told apart once each kit declares
them.

Registering the three words adds no red to the tree as it stands: no defined tag, selector or family
row has `leg`, `check` or `pack` as its first segment after its namespace, and no backticked or
bracketed span outside `memory/builds/` opens with one of them (both PINNED 2026-11-19 at
`a30a26466`, by `tools/playbook/tag_index.py#read_rows` and
`tools/playbook/tag_index.py#read_population` over the loaded view).

### The one key set

```bash
# tools/run-gates/run-gates.test.sh, once, near the top
LEG_KEYS="name argv guard impure reads chunk subject ceiling signature doc_reads pack enforces pass_leg scope_of stage tag"
```

Both Python programs that read the key set today (the arm and `keyset_probe`, cited in S4) take it
from `LEG_KEYS` as an argument, so a key cannot be admitted by one and refused by the other. The
value is the 15 keys both copies spell at `a30a26466` (PINNED 2026-11-19) plus `tag`.
`tools/run-gates/owed_rows.py` reads the `LEG_KEYS="…"` line where `read_known_copies` read each
`KNOWN = {...}` line; the row it owes for a key outside the set names `LEG_KEYS`, and its fixture's
canary text plants one `LEG_KEYS` line.

The run-gates kit's version moves at this pass, and `LEG_KEY_FLOORS["tag"]` is that version
(DERIVED at the pass from `KIT_RUN_GATES_VERSION`, `tools/run-gates/run-gates.sh@c828502568bf:36`,
1.50 at `a30a26466`), so an adopter whose installed canary predates `tag` never meets the key.

### Inventory

Minted: the leg tags, one per manifest row, the `[[namespace]]` rows `leg`, `check` and `pack`, `extract_leg`,
`extract_pack`, `extract_check`, `derive_kit_rows`, the `[[numbered_check]]` descriptor table and its
`ROW_TAG_KEYS` entry, `LEG_KEYS`, `LEG_KEY_FLOORS`, the gov canary's tag arm, S8's plants. Naming
cells: `extract_leg`, `extract_pack`, `extract_check` and `derive_kit_rows` each read `OK` from the
lexicon's `--suggest` under `--as py.function` (asked 2026-11-19). `LEG_KEY_FLOORS` has no cell: the
lexicon declares `js.function`, `js.type`, `py.function`, `py.type` and `sh.function`, and refuses
`py.constant` as undeclared, so the name follows the `*_FLOOR_RUN_GATES` constants beside it (S5).

### Migration

Additive. Every row gains a key; no name moves; an adopter's manifest gains `tag` on gov rows only
through `apply` or `update` above the floor.

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.sh` (the kit version)
- `tools/run-gates/owed_rows.py`
- `tools/run-gates/README.md`
- `tools/playbook/namespaces.toml`
- `tools/playbook/tag_index.py`
- `tools/playbook/gov_tag.py`
- `tools/playbook/adopt-playbook.sh` (S8's plant rows)
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `help/tags.md`

The 27 descriptors carrying `[[gate_leg]]` rows (PINNED 2026-11-19 at `a30a26466`;
DERIVED again 2026-11-19 at `d832ccb37`, 70 rows, the same set):

- `tools/branch-reconcile/kit.toml`
- `tools/codebase-map/kit.toml`
- `tools/drift-audit/kit.toml`
- `tools/gate-lint/kit.toml`
- `tools/lexicon/kit.toml`
- `tools/loop/kit.toml`
- `tools/memory-recall/kit.toml`
- `tools/memory-tree/kit.toml`
- `tools/playbook/kit.toml`
- `tools/policy/kit.toml`
- `tools/process-monitor/kit.toml`
- `tools/roles/kit.toml`
- `tools/run-gates/kit.toml`
- `tools/runlog/kit.toml`
- `tools/unattended/kit.toml`
- `tools/workflows/kit.toml`
- `tools/govkit/entries/check-agent-cap-restatement.kit.toml`
- `tools/govkit/entries/check-install-prefix.kit.toml`
- `tools/govkit/entries/check-kit-versions.kit.toml`
- `tools/govkit/entries/check-line-length.kit.toml`
- `tools/govkit/entries/check-microformats.kit.toml`
- `tools/govkit/entries/check-placeholders.kit.toml`
- `tools/govkit/entries/check-testsuite-counts.kit.toml`
- `tools/govkit/entries/check-wiring.kit.toml`
- `tools/govkit/entries/kickoff-manifest.kit.toml`
- `tools/govkit/entries/push-main.kit.toml`
- `tools/govkit/entries/settings-merge.kit.toml`

### Alternatives rejected

- **The tag in place of the name.** Every name-keyed file and the run-log history join on `name`
  (systems.md:265-271); moving them is a migration the clause does not ask for.
- **A per-key floor constant.** Four hand-copied constants exist already (S5, PINNED 2026-11-19), and a fifth is what I1
  forbids; one table keyed by row key is read the same way by every later key.
- **Tags hand-written per leg.** One hand choice per leg is not derived and cannot be re-checked; the rule
  is stated and its output measured.

## 5. Production-readiness checklist

- security — no new write path; descriptor and manifest edits through the existing govkit paths.
- perf / scale — three extractors over one JSON and the descriptors; the index re-parses only
  changed blobs.
- error / empty / loading states — `check` prints `unarmed` while no `[[numbered_check]]` row exists,
  never green; a duplicate or malformed tag reds the gov canary naming both rows. What `check` does not
  check: two rows sharing one `leg` tag, since no red site it reaches compares one defining row's tag
  against another's (§8 F10), so a duplicate in a manifest other than gov's own is red nowhere.
- observability — `gov_tag.py check` counts S2's namespaces and their members in its totals line,
  `tags: <n> namespaces, <n> tags, …`, and prints `tags: join check · unarmed …` and
  `tags: unarmed check (…)` while `check` declares nothing (`tools/playbook/gov_tag.py#run_check`). It
  prints no per-namespace member count; `where` and `refs` address one member.
- risks — the `check` namespace is empty at landing; an adopter below the floor carries no tags,
  so a selection by `leg.*` there selects nothing until it updates. `extract_check` takes the
  descriptor's `id` as `extract_command` does, so a policy kit `[[numbered_check]]` row would mint
  `check.policy.<id>`, which the shape check refuses on arrival, as it would a policy kit
  `[[command]]` row; no such row exists (§8 F9). A namespace a later build registers under a word
  some leg's owner segment spells reds that leg's tag in the same arm, at that build's pass.
- testing — AC1 to AC7 by a pass; the arms of §7 at the close.
- migration — additive, as §4 says.
- user docs — `help/tags.md`'s namespace table gains the three rows (S9); no help page describes the
  manifest's keys, and `tools/run-gates/README.md` names `tag` beside `name` at the pass.

## 6. Acceptance criteria

- **AC1** — When a probe reads `tools/gate-legs.json` after the pass, every row carries a `tag`
  matching `leg.<seg>.<seg>`, within `TAG_MAX_BYTES`, no two equal, each one returning None from
  `tag_index.derive_tag_fault` against the registry's words, and each descriptor-backed row's tag
  opens with its owner segment, the descriptor's `id` or, for the policy kit, `policy-kit`; the gov
  canary's tag arm, given a copy with one tag duplicated, names both rows.
  Red when: a row lacks a tag, two legs share one, or the policy kit's leg reads
  `leg.policy.policy-check`.
  figure: the row count is DERIVED from the manifest at observation; 198 is PINNED 2026-11-19 at `a30a26466`.
- **AC2** — When `grep -cE '^ns = "(leg|check|pack)"' namespaces.toml` runs in `tools/playbook/`,
  it prints 3, and `grep -cE '^\| .(leg|check|pack). \|' help/tags.md` run at the repository root
  prints 3.
  Red when: a row is missing, so a `leg.*` tag reads `namespace not registered`, or the help page
  omits one.
  figure: 3 is DERIVED from S2's three rows.
- **AC3** — When `python gov_tag.py --fixture --plant leg-rows` runs, `where` resolves the fixture's
  `leg.gate-lint.shell-hygiene` member to its manifest row and `check` exits 0, the plant printing
  both exits on one line, as `loop-rows` does. A duplicated tag is AC1's, on the gov canary (§8 F10).
  Red when: `extract_leg` reads the `name` instead of the `tag`, so `where` resolves no row.
- **AC4** — When `python gov_tag.py --fixture --plant pack-rows` runs, a fixture manifest whose rows
  carry `"pack": "tags"` twice and `"pack": "ratchet"` once yields exactly `pack.tags` and
  `pack.ratchet`; under `--plant check-rows`, two kits each declaring `[[numbered_check]]` with
  `id = "23"` beside their `[check]` table yield `check.memory-tree.23` and `check.unattended.23`, and
  with no `[[numbered_check]]` row the namespace prints `unarmed`.
  Red when: a pack word is counted once per row, a descriptor holding both tables fails to parse,
  or an empty `check` namespace reads green.
- **AC5** — When the canary's key-set arm and its `keyset_probe` are run over a fixture manifest
  with a row carrying `tag`, both pass; with `LEG_KEYS` edited to drop `tag`, both fail;
  `grep -c '^KNOWN = ' run-gates.test.sh` and `grep -c 'KNOWN cop' owed_rows.py` in
  `tools/run-gates/` each print 0; and `python owed_rows.py --selftest` there exits 0 with its
  key case naming `LEG_KEYS`.
  Red when: either arm keeps its own literal, so the two can disagree, or `owed_rows.py` still reads
  a `KNOWN` line the canary no longer holds.
  figure: each 0 is DERIVED from S4, which leaves no `KNOWN` copy.
- **AC6** — When a probe calls govkit's emitter over a fixture target whose installed runner reads
  one minor version below `LEG_KEY_FLOORS["tag"]`, the written row carries no `tag`; at the floor
  it carries the descriptor's tag.
  Red when: a target below the floor receives a key its canary refuses.
- **AC7** — When `govkit.py selfcheck` runs over a fixture whose descriptor row's `tag` differs
  from its manifest row's, check 7h names the leg and both tags.
  Red when: the two spellings drift unseen.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `playbook render selftest` · `policy fixtures` · `measure-legs selftest` · `branch-reconcile selftest` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `drift-audit selftest` · `lexicon selftest` · `pre-push run-log line` · `review-join self-test` · `run-gates run-log line` · `runlog selftest` · `shell-hygiene selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `hook destinations self-test` · `scratch-guard self-test` · `routed-commits selftest` · `tags (the resolver's checks)` · `memory hygiene`

New arm: tools/run-gates/run-gates.test.sh · covers AC5 · both key-set arms reading `LEG_KEYS`, and `owed_rows.py --selftest` reading it, staged by `tag` cut from it · that suite's arm count
New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · the tag presence and uniqueness arm, staged by one duplicated tag · that suite's arm count
New arm: tools/playbook/adopt-playbook.sh · covers AC3 AC4 · the playbook-render selftest runs `gov_tag.py --fixture` under S8's plants, its `run_plant_rows` rows, staged by `extract_leg` reading each row's `name`, which reds the `leg-rows` row · none
New arm: tools/govkit/selftest.py · covers AC6 AC7 · the `tag` floor pair and 7h's tag join, staged by the floor table entry removed · none

## 8. Open questions

- **F1 — What is a gov-exempt leg's owner segment?** Options: (a) `gov`; (b) `adopter`, as a
  repository's own leg; (c) the kit whose file the argv names. (b) collides with the form a real
  adopter's overlay rows take (TOOL-dWitnessedBar-28), so gov's and an adopter's own legs would be
  one population; (c) names a kit as owner of a leg its descriptor refused to declare.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What declares the `check` namespace's members?** Options: (a) declared rows in kit
  descriptors, read by `extract_check`, `unarmed` until a kit declares one; (b) parse each checker's
  numbered comment headers; (c) defer the row. (b) reads two comment styles that are conventions,
  not grammar (`# <n> — ` in `tools/memory-tree/check-memory-hygiene.sh@2c0cb6f24513:889`,
  `# ---- <n>: ` in `tools/unattended/check-unattended.sh@287ccb81fe28:1638`, and memory hygiene's
  own check 23 in the second style); (c) leaves the clause's namespace unregistered. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the declared-table precedent TOOL-dDeclaredLoop-18 F2
  set for `command`. The table's name is F8's. widens: none · relaxes: none
- **F3 — Where does the one key set live?** Options: (a) `LEG_KEYS` in `run-gates.test.sh`, the
  suite whose two arms read it; (b) a constant in `run-gates.sh` read by the canary, as
  `KNOWN_KNOBS` (`tools/run-gates/run-gates.sh@c828502568bf:635`) is. (b) puts in the runner a set
  the runner never reads, so the constant would describe nothing it governs. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **FACT-QUESTION · F4 — Does the stated rule give unique, shape-valid tags within `TAG_MAX_BYTES`?**
  Probe: the rule of §4 applied to `tools/gate-legs.json`, the descriptors named by
  `tools/govkit/registry.toml`'s `[[entry]]` rows and its `[[exempt_leg]]` rows, each tag then graded
  by `tools/playbook/tag_index.py#derive_tag_fault` and `tools/lexicon/lexicon.py#check_tag_name`
  against the registry's words plus `leg`, `check` and `pack`. Observation at `cdfbd1cf`,
  2026-10-25: 142 tags, 3 cut at 64 bytes, no collision, every segment valid. Liveness: before the
  cut, 3 tags exceeded 64 bytes, so the probe reports a negative when the cut is removed. RESOLVED
  (agent, 2026-10-25, delegated): the rule as stated, rung 2. widens: none · relaxes: none.
  Re-observed 2026-11-19 at `a30a26466`: 198 tags, 70 descriptor-owned in 27 descriptors (PINNED)
  and 128 exempt, 6 cut (PINNED 2026-11-19), no collision, every segment valid; both graders refuse
  exactly one, `leg.policy.policy-check`, whose first segment is the namespace word `policy`, which
  F9 settles. Liveness: before the cut, 6 tags exceeded `TAG_MAX_BYTES` (PINNED 2026-11-19).
- **F5 — Which write path renames or retires a leg tag?** PLAY-dOrderedCharter-15's door is an
  instruction unit's (§3). Options: (a) an ask to dOrderedCharter: the `new change` door of
  PLAY-dOrderedCharter-15 S7 accepts a `leg.*` tag in `Unit`, so S9's extractor writes the retired row
  from the same record kind and `gov_tag.py check` reads new text citing the old tag; (b) a hand-off to
  TOOL-dWitnessedBar-11's leg factory, which renames the tag where it emits the row and writes a
  record of its own, which S9's extractor then cannot read without a second record kind. (a) keeps one
  record kind and one retirement reader; its cost is a parent change, and until it lands a leg tag is
  renamed by no door. (b) needs no parent change but adds a mechanism to unit 11 and a second record of
  a tag's end. Recommendation (a). RESOLVED (owner, 2026-11-05): (a) an ask to dOrderedCharter's
  `new change` door. The ask this build run files in `memory/builds/dOrderedCharter/BACKLOG.md` is
  "PLAY-dOrderedCharter-15: the S7 `new change` door accepts a `leg.*` tag in `Unit`".
- **F6 — What does each row's `purpose-source` name, now that PLAY-dOrderedCharter-22's `purpose`
  arm grades the column?** The arm reads `<path>`, `<path>#<field>` over a `.toml` or `.py` path, or
  `#<field>` over each member's file, and reds a field read in any other file
  (`tools/playbook/tag_index.py#check_namespace_purpose`). Options: (a) path-only, the manifest for
  `leg` and `pack` and the govkit registry for `check`, as the `kit` and `command` rows read; (b) the
  systems record's `#design-tags` section, as rev-5 wrote; (c) `{prefix}/gate-legs.json#purpose`,
  ready for TOOL-dWitnessedBar-19's key. (b) and (c) each read a field in a `.md` or a `.json` file,
  which the arm reds on the bar's `tags` leg, so veto 1 discards both. RESOLVED (agent, 2026-11-19,
  delegated): (a), rung 3, the precedent of the path-only rows (eight, PINNED 2026-11-19). widens: none · relaxes: none
- **F7 — Which layer row does each of the three rows name?** rev-5 named `layer.flow` for `leg` and
  none for the other two. The `owned` arm (`tools/playbook/tag_index.py#check_owned`) reds a member
  of a core layer's namespace minted in a kit whose descriptor names an `optional` or `expansion`
  layer, and 8 of the descriptors do (PINNED 2026-11-19 at `a30a26466`). Options: (a) `leg` and `pack`
  in `layer.flow`, `check` in `layer.distribution`; (b) all three in `layer.flow`; (c) `pack` in the
  optional `layer.flow.leg-packs`. (b) reds a `[[numbered_check]]` row any of those kits declares,
  and `leg` and `pack` members sit in the manifest under no kit, so the arm never reaches them;
  (c) puts a core manifest's namespace in an optional layer no target need install. RESOLVED (agent,
  2026-11-19, delegated): (a), rung 3, the precedent of `kit` and `command`, the two rows minted from
  descriptors. widens: none · relaxes: none
- **F8 — What table declares a check member, when every descriptor already holds `[check]`?** Every
  descriptor the govkit registry names, 30 (PINNED 2026-11-19 at `a30a26466`), declares the `[check]`
  table, govkit's verifier `argv` or `none`, which selfcheck 7j2 requires
  (`tools/govkit/govkit.py#selfcheck`), and TOML refuses a `[[check]]` array beside it ("Cannot overwrite a value", asked of
  `tomllib`). Options: (a) a top-level `[[numbered_check]]` table, its rows read by `derive_tag_rows`
  under `ROW_TAG_KEYS`; (b) a nested `[[check.numbered]]` array inside `[check]`; (c) rename govkit's
  `[check]`. (b) gives one table two meanings, and `read_toml_tags` reads top-level tables only; (c)
  rewrites every descriptor and govkit's readers of the table, a public-surface change veto 2
  discards.
  RESOLVED (agent, 2026-11-19, delegated): (a), rung 3, the most criteria met with no change to a
  table another reader owns. widens: none · relaxes: none
- **F9 — What owner segment does a kit whose `id` is a namespace word take?** The policy kit's `id`
  is `policy`, a namespace word since TOOL-dDeclaredLoop-18, and the namespace-word rule reds a name
  of two or more segments opening with one. Options: (a) the id with `-kit` appended,
  `leg.policy-kit.policy-check`; (b) narrow the rule for `leg`; (c) rename the policy kit's `id`; (d)
  drop the owner segment from every leg tag. (b) is the exception keyed on a namespace
  TOOL-dDeclaredLoop-18 §3 rules out; (c) is that unit's excluded rename and a public-surface change,
  veto 2; (d) breaks the `leg.<owner>.<name>` form units 22 and 28 address. The suffix is written into
  the leg tags at the pass. `extract_check` keeps `extract_command`'s raw id: an extractor reading the
  registry's words would change its output with no change to its module, which
  `tools/playbook/tag_index.py#derive_extractor_versions` hashes as the index's cache key, so a policy
  kit check row is refused on arrival rather than respelled (§5). RESOLVED (agent, 2026-11-19, delegated): (a), rung 3, the only
  option that keeps the form and both rules. widens: none · relaxes: none
- **F10 — Which check reds two manifest rows sharing one `leg` tag?** rev-6's AC3 asked `check` to,
  but the first builder's return (`2026-11-19-build-TOOL-dWitnessedBar-12-1-builder-return`) found no
  red site `run_check` reaches that compares one defining row's tag against another's:
  `tools/playbook/tag_index.py#check_namespace_joins` keeps a tag's first declaration
  (`declared.setdefault`), `tools/playbook/gov_tag.py#run_name_check` grades `sorted(set(tags))`, and
  the `two-paths` plant holds one tag defined at two paths legal. Options: (a) a duplicate-definition
  arm in `check` for the `leg` namespace alone; (b) the same arm over every namespace; (c) the gov
  canary's tag arm alone (S7), observed by AC1, with AC3 keeping its extractor half and the `leg-dup`
  plant dropped. (a) and (b) each change the shape or join check, which §3 rules out as
  PLAY-dOrderedCharter-19's and -10's, so veto 1 discards both; (b) would also red what `two-paths`
  holds legal. (c) leaves a duplicate in a manifest other than gov's own red nowhere (§5).
  Recommendation (c). RESOLVED (agent, 2026-11-19, delegated): (c), rung 3, the one option §3 leaves
  standing. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 12, the brief's shared interfaces I1
  and I2 and owned-node table, scout B's row for cl-0350, systems.md `[design-tags]`, and the
  manifest, descriptors and canary read at base `cdfbd1cf`.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edges of TOOL-dWitnessedBar-51, written by the round-1 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-26 · §3 · §4 The tag rule · §8 F5 · re-grounded on the cross-check record
  `2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck`, row 37: a leg tag's rename or retirement
  has no write path in PLAY-dOrderedCharter-15, so it is named unowned, with F5 open for the owner and
  oc15 S9 named only as the reader of retired rows.
- rev-4 · 2026-11-05 · §3 · §4 The tag rule · §8 F5 · F5 RESOLVED (owner) to (a), by the brief
  `2026-11-05-prompt-TOOL-dWitnessedBar-3-1-spec-writer`: a leg tag's rename or retirement goes to
  PLAY-dOrderedCharter-15's `new change` door, by the ask filed in dOrderedCharter's `BACKLOG.md`;
  nothing else moved.
- rev-5 · 2026-11-19 · §7 · the leg line drops `agent-instructions self-test`, which
  PLAY-dOrderedCharter-31 retired from `tools/gate-legs.json` with its kit, whose registry `[[retired]]`
  successor `playbook-render` is tested by `playbook render selftest`, already on the line; it gains
  `policy fixtures`, whose manifest guard holds the §4 path `tools/gate-legs.json`; per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-27-spec-tokens-brief; nothing else moved.
- rev-6 · 2026-11-19 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 S2 S3 S4 S5 S6 S9 · AC1 AC2 AC4 AC5 ·
  F2 F3 F4 F6 F7 F8 F9 · re-grounded at `a30a26466` per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-12-reground-brief: the manifest, descriptor and exempt counts
  are re-pinned and the tag rule re-measured, which refuses the policy kit's leg, whose owner segment
  F9 suffixes; the namespace registry's rows and its `purpose` and `owned` arms have landed, so the
  three rows are spelled whole with path-only sources (F6) and `check` in `layer.distribution` (F7);
  the descriptors' existing `[check]` table moves the check rows to `[[numbered_check]]` (F8), read
  through a factory shared with `extract_command`; `LEG_KEYS` holds the landed keys plus `tag`, and
  `owed_rows.py`, landed, reads it with its two-copies refusal deleted and S4 answering for its
  readers; the floor constants and the run-gates version are re-read; Files touched drops the retired
  agent-instructions descriptor and gains the loop and policy descriptors, `owed_rows.py`, the
  run-gates README and `help/tags.md` (S9), and the leg line gains the legs they trip or that grade
  the rows; `LEG_KEY_FLOORS`' naming cell is undeclared; citations re-pinned as `path#symbol` or
  blob-pinned.
- rev-7 · 2026-11-19 · §2 §4 §5 §6 §7 §8 §10 · S7 S8 · AC3 · F10 · per brief
  2026-11-19-prompt-TOOL-dWitnessedBar-12-2-spec-writer, over the first builder's divergence: AC3's
  duplicate half moves to the gov canary arm AC1 observes (F10) and the `leg-dup` plant is dropped;
  Files touched gains `tools/playbook/adopt-playbook.sh`, whose `run_plant_rows` heredoc takes the
  plant rows, and lists each descriptor (27, DERIVED at `d832ccb37`) as its own bullet; §5's
  observability line states what `run_check` prints; nothing else moved.
- rev-8 · 2026-11-19 · §4 · per brief 2026-11-19-prompt-TOOL-dWitnessedBar-12-pin-fix-brief: the
  descriptor list's lead-in is rewrapped so its `DERIVED` marker sits on the line carrying the row
  count; no fact changed; nothing else moved.

## 10. Reuse audit

The seams extended are PLAY-dOrderedCharter-19's registry, index and fixture and
PLAY-dOrderedCharter-10's extractor module and shape check, landed since `cdfbd1cf` as
`tools/playbook/namespaces.toml`, `tools/playbook/tag_index.py` and `tools/playbook/gov_tag.py`
(`tools/playbook/gov_tag.py#build_tags_fixture` holds the plants, and the playbook-render selftest's
`run_plant_rows` heredoc in `tools/playbook/adopt-playbook.sh` runs them); the descriptor-row extractor
`tools/playbook/tag_index.py#extract_command`, whose body becomes the factory `extract_check` shares
([reuse], second instance), with `tools/playbook/tag_index.py#derive_tag_rows` and its
`ROW_TAG_KEYS` map; the canary's two key-set literals and their landed reader
`tools/run-gates/owed_rows.py#read_known_copies`; govkit's floor constants
(`tools/govkit/govkit.py#STAGE_FLOOR_RUN_GATES` and the three before it) and their reader
`tools/govkit/govkit.py#check_target_reads_subject`, the emitter's row builder in
`tools/govkit/govkit.py#write_gate_legs`, and selfcheck 7h in `tools/govkit/govkit.py#selfcheck`.
Re-run at `a30a26466`, the lookup
`python tools/codebase-map/reuse_lookup.py "give each gate leg a tag beside its free-text name"`
ranked generic `read_text`, `legs` and `leg` stems, `TagError` and `build_tags_fixture` and named no
seam for the tag itself, which is the expected answer: no tag field exists. One disagreement with
scout B stands corrected: it counts 70 descriptor rows; at `cdfbd1cf` 68 `[[gate_leg]]` rows sat in
26 descriptors, and at `a30a26466` 70 sit in 27, which with 128 `[[exempt_leg]]` rows covers all 198
legs. The recall probe returned scout B's row, the systems-retrofit review that introduced the `tag`
field, PLAY-dOrderedCharter-19 and TOOL-dDeclaredLoop-18's brief; none disagreed with source
otherwise.

Recall terms used: `python tools/memory-recall/query.py "how does a leg get a tag in the leg namespace while its name stays the join key" --terms "leg tag namespace name join key gate-legs.json KNOWN canary key set floor run-gates check pack"`
