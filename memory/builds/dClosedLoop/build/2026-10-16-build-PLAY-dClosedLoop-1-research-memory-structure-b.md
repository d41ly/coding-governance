# Research: memory structure, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 82's return, verbatim. Its question is in
`prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-26-researcher.md`, which dispatch 81 runs
too, and its use is in `build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`.

---

I've recommended a design: memory keeps its folders, records get tagged sections, and agents read one section through a single read command. Of the four mechanisms I tested, three failed their losing tests. I wrote no file in the repository. Every probe was read-only, and the scripts are in the session scratchpad (`memq.py`, `probe2.py`, `probe3.py`, `dup.py`, `sect.py`, `idx.py`). Byte counts convert to tokens at about 4 bytes per token.

## 1. Verdict

**Keyed sections, pulled through one read command and handed out by the work order.**
- **Where records live:** build folders stay where they are. Records that belong to no build go under `memory/<layer>/<kind>/` (EX-2). The library kinds keep the paths they have now.
- **Sections:** each record kind's schema in the registry declares its sections, each headed by a `[tag]`.
- **Index:** a generated section index, keyed by tree hash and never tracked, builds in 0.44 s.
  - `record find` returns rows only: `id#tag`, kind, bytes, blob, and what supersedes it.
  - `record show id#tag@blob` returns one section.
- **Work orders** hand sections, never paths.
- **Default load** is the charter plus a card of at most 8 KB.
- **Whole-file reads** are allowed but counted against the item.
- **Estimated effect:** an agent's median memory bytes fall from 68.9 KB to about 31 KB, and spec read bytes fall from 54 MB to at most 8 MB per 60 days.

## 2. Today

**What is stored, measured at HEAD with `git ls-files` and `wc -c` per folder:**

| Folder | Files | Bytes | Generated? |
|---|---|---|---|
| `builds/` | 4,018 | 64.2 MB | Only the README regions are generated, in 32 READMEs |
| — `spec/` | 1,322 | 27.3 MB | authored |
| — `reviews/` | 536 | 17.9 MB | authored |
| — `build/` (journals) | 1,185 | 12.6 MB | authored |
| — `prompts/` | 584 | 2.7 MB | rendered or prose |
| — README, RUN, BACKLOG | 167 / 89 / 126 | 1.4 / 1.3 / 0.9 MB | mixed |
| `map/` | 39 | 979 KB | `generated/` holds 611 KB (`symbols.json` alone is 555 KB) |
| `archive/` | 18 | 574 KB | rotated |
| `gotchas/` | 134 | 451 KB | `INDEX.md` (35.5 KB) is generated |
| `guides/` | 10 | 308 KB | authored (`UNATTENDED-VERBS.md` alone is 85.7 KB) |
| `project/` | 20 | 155 KB | waiver registries |
| `backlog/` | 4 | 100 KB | generated views (`TOOL.md` is 91 KB) |
| `ledger/` | 4 | 13 KB | generated |
| Top-level files | 5 | 160 KB | only `LIVE.md` (4.1 KB) is generated |

- **Totals:** 4,252 files and 66.9 MB. About 0.76 MB (1.1%) is generated; the rest is authored.
- **Builds are uneven:** median build 175 KB, p90 795 KB. The two largest, dDerivedDocket and dClosedLoop, are 5.3 MB each.

**Growth**, measured with `git ls-tree -r -l` at a commit on each date:
```
2026-08-15 files=275  3.9MB · 2026-09-01 1066 19.3MB · 2026-10-01 2663 45.9MB
2026-10-08 3281 54.0MB · 2026-10-16 4252 66.9MB
```
That is about 1.6 MB a day over the last 8 days.

**The read path**, measured from files and from transcripts since 2026-08-17 (3,632 transcripts, 2,445 of which touch `memory/`):

