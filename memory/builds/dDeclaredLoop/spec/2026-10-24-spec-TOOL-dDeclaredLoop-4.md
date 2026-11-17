# TOOL-dDeclaredLoop-4 — stage claims and the coverage gate

**Status:** CLOSED · rev-5 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 19 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0089@66b8552a whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-4-deviation-41.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-4-deviation-41.md) | deviation | — |
| [2026-10-25-build-TOOL-dDeclaredLoop-4-deviation-42.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-4-deviation-42.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-4-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-4-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-4-deviation-43.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-4-deviation-43.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-4-red-fix-26.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-4-red-fix-26.md) | red-fix | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-4-1-spec-reviewer.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-4-1-spec-reviewer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-4-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-4-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-4-build-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-4-build-brief.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-4-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-4-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

Every part of the product declares the stage it serves, so the loop is no longer implicit: a `stage`
claim on every dossier fence, gate leg, role, workflow and hook, and a coverage leg that reds an
unclaimed part and a stage with no witness, the parts joined both ways through the core's coverage
factory (gap-spine-01: "no kit, leg, dossier, role or hook declares the stage it serves"; the
walkthrough's unit 5,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md@e61a5385821e:43`;
P1, "Every shipped part declares its stage; a coverage gate reds an unclaimed part",
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:851`;
I24).

## 2. Scope (IN)

- **S1** — The claim's value: a non-empty list of step tags, each the `tag` of a `[[step]]` row that
  `tools/loop/loop_lib.py#read_steps` returns, or the one-word list `["none"]`, a declared statement
  that the part serves no build stage. A value of any other shape, an empty list, a tag that reader
  does not return, or `none` beside a tag is no claim: the part reads unclaimed, the value named.
  Observed by AC1, AC3.
- **S2** — The claim's home per part kind:
  - dossier: a top-level `stage` key in each `memory/map/features/*.md` TOML fence, written among the
    top-level keys above its `[claims]` table. `tools/codebase-map/map_lib.py#parse_dossier` admits it
    as one optional key beside its required seven, refuses it where it is not a list of non-empty
    strings, naming the key, and the `Dossier` it returns carries it as `stage`, None where the fence
    has none. The map kit grades the shape alone and reads no step tag;
  - gate leg: a `stage` field on each row of `tools/gate-legs.json`, written as the row's last key,
    as `enforces` is written;
  - workflow: the `step` of the loop definition's `[[workflow]]` row of that name, which
    `tools/loop/loop_lib.py#check_loop` already requires on every row;
  - role: derived from its role file's `workflow:` front-matter key, read through
    `tools/loop/loop_lib.py#read_role_defaults`, through that workflow's row, never typed on the role;
  - hook: one `[[hook]]` row of `tools/loop/loop.toml` per key of the map's `git-hooks` and
    `harness-hooks` inventories, with `key` and `stage`. A key naming a path under the tool root
    spells that root `{prefix}`, which the leg expands to the tool root's path relative to the
    repository root before the join (§8 F1).
  Observed by AC1, AC2, AC7.
- **S3** — The part join, `derive_part_claims` in `tools/loop/stage_coverage.py`, through
  `compute_coverage` (`tools/memory-tree/coverage_join.py#compute_coverage`) with an empty baseline.
  The five populations are inventories: the dossier stems under the map root's `features/`, read
  through `tools/codebase-map/map_lib.py#load_map_tree`; the names of the leg manifest's rows; the
  workflow names of the roles kit's `workflows.toml`, read through its `load_workflows`; the role slots
  `read_role_defaults` returns; and the `git-hooks` and `harness-hooks` keys of the map root's
  `generated/inventories.json`, read as `tools/codebase-map/reuse_lookup.py` reads it. The claims are
  one owner's, `stage-claims`: each part carrying a valid claim, each `[[hook]]` row's expanded key
  whose value is valid, each `[[workflow]]` row's name, and each role whose workflow names such a row.
  An unclaimed part is red, naming its kind and name; a claim naming no part, such as a `[[hook]]` row
  naming a hook the tree no longer holds, is red as stale. Observed by AC1, AC2, AC3.
- **S4** — The stage half, `derive_stage_witnesses`: a stage's witness is its exit item's declared
  witness. It reads the definition through `tools/loop/loop_lib.py#read_definition`, `check_loop` and
  `tools/loop/loop_lib.py#check_witness_classes`, and prints one line per step naming its exit item and
  that item's witness class. A refusal of either reader is the leg's red, printed as the reader words
  it, so a step whose exit item declares no witness is red with no predicate of this module's own
  (§8 F5). Observed by AC4.
- **S5** — The leg `loop stage coverage`, one row of `tools/gate-legs.json`: argv
  `["python", "{prefix}/loop/stage_coverage.py", "--selftest"]`, chunk `declarations`, subject `repo`,
  the ceiling `loop definition` carries, no `guard`, `"enforces": ["principle.p1"]` and
  `"stage": ["step.test"]`. It is gov's own: an `[[exempt_leg]]` row of `tools/govkit/registry.toml`,
  its row in `tools/govkit/subject-pins.tsv`, and a `gate-legs` claim of the `loop` dossier (§8 F7).
  It prints one line per join and per kind,
  `stage-coverage: part · <kind> · <n> parts · <n> unclaimed · <n> stale`, and `unarmed`, never green,
  for a population of zero, exit 1. It exits 2 `unarmed`, never a default, where the codebase-map or
  roles kit does not resolve through `tools/loop/loop_lib.py#resolve_kit_dir`, as
  `tools/loop/loop_items.py` does for its own reach. `--fixture --plant <case>` reads the tree with the
  case's one break made in memory, never on disk; `--selftest` runs the tree, then every plant through
  `tools/loop/loop_lib.py#run_selftest_cases`. Observed by AC1, AC2, AC3, AC4, AC5, AC8.
- **S6** — The seed: every dossier, leg and hook in the tree at this pass carries its claim at landing,
  by the rules of §4 "Rollout", so the leg is green over the tree it lands in. Observed by AC6.
- **S7** — The canary admits the key: `stage` joins both `KNOWN` copies of
  `tools/run-gates/run-gates.test.sh` (`tools/run-gates/run-gates.test.sh@316947ce773c:375` and :711)
  in this pass, because its arm 1a reds a manifest row carrying a key outside that set and every row
  carries one from this pass (§8 F6). No arm is added, so `FLOOR_ASSERTIONS` does not move. Observed
  by AC9.
- **S8** — The docs: `tools/codebase-map/README.md`'s `map_lib.py` entry names the optional `stage` key;
  `help/loop.md` gains a stage-claims section anchoring the new usage row,
  `script:{prefix}/loop/stage_coverage.py` in `tools/govkit/usage.toml` with the flags `--fixture`,
  `--plant=` and `--selftest`; `tools/loop/README.md` names the module; the header comment of
  `tools/loop/loop.toml` documents the `[[hook]]` row; and `tools/loop/kit.toml`'s comment names the
  module's reach. Observed by AC10.

## 3. Non-goals (OUT)

- The coverage factory itself, `compute_coverage` in `tools/memory-tree/coverage_join.py`, landed by
  dOrderedCharter-19 S9. This unit is one more consumer, never a copy.
- The step rows, the workflow rows and their reader: unit 1. The exit items' witnesses and stand-in
  rows: units 5, 9 and 13. This unit reads them through `loop_lib.py` and judges only whether each
  stage has one.
- Whether a witness holds, or whether a stand-in's owner has landed: the position engine's and the
  transition tables' (units 7 and 13).
- The loop kit's edge to memory-tree: `requires = ["memory-tree"]` already stands
  (`tools/loop/kit.toml@13965cfc3cca:58`), so the half of rev-3's S7 that added it leaves scope.
- A repository's own stage tags: a claim resolves against `read_steps`, which returns the five gov
  steps alone today, so a stage unit 25 splices is a legal claim once that reader returns it.
- Agreement between a dossier's stage and the stages of the parts it claims. The two are declared in
  two places, and no clause asks for the comparison; it is named as a follow-up, not built.
- A `stage` claim on kits, Skills, guides or gotcha classes: the clause names dossiers, legs, roles,
  workflows and hooks. FOUNDATION.md's fence may carry the key, and the leg does not grade it.
- The `stage` key on descriptors' `[[gate_leg]]` rows, its emitter and selfcheck path: unit 46. The
  near-miss control pair beside the admitted key: unit 56's S24.
- A gate leg factory's stage field: dWitnessedBar lands the gate leg kind's factory.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — `loop_lib.py`, the one reader of the loop definition's `[[step]]` and `[[workflow]]` rows, against which every claim's step tag resolves; without it no claim can be checked
- **consumes-from** external — dOrderedCharter-19 S9's `compute_coverage` in `tools/memory-tree/coverage_join.py`, and dOrderedCharter-7 S1 to S3's `principle.p<n>` registry, `enforces` key and meta-check, which S5's leg answers, all in the tree
- **hands-off** `TOOL-dDeclaredLoop-46` — the stage claim's descriptor, emitter and selfcheck path, which that unit completes (the round-1 spec audit's id 25); this pass admits the key to both canary copies (§8 F6) and carries the leg as gov's own (§8 F7), so that unit's S1 and S5 are re-grounded against both
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 9, 26, 36, 40, 58, each a scope item of that unit; its id 26 is re-grounded against this pass's `[[exempt_leg]]` row (§8 F7)
- **hands-off** `TOOL-dDeclaredLoop-25` — the `stage` key every leg row carries, and the gov-leg registration that unit's new leg follows

