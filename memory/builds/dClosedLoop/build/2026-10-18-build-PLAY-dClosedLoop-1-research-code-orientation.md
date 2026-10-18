# Research: code depth in the core, and orientation by role

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 102's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-6-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`.

---

## 1. Verdict

Today only the reuse scout is designed to see callers, and only when the optional codebase map is installed. The other six orienting roles see code down to kit and feature lines at most. The two roles the owner names, the researcher and the prompt writer, get no map at all.

I recommend three mechanisms together:
- **A, in core:** a derived code record (files, definitions with line ranges, imports, resolved calls, tests, kit membership), cached by tree hash.
- **B, per work order:** a `code` neighbourhood slot computed from A for each item's seed.
- **C, the fallback:** `git grep` as the floor for any language.

Purposes come from docstrings first, and agent enrichment is keyed to each symbol's body hash. Keying by file or feature loses: 60% of files change in a week, against 3.4% of symbols. Moving code depth into core partly reverses KN-1, so that is the owner's call (CM-1).

## 2. Today

**The kit, measured** (`tools/codebase-map/`, `memory/map/`):

| Item | Measure | Command and output |
|---|---|---|
| Generated files | `MAP.md` 20,305 B, `CARDS.md` 22,363 B, `inventories.json` 15,387 B, `symbols.json` 555,035 B | `wc -c memory/map/generated/*` |
| Symbol index | **Exists**: 4,670 rows, fields `id`, `kind`, `file` only. 4,605 functions, 55 classes, 10 const-exports, across 224 files. Public module-level definitions only: no methods, no nested or private definitions, no line numbers (`map_lib.py:318-360`). Rendered only where the project declares the symbol tier (`gen_map.py:147-151`) | python summary of `symbols.json` |
| Caller index | **None committed.** Fan-in counts name tokens on demand and resolves nothing (`map_lib.py:902-981`) | — |
| Dossiers | 31 dossiers with 141 path globs (138 file or pattern globs, 3 whole-directory). They claim 307 of 384 tracked files in `tools/` and `skills/` (79.9%), 85.3% of the bytes; 30 files are claimed twice. Unclaimed files sit mostly in memory-tree (17), lib (10) and run-gates (8) | glob probe over each dossier's toml fence |
| Dossier staleness | **25 of 31 stale** at HEAD, in 0.83 s. layer-memory `[map]` (line 743) recorded 28; the count moves with time | `map_diff.py --stale-dossiers --json` → `{'of': 31, 'stale': 25, 'live': True}` |
| Freshness check | exit 0, 4.8 s | `gen_map.py --check` |
| `reuse_lookup.py` | 3.2 s. For "render a role prompt with a task block and hash it into a spawn marker" it returned 33 name-stem hits, led by `render` (fan-in 13). The real seam, `tools/roles/handoff.py` `render_handoff`, is absent | `reuse_lookup.py "<query>"` |

**How a spec writer and a builder get code context today:**
- **Spec writer.** It reads only brief fields, `task:reuse?` and `card:route?` (`tools/roles/agents/gov-spec-writer.agent.md:7`). It is ordered to verify every claim about code by reading that code (`:30`).
- **Builder.** It reads `input:spec`, `card:route?` and `brief:non-goals?` (`gov-builder.agent.md:7`). `spec` is a path input (`handoff.py:99,331`), so the builder receives the spec's path, not its content, and is told to "read the spec whole" (`:19`).
- **The renderer.** `render_handoff` resolves only `task:`, `card:`, `brief:` and `input:` keys (`handoff.py:312-423`). No key carries code.

**One real unit, `TOOL-dRedressedBar-24`.** Its spec is 45,639 B and names 35 code paths, with 5 `file:line` citations. Its build commit `73b80ed31` touched 11 code files, and the spec named 10 of them beforehand. Probe: `probe_unit.py`, run over the two transcripts.

| Agent | Prompt | Code paths in the prompt | Calls | Code lookups | Code reads | Distinct code files read |
|---|---|---|---|---|---|---|
| spec writer (`agent-a8d6dbd5…`) | 7,097 B | 7 | 195 | 80 (149,970 B) | 30 (113,757 B) | 14 |
| builder (`agent-adce44e2…`, workflow) | 5,764 B | 1 | 238 | 45 (81,354 B) | 31 (180,808 B) | 19 |

