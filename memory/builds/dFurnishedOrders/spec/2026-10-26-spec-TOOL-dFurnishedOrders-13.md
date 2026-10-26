# TOOL-dFurnishedOrders-13 — the orientation scout composing the card's project-map cell, placed and shape-checked at the append, not installed until the map renderer lands

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 6 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0204@34f664ed whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-a.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |

<!-- /gen:spec-records -->

## 1. Goal

The project map's delivery gives the orientation scout the whole map and has it compose the card's
map cell within the card's 8 KB: the map's header and the build's neighbourhood, which is its layer,
its chain build's line, its features, its gap areas and the live builds overlapping its write set
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md:620`). The card
has no such cell today, and nothing renders a project map at base. This unit gives the card the
cell: composed by the scout TOOL-dFurnishedOrders-1 spawns, placed among the card's cells by the
append, checked there for the map's header, and rendered `not installed` until
TOOL-dTotalRecall-14's renderer lands.

## 2. Scope (IN)

- **S1** — The cell, shared interface J8 respelled by §8 F1: `project-map — <the level-0 header>`,
  then the neighbourhood as rows indented two spaces, the multi-line form the `overlaps —` cell
  already takes (`skills/session-kickoff/manifest-check.sh:546-553`). The header is
  TOOL-dTotalRecall-14 S5's first line, `map <tree-id> · nodes <n> · lines <n> · …`, copied
  verbatim. Observed by AC3.
- **S2** — The not-installed state. `check_card_map` in `skills/session-kickoff/manifest-check.sh`,
  called by `add_card_body` (`:1141`) on a body carrying a READY line, resolves
  `resolve_kit_file memory-tree gov_map.py` (`:854`). With none resolved, the stored card's startup
  gains `project-map — not installed: no gov_map.py in this tree (TOOL-dTotalRecall-14)` after its
  `live —` cell. Observed by AC1.
- **S3** — An invented map is refused. With no `gov_map.py` resolved, a body carrying a
  `project-map —` cell exits 1 naming the not-installed state, and nothing is appended. Observed by
  AC2.
- **S4** — The composed cell placed and checked. With `gov_map.py` resolved, the body must carry
  exactly one `project-map —` cell whose head matches `^project-map — map \S+ · nodes [0-9]+ · lines
  [0-9]+( · |$)`; the cell, its head and every indented row beneath it, is lifted out of the body and
  placed after the startup's `live —` cell, as the append already re-renders the `tree —` cell
  there (`:1171-1172`). A body with no cell, two cells or a head off the grammar exits 1 naming the
  shape, and nothing is appended. Observed by AC3 and AC4.
- **S5** — Under the card cap. The cell is placed before the append measures the card against
  `CARD_CAP_BYTES` (`:216`, `:1183-1185`), so a cell that takes the card over its cap is refused by
  the cap the card already keeps. Observed by AC5.
- **S6** — The scout composes it. `tools/roles/agents/gov-orienter.agent.md`'s job gains the cell:
  run `gov_map.py` for level 0 and `gov_map.py <ns>` for the namespaces the neighbourhood needs,
  copy the header line verbatim, and write the five neighbourhood rows project-map.md:620 names;
  where the append reports the map not installed, compose none. `skills/session-kickoff/SKILL.md`'s
  Step 5 card list names the cell beside the six sections. Observed by AC6.

## 3. Non-goals (OUT)

- The renderer, its header and its budget: TOOL-dTotalRecall-14's `tools/memory-tree/gov_map.py`.
  This unit reads its first line's grammar and nothing it derives.
- Judging the neighbourhood's rows. The append checks the header and the cell's shape; whether the
  rows name the right layer, features and gaps is the scout's judgment, the composition the clause
  gives it.
- The work order's `map` slot and the roles `memory.project-map` names: TOOL-dFurnishedOrders-12. The
  card's cell is composed under every value of that key, because the card is the session's own and
  the owner's session gets the card and the map under each (project-map.md:616-632).
- The instruction map PLAY-dOrderedCharter-4 prints on replay, a different map with its own
  `map —` block.
- The scout's sidechain spawn: TOOL-dFurnishedOrders-1.
- The startup write (`--card --write`) spawns no resolver for the cell: the SessionStart hook keeps
  its cost, and the cell appears with the kickoff's append.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-1` — `gov-orienter`, the orientation scout spawned in a sidechain at session start, whose composed body carries this cell; without it the cell is the main loop's own text
