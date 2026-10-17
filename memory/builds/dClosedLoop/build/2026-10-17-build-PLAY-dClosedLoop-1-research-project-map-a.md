# Research: the level-0 project map, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 87's return, verbatim, except that its title line is demoted to keep one H1 per
record. Its question is in
`prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-2-researcher.md`, which dispatch 88 runs too, and its use is in
`build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`. The return's own title calls it run B: neither run knew its letter, and the
letters follow the order the two were dispatched, so this is run A.

---

**The level-0 project map: research return, run B**

## 1. Verdict

I recommend **Candidate B, a tiered map that folds to fit, with per-item unfolds.** Core memory derives it from the one index, with no stored file. Each node of a bounded namespace (layers, principles, chain, live builds, features, kits, roles, hooks, policy namespaces, gap areas, major decisions) gets one line: its tag, a purpose of at most 60 characters, its counts and its relation keys (`layer=`, `owner=`, `after=`). Each unbounded namespace (legs, classes, decisions, gaps, config keys, populations, markers, records) gets one line holding its count and the drill verb.

- **Size.** The base map is 13.7 KB today, and about 19 KB with the designed namespaces, under `memory.map-budget=24k`.
- **Unfolds.** An item can declare a namespace's roll call. The architect's unfold costs 12.3 KB more.
- **Check.** One both-ways check joins the disk census, the index and the map.
- **Owner's view.** The atlas becomes the owner's render of the same node table.

## 2. Today

| Part | What it does | Measured | Where |
|---|---|---|---|
| Codebase map `MAP.md` | inventory of 11 populations, each with its claimant | 19.7 KB; 140 legs, 19 kits, 4 git hooks, 12 harness hooks, 139 gotcha classes… | `memory/map/generated/MAP.md:7`, `tools/codebase-map/map_extractors.py:408-418` |
| `CARDS.md` | one card per feature, at most 1 KB each | 22.4 KB, 31 features | `CARDS.md:5` |
| Readers of either file | no charter, skill, hook or guide names them; agents read them by hand | 344 reads (83 of CARDS, 261 of MAP) across 3,776 transcripts | `git grep` lists only the kit's own files and `memory/map/README.md` |
| `gen_build_index.py` | renders `LIVE.md` and the README regions from 5 sources | `--check` 4.40 s, 1,493 artifacts | `tools/memory-tree/gen_build_index.py:1-30` |
| Atlas generator | derives the whole design for the owner, with refusals when a population drops | `--check` 0.28 s: 133 records, 2,317 sections, 160 decision sections | `…-atlas.py:1-16`, `:270` |
| `gen_map.py --check` | byte-compares the map | 5.07 s | `tools/codebase-map/gen_map.py:1-12` |
| Design: `[views]` as revised | only the map is handed to agents (PM-1) | — | layer-memory `:744-750` |
| Design: the one index and its verbs | `show`, `where`, `refs`; `record find` returns at most 40 rows | not built | systems `:177-195`, `:462-466` |
| `compute_coverage` | the one both-ways join; systems moves it to `tools/lib` | — | `tools/codebase-map/map_lib.py:1404` |

**Where the records and the code disagree:**
- **The codebase map is installed by default.** It is in govkit's default selection (`tools/govkit/registry.toml:42`). Its README calls it "An opt-in kit" (`tools/codebase-map/README.md:3`), and the design calls it optional.
- **Two kit directories have no descriptor.** 17 of the 19 `tools/` directories hold a `kit.toml`; `govkit/` and `lib/` do not, against the charter's "Kinds" fact.
- **A build's purpose is declared.** `[probe]` says it has none. In fact all 167 build READMEs declare one in their H1, `# <slug> — <purpose>`. `LIVE.md` is simply the wrong source.

**Node census.** The full table is in §4, from `pm2_census.py`. Purpose is declared for 100% of layers, principles, chain builds, builds, features, roles, skills, guides, classes and policy keys. It is declared for **0%** of kits (19), legs (140), hooks (17), config keys (141), populations (23), items (81, which are designed) and design records (101). Neither the record-kind registry schema nor the namespace row (systems `:229-232`) has a purpose field. DECISIONS.md has no major or minor flag: 59 rows are bold, and gap-mem-02 counts 28 major.

**What structural roles read before their first act** (`python pm2/orient6.py`, all 3,711 subagent transcripts, medians):