| Path | Bytes | Where |
|---|---|---|
| Default load: `AGENTS.md` through `CLAUDE.md` | 16,732 | `CLAUDE.md:1` |
| Default load: auto-memory `MEMORY.md` | 14,005 (82 lines; 81 files, 150 KB) | `~/.claude/projects/C--projects-coding-governance/memory/` |
| Default load: the card, injected at SessionStart | median card file 3,559, p90 6,064 (21 cards) | `.claude/settings.json` SessionStart; `manifest-check.sh --card --write` |
| Conditional: `.claude/rules/product.md` | 3,054 | — |
| Kickoff: `SKILL.md`, the manifest, one recall query, LIVE | 18,310 + 19,626 + 16,226 (median emitted) + 4,079 | `SKILL.md:183-190` |
| Role work order (researcher prompts in dClosedLoop) | median 11.5 KB | `tools/roles/handoff.py:97` (`TASK_FIELDS` includes `reuse`) |
| Memory bytes returned per transcript | median 68.9 KB, p90 227 KB | `memq.py` |

**Where those reads went** (`memq.py`; 242.8 MB returned from `memory/` in total):

| Class | Calls | MB returned | Reads (whole-file) | Search misses |
|---|---|---|---|---|
| `builds/*/spec/` | 20,252 | 128.8 | 2,757 (1,541) | 66 |
| `builds/*/build/` | 6,259 | 29.4 | 807 (188) | 27 |
| `guides` | 5,096 | 18.7 | 420 (252) | 51 |
| `builds/*/reviews/` | 2,796 | 17.5 | 376 (139) | 24 |
| `builds/*/README.md` | 2,237 | 6.8 | 197 (161) | 15 |
| `DECISIONS.md` | 705 | 1.6 | 11 (5) | 13 |

- **Search misses are rare.** 347 of 24,635 searches over memory returned nothing (1.4%). The cost is reading too much, not finding nothing.
- **Agents read whole files and use little of them.** A whole spec read returns a median 21,883 B, 36.5 MB in total; a partial read returns a median 10,691 B. A spec's median section is 715 B, so a section is 0.04 of the file (`sect.py`).
- **What agents read was mostly named in their brief but not handed to them.** 64.7% of subagents' memory reads (3,154 of 4,876) were of paths their prompt named. The memory record's own measure puts handed researchers' reads of content the parent already held at 41.3% (layer-memory `[research]`).

**Recall misses** (`.git/recall/queries.jsonl`):
- 590 queries, each showing a median of 40 hits.
- 133 inferred first reads after a query. Only 33 were of a hit it showed (5.6% of queries); 100 read a file it did not show.
- The cache is 454 MB, untracked.

**Duplication and staleness:**
- **Verbatim duplication is small:** lines of 100 characters or more stated in two or more files are 0.9% of the bytes, mostly the charter rendered into prompts (`dup.py`).
- **Paraphrased facts are the real duplication.** "16 of 24" appears in 11 files and "0 of 24" in 10, and none carries its probe or SHA.
- **drift-audit** (`drift_report.py`, 28.8 s, read-only) reports:
  - `live_builds_without_activity` 21 of 25;
  - `dangling_pointers_in_own_ledger` 10;
  - `run_records_nonterminal_but_merged` 10, over its pin of 2;
  - `dossiers_older_than_their_paths` 25 of 31.
- **The auto-memory names gone paths:** 5 of 42 repository paths it names no longer exist.

**What already serves this system, in code and in the design records:**

| Part | What it does | Where |
|---|---|---|
| Index size caps | indexes, READMEs, dossiers, guides and `BACKLOG.md` are capped; specs, reviews, journals and prompts (74% of read bytes) are not | `check-memory-hygiene.sh:959-1060`; `.memory-tree.conf:483` (61,440) |
| Backlog views | uncapped on purpose, by owner ruling D3 | `check-memory-hygiene.sh:905-910` |
| Key-addressed retrieval that works | `gotchas.py --for-paths` returns 3,606 B in 0.12 s, run 1,084 times in 60 days; `gen_build_index.py --asks --json`, `--live-builds` | `tools/memory-tree/gotchas.py:7` |
| Heading-bounded chunks | recall's chunks arm, which scores 0.00 on its own bench | `tools/memory-recall/extract.py:727` |
| Supersession map | already derived from relations | `extract.py:703` |
| Read hook | `recall-opened.js` on PostToolUse Read, which only observes | `.claude/settings.json:65-71` |
| Settled in the design | the registry, the `record` door, generated views, work order as an agent's root, slug parser | layer-memory `[contract]`, `[build]`, `[views]`, `[names]` |
| Settled in the design | a subagent never re-reads its brief | orientation `[entry]` 4 |
| Settled in the design | the card carries pointers by tag; `card.pointers=every-item` | compaction-results `[conclusions]` 5, `[settled]` |
| Settled in the design | each optional slot renders one of three states | layer-library `[consult]` |