What those lookups were (`lookups.py`):

| Agent | Lookups | Name a defined symbol (upper bound) | Text or pattern searches | Headings | Definition outlines |
|---|---|---|---|---|---|
| builder | 56 | 36 | 14 | 5 | 1 |
| spec writer | 106 | 59 | 41 | 4 | 2 |

**Extraction available with no new dependency.** Probe: `codemap.py`, a read-only `ast` pass over `tools/`, `skills/` and `.githooks/`.

| Primitive | What it yields here | Time and size |
|---|---|---|
| Python `ast` | 3,241 definitions (2,735 top-level, 506 methods or nested), 69.1% with a docstring; 1,144 imports; 59,519 call sites, of which 2,849 edges resolve. 24.3% of calls are local, 3.1% module-attribute resolved, 0.2% resolved from-imports, and 28.4% are method or external attribute calls left unresolved | 12.0 s cold |
| Shell and JS by regex | 2,008 shell functions (49.6% with a comment line above); 1,167 cross-language edges; 298 JS definitions; 17 registry edges (paths inside JSON and TOML) | 0.24 s |
| Tests | 84 test files; 2,310 test-to-file edges by name | 0.8 s |
| The whole record | 941,381 B of uncompressed JSON | 13.1 s |
| `git grep -w` | 97–113 ms per query. `render_charter_blocks`: 4 files, against 2 resolved callers. `main`: 180 files, against 5. 92 of 2,450 top-level Python names (3.8%) are defined in more than one file | `git grep -lw <sym>` |
| ctags | not installed | `command -v ctags` → not found |

## 3. The design today

| Role | What it gets about code | Level | Slot | Record kind | Budget | Blind to |
|---|---|---|---|---|---|---|
| orientation scout | the whole level-0 map; its code nodes stop at `kit.*` (purpose and layer) and `feature.*` (purpose and leg count) | 0 | `map` | the map view over the one index | 32 KiB (`project-map.md:864`); the card ≤ 8 KB | every path, symbol and caller |
| prompt writer | nothing of its own: it frames the actor's resolved work order (`flow-roles.md:19-22`) | — | the actor's | — | — | everything its actor lacks; it is absent from the delivery table (`project-map.md:617-626`) |
| researcher | no map: not listed in `[delivery]`, and not a structural role | — | none | — | 96 KB item budget | all of it. Researchers today spend 12.1% of calls locating and 30.2% of bytes orienting (`layer-roles.md:121`) |
| reuse scout | the house index: symbols, callers, dossiers and reuse entries in M1c's shape, 2–33 KB (`layer-memory.md:682-701`) | 1–2 | `**Reuse:**` (`handoff.py:97`) | `symbols`, `callers`, `dossier` (`layer-memory.md:446-448`) | its packet | without the map installed, only reuse entries and a search of scope paths (`layer-library.md:324-325`) |
| architect | the map plus `design.inventory`'s unfolds: legs, checks, keys, populations, markers and kits, 12.3 KB (`project-map.md:594-595`) | 0–1 | `map` | the view | 32 KiB plus unfolds | symbols, callers, tests |
| spec writer | the level-0 map, and the reuse scout's matches | 0 | `map`, `**Reuse:**` | the view | 96 KB | what its unit touches: callers and tests of what it changes |
| builder | no map: its slice, the `refs` rows of its write set, a code-notes slot ≤ 2 KB of annotations (`systems.md:306-310`), gotchas by write set, and P29's excerpts "cut at their anchors" (`layer-roles.md:211`) | 2 | slice, code-notes | annotation index | ≤ 2 KB plus slice | the callers of, and tests for, the symbols it edits; excerpts reach it only where the spec cites anchors (unit 24's spec cites 5) |

- **`map.code`** appears only in `project-map.md:545-547` and in `research-project-map-a.md:148`. No chain row and no slot list declares it. dBoundRoles' generic clause covers "the map's dossiers" only (`v2:1189`).
- **The level-0 map is nearly full.** `map.py --check` reports "2170 nodes in 30 namespaces; 29982 B of 32768 (no degrade)", in 492 ms. That is 2.8 KB of headroom. The record's PM-4 table sized today's map at 13.2–13.7 KB (`project-map.md:736`), so the record and the instrument disagree.

