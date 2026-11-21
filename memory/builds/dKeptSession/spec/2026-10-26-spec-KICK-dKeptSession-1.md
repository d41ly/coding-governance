# KICK-dKeptSession-1 — the named presets as data, their completeness check, pair rules and core-only load

**Status:** INPROGRESS · rev-5 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 1 · advances KICK-dKeptSession-29

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
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-orders-1-2-reground-brief.md) | research | KICK-dKeptSession-19 KICK-dKeptSession-33 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

v2 names four presets, each a complete assignment of the policy keys a repository picks by one key,
`preset`, but no product file holds them: the catalogue's `preset` row lists the four names
(`tools/policy/catalogue.toml#preset`) and the reader names an unapplied preset in its reason
(`tools/policy/policy.py#read_default_value`), and nothing else reads them. This unit lands the
presets as the policy kit's data, the check that keeps each one complete and inside its keys'
schemas, the pair rules over each preset and over a repository's overrides on top of one
(`review.design.round-count` at or below `review.max-rounds` among them), and the core-only load,
each pair judged by the loop kit's one expansion rule. It also arms the preset kind the kinds
register holds pending for this build, so every reader in this build reads one store.

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
  `check_value(row, value)` (`tools/policy/policy.py#check_value`); the `standard` table equals each
  presettable row's literal catalogue default; the catalogue `preset` row's `of` list and the shipped
  table names are one set; each `never` entry names a catalogue row; and each pair holds in each
  preset. Each finding names the preset and the key. Observed by AC1, AC2 and AC3.
- **S3** — The repository side, as `validate`'s second table rule, `check_repo_presets(doc, text,
  rows)` beside `budgets.check_budgets` (`tools/policy/policy.py#validate`,
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
  `check_expansion_value` (`tools/loop/guard.py#check_expansion_value`) refuses the pair. A kit
  imports no sibling kit, so `presets.py` finds `guard.py` through the policy kit's inlined
  `resolve_kit_dir("loop", "guard.py", here)` (`tools/policy/policy.py#resolve_kit_dir`), a reach
  that takes no `requires` edge, as the loop kit's own subprocess reads of the playbook kit take none
  (`tools/loop/kit.toml#requires`); with the loop kit not found the load exits 2 naming the kit. This
  unit adds the `[[selects]]` row `build.closes` = `after-release-verifies` at the release slot's
  point, `point.flow.release`, which the core Flow row of `tools/playbook/layers.toml` declares.
  Today's rule refuses a value only where no core row declares its point
  (`tools/loop/guard.py#read_core_points`), so on the shipped register all four presets load; the
  refusal of `strict` and `guarded` for `build.closes` on a core-only install is the judgement the
  ask TOOL-dDeclaredLoop-101 owes (§8 F2). Observed by AC6, AC7 and AC8.
- **S5** — The arm `arm_presets` in `ARMS` of `tools/policy/check_policy.py`
  (`tools/policy/check_policy.py#ARMS`), `empty = "finding"` because the presets ship in the kit:
  S2's findings over the shipped store, then two halves comparing each shipped preset's S4 load with
  the expansion rule run on each `[[selects]]` pair the preset assigns. The by-key half reds a
  refusal whose key and value no `[[selects]]` row names. The row-named half reds a row-named pair
  the rule refuses and the load admits; where the rule admits a row-named pair the preset assigns,
  it prints `presets-core-only · not graded · TOOL-dDeclaredLoop-2 S8 admits after-release-verifies`
  and counts no finding, so the half grades the moment the ask's judgement refuses. Its row in the
  README's "Each arm in an adopter" table (`tools/policy/README.md`). Observed by AC2, AC7 and AC9.
