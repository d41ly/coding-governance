# KICK-dKeptSession-1 — the named presets as data, their completeness check, pair rules and core-only load

**Status:** DEFERRED · rev-3 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 1 · advances KICK-dKeptSession-29

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
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

v2 names four presets, each a complete assignment of the policy keys a repository picks by one key,
`preset`, but no product file holds them: the only reader of v2's preset table is a record, the
prior-art checker `preset-check.py`. This unit lands the presets as the policy kit's data, the check
that keeps each one complete and inside its keys' schemas, the pair rules over each preset and over a
repository's overrides on top of one (`review.design.round-count` at or below `review.max-rounds`
among them), and the core-only load, where `strict` and `guarded` are refused for `build.closes`
because the value they set selects an absent expansion. It also arms the preset kind dDeclaredLoop
left pending for this build, so every reader in this build reads one store.

## 2. Scope (IN)

- **S1** — The preset store `tools/policy/presets.toml` (shared interface I1): one `[preset.<name>]`
  table per shipped preset, `velocity`, `standard`, `strict` and `guarded`, each assigning every
  presettable key by a quoted dotted key (`"hooks.bypass" = "refused"`); a top-level `never` list,
  the keys presets never touch with `preset` and `floor` among them; and a top-level `pairs` list of
  `[<higher>, <lower>]` pairs. Seeded once from v2's table, v2:1474-1722, and v2's never list and
  pair rules, v2:1420-1433. Observed by AC1.
- **S2** — The shipped check, `check_presets(rows, presets)` in the new module
  `tools/policy/presets.py`, printed by `python presets.py check`: every catalogue row that `never`
  does not name is matched by at least one key of each shipped preset and every preset key matches a
  row, both through dGroundRules' one matcher `read_catalogue_row`; each value passes dGroundRules'
  `check_value(row, value)`; the `standard` table equals each row's literal catalogue default; the
  catalogue `preset` row's `of` list and the shipped table names are one set; each `never` entry
  names a catalogue row; and each pair holds in each preset. Each finding names the preset and the
  key. Observed by AC1, AC2 and AC3.
