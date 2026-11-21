# KICK-dKeptSession-1 — the named presets as data, their completeness check, pair rules and core-only load

**Status:** INPROGRESS · rev-9 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 1 · advances KICK-dKeptSession-29

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
| [2026-11-21-prompt-KICK-dKeptSession-1-4-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-4-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-divergence-3-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-divergence-3-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-divergence-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md) | research | KICK-dKeptSession-19 KICK-dKeptSession-33 |
| [2026-11-21-prompt-KICK-dKeptSession-1-rebuild-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-rebuild-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

v2 names four presets, each a complete assignment of the policy keys a repository picks by one key,
`preset`, but no product file holds them: the catalogue's `preset` row lists the names
(`tools/policy/catalogue.toml#preset`) and the reader names an unapplied preset in its reason
(`tools/policy/policy.py#read_default_value`). This unit lands the presets as the policy kit's
data, the check keeping each complete and inside its keys' schemas, the pair rules over each preset
(`review.design.round-count` at or below `review.max-rounds` among them), the repository presets a
policy file declares, and the core-only load, each pair judged by the loop kit's one expansion rule. It arms
the preset kind the kinds register holds pending, so every reader in this build reads one store.

## 2. Scope (IN)

- **S1** — The preset store `tools/policy/presets.toml` (shared interface I1): one `[preset.<name>]`
  table per shipped preset, `velocity`, `standard`, `strict` and `guarded`, each assigning a
  presettable key by a quoted dotted key (`"hooks.bypass" = "refused"`); a top-level `never` list,
  the keys presets never touch with `preset` and `floor` among them; and a top-level `pairs` list of
  `[<higher>, <lower>]` pairs. A presettable key is a catalogue row `never` does not name whose
  default `check_derived` does not flag (`tools/policy/policy.py#check_derived`); the derived-default
  rows are KICK-dKeptSession-33's. Seeded once from v2's `[presets]` section by the data model's
  rules, each presettable row v2 lacks at its catalogue default (§8 F6). Observed by AC1.
- **S2** — The shipped check, `check_presets(rows, presets)` in the new module
  `tools/policy/presets.py`, printed by `python presets.py check`: every presettable row is matched
  by at least one key of each shipped preset and every preset key matches a row, both through
  `read_catalogue_row` (`tools/policy/policy.py#read_catalogue_row`); each value passes
  `check_value(row, value)` (`tools/policy/policy.py#check_value`); `standard` equals each
  presettable row's literal default; the `preset` row's `of` and the table names are one set; each
  `never` entry names a row; each pair holds in each preset, the pair rules' one home (§8 F10). Each
  finding names the preset and the key. Observed by AC1, AC2, AC3 and AC4.
- **S3** — The repository side, `check_repo_presets(doc, text, rows)`, which `validate` imports and
  calls after `budgets` only for a file holding a top-level `presets` table (§8 F9)
  (`tools/policy/policy.py#validate`): each `[presets.<name>]` table declares a repository preset
  whose `extends` names a shipped preset and whose other keys are presettable, each value passing
  `check_value`, and the file's `preset` leaf is admitted when it names a shipped or a declared
  preset. A file without the table is judged as at the base; one holding it where `presets` does not
  import is one `Problem` naming `presets.py`. `validate` judges no pair: a repository file's round
  count above its ceiling stays `tools/loop/review_bounds.py#derive_review_bounds`' refusal (§8 F10).
  `scan_keys` (`tools/policy/policy.py#scan_keys`) leaves the `presets` table to this rule, each
  problem at the line `tools/policy/policy.py#derive_key_line` finds. Observed by AC4 and AC5.
- **S4** — The core-only load, `load_preset(name, table)` in `presets.py`, printed by `python
  presets.py load <name> [--repo <dir>]`: the named preset's assignment, every pair written as one
  `<key>=<toml value>` line to one run of S8's `guard.py --expansion` per load, a refusal only where
  `check_expansion_value` (`tools/loop/guard.py#check_expansion_value`) refuses the pair.
  `presets.py` finds `guard.py` through the inlined `resolve_kit_dir("loop", "guard.py", here)`
  (`tools/policy/policy.py#resolve_kit_dir`), no `requires` edge (§8 F7); the loop kit not found,
  the load exits 2 naming it. This unit adds the `[[selects]]` row `build.closes` =
  `after-release-verifies` at `point.flow.release`, which the core Flow row of
  `tools/playbook/layers.toml` declares, so today's rule (`tools/loop/guard.py#read_core_points`)
  loads all four presets on the shipped register; the core-only refusal of `strict` and `guarded` is
  the ask TOOL-dDeclaredLoop-101's (§8 F2). Observed by AC6, AC7 and AC8.
- **S5** — The arm `arm_presets` in `ARMS` of `tools/policy/check_policy.py`
  (`tools/policy/check_policy.py#ARMS`), `empty = "finding"` because the presets ship in the kit:
  S2's findings over the shipped store, then two halves comparing each preset's S4 load with the
  rule run on each `[[selects]]` pair it assigns. The by-key half reds a refusal no `[[selects]]` row
  names; the row-named half a row-named pair the rule refuses and the load admits; where the rule admits one it prints `presets-core-only · not graded ·
  TOOL-dDeclaredLoop-2 S8 admits after-release-verifies`, no finding. Where the loop kit does not
  resolve, both halves print `not graded · the loop kit does not resolve`, no finding (§8 F7), as the
  README's "Each arm in an adopter" row says (`tools/policy/README.md`). Observed by AC2, AC7, AC9
  and AC13.
- **S6** — The preset kind (shared interface I2): the `kind.preset` row of
  `tools/playbook/kinds.toml` gains its `population` (`{prefix}/policy/presets.toml`), `factory`
  (`python {prefix}/loop/factories.py preset`), `gate` (`policy check`), `summary` and `usage`, and its
  `kind` row leaves `tools/playbook/core-pending.txt`. The factory, `write_preset(top, kit_rel,
  name, source)` through `write_kind_instance` (`tools/loop/factories.py#write_kind_instance`):
  `python <prefix>/playbook/core.py new preset <name> --from <preset>` appends a `[preset.<name>]`
  table copying the shipped preset's assignment and adds the name to the `preset` row's `of`, both
  held through the guarded write, `arm_presets` run in process as
  `tools/loop/factories.py#run_policy_key_arms` runs its arms, every held byte put back on a red. The
  `policy check` leg already enforces the kind's bind, `principle.p16` (`tools/gate-legs.json`); the
  kinds reference page re-renders (`help/reference/kinds.md`). Observed by AC10.
  **Readers:** by name: `tools/playbook/core.py`'s `kinds` and `meta-check` through `read_pending`,
  and `tools/playbook/render_playbook.py`'s kinds page · by value: `core.py kinds`' pending count,
  `kinds · <n> registered, <k> pending`, which falls by one.
- **S7** — The page `help/policy.md` gains a section on presets: the four, the never list, the pair
  rules, a repository preset, and the core-only load and the ask its refusal waits on. Each
  `presets.py` command it shows, `check` and `load`, has its `[[usage]]` row in
  `tools/govkit/usage.toml`, which `tools/govkit/docs_leg.py#read_usage_rows` reads, and the page
  that row's usage anchor. Observed by AC11.
- **S8** — The verb `guard.py --expansion` in `tools/loop/guard.py`, ruled at §8 F4 and assigned
  here by F5: it reads `<key>=<toml value>` lines on stdin, judges each with
  `check_expansion_value(key, value, read_core_points(), top)`, `top` the working directory's
  repository, prints one `loop-guard: refused · <where> · <why>` line per refused pair, passes the
  rule's `fallback` line through as no refusal, and exits 2 on any refusal or unreadable line, else
  0, copying no part of the rule. Observed by AC6 and AC12.

## 3. Non-goals (OUT)

- The reader applying a preset: KICK-dKeptSession-2's step reads this store.
- The charter's preset section, intake's preset answer and a scenario's preset slot: units 3, 4 and
  20.
- The `[[selects]]` row for `build.closes` = `at-landing-maintain-owns`: no shipped preset sets it,
  and dShippedRelease, which owns the key and its reader, adds it with that reader.
- A preset store per stage or per build: v2 assigns per repository.
- The `on-invalid-strict` case's strict-cell parser (`tools/policy/check_policy.py#derive_strict_value`),
  an acceptance probe reading v2, which stays.
- The judgement that refuses a value whose core point no installed expansion attaches at, and the
  `needs` field a `[[selects]]` row would carry for it: the ask TOOL-dDeclaredLoop-101 (§8 F2).
- A value per shipped preset in `new policy-key`: the ask TOOL-dDeclaredLoop-102 (§8 F3).
- The derived-default rows, their unassigned rule and the literal `maintain.fixes` sets:
  KICK-dKeptSession-33.
- A repository file's pair: `derive_review_bounds`' refusal under `fixed-count` (§8 F10).

### Edges

- **hands-off** `KICK-dKeptSession-2` — `presets.toml` and `derive_preset_assignment`, which the reader's preset step answers from
- **hands-off** `KICK-dKeptSession-3` — `presets.toml`, against which the charter section prints only the keys that differ
- **hands-off** `KICK-dKeptSession-4` — `presets.toml`, whose shipped names intake admits as the `preset` answer
- **hands-off** `KICK-dKeptSession-20` — `presets.toml` and its `never` list, which a scenario's preset slot reads and may not set
- **hands-off** `KICK-dKeptSession-9` — `presets.toml`, whose strict table holds `orient.budget` = `warn-at-evidence-ceiling`
- **hands-off** `KICK-dKeptSession-7` — `presets.toml`, whose strict table holds the `deps.coordination` and `deps.early-build` cells
- **consumes-from** external — the policy kit's `check_value`, `check_derived`, `read_catalogue_row`, `scan_keys`, `derive_key_line`, `validate`, `resolve_kit_dir`, `ARMS` and `run_arm`; the loop kit's `check_expansion_value`, `read_core_points`, `[[selects]]` rows, `derive_review_bounds` and `tools/loop/factories.py`; the playbook kit's `kinds.toml`, `core-pending.txt`, `core.py` and `tools/playbook/layers.toml`; govkit's `usage.toml`; each landed at this spec's base
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
`point.flow.release` on the core Flow row and in the `uses` of `layer.integrations`, which no kit
descriptor names today (`tools/playbook/layers.toml`).

The seed reads each cell of v2's table as `derive_strict_value` reads a strict cell
(`tools/policy/check_policy.py#derive_strict_value`), with three rules for the prose cells that
reader leaves as text:

| Cell | Read as | Rows today |
|---|---|---|
| `none` on a set-valued row | `[]` | `review.opt-in`, `runtime.attended-allowance`, `review.breakpoints`, `probe.points` |
| `all three`, `all four triggers` on a set-valued row | the row's whole `of` list, in its order | `maintain.events`, `design.reentry` |
| a member of the row's `or` list | that member, a string | `tests.landing-levels` = `every-declared` in `strict` |

A derived-default row's cell is not seeded (S1). The `runtime.journal` pair binds only while
observability is installed, so it is no `pairs` row yet. The seeded pairs hold in all four presets.

### The checks

```
presets.py check                       # S2 over the shipped store; exit 0 green, 1 red
presets.py load <name> [--repo <dir>]  # S4; exit 0 loaded, 2 refused, one line per refused key
printf '%s\n' '<key>=<toml>' | python <prefix>/loop/guard.py --expansion   # S8; exit 0, 2 refused
python <prefix>/playbook/core.py new preset <name> --from <preset>        # S6, through factories.py
```

`derive_preset_assignment(name, presets, table)` returns `{key path: value}` for a shipped name, or
for a repository name its shipped `extends` assignment with the table's keys on top, one level: the
one assignment every reader takes (units 2 and 20).

The pair rules judge the store alone. A file holding `review.design.round-count = 4` under
`standard` (`review.max-rounds` 3) passes `validate`, and `derive_review_bounds` refuses it under
`fixed-count` as at the base (§8 F10).

`arm_presets` runs `load_preset` and S8's verb once per shipped preset, the verb over the
`[[selects]]` pairs it assigns. The runs share nothing but the rule, so a planted loader refusing by
key, or admitting every value, reds.

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
today, its point core-declared.

### Files touched (estimate)

- `tools/policy/presets.toml` (new)
- `tools/policy/presets.py` (new)
- `tools/policy/policy.py`: `validate` calls `check_repo_presets` for a file holding `presets`;
  `scan_keys` leaves that table
- `tools/policy/check_policy.py`: `arm_presets` and the four cases
- `tools/policy/README.md`: the arm's row
- `tools/loop/guard.py`: S8's verb
- `tools/loop/loop.toml`: the `[[selects]]` row
- `tools/loop/factories.py`: the `preset` subcommand, its gate and two plants
- `tools/loop/README.md`: the verb and the seventh factory
- `tools/playbook/kinds.toml`: the `kind.preset` row
- `tools/playbook/core-pending.txt`: the row out
- `tools/gate-legs.json`: the `policy fixtures` row's `guard` gains `{prefix}/loop/` and
  `{prefix}/playbook/layers.toml`, the two paths §6's copy reads, which its guard trace grades WRONG
  today (`tools/policy/check_policy.py#check_guard_trace`)
- `help/reference/kinds.md`: re-rendered by `render_playbook.py --reference`
- `help/policy.md`: the section and its two usage anchors
- `tools/govkit/usage.toml`: the `[[usage]]` rows for `presets.py check` and `presets.py load`
  (flag `--repo=`), shaped as `budgets.py`'s `resolve` row

### Alternatives rejected

- **Four preset fields per catalogue row**: a second owner on every one-owner row.
- **The store generated from v2 each run**: a product kit reads no record at run time.
- **The pair rule in `validate` for every file**: a refusal read back as the last valid revision,
  one rule in two homes (§8 F10).
- **A loader refusing a key an absent expansion owns**: v2 rules it out; AC7 plants it as a break.
- **A factory in `presets.py`**: a copy of the guarded write each kind's factory shares, `[reuse]`.

## 5. Production-readiness checklist

- security — the factory is the store's one writer, under the guarded write; a repository preset
  passes `validate` at the policy guard, deny by default for an undeclared name, and a file
  declaring one where `presets.py` is absent is refused (§8 F9).
- perf / scale — one TOML read per check; two `guard.py` subprocesses per preset, never one per key.
- error / empty / loading states — an absent store is a refusal naming `presets.toml`; a malformed
  one a finding at its line; an unreadable verb line a refusal; no loop kit, the halves announce (§8 F7).
- observability — each finding names the preset and the key; the load the key, value and point.
- risks — a key added later has no preset value, and `policy check` reds it until its build adds
  them or TOOL-dDeclaredLoop-102 lands (§8 F3).
- testing — the four fixture cases, two plants and the arm.
- migration — none; no read changes.
- user docs — `help/policy.md` (S7) and the kinds page (S6).

## 6. Acceptance criteria

The policy fixture is `check_policy.py --fixture`: one scratch repository per case under `%TEMP%`,
the kit at its own path. A case reaching the loop kit also copies it whole and the playbook kit's
`layers.toml`, the paths the `policy fixtures` guard gains (§4).

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
  figure: 5 and 2 are PINNED by the plant.
- **AC4** — When the `presets-pairs` case runs `python presets.py check` over that planted store
  copy, it exits 1, a finding naming `velocity`, `review.max-rounds` and
  `review.design.round-count`; when the case commits, as the file's only revision, `preset =
  "standard"` and `review.design.round-count = 4`, `python policy.py check` exits 0 printing `is
  valid`.
  Red when: the store's broken pair checks green, or `validate` refuses a repository file's pair.
  figure: 4 PINNED by the case, over the catalogue's ceiling of 3.
- **AC5** — When the `presets-repo` case commits `[presets.ours]` extending `strict` with one
  override and `preset = "ours"`, `python policy.py check` exits 0; committed alone with `extends =
  "lax"`, or `"policy-file.guard"` inside the table, it exits 2 naming the key. And `python
  review_bounds.py --fixture --plant count-above`, then `--plant no-driver`, in the loop kit each
  print `held`: the base's refusal of a repository file's count above its ceiling, unchanged.
  Red when: a declared preset extends no shipped one or sets a `never` key and passes, or a plant
  misses.
  fixture: `no-driver`'s kit copy holds no `presets.py` (§8 F9).
- **AC6** — When the `presets-core-only` case runs `python presets.py load standard` and `load
  strict` in a scratch tree whose register copy's core Flow row declares no `point.flow.release`,
  `standard` exits 0 and `strict` exits 2 naming `build.closes`, `after-release-verifies` and the
  point, and no other key; `arm_presets` unplanted there prints no finding, its row-named half
  grading the refused pairs of `strict` and `guarded`.
  Red when: a preset is refused for a key its value does not select, or `strict` loads where the
  rule refuses its value.
  fixture: the register copy stands in for the core-only judgement the ask TOOL-dDeclaredLoop-101
  owes; the shipped register's four loads are AC9's, over the real tree (§7).
- **AC7** — When the `presets-core-only` case plants `absent-by-key`, a loader refusing any key a
  `[[selects]]` row names, `arm_presets` reds naming `standard` and `build.closes`; planting
  `accept-all`, a loader admitting every value, it reds naming `strict` and `build.closes`.
  Red when: either planted loader reads green.
- **AC8** — When `grep -n -A2 '^key = "build.closes"' loop.toml` runs in the loop kit, it prints the
  `[[selects]]` row's three lines, its value `after-release-verifies` and its point
  `point.flow.release`.
  Red when: the row is absent, so no rule ever judges `strict`'s value.
- **AC9** — When `python check_policy.py --repo .` runs at the repository root, it prints
  `policy-check: arm_presets · 0 finding(s)` with a population of four presets, each loaded over the
  shipped register, and the row-named half's `presets-core-only · not graded` line.
  Red when: the arm is absent from `ARMS`, announces itself, or reds the shipped tree for the open
  ask.
- **AC10** — When `python factories.py --fixture --plant preset-new` runs, `core.py new preset trial
  --from standard` in the scratch clone gives `presets.toml` a `[preset.trial]` table and the
  `preset` row's `of` the name `trial`, the gate green, and `core.py kinds` prints `kind.preset` off
  the pending list; `preset-from-unknown`'s `--from nope` exits 2 naming it, both files unchanged.
  Red when: the factory leaves a non-conforming preset, writes before refusing, or the kind stays
  pending.
- **AC11** — When `grep -n "never touch\|pair rule\|core-only" policy.md` runs in the help directory,
  it prints the presets section's three paragraphs; `grep -c 'policy/presets.py#' usage.toml` in the
  govkit kit prints `2`.
  Red when: the page omits presets, or shows a `presets.py` command no row declares.
- **AC12** — When `printf 'build.closes="after-release-verifies"\n' | python tools/loop/guard.py
  --expansion` runs at the repository root, it exits 0 and prints no refusal; fed the line `x` it
  exits 2 naming the line.
  Red when: the verb is absent, refuses a core-declared point, or reads an unparsed line as admitted.
- **AC13** — When `python check_policy.py --fixture adopter-fresh-target` runs, each installed
  `--check` prints `arm_presets` with no finding and both halves' `not graded · the loop kit does not
  resolve`, and the README's `arm_presets` row joins `ARMS`.
  Red when: the arm reds a target without the loop kit, or prints a half graded there.

## 7. Gates

`govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `docs` · `playbook render selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy check` · `policy fixtures` · `loop guard fixtures` · `loop factories fixtures` · `loop review bounds fixtures` · `core kinds` · `core meta-check` · `help reference pages` · `scratch-guard self-test` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms`

The `policy fixtures` ceiling is 2420 s over an evidenced 1210 s, PINNED at 50d413db, at the margin
`max(120 s, 1.0 x max)` (`tools/gate-legs.json`, `tools/run-gates/ceiling-evidence.txt`,
`tools/run-gates/ceiling-margin.txt`). Measured in process over rev-8's draft, PINNED at 50d413db:
`presets-complete` 0.7 s, `presets-pairs` 1.4 s, `presets-repo` 0.5 s, `presets-core-only` 26.8 s,
of which eight loads took 1.5 s each, two unplanted arm runs 6 s each, the kit copy 0.01 s, PINNED.
AC6's narrowing drops the shipped-register half, AC9's, and two loads the unplanted arm grades:
about 14 s for the four, PINNED as an estimate. No ceiling moves here: a reading past 1210 s is the
owner's to size, PINNED. `arm_presets` adds 6.1 s to `policy check`'s 120 s ceiling, PINNED.

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC9 AC13 · the four `presets-*` cases' plants, each staged on a copy of the shipped store, the loader or the register, and `adopter-fresh-target`'s halves check · none
New arm: tools/loop/factories.py · covers AC10 · the `preset-new` plant's factory run and the `preset-from-unknown` plant's `--from nope` · none

## 8. Open questions

- **F1 — Where does the repository preset rule run?** (a) In `validate`, a table rule after
  `budgets.check_budgets` (`tools/policy/budgets.py#check_budgets`), so the guard refuses the commit;
  (b) an arm only, so the guard commits a file the bar reds. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 1, v2's Rules and the seam dGroundRules-9 built; narrowed at rev-9 to the
  declared presets, the pair rules leaving it (F10). widens: none · relaxes: none
- **F2 — How is `after-release-verifies` refused on a core-only install, when its point is core?**
  `check_expansion_value` refuses a value only where no core row declares its point
  (`tools/loop/guard.py#read_core_points`), and the core Flow row declares the release slot. (a) Ask
  dDeclaredLoop to judge a `[[selects]]` row carrying `needs = "attached"` absent unless an installed
  row lists its point in `uses`; (b) a point no core row declares, which EX-1 forbids an expansion
  to attach at (`tools/playbook/check_layers.py#check_point`); (c) a refusal in this loader, a second
  copy of the rule. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, one rule. The ask is
  TOOL-dDeclaredLoop-101 (`memory/builds/dDeclaredLoop/BACKLOG.md`), accept: such a row refused
  unless an installed layer row's `uses` lists its point, seen red on a core-only fixture. Until
  then the row-named half prints not graded (S5). widens: none · relaxes: none
- **F3 — Does a new catalogue key land without a value in every shipped preset?** v2's Rules say it
  cannot; `new policy-key` writes only the catalogue row, gated by arms that never run
  `arm_presets` (`tools/loop/factories.py#POLICY_KEY_ARMS`). (a) Ask dDeclaredLoop for a `--preset
  <name>=<toml>` per shipped preset, or `--never`, in the same restore; (b) a default copied into
  every preset, wrong for a posture key. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1. The
  ask is TOOL-dDeclaredLoop-102, accept: `new policy-key` refuses a presettable key missing a
  shipped preset's value. widens: none · relaxes: none
- **F4 — How does `presets.py` reach `check_expansion_value`, when `guard.py` has no verb printing its
  verdict?** A kit imports no sibling kit (`tools/loop/guard.py#main`). (a) `guard.py --expansion`
  over `<key>=<value>` lines on stdin, one line per refused pair, exit 2 on any, one subprocess per
  load; (b) a `requires_if` row naming `loop`, imported in process. Recommendation (a). RESOLVED
  (owner, 2026-11-05): (a), its text "TOOL-dDeclaredLoop-2 S8: `guard.py --expansion` judges
  `<key>=<value>` lines on stdin with `check_expansion_value`, one line per refusal, exit 2 on any".
- **F5 — Who lands F4's verb, now that dDeclaredLoop has landed without it?** dDeclaredLoop landed
  at `9e21ac76` without it. (a) This unit, as S8; (b) file the ask, the load waiting on no plan;
  (c) the in-process load by path (`tools/playbook/instructions_edit.py#read_loop_guard`), which F4
  declined. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; every owner term kept, only the
  builder moved. widens: none · relaxes: none
- **F6 — What does each preset assign a presettable row v2's table lacks?** Six rows joined after v2:
  `review.spec-audit.disposal`, `review.spec-audit.chain-stop`, `review.spec-audit.chain-ceiling`,
  `bar.inline-red-fixes`, `pass.fast-legs` and `memory.staged-render`. (a) Its catalogue default in
  all four; (b) a value per preset chosen here, a posture no owner record states; (c) the never
  list, which v2 closes. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; nothing invented.
  widens: none · relaxes: none
- **F7 — What do the load halves do where the loop kit does not resolve?** `adopter-fresh-target`
  installs no loop kit (`tools/policy/README.md`), so a miss under `empty = "finding"` reds it. (a)
  Each half prints `not graded · the loop kit does not resolve`, as the loop kit's cross-kit reads
  degrade (`tools/loop/kit.toml#requires`); (b) a finding; (c) a `loop` edge no policy read needs.
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the main loop's ruling on run
  `wf_c7d6ba36-6f3`. widens: none · relaxes: none
- **F8 — What does a `policy.py check` refusal exit, when it never exits 1?** 0 for a file valid,
  absent, or invalid with a last valid revision, else 2 (`tools/policy/policy.py#cmd_check`), as
  `tools/policy/check_policy.py#run_on_invalid_classes` pins. (a) Exit 2 over a fixture with no
  valid revision first; (b) an exit 1, moving that contract. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3, run `wf_73059b2b-dc2`; AC5 observes it. widens: none · relaxes: none
- **F9 — How does `validate` reach `presets` where a suite copies part of the policy kit?** Four
  suites and `tools/loop/review_bounds.py#build_plant_repo` copy `policy.py` without `presets.py`
  and commit a policy file holding no `presets` table. (a) `validate` imports `presets` only for a
  file holding that table, refusing one where it does not import; (b) an unconditional import, each
  copy gaining the two files, `review_bounds.py` among them, which F10 keeps untouched; (c) a skip
  where `presets.py` is absent, a silent pass. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3,
  re-ruled at rev-9 under F10: rev-7's copies in `tools/check-line-length.test.sh`,
  `tools/hooks/agent-cap.test.sh`, `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/unattended.test.sh` serve nothing and leave (YAGNI). widens: none · relaxes: none
- **F10 — Does `validate` judge the pair rules over a repository file?** Under the default
  `policy-file.on-invalid = "last-valid"` a refusal there reads back the last valid revision, so
  `tools/loop/review_bounds.py#read_review_bounds` reads old bounds where the base refuses (run
  `wf_b1359b32-6c1`), and `#derive_review_bounds` refuses that count under `fixed-count`. (a) The
  pair rules judge the preset store alone, through `presets.py check` and the arm's pairs case, a
  repository file's pair staying `derive_review_bounds`' refusal; (b) `validate` refusing it for
  every file, a silent fallback and one rule in two homes with two scopes. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3, the main loop's ruling; `review_bounds.py` and the
  `write_tracking_policy` arms of `tools/unattended/unattended.test.sh` are untouched. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges to `KICK-dKeptSession-33` and `KICK-dKeptSession-44` mirrored.
- rev-3 · 2026-10-26 · S4 · §3 · §5 · AC6 · §8 F4 · §10 · re-grounded on the record
  `2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`, row 3: the subprocess reach, F4 open.
- rev-4 · 2026-11-05 · S4 · AC6 · §8 F4 · F4 resolved by the owner to (a) under the brief
  `2026-11-05-prompt-KICK-dKeptSession-1-owner-forks`.
- rev-5 · 2026-11-21 · S1 S2 S3 S4 S5 S6 S7 S8 · §3 · §4 · §5 · AC1 AC2 AC6 AC7 AC8 AC9 AC10 AC12 · §7
  · §8 F2 F3 F4 F5 F6 · §10 · re-grounded at `c2a407b0` under the brief
  `2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief`: the derived-default rows to unit
  33, the `needs` field to TOOL-dDeclaredLoop-101, the factory into `factories.py`; S8 (F5), the
  seed's rules (F6), AC12 and the factories arm added; citations by symbol or blob pin.
- rev-6 · 2026-11-21 · S5 S6 · §4 · §5 · §6 · AC13 · §7 · §8 F7 · the divergence ruled under the
  brief `2026-11-21-prompt-KICK-dKeptSession-1-divergence-brief`: `tools/gate-legs.json` rejoins
  Files touched; the halves announce a missing loop kit (F7).
- rev-7 · 2026-11-21 · S2-S6 S8 · §4 · §5 · AC4 AC5 · §7 · §8 F1-F3 F5-F9 · §10 · brief
  `2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief`: exit 2 observed (F8); five partial
  policy-kit copies join (F9).
- rev-8 · 2026-11-21 · §1 · §4 · §6 · AC7 · §7 · §8 F9 · brief
  `2026-11-21-prompt-KICK-dKeptSession-1-divergence-2-brief`: F9 narrowed to four suites; the fifth
  and the two legs only it tripped leave.
- rev-9 · 2026-11-21 · §1 · S2 S3 S7 · §3 · §4 · §5 · AC3-AC6 AC8 AC9 AC11 · §7 · §8 F1 F9 F10 · §10 ·
  the third divergence ruled under the brief `2026-11-21-prompt-KICK-dKeptSession-1-divergence-3-brief`:
  the pair rules judge the store alone (F10); `validate` imports `presets` only for a file declaring
  one, so the four suite copies and the five legs only they tripped leave (F9); AC8 prints the row;
  the usage rows join; §7 states the ceiling and the narrowed core-only case's cost.

## 10. Reuse audit

The seams extended: `check_value`, `check_derived` and `read_catalogue_row`
(`tools/policy/policy.py#check_value`, `#check_derived`, `#read_catalogue_row`); `validate`'s
table-rule seam, the `budgets` call (`tools/policy/policy.py#validate`); `ARMS` and `run_arm`
(`tools/policy/check_policy.py#ARMS`, `#run_arm`); `derive_strict_value` for the seed;
`check_expansion_value` (`tools/loop/guard.py#check_expansion_value`) by subprocess through
`resolve_kit_dir` (`tools/policy/policy.py#resolve_kit_dir`); `write_kind_instance` and
`run_policy_key_arms` (`tools/loop/factories.py`); the kinds contract
(`tools/playbook/core.py#run_kinds`, `#run_new`); the `[[usage]]` rows
(`tools/govkit/docs_leg.py#read_usage_rows`); and, left untouched as a repository file's pair rule,
`tools/loop/review_bounds.py#derive_review_bounds`. The prior art,
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-preset-check.py`, gives its never
set, completeness checks and `PAIRS`. `python tools/codebase-map/reuse_lookup.py "named policy
presets completeness check pair rules"` (2026-11-21) ranked name stems only: no preset code is in
the tree. `python tools/memory-recall/query.py` with the terms below returned scout A's row 1 and the
flow review's M1 (`memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-flow-b.md`).
Disagreement with the earlier text: §8 F2, F3 and F10.

Recall terms used: preset presets completeness pair rules never-touch strict guarded build.closes selects expansion core-only review-bounds fixed-count last-valid