## 4. Design

### Evidence

Every reading below was taken on 2026-11-15 from branch/unattended-declared-loop-d56bf0 at
`a2ad508e9`, through `git show`, since this worktree's main lacks the loop kit.

- `check_loop` refuses a step row whose tag is not one of `STEP_TAGS`, the five gov steps
  (`tools/loop/loop_lib.py#check_loop`), so the legal tags are exactly what `read_steps` returns.
- Every `[[step]]` row and every `[[item]]` row declares a witness, refused when absent by
  `tools/loop/loop_lib.py#check_witness_classes`, and `check_program` refuses a step whose `exit` is no
  item of that step (`tools/loop/loop_lib.py#check_program`). Both run in `loop_lib.py --check`, the leg
  `loop definition`, which already carries `"enforces": ["principle.p1"]` in `tools/gate-legs.json`.
- Every step's exit item has a `[[stand-in]]` row today, its owning build unlanded
  (`tools/loop/loop.toml@86ccb031eca7:837` onward); the tables' checker does not check that every item
  of an unlanded build has one (`tools/loop/loop_table.py@8540d09a414a:51`).
- The fence parser requires exactly seven top-level keys, refusing any other, and `Dossier` holds no
  stage (`tools/codebase-map/map_lib.py#parse_dossier`, `tools/codebase-map/map_lib.py#Dossier`).