| Role | n | calls | reads | files | KB returned | existence probes, median and share of calls |
|---|---|---|---|---|---|---|
| researcher | 58 | 48 | 37 | 30 | 162.5 | 11 (25.2%) |
| spec writer | 76 | 20.5 | 16.5 | 13.5 | 149.2 | 2 (12.6%) |
| spec reviewer | 95 | 39 | 32 | 34 | 142.6 | 6 (15.4%) |
| prior-art lens | 49 | 51 | 45 | 36 | 240.6 | 5 (10.6%) |
| contradiction lens | 49 | 37 | 31 | 27 | 184.2 | 3 (9.4%) |
| seams lens | 64 | 41.5 | 28.5 | 22.5 | 161.5 | 3 (7.0%) |
| orientation stage | 46 | 41 | 34 | 29 | 182.7 | 5 (10.7%) |
| *builder (control)* | 38 | 25 | 19.5 | 12 | 166.9 | 3 (12.9%) |

**The second rater on `[sort]`.** I sorted the items myself, by the same question.

| Report | Not in view (rows A+C+B) | A+C only |
|---|---|---|
| library (`reviews/2026-10-16-…-library.md`), 19 items | 14 (73.7%): A H1 M1 M5 M8 M12 M13; B M2 M7 M9 M10 L1–L4 | 6 (32%) |
| debt-folds (`reviews/2026-10-17-…-debt-folds.md`), 20 items | 16 (80.0%): A M1 M4 M6–M9 L3; B H1 M3 M5 M11 M12 L1; C M2 M14 L5 | 10 (50%) |
| systems-retrofit, my re-rate of the 52 | 40 (76.9%), against the record's 37 | — |

- **Agreement on the 52 is 49 of 52 (94.2%), κ = 0.85.** I disagree on three items, each of which the record files as "genuinely missing":
  - M13 needed the existing gotcha `a-merge-of-the-default-branch-read-as-additions`;
  - M23 needed `backlog.py:81`'s WONTDO and KEEP verbs;
  - M32 needed `layer-expansions.md:100`'s grant and secret rules.
- **The sort holds.** Pooled over both raters' reports, 67 of 91 items (73.6%) were not in view.

## 3. Across the layers

| Layer | Needs from it | Gives to it |
|---|---|---|
| instruction | the work-order slot `map` rendered by the one renderer; map lines are typed as derived facts and pointers (P11) | the namespaces `unit` and `doc`, with their counts |
| flow | item declarations of a map input and unfold namespaces; `review.dispose`'s record | the mechanical "not in view" cause behind the losing test |
| roles | the `[matrix]` rows that PM-1 names | a whole view for 6 item roles, and `refs` for the rest |
| memory | the one index, extractors and verbs; `memory.item-budget`; the slice manifest | the map, the atlas render, and the `map.complete` leg |
| runtime | extension-point and hook-pack registrations as namespaces; the journal for map bytes | lines for `point` (9) and `hook` (17) |
| observability | — | map bytes per role, read by the Loop Review |
| integrations | registrations under its own prefix | its adapters listed under `layer=integrations` |
| distribution | the kit factory fills `purpose`; adopters' trees | a per-tree map; the codebase map adds code depth where it is installed |

| System | Needs | Gives |
|---|---|---|
| tags | namespace rows gain `purpose-source` and `owner`; the resolver | proof that every namespace has an extractor and an owner (it would have caught M10) |
| annotations | `gov:feature` anchors; the `marker` namespace | the 20 legacy `gov:` words on view (M33) |
| instruction writing | the slot selector by tag | — |
| role shapes | item declarations | map bytes on the shape-run record |
| memory structure | index, `record find`, slice manifest | the amended `[views]`, and a per-namespace overview |
| retrofit | ledger populations as the `population` namespace; purposeless legacy nodes held on the ledger | population counts, which are the progress cell gap-mem-24 lacks |

## 4. Candidates

The shared census command, `python pm2_census.py`, prints per-class bytes in its columns A flat, B tiered and C roll call:

```
layer 8 T 891 649 96 · principle 30 T 1717 1695 156 · chain 15 T 1080 1076 246
build-closed 142 F 14100 60 2261 · build-live 25 T 2430 2223 420 · feature 31 T 3626 2827 484
leg 140 F 4607 42 3917 · class 139 F 21250 46 5560 · decision 189 F 26514 52 4396
gap 219 F 25965 42 2948 · conf-key 141 F 6394 52 4999 · … all 1589 nodes: A 123786 · B 13802 · C 34453
```

The hit test, `python pm2_hits2.py`, asks one question of each render. Take the 22 audit items whose cause was a missing piece, rows A and C less the content-only M35. For how many does the render name the missing node?

```
B      13748 B  hits  5/22: H3 M26 M28 L10 M2
Barch  26002 B  hits 12/22: H1 H3 H4 M16 M20 M24 M26 M27 M28 M33 L10 M2
B+     55115 B  hits 12/22
C      47064 B  hits 11/22
```

