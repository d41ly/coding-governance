# KICK-dKeptSession-1 — the named presets as data, their completeness check, pair rules and core-only load

**Status:** INPROGRESS · rev-8 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 1 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0139@065e06ab whole
**Carries:** node:policy-key.preset

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-crosscheck-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-crosscheck-returns.md) | research | — |
| [2026-10-26-build-KICK-dKeptSession-1-departures-spec.md](../build/2026-10-26-build-KICK-dKeptSession-1-departures-spec.md) | journal | — |
| [2026-10-26-build-KICK-dKeptSession-1-deviation-11.md](../build/2026-10-26-build-KICK-dKeptSession-1-deviation-11.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-1-deviation-12.md](../build/2026-10-26-build-KICK-dKeptSession-1-deviation-12.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-1-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-1-fix-return.md) | research | KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md](../build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md) | research | — |
| [2026-10-26-build-KICK-dKeptSession-1-reground-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-reground-returns.md) | research | — |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-a.md) | research | KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-16 KICK-dKeptSession-19 KICK-dKeptSession-20 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-05-build-KICK-dKeptSession-1-deviation-13.md](../build/2026-11-05-build-KICK-dKeptSession-1-deviation-13.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md](../build/2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md) | research | KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 |
| [2026-10-26-prompt-KICK-dKeptSession-1-1-reuse-scout.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-1-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-2-reuse-scout.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-2-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-3-reuse-scout.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-3-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-4-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-4-spec-writer.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-5-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-5-spec-writer.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-6-spec-reviewer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-6-spec-reviewer.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-7-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-7-spec-writer.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md) | research | KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-owner-review-until-no-high.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-owner-review-until-no-high.md) | research | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-30-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-1-spec-writer.md) | journal | KICK-dKeptSession-30 |
| [2026-10-26-prompt-KICK-dKeptSession-56-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-56-1-spec-writer.md) | journal | KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-57-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-57-1-spec-writer.md) | journal | KICK-dKeptSession-57 |
| [2026-10-26-prompt-KICK-dKeptSession-64-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-64-1-spec-writer.md) | journal | KICK-dKeptSession-64 |
| [2026-10-26-prompt-KICK-dKeptSession-65-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-65-1-spec-writer.md) | journal | KICK-dKeptSession-65 |
| [2026-11-05-prompt-KICK-dKeptSession-1-1-spec-writer.md](../prompts/2026-11-05-prompt-KICK-dKeptSession-1-1-spec-writer.md) | journal | — |
| [2026-11-05-prompt-KICK-dKeptSession-1-owner-forks.md](../prompts/2026-11-05-prompt-KICK-dKeptSession-1-owner-forks.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-9 KICK-dKeptSession-20 KICK-dKeptSession-25 |
| [2026-11-21-prompt-KICK-dKeptSession-1-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-2-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-2-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-3-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-3-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-divergence-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md) | research | KICK-dKeptSession-19 KICK-dKeptSession-33 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

v2 names four presets, each a complete assignment of the policy keys a repository picks by one key,
`preset`, but no product file holds them: the catalogue's `preset` row lists the names
(`tools/policy/catalogue.toml#preset`) and the reader names an unapplied preset in its reason
(`tools/policy/policy.py#read_default_value`). This unit lands the presets as the policy kit's
data, the check keeping each complete and inside its keys' schemas, the pair rules over each preset
and a repository's overrides on one (`review.design.round-count` at or below `review.max-rounds`
among them), and the core-only load, each pair judged by the loop kit's one expansion rule. It arms
the preset kind the kinds register holds pending, so every reader in this build reads one store.

## 2. Scope (IN)

- **S1** — The preset store `tools/policy/presets.toml` (shared interface I1): one `[preset.<name>]`
  table per shipped preset, `velocity`, `standard`, `strict` and `guarded`, each assigning a
  presettable key by a quoted dotted key (`"hooks.bypass" = "refused"`); a top-level `never` list,
  the keys presets never touch with `preset` and `floor` among them; and a top-level `pairs` list of
  `[<higher>, <lower>]` pairs. A presettable key is a catalogue row `never` does not name whose
  default `check_derived` does not flag (`tools/policy/policy.py#check_derived`); the derived-default
  rows are KICK-dKeptSession-33's. Seeded once from the table, the never list and the pair rules of
  v2's `[presets]` section, each cell read by the seeding rules of the data model below, and each
  presettable row v2's table lacks at its catalogue default (§8 F6). Observed by AC1.