**Where a record and the code disagree:**
- `HYGIENE.md:26` lists `decisions/`, which does not exist.
- `gap-found-14` gives the auto-memory index as 13.2 KB. It is now 14,005 B.
- layer-memory `[current]` counts 1,301 specs. There are now 1,322.

## 3. Across the layers

**What this system needs from each layer, and what it gives it:**

| Layer | Needs | Gives |
|---|---|---|
| instruction | P11: section headings are tags; a derived fact carries its key; the `instructions.edit` door for promoting auto-memory directives | sections of records, handed as level-7 evidence; the tag rows a work order cites |
| flow | each item declares its read set as `id#tag` | the items' records, found by kind, build and tag; `build.distill` and `deploy.distill` rows |
| roles | the work order cut under P29; `roles.answered-calls` | `record show` as the cut's source; reads outside the order are counted |
| memory | owns it | registry section schemas, the index, the verb, the checks |
| runtime | a command-adapter registration for `record find` and `record show`, with an idempotence probe; card pointers | pointers resolved to `id#tag@blob`; load-metric events in the journal |
| observability | nothing; the core never depends on it | journal events (bytes loaded and read per item) for Maintain to trend |
| integrations | nothing | the release records' home `memory/integrations/`, indexed like every kind |
| distribution | install of the verb and its conf; the harness adapter's capability table (can auto-memory be disabled?) | the budget value per adopter |

**What it needs from and gives to the other four systems:**

| System | Needs | Gives |
|---|---|---|
| Tags | one tag grammar and parser for `[section]` and `<layer>.<kind>` | `record find --tag`, and an index row for every tag use in memory |
| Annotations | a `refs=<id#tag>` form in `gov:note` | resolution of `refs=` through the index; the same tree-hash cache pattern |
| Instruction writing | templates rendered from the registry schema, with sections as declared fields | record sections typed by statement type; keyed derived facts |
| Role shapes | a read set and a read allowance per role | per-role slices that cost bytes, not paths |

## 4. Candidates

| | A. Keyed sections + generated index + read verb | B. Push-only slices | C. Ranked retrieval as the read path | D. Age tiers (cold shards) |
|---|---|---|---|---|
| **Mechanism** | Sections tagged by schema; an untracked index of `id#tag`, bytes, blob and supersession; `find` returns rows; `show` returns a section | The executor embeds content in work orders; no read verb; layout unchanged | recall or embeddings choose what to read | Terminal builds and old records move to archive shards outside the default search population |
| **Efficiency** | Spec Read bytes 54 MB → ≤8 MB (≤3 sections of 715 B per read; whole reads kept for editors); agent median 68.9 → ~31 KB | Covers the 64.7% of reads a brief names; the other 35.3% stays as today | 16.2 KB per query; read-through 5.6% | Saves 0.2% of reads and 4.1% of search bytes |
| **Losing test, set beforehand** | (a) The median section/file ratio exceeds 0.25 for the kinds holding ≥50% of read bytes; (b) fewer than 80% of specs carry the template headings; (c) the index takes >5 s | More than 20% of agents' memory reads are of paths the brief did not name | Read-through below 25% of queries | Cold content under 10% of read and search bytes |
| **Result** | **Passes.** spec 0.04, reviews 0.05 (60% of bytes); 1,233–1,317 of 1,322 specs carry each numbered heading; 38,292 rows in 0.44 s | **Loses** as the sole mechanism: 35.3%, 1,722 of 4,876 (`probe2.py`). Kept as A's delivery | **Loses:** 33 of 590, and 100 of 133 first reads went to unshown files | **Loses:** 9 of 3,798 reads cold; 4.1% of grep bytes from builds cold more than 7 days, 4.3% from records more than 30 days old (`probe3.py`) |

