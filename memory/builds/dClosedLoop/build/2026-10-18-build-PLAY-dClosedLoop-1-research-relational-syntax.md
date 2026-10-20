# Research: one relational syntax across memory

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 103's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-7-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`.

---

1. **Verdict**

Pulling a tag and reading its enclosed regions works if a feature's members are declared where they already live, their spans are derived, and one closed set of typed edges joins them. A `gov tag bundle <tag>` verb then returns one row manifest per tag. Four of the five candidates lose a measured test. Explicit begin/end regions everywhere: 56% of the `roles` feature's outside spans are single-line uses that can be derived. Spans from symbols only: 68% of those spans sit in no symbol whose extent can be derived. Sidecar line spans: 88.9% shifted within 30 days. Pure grep: 36% precision. The pick is the hybrid. Two gaps block it: no instruction can be scoped to a feature, and decision rows carry no feature edge.

2. **Today**

All counts are at `beda01950`. The probes are in `…/scratchpad/p4rel/` (`census.py`, `sec.py`, `fl_drift.py`, `dossier.py`, `regions.py`, `spans.py`, `spandecay.py`). All of them read only.

| Pointer kind | Grammar | Count | Read by | Checked by | Stale (tested) |
|---|---|---|---|---|---|
| Charter rule tags | `- [tag] ` under `## 1.` | 46 rules; `rules:` in 10 role files | `render_charter_blocks` `tools/roles/roles_lib.py:279` | `check_rule_tags` `:252`, role→rule only | 0 dangling (leg-gated) |
| Record section tags | `## [tag]` | 563 definitions, 335 distinct, 47 files, **0 outside dClosedLoop** | nothing in `tools/` | nothing | of 3,696 citations: 1,231 ambiguous (33%), 415 defined nowhere (11%; `[check]` 134, `[claims]` 50, `[config]` 36 are TOML tables) |
| Item tags | `` `step.name` `` | 5,189 citations in 228 memory files; 18 in code | nothing | nothing | declared only in design records |
| Ids | `FAMILY-slug-seq` | 132k occurrences in memory, 8,322 in 296 code files | `grammar_for` `tools/memory-recall/extract.py:569` | hygiene checks 13 and 14; drift-audit report-only | 116 of 1,199 code-cited ids appear nowhere in memory, nearly all fixtures (`zFixture`, `aSeed`) |
| Gap ids | `gap-<area>-NN` | 2,392 in memory, 2 in code | nothing | nothing | not tested |
| `gov:` words | `gov:<word>` | 20 words, 430 occurrences in 135 files; `gov:note` and `gov:feature` **0** | each word's own gate | per word | not tested |
| **Region markers** (5 families) | `# >>> n`/`# <<< n`; `gov:argv-*`; `gov:conf-allow-*`; `<!-- gov:playbook -->`; `<!-- gen:* -->` | 2,432 pairs | **5 separate parsers**: `check-unattended.sh:211`, `resolve-python.test.sh:203`, `render_playbook.py:118-120`, `map_lib.py:860`, `gen_build_index.py:104` | byte parity or re-render | **0 unbalanced**; marker lines were edited in 62 of 2,043 commits (3.0%) touching their files in 90 days |
| Paths | `tools/…`, `memory/…` | 107,199 in memory | agents | `check-dead-paths` (deleted names only) | 3.5% dead |
| file:line | `path:N` | 10,655 code citations in memory, **12 in live (non-build) memory** | agents | nothing | sample of 60: **6 still on the same line**, 34 with the text moved, 19 changed, 1 file gone |
| Dossier claims | TOML `[claims]`, `[paths]`, `decisions` | 31 dossiers, 120 leg claims, 74 decision ids | `compute_coverage` `map_lib.py:1404` | gated both ways | 120/120 legs resolve; **prose: 25/31 have code newer than the dossier** |
| Recall index | FTS5, keyed per record and chunk | derived, cached under the git common dir (`query.py:291,382`) | `query.py` | its selftest | rebuilt, not stale |
| Relation keys | map `rel := layer\|owner\|after\|implements`; build `parents:` | `parents:` in 11 of 173 READMEs | `gen:build-edges` | re-render | `map.py:393` renders only `after`/`owner`/`layer` |