- **S2** — The shipped check, `check_presets(rows, presets)` in the new module
  `tools/policy/presets.py`, printed by `python presets.py check`: every presettable row is matched
  by at least one key of each shipped preset and every preset key matches a row, both through
  `read_catalogue_row` (`tools/policy/policy.py#read_catalogue_row`); each value passes
  `check_value(row, value)` (`tools/policy/policy.py#check_value`); `standard` equals each
  presettable row's literal default; the `preset` row's `of` and the table names are one set; each
  `never` entry names a row; each pair holds in each preset. Each finding names the preset and the
  key. Observed by AC1, AC2 and AC3.
- **S3** — The repository side, `validate`'s second table rule `check_repo_presets(doc, text, rows)`,
  imported inside `validate` unconditionally as `budgets` is, so a kit copy lacking `presets.py`
  fails closed (§8 F9) (`tools/policy/policy.py#validate`,
  `tools/policy/budgets.py#check_budgets`): a `[presets.<name>]` table in `.governance/policy.toml`
  declares a repository preset whose `extends` names a shipped preset and whose other keys are
  presettable keys, each value passing `check_value`; the file's `preset` value is admitted when it
  names a shipped or a declared preset; and the pair rules hold over the effective assignment, the
  named preset's values with the file's own keys on top. `scan_keys`
  (`tools/policy/policy.py#scan_keys`) leaves the top-level `presets` table to this rule, and
  `validate` leaves the `preset` leaf to it. Each problem is a `Problem` at the line
  `derive_key_line` finds (`tools/policy/policy.py#derive_key_line`). Observed by AC4 and AC5.
- **S4** — The core-only load, `load_preset(name, table)` in `presets.py`, printed by `python
  presets.py load <name> [--repo <dir>]`: the named preset's assignment, every pair written as one
  `<key>=<toml value>` line to one run of S8's `guard.py --expansion` per load, a refusal only where
  `check_expansion_value` (`tools/loop/guard.py#check_expansion_value`) refuses the pair.
  `presets.py` finds `guard.py` through the inlined `resolve_kit_dir("loop", "guard.py", here)`
  (`tools/policy/policy.py#resolve_kit_dir`), no `requires` edge, as the loop kit's subprocess reads
  of the playbook kit take none (`tools/loop/kit.toml#requires`); the loop kit not found, the load
  exits 2 naming it. This unit adds the `[[selects]]` row `build.closes` = `after-release-verifies` at
  `point.flow.release`, which the core Flow row of `tools/playbook/layers.toml` declares, so today's
  rule (`tools/loop/guard.py#read_core_points`) loads all four presets on the shipped register; the
  core-only refusal of `strict` and `guarded` is the ask TOOL-dDeclaredLoop-101's (§8 F2). Observed by
  AC6, AC7 and AC8.
- **S5** — The arm `arm_presets` in `ARMS` of `tools/policy/check_policy.py`
  (`tools/policy/check_policy.py#ARMS`), `empty = "finding"` because the presets ship in the kit:
  S2's findings over the shipped store, then two halves comparing each preset's S4 load with the
  expansion rule run on each `[[selects]]` pair it assigns. The by-key half reds a refusal whose key
  and value no `[[selects]]` row names. The row-named half reds a row-named pair the rule refuses and
  the load admits; where the rule admits one it prints `presets-core-only · not graded ·
  TOOL-dDeclaredLoop-2 S8 admits after-release-verifies`, no finding, so it grades once the ask's
  judgement refuses. Where `resolve_kit_dir("loop", ...)` misses, both halves print `not graded · the
  loop kit does not resolve`, no finding (§8 F7). The README's "Each arm in an adopter" row
  (`tools/policy/README.md`) says both. Observed by AC2, AC7, AC9 and AC13.
- **S6** — The preset kind (shared interface I2): the `kind.preset` row of
  `tools/playbook/kinds.toml` gains its `population` (`{prefix}/policy/presets.toml`), `factory`
  (`python {prefix}/loop/factories.py preset`), `gate` (`policy check`), `summary` and `usage`, and its
  `kind` row leaves `tools/playbook/core-pending.txt`. The factory, `write_preset(top, kit_rel,
  name, source)` through `write_kind_instance` (`tools/loop/factories.py#write_kind_instance`):
  `python <prefix>/playbook/core.py new preset <name> --from <preset>` appends a `[preset.<name>]`
  table copying the shipped preset's assignment and adds the name to the `preset` row's `of`, both
  held through the guarded write, `arm_presets` run in process as `run_policy_key_arms` runs its arms
  (`tools/loop/factories.py#run_policy_key_arms`), every held byte put back on a red. The `policy
  check` leg already enforces the kind's bind, `principle.p16` (`tools/gate-legs.json`). The kinds
  reference page re-renders from the row (`help/reference/kinds.md`). Observed by AC10.
  **Readers:** by name: `tools/playbook/core.py`, whose `kinds` and `meta-check` verbs read the
  pending list through `read_pending`, and `tools/playbook/render_playbook.py`, whose kinds page
  renders the row's `usage` · by value: `core.py kinds`' pending count, `kinds · <n> registered, <k>
  pending`, which falls by one.
