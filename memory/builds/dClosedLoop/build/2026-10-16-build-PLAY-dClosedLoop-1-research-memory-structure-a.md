# Research: memory structure, run A

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 81's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-26-researcher.md`, which dispatch 82 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

## 1. Verdict

I recommend a **keyed catalogue with section slices**. The repository already has two of the pieces. handoff.py resolves keyed sources into a work order and refuses one that resolves to nothing (`tools/roles/handoff.py:56-63`), and `roles_lib.parse_charter` already slices a document by heading (`tools/roles/roles_lib.py:171-219`).

The pick adds a catalogue generated per git tree, with one row per record and per section. Agents look up a record by its id, tag or heading anchor and get back a single slice. The executor puts those slices into the work order and refuses one that goes over the item's byte budget.

Only the card loads by default, and the harness's auto-memory index stops loading. Nothing in the tree moves: older files get heading anchors derived for them, and new records are tagged when `record` writes them.

## 2. Today

| Part | What it does | Measured | Where |
|---|---|---|---|
| `memory/` overall | trail and library | 4,246 files, 66.75 MB. Builds hold 64.10 MB in 4,013 files: specs 27.3 MB, reviews 17.9, journals 12.5, prompts 2.7, README 1.4, RUN 1.3, BACKLOG 0.9 | measured below |
| Growth | — | 263 KB (Jul 15), 3.87 MB (Aug 15), 31.6 MB (Sep 15), 45.9 MB (Oct 1), 66.8 MB (Oct 16). That is about 1.39 MB a day, and builds are 96% of it | `git ls-tree` per date |
| Generated vs authored | LIVE, backlog shards, ledger, `map/generated`, README `gen:` regions | 3.46 MB generated (5.2%). Another 360 KB is rendered from kit templates: HYGIENE, TEMPLATE-SPEC and six guides | `memory/LIVE.md:1`, `gen_build_index.py:101` |
| Default load | charter, card, harness auto-memory | AGENTS.md 16,732 B, auto-memory `MEMORY.md` 14,005 B (82 lines, 81 files), card median 3,599 B (p90 6,064). Total about 34.3 KB | `CLAUDE.md`, `.claude/settings.json:32`, `.git/orientation/` |
| The charter's read set | the files the charter points sessions at | 8 files, 280,032 B. Each is capped at 61,440 B | `corpus_ids.py --report`, `.memory-tree.conf:483` |
| Read budget | — | **retired**: "never caused a trim: 27 movements… 26 of them up" | `memory/builds/dSpentCeiling/README.md:14-15`, `corpus_ids.py:99,725-728` |
| Kickoff | reads the manifest, M5, recall | SKILL 18,310 B plus SESSION-KICKOFF 19,626 B. Its Step 3 tells the agent to "DERIVE" from decision logs, the backlog, journals and the ledger | `skills/session-kickoff/SKILL.md:126-131,166-190` |
| Work orders | keyed families `task:`, `card:`, `brief:`, `input:`, rule tags | 584 prompts, median 3,335 B (p90 9,997). This one is 18,297 B | `handoff.py:56-63,97` |
| Recall | ranked search | 584 queries, 33 followed by a read of a shown hit (5.7%). The cache is **477 MB** in 3 copies, against a 512 MB-per-copy default | `.git/recall/`, `recall_conf.py:185`, `query.py:301-302` |
| Supersession | relation rows on decisions and gotchas | `check_relations` and `derive_supersession_map` cover only the decision log and gotchas | `row_grammar.py:1282`, `extract.py:703` |
| Drift | report only | 21 of 25 live builds without activity, 10 merged runs non-terminal, 10 dangling ledger pointers, 25 of 31 dossiers stale. It took 27.7 s | `drift_report.py` (run below) |
| Design records | registry, `record`, views, work order as root | settled. They name no index by key, no slice and no read budget | layer-memory `:299-381`, `:383-403`, `:707-724` |

Where the records and the code disagree:
- The cost research's default load leaves out auto-memory's 14,005 B (`research-orientation-cost.md:18`).
- `gap-orient-10` gives 12 of 98 dead paths. My predicate, repository paths with a file extension, finds 3 of 40. The two predicates differ, and I did not reconcile them.
- No design record mentions that dSpentCeiling retired a read budget. Any new budget has to answer that finding.