```
$ python -I census.py .            # abridged
section-tag defs (memory): (563, 47) · `[tag]` citations memory: (3705, 380) · item-tag cites memory: (5189, 228)
gov: words: kit=198, fixed-verifiers=50, bounded-fanout=42, … (no note, no feature)
$ python -I fl_drift.py . 60 4
code file:line citations in memory: 10655
sample 60: same 6  moved(line text elsewhere) 34  changed/removed 19  file gone 1
$ python -I regions.py .   -> >>>/<<< pairs 242 · argv 2 · conf-allow 1 · playbook 2 · README gen: 2185 · unbalanced 0 each
$ python -I dossier.py .   -> dossiers 31; code newer than dossier 25 · leg claims 120, unknown 0 · decision ids 74, missing 0
```

**The cost of orienting on `roles` today** (`memory/map/features/roles.md`):

| What | Lookups | Bytes read whole |
|---|---|---|
| The dossier | Glob + Read = 2 | 11,377 |
| The code (`tools/roles`, 31 files) | ls + 5 reads | 233,608 (165,344 in py and sh) |
| The tests (4 legs) | grep `gate-legs.json` + 1 read | 35,564 (`adopt-roles.test.sh`) plus selftests inside the sources |
| The decisions (11 spec ids) | Glob + 11 reads + grep `DECISIONS.md` | 434,657. **0 of the 11 are log rows, and the dossier omits the 2 log rows that exist** (`DECISIONS.md:12,138`) |
| Outside readers | grep that needs the symbol names + about 15 slice reads | 212 relevant lines across 15 files (38,612 lines) |
| Instructions | grep, then a guess | no join exists. `AGENTS.md` has 6 lines; `WIRE-INTO-PROJECT.md` is 162,896 B |
| The build | 1 read | 18,851 |
| **Total** | **about 42 calls** | **about 734 KB whole-file**, before readers and guides |

The bare word `roles` hits 44 code files outside the kit, and 16 of them are real readers (36% precision).

3. **The design today**

| Need | What the design gives | What it lacks |
|---|---|---|
| Pull a tag | `gov tag show\|where\|refs\|check`; leaf slice, one call (systems `[design-tags]` :247-249) | **No bundle verb.** `show` returns one slice and `refs` returns inbound keys, so the bundle is assembled by hand |
| Regions in records | `## [tag]` sections; derived anchors for legacy headings (`[design-memory-structure]` :456-463) | nothing new is needed: sections are the regions |
| Regions in code | `gov:note` "heads an annotated block"; the budget is ≤12 comment lines (:287-305) | **No code extent.** Nothing says where a note's code ends |
| Feature tags across layers | `feature` namespace (dTotalRecall); `gov:feature` anchor joined to the reuse entry | **Instructions cannot select a feature.** R-B's selectors are reader, role, item, step, practice and policy (`layer-instruction.md:409-412`); P13 scope names "steps, items, roles, policies and layers" |
| Typed edges | map `layer\|owner\|after\|implements` (`project-map.md:556`); build relations `depends-on\|patches\|amends\|supersedes\|implements` (`layer-memory.md:523-529`); legs declare principles (dWitnessedBar row) | **Two vocabularies, no closed set**, and no `tests`, `decides` or `instructs` edge type. `implements` has different targets in each |
| One resolver | one index and resolver (`[cross]` :177-195) | correct; the bundle only adds a walk over typed edges |

Where records and code disagree:
- `project-map [line]` lists `implements`, but `map.py:393` renders only three keys.
- The `roles` dossier's `decisions` field omits both `aOrientedCast` log rows.
- `check-playbook-parity.sh:14` says the charter has no numbered sections, yet `roles_lib.py:61` requires `## 1. `.
- tags-a's 358 headings in 34 files is now 563 in 47 (growth, not an error).

4. **Candidates**

