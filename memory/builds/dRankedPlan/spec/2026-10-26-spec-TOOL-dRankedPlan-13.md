# TOOL-dRankedPlan-13 — the plan record's intent fields: affected systems derived from the `code` record and checked, open questions as fork tags

**Status:** OPEN · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 7 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0381@634c7b47 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-14 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

The plan record names no affected systems and no open questions, the two intent fields the
AI-native SDLC playbook's intent carries beside gov's (gap-plan-08,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:348`). The night
pass settled both (S3, `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:396-397`):
"affected systems", derived from the code map and checked, and "open questions" as fork tags. This
unit gives the plan record (I3, TOOL-dRankedPlan-16) its three intent fields, `Scope`,
`Affected systems` and `Open questions` (shared interface I18): the scope arms the `scope-paths` code
seed TOOL-dPlacedRequest-8 left unarmed for this build, the affected systems are derived from the
`code` record's `code_file` rows over that scope and checked both ways, and each open question is a
tag `fork.<build>.<name>` in a registered `fork` namespace, so Design's forks can join it.

## 2. Scope (IN)

- **S1** — The module `tools/memory-tree/plan_fields.py` (shared with TOOL-dRankedPlan-11 and -12).
  It reads the build's one plan record, `memory/builds/<slug>/build/<date>-build-<FAMILY>-<slug>-1-plan-1.md`,
  only through TOOL-dRankedPlan-16's `find_plan_record` and `read_plan_fields`
  (`tools/memory-tree/plan_record.py`, its S4, imported within the kit), the factory's `FIELD` grammar
  under them; no plan record prints `plan field — no plan record for <slug>` and exits 1, and two exit 2
  naming both paths. The field table `FIELD_CHECKS` maps a field name to its check;
  `check_plan_fields(root, slug, field=None)` runs every listed check, or one, and the verb
  `python tools/memory-tree/plan_fields.py check <slug> [--field <name>]` prints `plan field — <name>:
  ok` or `plan field — <name>: <why>` per field and exits 1 when any refuses. This unit lists `Scope`,
  `Affected systems` and `Open questions`. Observed by AC2, AC4 and AC8.
- **S2** — `Scope`: `none`, or repository-relative paths joined by `, `, each normalised by
  `resolve_ask_path` (`tools/memory-tree/gen_build_index.py:3256`, imported within the kit). The check
  refuses an absolute path, a drive letter, a `..` segment or an empty entry, naming it, because these
  paths later select files for a role's code slot. Observed by AC8.
- **S3** — `Affected systems`, derived: `derive_affected_systems(root, scope, tree)` reads the `code`
  record's `code_file` rows for `tree` (TOOL-dTotalRecall-8 S7) and, per scope path, takes the `kit`
  of every row at the path or under it; a path no row holds, a file the build will create, takes the
  kit whose `tools/<kit>/` directory prefixes it among the kits the rows name. A row or path no kit
  holds counts as the system `unkitted`. The value is the sorted set joined by `, `, or `none` for a
  `none` scope. `python tools/memory-tree/plan_fields.py derive <slug>` prints it for the planner to
  write. Observed by AC1.
- **S4** — `Affected systems`, checked both ways: its `FIELD_CHECKS` entry re-derives S3 at HEAD's
  tree and refuses a typed value that differs, naming each `missing <system>` and `extra <system>`.
  Observed by AC2.
- **S5** — The degraded floor. When `code_meta` marks the record `degraded` (TOOL-dTotalRecall-8 S9)
  or no `code_record.py` resolves, S3 takes the tree's paths from `git ls-tree -r --name-only <tree>`
  and applies the record's own kit rule, the nearest `tools/<kit>/` holding a `kit.toml` (its S6), and
  prints `affected systems — degraded: <reason>, derived from the tree` before the value. Observed by
  AC3.
- **S6** — `Open questions`: `none`, or entries joined by `; `, each `<fork tag>: <question>`, the
  tag `fork.<build>.<name>` where `<build>` is the slug lower-cased and `<name>` one or more segments of
  the tag grammar (PLAY-dOrderedCharter-19 S1, `seg := [a-z0-9][a-z0-9-]*`, at most 64 bytes), held in
  the module as `FORK_TAG_RE` and `FORK_TAG_MAX_BYTES`. The check refuses a tag outside the shape, a tag
  naming another build, a repeated tag or an empty question, naming the entry and the rule. Observed by
  AC4 and AC5.
- **S7** — The `fork` namespace: one `[[namespace]]` row in `tools/playbook/namespaces.toml`
  (PLAY-dOrderedCharter-19 S2), `ns = "fork"`, `owner = "dRankedPlan"`, `layer = "layer.memory"`,
  `extractor = "plan_fields:extract_fork"`, `role = "describes"`, and the extractor
  `extract_fork(path, text)` in S1's module, yielding one row per `Open questions` entry of a plan
  record: its tag, kind `fork`, its line, and the question as text. The citation extractor then
  indexes every `fork.*` token a later record cites (PLAY-dOrderedCharter-19 §4). Observed by AC6.
- **S8** — The `scope-paths` seed armed. `resolve_item_seed`'s `scope-paths` arm in
  `tools/loop/loop_lib.py` (TOOL-dPlacedRequest-8 S4) runs `plan_fields.py scope <slug>` as a
  subprocess, found through the loop kit's inline `resolve_kit_dir` block, and passes its output
  through: one path per line, or the one line `unarmed — scope-paths: <why>` (`<slug> has no plan
  record`, `<slug>'s plan record scopes none`, or `no memory-tree kit resolves`). Observed by AC7.
- **S9** — The join to the plan record's schema check. `item.plan.record`'s witness is the
  plan-record schema check (flow-steps.md:184), `check_plan_record(root, slug)` in
  `tools/memory-tree/plan_record.py`, which TOOL-dRankedPlan-16 S3 lands with `record-kind.plan` and
  opens to each field owner's call. This unit's pass adds the one call `check_plan_fields(root, slug)`
  inside it, after the row's generated field check, so `plan_record.py check <slug>` prints
  `item.plan.record — unwitnessed · plan field — <name>: <why>` while a field check of this module
  refuses, and `plan.exit`, which needs every reached item's witness (flow-steps.md:190), cannot pass.
  The one call carries every entry of `FIELD_CHECKS`, TOOL-dRankedPlan-11's and -12's included.
  Observed by AC10.
- **S10** — The leg `plan-fields selftest`, argv `python3 {kit}/plan_fields.py --selftest`, subject
  `kit`, guard `{kit}/plan_fields.py`, declared as a `[[gate_leg]]` in `tools/memory-tree/kit.toml` and
  in `tools/gate-legs.json`, with `enforces = ["principle.p32"]` (§8 F6) and the rows a new leg owes:
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt` and the `gate-legs` claim of
  `memory/map/features/memory-tree-hygiene.md`; `KIT_MEMORY_TREE_VERSION`
  (`tools/memory-tree/check-memory-hygiene.sh:69`) moves, since shipped bytes move. `--selftest` runs
  every plant of `--fixture --plant <case>`, a throwaway repository under the system temp directory
  holding a planted plan record and a stub `code_record.py` answering planted `code_file` rows.
  NOT OBSERVED by a criterion: each meta-gate grades its row at the close.
- **S11** — The page `help/plan.md` (TOOL-dRankedPlan-16 S9) gains a section "The plan record's
  intent fields": the three fields, their grammar, `derive`, `check`, `scope`, and the `unkitted`
  system. Observed by AC9.

## 3. Non-goals (OUT)

- The plan record kind, its file, its writer and its schema check: TOOL-dRankedPlan-16's. This unit
  adds three fields' checks and one call into that check.
- The `code` record itself, its rows and its kit rule: TOOL-dTotalRecall-8's, read here.
- The `code` slot that turns a seed into ranges in a work order: dFurnishedOrders'. S8 hands it paths.
- Scope drift, "landed paths outside the plan's affected systems" (night-pass.md:403): dCalibratedLens'
  Loop Review metric, which reads this field.
- Joining a Design fork to the open question it settles: dIndexedDesign's `design.decompose`, which
  cites the `fork.*` tag; the fork record's grade is TOOL-dBoundRoles-11's.
- A bar leg re-checking every landed plan record: a landed record's systems drift as kits land, so
  S4 checks a plan at its own schema check only (§8 F2).

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `record-kind.plan`, the plan record whose `Scope`, `Affected systems` and `Open questions` fields this unit defines, read through `read_plan_fields`, and `check_plan_record`, the schema check S9's call joins
- **hands-off** `TOOL-dRankedPlan-11` — `plan_fields.py`, the module and `FIELD_CHECKS` table that unit lists `Read sets` in
- **hands-off** `TOOL-dRankedPlan-12` — `plan_fields.py`, the module and `FIELD_CHECKS` table that unit lists `Probes owed` in
- **consumes-from** external — dTotalRecall: the `code` record, `code_file` and `code_meta` (TOOL-dTotalRecall-8 S6, S7, S9); the record-file factory's reader (PLAY-dOrderedCharter-7 S7); the namespace registry and the tag grammar (PLAY-dOrderedCharter-19 S1, S2); each DEFERRED at base and re-grounded on its landed code
- **consumes-from** external — dPlacedRequest: `resolve_item_seed` and its `scope-paths` arm (TOOL-dPlacedRequest-8 S4), which that spec hands to this build to arm
- **hands-off** external — dCalibratedLens' scope drift reads `Affected systems`; dIndexedDesign's `design.decompose` cites the `fork.*` tags
- **hands-off** `TOOL-dRankedPlan-19` — S9's call of `check_plan_fields` inside `check_plan_record`, which carries the field refusals into the witness that unit's gate reads (round-1 spec audit, id 1)
- **hands-off** `TOOL-dRankedPlan-29` — the `Scope` check, the `scope` verb and the `plan-fields selftest` leg, which that unit's S19, S25, S34 and S39 correct (round-1 spec audit, ids 23, 30, 41, 49)
- **hands-off** `TOOL-dRankedPlan-37` — S2's `Scope` check, which that unit points at the shared `check_repo_relative_path` in `tree_lib.py` (spec audit of units 19 to 29, id 17)

## 4. Design

### Evidence

- `deviation_join.py`'s `FIELD` (`tools/memory-tree/deviation_join.py:145`) admits a field name of
  one capitalised word and at most one lower-case word, so `Affected systems` and `Open questions`
  parse; its value is one line.
- `resolve_ask_path` (`tools/memory-tree/gen_build_index.py:3256`) folds `\` to `/` and strips a
  `:<line>`, a leading `./` and a trailing `/`; `check_ask_path` (:3265) matches a path, or a
  whole-segment directory of one, which S3's prefix test repeats.
- The `kit.toml` descriptors at base sit under `tools/<kit>/` for 18 kits; `tools/govkit/` holds
  `entries/*.kit.toml` and no `kit.toml` of its own, and `skills/session-kickoff/` none, so both read
  `unkitted` under the record's rule (PINNED, `git ls-files` at `0689e7fa`).
- `extractor = "code_record:extract_code_rows"` (TOOL-dTotalRecall-8 S11) is the precedent for an
  extractor living in the memory-tree kit.

### The fields

```
- **Scope:** tools/memory-tree/gen_build_index.py, tools/loop, help/plan.md
- **Affected systems:** loop, memory-tree, unkitted
- **Open questions:** fork.dexample.view-home: does the plan view get its own file?; fork.dexample.priority-grammar: is priority a rank or a band?
```

### Derivation

| Scope path | `code_file` rows | Systems |
|---|---|---|
| a file the tree holds | its row | its `kit`, or `unkitted` |
| a directory | every row under it | each row's `kit`, `unkitted` for a row with none |
| a path the tree lacks | none | the kit whose `tools/<kit>/` prefixes it, else `unkitted` |
| `none` | — | `none` |

A scope path under a kit the build itself creates reads `unkitted` until that kit's `kit.toml`
lands, the record's own rule; S4 runs at the plan's schema check, before the kit exists, so the
derived and typed values agree there.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/memory-tree/plan_fields.py` | module | none declared for files |
| `check_plan_fields`, `derive_affected_systems`, `extract_fork` | functions | `py.function`, asked at the pass |
| `FIELD_CHECKS`, `FORK_TAG_RE`, `FORK_TAG_MAX_BYTES` | constants | none declared |
| `check`, `derive`, `scope` | verbs of `plan_fields.py` | none |
| `Scope`, `Affected systems`, `Open questions` | plan record fields | none |
| `fork` | tag namespace | none |
| `unkitted` | system value | none |
| `plan-fields selftest` | leg | none |
| plants `systems-derive`, `systems-mismatch`, `systems-degraded`, `scope-bad`, `forks`, `fork-tag-parity`, `fork-extract`, `schema-join` | fixture cases | none |

### Migration

None. No plan record exists before TOOL-dRankedPlan-16 lands the kind; the `scope-paths` arm keeps
printing `unarmed` for a build with no plan record.

### Rollout

Live at landing for every plan record written after it; a build with no plan record is untouched.

### Files touched (estimate)

- `tools/memory-tree/plan_fields.py` (new): S1 to S7, S10's fixture
- `tools/loop/loop_lib.py`: S8's arm
- `tools/playbook/namespaces.toml`: S7's row
- `tools/memory-tree/plan_record.py`: S9's call inside `check_plan_record`
- `tools/memory-tree/kit.toml`: S10's `[[gate_leg]]`
- `tools/gate-legs.json`: S10's leg
- `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt`: S10's rows
- `memory/map/features/memory-tree-hygiene.md`: the `gate-legs` claim
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION`
- `tools/memory-tree/README.md`: a line naming `plan_fields.py`
- `help/plan.md`: S11's section

### Alternatives rejected

- **Systems as the codebase-map's features**, `attribute_paths` (`tools/codebase-map/map_lib.py:1777`):
  the clause derives from the `code` record, and the map is an optional kit whose dossiers go stale.
- **Systems as raw paths**: a second copy of `Scope`, so the field would say nothing `Scope` does not.
- **A second field reader here.** TOOL-dRankedPlan-16 S4's `read_plan_fields` is the one every unit
  of this build reads a plan field through.
- **The extractor in `tools/playbook/tag_index.py`**, beside `extract_doc`: a second parser of the
  `Open questions` field in another kit, against `[one-fact]`.

## 5. Production-readiness checklist

- security — `Scope` is validated once, at S2's check, before S8 hands its paths to a role's code
  slot: no absolute path, drive letter or `..` segment. Every subprocess is an argv list, never a
  shell string. The namespace adds read-only index rows.
- perf / scale — one `code_file` read per check, cached by tree hash in the one index
  (TOOL-dTotalRecall-8 S7); the degraded floor is one `git ls-tree`.
- error / empty / loading states — no plan record, two plan records and an unresolved kit each name
  their cause; `none` is a legal value of all three fields.
- observability — every field prints its own `plan field —` line; the degraded floor says so.
- risks — the `kit` column's spelling and the `code_file` reader's call are re-grounded on
  TOOL-dTotalRecall-8's landed module (§8 F5); a new kit's paths read `unkitted` until it lands.
- testing — the eight plants of §4 and the `seed-scope` case, red and green.
- migration — none.
- user docs — `help/plan.md`, S11.

## 6. Acceptance criteria

- **AC1** — When `python plan_fields.py --fixture --plant systems-derive` runs `derive tFix` over a
  plan record planted in the fixture tree, its `Scope` four planted paths named here by basename: the
  file `a.py` in the fixture's `alpha` kit directory, the `beta` kit directory, the doc `x.md` in its
  docs directory, and the not-yet-mapped file `new.py` in the `alpha` directory; and stub `code_file`
  rows placing `a.py` in kit `alpha`, two files under the `beta` directory in kit `beta` and `x.md` in
  none, it prints `alpha, beta, unkitted`.
  Red when: a directory scope misses a kit under it, the new file is not given `alpha`, or the
  unkitted path is left out.
- **AC2** — When the plant `systems-mismatch` runs `check tFix --field "Affected systems"` with the
  field typed `alpha, beta`, it exits 1 printing `missing unkitted`; typed `alpha, beta, gamma,
  unkitted` it prints `extra gamma`; typed as AC1 derives it exits 0.
  Red when: a typed value differing from the derivation passes.
- **AC3** — When the plant `systems-degraded` sets the stub's `code_meta` to `degraded = time ceiling`,
  `derive tFix` prints `affected systems — degraded: time ceiling, derived from the tree` and the value
  AC1 prints.
  Red when: a degraded record's rows are read as whole, or the floor gives another value.
- **AC4** — When the plant `forks` runs `check tFix --field "Open questions"` over the entries
  `fork.tfix.view-home: where?; fork.other.x: why?; fork.tfix.Bad: what?; fork.tfix.view-home: again`,
  it exits 1 naming the foreign build `other`, the segment `Bad` and the repeated `fork.tfix.view-home`;
  over `none`, and over the first entry alone, it exits 0.
  Red when: a malformed, foreign or repeated tag passes.
- **AC5** — When the plant `fork-tag-parity` feeds its probe set to `FORK_TAG_RE` and to the playbook
  kit's `parse_tag`, the two agree on every probe whose namespace is `fork`.
  Red when: a probe one admits and the other refuses.
  fixture: `tag_index.py` lands with PLAY-dOrderedCharter-19; with no playbook kit the plant prints
  `unarmed`, never green.
- **AC6** — When the plant `fork-extract` runs `extract_fork` over a plan record holding two open
  questions, it yields two rows, each with its `fork.*` tag, kind `fork`, its line and its question;
  and `grep -n 'ns = "fork"' namespaces.toml` finds the row naming `plan_fields:extract_fork`.
  Red when: an entry yields no row, or the namespace row is absent.
- **AC7** — When TOOL-dPlacedRequest-8's plant `seed-scope` runs `python loop_lib.py seed
  item.design.inventory --build tFix`, planted in the fixture tree beside a plan record whose `Scope`
  is AC1's planted `a.py` and its docs directory, it prints those two paths; with no plan record it
  prints `unarmed — scope-paths: tFix has no plan record`.
  Red when: a scoped build still prints the unarmed line, or an unscoped one prints a path.
  fixture: `loop_lib.py`, `resolve_item_seed` and the `seed-scope` plant land with
  TOOL-dPlacedRequest-8; this unit plants the plan record and moves the plant's expectation.
- **AC8** — When the plant `scope-bad` runs `check tFix --field Scope` over `/etc/x, C:/y, ../z,
  tools/ok.py`, it exits 1 naming each of the first three and not the fourth; and `check tFix` with
  two plan records in the build folder exits 2 naming both paths.
  Red when: a path outside the repository passes the check.
- **AC9** — When `grep -n "intent fields" plan.md` runs over the help page, it finds S11's section
  naming `Affected systems`, `Open questions` and `unkitted`.
  Red when: the page does not describe the fields.
- **AC10** — When the plant `schema-join` runs `python plan_record.py check tFix` over AC2's
  mismatched record, it prints `item.plan.record — unwitnessed` naming `Affected systems`; over AC1's
  derived record it prints `item.plan.record — witnessed`.
  Red when: the schema check witnesses a plan record whose intent field check refuses.
  fixture: `plan_record.py` and `check_plan_record` land with TOOL-dRankedPlan-16.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `policy fixtures` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `recall floor` · `recall floor arms` · `playbook render selftest` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: tools/memory-tree/plan_fields.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC8 AC10 · the leg `plan-fields selftest` runs every plant, its failing case staged by a stub row whose kit the check does not re-derive · none

New arm: tools/loop/loop_lib.py · covers AC7 · TOOL-dPlacedRequest-8's `seed-scope` case under its `loop definition` leg, given a planted plan record, staged by a scoped build whose arm still prints `unarmed` · none

## 8. Open questions

- **F1 — What is the unit of an "affected system"?** Options: (a) the kit, the `code_file` row's
  `kit`; (b) the codebase-map's features through `attribute_paths`; (c) the layer; (d) the paths
  themselves. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1: the clause derives the systems
  "from the `code` record", whose only grouping column is `kit` (TOOL-dTotalRecall-8 S6, S7); (b) reads
  the optional map instead, (c) is carried by no `code` row, and (d) restates `Scope`. A path no kit
  holds is the system `unkitted`, so no scope path is left out of the set. widens: none · relaxes: none
- **F2 — Does "checked" refuse a mismatch or warn, and where?** Options: (a) refuse at the plan's own
  schema check; (b) warn there; (c) refuse in a bar leg over every landed plan record. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the most feature-rich survivor: [derive] checks a derived value
  both ways, and (c) would red a landed record as kits are added after it, a record this repo does not
  rewrite. widens: none · relaxes: none
- **F3 — What grammar is a fork tag?** Options: (a) `fork.<build>.<name>` in a registered `fork`
  namespace whose extractor reads the field; (b) the §8 `F<n>` ids; (c) `fork.` strings held by a
  local pattern, no namespace. (b) loses: no spec exists at Plan, and `F<n>` repeats in every spec of
  every build. (c) loses: the citation extractor indexes only a registered namespace's tokens
  (PLAY-dOrderedCharter-19 §4), so a Design record citing the tag would join nothing. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3: the clause names fork tags, and a `[[namespace]]` row is the
  registry's own extension point (TOOL-dTotalRecall-8 S11 adds `code` the same way). The build segment
  keeps two builds' open questions apart. widens: none · relaxes: none
- **F4 — Which kit holds the module?** Options: (a) the memory-tree kit, beside the `code` record,
  the record-file factory and the read budget; (b) the loop kit, beside `loop_lib.py`. (b) reaches all
  three of (a)'s neighbours by subprocess, and (a) reaches the loop kit once, at S8, the way
  TOOL-dPlacedRequest-8 S5 reaches the unattended driver. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, fewest crossings of the kit boundary. widens: none · relaxes: none
- **F5 — The parents this unit calls are DEFERRED at base.** RESOLVED (agent, 2026-10-26, delegated):
  the build run re-grounds the `code_file` reader, the factory's reader, the namespace row's columns
  and `resolve_item_seed`'s arm on their landed code, and records any difference as a §9 rev, rung 1,
  as TOOL-dTotalRecall-8 §8 F5 does. widens: none · relaxes: none
- **F6 — Which principle does the new leg enforce?** PLAY-dOrderedCharter-7 S3's meta-check reds a leg
  with no `enforces`, and v2's `[enforcement]` table names no clause of this build. Options: (a)
  `principle.p32`, every role sees the code its item touches, which S8's armed seed serves; (b)
  `principle.p33`, one relational syntax, which S7's tags serve. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3: the leg's largest share of plants is the derivation from the `code` record,
  P32's subject (v2:1029). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 13, night-pass.md:340-403 (point 6, S3
  and S4), flow-steps.md:180-190, TOOL-dRankedPlan-16 S3, S4 and S9, TOOL-dTotalRecall-8 S6, S7, S9
  and S11, TOOL-dPlacedRequest-8 S4, PLAY-dOrderedCharter-19 S1, S2 and §4, and scout A's row 6.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-19`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended: TOOL-dTotalRecall-8's `code` record (`code_file`, `code_meta`, the kit rule of its
S6), read and never re-derived except on its own degraded floor; `resolve_ask_path`
(`tools/memory-tree/gen_build_index.py:3256`, verified at base) for path normalisation; TOOL-dRankedPlan-16 S4's `read_plan_fields`, over the record-file
factory PLAY-dOrderedCharter-7 S7 extracts from `deviation_join.py` (`FIELD` :145, `read_record` :212,
verified at base), for field reads; PLAY-dOrderedCharter-19's namespace registry for the `fork` row;
and TOOL-dPlacedRequest-8 S4's `scope-paths` arm, which that spec leaves unarmed for this build.
`python tools/codebase-map/reuse_lookup.py "derive which kits a set of file paths belongs to and check
a typed list against it"` ranked name stems (`check`, `resolve_kit_dir`, `kit_rel`, `kit_dir`,
`attribute_paths`); `attribute_paths` (`tools/codebase-map/map_lib.py:1777`) maps paths to the map's
features, not kits (§4 Alternatives rejected), and no existing seam fits the fork tags, scout A's
probe over every spec and v2 finding only night-pass.md:397. Where scout A and source disagree:
scout A cites `resolve_ask_path` at :3256, matching base; TOOL-dPlacedRequest-8 S4 cites :3185, which
is stale. The recall query returned scout A's row 6 and the brief's I18 row; no record decides the
fork-tag grammar.

Recall terms used: `python tools/memory-recall/query.py "how does the plan record name its affected systems and open questions" --terms "plan record intent fields affected systems code record code_file kit open questions fork tags scope-paths"`