- **S3** — The repository side, as `validate`'s second table rule, `check_repo_presets(doc, text,
  rows)` beside `budgets.check_budgets`: a `[presets.<name>]` table in `.governance/policy.toml`
  declares a repository preset whose `extends` names a shipped preset and whose other keys are
  catalogue keys outside `never`, each value passing `check_value`; the file's `preset` value is
  admitted when it names a shipped or a declared preset; and the pair rules hold over the effective
  assignment, the named preset's values with the file's own keys on top. `scan_keys` leaves the
  `presets` table to this rule. Each problem carries the line `derive_key_line` finds. Observed by
  AC4 and AC5.
- **S4** — The core-only load, `load_preset(name, table)` in `presets.py`, printed by `python
  presets.py load <name>`: the named preset's assignment, each pair judged by dDeclaredLoop's
  `check_expansion_value(key, value)` (TOOL-dDeclaredLoop-2 S8), a refusal only for a value a
  `[[selects]]` row of `tools/loop/loop.toml` names (shared interface I3), never for a key alone. A
  kit imports no sibling kit (TOOL-dGroundRules-1 §4; TOOL-dDeclaredLoop-12 S4), so `presets.py` finds
  `guard.py` through the policy kit's one inline block, `resolve_kit_dir("loop", "guard.py", here)`
  (`tools/policy/policy.py:1132-1169`), and runs it as one subprocess per load, the verb §8 F4 asks
  for; with the loop kit not found, the load exits 2 naming the kit, as PLAY-dOrderedCharter-7's
  reader refuses with no policy kit found. This unit adds the
  `[[selects]]` row `build.closes` = `after-release-verifies` at the release slot's point, so on an
  install whose layer register attaches nothing there `strict` and `guarded` are refused for
  `build.closes` and `velocity` and `standard` load. Observed by AC6, AC7 and AC8.
- **S5** — The arm `arm_presets` in `ARMS` of `tools/policy/check_policy.py`, `empty = "finding"`
  because the presets ship in the kit: S2's findings over the shipped store, then S4's load of each
  shipped preset compared both ways with the `[[selects]]` rows, red on a refusal whose value no row
  names and on a row-named value that loads while the register attaches nothing at its point. Its row in the README's "Each arm in an adopter" table.
  Observed by AC2, AC7 and AC9.
- **S6** — The preset kind (shared interface I2): the `kind.preset` row of
  `tools/playbook/kinds.toml` gains its `population` (`tools/policy/presets.toml`), `factory`
  (`python {prefix}/policy/presets.py new`) and `gate` (`policy check`), and its `kind` row leaves
  `tools/playbook/core-pending.txt`. The factory, `python tools/playbook/core.py new preset <name>
  --from <preset>`, appends a `[preset.<name>]` table copying the named preset's assignment and adds
  the name to the catalogue `preset` row's `of` list, runs the gate, and restores both files on a red.
  The `policy check` leg's `enforces` gains each tag of the kind's `binds`. Observed by AC10.
  **Readers:** by name: READER NOT IN TREE — `tools/playbook/core-pending.txt` and its two readers,
  `core.py kinds` and `core.py meta-check` (PLAY-dOrderedCharter-7 S3, S5), are specced and unbuilt
  at this spec's base; TOOL-dDeclaredLoop-6 AC9 greps the row as that unit's own acceptance, a closed
  unit's ledger line rather than a reader · by value: `core.py meta-check`'s pending count, which
  falls by one.
- **S7** — The page `help/policy.md` gains a section on presets: the four, the never list, the pair
  rules, a repository preset, and the core-only refusal. Observed by AC11.

## 3. Non-goals (OUT)

- The reader applying a preset: KICK-dKeptSession-2's step reads this store.
- The charter's preset section, intake's preset answer and a scenario's preset slot: units 3, 4 and
  20.
- The `[[selects]]` row for `build.closes` = `at-landing-maintain-owns`: no shipped preset sets it,
  and dShippedRelease, which owns the key and its reader, adds it with that reader.
- A preset store per stage or per build: v2 assigns per repository.
- The `on-invalid-strict` fixture case's strict-cell parser (`derive_strict_value`,
  `check_policy.py:1753`): it reads v2 as the build's acceptance probe, a record, and stays.
- The change to `check_expansion_value` that judges an attachable core point absent (§8 F2): an ask
  for dDeclaredLoop.

### Edges

- **hands-off** `KICK-dKeptSession-2` — `presets.toml` and `derive_preset_assignment`, which the reader's preset step answers from
- **hands-off** `KICK-dKeptSession-3` — `presets.toml`, against which the charter section prints only the keys that differ
- **hands-off** `KICK-dKeptSession-4` — `presets.toml`, whose shipped names intake admits as the `preset` answer
- **hands-off** `KICK-dKeptSession-20` — `presets.toml` and its `never` list, which a scenario's preset slot reads and may not set
- **hands-off** `KICK-dKeptSession-9` — `presets.toml`, whose strict table holds `orient.budget` = `warn-at-evidence-ceiling`
- **hands-off** `KICK-dKeptSession-7` — `presets.toml`, whose strict table holds the `deps.coordination` and `deps.early-build` cells
- **consumes-from** external — dGroundRules' `check_value`, `read_catalogue_row`, `validate` with its `budgets` table rule, `check_policy.py`'s `ARMS` and fixture (TOOL-dGroundRules-1, -2, -9); dDeclaredLoop's `check_expansion_value`, reached by subprocess, and `[[selects]]` rows (TOOL-dDeclaredLoop-2 S8) and its factory module (TOOL-dDeclaredLoop-6 S2); dOrderedCharter's `kinds.toml`, `core-pending.txt`, `core.py new` (PLAY-dOrderedCharter-7 S4-S6) and the layer register (PLAY-dOrderedCharter-16 S1)
- **hands-off** external — the attached-point judgement in `check_expansion_value` (§8 F2), a value per shipped preset in `new policy-key` (§8 F3) and a `guard.py` verb printing `check_expansion_value`'s verdict (§8 F4), each an ask for dDeclaredLoop
- **hands-off** `KICK-dKeptSession-33` — `presets.toml` and `check_presets`, whose rule for the eight derived-default rows that unit states (id 17)
- **hands-off** `KICK-dKeptSession-44` — `arm_presets`' row-named half, `check_repo_presets`' shipped-name collision, the never-list comment and the one pair rule, the batch's S1, S32, S38 and S41 (ids 3, 62, 18, 43)

## 4. Design

### Data model

```toml
# tools/policy/presets.toml — the shipped presets; one table per name, quoted dotted keys
never = ["floor", "preset", "policy-file.guard", "policy-file.proof", "policy-file.on-invalid",
         "charter.practices", "instructions.edit", "...", "platforms.provision"]   # v2:1427-1433
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
needs = "attached"
```

The release slot is a core point, Flow's in Deploy, that integrations' engines attach at
(`2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:179`). Its spelling follows
PLAY-dOrderedCharter-16 §4's rule `point.<layer>.<seg>`; where that unit lands another spelling, the
row takes the landed one. `needs = "attached"` is the field §8 F2 asks dDeclaredLoop for.

The `runtime.journal` pair binds only while observability is installed (v2:1423-1424), so it is not a
`pairs` row until that expansion lands its key's reader.

### The checks

```
presets.py check                       # S2 over the shipped store; exit 0 green, 1 red
presets.py load <name> [--repo <dir>]  # S4; exit 0 loaded, 2 refused, one line per refused key
presets.py new <name> --from <preset>  # S6's factory, through core.py new preset
```

`derive_preset_assignment(name, presets, table)` returns `{key path: value}` for a shipped name, or
for a repository name its shipped `extends` assignment with the table's own keys on top; it is the
one assignment every reader takes (KICK-dKeptSession-2 reads it in its step, unit 20 in the
scenario's). A repository preset extends a shipped one only, so the walk is one level.

The pair rule over a repository is judged on the effective assignment: the named preset's
assignment, a declared preset's included, with the file's own top-level keys on top, so a file that
sets `review.design.round-count = 4` under `standard` (`review.max-rounds` 3) is refused at its line.
A pair whose two keys are unset in both the preset and the file binds nothing.

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `tools/policy/presets.toml` | data file | new |
| `load_presets`, `derive_preset_assignment`, `check_presets`, `check_repo_presets`, `load_preset`, `write_preset` | functions | `tools/policy/presets.py` (new) |
| `arm_presets` | arm | `tools/policy/check_policy.py` |
| `presets-complete`, `presets-pairs`, `presets-repo`, `presets-core-only`, `presets-factory` | fixture cases | `tools/policy/check_policy.py` |

### Migration

`.governance/policy.toml` gains no key. A policy file that named a preset read every key at its
default before KICK-dKeptSession-2; this unit changes no read.

### Rollout

The store lands with its arm; the reader's step lands in unit 2, so no read changes in this pass.

### Files touched (estimate)

- `tools/policy/presets.toml` (new)
- `tools/policy/presets.py` (new)
- `tools/policy/policy.py`: `validate` calls `check_repo_presets`; `scan_keys` leaves `presets`
- `tools/policy/check_policy.py`: `arm_presets` and the five cases
- `tools/policy/README.md`: the arm's row
- `tools/policy/kit.toml`: the two new files in `[[files]]`
- `tools/loop/loop.toml`: the `[[selects]]` row
- `tools/playbook/kinds.toml`: the `kind.preset` row
- `tools/playbook/core-pending.txt`: the row out
- `tools/gate-legs.json`: `enforces` on `policy check`
- `help/policy.md`

### Alternatives rejected

- **A field per catalogue row holding its four preset values.** The catalogue is dGroundRules' and
  one row per v2 `[policies]` row; four more fields per row would put a second owner on every row.
- **Generate the store from v2 at every run.** v2 is a frozen record; a product kit cannot read a
  record at run time, which is why `preset-check.py` stays a record.
- **The pair rule as an arm only.** `validate` is the policy file's one judge and already runs the
  `[budgets]` table's own rule; an arm alone would let the guard commit a file the bar then reds.
- **A loader that refuses a key an absent expansion owns.** v2's revision (v2:304-306) rules it out:
  such a key is unread, so no preset is refused for it. The fixture plants it as AC7's break.

## 5. Production-readiness checklist

- security — the store ships in the kit and is read, never written, by readers; the factory is the
  one writer and runs the gate; a repository preset passes `validate` at the policy guard's write
  boundary, deny by default for a name neither shipped nor declared.
- perf / scale — one TOML read per check; the load is four presets times about 250 keys, one
  `guard.py` subprocess per preset, never one per key.
- error / empty / loading states — an absent store is a refusal naming `presets.toml`; a malformed
  one is a finding naming its line.
- observability — every finding names the preset and the key; the load names the key, the value and
  the point.
- risks — the store and v2 diverge as keys are added: S2's completeness check and the factory's gate
  catch a key with no preset value (§8 F3).
- testing — the five fixture cases of §6 and the arm in §7.
- migration — none; no read changes.
- user docs — `help/policy.md`, S7.

## 6. Acceptance criteria

The fixture is dGroundRules' `check_policy.py --fixture`: one scratch repository per case under
`%TEMP%` with a short prefix, the kit copied at its own path, a policy file committed with a
remote-tracking ref.

- **AC1** — When `python presets.py check` runs in the policy kit, it exits 0 and prints the four
  preset names with one presettable count for each.
  Red when: a shipped preset lacks a presettable key, names a `never` key, or holds a value its row
  refuses.
  figure: the count is DERIVED from the catalogue and `never`; 246 keys at v2's table, measured
  2026-10-26 by `preset-check.py` over v2.
- **AC2** — When `python check_policy.py --fixture presets-complete` runs, each plant reds
  `arm_presets` naming its preset and key: a key cut from `strict`, `hooks.bypass` set to `maybe` in
  `guarded`, `standard`'s `leases` set off its catalogue default, and a fifth table the `preset`
  row's `of` lacks; each unplanted copy is green.
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
  preset in a scratch install whose layer register attaches nothing at `point.flow.release`,
  `velocity` and `standard` exit 0 and `strict` and `guarded` exit 2, each naming `build.closes`,
  `after-release-verifies` and the point, and no other key.
  Red when: a preset is refused for a key its value does not select, or `strict` loads.
  fixture: needs the loop kit's `loop.toml`, §8 F4's `guard.py` verb and the layer register landed
  by dDeclaredLoop and dOrderedCharter; none is in the tree today.
- **AC7** — When the `presets-core-only` case plants `absent-by-key`, a loader refusing any key a
  `[[selects]]` row names whatever its value, `arm_presets` reds naming `standard` and
  `build.closes`; when it plants `accept-all`, a loader admitting every value, it reds naming
  `strict` and `build.closes`.
  Red when: either planted loader reads green, which is the clause's red both ways.
- **AC8** — When `grep -n "build.closes" loop.toml` runs in the loop kit, it prints the
  `[[selects]]` row naming `after-release-verifies` and `point.flow.release`.
  Red when: the row is absent, so `strict` and `guarded` load on a core-only install.
- **AC9** — When `python check_policy.py --repo .` runs at the repository root, it prints
  `policy-check: arm_presets · 0 finding(s)` with a population of four presets.
  Red when: the arm is absent from `ARMS` or announces itself.
- **AC10** — When the `presets-factory` case runs `python core.py new preset trial --from standard`
  in its scratch repository, `presets.toml` gains `[preset.trial]` and the `preset` row's `of` names `trial`, and
  `python core.py kinds` lists `kind.preset` out of the pending list; with `--from nope` it exits 1
  and both files keep their bytes.
  Red when: the factory leaves a non-conforming preset, or the kind stays pending.
- **AC11** — When `grep -n "never touch\|pair rule\|core-only" policy.md` runs in the help directory,
  it prints the presets section's three paragraphs.
  Red when: the page omits presets.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy check` and `policy fixtures` legs run `arm_presets` and the four cases once