| | **R: regions everywhere** | **A: point anchors + derived spans** | **S: sidecar manifest per feature** | **Q: query only** | **H: declare at the site, derive the rest (pick)** |
|---|---|---|---|---|---|
| Syntax | `gov:region <tag>` … `gov:end <tag>` in comments; records keep `## [tag]` | `gov:note <tags>` head line; span = the enclosing symbol from the code map | the dossier grows `[members]` rows: path, span, tags, units | none | the existing sites (dossier globs and claims, `gov:feature`, `gov:note`, `## [tag]`, unit scope, leg fields) plus typed edge keys `type=key[,key]`. A span is the symbol extent where one is derived, else an explicit `gov:end <tag>` |
| Resolution and bundle | index of regions by tag; content = region text | index of anchors; span through the map | read the manifest | ranked grep or FTS | `gov tag bundle <tag>`: the node row plus inbound edges grouped by type, each row `path:span · type · bytes`, content per row via `show`. `roles` ≈ 39–44 rows, about 4.5 KB, folded by type past `tags.bundle-rows` (map fold rule) |
| Instructions | the region holds the directive | `→ unit` | manifest column | none | units carry a `feature.*` selector, so the bundle lists them by edge type |
| Drift and rot | markers move with the code; content can drift silently | symbol renames: 3.6% lost per month | line spans shift | none to rot | gated joins plus derived spans; no line numbers are stored |
| Merges | one extra line per boundary; edited in 3.0% of commits | none | one hot file per feature | none | edge keys sit beside the facts they annotate; the index is never committed |
| Languages | any comment syntax | only where a symbol extractor exists | any | any | symbol extents per the map's language packs; `gov:end` covers the rest |
| Gates | balance, tag resolves | anchor resolves | manifest freshness | none | edge type registered; target resolves; feature joins (≥1 `implements`, ≥1 `tests`), armed per population |
| Prior art | `#region`; Doxygen `@{ @}` groups; noweb chunks | ctags; SCIP/LSIF ranges | Doorstop/sphinx-needs items | grep; recall FTS5 | Kythe/SCIP (derived anchors plus typed edges); sphinx-needs typed links; wiki backlinks (inbound derived) |
| **Losing test** | wrapping a feature's outside code is cheap and states nothing derivable | ≥80% of a feature's spans sit in a derivable symbol | line spans survive 30 days | precision ≥50% for the feature word | every member class of `roles` has a declaring site or a derivation, and the bundle fits 40 rows |
| **Result** | **Loses.** `roles` has 57 spans in 15 files; 32 are single-line uses the map can derive; wrapping costs 114 marker lines around 212. Rot passes: 2,432 pairs, 0 unbalanced | **Loses.** 18 of 57 spans (32%) sit in a symbol under 400 lines; shell top-level code and tests have none | **Loses.** Python extents at `c237672a5` → HEAD: 7.4% same range, 88.9% shifted, 3.6% gone. Dossier prose: 25/31 stale | **Loses.** 16 true of 44 hits (36%) | **Passes, with two misses.** Kit files via globs 31/31, legs 4/4, specs 11/11, readers 15/15 by derived symbol mention. **Decision rows 0/2 and units 0** have no declaring site (the gaps below). Rows: about 44 unfolded, 39 with the kit folded to one row |

```
$ python -I spans.py . 'roles_lib|roles\.json|handoff\.py|render_agents|loadRoleIndex|role index|roles kit' <16 readers>
TOTAL spans 57 span-lines 212 inside derivable symbol 18 (32%)        # sizes: 1 line 32, 2-8 lines 19, 9+ lines 6
$ python -I spandecay.py . c237672a5      # 2026-09-17
symbols at c237672a5 1428: same line range 106 (7.4%), range changed 1270 (88.9%), path::name gone 52 (3.6%)
$ git grep -lw roles -- tools skills .githooks .claude ':!tools/roles' | wc -l   -> 44   (true readers 16)
$ git log --since=2026-07-20 -G'^\s*(#|//) (>>>|<<<) ' -- <126 files> | wc -l -> 62 of 2043
```

The JS and shell symbol scan in `spans.py` is a brace heuristic, so the 32% may under-count JS methods. The build must re-run this test with the map's own extractors and must red if the share is ≥80%. R survives only inside H, as the explicit `gov:end` for blocks with no symbol: 6 of the 57 spans run 9 lines or more. I stopped at five: tracked versus cached bundles, or one manifest per kit, differ from these only in detail.

5. **One relational syntax**