- **S7** — The page `help/policy.md` gains a section on presets: the four, the never list, the pair
  rules, a repository preset, and the core-only load and the ask its refusal waits on. Observed by
  AC11.
- **S8** — The verb `guard.py --expansion` in `tools/loop/guard.py`, ruled at §8 F4 and assigned
  here by F5: it reads `<key>=<toml value>` lines on stdin, judges each with
  `check_expansion_value(key, value, read_core_points(), top)`, `top` the working directory's
  repository, prints one `loop-guard: refused · <where> · <why>` line per refused pair naming the
  key, value and point, passes the rule's `fallback` line through as no refusal, and exits 2 on any
  refusal or unreadable line, else 0, copying no part of the rule. Observed by AC6 and AC12.

## 3. Non-goals (OUT)

- The reader applying a preset: KICK-dKeptSession-2's step reads this store.
- The charter's preset section, intake's preset answer and a scenario's preset slot: units 3, 4 and
  20.
- The `[[selects]]` row for `build.closes` = `at-landing-maintain-owns`: no shipped preset sets it,
  and dShippedRelease, which owns the key and its reader, adds it with that reader.
- A preset store per stage or per build: v2 assigns per repository.
- The `on-invalid-strict` fixture case's strict-cell parser
  (`tools/policy/check_policy.py#derive_strict_value`): it reads v2 as the build's acceptance probe, a
  record, and stays.
- The judgement that refuses a value whose core point no installed expansion attaches at, and the
  `needs` field a `[[selects]]` row would carry for it: the ask TOOL-dDeclaredLoop-101 (§8 F2).
- A value per shipped preset in `new policy-key`: the ask TOOL-dDeclaredLoop-102 (§8 F3).
- The derived-default rows, their unassigned rule and the literal `maintain.fixes` sets:
  KICK-dKeptSession-33.

### Edges

- **hands-off** `KICK-dKeptSession-2` — `presets.toml` and `derive_preset_assignment`, which the reader's preset step answers from
- **hands-off** `KICK-dKeptSession-3` — `presets.toml`, against which the charter section prints only the keys that differ
- **hands-off** `KICK-dKeptSession-4` — `presets.toml`, whose shipped names intake admits as the `preset` answer
- **hands-off** `KICK-dKeptSession-20` — `presets.toml` and its `never` list, which a scenario's preset slot reads and may not set
- **hands-off** `KICK-dKeptSession-9` — `presets.toml`, whose strict table holds `orient.budget` = `warn-at-evidence-ceiling`
- **hands-off** `KICK-dKeptSession-7` — `presets.toml`, whose strict table holds the `deps.coordination` and `deps.early-build` cells
- **consumes-from** external — the policy kit's `check_value`, `check_derived`, `read_catalogue_row`, `scan_keys`, `derive_key_line`, `validate` with its `budgets` table rule, `resolve_kit_dir`, and `check_policy.py`'s `ARMS`, `run_arm` and fixture; the loop kit's `check_expansion_value`, `read_core_points` and `[[selects]]` rows in `tools/loop/guard.py` and `tools/loop/loop.toml`, and its factory module `tools/loop/factories.py`; the playbook kit's `kinds.toml`, `core-pending.txt`, `core.py new` and `core.py kinds`, and the layer register `tools/playbook/layers.toml`; each landed at this spec's base
- **hands-off** external — the attached-point judgement in `check_expansion_value` (§8 F2, TOOL-dDeclaredLoop-101) and a value per shipped preset in `new policy-key` (§8 F3, TOOL-dDeclaredLoop-102), each an open ask in dDeclaredLoop's `BACKLOG.md`
- **hands-off** `KICK-dKeptSession-33` — `presets.toml` and `check_presets`, whose rule for the eight derived-default rows that unit states (id 17)
- **hands-off** `KICK-dKeptSession-44` — `arm_presets`' row-named half, `check_repo_presets`' shipped-name collision, the never-list comment and the one pair rule, the batch's S1, S32, S38 and S41 (ids 3, 62, 18, 43)

## 4. Design

### Data model

```toml
# tools/policy/presets.toml — the shipped presets; one table per name, quoted dotted keys
never = ["floor", "preset", "policy-file.guard", "policy-file.proof", "policy-file.on-invalid",
         "charter.practices", "instructions.edit", "...", "platforms.provision"]   # v2 [presets], Rules
pairs = [["review.max-rounds", "review.design.round-count"],
         ["install.deprecation-window", "currency.max-behind"]]

[preset.velocity]
"hooks.bypass" = "allowed"
"review.max-rounds" = 2
# … every presettable key

[preset.strict]
"hooks.bypass" = "refused"
"build.closes" = "after-release-verifies"
"review.max-rounds" = 4
# …
```