- `tools/gate-legs.json` holds 184 rows (PINNED, 2026-11-15); their keys are `name`, `argv`, `chunk`,
  `subject`, `ceiling`, `guard`, `enforces`, `pass_leg`, `reads`, `doc_reads`, `pack`, `signature` and
  `scope_of`, and no row carries `stage`.
- The canary's arm 1a reds a row carrying a key outside `KNOWN`, held in two copies that lack `stage`
  (`tools/run-gates/run-gates.test.sh@316947ce773c:375`, :711), and the owed-rows probe owes every key
  of every row in each copy (`tools/run-gates/owed_rows.py@cf24e52937cf:15`).
- The generated inventories hold 184 gate legs, 4 git hooks and 13 harness hooks, PINNED 2026-11-15
  (`memory/map/generated/inventories.json@91d2f99d60e3`; AC6 re-derives the counts). A harness key is `<event> <script>`, the script repo-relative
  (`tools/codebase-map/map_extractors.py#_derive_harness_hooks`), such as
  `PreToolUse tools/hooks/scratch-guard.js`.
- The install-prefix counter bans a literal kit path on any line of a tracked file under the tool root
  and drains `{prefix}/` (`tools/check-install-prefix.sh@401a476dfb69:48` to :56), and the loop kit
  ships every file it holds (`tools/loop/kit.toml@13965cfc3cca:63`), so a `[[hook]]` key spelling
  `tools/` literally would red `install-prefix (shipped surface)`.
