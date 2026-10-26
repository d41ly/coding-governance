# TOOL-dLinkedLibrary-20 — the `feature` namespace armed as an instruction selector

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 11 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0257@ac01a5f8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md) | research | TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-21 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |

<!-- /gen:spec-records -->

## 1. Goal

An instruction cannot be scoped to a feature today: the night pass asked "Can an instruction be
scoped to a feature?" and the owner answered "Yes, a selector (Recommended)" (NP-13,
`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:533`, `:661`), so
"pulling a feature's tag brings its instructions with its regions" (the same record, point 4 item 5).
This unit arms the `feature` namespace as an instruction selector when it registers: its registry
row carries `role = "selects"`, so an instruction unit scoped to `feature.<name>` is selected, typed
as an `instructs` edge and listed in that feature's bundle, and a feature no unit selects stays legal.

## 2. Scope (IN)

Preconditions this unit calls and does not build, each DEFERRED at base `5fede642` and landed before
this build run: the registry `tools/playbook/namespaces.toml` and its row shape
(PLAY-dOrderedCharter-19 S2), the resolver and fixture `tools/playbook/gov_tag.py`
(PLAY-dOrderedCharter-19 S6, S13), the edge registry's `selects` class (PLAY-dOrderedCharter-24 S4,
S6), the joins (PLAY-dOrderedCharter-10 S4), unit selection (PLAY-dOrderedCharter-9 S4), the site
adapters (PLAY-dOrderedCharter-28 S5), the bundle (PLAY-dOrderedCharter-25 S1, S7) and the `feature`
row with `extract_feature` (TOOL-dTotalRecall-9 S1). The members are the `feature.<name>` tags
TOOL-dLinkedLibrary-19 derives from each dossier header.

- **S1** — The row's role. The `feature` row of `tools/playbook/namespaces.toml`, which
  TOOL-dTotalRecall-9 S1 registers, carries `role = "selects"`. Where the landed row already reads
  `selects`, the pass leaves the row unchanged and says so in its commit's `Decided:` trailer; where
  it reads `describes`, the pass sets `selects` and changes no other field. No second `feature` row is
  written. Observed by AC1 and AC2.
- **S2** — The selection reaches every existing reader with no edit to any of them. An instruction
  unit whose scope names `feature.<name>` is: a legal `instructs=feature.<name>` edge, since
  PLAY-dOrderedCharter-24 S6 opens `instructs` to every `selects` row; read into that edge by the
  instruction-unit site adapter of PLAY-dOrderedCharter-28 S5; returned by
  `derive_unit_selection(units, "feature.<name>")` (PLAY-dOrderedCharter-9 S4); and listed under
  instructions by `gov_tag.py bundle feature.<name>` (PLAY-dOrderedCharter-25 S1). The pass edits none
  of `edges.toml`, `edge_grammar.py`, `instruction_units.py` or the bundle. Observed by AC2 and AC3.
- **S3** — A feature no unit selects stays legal. The dead-selector arm of PLAY-dOrderedCharter-10
  S4 stays named to `reader` and `practice`, as TOOL-dDeclaredLoop-18 §4 keeps it for `step` and
  `item`: a declared `feature` member no unit selects is printed among the unused members, never red,
  and a `feature.<name>` a unit's scope names that no extractor declares stays red through that join's
  cited-but-undeclared half (§8 F2). Observed by AC4.
- **S4** — The plants, on PLAY-dOrderedCharter-19 S13's `gov_tag.py --fixture --plant <case>`, each
  a scratch registry holding a `feature` row, a dossier header or `gov:feature` anchor declaring
  `feature.alpha`, and one instruction unit:
  `feature-selects` (the row `selects`, the unit scoped to `feature.alpha`),
  `feature-describes` (the same with the row flipped to `describes`),
  `feature-unselected` (a second declared member `feature.beta` no unit selects) and
  `feature-undeclared` (the unit scoped to `feature.gamma`, which nothing declares).
  Observed by AC2 to AC5.
- **S5** — `tools/playbook/README.md`'s line naming the build that arms each later namespace
  (PLAY-dOrderedCharter-10 S5) names dTotalRecall as registering `feature` and dLinkedLibrary as
  arming it as a selector, with this unit's id. Observed by AC6.

## 3. Non-goals (OUT)

