# Research: the level-0 project map, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 88's return, verbatim. Its question is in
`prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-2-researcher.md`, which dispatch 87 runs too, and its use is in
`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`.

---

I wrote nothing to the repository. All scripts ran from the session scratchpad, and `git status --porcelain` printed 0 before and after the generator timings.

## 1. Verdict

The pick is a **two-tier project map that core memory derives from the one index** (dTotalRecall, kit memory-tree).
- **Tier 0** gives every structural node one line: tag, declared purpose of at most 60 characters, counts and up to three relation keys. Each large population folds into a group line that carries its count and the verb that drills into it. Today that is 173 lines and 13.2 KB.
- **Tier 1** is `gov map <ns>`: one namespace, one line per node.
- **Drill-down** uses `gov tag show`, and relations use `gov tag refs` and `where`, both already designed.
- **"No piece lost"** is a closure check in both directions: every index node is either a line on the map or counted in a group line.
- **Renders:** the map goes into the work orders of the roles PM-1 names, and the atlas is the owner's render of the same derivation.
- **Losing test:** a replay of past reviews, with the map handed and without, scored on the share of findings "not in view".

## 2. Today

| Part | What it does | Measured | Where |
|---|---|---|---|
| Codebase map: `MAP.md` and `CARDS.md` | inventory keys with their claimant, and one card per feature capped at 1,024 B | 19,728 B and 22,363 B; 31 cards; `--check` takes 5.6 s | `tools/codebase-map/gen_map.py:137-152`, `map_lib.py:1666`, `:1715` |
| Who reads them | no agent | a grep of skills/, .claude/, tools/hooks/, tools/roles/, AGENTS.md and the charter template returns nothing | — |
| Build index | renders `LIVE.md` and the README regions from five sources | `--check` takes 4.6 s and reports "clean (1493 artifact(s))"; LIVE.md is 4,079 B with 25 live builds | `tools/memory-tree/gen_build_index.py:1-40`, `:847` |
| Atlas | a whole-design view for the owner | `--check` takes 309 ms: 133 records, 2,317 sections, 160 decision sections. It reads 7 records of one build and none of the tree's populations (0 hits for gate-legs, kit.toml, gotchas, features or LIVE) | `atlas.py:1-16`, `:38-46` |
| Session card | where an agent orients today | 21 cards: median 3,599 B, max 7,777 B, against an 8 KB budget | `.git/orientation/*.md` |
| Work order fields | what a role is handed | `title goal in out todo reuse acceptance gates`; there is no map field | `tools/roles/handoff.py:97` |
| Orientation scout | per PM-1, it composes the card | `gov-orienter.agent.md:8,11` exists, but none of the 3,283 typed subagent meta files is a gov-orienter spawn | meta.json `agentType` counts |
| Design: views | PM-1 now allows one view, the map, to reach agents | — | layer-memory `:741-750` |
| Design: index and verbs | one JSON file per tree, plus `tag show/where/refs`, `record find/show` | not built: no `gov tag` exists in tools/ | systems `:177-196`, `:245-247`, `:462-466` |

**Node census.** This counts every class, one line per node at a 90-character purpose. The script is `census.py` in the scratchpad.

| Class | Nodes | Bytes | Where a purpose is declared today |
|---|---|---|---|
| layer | 8 | 910 | v2 `[layers]` definition column |
| principle | 30 | 1,717 | the bold title in v2 |
| chain build | 15 | 1,238 | **only a stage word** in v2 `[chain]` |
| build, live / closed | 25 / 142 | 3,066 / 17,206 | the README H1 after the slug (167 of 167 have one), but no declared field |
| feature | 31 | 3,496 | the dossier's toml `title` |
| kit | 19 | 1,397 | **none**: kit.toml has no purpose field, and govkit and lib have no kit.toml |
| gate leg | 140 | 5,167 | **name only**: gate-legs.json keys are name, argv, chunk, subject, ceiling, guard, reads, doc_reads, signature |
| harness and git hooks | 13 + 4 | 1,135 | **none** |
| skill | 7 | 531 | SKILL.md `description` |
| role (today) | 10 | 673 | agent.md `description` |
| workflow script | 15 | 483 | **none** |
| bug class | 139 | 19,941 | gotcha `description` |
| guide | 10 | 787 | H1 only |
| decision row | 200 | 24,826 | the row text; the major class is not yet routed |
| policy namespace | 50 | 1,334 | **none** per namespace; each key has a "why" |
| gap area | 17 | 377 | **none** per area; each gap has its row text |
| item | 81 | 9,061 | the flow-steps `does` column |
| design record (dClosedLoop) | 101 | 9,928 | H1 only |
| **all** | **1,057** | **103,273** | |