- **The undercount in the cold measure.** It uses each build's last commit as of today, so it undercounts cold reads. Even taken at ten times its value, D stays below 10% of read bytes.
- **A digest or summary tier was rejected on the records' evidence.**
  - Agents bypass a root: 77.9% never read the README (layer-memory `[current]`).
  - Summaries drop what matters: compaction kept 1 of 9 numbers and 1 of 7 identifiers (compaction-results `[measured]`).

The index probe (`idx.py`):
```
files 4142 section rows 38292 already [tag]-headed 395 index bytes 4500461 secs 0.44
```

## 5. The pick, specified

**Shape.**
- **Section heading:** `## [<tag>] <title>`, with the tag in the shared tag grammar. The registry declares per kind `sections = [{tag, required, statement-types}]`.
- **Legacy specs:** the template's numbered headings map to tags by a table: `1. Goal` → `goal`, through `10. Reuse` → `reuse-audit`. They are derived and never rewritten.
- **Index row:** `id#tag  kind  layer  build  bytes  blob  tags  superseded-by  lifecycle`.
  - It lives at `.git/gov/index/<tree-hash>.tsv`, untracked and rebuilt when the key misses. It is never loaded whole (4.5 MB); only the verb reads it.
- **Verbs** extend the `record` door, which is P30's writer:
  - `record find --kind/--tag/--build/--paths [--all]` returns at most 40 rows and no content. Superseded rows are hidden by default.
  - `record show <id>#<tag>[@blob]` returns the section bytes and its key.
  - `gotchas.py --for-paths` becomes `find --kind bug-class --paths`.
- **Homes:**
  - the trail stays at `memory/builds/<slug>/`;
  - records no build owns go to `memory/<layer>/<kind>/` (EX-2);
  - `DECISIONS.md`, `gotchas/` and `map/` are declared as homes at their current paths.

**Who owns it.** The memory layer, and the chain build dTotalRecall, through memory-tree, its core engine. dBoundRoles renders the slices into work orders, and dOrderedCharter owns the auto-memory promotion.

**Records and kits.**
- It adds no tracked record kind. The index is a generated, untracked kind with its generator as its door.
- The registry gains a `sections` field per kind.
- The kit is memory-tree. `gotchas.py` and `gen_build_index.py --asks --json` are the seams it extends.

**Checks** (each must be seen red first, per HYGIENE rule 5 on non-empty populations):

| Check | Turns red when |
|---|---|
| `memory.sections` | a record of a registered kind, written after its cutoff, lacks a required `[tag]` or repeats one (plant a spec with `## Goal`) |
| `memory.cites-resolve` | an `id#tag` in a work order or a current-state record does not resolve at its blob (plant `#nosuch`). Append-only records are checked at write |
| `memory.load-budget` | the SessionStart memory output (card plus any memory injection) is over `memory.load-budget` (pad the card to 9 KB) |
| `memory.find-current` | `find` returns a superseded row without `--all` (plant a `supersedes` edge) |
| `memory.index-fresh` | a served row's blob differs from HEAD's (edit a section and query again) |

**Read-path cost:**

| Path | Today | Pick | Method |
|---|---|---|---|
| Memory's share of default load | card ~3.6 KB + auto-memory 14.0 KB | card ≤8 KB; auto-memory per F3 | measured; budget from the card's p90 (6.1 KB) and max (7.8 KB) |
| Kickoff prior-records lookup | 16.2 KB per recall query | ≤40 rows × ~120 B ≈ 4.8 KB | row width from `idx.py` |
| Agent memory bytes, median | 68.9 KB | ~31 KB | the 64.7% named reads become handed sections at a ratio of about 0.15; the 35.3% unnamed stay as they are |
| Checks | drift-audit 28.8 s | index 0.44 s; each check under 1 s | measured / estimated |