- **consumes-from** external — TOOL-dTotalRecall-14's `gov_map.py` and its S5 header, specced and DEFERRED at base `2193e25d`; until it lands the cell renders not installed

## 4. Design

### The card, installed

```
live — LIVE.md · 4 non-terminal builds
project-map — map gov-main · nodes 1412 · lines 211 · folded code,record
  layer — Orders (dFurnishedOrders), after dBoundRoles
  chain — dFurnishedOrders · 20 clauses · 13 gaps
  features — roles, kickoff, runlog
  gaps — roles 11, orient 1, conc 1, mem 1
  overlaps — dKeptSession (skills/session-kickoff/manifest-check.sh)
claims — …
```

### The card, not installed

```
live — LIVE.md · 4 non-terminal builds
project-map — not installed: no gov_map.py in this tree (TOOL-dTotalRecall-14)
claims — …
```

The words `not installed` are the slot grammar's (shared interface J4's state), so a reader of the
card and a reader of a work order's slot see one spelling for one state.

### The append's order

`add_card_body` already checks citations, then the task, then the base, then the route, then
annotates, then rebuilds the startup with the `tree —` cell re-rendered, then measures the cap.
`check_card_map` runs after the route check and before the annotation, so a refusal leaves the card
untouched; the startup rebuild writes the cell after `live —`, and the cap is measured over the
result. A body with no READY line, the route-only append, carries no cell and is refused if it
does: one card holds one kickoff, as its READY rule already says (`:1147`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_card_map` | function, `manifest-check.sh` | `sh.function`, OK |
| `project-map —` | card cell head | none |

### Migration

Additive. A card appended before this unit carries no `project-map —` cell and reads as today; the
replay prints the stored card as it is.

### Rollout

Live at landing. `KIT_MANIFEST_VERSION` and `KIT_ROLES_VERSION` move with their kits' bytes for the
kit epoch leg. The engine's row in `tools/template-size-limits.txt` is raised only by the terms
TOOL-dFurnishedOrders-1 §8 F3 follows, if this unit's line takes the engine past it.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `skills/session-kickoff/SKILL.md`
- `tools/template-size-limits.txt`
- `memory/DECISIONS.md`
- `tools/roles/agents/gov-orienter.agent.md`, rendered to `.claude/agents/gov-orienter.md` and
  `.claude/roles.json`
- `help/roles.md`

### Alternatives rejected

- **The append rendering the cell itself from `gov_map.py`.** The neighbourhood is a judgment over
  the map, the composition the clause gives the scout; a script would print level 0 whole, which the
  card's 8 KB cannot hold beside the rest.
- **A `## map` body section.** The card's derived facts are cells; a body section is the scout's
  prose, and the map's header is a derived fact the append can check.

## 5. Production-readiness checklist

- security — no new write path: the card is written where it is written today; the cell's rows are
  the scout's text, cited, never executed.
- perf / scale — one resolver spawn per kickoff append; none at the SessionStart write.
- error / empty / loading states — not installed is a cell, never an absence; a malformed cell
  refuses the append naming the shape.
- observability — the cell's head names the map's tree and counts.
- risks — a cell whose rows are wrong passes the shape check; the header line is the part checked.
- testing — AC1 to AC6 by a pass over scratch adopters; the arm of §7 at the close.
- migration — additive.
- user docs — `help/roles.md`, step 1, names the cell beside the card's sections.

## 6. Acceptance criteria

- **AC1** — When `bash manifest-check.sh --card --append --session s1` runs in a scratch adopter
  holding no `gov_map.py`, with a READY body carrying no `project-map —` cell, it exits 0 and the
  stored card holds `project-map — not installed: no gov_map.py in this tree (TOOL-dTotalRecall-14)`
  on the line after its `live —` cell.
  Red when: the card carries no cell, so a map not installed reads as a map never composed.
  fixture: a scratch adopter under `%TEMP%` with the kickoff kit and a card written by `--card --write`.
- **AC2** — When the AC1 append's body carries a `project-map —` cell, it exits 1 naming the
  not-installed state, and the stored card is byte-identical to the one before the call.
  Red when: a cell composed from no map lands on the card.
- **AC3** — When the AC1 adopter tracks a stub `gov_map.py` under its memory-tree kit and the body
  carries `project-map — map t1 · nodes 3 · lines 3` with two indented rows, the stored card holds
  that head and both rows after its `live —` cell, and its tail below `recent —` holds no
  `project-map —` line.
  Red when: the cell stays in the body or loses its rows.
- **AC4** — When the AC3 adopter appends a READY body with no `project-map —` cell, and again with
  the head `project-map — level 0`, each exits 1 naming the expected head, and nothing is appended.
  Red when: a card lands with no map, or with a head off the grammar, where the map is installed.
- **AC5** — When the AC3 append runs with `CARD_CAP_BYTES` set to the card's bytes without the cell
  plus 10, it exits 2 with the `over the` cap line.
  Red when: the cell is placed after the cap is measured, so the card grows past its cap.
- **AC6** — When `grep -n 'gov_map.py' gov-orienter.agent.md` runs in `tools/roles/agents/` and
  `grep -n 'project-map' SKILL.md` in `skills/session-kickoff/`, each prints the line naming the
  cell.
  Red when: the scout is never told to compose the cell.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `policy fixtures` · `kickoff engine size <=18KiB` · `check-wiring self-test` · `roles catalogue` · `roles render wiring` · `roles adopter self-test` · `kit epoch (shipped bytes move, the version moves)` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC3 AC4 AC5 · READY bodies with and without a cell, appended with and without a stub `gov_map.py`, and one under a lowered cap · none

## 8. Open questions

- **F1 — The cell's head: J8's `map —`, or another spelling?** PLAY-dOrderedCharter-4 S4 prints a
  `map —` block, the instruction map, before the stored card on every replay, so J8's spelling puts
  two `map —` heads naming two different maps one above the other. Options: (a) `map —` as J8
  spells it; (b) `project-map —`. (b) satisfies every criterion (a) does and leaves no ambiguity for
  the reader of a replay. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, tie-broken by fewer
  open questions; J8's owner is this unit, so no sibling reads the old spelling. widens: none ·
  relaxes: none
- **F2 — What does the append check of a composed cell?** Options: (a) the header line against
  TOOL-dTotalRecall-14 S5's grammar and the cell's shape; (b) nothing, the scout's text trusted;
  (c) the append renders the cell from `gov_map.py` itself. (c) takes the composition from the scout,
  against the clause's wording; (a) satisfies AC4, which (b) fails. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — The renderer is DEFERRED.** TOOL-dTotalRecall-14 is dTotalRecall's, a build the packet names
  as a stand-in for this clause's family. RESOLVED (agent, 2026-10-26, delegated): this unit builds
  on base with the not-installed state live and the installed branch held to S5's header as specced;
  the build run re-grounds on TOOL-dTotalRecall-14 S5 and follows a respelled header if its spec
  moved, rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 13, the brief's J8, scout A's row for
  cl-0204, project-map.md's delivery table, and the source at `2193e25d`.

## 10. Reuse audit

The seam extended is the card pipeline in `skills/session-kickoff/manifest-check.sh`: the
`<cell> — <value>` form with indented rows of `derive_overlaps_line` (`:555`) and its `skipped:`
idiom, `add_card_body`'s startup rebuild that already re-renders `tree —` (`:1141`, `:1171-1172`),
its cap (`:216`) and the sibling resolver `resolve_kit_file` (`:854`). `python
tools/codebase-map/reuse_lookup.py "render one cell of the session orientation card from an optional
component or say it is not installed"` ranked `render_cards_md` and `render_map_md`
(`tools/codebase-map/map_lib.py`), which render the codebase map's dossiers, not the project map,
as scout A found and TOOL-dTotalRecall-14 §3 keeps apart; no seam renders a project map, so the cell
reads the later build's header and renders nothing itself. The recall probe returned
TOOL-dTotalRecall-14, scout A's row and project-map.md's delivery table; scout A's
`render_card` `:517` and its cell idiom `:520-531` agree with source, and its proposed
`map — not installed` spelling is the one §8 F1 moves.

Recall terms used: `python tools/memory-recall/query.py "how does the orientation card carry the
project map cell" --terms "card map cell project map level-0 neighbourhood orientation scout not
installed gov_map render_card cap"`