Three classes are designed but not yet derivable: record kinds (about 37, layer-memory `:366-376`), tag namespaces (25, systems `:229-231`) and extension points (10). None has a purpose field.

**What the PM-1 roles read before their first act.** The script is `tx.py` over 3,534 or more subagent transcripts. Read-only roles count the whole run; writers count up to their first Write or Edit.

| Role | n | median KB | p90 KB | reads | distinct files | searches | existence searches | share of calls |
|---|---|---|---|---|---|---|---|---|
| coherence lens | 110 | 162.0 | 365.7 | 27 | 21 | 15 | 3 | 9.2% |
| reuse lens | 48 | 197.1 | 490.4 | 45 | 32 | 24 | 5 | 10.4% |
| spec writer | 76 | 149.9 | 373.3 | 16 | 14 | 10 | 2 | 12.0% |
| spec reviewer | 95 | 143.1 | 253.8 | 32 | 24 | 24 | 5 | 14.2% |
| Plan agent | 18 | 98.3 | 142.7 | 12 | 8 | 9 | 1 | 5.7% |
| builder (control) | 38 | 167.7 | 352.4 | 18 | 12 | 10 | 3 | 12.1% |

Per call in these roles, a Read returns 2,688 B median and 5,624 B mean, and a search 827 B median and 1,587 B mean (`per_call.py`).

**The second rater.** I sorted every item by the record's four causes.

| Report | Not in view (rows 1–3) | Breakdown (rows 1/2/3/4) |
|---|---|---|
| library (`reviews/2026-10-16-…-library.md`, 19 items) | 14 (74%) | 5/9/0/5 |
| debt-folds (`reviews/2026-10-17-…-debt-folds.md`, 20 items) | 17 (85%) | 7/7/3/3 |
| systems-retrofit, re-rated (52) | 39 (75%), against the record's 37 (71%) | agree on 50 of 52, kappa 0.90 |

- **Where I disagreed.** On M13 (`resolve_compare_base` already exists) and M32 (layer-expansions' grant rules already exist), I sorted the item as "not in view" where the record sorts it "missing".
- **This rating was not blind.** I had read `[sort]` before rating the 52. The library and debt-folds sorts had no prior sort to follow.
- **Across all three reports,** 70 of 91 items (77%) are "not in view".
- **What tier 0 or tier 1 would have named.** Of the systems audit's 20 row-1 items, about 13 miss a node that tier 0 or tier 1 holds: hygiene check 3, `workflows.toml`, the legs, the renderers, `tools/lib`, the `gov:` markers, `help/`, the merge driver. Three miss a symbol (M14, M19, M21), which is code depth. Four miss detail inside a record (H3, M15, M35, L6). That sets the map's ceiling at about 13 of 20.

**Growth.** From git history and README `opened:` dates:

| Class | Count over time | Rate |
|---|---|---|
| builds | 12, 72, 47, 36 opened per month (Jul to Oct 17) | about 45 a month |
| legs | 17 (Aug 1), 86 (Sep 1), 123 (Oct 1), 140 | about 30 to 48 a month |
| decisions | 0, 92, 181, 200 at the same dates, after a rotation of 79 rows | about 50 to 60 a month |
| bug classes | — | about 50 a month |
| features | — | 4 to 9 a month |
| kits | — | about 2 a month |

- **Flat:** about 21 KB a month.
- **Tier 0:** only the structural classes grow, at about 0.7 KB a month. That is 16 KB in about 4 months at 60-character purposes, or about 6 months at 40.

**What one derivation costs.** gen_map 5.6 s, gen_build_index 4.6 s, atlas 0.31 s. The map is a projection of the index plus a fold, so it should cost about the atlas's 0.3 s once the index is warm. The index rebuild on a miss is what dominates.

## 3. Across the layers

| Layer | What the map needs from it | What the map gives it |
|---|---|---|
| instruction | the statement type "derived fact", P11; work-order render at level 6; one renderer | the `doc` and `unit` nodes; a load unit that P27 can budget |
| flow | items declared as data, with `does` as their purpose | the map slot for the Plan and Design items and for `review.lens` (coherence, reuse); the `map` legs at Test |
| roles | the work-order renderer, which reads `memory.project-map`; role purposes | fewer existence searches for the structural roles |
| memory | the one index, the record-kind registry, `record find/show` | the map view, `gov map`, the closure check, record kinds as nodes |
| runtime | the extension-point registry and hook packs with a purpose; the journal, to count reads outside the slice | points, hooks and commands as nodes |
| observability | the journal-reader point | the Loop Review reads the map's bytes against the not-in-view share |
| integrations | adapters registered under their own prefix | an absent expansion's line renders "not installed" (the optional slot's three states) |
| distribution | kit.toml `purpose`; per-tree derivation in the adopter | kits as nodes; the adopter's map at adoption |