## 4. Candidates

Each candidate's losing test was written before its probe ran.

| | **A. Code record kind, derived, with declared enrichment** | **B. Per-work-order code neighbourhood** | **C. Query only, no stored record** | **D. The design as it stands: `map.code` optional (KN-1)** | **F. Dossiers as the enrichment layer (today)** |
|---|---|---|---|---|---|
| Mechanism | One generated record per tree hash: files, definitions with `[start,end]` ranges and body hashes, imports, resolved edges, cross-language and registry edges, test edges, kit and feature membership. Read at level 1 through `gov map code[.<kit>]` and at level 2 through `gov code show\|callers\|tests`. Level 0 holds one counted line | The executor renders a `code` slot per item from a seed (the write set at Build, scope paths at Design): seed files, their definitions with ranges, inbound and outbound edges, tests, and same-kit siblings, as references with line ranges | `gov code where\|callers <sym>`: `git grep -w` plus `ast` on the files hit, at query time | Core shows kits and features; symbols, callers and dossiers come from the optional kit; the reuse scout alone gets callers | Authored feature prose over path globs |
| Derived | everything structural | everything; it is a projection of A | everything, each time | kit lines only, in core | claims are gated; the prose is not |
| Enriched | a purpose slot per symbol and per file: drawn from the docstring or header first (69.1% and 97.5% derivable), the rest written by an agent, plus `relates=` keys | nothing: it inherits A's purposes | nothing | dossiers, reuse entries | everything |
| Honesty | each slot is keyed to its symbol's body hash, and stale when the hash moves. Joined both ways: every slot resolves to a live symbol, and every symbol with no purpose is in a pending population, as PM-5 does for nodes | the slot is hashed into the work order; freshness compares tree ids, as the map check does | none needed: it is always fresh | dossier staleness by path ancestry | path ancestry |
| Cost | 13.1 s cold and 941 KB uncompressed here; re-parse only changed blobs | the list is 2.9–5.1 KB for 80–139 files; the content those files hold is 9.4–11.7 MB, so the slot hands ranges, not bodies | ~100 ms per query | 0 | authoring time |
| Portability | Python through stdlib `ast`; shell and JS through the map's regex tokenizers; any other language falls to file level plus C | it inherits A's coverage, file level elsewhere | any language, since it works on text | — | any language |
| **Losing test** | (1) cold derivation over 30 s or record over 1 MB; (2) enrichment staleness firing on over 10% of entries a week; (3) a code namespace at level 0 pushing past 32 KiB | not better than its own seed on recall of the feature files the agent then read (procedure tools excluded) | precision on homonyms: its file count for a name more than 3× the resolved callers | any of the seven roles blind to the callers of what its unit changes, with the kit installed | over half its entries stale |
| **Result** | (1) **passes**: 13.1 s, 941 KB. (2) **passes keyed by symbol**: 98 of 2,898 body hashes changed in 7 days, 3.4%. **Loses keyed by file**: 145 of 240 code files touched in 7 days, 60%. (3) **loses at level 0**: file lines estimate 30,361 B against 2.8 KB of headroom, so code stays at level 1 and below | **Spec writer: wins.** Seed 5/20 (25%); 1-hop plus kit 16/20 (80%) in a 5,053 B list. It missed only `tools/gate-lint/*`, the seam it chose to extend, which is the reuse scout's question, not a relation. **Builder: wins as symbols, a rehearsal as a file list.** Seed 11/12 (92%), 1-hop 12/12. Its cost is lookups inside files it already knew: 36 of 56 name a defined symbol | **Loses as the caller source.** `main`: 180 files against 5 resolved; `load_conf`: 35 against 16. **Survives as the floor**: 14 of the builder's 56 lookups are text or pattern searches that no map answers | **Loses**: 6 of 7 roles get no callers (`layer-memory.md:682-686`), and with the kit absent, none does | **Loses**: 25 of 31 stale |