| Candidate | Mechanism | Efficiency | Losing test | Result |
|---|---|---|---|---|
| **A. Flat** | one line per node for every class | 123.8 KB; grows about 20 KB a month (builds 2.1 a day, classes 2.8 a day in October) | fits `memory.item-budget` of 96 KB | **Loses**: 123.8 KB is over 96 KB today |
| **B. Tiered, folding, item unfolds (pick)** | bounded classes per node; unbounded classes as count lines; roll calls unfolded per item; deterministic fold to budget | base 13.7 KB, growing about 1 KB a month; architect 26.0 KB | (a) the base fits 24 KB; (b) item unfolds reach the hits of the full roll call | **Survives**: 13.7 KB; 12 of 22 hits, equal to B+ at 47% of its bytes |
| **C. Roll call** | every node's name, comma-joined per class, with no purpose | 47.1 KB; names every node | hits at least B's at fewer bytes than Barch | **Loses**: 11 of 22 at 47 KB, against Barch's 12 at 26 KB; humorous build names carry no meaning |
| **D. Query only** | the designed verbs, with no map | 0 B loaded | the not-in-view share falls with queries alone | **Loses on the record.** Existence probes already run at 7–25% of structural calls, yet 73.6% of items were not in view. The verbs are a faster grep, and the asker still has to name the piece |
| **E. Extend the codebase map** | design-side extractors in `map_extractors.EXTRACTORS` | MAP.md shape, 19.7 KB per 11 inventories | the map exists with the kit absent (PM-2, P28) | **Loses**: the kit is optional by design, and it re-scans for 5.07 s per check |

**What B saves in bytes and lookups (estimated):**
- **Bytes.** 19 KB of base map is 8–13% of a structural role's 142–241 KB read before acting.
- **Lookups.** 46.0% of 2,709 structural existence probes name a node of map B by their final path segment (`pm2_probes2.py`). In a 14-probe sample, about 5 were genuine. So about 16% of probes, roughly 1–2 calls a run, are answerable.
- **The real lever is the not-in-view share.** Projected, it falls from 37 of 52 to at most 25 of 52 (Barch hits), or 23 of 52 with `owner=` keys, which also expose M3 and M10.

## 5. The pick, specified

**One line:**

```
line   := "- " tag [" — " purpose] [" · " count{","count}] [" · " rel{" "rel}]
purpose:= ≤60 chars, verbatim from the namespace's declared purpose-source
count  := <word> " " int        (derived from the index)
rel    := ("layer"|"owner"|"after"|"implements") "=" tag{"," tag}
nsline := "- " ns ".* — " int " nodes · gov tag show " ns ".*"
```

- **What a line never holds:** content, dates and ages, typed status words, line numbers, summaries, render provenance or judgments.
- **What derived status may appear:** a live build's status, as gen_build_index derives it.

**Tiers:**
- **L0** is the slot. It has a header line with the index tree id, then the bounded namespaces, then one nsline per unbounded namespace.
- **L1** is `gov tag show <ns>.*`: that namespace's lines with their purposes.
- **L2** is `gov tag show <tag>` or `record show`.
- **Relations:** outbound through the line's `rel` keys, inbound through `gov tag refs`.
- **Fold rule:** when L0 is over `memory.map-budget`, fold the largest bounded namespace to its roll call and then to its nsline, until it fits. Every fold renders as a pointer line.
- **Code depth:** an optional slot, `map.code`, rendered filled, searched with nothing found, or not installed with `gov tag where` as the fallback.

**Delivery (PM-1):**
- `entry.orient` gets L0 and cuts the card's "neighbours" cells from it: the build's chain line, its features, its gap areas. The card stays at most 8 KB.
- `plan.*` role items, `design.inventory`, `design.decompose`, `design.reason`, `design.unit-spec`, and `review.lens` under the coherence and reuse lenses all get the `map` slot.
- `design.seams` gets L0 inside the house index.
- Unit workers get only `refs` rows for their write set.

**Ownership:**
- **Layer:** memory.
- **Kit:** memory-tree.
- **Chain build:** **dTotalRecall** builds the renderer, the check and the atlas re-render.
- **Other builds:**
  - dOrderedCharter adds `purpose-source` and `owner` to the namespace row;
  - dBoundRoles renders the slot;
  - each owning build fills its namespace's purpose: dWitnessedBar for `leg`, dWellOiledMachine for `hook` and `point`, dShippedRelease's kit factory for `kit`.
- **Records:** no new kind. The map is a view, and the atlas is its owner render.

**Checks, in the `memory` leg pack:**

