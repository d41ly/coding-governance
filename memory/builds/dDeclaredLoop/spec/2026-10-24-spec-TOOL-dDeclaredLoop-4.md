# TOOL-dDeclaredLoop-4 — stage claims and the coverage gate

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 19 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0089@66b8552a whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-readers-fix-return.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-readers-fix-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

Every part of the product declares the stage it serves, so the loop is no longer implicit: a `stage`
claim on every dossier fence, gate leg, role, workflow and hook, and a coverage leg that reds an
unclaimed part and a stage with no witness, joined both ways through the core's coverage factory
(gap-spine-01: "no kit, leg, dossier, role or hook declares the stage it serves"; the walkthrough's
unit 5, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md:43-44`;
P1; I24).

## 2. Scope (IN)

- **S1** — The claim's value: a non-empty list of step tags (`step.plan`, `step.design`, `step.build`,
  `step.test`, `step.deploy`, or a repository's `step.adopter.<name>`), each one a `[[step]]` row of
  `tools/loop/loop.toml` read through `loop_lib.py`; or the single word `none`, a declared statement
  that the part serves no build stage. Observed by AC1, AC3.
- **S2** — The claim's home per part kind:
  - dossier: a top-level `stage` key in each `memory/map/features/*.md` TOML fence, which
    `tools/codebase-map/map_lib.py`'s fence parser accepts as an optional top-level key beside the
    required seven (`tools/codebase-map/map_lib.py:1042`) and refuses when it is not a list of strings;
  - gate leg: a `stage` field on each row of `tools/gate-legs.json`, the pattern of dOrderedCharter-7
    S2's `enforces`;
  - workflow: the `step` field of each `[[workflow]]` row unit 1 writes in `tools/loop/loop.toml`;
  - role: derived from its `workflow:` front-matter key (`tools/roles/agents/gov-builder.agent.md:6`)
    through that row, never typed;
  - hook: a `[[hook]]` row of `tools/loop/loop.toml` per key of the map's `harness-hooks` and
    `git-hooks` inventories, with `key` and `stage`.
  Observed by AC1, AC2.
- **S3** — The part join, in `tools/loop/stage_coverage.py`: the five part populations as
  inventories (dossier stems; leg names; workflow names; role slots; the `harness-hooks` and
  `git-hooks` keys read from `memory/map/generated/inventories.json`), and the claims as one owner's,
  through `compute_coverage`. An unclaimed part is red, naming its kind and name; a claim naming no
  part, such as a `[[hook]]` row naming a hook the tree no longer holds, is red as stale. Observed by AC1, AC2.
- **S4** — The stage join: the step tags as the inventory, and as claims each step's exit item (the
  `exit` of its `[[step]]` row) where that item declares a witness or a stand-in row stands in for it,
  read through `loop_lib.py`, through `compute_coverage` again. A step with no witnessed exit item is
  red as a stage with no witness; a claim naming an undeclared step tag is red. Observed by AC3, AC4.
- **S5** — The leg `loop stage coverage` in `tools/gate-legs.json`, argv
  `python {prefix}/loop/stage_coverage.py`, printing one line per join and per kind,
  `stage-coverage: <join> · <kind> · <n> parts · <n> unclaimed · <n> stale`, and `unarmed`, never
  green, for a population of zero. Its `--fixture --plant <case>` builds a scratch repository per
  case. Observed by AC1 to AC5.
- **S6** — The seed: every dossier, leg and hook carries its claim at landing, by the rules of §4
  "Rollout", so the leg is green over today's tree. Observed by AC6.
- **S7** — The kit's `requires` gains `memory-tree`, through whose `coverage_join.py` the join is
  imported as codebase-map imports it, and `tools/codebase-map/README.md` names the optional `stage`
  key. Observed by AC7.

## 3. Non-goals (OUT)

- The coverage factory itself, moved to `tools/lib/coverage_join.py` and shipped in
  `tools/memory-tree/coverage_join.py` by dOrderedCharter-19 S9. This unit is its third consumer,
  never a third copy.
- The stage rows, the workflow rows and their reader: unit 1. The exit items' witnesses and stand-in
  rows: units 9 and 13. This unit reads them through `loop_lib.py` and judges only whether each stage
  has one.
- Agreement between a dossier's stage and the stages of the parts it claims. The two are declared in
  two places, and no clause asks for the comparison; it is named as a follow-up, not built.
- A `stage` claim on kits, Skills, guides or gotcha classes: the clause names dossiers, legs, roles,
  workflows and hooks.
- A gate leg factory's stage field: dWitnessedBar lands the gate leg kind's factory.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — `loop_lib.py`, the one reader of the loop definition's `[[step]]` and `[[workflow]]` rows, against which every claim's step tag resolves; without it no claim can be checked
- **consumes-from** external — dOrderedCharter-19 S9's `compute_coverage` in `tools/memory-tree/coverage_join.py`, landed before this build's build run
- **hands-off** `TOOL-dDeclaredLoop-46` — the stage claim's descriptor, emitter and selfcheck path, which that unit completes (the round-1 spec audit's id 25)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 9, 26, 36, 40, 58, each a scope item of that unit

## 4. Design

### Evidence

- Coverage is per inventory key: `compute_coverage` asserts unclaimed, stale-claim, stale-baseline and
  lazy-baseline both ways (`tools/codebase-map/map_lib.py:1404-1432`), over the inventories
  `map_extractors.py` builds (`tools/codebase-map/map_extractors.py:193-215`).
- The fence parser refuses any top-level key outside its seven (`tools/codebase-map/map_lib.py:1042-1048`).
- `tools/gate-legs.json` rows carry `argv`, `ceiling`, `chunk`, `doc_reads`, `guard`, `name`,
  `reads`, `signature` and `subject`, read 2026-10-24 over 142 rows (PINNED); no row carries a stage.
- The generated inventories hold 142 gate legs, 4 git hooks and 12 harness hooks
  (`memory/map/generated/inventories.json`, read 2026-10-24, PINNED; AC6 re-derives the counts).
- A role names its workflow in front matter, `workflow: build` (`tools/roles/agents/gov-builder.agent.md:6`).
- codebase-map imports the memory tree's modules because its descriptor requires that kit
  (`tools/codebase-map/kit.toml:7`).

### Data model

```toml
# memory/map/features/<feature>.md, the fence
stage = ["step.build", "step.test"]

# tools/loop/loop.toml, one row per hook
[[hook]]
key = "PreToolUse:scratch-guard.js"     # a harness-hooks or git-hooks inventory key, verbatim
stage = ["step.build"]
```

```json
{ "name": "memory hygiene", "argv": ["..."], "stage": ["step.test"] }
```

### The two joins

```
part join:  inventories = {dossier: stems, leg: names, workflow: names, role: slots, hook: keys}
            owners      = {"stage-claims": {kind: parts carrying a valid claim}}
            baseline    = {}                       -> unclaimed parts, stale claims
stage join: inventories = {"step": declared step tags}
            owners      = {"exit-witness": {"step": steps whose exit item has a witness or stand-in}}
            baseline    = {}                       -> stages with no witness, claims on no step
```

The baseline is empty on purpose: a shrink-only exemption list here would let a part stay unclaimed
indefinitely, and the seed claims every part at landing.

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
| `--fixture` | CLI flag | `tools/loop/stage_coverage.py` |
| `stage` | dossier fence key, gate-leg field | `memory/map/features/*.md`, `tools/gate-legs.json` |
| `[[hook]]` | table | `tools/loop/loop.toml` |
| `loop stage coverage` | gate leg | `tools/gate-legs.json` |

### The fixture cases

| Case | Plant | Outcome |
|---|---|---|
| `unclaimed-leg` | a leg row with no `stage` | red naming the leg |
| `unclaimed-hook` | a harness hook key with no `[[hook]]` row | red naming the key |
| `stale-hook` | a `[[hook]]` row whose key no inventory holds | red as stale |
| `bad-tag` | a dossier claiming `step.ship` | red naming the undeclared tag |
| `stage-no-witness` | a step whose exit item has no witness and no stand-in | red naming the step |
| `role-derived` | a role whose workflow's row says `step.build` | the role claimed with no field of its own |

### Files touched (estimate)

- `tools/loop/stage_coverage.py`
- `tools/loop/loop.toml`
- `tools/loop/kit.toml`
- `tools/loop/README.md`
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/README.md`
- `tools/codebase-map/selftest.py`
- `help/loop.md`
- `tools/gate-legs.json`
- `memory/map/features/`
- `memory/map/generated/inventories.json`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The stage in each dossier's `[claims]` table, keyed per part.** It puts every leg's stage in a
  dossier the leg does not live in, and the brief fixes the leg's field on its own row.
- **A stage's witness as any leg or hook claiming it.** Every leg runs in the bar, so Plan, Design and
  Deploy would have none until later builds, and the leg would land red or carry an exemption list.
- **A typed stage on each role.** The role's workflow already decides it, and a second field would be
  one fact twice.

## 5. Production-readiness checklist

- security — no write path: the leg reads files and prints.
- perf / scale — one read of each population; 142 legs, 31 dossiers, 16 hooks, 10 workflows and 10
  roles at base (PINNED, 2026-10-24).
- error / empty / loading states — an empty population prints `unarmed` and exits 1; an unparsable
  fence fails as the map's parser fails.
- observability — one line per join and kind with its counts, then each red part.
- risks — the seed's judgement on harness hooks; every value is declared and reviewable in its home.
- testing — the six fixture cases and the leg over the real tree.
- migration — the optional fence key; an adopter's dossiers without it still parse, and only the loop
  kit's leg requires it.
- user docs — `tools/codebase-map/README.md` and `help/loop.md`, which unit 1 creates, gain the claim
  and its leg.

## 6. Acceptance criteria

- **AC1** — When `python stage_coverage.py --fixture --plant unclaimed-leg` runs, it exits 1 naming
  the leg, and with `--plant unclaimed-hook` naming the hook key.
  Red when: a part with no stage claim passes.
- **AC2** — When `python stage_coverage.py --fixture --plant stale-hook` runs, it exits 1 naming the
  stale row, and with `--plant role-derived` the role reads claimed.
  Red when: a claim on a removed part passes, or a role needs a field of its own.
- **AC3** — When `python stage_coverage.py --fixture --plant bad-tag` runs, it exits 1 naming
  `step.ship`.
  Red when: a claim names a step the definition does not declare and passes.
- **AC4** — When `python stage_coverage.py --fixture --plant stage-no-witness` runs, it exits 1 naming
  the step.
  Red when: a stage with no witnessed exit item passes.
- **AC5** — When `python stage_coverage.py --fixture --plant unclaimed-leg` runs with the leg file
  emptied, it prints `unarmed` for the leg kind and exits 1.
  Red when: an empty population reads green.
- **AC6** — When `python stage_coverage.py` runs over the repository after the seed, it
  exits 0 and its counts equal the generated inventories' leg and hook counts.
  Red when: any part of today's tree is unclaimed.
  figure: the counts are DERIVED at observation from `memory/map/generated/inventories.json`.
- **AC7** — When a dossier fence with `stage = ["step.build"]` is parsed by
  `tools/codebase-map/map_lib.py`, it loads, and with `stage = "step.build"` it raises naming the key.
  Red when: the optional key is refused, or a non-list value is accepted.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/loop/stage_coverage.py · covers AC1 AC2 AC3 AC4 AC5 · each `--plant` case, and `unclaimed-leg` red with the part join's owner fed every part · none
New arm: tools/codebase-map/selftest.py · covers AC7 · a fence with a list `stage` and one with a string · none

## 8. Open questions

- **F1 — Where does a hook's claim live?** (a) `[[hook]]` rows of the loop definition keyed by the
  map's inventory key; (b) a `stage` key in each hook fragment's JSON; (c) the dossier's fence.
  (b) has no home for the four git hooks, which have no fragment, and adds a key the settings merge
  carries into settings files; (c) puts a part's stage in a document the part does not live in. (a)
  covers both hook inventories and is joined both ways. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-24, delegated): (a). widens: none · relaxes: none
- **F2 — What is a stage's witness?** (a) Its exit item, witnessed or stood in for; (b) any leg or
  hook claiming the stage. (b) reds Plan, Design and Deploy until later builds land their checks,
  since every leg claims Test. (a) reads what unit 13's stand-ins already declare (C2-F8).
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24, delegated): (a). widens: none ·
  relaxes: none
- **F3 — May a part claim no stage?** A tool such as the drift audit serves the Loop Review, a cadence
  program, and no build stage. (a) The word `none`, declared and counted as claimed; (b) every part
  forced onto a step. (b) types false claims. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-24,
  delegated): (a). widens: none · relaxes: none
- **F4 — Does the change to the map's fence parser fall under the grant?** It is a governance carrier
  under `tools/` and the clause names the dossier claim. RESOLVED (agent, 2026-10-24, delegated):
  lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3 the map fence's optional `stage`
  key and the gate-leg rows' `stage` field · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-46, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md); no scope moved.

## 10. Reuse audit

The seam extended is the both-ways join, `compute_coverage`, today at
`tools/codebase-map/map_lib.py:1404` and moved by dOrderedCharter-19 S9 to
`tools/memory-tree/coverage_join.py`; this unit calls it twice and copies none of it. The fence parser
(`tools/codebase-map/map_lib.py:1042`) gains one optional key, and the gate-leg rows gain one field in
the pattern of `enforces`. `python tools/codebase-map/reuse_lookup.py "join each part claim to an
inventory both ways and red an unclaimed part"` ranked `claims` in `selftest.py`, `inventory_ids` and
`json_artifact_inventory`, which are the map's own join and inventories, the seam named above; no
stage-aware seam exists. The scout cited `compute_coverage` at :1404 and the inventories at
`map_extractors.py:193`; both agreed with source.

Recall terms used: `python tools/memory-recall/query.py "which stage does each gate leg dossier role
and hook serve" --terms "stage claim coverage gate dossier fence gate leg workflow role hook
compute_coverage ratchet"`