| System | What the map needs from it | What the map gives it |
|---|---|---|
| tags | a namespace registry row with `purpose` and `map: line|fold`, and the resolver | a population for the "resolves" and "joins" checks |
| code annotations | `gov:feature` anchors | anchor counts per feature; the annotation rows stay behind `refs` |
| instruction writing | purposes authored through `instructions.edit` | a map line is a derived fact, never authored |
| role workflow shapes | each shape's items declare the slot | shapes as nodes |
| memory structure | its own slot and its own key, which avoids M1's three answers | a slot priced outside `memory.item-budget` |
| retrofit | the ledger factory | nodes without a purpose become a shrink-only population |

## 4. Candidates

| | Mechanism | Efficiency | Losing test | Result |
|---|---|---|---|---|
| **A. Flat map** | every node of every namespace, one line each, handed whole | 96.3 KB at 90 characters, 81.2 KB at 60, 30.7 KB tags only; grows about 21 KB a month | loses if it exceeds the 8 KB card budget (`memory.load-budget`) or a 16 KB slot | **Rejected.** `tiers.py` prints `flat, all 1057 nodes, purpose<=60: 81191 B`, five times a 16 KB slot, and still 30.7 KB with tags alone |
| **B. Two tiers from the index (pick)** | tier 0: structural nodes one line each, large populations folded to counted group lines; tier 1 is `gov map <ns>` | 173 lines, 13,234 B at 60 characters, 6,127 B tags only. That is 2.3 mean Reads or 8 mean searches; break-even is about 2 to 3 reads averted per spawn, out of the 12 to 45 reads these roles make before their first act | loses if a node is in neither a line nor a group count, or if tier 0 exceeds 16 KB | **Passes on today's sources.** `tier 0, purpose<=60: 173 lines 13234 B; structural lines 155`. The group lines carry legs 140, classes 139, closed builds 142, decisions 200, items 81 and records 101, which with the 155 structural lines account for all 1,057. Fails 8 KB unless tags-only |
| **C. Query only** | no map: `gov tag where/refs`, `record find` (at most 40 rows) | 0 B up front; 2 to 5 existence searches per structural agent today, 9 to 14% of calls | loses if the not-in-view share under query and grep stays high | **Loses** on the audit evidence: 70 of 91 (77%) under today's query-and-grep regime. It stays as the control arm of B's replay |
| **D. Extend an existing generator (the seam)** | D1 grows the codebase map's MAP.md and CARDS.md; D2 promotes the atlas to the source | D1 is already 42 KB for code alone; D2 takes 0.31 s | D1 loses if it cannot exist without the optional kit (PM-2, P28); D2 loses if it cannot see the tree's populations | **Both rejected.** D1: `gen_map.py:12` and `:34-36` need a filled `map_extractors` and `reuse_lookup`, `kit.toml` has `requires = ["memory-tree"]`, and MAP.md holds 0 design nodes. D2: `atlas.py:38-46` reads 7 records of one build, and the source grep returned 0. The atlas is kept as the owner's render |