Commands (outputs trimmed):
```
$ git ls-tree -r -l <rev> memory | awk …   →  2026-10-01 files=2663 bytes=45874233 … 2026-10-16 files=4246 bytes=66750246
$ python3 tools/memory-tree/corpus_ids.py --report  →  read path: 8 files, 280032 B … ids defined: 2141
$ du -sb .git/recall/cache/*  →  163561059 / 160644683 / 151576063
```

**Transcript probes.** I ran these over 3,627 transcripts from 2026-08-08 to 2026-10-16, using scratchpad scripts `memq*.py`, `cold.py`. They were read-only.

| Measure | Value |
|---|---|
| tool calls touching `memory/` | 58,636, which returned 270.8 MB |
| bytes returned, by kind | specs 152 MB, journals 23.1 MB, guides 20.3 MB, reviews 19.3 MB |
| memory searches by query class (31,790) | unit id 11,813 (37%), free text 10,956, build slug 7,930 (25%), section tag 433 (1.4%), gap id 24 |
| empty-result misses | 0.7%. Searches rarely come back empty; they come back too wide (see the next row) |
| files one id grep returns (80 sampled ids) | median 15.5, p90 52, max 113. 94% return 3 or more |
| subagent memory Read bytes (1,328 agents) | median 52,694, p90 183,553 |
| share of those bytes that were re-reads | 9.2% |
| share of read bytes whose file the agent's final text names (a lower bound on use) | 3.9%: specs 4.8%, reviews 0.0%, guides 2.1% |

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | statement types; P11, under which a typed fact that can go stale never loads; level-0 load list | memory never loads as instruction. The reuse entries' text reaches work orders as slices keyed by tag |
| flow | each item's declared read keys; items Plan sizes to fit one context (`compaction-results.md:306-308`) | slice manifests that become part of the render witness; `next` and the card cite keys |
| roles | a byte budget per role item; the work order as the agent's root | `rec:<key>` slices for handoff.py's key families; re-reads become answered calls |
| memory | the registry declares the catalogue kind, and `record` is its door | id, tag and anchor lookups; supersession and freshness for each row; the research and routing views as queries |
| runtime | the `record get/find` command adapter; a journal reader; the harness adapter's default-load list | load-set bytes for each harness, and an idempotence key (tree hash) |
| observability | a journal reader that computes read-past-order bytes per item | the read-past signal, with its liveness; the trend for the Loop Review |
| integrations | none | none: release records are only keyed rows under `memory/integrations/` |
| distribution | installs the generator, and the slot's state when recall or the map is absent | a catalogue that works with core alone, so recall is not needed |

| System | Needs from it | Gives it |
|---|---|---|
| Tags | one grammar for section tags `[a-z0-9-]+` and kind tags `record.<kind>`, with a registry | resolution of a tag to its home, and a check that runs both ways (a dangling tag, a duplicate tag) |
| Code annotations | the `refs=` key grammar | `gov:note refs=` and `gov:feature` resolve through the catalogue; the annotation index becomes one of its shards (map installed) |
| Instruction writing | the six statement types; template-rendered sections that carry tags | memory sections arrive in a work order as tagged slices, never as pointers |
| Role workflow shapes | each item's read keys and budget, declared in the item | slice rendering, budget refusal, and the read-past measure for each role |

## 4. Candidates

| | A. Folders and views (the design as written) | **B. Keyed catalogue and section slices** | C. Summary tiers (progressive disclosure) | D. Search first (recall as the default path) |
|---|---|---|---|---|
| Mechanism | registry homes and generated views. A work order hands paths and fields, and agents grep and Read | generated rows (key, kind, home, byte range, blob, status, superseded-by). `record get <key>` returns one slice, and the executor inlines it under a budget | every record carries a summary, and agents read summaries first | ranked chunks answer each query |
| Efficiency (method) | per handoff 193,157 B handed whole; an id lookup returns 15.5 files (measured) | 55,451 B per handoff (29% of whole, n = 1). An id lookup returns 1 row. The catalogue builds in 0.9 s over 4,134 files | estimated small, but loses its test | 5.7% read-through; a 477 MB cache |
| Losing test | A loses if a work order that can address only files hands no more than 1.5 times what a section-addressed one hands, **or** if an id lookup already returns 2 files or fewer at the median | B loses if (a) the catalogue takes more than 5 s to build, (b) the median section is not much smaller than a file, (c) less than 60% of bytes can be sliced, or (d) an id lookup already returns one file | C loses if summaries drop the exact identifiers that make up at least 50% of agent queries | D loses if read-through of shown hits is under 30% |
| Result | **LOSES**: 3.5 times as many bytes, and a median of 15.5 files per id | **PASSES**: 0.9 s; median section 962 B (p90 2,928); 90% of bytes sliceable; 15.5 files per id | **LOSES**: id, slug and tag lookups are 63% of searches, and summaries kept 1 of 9 numbers and 1 of 7 identifiers (`compaction-results.md:186-193`) | **LOSES**: 33 of 584 (5.7%), and the chunks arm scores 0.00 |

