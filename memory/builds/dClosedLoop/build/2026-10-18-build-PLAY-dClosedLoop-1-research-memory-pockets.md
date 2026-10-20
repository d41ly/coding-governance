# Research: the memory the repository holds, under one writing practice

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 106's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-9-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`.

---

1. **Verdict**

The repository holds 27 memory pockets. Only one family of typed links works end to end today: the `**Serves:**` field line, whose inverse a generator derives (`gen:spec-records`) and a check grades (check 21). It runs over 2,278 records. Outside dClosedLoop, no memory section carries a tag (0 tagged headings), and the guides cite by position (121 `§`, 72 "check N"). I recommend **H**: each section declares its own edges on one line under its heading, the way `**Serves:**` already declares them for the whole record. The other three candidates each lose a measured test. Tracing the `roles` feature, 7 of 12 hops are typed and 5 need prose or search. The closed edge set is missing four types: `serves`, `answers`, `reads`/`writes` and `promoted-from`. The atlas can derive kinds, owners and writers today. Homes, readers and lifecycles appear for 0 of the 70 kinds.

2. **Pockets**

The measuring scripts are `census.py`, `links.py`, `cands*.py`, `sidecar.py`, `ftest.py` and `htest.py`, under `…/scratchpad/away/d106/`. All of them only read. The record-kind list comes from `map.py --ns record-kind`: 70 kinds, every one with purpose `—` and an `owner=` (map.py:299-301).

| Pocket | Where | Writer → reader | Address | Count | Tagged heads / with an id / typed link | Maps to (kind · owner) or gap |
|---|---|---|---|---|---|---|
| Charter | `AGENTS.md`, `CLAUDE.md`, template | `render_playbook.py` → every session | `- [tag]` rules (45) | 2+1 | 0 of 9 heads tagged; 3 numbered (`## 1.`, AGENTS.md:12,84,98) | instruction L0, dOrderedCharter |
| Guides and protocols | `memory/guides/` (10), HYGIENE, TEMPLATE-SPEC, memory/README | by hand, plus `adopt-memory-tree.sh --render` → agents on trigger | path | 13 | 0 of 138 tagged; 56 numbered; 162 `§`, 115 "check N" | instruction L3, dConvergedCharter |
| Kickoff manifest | `memory/guides/SESSION-KICKOFF.md` (manifest-check.sh:64) | kickoff → card | path | 1 | — | **gap**: no kind and no unit |
| Role sources and renders | `tools/roles/agents/` (10), `.claude/agents/` (9), `roles.json` | `render_agents.py` → spawns | `name`; typed `reads:` `writes:` `rules:` (gov-researcher.agent.md:6-9) | 20 | `rules:` gated by `check_rule_tags` (roles_lib.py:252) | instruction L5, dBoundRoles |
| Skills and path rules | `.claude/skills/` (7), `.claude/rules/` (1) | render → harness | — | 8 | 0 tagged | instruction L4 |
| Handoffs | `builds/*/prompts/` | `handoff.py` → role | Serves plus `gov:handoff` marker | 595 | marker on **59 (9.9%)**, path==file 59/59 | work order, dBoundRoles |
| Build README | `builds/*/README.md` | `gen_build_index.py --new-build` → owner, scout | front matter | 167 | front matter 167/167; `ids:` agrees with defined ids 162/167 (5 miss `-1b/-1c` sub-ids) | build readme, dTotalRecall |
| Specs | `builds/*/spec/` | spec writer → builder | id; `**Status:**` line | 1,322 | 0 tagged; 13,131 numbered heads; `gen:spec-records` 1,317/1,322 | spec, dIndexedDesign |
| Build records | `builds/*/build/` | roles and commands → reviewers | Serves | 1,128 md + 94 non-md | 13% tagged, **all dClosedLoop** (672; 0 elsewhere) | design record, acceptance, probe… |
| Reviews | `builds/*/reviews/` | harness → fold | Serves | 552 | 0 tagged; 5,723 numbered | review, dFairHearing |
| Per-build asks | `builds/*/BACKLOG.md` | filer → triage | id rows | 126 | id 100% | ask / backlog row, dTotalRecall |
| Run records | `builds/*/RUN*.md` | unattended → owner | path | 98 | — | run record, dTendedCadence |
| Decisions | `memory/DECISIONS.md` | by hand → recall, dossiers | id per row | 200 rows | id 200/200 defined; detail paths 32/32 resolve; relation word on **1**; feature edge **0** | decision, dLinkedLibrary |
| Ask views | `memory/backlog/*.md` | generated | id | 4 | derived | **gap**: views have no kind row |
| Gotchas | `memory/gotchas/` | by hand → builders | front matter `name` | 149 | front matter 148; `from:` **0**; `decision:` 3 | gotcha, dLinkedLibrary |
| Dossiers | `memory/map/features/` | by hand → reuse scout | `feature =` | 31 | claims gated 120/120; 72 decision ids, all defined, 15 of them log rows; 14 empty | dossier, dTotalRecall |
| Map generated | `memory/map/generated/` (MAP, CARDS, symbols.json, inventories.json) | `gen_map.py` | — | 4 | derived | code record / views |
| LIVE and ledger | `memory/LIVE.md`, `memory/ledger/` | `gen_build_index --write` | build links | 1+4 | derived | **gap**: view, no kind |
| Project registries | `memory/project/*.txt` (20) | gates' `--emit-pin` → gates | path-keyed rows | 20 | 872 path rows, 78 not tracked (most are deliberate fixture or "does not exist" reasons) | **gap**: no kind ("waivers → row registries", layer-memory.md:664) |
| Archive | `memory/archive/` | rotation | — | 18 | — | **gap**: rotation, no kind |
| Lexicon | `tools/lexicon/LEXICON.md`, `.lexicon.conf` | by hand | — | 2 | — | lexicon declaration, dMindYourWords |
| Recall index | git common dir (`query.py:291`) | derived | — | — | derived | recall index, dLinkedLibrary |
| Instruments | `.py/.tsv/.html/.svg` in `build/` | researchers | — | 94 | 3 `.tsv` carry no Serves (check 21 "A") | **gap**: no kind |
| help/ | `help/` | by hand → users | — | 2 | — | outside every load set |