- **S6** — The preset kind (shared interface I2): the `kind.preset` row of
  `tools/playbook/kinds.toml` gains its `population` (`{prefix}/policy/presets.toml`), `factory`
  (`python {prefix}/loop/factories.py preset`), `gate` (`policy check`), `summary` and `usage`, and its
  `kind` row leaves `tools/playbook/core-pending.txt`. The factory is a subcommand of the kinds'
  factory module, `write_preset(top, kit_rel, name, source)` through `write_kind_instance`
  (`tools/loop/factories.py#write_kind_instance`): `python <prefix>/playbook/core.py new preset
  <name> --from <preset>` appends a `[preset.<name>]` table copying the named shipped preset's
  assignment and adds the name to the catalogue `preset` row's `of` list, both held through the
  guarded write, its gate `arm_presets` run in process as `run_policy_key_arms` runs its arms
  (`tools/loop/factories.py#run_policy_key_arms`), every held byte put back on a red. The `policy
  check` leg already enforces the kind's one bind, `principle.p16` (`tools/gate-legs.json`), so no
  leg changes. The kinds reference page re-renders from the row (`help/reference/kinds.md`).
  Observed by AC10.
  **Readers:** by name: `tools/playbook/core.py`, whose `kinds` and `meta-check` verbs read the
  pending list through `read_pending`, and `tools/playbook/render_playbook.py`, whose kinds page
  renders the row's `usage` · by value: `core.py kinds`' pending count, `kinds · <n> registered, <k>
  pending`, which falls by one.
- **S7** — The page `help/policy.md` gains a section on presets: the four, the never list, the pair
  rules, a repository preset, and the core-only load and the ask its refusal waits on. Observed by
  AC11.
- **S8** — The verb `guard.py --expansion` in `tools/loop/guard.py`, the one the owner ruled at §8 F4
  and §8 F5 assigns here: it reads `<key>=<toml value>` lines on stdin, judges each with
  `check_expansion_value(key, value, read_core_points(), top)`, `top` the working directory's
  repository, prints one `loop-guard: refused · <where> · <why>` line per refused pair, which names
  the key, the value and the point, passes the rule's own `fallback` line through as no refusal, and
  exits 2 on any refusal or unreadable line, else 0. The verb copies no part of the rule. Observed by
  AC6 and AC12.

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

The release slot is a core point, Flow's in Deploy, that integrations' engines attach at
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md@c2a407b0:179`);
the register spells it `point.flow.release` on the core Flow row and lists it in the `uses` of
`layer.integrations`, an expansion row no kit descriptor names today (`tools/playbook/layers.toml`).

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
for a repository name its shipped `extends` assignment with the table's own keys on top; it is the
one assignment every reader takes (KICK-dKeptSession-2 reads it in its step, unit 20 in the
scenario's). A repository preset extends a shipped one only, so the walk is one level.

The pair rule over a repository is judged on the effective assignment: the named preset's
assignment, a declared preset's included, with the file's own top-level keys on top, so a file that
sets `review.design.round-count = 4` under `standard` (`review.max-rounds` 3) is refused at its line.
A pair whose two keys are unset in both the preset and the file binds nothing.

`arm_presets` runs `load_preset` once per shipped preset and S8's verb once per preset over the
`[[selects]]` pairs that preset assigns, read from the loop kit's `loop.toml` through the same
`resolve_kit_dir`. The two runs share no state but the rule they are compared against, so a planted
loader that refuses by key, or admits every value, differs from the rule and reds.

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

`.governance/policy.toml` gains no key. A policy file that named a preset read every key at its
default before KICK-dKeptSession-2; this unit changes no read.

### Rollout

The store lands with its arm; the reader's step lands in unit 2, so no read changes in this pass.
The `[[selects]]` row changes no verdict today, since its point is core-declared: `policy_edit.py
set build.closes after-release-verifies` is admitted as before.

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
- `help/reference/kinds.md`: re-rendered by `render_playbook.py --reference`
- `help/policy.md`

### Alternatives rejected

- **A field per catalogue row holding its four preset values.** The catalogue is one row per v2
  `[policies]` row with one owner each; four more fields per row would put a second owner on every
  row.
- **Generate the store from v2 at every run.** v2 is a frozen record; a product kit cannot read a
  record at run time, which is why `derive_strict_value` stays a fixture reader.
- **The pair rule as an arm only.** `validate` is the policy file's one judge and already runs the
  `[budgets]` table's own rule; an arm alone would let the guard commit a file the bar then reds.
- **A loader that refuses a key an absent expansion owns.** v2's revision rules it out: such a key
  is unread, so no preset is refused for it. The fixture plants it as AC7's break.
- **A factory of its own in `presets.py`.** The kinds' factory module already holds the guarded
  write, the restore and the gate wrapper every kind's factory shares, and the loop kit's README
  names the preset kind as its pending member; a second copy is the defect `[reuse]` names.

## 5. Production-readiness checklist

- security — the store ships in the kit and is read, never written, by readers; the factory is the
  one writer and runs the gate under the guarded write; a repository preset passes `validate` at the
  policy guard's write boundary, deny by default for a name neither shipped nor declared.
- perf / scale — one TOML read per check; the arm runs two `guard.py` subprocesses per preset, never
  one per key.
- error / empty / loading states — an absent store is a refusal naming `presets.toml`; a malformed
  one is a finding naming its line; an unreadable verb line is a refusal naming it.
- observability — every finding names the preset and the key; the load names the key, the value and
  the point; the row-named half prints why it is not graded.
- risks — a key another build adds after this unit lands has no preset value, `new policy-key`'s
  gate (`tools/loop/factories.py#POLICY_KEY_ARMS`) does not run `arm_presets`, so the `policy check`
  leg reds it until its build adds the values or the ask TOOL-dDeclaredLoop-102 lands (§8 F3).