**Grammar** (it extends `[design-tags]` and reuses the map's `rel` form):
```
node   := tag | id | section            (as [design-tags])
edge   := type "=" target ("," target)*   target := node | path["#" symbol]
type   := one of the closed set below; an unregistered type reds
inline := gov:note <tags> — <def> → <ptr> [refs=…] [<edge>…]      (code; tags = part-of)
          gov:feature <tag>                                         (code; implements, canonical)
          gov:end <tag>                                             (code; only where no symbol extent derives)
```

**The closed edge types.** Each row is one registry entry in dOrderedCharter's namespace table. The inverse is always derived.

| Type | Inverse | From → to | Declared at |
|---|---|---|---|
| `part-of` | has-part | path, span or section → feature, kit or layer | dossier globs; `gov:note` tags; `kit.toml` `layers` |
| `implements` | implemented-by | code or build → feature, reuse entry or item | `gov:feature`; build front matter |
| `tests` | tested-by | leg or test → feature, item or unit | leg row field (dWitnessedBar) |
| `decides` | decided-by | decision row, fork or spec → feature or tag | decision row and spec field |
| `instructs` | instructed-by | unit → any selector, `feature.*` included | unit scope tags (P13) |
| `enforces` | enforced-by | leg, check or hook → principle, rule or unit | leg and check rows |
| `after` | before | build → build (today's `parents:`, `depends-on`) | README front matter; chain |
| `supersedes` · `amends` · `patches` | the passive forms | record or unit → record or unit | `record` front matter |
| `owner` · `layer` | owns · contains | node → chain build · layer | PM-8 fields |
| `cites` | cited-by | any → any | **derived** from `[tag]`, `refs=`, `→` and ids in text |

**Derived, never written:** every inverse; spans (section bounds, symbol extents); uses (map callers and mentions); `cites`; the dossier's `decisions` list (it becomes the `decided-by` view); bundles; staleness. A file:line pointer in new text joins the positional population that `tags.positional` holds; new text cites `path#symbol` or `@blob`.

6. **Chain, gaps and forks**

**Units to add, by build:**

| Build | Unit |
|---|---|
| dOrderedCharter | the edge-type registry and the `edge` grammar; `feature` added as a selector (amends R-B and P13); `gov tag bundle` with `tags.bundle-rows` and the fold; the type-registered and target-resolves checks |
| dTotalRecall | extractors emitting typed edges from annotations, front matter, dossiers and decision rows; the span rule (symbol extent, else `gov:end`); the region-parser factory in `tools/lib` (six region families once `gov:end` arrives, so [reuse] requires the factory); the dossier's header becomes the feature node, with its prose moved to units and records; `decides` on decision rows; a fix so `map.py`'s successor renders `implements` |
| dBoundRoles | the work order selects by `feature.*`; the code-notes slot filled from the bundle |
| dWitnessedBar | `tests=` and `enforces=` fields on legs |
| dIndexedDesign | the structured spec declares `implements=` and `decides=`; `design.seams` reads the bundle |
| dTendedCadence | a detector for bundle members whose code changed while their head line did not |
| dConvergedCharter | feature-specific guide prose migrated into feature-scoped units |

**Gaps to register** (the register owner mints the ids):
1. No instruction can be scoped to a feature (`layer-instruction.md:409-412`). dOrderedCharter.
2. Two relation vocabularies and no closed edge set (`project-map.md:556`, `layer-memory.md:523-529`). dOrderedCharter.
3. `gov:note` has no code extent, and 68% of a feature's outside spans have no derivable symbol. dTotalRecall.
4. The decision-to-feature join runs one way only: 0 of the 2 log rows appear in the dossier. dTotalRecall.
5. Five region parsers and no factory. dTotalRecall.
6. file:line citations go stale: about 90% have moved, and no check sees them. dOrderedCharter, as a positional class.

**The owner's forks:**

| Fork | Options, recommendation first |
|---|---|
| RS4-1 Span mechanism | derived spans, with explicit `gov:end` only where no symbol extent derives; explicit regions everywhere; point anchors with no spans |
| RS4-2 Feature as an instruction selector | add `feature.*` as a selector; features stay descriptors, and instructions reach a feature only through its reuse entry |
| RS4-3 Bundle content | a row manifest, with content pulled per row; content inlined under a byte budget; both, by flag |
| RS4-4 The edge set | the closed set above; a minimal six (`part-of`, `implements`, `tests`, `decides`, `instructs`, `cites`), with lifecycle relations left to `record` |
| RS4-5 The dossier | its header becomes the feature node and its prose moves out; keep it as is; fold it into the reuse entry |
| RS4-6 file:line in new text | refuse under `tags.positional`; report only |

The probe scripts are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/p4rel/`. Nothing in the repository was written.