| Check | Red on |
|---|---|
| complete, three ways (the disk census through `compute_coverage`, against the index, against the map) | a planted `tools/newkit/` with no `kit` row; a map line whose tag resolves nowhere |
| a namespace without an extractor or owner | `doc` registered with neither |
| count | an nsline count that differs from the index count (a planted extractor that drops a row) |
| purpose, as `memory.map-purpose` says | a new `kit.toml` with no `purpose`; legacy nodes sit on a shrink-only ledger population |
| budget | the nslines alone over the budget (a planted 4k budget) |
| render parity | a node in the atlas that is not on the map, or the reverse |
| no stale typed facts | a line carrying a date or a typed status |

**Read-path cost:**
- L0 is about 19 KB per structural spawn, and unfolds add up to 12.3 KB for the architect. Both are memory slices, priced by `memory.item-budget` and reported over budget (MS-3).
- Deriving the map is a view over the cached index, at most 0.11 s. That figure is the census over the raw sources, an upper bound; the index rebuild on a miss is 0.18–0.9 s, as the research measured.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `entry.orient` (filled) | orientation scout | composes the card's neighbour cells from L0 | the card cells keyed to the index tree id | map over budget: fold, reported |
| `design.inventory` (filled) | architect | reads L0 plus the roll calls of `leg`, `check`, `conf-key`, `population`, `marker` and `kit` | the slice manifest names the map's tree id and its unfolds | over the item budget: reported (MS-3) |
| `plan.triage-judge`, `plan.reason`, `design.unit-spec`, `review.lens` for the coherence and reuse lenses (filled) | planner, spec writer, reviewer | read L0 | the slice manifest | as above |
| `review.dispose` (filled) | command | marks each confirmed finding `not-in-view` when the address its fix needs is absent from the author's slice manifest and map | the dispose record's computed cause field | none; it is derived |

| Key | Values | Default | Why |
|---|---|---|---|
| `memory.project-map` | structural-roles, every-role, owner-only | structural-roles | PM-1 |
| `memory.map-budget` | 16k, 24k, 32k | 24k | measured 13.7 KB, plus about 5 KB of designed namespaces |
| `memory.map-purpose` | required, report, off | required | 0% purpose on 5 classes today |
| `memory.map-unfold` | item-declared, none, all | item-declared | Barch reaches B+'s hits at 47% of its bytes |

## 7. Gaps

**What it serves.** It partly closes gap-orient-04, where orientation is exploratory at a median 35 calls, and gap-orient-07, where 15% of calls locate. It also serves gap-mem-05, where READMEs route only to specs, and gap-mem-24, the retrofit's progress cell.

**New gaps, with their evidence:**
- **gap-mem-26 (HIGH): no whole-project view reaches an agent.**
  - 37 of 52 and 30 of 39 review items needed a piece not in view;
  - MAP.md and CARDS.md are loaded by nothing.
- **gap-mem-27 (MED): purpose is undeclared for kits, legs, hooks, config keys and populations (0 of 450 nodes).**
  - Neither the namespace row nor the record-kind registry has a purpose field.
- **gap-mem-28 (LOW): the codebase map is installed by default while the design calls it optional.**
  - `registry.toml:42` against the kit's README `:3`.

## 8. Forks

| Fork | Options, recommendation first |
|---|---|
| PM-4: the base map's budget | 24k; 16k (folds features now); 32k |
| PM-5: purpose lines | required for new nodes, with legacy nodes on the ledger; derived from the first comment or README line; optional |
| PM-6: unfolds | declared by the item; none; every roll call for every structural role (55 KB) |
| PM-7: the attended main session | a pointer to `gov tag show --map` in the card; L0 loaded by default (`memory.default-load=card-and-map`, over the 8 KB budget); nothing |
| PM-8: the losing test | the continuous `review.dispose` cause, judged over the next 38 findings, plus one replay at dTotalRecall's acceptance; the replay alone |

**The losing test.**
- **Method.** Use the mechanical not-in-view share of confirmed findings, A+C, which is 44% on the record's sort and 32–50% on mine. Compare it with the map handed and without, on a replay of the systems round's authoring under one review preset.
- **The map is retired if** the share does not fall by at least 15 points. 38 findings are enough to detect a drop from 74% to 55% at α = 0.05 and power 0.8.

**One process note.** The twin run shares this scratchpad. It overwrote my `census.py` and `orient.py` mid-run, which is why my scripts carry the `pm2_` prefix.

Files:
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-17-build-PLAY-dClosedLoop-1-project-map.md
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\codebase-map\map_extractors.py
- C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\govkit\registry.toml
- C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\pm2_census.py
- C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\pm2_hits2.py
- C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\pm2_probes2.py
- C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\orient6.py