The commands, in brief:

```
$ python census.py            -> all 1057 nodes 103273 B
$ python tiers.py census.py   -> flat purpose<=0/40/60/90: 30746/68042/81191/96279 B
                                 tier 0 purpose<=0/30/40/60: 6127/10613/11665/13234 B (173 lines)
$ python tx.py                -> the role table above
$ python per_call.py          -> read median 2688 B / mean 5624; search 827 / 1587
```

## 5. The pick, specified

**Owner.** The memory layer, kit memory-tree, chain build **dTotalRecall**. Each namespace's `purpose` field is owned by the build that registers it (systems `:266-273`). dBoundRoles renders the slot.

**Line grammar:**
```
line   := <tag> SP <purpose> (" · " <count>)* (" · " <rel>)?
count  := <ns> "=" <int>                       e.g. items=12  gaps=21
rel    := ("layer"|"after"|"owner"|"implements") "=" <tag>("," <tag>)*   at most 3 keys
group  := <ns> ".* " <int> " by " <facet> ": " (<k> ":" <int> SP)+ "→ gov map " <ns>
header := "map " <tree-id> " nodes=" <N> " lines=" <L> " folded=" <ns>("," <ns>)*
```

- **Purpose:** the node's registered `purpose` field, cut at `memory.map-purpose`. A node without one renders `—`.
- **What the map never holds:** section content; typed figures or status words (only statuses the index derives); dates; render provenance; anything the index lacks; prose.

**Tiers and growth.**
- **Order:** namespaces render in a declared priority order: layer, principle, chain, step, role, feature, kit, live build, point, record kind, tag namespace, policy namespace, gap area.
- **Folding:** a registry row marked `map: fold`, or a population over 40, renders as group lines.
- **Over budget,** tier 0 degrades in a fixed order and reports each step: purposes drop to 40 characters, then lowest-priority namespaces drop to tags only, then they fold. A node is never dropped.
- **Tier 1** is `gov map <ns>[.<seg>]`: the same grammar, one namespace.
- **Tier 2** is `gov tag show`, for content.
- **Relations:** `gov tag refs` gives inbound edges, and the line's own keys give outbound ones.

**Delivery** (`memory.project-map=structural-roles`):

| Reader | What it receives |
|---|---|
| orientation scout (`entry.orient`) | tier 0 whole. It composes the card's `map` cell from it: the header, plus the build's neighbourhood (its layer, chain build, features, the live builds that overlap it), within the 8 KB card |
| planner, architect, spec writer, coherence and reuse lenses | tier 0 as a work-order field `map`, beside `reuse` (`handoff.py:97`), hashed with the work order |
| builder, tester, other unit workers | no map; their slice and `refs`. A `gov map` read is journaled as outside the slice |

**Records and kits.** The `map` kind is generated: its writer is the generator, and its check is a re-render (layer-memory `:345-348`). It is never committed. It is cached beside the index at `<git-common-dir>/gov/index/<tree>.map`.

**Checks** (the `map` leg pack):

| Check | Red on |
|---|---|
| closure, forward | a planted index node absent from every line and group count, or a group count one off |
| resolves, backward | a line naming `feature.ghost`, or a relation key whose target does not resolve |
| purpose declared | a new kit.toml with no `purpose`; today's purpose-less nodes are a shrink-only ledger population (gap below) |
| budget | under `refuse`, a planted 17 KB tier 0; under `degrade`, a degraded render whose report lacks the step |
| freshness | a work order whose map tree id is not the served index's, outside dirty rows |
| delivery (P27) | a structural role's work order without the slot, or a builder's work order with it |
| populated | fewer than the registered namespaces present: "unarmed", never green |

**Read-path cost.**
- **Structural spawn:** +13.2 KB (about 3.3k tokens), against a 98 to 197 KB median pre-act read. That is 7 to 13%.
- **Unit worker:** 0 B.
- **Card:** at most 4.4 KB of headroom, which the neighbourhood slice fits.