```toml
# .governance/policy.toml — a repository preset (S3)
preset = "ours"

[presets.ours]
extends = "strict"
"leases.expiry-hours" = 12
```

```toml
# tools/loop/loop.toml — the row this unit adds (S4)
[[selects]]
key = "build.closes"
value = "after-release-verifies"
point = "point.flow.release"
```

The release slot is a core point, Flow's in Deploy, where integrations' engines attach
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md@c2a407b0:179`),
spelled `point.flow.release` on the core Flow row and in the `uses` of `layer.integrations`, a row
no kit descriptor names today (`tools/playbook/layers.toml`).

The seed reads each cell of v2's table as `derive_strict_value` reads a strict cell
(`tools/policy/check_policy.py#derive_strict_value`), with three rules for the prose cells that
reader leaves as text:

| Cell | Read as | Rows today |
|---|---|---|
| `none` on a set-valued row | `[]` | `review.opt-in`, `runtime.attended-allowance`, `review.breakpoints`, `probe.points` |
| `all three`, `all four triggers` on a set-valued row | the row's whole `of` list, in its order | `maintain.events`, `design.reentry` |
| a member of the row's `or` list | that member, a string | `tests.landing-levels` = `every-declared` in `strict` |

A cell on a derived-default row is not seeded (S1). The `runtime.journal` pair binds only while
observability is installed (v2's pair rules), so it is not a `pairs` row until that expansion lands
its key's reader. The seeded pairs hold in all four presets.

### The checks

```
presets.py check                       # S2 over the shipped store; exit 0 green, 1 red
presets.py load <name> [--repo <dir>]  # S4; exit 0 loaded, 2 refused, one line per refused key
printf '%s\n' '<key>=<toml>' | python <prefix>/loop/guard.py --expansion   # S8; exit 0, 2 refused
python <prefix>/playbook/core.py new preset <name> --from <preset>        # S6, through factories.py
```

`derive_preset_assignment(name, presets, table)` returns `{key path: value}` for a shipped name, or
for a repository name its shipped `extends` assignment with the table's keys on top: the one
assignment every reader takes (KICK-dKeptSession-2's step, unit 20's scenario). A repository preset
extends a shipped one only, so the walk is one level.

The repository pair rule judges the effective assignment, the named preset's with the file's
top-level keys on top, so `review.design.round-count = 4` under `standard` (`review.max-rounds` 3)
is refused at its line. A pair whose two keys are unset in both binds nothing.

`arm_presets` runs `load_preset` and S8's verb once per shipped preset, the verb over the
`[[selects]]` pairs it assigns, read from `loop.toml` through the same `resolve_kit_dir`. The runs
share nothing but the rule they are compared against, so a planted loader refusing by key, or
admitting every value, reds.

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `tools/policy/presets.toml` | data file | new |
| `load_presets`, `derive_preset_assignment`, `check_presets`, `check_repo_presets`, `load_preset` | functions | `tools/policy/presets.py` (new) |
| `arm_presets` | arm | `tools/policy/check_policy.py` |
| `presets-complete`, `presets-pairs`, `presets-repo`, `presets-core-only` | fixture cases | `tools/policy/check_policy.py` |
| `--expansion` | verb | `tools/loop/guard.py` |
| `write_preset`, the `preset` subcommand | function and verb | `tools/loop/factories.py` |
| `preset-new`, `preset-from-unknown` | fixture plants | `tools/loop/factories.py` |

### Migration

`.governance/policy.toml` gains no key, and this unit changes no read: a named preset reads every
key at its default until KICK-dKeptSession-2.

### Rollout

The store lands with its arm, the reader's step in unit 2. The `[[selects]]` row moves no verdict
today, its point core-declared: `policy_edit.py set build.closes after-release-verifies` is
admitted as before.

### Files touched (estimate)

- `tools/policy/presets.toml` (new)
- `tools/policy/presets.py` (new)
- `tools/policy/policy.py`: `validate` calls `check_repo_presets`; `scan_keys` leaves `presets`
- `tools/policy/check_policy.py`: `arm_presets` and the four cases
- `tools/policy/README.md`: the arm's row
- `tools/loop/guard.py`: S8's verb and its docstring line
- `tools/loop/loop.toml`: the `[[selects]]` row
- `tools/loop/factories.py`: the `preset` subcommand, its gate and two plants
- `tools/loop/README.md`: the verb and the seventh factory
- `tools/playbook/kinds.toml`: the `kind.preset` row
- `tools/playbook/core-pending.txt`: the row out
- `tools/gate-legs.json`: the `policy fixtures` row's `guard` gains `{prefix}/loop/` and
  `{prefix}/playbook/layers.toml`, the two paths §6's copy reads, which its guard trace grades WRONG
  today (`tools/policy/check_policy.py#check_guard_trace`); the path trips `run-gates canary`, `run-gates
  gov canary`, `measure-legs selftest` and `policy fixtures`, each on §7's leg line
- `help/reference/kinds.md`: re-rendered by `render_playbook.py --reference`
- `help/policy.md`
- each partial policy-kit copy gains `presets.py` and `presets.toml` (§8 F9):
  `tools/check-line-length.test.sh` (`build_repo`), `tools/hooks/agent-cap.test.sh` (rule 7's
  `LIMPK` loop), `tools/unattended/check-unattended.test.sh` (`seed_bound_kits`),
  `tools/unattended/unattended.test.sh` (`write_switch_fixture`)

### Alternatives rejected

- **Four preset fields per catalogue row**: a second owner on every one-owner row.
- **The store generated from v2 each run**: a product kit reads no record at run time.
- **The pair rule as an arm only**: the guard would commit a file the bar then reds (§8 F1).
- **A loader refusing a key an absent expansion owns**: v2 rules it out, the key being unread; AC7
  plants it as a break.
- **A factory in `presets.py`**: `tools/loop/factories.py` holds the guarded write, restore and gate
  wrapper each kind's factory shares; a copy is the `[reuse]` defect.

## 5. Production-readiness checklist

- security — readers never write the store; the factory is its one writer, gated under the guarded
  write; a repository preset passes `validate` at the policy guard, deny by default for a name
  neither shipped nor declared, and a kit copy lacking `presets.py` fails closed (§8 F9).
- perf / scale — one TOML read per check; two `guard.py` subprocesses per preset, never one per key.
- error / empty / loading states — an absent store is a refusal naming `presets.toml`; a malformed
  one a finding at its line; an unreadable verb line a refusal naming it; no loop kit, the load
  halves announce, never a finding (§8 F7).
- observability — each finding names the preset and the key; the load the key, value and point.
- risks — a key added after this unit has no preset value and the `policy check` leg reds it until
  its build adds them or TOOL-dDeclaredLoop-102 lands (§8 F3).
- testing — the four fixture cases and two plants of the criteria below, and the arm.
- migration — none; no read changes.
- user docs — `help/policy.md`, S7, and the kinds reference page, S6.

## 6. Acceptance criteria

The policy fixture is `check_policy.py --fixture`: one scratch repository per case under `%TEMP%`,
the kit at its own path, a policy file committed with a remote-tracking ref. A case reaching the
loop kit also copies it whole and the playbook kit's `layers.toml`, the two paths the `policy
fixtures` guard gains (§4).

- **AC1** — When `python presets.py check` runs in the policy kit, it exits 0 and prints the four
  preset names with one presettable count for each.
  Red when: a shipped preset lacks a presettable key, names a `never` key, or holds a value its row
  refuses.
  figure: the count is DERIVED from the catalogue, `never` and `check_derived` at each run.
- **AC2** — When `python check_policy.py --fixture presets-complete` runs, each plant reds
  `arm_presets` naming its preset and key: a key cut from `strict`, `hooks.bypass` set to `maybe` in
  `guarded`, `standard`'s `leases.expiry-hours` set off its catalogue default, and a fifth table the
  `preset` row's `of` lacks; each unplanted copy is green.
  Red when: a plant reads green.
- **AC3** — When the `presets-pairs` case sets `review.design.round-count` 5 in the `velocity` table,
  whose `review.max-rounds` is 2, `arm_presets` reds naming the pair and the preset.
  Red when: a preset breaking a pair loads clean.
- **AC4** — When the `presets-pairs` case commits, as the file's only revision, `preset = "standard"`
  and `review.design.round-count = 4`, `python policy.py check` exits 2, its stderr line opening
  `policy: refused ·` at the override's line, naming both keys and `no valid revision`; with the
  override at 3 it exits 0 printing `is valid`.
  Red when: an override past `review.max-rounds` passes `validate`.
  fixture: no valid revision precedes, so `cmd_check` refuses rather than falls back (§8 F8).
- **AC5** — When the `presets-repo` case commits `[presets.ours]` extending `strict` with one
  override and `preset = "ours"`, `python policy.py check` exits 0; committed alone with `extends =
  "lax"`, or `"policy-file.guard"` inside the table, it exits 2, the refusal line naming the key.
  Red when: a declared preset extends no shipped one, or sets a `never` key, and passes.
- **AC6** — When the `presets-core-only` case runs `python presets.py load <name>` for each shipped
  preset in a scratch tree whose register copy's core Flow row declares no `point.flow.release`,
  `velocity` and `standard` exit 0 and `strict` and `guarded` exit 2, each naming `build.closes`,
  `after-release-verifies` and the point, and no other key; over the shipped register all four
  exit 0.
  Red when: a preset is refused for a key its value does not select, or `strict` loads where the
  rule refuses its value.
  fixture: the register copy stands in for the core-only judgement the ask TOOL-dDeclaredLoop-101
  owes; on a real core-only install `strict` loads until that ask lands.
- **AC7** — When the `presets-core-only` case plants `absent-by-key`, a loader refusing any key a
  `[[selects]]` row names whatever its value, `arm_presets` reds naming `standard` and
  `build.closes`; when it plants `accept-all`, a loader admitting every value, over the same register
  copy, it reds naming `strict` and `build.closes`.
  Red when: either planted loader reads green.
- **AC8** — When `grep -n "build.closes" loop.toml` runs in the loop kit, it prints the
  `[[selects]]` row naming `after-release-verifies` and `point.flow.release`.
  Red when: the row is absent, so no rule ever judges `strict`'s value.
- **AC9** — When `python check_policy.py --repo .` runs at the repository root, it prints
  `policy-check: arm_presets · 0 finding(s)` with a population of four presets and the row-named
  half's `presets-core-only · not graded` line.
  Red when: the arm is absent from `ARMS`, announces itself, or reds the shipped tree for the open
  ask.
- **AC10** — When `python factories.py --fixture --plant preset-new` runs, `core.py new preset trial
  --from standard` in the scratch clone gives `presets.toml` a `[preset.trial]` table and the
  `preset` row's `of` the name `trial`, the gate prints green, and `python core.py kinds` prints
  `kind.preset` off the pending list; the `preset-from-unknown` plant's `--from nope` exits 2 naming
  it, and both files keep their bytes.
  Red when: the factory leaves a non-conforming preset, writes before refusing, or the kind stays
  pending.
- **AC11** — When `grep -n "never touch\|pair rule\|core-only" policy.md` runs in the help directory,
  it prints the presets section's three paragraphs.
  Red when: the page omits presets.
- **AC12** — When `printf 'build.closes="after-release-verifies"\n' | python tools/loop/guard.py
  --expansion` runs at the repository root, it exits 0 and prints no refusal; fed the line `x` it
  exits 2 naming the line.
  Red when: the verb is absent, refuses a core-declared point, or reads an unparsed line as admitted.
- **AC13** — When `python check_policy.py --fixture adopter-fresh-target` runs, each installed
  `--check` prints `arm_presets` graded with no finding and both load halves' `not graded · the loop
  kit does not resolve`, and the README's `arm_presets` row joins `ARMS`.
  Red when: the arm reds a target without the loop kit, or prints a half graded there.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy check` · `policy fixtures` · `loop guard fixtures` · `loop factories fixtures` · `core kinds` · `core meta-check` · `help reference pages` · `scratch-guard self-test` · `line-length gate selftest` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC9 AC13 · the four `presets-*` cases' plants, each staged on a copy of the shipped store, the loader or the register, and `adopter-fresh-target`'s halves check · none
New arm: tools/loop/factories.py · covers AC10 · the `preset-new` plant's factory run and the `preset-from-unknown` plant's `--from nope` · none

## 8. Open questions

- **F1 — Where does the pair rule over a repository's overrides run?** (a) In `validate`, as a
  second table rule beside `budgets.check_budgets`, so the guard refuses the commit and the reader
  falls back to the last valid revision; (b) an arm only, so the guard commits a file the bar reds.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2's Rules (a check refuses) and the seam
  dGroundRules-9 built. widens: none · relaxes: none
- **F2 — How is `after-release-verifies` refused on a core-only install, when its point is core?**
  `check_expansion_value` refuses a value only where no core row declares its point
  (`tools/loop/guard.py#read_core_points`), and the core Flow row declares the release slot. (a) Ask
  dDeclaredLoop to judge a `[[selects]]` row carrying `needs = "attached"` absent unless an installed
  row lists its point in `uses`; (b) a point no core row declares, where EX-1 forbids an expansion to
  attach (`tools/playbook/check_layers.py#check_point`); (c) a refusal in this kit's loader, a second
  copy of the rule gap-spine-07 names. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, one rule
  and a value an installed expansion can admit. The ask is TOOL-dDeclaredLoop-101
  (`memory/builds/dDeclaredLoop/BACKLOG.md`), accept: such a row is refused unless an installed
  layer row's `uses` lists its point, seen red on a core-only fixture admitting
  `after-release-verifies`. Until then the row-named half prints not graded (S5) and AC6 observes
  the refusal over a register copy. widens: none · relaxes: none
- **F3 — Does a new catalogue key land without a value in every shipped preset?** v2's Rules say it
  cannot. `new policy-key` writes only the catalogue row, gated by four arms that never run
  `arm_presets` (`tools/loop/factories.py#POLICY_KEY_ARMS`), so the `policy check` leg reds the key
  after. (a) Ask dDeclaredLoop for a `--preset <name>=<toml>` per shipped preset, or `--never`,
  written into `presets.toml` in the same restore; (b) a default copied into every preset, wrong for
  a posture key by v2's strict and guarded columns. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 1, v2's Rules. The ask is TOOL-dDeclaredLoop-102, accept: `new policy-key` refuses a
  presettable key missing a shipped preset's value, seen red with the `strict` value absent.
  widens: none · relaxes: none
- **F4 — How does `presets.py` reach `check_expansion_value`, when `guard.py` has no verb printing its
  verdict?** A kit imports no sibling kit, and the function lives in `tools/loop/guard.py`, whose
  flags are `--staged`, `--push-range`, `--fixture` and `--selftest` (`tools/loop/guard.py#main`).
  Options: (a) `guard.py --expansion` reads `<key>=<value>` lines on stdin, judges each with
  `check_expansion_value`, prints one line per refused pair naming the key, the value and the point,
  and exits 2 on any refusal, run by S4 as one subprocess per load; (b) a declared `requires_if` row
  on `tools/policy/kit.toml` naming `loop`, `presets.py` importing the function in process.
  Recommendation (a). RESOLVED (owner, 2026-11-05): (a) the `guard.py --expansion` ask, its text
  "TOOL-dDeclaredLoop-2 S8: `guard.py --expansion` judges `<key>=<value>` lines on stdin with
  `check_expansion_value`, one line per refusal, exit 2 on any".
- **F5 — Who lands F4's verb, now that dDeclaredLoop has landed without it?** dDeclaredLoop landed
  at `9e21ac76`, and no row of its `BACKLOG.md` carries the verb. (a) This unit, as S8, the ruled
  text its acceptance; (b) file the ask, S4, AC6, AC7 and the load halves waiting on a run no plan
  schedules; (c) the in-process load of `guard.py` by path
  (`tools/playbook/instructions_edit.py#read_loop_guard`), which F4 declined. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3; every term the owner ruled kept, only the builder moved, and
  the one option under which this unit's load runs. widens: none · relaxes: none
- **F6 — What does each preset assign a presettable row v2's table lacks?** Six presettable rows
  joined the catalogue after v2: `review.spec-audit.disposal`, `review.spec-audit.chain-stop`,
  `review.spec-audit.chain-ceiling`, `bar.inline-red-fixes`, `pass.fast-legs` and
  `memory.staged-render`. (a) Its catalogue default in all four, the value the standard rule demands,
  no posture moving until its owner sets one; (b) a value per preset chosen here, a posture no
  owner record states; (c) the never list, which v2 closes. RESOLVED (agent, 2026-11-21, delegated):
  (a), rung 3; every rule holds with nothing invented. widens: none · relaxes: none
- **F7 — What do the load halves do where the loop kit does not resolve?** `adopter-fresh-target`
  installs policy, its `requires` closure and run-gates (`tools/policy/README.md`, "Each arm in an
  adopter"), no loop kit, so a miss under `empty = "finding"` reds it. (a) Each half prints `not
  graded · the loop kit does not resolve`, the store still graded, as the loop kit's cross-kit reads
  degrade (`tools/loop/kit.toml#requires`); (b) a finding; (c) a `loop` edge no policy read needs.
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the main loop's ruling on run
  `wf_c7d6ba36-6f3`. widens: none · relaxes: none
- **F8 — What do AC4 and AC5 observe, when `policy.py check` never exits 1?** It exits 0 for a file
  valid, absent, or invalid with a last valid revision, else 2 on a refusal
  (`tools/policy/policy.py#cmd_check`, `#read_last_valid_value`), exits
  `tools/policy/check_policy.py#run_on_invalid_classes` pins. (a) Exit 2 and its refusal line over a
  fixture committing no valid revision first; (b) an exit 1 for an invalid file, moving that pinned
  contract for two criteria. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3, the main loop's ruling on run `wf_73059b2b-dc2`; `cmd_check`
  is untouched. widens: none · relaxes: none
- **F9 — How does `validate` reach `presets` where a suite copies part of the policy kit?** Four
  suites copy `policy.py` without `presets.py` and commit a policy file `validate` reads (§4 Files
  touched). (a) Each copies `presets.py` and `presets.toml`, `validate` importing `presets`
  unconditionally, so the pair rules fail closed; (b) `validate` skipping where `presets.py` is
  absent, a silent pass under deny by default. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3,
  the main loop's ruling on run `wf_73059b2b-dc2`, narrowed at rev-8 from five:
  `tools/workflows/unattended-build.test.sh#build_layout` commits no policy file. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-33`, `KICK-dKeptSession-44`
  mirrored, the other ends of the edges the round-1 spec audit's promoted units declare; no other
  section moved.
- rev-3 · 2026-10-26 · S4 · §3 Edges · §5 · AC6 · §8 F4 · §10 · re-grounded on the cross-check record
  `2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`, row 3: `presets.py` reaches
  `check_expansion_value` by subprocess through the policy kit's inline `resolve_kit_dir`, with F4
  open for the `guard.py` verb.
- rev-4 · 2026-11-05 · S4 · AC6 · §8 F4 · F4 resolved by the owner to (a), the `guard.py --expansion`
  ask filed in dDeclaredLoop's `BACKLOG.md`, under the brief
  `2026-11-05-prompt-KICK-dKeptSession-1-owner-forks`; no other section moved.
- rev-5 · 2026-11-21 · S1 S2 S3 S4 S5 S6 S7 S8 · §3 · §4 · §5 · AC1 AC2 AC6 AC7 AC8 AC9 AC10 AC12 · §7
  · §8 F2 F3 F4 F5 F6 · §10 · re-grounded on the landed tree at `c2a407b0` under the brief
  `2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief`. Narrowed: the derived-default
  rows leave S1 and S2 to unit 33; the `needs` field leaves the `[[selects]]` row for ask
  TOOL-dDeclaredLoop-101; the `gate-legs.json` and `kit.toml` edits leave Files touched, already
  satisfied; the factory moves into `factories.py`; the row-named half prints not graded while the
  ask is open. Added: S8, the verb (F5), the seed's cell rules and the six rows v2 lacks (F6), AC12,
  the factories arm; every line-number citation re-cited by symbol or blob pin.
- rev-6 · 2026-11-21 · S5 S6 · §4 · §5 · §6 · AC13 · §7 · §8 F7 · the divergence ruled under the
  brief `2026-11-21-prompt-KICK-dKeptSession-1-divergence-brief`: `tools/gate-legs.json` rejoins
  Files touched, correcting rev-5's "already satisfied"; the halves announce a missing loop kit (F7).
- rev-7 · 2026-11-21 · S2-S6 S8 · §4 · §5 · AC4 AC5 · §7 · §8 F1-F3 F5-F9 · §10 · the second
  divergence ruled under the brief `2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief`: AC4
  and AC5 observe exit 2 and the refusal line (F8); the five partial policy-kit copies and the legs
  they trip join (F9); the rest trimmed under the size cap, no term moved.
- rev-8 · 2026-11-21 · §1 · §4 · §6 · AC7 · §7 · §8 F9 · brief
  `2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief`: F9 narrowed to four suites; the fifth
  and the two legs only it tripped leave.

## 10. Reuse audit

The seams extended: `check_value`, `check_derived` and `read_catalogue_row`
(`tools/policy/policy.py#check_value`, `#check_derived`, `#read_catalogue_row`); `validate`'s
table-rule seam, the `budgets` call (`tools/policy/policy.py#validate`); `ARMS` and `run_arm`
(`tools/policy/check_policy.py#ARMS`, `#run_arm`); `derive_strict_value` for the seed;
`check_expansion_value` (`tools/loop/guard.py#check_expansion_value`) by subprocess through
`resolve_kit_dir` (`tools/policy/policy.py#resolve_kit_dir`); `write_kind_instance` and
`run_policy_key_arms` (`tools/loop/factories.py`); and the kinds contract
(`tools/playbook/core.py#run_kinds`, `#run_new`). The prior art,
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-preset-check.py`, gives its never
set, completeness and allowed-value checks and `PAIRS`, not its `FREE` regex, since `check_value`
judges the parsed `allowed` table. `python tools/codebase-map/reuse_lookup.py "named policy presets
completeness check pair rules"` (2026-11-21) and `"kind factory guarded write restore gate"` ranked
name stems only (`check`, `pair`, `write`, `write_text`): no preset code is in the tree, and the
factory module was found through the kinds register's `factory` cells. `python
tools/memory-recall/query.py` with the terms below returned scout A's row 1, this build's brief and
the flow review's M1 (`memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-flow-b.md`),
naming `build.closes` as the key a core-only install refuses. Disagreement with the earlier text: §8
F2 and F3.

Recall terms used: preset presets completeness pair rules never-touch strict guarded build.closes selects expansion core-only