**The test the build must run.** Re-run `memq.py` 30 days after landing. The pick loses if the median memory bytes per agent transcript are not below 40 KB.

## 6. Items and policies

**Items.**

| Tag | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `record.write` (fills P30's door) | command | refuses a registered kind without its tagged sections | the `memory.sections` verdict at the commit | refusal returns the missing tags to the writer |
| work-order cut (fills dBoundRoles' cut) | executor | hands `id#tag@blob` sections, not paths | every handed fact carries its key, and `cites-resolve` is green | an unresolved cite blocks the spawn and routes to `next` |
| `deploy.distill` (existing) | command | appends the decision rows | as settled | as settled |

`record find` and `record show` change no state, so they are not items. They register as command adapters, with a re-render as their idempotence probe.

**Policy keys.**

| Key | Allowed | Default | Why |
|---|---|---|---|
| `memory.read-path` | `sections`, `files`, `refuse-whole` | `sections` | 56% of spec reads are whole-file at 21.9 KB against a 715 B section; `refuse-whole` is for strict |
| `memory.default-load` | `card`, `card-and-live` | `card` | `LIVE.md` is the owner's view; agents get it through `next` |
| `memory.load-budget` | `4k`, `8k`, `16k` | `8k` | the card's p90 is 6.1 KB and its max 7.8 KB, and `card.pointers=every-item` grows it |
| `memory.legacy-sections` | `derive`, `whole-file` | `derive` | 93–99.6% of specs carry the template's headings |
| `memory.find-superseded` | `hide`, `show` | `hide` | 47 decision rows chain supersessions |

## 7. Gaps

**Closed by the pick:**
- `gap-mem-05`, routing by purpose: `find` replaces README routing for agents.
- `gap-mem-15`, no research view: `find --kind research-return` is its core query.
- `gap-orient-07`, in part: briefs carry keyed sections instead of pointers.
- `gap-orient-10`, in part: `cites-resolve` covers memory's own pointers, but not the harness's auto-memory.
- `gap-mem-01`, in part: the registry gains its `sections` field.

**New gaps it exposes:**
- **MED: no read path or read budget.**
  - 1,541 whole-file spec reads; 0 spec headings tagged; 395 tagged headings across 38,292 sections.
  - Size caps miss specs, reviews, journals and prompts, which are 74% of read bytes (`check-memory-hygiene.sh:959-1060`).
  - Nothing measures default load: the auto-memory index grew from 13.2 KB to 14.0 KB unchecked.
- **LOW: measured facts are restated without a key.** "16 of 24" appears in 11 files and "0 of 24" in 10, so a stale copy cannot be found. The fix is that a derived fact cites `id#tag`, through the instruction writing system.
- **LOW (extends `gap-mem-11`):** `HYGIENE.md:26,52,195` names a `decisions/` folder that does not exist.

## 8. Forks

These need your decision:

- **F1. Library homes.**
  - Options: keep `DECISIONS.md`, `gotchas/` and `map/` at their paths as declared homes; or move them to `memory/memory/<kind>/` as EX-2 reads literally.
  - **Recommend: keep them.** The decision log has 32 code readers, and gotchas are cited in 276 reviews and 523 commit lines.
- **F2. Legacy records.**
  - Options: derive tags from the numbered headings; rewrite 1,322 specs once; or leave legacy records read whole.
  - **Recommend: derive.**
- **F3. The harness's auto-memory (14.0 KB loaded every session).**
  - Options:
    - promote its standing directives through `instructions.edit`, then hold it to the load budget;
    - disable it where the harness adapter can;
    - leave it as it is.
  - **Recommend: promote, then budget.** This is your own memory, and `gap-found-14` already sits with dOrderedCharter.
- **F4. Whole-file reads.**
  - Options: counted, which is `sections`; or refused for registered kinds, which is `refuse-whole`.
  - **Recommend: counted**, with refusal reserved for the strict preset.

**Files:**
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\check-memory-hygiene.sh`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\gotchas.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\handoff.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\HYGIENE.md`
- Probe scripts are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\`