**Losing test** (the build must run it; I have not built it):
- **Known set:** the not-in-view items of the systems-retrofit, library and debt-folds audits.
- **Method:** at each audit's base commit, run the coherence and reuse lenses 2× with tier 0 and 2× without. Score with `tools/workflows/review_replay.py`, deduplicated per known defect, as dFairHearing's M13 fix requires.
- **The map loses** if any of these holds:
  - recall of the known set rises by less than the difference between the twin runs, plus 5 items;
  - median existence searches per lens do not fall by 1 or more;
  - pre-act bytes rise by more than 13 KB.
- **After landing:** the not-in-view share of later audits, the 77% baseline, must fall in the Loop Review's 30-day window. If it does not, the map is retired.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `entry.orient` (fills) | orientation scout | composes the card's `map` cell from tier 0 | the card's map cell tree id equals the index's | unchanged |
| `plan.triage-judge`, `plan.reason`, `design.inventory`, `design.decompose`, `design.reason`, `design.seams`, `design.unit-spec`, `review.lens` (coherence, reuse), `review.fold` (fill) | their role | receive `map` in the work order | the slice manifest lists `map@<tree>` with its bytes | over budget: as `memory.map-overflow` says |
| `test.select` (fills) | command | selects the `map` leg pack when the index or a registry row changes | the verdict | normal |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `memory.project-map` | structural-roles, every-role, owner-only | structural-roles | PM-1 |
| `memory.map-budget` | 8k, 16k, 32k | 16k | measured 13.2 KB at 60 characters; 8k forces tags only (6.1 KB) |
| `memory.map-purpose` | 40, 60, 90 | 60 | 11.7, 13.2 and 15.1 KB (the last estimated) |
| `memory.map-overflow` | degrade, refuse | degrade | the map is useful only while it covers every node; degrading in order keeps that. Refuse is offered for strict |

## 7. Gaps

It partly closes:
- **gap-orient-04,** exploratory orientation: existence searches are 9 to 14% of calls.
- **gap-mem-05,** routing by purpose: tier 0 routes by purpose across builds.

It depends on gap-mem-20 (the index) and gap-found-21 (untagged populations). Its closure check cannot arm over an untagged population.

New gaps to register:

| Proposed id | Gap | Evidence |
|---|---|---|
| gap-mem-26 | No whole-project view reaches a structural role, and the two views that exist are read by none | not in view: 37 of 52 (the record), 14 of 19 and 17 of 20 (this rating); a grep for readers of MAP.md and CARDS.md returns nothing |
| gap-mem-27 | Nodes carry no declared purpose | kits 19, hooks 17, workflow scripts 15, chain builds 15 (a stage word only), policy namespaces 50, gap areas 17, tag namespaces 25, record kinds (designed), with legs carrying a name only |
| gap-orient-15 | The orientation scout PM-1 relies on is never spawned | 0 gov-orienter among 3,283 typed subagent meta files |

**Where the records and the code disagree:**
- The handoff says Runtime declares nine extension points; layer-runtime `:894` says "the ten", and layer-expansions `:135` adds the tenth, cadence items.
- The charter's Kinds fact says every kit has a kit.toml; there are 17 kit.toml files against MAP.md's 19 kits, since govkit and lib have none.
- The atlas has grown since the project-map record cited it: 133, 2,317 and 160, against 132, 2,307 and 157.
- MAP.md lists 12 harness hooks; `.claude/settings.json` holds 13 hook commands.

## 8. Forks

| Fork | Options, the recommendation first |
|---|---|
| PM-4, the budget for tier 0 | 16k with purposes at 60 characters; 8k with tags only; 32k |
| PM-5, what the card carries | the build's neighbourhood slice of tier 0 within 8 KB; the header line only |
| PM-6, purpose-less nodes today | render `—` and hold them as a shrink-only ledger population that each registering build drains; refuse the render until every purpose is declared, which blocks dTotalRecall on six builds |
| PM-7, when the replay runs | at dTotalRecall's first unit, with a map derived from today's sources as `tiers.py` does, so a losing map is never built; after landing only |

The measuring scripts are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/`:
- `census.py`
- `tiers.py`
- `tx.py`
- `per_call.py`