Commands behind B's test:
```
$ python3 - (walk memory/*.md, split at ^#{2,3} )
md files 4134 bytes 64980774; >=3 headings: 2902 files 58297340 bytes (90%); headings 38236, tagged 358;
section median 962 p90 2928; scan 0.9s
$ python3 - (80 random ids from corpus_ids --print-defined-ids; git grep -l -w per id)
ids 2141 sample 80 files per id median 15.5 p90 52 max 113 share>=3 0.9375
$ python3 - (slice layer-memory [design,tools,revised], layer-library [design,consult,settled-lb], layer-expansions [revised])
total 193157 55451 29%
```

D's command: `python3 -c … .git/recall/queries.jsonl` returned `Counter({'query': 584, 'opened': 133, 'refused': 6}) opened-in-shown 33`.

A rejected variant that is not a separate design is a hot and cold partition, moving dormant builds out of the default path. Its test was whether the cold set is stable and rarely read. It failed: 143 of 173 builds had a commit in the last 21 days because of sweeps, and 13.4% of the bytes agents read from builds still went to dormant builds (`cold.py`: `cold 738 12305172 … 13.4%`).

## 5. The pick, specified

**Key grammar**, which the tags system owns:

```
key     := id | slug | kind ":" natural-key | path "#" anchor | key "#" anchor
anchor  := tag            ; [a-z0-9-]+, from "## [tag]" — unique per record
         | "h-" slug(heading) [ "-" n ]   ; derived for legacy headings, never typed
```

**Catalogue row** (kind `record.catalogue`, generated, layer `memory`):

`key, kind, layer, home (path|ref), anchor, start, end, bytes, blob, status (derived), superseded_by, cites[], lifecycle, tree`

The catalogue sits in `<git-common-dir>/gov/catalogue/<tree>.jsonl`. It is cached by tree hash and never tracked, which is the rule the map's callers already follow (layer-memory `:634-636`). That choice is fork F1.

**Kits and code:**
- memory-tree gets `record get <key>`, `record find --kind/--tag/--status/--since` and `record cites <key>`, which returns the inverse.
- The slicer is `parse_charter`'s section split, generalised (`roles_lib.py:186-191`).
- The id grammar comes from the one parser (layer-memory `[names]`).
- handoff.py gains a key family `rec:<key>`, and refuses a key that resolves empty, as it already does (`handoff.py:62-63`).
- The work order carries a slice manifest: key, blob and bytes for each slice.

**Owners:** the memory layer, in chain build **dTotalRecall**. The render is dBoundRoles' and the read-set sizing is dRankedPlan's.

**What loads:**