The table spells guide counts from `census.py`. Its "§" and "Mn" columns are regex upper bounds.

**Where records and code disagree:**
- `check-playbook-parity.sh:14` says the charter has no numbered sections, but `AGENTS.md:12` has `## 1.` and `roles_lib.py:61` requires it.
- The `DOSSIER_DECISIONS_EMPTY_PIN=16` in layer-memory.md:655 does not match the tree, which has 14 empty `decisions = []`.
- **The design build fails the one typed-record check that exists.** `gen_build_index.py --print-bindings` gives `215 B` and `3 A` rows, all in dClosedLoop: "PLAY-dClosedLoop-1 is named but no spec H1 in this tree defines it" (check-memory-hygiene.sh:1411-1414).
- "journal" names two things: a Serves kind (1,436 records) and Runtime's journal kind (layer-memory.md:440).

3. **One writing practice**

**The shared grammar** (systems `[design-tags]`, research-relational-syntax.md:103-128):
- **Node:** a tag, or `<doc> [<seg>]`.
- **Edge:** `type=target[,target]`, with the type drawn from one closed set.
- **Level:** belongs to instruction units (0–6). Memory is level 7 by kind and is never levelled per section (P13, P30).

**What makes a record section a node:**
- a unique `## [tag]` heading, or a derived anchor for a legacy heading;
- its record's kind, from the record's header (today's `**Serves:**`);
- one edge line for the facts the section owns (`owner`, `decides`, `supersedes`, `amends`, `serves`).

**What stays prose:** the evidence (measurements, output, the owner's verbatim words, reasoning). It is data, not a loaded instruction (P11 governs loaded units). Sections are a median 1,382 B, and 21.7% hold a table or a code fence. Inverses and `cites` are derived.

| | U: section = instruction-shaped unit row | **H: edge line under the heading (pick)** | F: front matter keyed by section | S: sidecar per record | Q: derive only |
|---|---|---|---|---|---|
| Syntax | TOML row `tag, kind, text, edges`, rendered to md | `## [design] …` then `**Edges:** decides=feature.roles owner=dTotalRecall` | `---\nedges: {design: {decides: […]}}\n---` | `<record>.edges.toml` | none; `cites` from text |
| Seam it extends | instruction R-A | `**Serves:**`, `**Commissions:**`, `**Status:**` field lines plus the `gen:spec-records` derived inverse (gen_build_index.py:145) | README and gotcha front matter | dossier `decisions` list, `memory/project` rows | recall FTS |
| Enforcement | `record` renders; render parity | `record` writes the line; generated checks: type registered, target resolves, inverse rendered (check 21 generalized) | front-matter schema; section keys resolve | freshness check | none |
| Migration (legacy left as is past the cutoff, layer-memory.md:358) | 14,405 sections to convert, or two systems forever | 0 rewrites; 2,278 Serves and 16 Commissions lines become `serves` edges mechanically | 0 rewrites | 0 rewrites; new hot files | 0 |
| **Losing test** | ≥50% of sections fit a 200 B unit | the inline edge line parses and resolves tree-wide, and fits one line | edges are record-level, so a top block stays at its fact | an edge list kept apart from its declaring rows stays complete | an inferred type is ≥50% precise |
| **Result** | **Loses.** 7.3% ≤200 B; median 1,382 B; p90 3,214 B | **Passes.** Serves: 5,219 ids, 96.0% defined; the 4.0% are all dClosedLoop's design-only id, which the check caught. Upper-bound edge line: median 40 B, p90 204 B, 10.1% over 200 B (one line per type covers those) | **Loses.** 43 of 45 multi-section dClosedLoop records cite different chain builds per section, so F becomes a section-keyed table away from its fact. Its rename-stranding risk measured 0 of 15 heading edits | **Loses.** Dossier lists hold 16 of 120 log rows from their own builds (upper bound; 12 of 31 dossiers omit some), and `roles` omits both its log rows (DECISIONS.md:12,138) | **Loses.** A bare-name search is 36% precise; 33% of `[tag]` citations are ambiguous (dispatch 103). Q survives only as derived `cites` |

**Today's practice:**
- Instruction text follows the one-line rule only inside the charter's one-line regions: `ONE_LINE_MAX = 200`, render_playbook.py:121-126.
- P11's statement types are checked nowhere except the micro-formats (`check-microformats.sh`).
- Memory follows neither rule.

4. **The cycle**

The trace runs on `roles` (memory/map/features/roles.md):

| Hop | Today | Typed? | P33 type |
|---|---|---|---|
| charter `[roles]` (AGENTS.md:46) → feature | same word, no join | **prose** | `instructs` (needs the `feature.*` selector) |
| feature → code | `[claims] kits` via `compute_coverage` | typed, gated | `part-of` |
| code → feature | derived inverse per kit; `gov:feature` lines: 0 | typed (kit level) | `implements` |
| code → decision | 19 distinct ids cited in `tools/roles` | typed by grammar; resolve is report-only | `cites` (derived) |
| feature → decision | `decisions = [11]`, 11/11 defined, 0 log rows | typed, incomplete | `decides` inverse |
| decision row → feature | none (0/200 rows) | **search** | `decides` |
| decision id → spec | the id grammar (`grammar_for`) | typed | node identity |
| spec ↔ records and handoffs | Serves, with the inverse in `gen:spec-records` | typed, gated both ways | **missing: `serves`** |
| handoff → role | `gov:handoff role=`, 9 of 38 aOrientedCast prompts | partly typed | **missing: `reads`/`writes`** (item/role ↔ kind) |
| role → charter rules | `rules:`, gated | typed | `instructs` inverse |
| return → its handoff | prose in 58 of 88 research records | **prose** | **missing: `answers`** |
| memory → instruction (promotion, P30) | no route (`gap-found-14`) | **none** | **missing: `promoted-from`** |

Of the 12 hops, 7 are typed (4 gated) and 5 need prose or search. P33's set closes instruction→code (`instructs`, `part-of`, `implements`, `tests`) and code→decision (`decides`). It cannot express a record serving a unit, a return answering a work order, item/kind read and write, or promotion. Commits and session ids belong to the other two researchers.

5. **The memory view**

**What the owner needs to see:**
- **Nodes:** the 70 record kinds, plus the gap pockets above.
- **Families:** trail (witnesses, transitions, card); library (decision, gotcha, reuse entry, research); optional components (dossier, owner views, recall, lexicon); generated views; the level-7→level-3 promotion boundary.
- **Typed edges between kinds,** from the closed set.
- **Owner per kind** (chain build colour); **writer** item and **reader** items or roles; **home** (path or ref); **lifecycle.**
- **A cycle overlay:** the hops above, each marked typed, gated or prose, with the measured counts.
- **A pocket overlay:** today's count and link coverage per pocket.

**What it can derive today, or must have declared:**

| Datum | Derivable now? | Source |
|---|---|---|
| kinds, owners | yes, 70/70 | layer-memory.md:395-466, already parsed (map.py:299) |
| writer | 37/70 | "its writer is `x.y`" |
| core / optional family | yes | `[contract]` lists, layer-memory.md:369-386 |
| edge types and their from→to namespaces | yes | research-relational-syntax.md:115-126 |
| library fill points | yes | atlas `libraryPaths` already |
| pocket counts and coverage | yes, from the tree | census as above |
| home, readers, lifecycle, layer per kind | **0/70** | must be declared in the registry first (P30) |

Today the atlas shows memory only as one layer node and an inspector panel (atlas.html:660-663, 788-836). It has no kind graph (`V2_VIEWS`, atlas.py:117).

6. **Chain, gaps and forks**

**Units to add, by build:**

| Build | Unit |
|---|---|
| dClosedLoop (now) | an atlas **Memory** view: kinds by family, owners and writers, the closed-set edges, and the cycle and pocket overlays, derived as above; the render parity check against `map.py` (project-map.md:686) |
| dOrderedCharter | one edge-line grammar shared by instruction units, `gov:note` and record sections; add `serves`, `answers`, `reads`/`writes` and `promoted-from` to the closed set |
| dTotalRecall | registry rows gain home, lifecycle, readers and layer; `record` writes the header and edge lines; check 21 generalized into the edge extractor (Serves→`serves`, Commissions); the `gen:spec-records` inverse becomes the derived-inverse factory; view kinds (LIVE, ledger, ask views, research view); kinds for registries, archive and instruments; the kickoff manifest mapped |
| dLinkedLibrary | `decides=` on log rows; gotcha `from:` (0/149 today); dossier `decisions` derived from rows |
| dBoundRoles | every handoff carries the marker (59/595 today); role `reads:`/`writes:` become edges; return→work-order `answers` |
| dConvergedCharter | the guides' positional references (162 `§`, 115 "check N", 56 numbered heads) to tags |

**Gaps to register:**
1. Design-only builds fail check 21 (218 rows).
2. "journal" names two kinds.
3. Views, registries, archive and instruments have no kind.
4. P30's per-kind fields are undeclared (home, readers, lifecycle 0/70).
5. The closed set lacks four types.
6. Handoff markers sit on 9.9% of handoffs.
7. No promotion route (extends `gap-found-14`).

**Owner's forks:**

| Fork | Options, recommendation first |
|---|---|
| MW-1 Section edge syntax | H, an edge line under the heading; F, front matter keyed by section; S, a sidecar |
| MW-2 Closed-set growth | add `serves`, `answers`, `reads`/`writes`, `promoted-from`; or widen `part-of` and `cites` to carry them |
| MW-3 Legacy records | derived anchors plus a mechanical Serves→`serves` backfill, no rewrite; or derived anchors only; or a full retag |
| MW-4 Design-only build ids | the README `ids:` defines the unit node; or exempt design builds from check 21 |
| MW-5 Memory view source | derive it from the registry and records now, filling it in as fields are declared; or a hand-drawn diagram until dTotalRecall |

Nothing in the repository was written. The probes are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d106/`.