- The `feature` row itself, its `source` and `extractor`, and `extract_feature`: TOOL-dTotalRecall-9
  S1's. This unit sets one field of that row.
- The feature members: the dossier header as the node is TOOL-dLinkedLibrary-19's, and `gov:feature`
  anchors are TOOL-dLinkedLibrary-4's.
- Writing any instruction unit scoped to a feature. A reuse entry is a level-3 instruction unit
  (TOOL-dLinkedLibrary-1); whether its scope names `feature.<name>` is that unit's to say, and every
  unit written later is data this arming admits.
- The edge registry, the grammar, the join factory, the selection, the bundle and the resolver: their
  units' (S2's preconditions), called and never re-specced.
- A feature binding join beside `check_role_bindings` (TOOL-dBoundRoles-14 S5): that join binds a
  role's `rules:` to the units naming it, and a feature carries no field a unit's scope must agree with,
  so a third join would grade nothing the cited-but-undeclared half does not.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-19` — `feature.<name>`, the members derived from each dossier header that a unit scoped to a feature selects; without them `feature-selects` has no real member to name
- **consumes-from** external — dTotalRecall's `feature` row and `extract_feature` (TOOL-dTotalRecall-9 S1); dOrderedCharter's registry, resolver, fixture, `selects` class, joins, selection, site adapters and bundle (PLAY-dOrderedCharter-19, -24, -10, -9, -28, -25)
- **hands-off** external — the ask of §8 F1, that TOOL-dTotalRecall-9 S1 spells `role = "selects"` on the row it registers

## 4. Design

### Evidence

- No `tools/playbook/namespaces.toml`, `gov_tag.py`, `edge_grammar.py` or `edges.toml` exists at base
  (`ls tools/playbook/` lists `README.md`, `adopt-playbook.sh`, `fleet.toml`, `kit.toml`,
  `render_playbook.py`); every reader this unit relies on is specced and unbuilt.
- PLAY-dOrderedCharter-19 S2's row shape names `role` (`selects` or `describes`); its own `doc` row
  reads `describes`.
- PLAY-dOrderedCharter-24 S6 and AC6 already plant `feature` with `role = "selects"` admitting
  `instructs=feature.x` with `edges.toml` unchanged, and `describes` refusing it.
- PLAY-dOrderedCharter-25 §3 says "`feature` as a selector and its namespace: dTotalRecall registers
  it (NP-13)", and the night pass point 4 item 5 says "armed by dTotalRecall when it registers the
  namespace"; v2's chain row moved the arming clause to this build (`cl-dClosedLoop-0257`).
- TOOL-dTotalRecall-9 S1 registers the `feature` row and names no `role` value: scout C's
  disagreement at `memory/builds/dLinkedLibrary/build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md:36`.
- Five later selectors already exist in specs beside `reader` and `practice`: `role`
  (TOOL-dBoundRoles-14), `step` and `item` (TOOL-dDeclaredLoop-18), `leg` and `pack`
  (TOOL-dWitnessedBar-12). None widens the dead-selector arm, and TOOL-dDeclaredLoop-18 §4 states why
  for its two: "a step or item no unit selects is printed, never red".

### The row after this unit

```toml
# tools/playbook/namespaces.toml — the row TOOL-dTotalRecall-9 S1 writes; this unit owns `role` only
[[namespace]]
ns = "feature"
owner = "dTotalRecall"
extractor = "record_extract:extract_feature"
role = "selects"
```

The other fields, `source` among them, are dTotalRecall's as it lands them; the block shows only the
row's key, its owner and extractor as TOOL-dTotalRecall-9 S1 spells them, and the one field this unit
writes.

### What each reader does with it

| Reader | With `selects` | With `describes` |
|---|---|---|
| `edge_grammar.py`, the `instructs` row's `to = ["selects"]` | `instructs=feature.alpha` parses | refused, the target outside `to` |
| the instruction-unit site adapter | a scope tag `feature.alpha` becomes `instructs` | the same edge, then refused as above |
| `derive_unit_selection(units, "feature.alpha")` | returns the unit | returns the unit (it reads scope, not role) |
| `gov_tag.py bundle feature.alpha` | the unit under instructions | instructions read `searched-empty` |
| PLAY-dOrderedCharter-10 S4, cited-but-undeclared | `feature.gamma` red | the same |
| PLAY-dOrderedCharter-10 S4, dead selector | `feature.beta` printed, exit 0 | printed, exit 0 |

The arming is therefore observable at two readers, the edge parser and the bundle; selection by scope
does not read `role`, which is why AC3 observes the bundle rather than the selection alone.

### Inventory

Minted: the four plant names of S4. No function, flag, file or key. Naming cells: none; the plant
names are fixture case names, which no lexicon cell grades.

### Migration

None. The row's other fields, every member and every instruction unit are unchanged; a unit written
before this pass that names `feature.<name>` was red as an `instructs` target and turns legal.

### Rollout

Live at landing. A repository with no instruction unit scoped to a feature sees no change in any
check's verdict.

### Files touched (estimate)

- `tools/playbook/namespaces.toml`: the `feature` row's `role` (S1)
- `tools/playbook/gov_tag.py`: the four plants of S4 in its fixture
- `tools/playbook/README.md`: S5's line

### Alternatives rejected

- **The dead-selector arm reading `role = "selects"` rows.** It would red every declared feature no
  unit selects, which at landing is every one of them (§8 F2).
- **A new `[[namespace]]` field naming whether unused members are red.** No reader asks for it beyond
  this arm, and it changes PLAY-dOrderedCharter-19 S2's row shape, a parent's contract.
- **Leaving the role to dTotalRecall alone.** The clause gives the arming to this build, and
  TOOL-dTotalRecall-9 names no value, so nothing would make the row `selects`.

## 5. Production-readiness checklist

- security — no new write path: one field of a tracked registry row, edited by the pass.
- perf / scale — none: the registry gains no row and the index no extractor.
- error / empty / loading states — a feature no unit selects is printed, never red; a scope naming an
  undeclared feature is red with its path and line, through the existing join.
- observability — `gov_tag.py check` names every unused selector member it prints.
- risks — a later build reading `role` to red unused members would red every feature; S3 and §8 F2
  record why the arm stays literal.
- testing — S4's four plants, red and green, on the parent's fixture.
- migration — none.
- user docs — N/A — the tag verbs' reference pages are rendered from their rows by
  PLAY-dOrderedCharter-37, and S5 updates the playbook kit's README line that names each namespace's
  arming build.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys, tomllib; print([r['role'] for r in tomllib.load(open(sys.argv[1], 'rb'))['namespace'] if r['ns'] == 'feature'])" namespaces.toml`
  runs in `tools/playbook` after the pass, it prints `['selects']`.
  Red when: the row reads `describes`, or a second `feature` row exists and two values print.