| Load | Default | On demand |
|---|---|---|
| main session | charter (instruction's), and the card, with handles and pointers given as keys (`card.pointers`) | `record get` |
| role agent | its work order, with slices inlined under budget | one probe outside the order, journaled and counted |
| owner | — | the generated views |

**Read-path cost (estimates and method):**

| Measure | Today | Pick | How the number is reached |
|---|---|---|---|
| memory bytes in the default load | 17.6 KB (auto-memory plus card) | card only, 6 KB or less | today's p90 card size |
| one id lookup | 15.5 files returned | 1 row | measured above |
| memory a role agent reads | median 52.7 KB | 24 KB or less | the 29% slice ratio, plus a margin. The ratio comes from n = 1, so dTotalRecall's acceptance re-measures it on 30 work orders |
| re-read bytes | 9.2% | 0 | a re-read becomes an answered call |

**Checks.** Each turns red on a planted case.

| Check | Red case |
|---|---|
| `memory.catalogue-fresh`: a re-render equals the cache for HEAD's tree | a record edited and the cached row left at its old blob |
| `memory.keys-resolve` (both ways): every key in a card, work order, relation or `refs=` resolves to exactly one row, and every tagged section is unique | a duplicate `[design]` in one record; a dangling `rec:` key |
| `memory.order-budget`: a work order's slice bytes are at or under its item's budget, or the render refuses | a planted three-slice order over budget |
| `memory.no-default-ingest`: the default-load set the harness adapter lists contains no `memory/` file except the card | a planted `@memory/DECISIONS.md` in CLAUDE.md |
| `memory.superseded-in-order`: a slice whose row has `superseded_by` set is refused unless it is marked as history | a planted superseded decision row handed to a builder |
| `observe.read-past` (report only, with liveness): bytes read under `memory/` outside the manifest, per item | a DEAD PROBE reading on an empty journal |

`order-budget` binds each item at the time it is rendered. It does not bind a global sum, so it does not repeat the retired one: the old global budget priced kit releases this repository could not trim (dSpentCeiling `:14-21`).

## 6. Items and policies

| Item | Actor | What it does | Witness | Routes |
|---|---|---|---|---|
| `plan.read-set` (new) | planner role | declares each item's read keys and estimates their bytes | the plan record's keys resolve at the base SHA, and each sum is at or under budget | over budget: split the item |
| the render step of the item cycle (filled) | executor | resolves the `rec:` keys, inlines the slices and writes the manifest | every manifest row's blob equals the catalogue at the item's SHA | refusal: `next` returns `plan.read-set` |
| `entry.orient` (filled) | hook | the card's pointers become keys | each pointer resolves | a stale key is re-derived |
| `maintain.read-audit` (new; observability) | command, as a journal reader | computes read-past bytes for each item and role | a report record keyed by period, under `memory/observability/` | over threshold: file an ask whose acceptance is the next period under the threshold |

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `memory.default-load` | `card`, `card-and-live`, `none` | `card` | memory takes 17.6 KB of today's default load, and P11 says a typed fact that can go stale never loads |
| `memory.item-budget` | KB, from 8 to 256, set per role | builder 24, reviewer 48, researcher 64 | the subagent median is 52.7 KB and the p90 183.6 KB |
| `memory.over-budget` | `refuse`, `report`, `off` | `refuse` | a budget that only reports never trimmed (dSpentCeiling) |
| `memory.legacy-anchors` | `derived`, `none` | `derived` | 99.1% of today's headings carry no tag (358 of 38,236) |
| `memory.superseded-slices` | `refuse`, `mark` | `refuse` | a fact that has been replaced should never be handed as current |
| `memory.harness-memory` | `unloaded`, `loaded`, `promote-only` | the owner's call (F2) | 14,005 B loads every session, outside the contract |

## 7. Gaps

**Closed or advanced.** The ids are the ones cited in the records named for this part.

| Gap | How the pick closes it |
|---|---|
| `gap-mem-05` | the README's routing region is a catalogue query by kind |
| `gap-mem-15` | the research view is `record find --kind research-return` |
| `gap-mem-09` | the core gets a retrieval path that does not need recall |
| `gap-mem-16` | non-build homes become catalogue rows keyed by kind |
| `gap-orient-14` | after a compaction, the card's keys re-derive what was lost |
| `gap-orient-10` | closed if F2 unloads auto-memory |

**New gaps the pick exposes** (proposed ids):

| Gap | Severity | Evidence |
|---|---|---|
| `gap-mem-17`: no index by key or section | HIGH | an id grep returns a median 15.5 files; 358 of 38,236 headings carry a tag; no tool parses section tags (an empty grep over `tools/` and `skills/`) |
| `gap-mem-18`: no read budget for an item, and the global one was retired | MED | subagents read a median 52.7 KB and a p90 183.6 KB of memory; re-reads are 9.2% of bytes; check 16's budget was retired (`corpus_ids.py:99`) |
| `gap-mem-19`: recall's cache dwarfs the corpus | LOW | 477 MB in 3 copies for a 67 MB corpus |

**Not closed:** the build folder grows by about 1.39 MB a day with no retention except rotation of the decision log. The read path is unaffected while nothing loads by default, but grep widens as the folder grows.

## 8. Forks

| Fork | Options | Recommendation |
|---|---|---|
| F1: where the catalogue lives | a cache keyed by tree hash (never merged, rebuilt in 0.9 s), or tracked and sharded per build (re-rendered after each merge) | the cache, as callers already do |
| F2: the harness's auto-memory | `unloaded`, `loaded` (today) or `promote-only` (R-I promotes its entries) | `promote-only`: P23 already treats it as evidence |
| F3: what happens over budget | refuse at render, or report only | refuse: the reporting budget never trimmed anything |
| F4: anchors for legacy records | headings derived for all 4,134 files, or tags only on new records | derived: 90% of bytes can be sliced today |

The probe scripts are in the session scratchpad, `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\` (`memq.py`, `memq2.py`, `memq3.py`, `cold.py`).