Neither A nor B covers population hunts (unit 24's `mv -f` temp-writer sweep). C stays as the floor for those and for languages with no extractor. A fourth push mechanism, a read hook that injects code relations when a file opens, is the same mechanism as AN-2's hook (`systems.md:558-579`) and has the same measured reach: 3–5% of code reads go through Read. I fold it into AN-2 rather than rank it separately.

## 5. Core and optional

| Part | Today | Proposed under P28 |
|---|---|---|
| Code record: files, definitions with ranges, imports, resolved edges, tests, kit membership | optional (`layer-memory.md:378-381`); its caller map is already built by dTotalRecall (`v2:1190`) | **core**, extracted through the shared primitive in `tools/lib` (LX-2, already in `v2:1190`) |
| Core extractor packs | per language, optional | Python `ast`, shell and JS in core; every other language at file level plus C, with the state declared |
| `code` neighbourhood slot (B) | absent | **core**, dBoundRoles |
| Purpose enrichment keyed by symbol hash | dossiers, keyed by path | **core** workflow; dossiers stay optional, re-anchored to symbol keys as `layer-memory.md:741-744` already plans |
| Owner views `MAP.md` and `CARDS.md`, the reuse digest's ranking, extra language packs | optional | optional |
| `reuse_lookup.py` | live | retire, as `[tools]` says; the probe confirms the result above |

**What happens to `map.code`.** It stops being an optional slot and becomes the core `code` slot. Its three states change meaning:
- **filled**;
- **derived, nothing related**;
- **not extracted for `<language>`**, which names `gov code where` (C) as the fallback.

"Not installed" stays only for the extra packs. `gov tag where` is no longer the fallback for code depth, because it finds tags, not callers. Level 0 gains a single counted line, `- code.* — N nodes · gov map code`, and never one line per file.

## 6. Chain, gaps and forks

**Units by build:**

| Build | Unit to add |
|---|---|
| dTotalRecall | the `code` record kind (replacing optional `symbols` and `callers` as core kinds), derived per blob, cached by tree hash, freshness-checked |
| dTotalRecall | `gov map code[.<kit>]` and `gov code show\|callers\|tests\|where`, with C as `where`'s engine and fallback |
| dTotalRecall | the enrichment workflow: derived-first purposes, the agent's pass for pending symbols, body-hash staleness, the both-ways join and its pending population, each check seen red on a planted case |
| dTotalRecall | the replay losing test, extended to code: unit 24-style recall of files read and the count of lookups, with the slot against without it |
| dBoundRoles | the `code` slot rendered per item from the declared seed, with its states and budget; `[delivery]` extended to the researcher and the prompt writer |
| dDeclaredLoop | each item declares its seed: write set, scope paths, or the question's paths |
| dOrderedCharter | the `memory.code-*` keys, and the slot's share of each role's load set |
| dCalibratedLens | the not-in-view cause reads the `code` slot as well as the map |

**Gaps to register:**

| Gap | Severity | Owner |
|---|---|---|
| no core role but the reuse scout sees the callers or tests of the code its unit changes. Unit 24's spec writer made 80 code lookups and its builder 45 | HIGH | dTotalRecall, dBoundRoles |
| `map.code` is declared in no chain row and no slot list | MED | dBoundRoles |
| the researcher and the prompt writer are absent from the map's delivery table, against the owner's point 3 | MED | dBoundRoles |
| enrichment keyed by file or feature rots: 25 of 31 dossiers are stale, and 60% of files change in a week | MED | dTotalRecall |
| the level-0 map is at 29,982 of 32,768 B, against the record's 13.2–13.7 KB | LOW | dTotalRecall |

**The owner's forks:**

| Fork | Options, the recommendation first |
|---|---|
| CM-1: where code depth lives | **A in core**, partly reversing KN-1; D, kept optional as now; C only |
| CM-2: how code reaches a role | **B pushed per item, plus pull verbs**; pull only; every structural role gets the whole code namespace |
| CM-3: where enrichment lives | **record slots keyed by symbol hash, derived first**; in-code `gov:note` only; none, derived only |
| CM-4: which roles get the `code` slot | **spec writer, builder, researcher, architect, reviewer, and the prompt writer through its actor**; every role; structural roles only |
| CM-5: which languages are in core | **Python, shell and JS, others at file level plus C**; file level only in core; require ctags, which is absent on this node |
| CM-6: the slot's budget | **8 KB, with symbol ranges and never bodies**; 4 KB; 16 KB |

The probe scripts are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/` (`codemap.py`, `nbhd2.py`, `probe_unit.py`, `lookups.py`). Unit 24's spec was read from commit `5b30e4b47` and its build from `73b80ed31`.