- A role names its workflow in front matter, `workflow: build`
  (`tools/roles/agents/gov-builder.agent.md@062f8fad387c:6`), and `read_role_defaults` returns the
  roles kit's catalogue as its `load_roles` reads it, the raw keys included.
- The meta-check joins every leg through `compute_coverage` and reds a leg with no `enforces` unless a
  `leg` row of `tools/playbook/core-pending.txt` excuses it, and, under `core.bypass` `never`, a leg
  carrying both `enforces` and a `guard` (`tools/playbook/core.py#run_meta_check`). The pending list only
  shrinks (`tools/playbook/core-pending.txt@9cddd164d7e0:5`), so a new leg carries `enforces`. P1's
  clauses name this unit's `cl-dClosedLoop-0089` (`tools/playbook/principles.toml@701c20bb8c9c:12`).
- govkit's selfcheck reds a leg no descriptor claims and no `[[exempt_leg]]` row carries, and pins every
  leg's subject and chunk (`tools/govkit/govkit.py#selfcheck`); the loop legs landed since unit 15
  are `[[exempt_leg]]` rows, `loop claims fixtures` the latest
  (`tools/govkit/registry.toml@f10f1954f222:875`).
- The tag resolver reads every backticked span of tracked Markdown outside fences
  (`tools/playbook/tag_index.py#extract_citations`), and its `check` reds one naming no registered tag
  outside the builds folder.

### Data model

```toml
# memory/map/features/<feature>.md, the fence's top-level keys, above [claims]
stage = ["step.build", "step.test"]

# tools/loop/loop.toml, one row per hook inventory key
[[hook]]
key = "PreToolUse {prefix}/hooks/scratch-guard.js"   # the inventory key, the tool root spelled {prefix}
stage = ["step.build"]

[[hook]]
key = "pre-push"
stage = ["step.test"]
```

```json
{ "name": "memory hygiene", "argv": ["..."], "chunk": "...", "subject": "repo", "stage": ["step.test"] }
```

### The two halves

```
part join:  inventories = {dossier: stems, leg: names, workflow: roles-kit names, role: slots, hook: keys}
            owners      = {"stage-claims": {kind: parts carrying a valid claim, hook keys expanded}}
            baseline    = {}                       -> unclaimed parts, stale claims
stage half: check_loop and check_witness_classes over the definition
                                                   -> one line per step, a refusal red
```

The baseline is empty on purpose: a shrink-only exemption list here would let a part stay unclaimed
indefinitely, and the seed claims every part at landing.

The lines, in order:

```
stage-coverage: part · <kind> · <n> parts · <u> unclaimed · <s> stale
stage-coverage: part · <kind> · unarmed — no <kind> in the tree
stage-coverage: role <slot> · workflow <name> · <stage>
stage-coverage: stage · <step tag> · exit <item tag> · witness <class>
stage-coverage: unclaimed <kind> <name> · <no claim | the value it carries>
stage-coverage: stale <kind> <name>
stage-coverage: refused · <the reader's refusal>
```

### Rollout — the seed rules

Applied once at the build pass, each value written into its home and declared thereafter:

| Part | Seed claim |
|---|---|
| gate leg | `["step.test"]`, the bar being the Test step's verdict; also `step.build` for a leg `.githooks/pre-commit` runs on staged paths |
| git hook | `pre-commit`, `commit-msg` and `pre-rebase` `["step.build"]`; `pre-push` `["step.test"]` |
| harness hook | the steps of the workflows whose roles its script gates, or all five for a hook every session runs |
| dossier | the union of the stages its claimed legs and hooks claim, or `["none"]` for one claiming neither |
| workflow, role | unit 1's `step` field, `none` included, and its derivation |

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_part_claims`, `derive_stage_witnesses`, `main` | function | `tools/loop/stage_coverage.py` |
| `PLANTS` | the plant table | `tools/loop/stage_coverage.py` |
| `--fixture`, `--plant`, `--selftest` | CLI flags | `tools/loop/stage_coverage.py` |
| `stage` | dossier fence key and `Dossier` field | `memory/map/features/*.md`, `tools/codebase-map/map_lib.py` |
| `stage` | gate-leg row key | `tools/gate-legs.json` |
| `[[hook]]` | table | `tools/loop/loop.toml` |
| `loop stage coverage` | gate leg | `tools/gate-legs.json` |

### The fixture cases

Each plant reads the tree, makes its one break in memory, and runs both halves.

| Case | Plant | Outcome |
|---|---|---|
| `unclaimed-leg` | the first leg row's `stage` taken out | exit 1, red naming the leg |
| `unclaimed-hook` | the `[[hook]]` row of the first harness key taken out | exit 1, red naming the key |
| `stale-hook` | a `[[hook]]` row whose key no inventory holds | exit 1, red as stale |
| `bad-tag` | the first dossier's claim set to `step.ship` | exit 1, red naming the tag |
| `stage-no-witness` | the witness of `step.build`'s exit item taken out | exit 1, the refusal naming `item.build.exit` |
| `role-derived` | the `build` workflow row's `step` set to `step.test` | exit 0, role `gov-builder` reads `step.test` with no field of its own |
| `no-legs` | the leg rows emptied | exit 1, `unarmed` for the leg kind |

### Files touched (estimate)

- `tools/loop/stage_coverage.py`
- `tools/loop/loop.toml`: the `[[hook]]` rows above the `[[item]]` rows, and their header comment
- `tools/loop/kit.toml`: a comment naming the module's reach, the codebase-map and roles kits found by
  `resolve_kit_dir` with no edge, and its leg gov's own
- `tools/loop/README.md`
- `help/loop.md`: the stage-claims section, its usage anchor stamped
- `tools/govkit/usage.toml`
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/README.md`
- `tools/codebase-map/selftest.py`
- `tools/gate-legs.json`: a `stage` on every row, and the leg's row
- `tools/govkit/registry.toml`: the leg's `[[exempt_leg]]` row
- `tools/govkit/subject-pins.tsv`: the leg's row
- `tools/run-gates/run-gates.test.sh`: `stage` in both `KNOWN` copies
- `memory/map/features/`: a `stage` in every dossier, and the leg in `loop`'s claims
- `memory/map/generated/inventories.json`
- `memory/map/generated/MAP.md`
- `memory/map/generated/CARDS.md`
- `memory/map/generated/symbols.json`
- `memory/guides/SESSION-KICKOFF.md`: the audit block restamped

### Alternatives rejected

- **The stage in each dossier's `[claims]` table, keyed per part.** It puts every leg's stage in a
  dossier the leg does not live in, and the brief fixes the leg's field on its own row.
- **A stage's witness as any leg or hook claiming it.** Every leg runs in the bar, so Plan, Design and
  Deploy would have none until later builds, and the leg would land red or carry an exemption list.
- **A typed stage on each role.** The role's workflow already decides it, and a second field would be
  one fact twice.
- **A second `compute_coverage` join for the stage half.** Every exit item already declares a witness
  the definition's reader refuses when absent, so the join could never red where the reader had not
  (§8 F5).
- **Plants in a scratch repository per case.** Every population is read once from the tree and each
  break is a change to that data, as `loop_lib.py`'s plants are made in memory; a scratch copy of the
  map, the manifest and two kits would cost a clone per case for nothing more observed.

## 5. Production-readiness checklist

- security — no write path: the leg reads files and prints, and spells no kit path.
- perf / scale — one read of each population, plus the one leg unit 7 adds to the branch tip's:
  184 legs, 33 dossiers, 17 hooks, 10 workflows and 10 roles, PINNED 2026-11-15.
- error / empty / loading states — an empty population prints `unarmed` and exits 1; a fence that does
  not parse fails as the map's parser fails; a kit that does not resolve exits 2 `unarmed`.
- observability — one line per join and kind with its counts, one per derived role and per step, then
  each red.
- risks — what this change could newly red, and what keeps each green:
  - `run-gates canary` arm 1a: `stage` in both `KNOWN` copies in the same commit as the first row
    carrying it (S7).
  - `core meta-check`: the leg carries `enforces` and no `guard`.
  - `govkit selfcheck`: the `[[exempt_leg]]` row with its reason, and the subject pin row
    naming the leg with subject `repo` and chunk `declarations`, as `selfcheck --write` derives it.
  - `codebase-map coverage + freshness`: the `loop` dossier claims the leg, and the four generated files
    are regenerated after every fence gains its key.
  - `install-prefix (shipped surface)`: each `[[hook]]` key under the tool root spells `{prefix}`, and
    the module finds every file through `resolve_kit_dir`, its kit directory's parent or the map conf.
  - `tags (the resolver's checks)`: no backticked span in `help/loop.md`, `tools/loop/README.md` or
    `tools/codebase-map/README.md` names an undeclared step tag; the plant's tag is written unquoted.
  - the pass-legs check: `pass_legs.py`'s `render_pass_field` re-inserts each `pass_leg` line directly
    after its row's `name` line (`tools/run-gates/pass_legs.py#render_pass_field`), so `stage` is
    written as each row's last key and never between the two.
  - `docs`: the usage row and the anchor in `help/loop.md` land together.
  - `loop definition`, `loop item kind` and `loop transition tables`: each reads named tables of the
    definition, and none refuses an unknown table, so the `[[hook]]` rows leave them green.
  - `roles adopter self-test` and the unattended suites copy `loop.toml` into fixtures and edit named
    rows, which the new table does not touch.
- dependency — order 19, after units 7, 59 (order 17) and 14, 45, 69 (order 18). Unit 7 adds the leg
  `loop position fixtures` to `tools/gate-legs.json` and the `loop` dossier's claims, so the seed covers
  it, read from the tree this pass starts from; unit 14 changes that row's `enforces` alone. Units 59
  and 69 change `tools/loop/guard.py` and unit 45 `tools/loop/position.py`, none of which this unit
  reads. Unit 46 (order 20) carries `stage` to descriptors and adopters after it.
- registry and pins — one leg added: its `[[exempt_leg]]` row, its pin row and its dossier claim, and
  no `tools/run-gates/selftest-budgets.txt` row, since that file owes a row only to a `selftests`-chunk
  or `kit`-subject leg (`tools/run-gates/run-selftests.sh@25d3174e1eab:953`, as `loop transition tables`
  stands with none). The kickoff manifest watches `tools/gate-legs.json`, so
  `memory/guides/SESSION-KICKOFF.md`'s audit block is restamped with a `manifest-audit:` delta line.
  The verdict-epoch gate's delegate list holds memory-tree modules and the spec-token checker, no file
  of this unit, so it does not move. The kit versions are minted by the lander.
- testing — the seven fixture cases through `--selftest`, the leg over the real tree, and the map
  selftest's two fence arms.
- migration — the optional fence key; an adopter's dossiers without it still parse, and only gov's leg
  requires it.
- user docs — `tools/codebase-map/README.md` and `help/loop.md` gain the claim and its leg.

## 6. Acceptance criteria

Each of AC1 to AC6 runs the module in the loop kit's folder.

- **AC1** — When `python stage_coverage.py --fixture --plant unclaimed-leg` runs, it exits 1
  naming the leg, and with `--plant unclaimed-hook` it exits 1 naming the hook key.
  Red when: a part with no stage claim passes.
- **AC2** — When `python stage_coverage.py --fixture --plant stale-hook` runs, it exits 1
  naming the stale row's key, and with `--plant role-derived` it exits 0 and the `role gov-builder`
  line reads `step.test`.
  Red when: a claim on a removed part passes, or a role's stage is read from anything but its
  workflow's row.
- **AC3** — When `python stage_coverage.py --fixture --plant bad-tag` runs, it exits 1
  naming `step.ship`.
  Red when: a claim names a step the definition does not declare and passes.
- **AC4** — When `python stage_coverage.py --fixture --plant stage-no-witness` runs, it
  exits 1 and its `refused` line names `item.build.exit`.
  Red when: a stage whose exit item declares no witness passes.
- **AC5** — When `python stage_coverage.py --fixture --plant no-legs` runs, it prints
  `unarmed` for the leg kind and exits 1.
  Red when: an empty population reads green.
- **AC6** — When `python stage_coverage.py` runs over the repository after the seed, it
  exits 0, and its leg and hook counts equal those of `memory/map/generated/inventories.json`.
  Red when: any part of the tree is unclaimed.
  figure: the counts are DERIVED at observation from `memory/map/generated/inventories.json`.
- **AC7** — When `python -c` calls `parse_dossier` from `tools/codebase-map/map_lib.py` on a fence
  carrying `stage = ["step.build"]`, the `Dossier` it returns carries that list as `stage`, and with
  `stage = "step.build"` it raises `MapError` naming the key.
  Red when: the optional key is refused, or a non-list value is accepted.
- **AC8** — When `python -m json.tool tools/gate-legs.json` is read for the row named
  `loop stage coverage`, it carries `"enforces": ["principle.p1"]`, `"stage": ["step.test"]` and no
  `guard`, and `grep -c 'name = "loop stage coverage"' tools/govkit/registry.toml` and
  `grep -c '^loop stage coverage' tools/govkit/subject-pins.tsv` each print 1.
  Red when: the leg carries no `enforces`, carries a guard, or no registry or pin row claims it.
- **AC9** — When `grep -c '^KNOWN = {.*"stage"' tools/run-gates/run-gates.test.sh` runs, it prints 2.
  Red when: either `KNOWN` copy lacks the key, so arm 1a reds every row at landing.
- **AC10** — When `grep -c stage_coverage.py loop.md` runs in the help folder it prints at least 1,
  `grep -c 'stage_coverage.py' tools/govkit/usage.toml` prints at least 1, and
  `grep -n 'stage' tools/codebase-map/README.md` shows the `map_lib.py` entry naming the optional key.
  Red when: the leg or the key ships undocumented.

## 7. Gates

The pass also keeps `loop definition`, `loop item kind` and `loop transition tables` green; they are
named here rather than on the leg line, which the spec-token checker resolves against a tree that may
not hold the loop kit.

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `memory hygiene` · `core meta-check` · `govkit selfcheck` · `govkit selftest` · `docs` · `install-prefix (shipped surface)` · `tags (the resolver's checks)` · `roles adopter self-test` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/loop/stage_coverage.py · covers AC1 AC2 AC3 AC4 AC5 · each `--plant` case through `--selftest`, and `unclaimed-leg` red with the part join's owner fed every part · none
New arm: tools/codebase-map/selftest.py · covers AC7 · a fence with a list `stage` and one with a string · none

## 8. Open questions

- **F1 — Where does a hook's claim live?** (a) `[[hook]]` rows of the loop definition keyed by the
  map's inventory key; (b) a `stage` key in each hook fragment's JSON; (c) the dossier's fence.
  (b) has no home for the four git hooks, which have no fragment, and adds a key the settings merge
  carries into settings files; (c) puts a part's stage in a document the part does not live in. (a)
  covers both hook inventories and is joined both ways. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-24, delegated): (a). widens: none · relaxes: none. At rev-4 a key under the tool root spells
  that root `{prefix}`, since the definition ships and the install-prefix ban reds a literal kit path.
- **F2 — What is a stage's witness?** (a) Its exit item, witnessed or stood in for; (b) any leg or
  hook claiming the stage. (b) reds Plan, Design and Deploy until later builds land their checks,
  since every leg claims Test. (a) reads what unit 13's stand-ins already declare (C2-F8).
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a).
  widens: none · relaxes: none
- **F3 — May a part claim no stage?** A tool such as the drift audit serves the Loop Review, a cadence
  program, and no build stage. (a) The word `none`, declared and counted as claimed; (b) every part
  forced onto a step. (b) types false claims. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24,
  delegated): (a). widens: none · relaxes: none
- **F4 — Does the change to the map's fence parser fall under the grant?** It is a governance carrier
  under `tools/` and the clause names the dossier claim. RESOLVED (agent, 2026-10-24, delegated):
  lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the map fence's optional `stage`
  key and the gate-leg rows' `stage` field · widens: none · relaxes: none
- **F5 — How is a stage's witness read?** (a) Through the definition's own readers, `check_loop` and
  `check_witness_classes`, one line per step and their refusal the red; (b) a second `compute_coverage`
  join of the step tags against the steps whose exit item has a witness. Since units 5 and 9 every
  step row and item row declares a witness the reader refuses when absent, so (b) can never red where
  the reader has not, and its plant could not be read at all. Recommendation (a), the body's.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: one predicate, in the reader that owns it
  widens: none · relaxes: none
- **F6 — Who admits `stage` to the canary's `KNOWN` copies?** (a) This pass, in the commit whose rows
  first carry the key; (b) unit 46's S1, at order 20. Under (b) arm 1a of `run-gates canary` reds every
  row from this landing to that one. Recommendation (a), the body's; unit 46 keeps the version move
  and the emitter, and unit 56's S24 the control pair.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: the key and its admission land together
  widens: none · relaxes: none
- **F7 — Where is the leg claimed?** (a) gov's own `[[exempt_leg]]` row; (b) a `[[gate_leg]]` of the
  loop kit's descriptor, shipping the leg. Under (b) every adopter would run a leg over rows that carry
  no `stage` until unit 46 lands, over `[[hook]]` rows naming gov's hooks, stale in its tree, and over a
  map it may not install. Every loop leg landed since unit 15 is gov's `[[exempt_leg]]`.
  Recommendation (a), the body's; whether a later unit ships it is unit 46's question.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: the leg's populations are gov's tree
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-46, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md); no scope moved.
- rev-3 · 2026-10-25 · S5 · §3 Edges · §4 Evidence · AC8 · re-grounded on dOrderedCharter-7 rev-5 by
  `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md` row 23: the leg
  `loop stage coverage` carries `enforces = ["principle.p1"]` in this pass, observed by AC8, since a
  later build can add no `leg` row to the shrink-only `core-pending.txt`.
- rev-4 · 2026-11-15 · §1 · S1 S2 S3 S4 S5 S6 S7 S8 · §3 · §4 · §5 · AC1 to AC10 · §7 · §8 F1 F5 F6 F7 ·
  §10 · re-grounded at `a2ad508e9`, the tip of branch/unattended-declared-loop-d56bf0, by the brief
  2026-11-15-prompt-TOOL-dDeclaredLoop-4-1-spec-writer; mechanism, carries, order and status kept. The
  claim's tags are what `read_steps` returns; the stage half reads the definition's own witness readers
  (F5); a hook key spells the tool root `{prefix}` (F1); the leg is gov's `[[exempt_leg]]` (F7) and runs
  its plants in memory through `--selftest`; `stage` is admitted to both canary copies here (F6, S7);
  the docs and usage row are S8. The memory-tree edge already stands and leaves scope. Line citations
  become symbol citations or blob-pinned lines.
- rev-5 · 2026-11-15 · §3 · the Edges block gains the hands-off mirroring TOOL-dDeclaredLoop-25 rev-5's consumes-from edge; nothing else moved.

## 10. Reuse audit

The seam extended is the both-ways join, `compute_coverage`
(`tools/memory-tree/coverage_join.py#compute_coverage`), called as the core's meta-check calls it for
legs (`tools/playbook/core.py#run_meta_check`), and reached through the loop kit's own
`tools/loop/loop_lib.py#read_memory_tree`; this unit calls it once and copies none of it. The loop
reader's `read_steps`, `check_loop`, `check_witness_classes`, `read_role_defaults`, `resolve_kit_dir`
and `run_selftest_cases` are reused as they stand, and the map's `parse_dossier` gains one optional key
read by its own `load_map_tree`. `python tools/codebase-map/reuse_lookup.py "join each part's stage
claim to its inventory both ways and red an unclaimed part"`, run on 2026-11-15 in this worktree, cut
from main at `aebbb4a72`, which holds no loop kit, ranked `claims` in `selftest.py`, `inventory_ids`,
`check_namespace_joins` and `json_artifact_inventory`: the map's own join and inventories and the tag
resolver's namespace join, none stage-aware, so the seam is the factory named above.

Recall terms used: `python tools/memory-recall/query.py "which stage does each gate leg dossier role
and hook serve" --terms "stage claim coverage gate dossier fence gate leg workflow role hook
compute_coverage exempt_leg KNOWN"`