dGroundRules has landed them; the arm line below is where they are declared.

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC9 AC10 · the five `presets-*` cases' plants, each staged on a copy of the shipped store, the loader or the factory's `--from nope` · none

## 8. Open questions

- **F1 — Where does the pair rule over a repository's overrides run?** (a) In `validate`, as a
  second table rule beside `budgets.check_budgets`, so the guard refuses the commit and the reader
  falls back to the last valid revision; (b) an arm only, red at the bar. (b) lets the policy guard
  commit a file the bar reds. v2:1421-1422 says a check refuses, and the `[budgets]` rule is the seam
  that already runs in `validate`. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1421
  and the seam dGroundRules-9 built. widens: none · relaxes: none
- **F2 — How is `after-release-verifies` refused on a core-only install, when its point is core?**
  TOOL-dDeclaredLoop-2 S8 refuses a value only when no core row of the layer register declares its
  point, and the release slot is declared by the core Flow row (layer-expansions.md:179;
  PLAY-dOrderedCharter-16 §4), so the rule as specced admits the value and the clause's red case
  fails. (a) Ask dDeclaredLoop to judge a `[[selects]]` row carrying `needs = "attached"` absent
  unless an installed register row lists its point in `uses`, the two `policy-file.proof` rows
  unchanged; (b) name a point no core row declares, which PLAY-dOrderedCharter-16 S3 forbids an
  expansion to attach at, so integrations could never admit the value; (c) a refusal in this kit's
  loader, a second copy of the absent-expansion rule gap-spine-07 names. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the one option keeping one rule and a value an installed expansion can
  admit; this unit's AC6 to AC8 wait on it. Ask for dDeclaredLoop, target TOOL-dDeclaredLoop-2 S8,
  accept: a `[[selects]]` row with `needs = "attached"` is refused unless an installed layer row's
  `uses` lists its point, seen red on a core-only fixture that admits `after-release-verifies`.
  widens: none · relaxes: none