- **AC2** — When `python gov_tag.py --fixture --plant feature-selects` runs, `edge_grammar.py --parse`
  over the plant's instruction unit prints one `instructs` edge to `feature.alpha` and exits 0; under
  `--plant feature-describes` the same parse exits 1 naming `feature.alpha` and the `instructs` row's
  `to`.
  Red when: a descriptor `feature` row admits `instructs=feature.alpha`, or a selector row refuses it.
- **AC3** — When `python gov_tag.py --fixture --plant feature-selects` runs `gov_tag.py bundle
  feature.alpha`, the bundle lists the planted unit under instructions; under `--plant
  feature-describes` its instructions section reads `searched-empty`.
  Red when: the selector's unit is missing from its feature's bundle.
- **AC4** — When `python gov_tag.py --fixture --plant feature-unselected` runs `gov_tag.py check`, it
  exits 0 and prints `feature.beta` among the unused selector members.
  Red when: a declared feature no unit selects turns the check red.
- **AC5** — When `python gov_tag.py --fixture --plant feature-undeclared` runs `gov_tag.py check`, it
  exits 1 naming `feature.gamma` with the instruction unit's path and line.
  Red when: a unit scoped to a feature nothing declares passes.
- **AC6** — When `grep -n "feature" README.md` runs in `tools/playbook`, the line naming each later
  namespace's arming build names dTotalRecall for `feature` and `TOOL-dLinkedLibrary-20` for its
  selector.
  Red when: the README still names no build arming the `feature` selector.

## 7. Gates

The pass adds no leg: PLAY-dOrderedCharter-19's `tags` leg runs `gov_tag.py check` over the tree once
its build lands, and this unit's row value joins it as data. It is named here rather than on the leg
line because it does not exist at this spec's base.