- testing — the four fixture cases and two plants of the criteria below, and the arm.
- migration — none; no read changes.
- user docs — `help/policy.md`, S7, and the kinds reference page, S6.

## 6. Acceptance criteria

The policy fixture is `check_policy.py --fixture`: one scratch repository per case under `%TEMP%`
with a short prefix, the kit copied at its own path, a policy file committed with a remote-tracking
ref. A case reaching the loop kit also copies the loop and playbook kits and the kits the loop
kit's descriptor `requires`, each at its own path.

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
- **AC4** — When the `presets-pairs` case commits a policy file with `preset = "standard"` and
  `review.design.round-count = 4`, `python policy.py check` exits 1 naming both keys at the
  override's line; with the override at 3 it exits 0.
  Red when: an override past `review.max-rounds` passes `validate`.
- **AC5** — When the `presets-repo` case commits `[presets.ours]` extending `strict` with one
  override and `preset = "ours"`, `python policy.py check` exits 0; with `extends = "lax"`, or with
  `"policy-file.guard"` inside the table, it exits 1 naming the key.
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
  Red when: either planted loader reads green, which is the clause's red both ways.
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

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy check` · `policy fixtures` · `loop guard fixtures` · `loop factories fixtures` · `core kinds` · `core meta-check` · `help reference pages` · `scratch-guard self-test` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC9 · the four `presets-*` cases' plants, each staged on a copy of the shipped store, the loader or the register · none
New arm: tools/loop/factories.py · covers AC10 · the `preset-new` plant's factory run and the `preset-from-unknown` plant's `--from nope` · none

## 8. Open questions

- **F1 — Where does the pair rule over a repository's overrides run?** (a) In `validate`, as a
  second table rule beside `budgets.check_budgets`, so the guard refuses the commit and the reader
  falls back to the last valid revision; (b) an arm only, red at the bar. (b) lets the policy guard
  commit a file the bar reds. v2's Rules say a check refuses, and the `[budgets]` rule is the seam
  that already runs in `validate`. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2's Rules
  and the seam dGroundRules-9 built. widens: none · relaxes: none
- **F2 — How is `after-release-verifies` refused on a core-only install, when its point is core?**
  `check_expansion_value` refuses a value only where no core row of the layer register declares its
  point (`tools/loop/guard.py#read_core_points`), and the core Flow row declares the release slot,
  so the rule as landed admits the value. (a) Ask dDeclaredLoop to judge a `[[selects]]` row
  carrying `needs = "attached"` absent unless an installed register row lists its point in `uses`;
  (b) name a point no core row declares, which the layer check's EX-1 forbids an expansion to attach
  at (`tools/playbook/check_layers.py#check_point`), so integrations could never admit the value; (c)
  a refusal in this kit's loader, a second copy of the absent-expansion rule gap-spine-07 names.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the one option keeping one rule and a value
  an installed expansion can admit. The ask is TOOL-dDeclaredLoop-101, open at dDeclaredLoop's
  landing (`memory/builds/dDeclaredLoop/BACKLOG.md`), accept: a `[[selects]]` row with `needs =
  "attached"` is refused unless an installed layer row's `uses` lists its point, seen red on a
  core-only fixture that admits `after-release-verifies`. Until it lands the row-named half prints
  not graded (S5) and AC6 observes the refusal over a register copy. widens: none · relaxes: none