- **F3 — Does a new catalogue key land without a value in every shipped preset?** v2:1421 says it
  cannot. `new policy-key` (TOOL-dDeclaredLoop-6 S4) writes only the catalogue row, so its wrapped
  `policy check` gate, which runs `arm_presets`, reds and restores every presettable key it adds.
  (a) Ask dDeclaredLoop for a `--preset <name>=<toml>` per shipped preset, or `--never`, written into
  `presets.toml` in the same restore; (b) a default copied into every preset, which v2's strict and
  guarded columns show is wrong for a posture key. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 1, v2:1421. Ask for dDeclaredLoop, target TOOL-dDeclaredLoop-6 S4, accept: `new policy-key`
  takes one `--preset <name>=<toml>` per shipped preset or `--never`, and refuses a presettable key
  missing one, seen red on a key added with the `strict` value absent. widens: none · relaxes: none
- **F4 — How does `presets.py` reach `check_expansion_value`, when `guard.py` has no verb printing its
  verdict?** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; TOOL-dDeclaredLoop-12 S4), and the
  function lives in `tools/loop/guard.py`, whose only CLI flags are `--staged`, `--push-range` and
  `--fixture` (TOOL-dDeclaredLoop-2 §4 Inventory). Options: (a) an ask to dDeclaredLoop: `guard.py
  --expansion` reads `<key>=<value>` lines on stdin, judges each with `check_expansion_value`, prints
  one line per refused pair naming the key, the value and the point, and exits 2 on any refusal, run
  by S4 as one subprocess per load; (b) a declared `requires_if` row on `tools/policy/kit.toml` naming
  `loop`, `presets.py` importing the function in process, which the rule admits only as a declaration
  `govkit selfcheck` grades and that installs nothing, the shape of `tools/memory-tree/kit.toml:8`.
  (a) keeps the call in the shape dDeclaredLoop uses for its own sibling reads (its spec 12 S4 and §8
  F5) and dWitnessedBar's spec 3 §8 F6 asks the same way; its cost is a wait, since AC6, AC7 and the
  arm's load half cannot pass until the ask lands. (b) needs no parent change, but makes the policy
  kit an in-process consumer of a loop-kit function its owner reaches only by subprocess.
  Recommendation (a). Open for the owner: the ask the build run files is "TOOL-dDeclaredLoop-2 S8:
  `guard.py --expansion` judges `<key>=<value>` lines on stdin with `check_expansion_value`, one line
  per refusal, exit 2 on any".

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-33`, `KICK-dKeptSession-44`
  mirrored, the other ends of the edges the round-1 spec audit's promoted units declare; no other
  section moved.
- rev-3 · 2026-10-26 · S4 · §3 Edges · §5 · AC6 · §8 F4 · §10 · re-grounded on the cross-check record
  `2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`, row 3: `presets.py` reaches
  `check_expansion_value` by subprocess through the policy kit's inline `resolve_kit_dir`, with F4
  open for the `guard.py` verb.

## 10. Reuse audit

The seams extended: dGroundRules' `check_value` (GR `policy.py:143`) and `read_catalogue_row`
(`:219`) for every value and key, `validate`'s table-rule seam (`:581-601`, the `budgets` call), the
`ARMS` table (`check_policy.py:737`); dDeclaredLoop's `check_expansion_value` over `[[selects]]`
(TOOL-dDeclaredLoop-2 S8), run by subprocess through the policy kit's inline `resolve_kit_dir`
(`tools/policy/policy.py:1132`, which `check_policy.py:876` already shares); the kinds contract (PLAY-dOrderedCharter-7 S4-S6). The prior art is
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-preset-check.py`: its never set
(`:30-35`), completeness and allowed-value checks (`:50-67`) and `PAIRS` (`:72`) are promoted; its
`FREE` allowed-text regex (`:56`) is not, since `check_value` judges the parsed `allowed` table.
`python tools/codebase-map/reuse_lookup.py "named policy presets completeness check pair rules"`
ranked `check`, `pair`, `checks` and `load_policy` (`tools/roles/roles_lib.py:373`, the roles kit's
house policy, a different file), name stems only: no preset code is in the tree, since `tools/policy/`
lives on `branch/unattended-dgroundrules-e47ae1` at `3c8c4718a`, read there. `python
tools/memory-recall/query.py "how are the named policy presets checked complete and loaded on a
core-only install"` returned scout A's row 1, this build's brief, and the flow review's M1
(`reviews/2026-10-15-review-PLAY-dClosedLoop-1-flow-b.md:77`), which names `build.closes` as the key
a core-only install refuses. Disagreement with the brief: TOOL-dDeclaredLoop-2 S8's absent test
cannot refuse a value whose point is core (§8 F2). Line numbers in scout A's row 1 match the branch.

Recall terms used: preset presets completeness pair rules never-touch strict guarded build.closes selects expansion core-only