`playbook render selftest` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC2 AC3 AC4 AC5 · the playbook-render selftest runs `gov_tag.py --fixture` under each plant of S4, its failing case staged by `feature-describes` admitting the edge and `feature-undeclared` passing · none

## 8. Open questions

- **F1 — Who writes `role = "selects"` on the `feature` row?** Options: (a) this unit sets the field
  at its build pass where the landed row lacks it, and asks dTotalRecall to spell it in
  TOOL-dTotalRecall-9 S1 so the row is armed the moment it registers; (b) an ask alone, building
  nothing here; (c) this unit writes its own `feature` row. (b) leaves the clause unbuilt whenever
  dTotalRecall lands the row as `describes`, and (c) is a second row for one namespace, which
  PLAY-dOrderedCharter-19's registry refuses. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1:
  v2's chain row gives this build the arming (`cl-dClosedLoop-0257`), NP-13 settles the value, and
  PLAY-dOrderedCharter-24 S6 and -25 §3 already read the row as a selector; the parent spec is never
  edited here, so the ask goes to dTotalRecall for the main loop to file: target build dTotalRecall,
  accept TOOL-dTotalRecall-9 S1's `feature` row is written with `role = "selects"`, seen as
  `edge_grammar.py --parse` admitting `instructs=feature.<name>` over the landed registry with no
  edit by a later build. widens: none · relaxes: none
- **F2 — Does a declared feature no unit selects red, as an unused `reader` or `practice` does?**
  Options: (a) no: the dead-selector arm stays named to `reader` and `practice`, and an unused feature
  is printed; (b) yes: the arm reads every `role = "selects"` row, through a selector-set function this
  unit extracts into `tag_index.py`, the brief's "factory at the third instance"; (c) an ask to
  dOrderedCharter for (b) in PLAY-dOrderedCharter-10 S4. (b) and (c) red every feature at landing,
  since no instruction unit selects one yet, and red the `role`, `step`, `item`, `leg` and `pack`
  members their own specs keep printed, so both fail AC4 and contradict TOOL-dDeclaredLoop-18 §4.
  The literal pair is not a second spelling of the selector set: it names the narrower set whose
  members exist only to select, which `role` does not say, so no factory is owed. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the only option satisfying AC4; the brief's count was wrong, as
  `feature` is the sixth later selector, not the third, and the return says so. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 20, NP-13, the night pass point 4,
  PLAY-dOrderedCharter-19 S2, -24 S6, -10 S4, -9 S4, -25 S1, -28 S5, TOOL-dTotalRecall-9 S1,
  TOOL-dDeclaredLoop-18 §4, TOOL-dBoundRoles-14 S5, and scout C's row for this unit.

## 10. Reuse audit

The seam extended is the namespace registry's `role` field (PLAY-dOrderedCharter-19 S2) on the row
TOOL-dTotalRecall-9 S1 registers, read by the edge registry's `selects` class (PLAY-dOrderedCharter-24
S6) and the bundle (PLAY-dOrderedCharter-25 S1); the fixture extended is PLAY-dOrderedCharter-19 S13's
`gov_tag.py --fixture`, as TOOL-dBoundRoles-14 S8 extends it. `python tools/codebase-map/reuse_lookup.py
"register a tag namespace as an instruction selector"` ranked name-stem neighbours (`check_rule_tags`,
`resolve_landing_tag`, `check_selected`, `selectable` in `tools/memory-tree/gotchas.py`); none
registers a namespace or reads a selector role, since the registry is unbuilt at base, so no existing
seam at base fits and the specced registry is the seam. Scout C's row named a feature binding join
beside `check_role_bindings` in `gov_tag.py`; §3 records why it is not built. Scout C's line for the
dead-selector join was verified against PLAY-dOrderedCharter-10 S4 (line 56 of its spec, "the two
selector namespaces `reader` and `practice`"), and its "third selector" count disagrees with the
five later selector rows found in TOOL-dBoundRoles-14, TOOL-dDeclaredLoop-18 and TOOL-dWitnessedBar-12.
The recall query returned scout C's row, the brief's row and PLAY-dOrderedCharter-24 S6.

Recall terms used: `python tools/memory-recall/query.py "how does the feature namespace become an instruction selector" --terms "feature namespace selector role selects instructs NP-13 namespaces.toml dead-selector unarmed binding join"`