- **F3 — Does a new catalogue key land without a value in every shipped preset?** v2's Rules say it
  cannot. `new policy-key` writes only the catalogue row and its gate is `POLICY_KEY_ARMS`, four arms
  that never run `arm_presets` (`tools/loop/factories.py#POLICY_KEY_ARMS`), so the factory lands the
  key and the `policy check` leg reds it after. (a) Ask dDeclaredLoop for a `--preset <name>=<toml>`
  per shipped preset, or `--never`, written into `presets.toml` in the same restore; (b) a default
  copied into every preset, which v2's strict and guarded columns show is wrong for a posture key.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2's Rules. The ask is
  TOOL-dDeclaredLoop-102, open at dDeclaredLoop's landing, accept: `new policy-key` takes one
  `--preset <name>=<toml>` per shipped preset or `--never`, and refuses a presettable key missing
  one, seen red on a key added with the `strict` value absent. widens: none · relaxes: none
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
  at `9e21ac76`, and no row of its `BACKLOG.md` carries the verb. (a) This unit, as S8, in
  `tools/loop/guard.py`, the ruled text its acceptance; (b) the run files the ask now and S4, AC6,
  AC7 and the arm's load halves wait on a later dDeclaredLoop run no plan schedules; (c) the playbook
  kit's in-process load of `guard.py` by path (`tools/playbook/instructions_edit.py#read_loop_guard`),
  the shape F4's ruling declined. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; it keeps
  every term the owner ruled, the verb, its grammar, its exit and the subprocess, moves only who
  builds it, and is the one option under which this unit's load runs. widens: none · relaxes: none
- **F6 — What does each preset assign a presettable row v2's table lacks?** Six presettable rows
  joined the catalogue after v2: `review.spec-audit.disposal`, `review.spec-audit.chain-stop`,
  `review.spec-audit.chain-ceiling`, `bar.inline-red-fixes`, `pass.fast-legs` and
  `memory.staged-render`. (a) Its catalogue default in all four presets, the one value the catalogue
  declares and the one the standard rule demands, so no posture moves until its owner sets a preset
  value; (b) a value per preset chosen here, a posture no record of the owner's states; (c) the never
  list, which v2 closes. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the only option
  every rule holds under with nothing invented. widens: none · relaxes: none

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

## 10. Reuse audit

The seams extended: the policy kit's `check_value`, `check_derived` and `read_catalogue_row`
(`tools/policy/policy.py#check_value`, `#check_derived`, `#read_catalogue_row`) for every key and
value; `validate`'s table-rule seam (`tools/policy/policy.py#validate`, the `budgets` call); the
`ARMS` table and `run_arm` (`tools/policy/check_policy.py#ARMS`, `#run_arm`); the cell reader
`derive_strict_value` for the one-time seed; the loop kit's `check_expansion_value` over
`[[selects]]` (`tools/loop/guard.py#check_expansion_value`), run by subprocess through the policy
kit's inlined `resolve_kit_dir` (`tools/policy/policy.py#resolve_kit_dir`); the kinds' factory
module, `write_kind_instance` and `run_policy_key_arms` (`tools/loop/factories.py`), whose README
section names the preset kind pending; and the kinds contract (`tools/playbook/core.py#run_kinds`,
`#run_new`). The prior art is
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-preset-check.py`: its never set,
completeness and allowed-value checks and `PAIRS` are promoted, and its `FREE` allowed-text regex is
not, since `check_value` judges the parsed `allowed` table. `python
tools/codebase-map/reuse_lookup.py "named policy presets completeness check pair rules"`, re-run
2026-11-21, ranked `check`, `pair`, `checks`, `read_policy_value` and `read_policy_kit`, name stems
only: no preset code is in the tree. `python tools/codebase-map/reuse_lookup.py "kind factory
guarded write restore gate"` ranked `write`, `write_text` and `write_fixture_files`, name stems;
the factory module was found by reading the kinds register's `factory` cells. `python
tools/memory-recall/query.py` with the terms below returned scout A's row 1, this spec, this build's
brief and the flow review's M1 (`memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-flow-b.md`),
which names `build.closes` as the key a core-only install refuses. Disagreement with the earlier
text: the landed rule cannot refuse a value whose point is core (§8 F2), and the factory gate does
not run this unit's arm (§8 F3).

Recall terms used: preset presets completeness pair rules never-touch strict guarded build.closes selects expansion core-only
