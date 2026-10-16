# Layer review: the memory layer

**Serves:** research PLAY-dClosedLoop-1

The fourth round of the owner's layer-by-layer review: the memory layer. Five researchers measure its
parts in parallel, dispatches 22 to 26. Their returns are saved verbatim beside this record, and the
design that answers the owner is written here once they return.

The same message opened with a note on the roles layer's mechanical shape. It is recorded with that
layer, in `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md` (`[owner-notes]`).

## [words] The owner's words, 2026-10-15

> Let's review the Memory (Build) Layer now:
> [4. Memory Layer]
>
> * Memory layer contains and manages all development lifecycle memory about a project/repo/codebase.
> * Memory layer needs an extensive definition of its own conventions to ensure consistent practices
>   across all of its moving parts: the layer itself consists of several pieces (builds, backlog,
>   decisions, codebase map, reuse, code annotations/commentary, other tool extensions).
> * Memory layer is complex as it's involved across all agent workflows and intended to provide human
>   owner orientation at a glance through readability.
> * Gov is 'Build' centric - a build is a memory 'unit' that contains structured, templated
>   prompt/plan/design/spec/etc. records that along with the 1. Instruction layer shape written
>   product code. They are structured in a tree-like manner to eliminate automatic read-path
>   inflation for agents - agents should not automatically ingest every build document and artifact
>   past the build's root README unless necessary.
> * Builds are identified by their slug which is a combination of work node identifier + 1-3 words in
>   CamelCase summing up to a humorous ID. Humorous build IDs are a foundation of the product, but
>   naming convention as well as additional build slug properties (such a DATE) are owner-adjustable.
> * Builds maintain clear relations to one another - dependencies, that allow tracing feature
>   relations, patches and amendments.
> * Backlog is part of memory that allows tracking of surfaced work that's not been turned into builds
>   yet.
> * Codebase-map toolkit is supposed to provide a mechanical, generated view of the each codebase
>   functions, classes, methods, subroutines, procedures, their relations and caller map. The purpose
>   is to speed up codebase orientations and see all relations at a glance. Unfortunately, the
>   toolkit is not well developed at the moment and is underutilitized: some languages and features
>   are invisible to the kit, relations and callers aren't tracked.
> * Decision index doesn't currently serve its intended function and is broken - agents record every
>   miniscule decision to this index, often without any logic. Originally, intention was to use this
>   index as a way to keep track of MAJOR product decisions and implemented features, ensure reuse,
>   and encourage systemic design. For example: a modal media gallery picker was built in inCMS,
>   which is a major feature - a decision log entry for this feature would include a date, the build
>   slug (id), code tag references, brief feature description and an INSTRUCTION (with an appropriate
>   ranking) for the reading agent to REUSE THIS FEATURE anywhere an image/video/media selector is
>   needed, integrating existing functionality instead of reinventing it. Another example, screen
>   reader support was implemented in inCMS, and a decision record pointing to its convention and
>   instructions to ensure every new page supports screen reading would be recorded in the index.
> * Reuse tools (memory recall, reuse lookup) are currently broken - they do not surface the right
>   features when queried (aScoutedSeam tested reuse lookup and it was unable to solve any test
>   cases). These tools need to be either redesigned under the new memory conventions or retired if
>   they serve no meaningful purpose.
> * Code commentary/annotations are ALSO part of the memory layer and must be brought in scope -
>   reading code annotations is a major orientation point for agents and must be used as such,
>   following the universal memory+instruction layers' conventions - tags, short and clear
>   descriptions, action pointers, references, build ids.
> * Current tooling must be fully mapped to work with the new architecture of the product. What tools
>   it makes sense to keep? Which tools need to be re-engineered? What should be retired to declutter
>   the repo?
> * Every memory practice needs to be templated and deterministic.

## [settled] What the design already fixes

- **The layers** (layers round one):
  - Memory is a core layer, meaning the build trail.
  - Knowledge is an expansion. It holds:
    - the codebase map and the reuse lookup;
    - decisions, through memory-recall;
    - the gotchas;
    - the lexicon;
    - research records.
  - The owner's memory layer spans both: the core trail, and the Knowledge expansion's stores. The
    core never depends on Knowledge (P28).
  - **Revised 2026-10-16, KN-1** (`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`): Knowledge folds into this layer.
    The layer is the trail and the library: major decisions, reuse entries, bug classes and research.
    The codebase-map, memory-recall and lexicon kits are its optional components, under P28.
- **Records are evidence, at level 7 of the ladder.** The charter's `[memory]` rule keeps recalled
  memory from instructing. `gap-found-14` (HIGH, dOrderedCharter) already records that the auto-memory
  index instructs outside the ladder. The layers round left the gap's home to this review.
- **The card** (orientation round, adopted from dispatch 15):
  - Its truth is a ref per build on the shared remote.
  - The clone's `.git/orientation/` holds a cache of it.
  - The build folder holds a snapshot at the build's terminal transition.
- **Position lives only in witnessed state.** `next` derives a build's position from its records.
  Typed status words, README status, session logs and auto-memory are evidence only (orientation
  `[trust]`).
- **Records travel; roles do not** (flow-roles `[records]`). A build moves because its records
  accumulate, from the intake record to the landing record. P29 makes those records the keyed sources
  of every handed fact.
- **The ask register is core memory** (step definitions `[open]`):
  - Core flow items file asks.
  - Plan's triage selects an ask into a build, or retires it.
  - The register's generated index, rotation and labels may stay optional.
- **Kits:**
  - memory-tree is the memory layer's core engine. Its backlog, rotation and gotchas were left to
    this review.
  - codebase-map, lexicon and memory-recall belong to Knowledge, and since KN-1 they are this layer's
    optional components.
- **Gaps already registered that touch memory:**

  | Gap | What it records |
  |---|---|
  | `gap-plan-02` | unlabelled asks |
  | `gap-plan-06` | asks not ready to build |
  | `gap-design-01` | the map is an inventory |
  | `gap-design-05` | reuse audits are unchecked |
  | `gap-design-07` | the reuse stage is unrecorded |
  | `gap-maint-04` | records dominate the commits |
  | `gap-maint-05` | run records never close |
  | `gap-maint-06` | the map goes stale |
  | `gap-maint-08` | lexicon and ledger signals are report-only |
  | `gap-found-14` | memory instructs outside the ladder |

## [research] Dispatched, 2026-10-15

| # | Part | Handoff |
|---|---|---|
| 22 | builds: anatomy, read path, slug, relations, determinism | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-3-researcher.md` |
| 23 | the ask register and the decision index | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-4-researcher.md` |
| 24 | the codebase map and the reuse tools | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-5-researcher.md` |
| 25 | code annotations, the gotchas and the lexicon | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-6-researcher.md` |
| 26 | the tooling map: keep, re-engineer or retire | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-7-researcher.md` |

- **Briefs that hand their facts.** Each brief hands the settled facts and measured sizes as content,
  marked as settled. It tells the researcher not to re-derive them, and not to read the dClosedLoop
  design records. This is P29 applied by hand, before its mechanism exists.
- **Measured afterwards.** `role_orientation.py` (layer-roles `[instrument]`) measures these five
  agents against the roles round's baseline.
- **At the cap.** Five is the direct-spawn budget per owner turn (`tools/hooks/agent-cap.js`), so
  this round has no sixth researcher.

### Returned, 2026-10-15

| # | Part | Return | Wall | Out |
|---|---|---|---|---|
| 22 | builds | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md` | 10m58s | 39.4k |
| 23 | the ask register and the decision index | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-asks-decisions.md` | 7m05s | 39.7k |
| 24 | the codebase map and the reuse tools | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-map-reuse.md` | 6m23s | 27.9k |
| 25 | code annotations, the gotchas and the lexicon | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-annotations.md` | 6m32s | 29.0k |
| 26 | the tooling map | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` | 7m55s | 33.0k |

Their probe scripts, which they cited from scratch paths, are kept in
`build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-instruments.md`.

**The briefs that handed their facts, measured.** `ro_compare.py` (`[instrument]`) reads these five
researchers through `role_orientation.py`'s classes, unchanged, beside every earlier researcher:

| group | agents | calls | calls/agent | state % | locate % | method % | orient bytes % | parent-had % of reads | reads of dClosedLoop records |
|---|---|---|---|---|---|---|---|---|---|
| handed (22-26) | 5 | 245 | 49.0 | 2.4 | 15.9 | 13.9 | 38.5 | 41.3 | 0 |
| earlier researchers | 21 | 692 | 33.0 | 1.0 | 12.1 | 19.7 | 30.2 | 25.8 | 24 |

- **Where the brief was explicit, it held.** "Do not read the dClosedLoop design records" was obeyed:
  0 reads, where earlier researchers made 24.
- **The path classes cannot judge this round.** Its subject is memory itself, so `LIVE.md`, the
  READMEs and the guides were the task's content. That is why locate, method and parent-had read
  higher here.
- **For dBoundRoles' acceptance (R3-F),** the measure is therefore the answered call: a read the work
  order already holds. A path class is not enough, and the layer-roles record now says so.

## [current] What the layer holds and does, measured 2026-10-15

**Builds** (dispatch 22):
- **The folders** hold:

  | Kind | Count | Median size | Template |
  |---|---|---|---|
  | READMEs | 167 | 6.5 KB | none |
  | specs | 1,301, in 163 builds | 16.8 KB (p90 40.8 KB) | yes |
  | journals under `build/` | 1,048 | — | none |
  | prompts | 565 | — | rendered handoff; only 30 carry its marker |
  | reviews | 517 | 30.2 KB | none |
  | `BACKLOG.md` | 126 | — | — |
  | `RUN.md` | 89 | — | — |
- **Reads go past the README.** 96.4% of build-folder Read calls go past it, and 99.0% of the
  bytes. 77.9% of agent-build pairs never read the README. Specs take 72.6% of the reads.
- **Routing.** The README routes only to specs, and records route only through spec regions.
- **Slugs.** All 173 slugs have two words. The rule is prose ("adjective-noun", `HYGIENE.md:175`),
  where the owner says one to three.
- **Slug readers.** At least eleven readers in seven kits each spell their own slug pattern. A digit
  date in a slug breaks 6 of them, and a hyphenated date breaks 10. The one setting that exists,
  `BUILD_SLUG_RE`, reaches 1 reader.
- **Relations** are one untyped field, `parents:`, used by 11 builds for 13 edges:
  - nothing types a patch, an amendment or a supersession, and supersession lives in prose in 110
    builds;
  - no unit edge crosses builds;
  - nothing checks for cycles.
- **Front matter is open-world.** A misspelled `parent:` is accepted silently. `node`, `roster` and
  `streams` are derivable in 167, 162 and 151 of 167 READMEs.

**The ask register and the decision index** (dispatch 23):
- **The ask register works** and is derived. It has a row grammar, disposition verbs, an order-free
  fold into status, severity rows and READY grading.
- **Its counts:** 859 asks, 521 of them live. 435 of the live asks are unlabelled, and 360 are 31 to
  60 days old.
- **Missing acceptance.** 132 OPEN asks lack an acceptance, most of them filed before `ASK_CUTOFF`
  (2026-10-01). Since then, backlog.py's V14 refuses an ask filed without `accept` or a `seen … run`
  (owner ruling D12-d, dDerivedDocket), red through hygiene check 9. READY rule R5 grades the older
  rows.
- **Parked asks.** 297 DEFERRED asks are parked on one owner-triage ask.
- **The decision index:** `memory/DECISIONS.md` holds 200 rows. Classified by one rater against a
  stated rubric:

  | Class | Rows |
  |---|---|
  | owner rulings | 47 |
  | process and tooling rules | 58 |
  | minor choices and findings | 52 |
  | waivers | 15 |
  | major product decisions | 12 |
  | features and conventions others must reuse | 16 |
- **Against the owner's intent:** only the last two classes match it, 28 rows (14%).
  - No row carries a reuse instruction (0 of 200).
  - Nothing requires a row.
  - Recall opened the file 0 times in 121 opens.
  - 47 rows chain a supersession or a narrowing.
  - 79 rows sit within 20 characters of the 300-character cap.
- **The dossier seam.** Every dossier (31 of 31) carries `## Shared seams`. 12 of the 28 matching rows
  are already cited in a dossier.

**The codebase map and the reuse tools** (dispatch 24):
- **The map stores definitions only:**
  - Python's public module-level functions and classes under `tools/`, 75.5% of its definitions
    (methods, nested and private functions are missing);
  - shell's public functions, about 97%;
  - JavaScript's, about 100%;
  - no symbols for Markdown, TOML or JSON.
- **No callers.** It has 0 caller edges. Its "fan-in" counts files that mention a name.
- **A caller map is feasible on the stdlib.** A probe with the stdlib and the lexicon kit's existing
  tokenizers built an import-aware Python call graph: 2,857 resolved edges, with 11 ambiguous sites
  out of 1,997 import-resolvable ones. It left 21,588 attribute and method calls unresolved. The
  name-only probe over all three languages took 7.8 seconds, and the import-aware Python pass 4.4.
  - Shell and JavaScript are 45% and 46% ambiguous by name alone.
  - 1,012 sites invoke a repository script across languages.
- **`reuse_lookup.py`** ranks by shared name stems, then by mentions:
  - its top answers were test helpers;
  - it shows a median of 110 candidates, and never none;
  - it solved 0 of 24 cases in aScoutedSeam's benchmark.
- **memory-recall** indexes memory Markdown and no code.
  - Its records arm scores 0.83 at r@5 on its 12-query bench, and its chunks arm scores 0.00.
  - 29 of 530 queries (5.5%) were followed by a read of a hit it showed.

**Code annotations, the gotchas and the lexicon** (dispatch 25):
- **Comments are a load point.** Full-line comments are 35.3% of the code's bytes, and agents made
  2,866 code reads in 60 days.
- **What comments carry:**
  - build or record ids, in 7.1% of comment lines: 1,121 distinct ids, 0 dangling;
  - tags: none;
  - `gov:` markers on 164 lines, read by four gates.
- **The style guide refuses** a grammar, a marker and a gate by design (`ANNOTATION-STYLE.md`, A1).
  Agents read it once in 60 days. An agent followed a cited id to its record within 3 calls 2.5% of
  the time.
- **The refusal's reason** (aKeyedAnnotation's design pass, 2026-09-05): drift-audit reads
  source-cited unit ids as evidence that a unit shipped. That signal discriminates only because
  citation is sparse and late, so a mandate would break it.
- **The gotchas earn their keep.** 276 of 517 review files cite a gotcha, as do 523 commit lines.
  Agents ran `--for-diff` 747 times in 60 days.
- **The lexicon is used** (1,277 runs), but its gate absorbs debt. `VERB_OFFENDER_PIN` rose from 412
  to 1,087, with one real drain in 60 days.

**The tooling** (dispatch 26):
- **The population:** 17 kits with a `kit.toml` (govkit and lib carry none); 14 top-level check
  scripts, with their 14 test suites, `check-wiring.sh` and one fragment, 14 of them run as legs; 9
  Skills; and 140 gate legs.
- **Seven overlaps:**
  1. gate legs are declared twice, and 81 exist only in `gate-legs.json`;
  2. wiring is judged three ways;
  3. hooks are spread over five kits;
  4. version lockstep is checked four ways;
  5. a dangling-path test is implemented twice;
  6. 73 files carry inline copies of `resolve_python`;
  7. the flow's step order lives in `unattended.sh` and in `roles/workflows.toml`.
- **Dead or undogfooded:**
  - the deploy-governance Skill has no reader and 0 loads, and repeats govkit's verbs;
  - pytest-parallel-guardrails has 0 runs and one held leg, though gov dogfoods every kit it ships;
  - `reuse_lookup.py`, as above.

## [fit] The owner's layer against the design

| The owner's point | Today | This round's answer |
|---|---|---|
| All lifecycle memory | the core trail plus Knowledge's stores, with conventions spread over `HYGIENE.md` (58.5 KB), the spec template, the guides and 21 memory-tree legs | one memory contract over both, sorted into the trail, the library and the optional components by P28, after KN-1 (`[contract]`) |
| An extensive definition of its conventions | no single declaration | the record-kind registry (`[contract]`) |
| Every workflow uses it; the owner orients at a glance | some views generated (`LIVE.md`, README regions, `MAP.md`) | every view generated, while agents get handed fields (`[views]`) |
| Build-centric, a tree, no read-path inflation | 96.4% of reads past the README, 77.9% never reading it | the work order is the agent's root and the README the owner's (`[build]`) |
| Humorous slugs; naming and date owner-adjustable | 173 two-word slugs, eleven readers each with its own pattern | the slug grammar as policy values, read from one parser (`[names]`) |
| Relations: dependencies, patches, amendments | `parents:` only, untyped | typed relations, inverted and checked both ways (`[relations]`) |
| The backlog | a working, derived register; acceptance optional | the grammar kept; acceptance at filing (`[asks]`) |
| The codebase map: symbols, relations, callers | definitions only, 0 callers | generated symbols and callers on the stdlib (`[map]`) |
| Decisions: major ones, with a ranked reuse instruction | 14% of rows fit, 0 instruct, none read | decisions split by kind; reuse entries as ranked instruction units, rendered into work orders (`[decisions]`) |
| Reuse tools | lookup 0 of 24; recall rarely read through | the lookup retired; the reuse scout reads a generated house index; recall narrowed (`[reuse]`) |
| Code annotations | ids but no tags, no grammar, no index | a `gov:note` grammar, `gov:feature` anchors and a generated index (`[annotations]`) |
| The tooling map | 19 kits, 30 checks, 9 Skills, 7 overlaps | keep, re-engineer or retire, each with its deciding fact (`[tools]`) |
| Templated and deterministic | specs and handoffs templated; reviews, journals and most prompts free prose | every kind templated, written by one command, checked both ways (`[determinism]`) |

## [design] The memory layer, as proposed

### [contract] One memory contract: every record kind declared once

The memory layer fills P28's layer contract with a **record-kind registry**. Each kind is declared
once, with:
- **identity:** its tag (`record.<kind>`) and its layer, core or the expansion that owns it;
- **home:** a path, or a ref (the card's truth, leases and the mailbox live on refs), with its name
  grammar and its id rule, ids minted, never typed;
- **schema:** its fields, their types, and which are required. Its template is rendered from the
  schema;
- **writer and readers:** the item or command that writes it, and the items whose work orders hand
  its fields;
- **lifecycle:** append-only, current-state (edited in place), or frozen at a transition;
- **check:** generated from the schema, and run both ways. Every reference in a current-state
  record resolves, and every declared inverse exists. An append-only or frozen record's references are
  checked when it is written, never after, since a path it names may later be deleted, as the
  dead-path gate already rules.

One write command, `record`, is the only writer of authored record structure, as R-I's command is
for instructions:
- it mints the id under a claim or a lease. A build's slug is claimed first, by the flow's
  `entry.claim`: a compare-and-swap push that creates `refs/gov/claims/<slug>` on the remote, the way
  unattended claims `refs/gov/runs/<slug>`. `check_slug_claimed` is only its local pre-check, since
  it reads the local clone. The records a build writes before its lease (dupes, triage, plan) mint
  under that claim, and every later one under the build's lease, taken at `plan.lease`, or at
  `entry.claim` for a patch build. The intake record mints nothing: it is keyed by its session and
  content. An ask that `entry.place` files outside any build mints under its family's claim ref,
  created the same compare-and-swap way. dTotalRecall owes both refs (`gap-mem-13`). A slug's claim
  ref is never pruned, so a slug is minted once; the supervisor prunes run claims only. So two clones
  never mint one id, and the charter's `[ids]` rule holds: the session that owns an id mints it;
- it is idempotent and content-addressed: a write is keyed by its kind's key, an id or a content key
  such as a return's task-sha. Replaying an equal write is a no-op. A different value under an
  existing key is refused, or versioned where the kind's lifecycle says so. Runtime's take-over
  reconcile relies on this (layer-runtime);
- it renders the template;
- it refuses an invalid value at the write boundary.

It extends the writers that exist: `gen_build_index.py --new-build` (the slug grammar, its collision
check and the README) and `--new-spec` (the spec skeleton with every cutoff's shapes), and runlog's
`RECORD_SCHEMA`, whose renderer and `check-records` leg already make the run record a schema-as-data
kind.

Each kind has one door, and the registry names it. A generated kind, such as symbols, callers, the
annotation index, the recall index or a view, is written by its generator and checked against a
re-render. A reuse entry is an instruction unit, so its door is the instruction command, and the
registry does not list it (LR-6).

Agents supply field values. `HYGIENE.md` is already rendered, by `adopt-memory-tree.sh --render` from
`HYGIENE.template.md` under its `gov:kit memory-tree@` carrier, and the registry becomes that render's
source. Its schema checks become generated checks. Its history, size-cap and grandfather checks stay
authored, each registered against the kinds it grades. Every check carries a tag, and today's number
stays its alias, never reused, since comments, gotchas and guides cite them.

**The population before the registry.** A kind's schema binds records written after its registration
cutoff, as V14's `ASK_CUTOFF` does for asks. Older records keep their form and the checks they were
written under: the 167 READMEs, the 535 free-prose prompts, the 517 reviews, the 1,048 journals, and
the asks filed without an acceptance. A front-matter key outside the derived set stays readable, never
refused.

**Across nodes.** Authored row stores, such as reuse-entry parts, the decision log and relations, are
reconciled additively at merge. Generated stores and views are re-rendered after a merge, never merged
(the charter's `[reconcile]`). Each new store registers in `--dispatch`'s write-set conditions: an
authored shared one under `SHARED_RECORDS`, a generated one under `GENERATED_INDEXES`.

Each layer's contract registers its own kinds, so the list below is the memory layer's, not a closed
set. The kinds sort by P28:
- **Core:** intake, card, plan, seams, feature design, spec, research return, design record, review,
  ask, the backlog row,
  the run record (`RUN.md`), work order, decision (each resolved fork's, its class declared, a major one
  becoming a log row), and one witness record per witness the flow
  declares (acceptance, verdict, attribution, transition, landing among them). Flow registers its
  flake, dupes and scope records. Runtime registers its return, act (launch, epoch, outcome), lease,
  session binding, mailbox message and journal records.
- **Optional components** (KN-1; Knowledge's before it): dossier, symbols and callers, with the map; the
  lexicon; the recall index. The gotcha kind is core since KN-1, on the library side. The annotation
  index stays with the map and drift-audit, and the core reads `gov:feature` anchors by a one-marker
  scan (LB-4, layer-library `[placements]`).

**One refinement to layers round one,** for research records and major decisions alike. Core items
write them (`plan.research`, `design.research`, and each build's decisions as it makes them), so their
kinds are core. Knowledge holds the consulting: memory-recall over decisions, and the research library
across builds. v2's `[layers]` carries it. Since KN-1 the consulting is this layer's own: recall is an
optional component, and the research library is the library side.

### [build] The build: one root for the owner, one for each agent

- **The README stays the build's root for the owner and for the orientation scout.**
  - Its front matter gains a declared schema, dispatch 22's pick D. Unknown keys are refused.
    `node`, `roster` and `streams` become derived, since nearly every README already matches the
    derivation. They leave the front matter: the generated region renders them, and the schema
    refuses them typed. Where 16 READMEs disagree with the derivation for `streams`, the derivation
    wins at the cutover, each change listed.
  - A generated routing region sends a reader to a record by purpose: the plan, each unit's spec,
    the reviews, the open asks, the card.
- **An agent's root is its work order.**
  - Under P29 the executor cuts each work order from the build's records, with its facts keyed.
  - An agent reads past it only for what its own work produces from.
  - A re-read of handed content is an answered call, refused by `roles.answered-calls`.

  This is how "no automatic ingestion past the root" holds for agents: they are never sent to the
  folder at all. Asked as F4-5, since it reads the owner's words for agents differently.
- **Bodies get templates from their kinds:**
  - a review's body is the synthesizer's typed return;
  - each journal record is the record its flow item writes;
  - every prompt is a rendered work order.

### [names] Slugs and names

- **The grammar is policy values, read from one parser.** The id grammar is already single-sourced:
  memory-recall's `extract.grammar_for`, imported by memory-tree (`backlog.py`, `corpus_ids.py`) and by
  drift-audit. The core needs it without memory-recall, an optional component (P28; KN-1), so the parser moves into memory-tree, the
  core engine, and memory-recall imports it from there. The slug grammar joins that parser:
  - `builds.slug-words`, 1 to 3 by the owner's words;
  - `builds.slug-style`, humorous, which is the product's foundation;
  - `builds.slug-date`, `none` by F4-7, with `shown` and `in-slug` allowed.

  Every slug and id reader then reads the parser. `BUILD_SLUG_RE` in `.memory-tree.conf` becomes
  derived from the `builds.slug-*` keys, so the slug grammar has one carrier, and check 4, its one
  reader, reads the parser.
- **The test that prices it** is dispatch 22's. Flip the grammar in a scratch clone and run every
  reader. Each must turn green.
  - The population is a predicate over the tree: every tracked file that matches a slug or id pattern,
    found by the parser's own search, not the enumerated eleven readers.
  - The flips are named: `slug-words` 1 and 3, `slug-style` `descriptive`, and `slug-date` `shown`, and
    `in-slug` in both a digit and a hyphenated form.
- **A changed grammar binds new mints only.** Existing slugs and ids keep their form, every reader
  accepts both, and the grammar in force at minting is recorded with each slug.
- **The date.** Under `shown`, a date is rendered from `opened:` beside the slug in every view, never
  inside an id, so no id parser changes. Under `in-slug`, it costs the six to ten readers that break
  today, until all of them read the one grammar. The default, `none`, renders no date.
- **The record command mints the slug.** It checks the grammar and collisions, so a slug is never
  typed. The style is the minting source, not a property a parser checks: `humorous` mints from the
  kit's word lists, and `descriptive` from the plan record's title. The minting record names its
  source, which is what a check reads.

### [relations] Typed relations between builds

| Relation | Means | Inverse rendered in the target |
|---|---|---|
| `depends-on <slug>` | today's `parents:`, kept as an alias | depended on by |
| `patches <unit-id>` | a patch build's target unit | patched by |
| `amends <unit-id>` | a new unit, in another build, that changes a built unit's behaviour; the built spec stays frozen (P19) | amended by |
| `supersedes <slug>` | P20's superseded ending | superseded by |
| `implements <reuse-entry>` | a build that creates or changes a feature or convention | implemented by |

- **Checks:** every relation's target must exist, and `depends-on` must form no cycle. Unit edges may
  cross builds. A target on another node's unlanded branch resolves through the remote's refs, the
  build's card and lease refs. A target found nowhere is pending, not red, until its build lands or is
  withdrawn.
- **`implements <reuse-entry>`** is a core relation since KN-1: reuse entries are the library side, so
  every install has all five.
- **Views:** the generated graph feeds the plan view, so a feature can be traced from the build that
  made it, through its patches and amendments, to its current entry.

### [asks] The ask register

- **Kept as the core kind it already is:** the row grammar, the disposition verbs, the order-free fold,
  severity rows and READY grading.
- **One change: an acceptance at filing** (F4-6, LR-5). A core filer states one mechanically:
  - a red: a later green of the same leg;
  - an unverified finding: a review round that rules on it;
  - a stray: the path claimed or reverted;
  - a repair: the producer's record corrected;
  - a deferral: triage selects or retires it;
  - a lander refusal: `--prepare` next succeeds for the build;
  - a carried commit: its build claims it;
  - an adapter fault: the adapter's next run passes;
  - a held flaky leg: the leg green on as many consecutive runs as `verdict.flakes`' threshold,
    which the runner records in the flake record (`gap-test-04`), or its manifest row changed.
    `test.flakes` files it under `quarantine`; the runs come as `verdict.held` schedules held legs, or
    on demand by whoever takes the ask;
  - an unrun test level: its first green run, once observability's Maintain runs it;
  - a confirmed finding filed below `review.findings`' threshold: its unit is built, or a review round
    rules it out.

  These are the core filers' whole set (LR-7). An item that files an ask names its form, and a new core
  ask kind adds its form here first. Every other filer, whether the owner, a surfaced idea, an expansion or the supervisor on a role's
  behalf, states an `accept` line, and the ask's closing must cite it. Filing without either is
  refused. backlog.py's V14 already refuses an ask filed since `ASK_CUTOFF` without `accept` or a
  `seen … run` (owner ruling D12-d), so dTotalRecall extends V14 rather than building a refusal.
- **A refused ask is not lost.** The refusal returns to the filer with the forms it may state. An item
  that cannot file routes as any refusal does: `next` returns its frontier.
- **Labels, family views and rotation stay optional bookkeeping.**
- **The parked asks are triage's.** Draining 297 parked asks is Plan's job (`gap-plan-02`, dRankedPlan).

### [decisions] Decisions, split by what each one is

The owner's intended entry, "a decision with an INSTRUCTION, with an appropriate ranking", is two
records. Neither may instruct by being recalled.

1. **A reuse entry is an instruction unit.**
   - **Kind and placement:** level 3, kind `reuse`. Its statement type is a directive: MUST, with its
     trigger as its condition (instruction R-D). Its rank among entries is the owner's ranking, a
     field. It carries a policy tag, so the owner can switch it.
   - **Fields:**
     - the feature's tag;
     - the needs that trigger it, as tags or phrases, such as "media selection" or "a new page";
     - its code anchors (`[annotations]`);
     - its date;
     - the build that made it;
     - the decision that created it.
   - **Home:** a part of the adopter's instruction manifest beside its feature's dossier,
     `<feature>.reuse.toml` (instruction R-I's manifest parts), dispatch 23's pick C4′. A convention
     that crosses features lives in a part under `memory/map/conventions/`, since check 3 keeps the
     map root to its four files.
   - **What it extends:** each dossier's gated `## Reuse affordance` block (`seam: <id> — reuse for
     <need>; extend via <point>`) and its `decisions = [...]` key already hold the facts. Their seams
     become the entries' anchors, migrated once. No instruction carries them today.
   - **Lifecycle (LR-6):** it is written once and edited in place, so it says what holds now. Its one
     door is the instruction layer's write path (R-I, `instructions.edit`):
     - the builder of the feature proposes it through the instruction command, and the build's
       `gov:feature` check counts a proposed entry;
     - the owner's disposition of the proposal is an owner item, and the entry renders into work
       orders once accepted;
     - best effort never accepts it, since `instructions.edit` is a guard that presets never touch;
     - the owner item has three dispositions: accept, and the entry renders; reject and remove, and the
       entry becomes `removal-pending`, which the both-ways check accepts until a patch build removes
       the landed `gov:feature` anchor and the entry in one landing; reject and keep, and the entry
       stays `rejected`, never rendered, which the check accepts.
   - **The owner's examples:**
     - the media picker becomes "MUST reuse the media picker wherever an image, video or media
       selector is needed", triggered by the need, anchored to `gov:feature media-picker`;
     - screen-reader support becomes a convention: "MUST support screen reading on every new page",
       with its convention's anchor.
   - **On every install** (KN-1): the reuse entry is the library side, so the charter's `[records]`
     rule renders its reuse-entry clause wherever gov is installed, and `implements <reuse-entry>` is a
     relation the memory contract registers.
2. **The decision log keeps major product decisions only.** That is about 12 of today's rows. Each row
   carries:
   - its date;
   - its build;
   - the decision;
   - a pointer to its rationale;
   - the reuse entry it created, if any.

   Since LB-3 (2026-10-16) a decision's author declares it major by the rubric, and `deploy.distill`
   appends the build's major decisions to the log when it lands (layer-library `[log]`).

   Supersession extends the typed relations that exist. Check 27 (`row_grammar.py
   --check-relations`) obliges `supersedes`, `coexists-with` or `disputes` on every added row and
   gotcha, and memory-recall's `derive_supersession_map` already tags superseded hits. The generated
   "holds now" view renders that map.

   - **The log keeps its path,** `memory/DECISIONS.md`, so its 32 code readers keep working. The
     charter's facts line that sends a reader there "for why anything is the way it is" is re-worded
     to the log's new meaning, and each carrier that names it as the home of owner raises is
     re-pointed to the policy values and the ask register.
   - **It stays append-only.** A row leaves only by the existing rotation (`ROTATION_MODE`,
     byte-identical) into the archive. A routed row is superseded by a pointer row to its new home,
     never edited.
   - **Readers by value move with the rows:** the dossiers' `decisions = [...]` fields (17 cite ids,
     and the shrink-only `DOSSIER_DECISIONS_EMPTY_PIN=16` counts the empty ones), invariant gotchas'
     `decision:` keys under check 18, and the recall bench's 14 expected answers. Each routed row keeps
     its id, and its pointer row resolves for every one of them.
3. **Every other row goes to its true home:**

   | Class | Home |
   |---|---|
   | Owner rulings | policy values, since every behaviour is a policy |
   | Process and tooling rules | method or protocol text, in the instruction layer |
   | Waivers | the gates' row registries |
   | Minor choices and findings | the build's own records, or a gotcha when they name a bug class |

   The 200 live rows are routed once, by two raters. Their agreement must reach kappa 0.8 before the
   migration counts.
   - The raters are two independent agents with the rubric, neither seeing the other's labels, and the
     owner rules on each row they disagree on.
   - Below kappa 0.8 the rubric is revised and the routing re-run, and no row moves until it passes.
4. **The charter's `[records]` rule follows.** Each decision is recorded in its build as it is made. A
   major one is also logged. A reusable feature or convention becomes a reuse entry.

**This is also the route `gap-found-14` lacked.** Memory never instructs. A standing directive found
in memory, whether an auto-memory feedback entry or a decision row, becomes an instruction only by
promotion through R-I. The reuse entry is what that promotion produces for features and conventions.

### [reuse] Reuse: a scout reading a generated house index

aScoutedSeam measured the mechanism:
- the lookup solved 0 of 24 cases;
- a checklist scout solved 13;
- the scout that first reads a generated house index solved 16 in each of two runs.

So the design is:
- **Reuse is the reuse scout's item** (`design.seams`). Its work order hands it the house index, never
  a ranking:
  - the map's symbols and callers;
  - the dossiers and their seams;
  - the reuse entries.
- **Rendered delivery.** The scout matches the build's needs against the entries' triggers. Its
  matches fill the task card's `**Reuse:**` field, the slot that `handoff.py`'s `TASK_FIELDS` already
  render into every work order. The reuse scout declares that field an optional input today, and
  becomes its producer. Delivery by path is rejected, because "anywhere a media selector is needed"
  is a need, not a path.
- **The slot has three states,** each rendered distinctly: matched, with the entries; searched, with no
  match; and not searched, with the reason: the scout failed, or the index is stale. Without the map,
  an optional component since KN-1, the index holds the reuse entries alone, and the slot says so.
- **Under `reuse.delivery=on-demand`,** nothing is rendered into every work order. The reuse scout runs
  only when an item's work order asks for reuse, and its matches are handed to that item alone.
- **The index's shape is M1c's.** Its 16 of 24 came from a small curated digest, 2 to 33 KB, with an
  implementation sketch and a convention census. The scout gets that shape: a digest generated from
  the symbols, callers, dossiers and entries, sized to its packet, with the sketch and the census as
  steps of its checklist. dTotalRecall's acceptance re-runs aScoutedSeam's 24-case benchmark against
  the built index and entries, and must meet M1c's 16.
- **`reuse_lookup.py` retires as a ranker.** The retiring unit rewrites its readers, found by name and
  by value:
  - by name: about 40 files outside the build folders, among them the review harness's reuse lens and
    its template, `orient-counterfactual.js`, `WIRE-INTO-PROJECT.md`, the shipped BUILD-METHOD and
    SPEC-TEMPLATE templates, both kit READMEs, `INVENTORY-DERIVATION.md`, the reuse scout's agent files
    and `gen_map.py`;
  - by value: hygiene check 12's §10 arm accepts the token `reuse_lookup` as reuse evidence
    (`SPEC10_EVIDENCE_CUTOFF`), and the spec template and the charter require running the tool. The arm
    accepts the reuse scout's record instead, past a new cutoff;
  - by value: unattended finds the stale-dossier reader `map_diff.py` through `MAP_CLI`'s directory,
    which names `reuse_lookup.py`, so `MAP_CLI` is re-pointed at the map's CLI;
  - by value: the `reuse-probed` DoD item and M5 count the lookup's and recall's query logs as proof
    of a reuse probe. They read the reuse scout's record instead.
- **memory-recall narrows to a record finder for "why" questions,** an optional component of this layer
  since KN-1. It leaves the
  reuse obligation, since it holds no code. Its chunks arm is fixed or dropped.

### [map] The map: symbols and callers, generated

The map extends the existing seam, dispatch 24's pick A:
- **Definitions:** every Python definition, including methods, nested and private functions, through
  `ast`.
- **Python callers:** import-aware resolution for module-level calls. A method call resolves through
  its definitions' enclosing classes and bases; one that resolves to neither ships as a mention, and
  its count is reported. The probe's 11 ambiguous sites were among 1,997 import-resolvable ones, and it
  left 21,588 attribute and method calls unresolved.
- **Shell and JavaScript callers:** through the map's own extractors, scoped to sourced files and the
  caller's kit. The lexicon review made the map own extraction, the shell and JavaScript tokenizers
  included. Each definition carries its enclosing class, its bases resolved through imports, its
  decorators with aliases resolved, and its module's imports. Their ambiguity must fall below 10%, or
  they ship as "mentions", and the record says so.
- **Cross-language edges:** from interpreter-and-path invocations.
- **Freshness:** callers are generated on demand and cached by tree hash, never tracked, since a
  tracked fan-in file would go stale on every commit, which is why the map omits fan-in today. The
  freshness check covers the tracked definitions.
- **Cost:** the name-only probe took 7.8 seconds and the import-aware Python pass 4.4. The designed
  pipeline is untimed, so dTotalRecall's suite declares its ceiling (`[cost]`).

Around it:
- **Dossiers** stay the authored layer above: feature to symbols, paths, seams and reuse entries. They
  extend the gated `[claims]` table, keyed both ways, and `map_lib.measure_dossier_staleness`. 28 of 31
  are stale today by path ancestry, which symbol keys do not fix, so the staleness measure moves to the
  symbols each claim names.
- **Languages** are a declared list, with one extractor pack per language.
- **The owner** reads the generated views, `MAP.md` and `CARDS.md`, plus a callers view for each
  symbol.

### [annotations] Annotations: a grammar inside the `gov:` family

- **One head line per annotated block:**
  `gov:note <tags> — <short description> → <action pointer> refs=<id|path>`.
  - It uses the instruction layer's statement types.
  - A directive in code must point to its record.
- **The block's shape is checked when it is present. Presence stays voluntary.** That keeps
  aKeyedAnnotation's shipped-evidence signal intact. The build's first test re-reads its numbers:
  signal 2 must discriminate before and after.
- **`gov:feature <tag>` marks the canonical implementation of a reuse entry.** It is checked both
  ways with the entry: the entry's anchor resolves, and every feature tag has an entry, proposed,
  accepted, rejected and kept, or pending removal (LR-6). This is the owner's "code tag references". A second `gov:feature` line for one tag is
  a finding, and a file with no extractor pack cannot hold an anchor.
- **A generated annotation index** comes from the map's comment lexer, which today strips comments. The
  lexer gains a profile chosen by shebang for extensionless files, the git hooks among them, and reads
  Python docstrings. The index is queried by tag and never loaded whole.
- **References must resolve, and the check is a gate.** drift-audit's
  `source_cited_ids_resolving_to_no_record` is report-only today: it is not gateable, so crossing its
  pin of 2 never blocks a merge, and it counts ids only. The resolve check is a gate leg built on its
  function, `build_source_cited_ids_with_no_record`, extended to read `gov:note … refs=` ids and paths
  and `gov:feature` tags. Its pin stays shrink-only through the RATCHETS row.
  - Its first green proves nothing: no `gov:note` or `gov:feature` line and no reuse part exists, so
    the population is empty. Three planted red cases are owed, each seen red before the check is
    trusted: a dangling `refs=` id, a dangling `refs=` path, and a `gov:feature` tag with no entry.
    The check asserts a non-empty population once the first annotation lands.
  - Over every comment-cited id, 35 ids resolve nowhere: fixture ids and foreign families such as `PKG`
    and `ARCH`. Each class is an exemption row in the check's registry.
- **ANNOTATION-STYLE.md changes with it.** The grammar and the required anchor overturn its A1 (no
  grammar, marker or gate) and A2 (voluntary) in part. The guide and its shipped template are amended in
  the same unit, since `kit-dogfood-parity.test.sh` pairs them.
- **Tests owed by the build:**
  - a 30-block mutation probe, since a reference-only gate cannot see that a comment has drifted from
    its code;
  - the load the head lines add;
  - follow-through after landing, against today's 11.0%, its 6.1% control and the 2.5% exact.

  If follow-through does not rise, the runner-up is a hook that pushes records anchored to a file when
  it is opened, with per-session dedupe. The test's threshold, sample and window are dTotalRecall's to
  set (`gap-mem-12`).
- **Under `annotations.grammar=pushed-at-read`,** that hook is the mechanism: a pack of this layer's
  optional components in Runtime's one dispatcher entry, at PostToolUse on a read, registered by the
  memory contract (KN-1).
  dTotalRecall builds it.

### [knowledge] Gotchas, the lexicon and recall

- **Gotchas** stay, as the bug-class kind on the library side, core since KN-1. Every confirmed
  finding files a class or names a gate (LB-1, `review.unclassed`).
  - They are handed in builder and reviewer work orders by the unit's write set, instead of run by
    agents.
  - The six universal classes ride the role's static block.
- **The lexicon** keeps its vocabulary and `--suggest`, handed to builders for new names. Its offender
  pin should only ever fall, since a pin that rises is a waiver. Asked as F4-8. Shrink-only is one row
  in drift-audit's RATCHETS (`ratchet_findings`), beside `ORPHAN_ID_PIN`, `DEAD_PATH_PIN` and
  `DOSSIER_DECISIONS_EMPTY_PIN`. The lexicon review gave the lexicon's re-engineering, the pin and
  `--suggest`'s handling included, to dMindYourWords.
- **Recall:** see `[reuse]`.

### [views] Orientation at a glance

Every view the owner reads is generated from records, never authored state:
- `LIVE.md`;
- each build's README, with its routing and typed edges;
- the plan view across builds;
- the decision log's "holds now" view;
- the reuse view: features and conventions by area, with their directives;
- the map views;
- the ask views;
- the gotcha index;
- the research view: every research return by build, date and question (layer-library
  `[research-view]`, 2026-10-16).

Agents never read a view to work: their work orders hand them fields. The orientation scout is the
one exception, reading the README, the owner's root, to compose the card. Under
`builds.agent-root=readme`, the executor hands each agent the README's routing region as its work
order's root field, never the file.

### [determinism] What makes every memory practice deterministic

- Each kind has a schema in the registry, and a template rendered from it.
- One command mints ids, renders templates and refuses invalid values.
- Status, indexes, inverses and views are derived, never typed.
- References resolve, and relations are checked both ways.
- Views are byte-compared after rendering, the way check 9 compares README regions today.
- A decision's class is a declared field. The write command checks it, and the routing rubric is held
  to two-rater agreement.

## [tools] The tooling map: keep, re-engineer, retire

From dispatch 26. Where the memory design changes a verdict, the change is noted.

| Verdict | Tools | Deciding fact |
|---|---|---|
| Retire | `reuse_lookup.py` and its agent file | 0 of 24; ranks test helpers first |
| Retire | the deploy-governance Skill | no reader, 0 loads, repeats govkit's verbs |
| Retire | `DECISIONS.md` as an append-anything log | 14% of rows fit its purpose; routed by `[decisions]` |
| Re-engineer | memory-tree | becomes the memory contract's engine: the registry, the `record` command and the generated checks. Its ask grammar is kept |
| Re-engineer | codebase-map | symbols, callers and the annotation index; the lookup dropped |
| Re-engineer | memory-recall | narrowed to a record finder |
| Re-engineer | lexicon | its pin becomes shrink-only (F4-8), built by dMindYourWords |
| Re-engineer | playbook, agent-instructions | tag-sliced views |
| Re-engineer | roles | its stage order moves to the loop kit |
| Re-engineer | run-gates | legs read from the kit packs (81 exist only in the JSON) |
| Re-engineer | unattended | the flow ladder extracted into the loop kit (4.5 MB, 54 asks) |
| Re-engineer | hooks | one Runtime surface (five kits today) |
| Re-engineer | govkit, with check-wiring and check-placeholders folded in | one wiring verdict, one version check |
| Re-engineer | lib | the 73 inline `resolve_python` copies generated, not hand-kept |
| Re-engineer | check-agent-cap-restatement | generalised to "a policy value restated" |
| Re-engineer | check-microformats | rebuilt on the statement types |
| Keep | workflows | grows into the always-spawn harness |
| Re-engineer | runlog | its journal grammar moves into the core (Runtime), and its run record joins the registry |
| Keep | push-main.sh, session-kickoff, process-monitor, settings-merge.py | live and needed |
| Keep | drift-audit | shares its dangling-path function with check-dead-paths |
| Keep | branch-reconcile and cleanup, gate-lint | expansion and pack |
| Keep | check-spec-tokens | as Design's pack |
| Keep | the other checks | regrouped into Instruction and Distribution packs |
| Keep | the adopter-facing Skills | drift-audit, memory-recall and runlog have 0 loads, but their scripts ran 365, 314 and 32 times |
| Demote | pytest-parallel-guardrails | 0 runs and no xdist suite: dogfood it, or declare it adopter-only |

**On the order.** Dispatch 26 picks "Flow first": extract the loop kit, then the leg packs, hooks,
memory-tree, the instruction views and the expansions.
- **Its objection.** It rejects starting with the instruction layer, because step tags come from the
  loop kit.
- **The answer.** The step tags are already declared in the step definitions, so dOrderedCharter can
  register them first.
- **Where it is settled.** The order is the chain re-cut's input, not this round's decision.

## [gaps-proposed] Gaps to register once the forks settle their home

Registered on 2026-10-15, after the forks, as `gap-mem-01` to `gap-mem-11` and `gap-tool-01` to
`gap-tool-06`, in the order below.

New area `Memory`:
1. HIGH. No memory contract:
   - no registry declares the record kinds;
   - conventions spread over `HYGIENE.md`, the spec template, the guides and 21 legs;
   - reviews, journals and 535 of 565 prompts are free prose;
   - front matter is open-world.
2. HIGH. The decision index holds the wrong things and instructs no one:
   - 28 of 200 rows fit;
   - 0 carry a reuse instruction;
   - nothing requires a row;
   - recall never opened it;
   - 47 rows chain supersessions.
3. HIGH. No reuse instruction reaches an agent:
   - no kind holds one;
   - the card's `reuse` slot has nothing behind it;
   - the lookup solved 0 of 24.
4. HIGH. The map stores no relations:
   - 0 caller edges;
   - fan-in counts mentions;
   - Python 75.5% covered;
   - 1,012 cross-language invocations are unseen.
5. MED. A README routes only to specs. Nothing routes by purpose, and 77.9% of agent-build pairs never
   read it.
6. MED. Slug and id patterns are spelled per reader:
   - eleven readers in seven kits;
   - a dated slug breaks 6 to 10 of them;
   - the prose rule says two words, the owner one to three, and nothing checks either.
7. MED. Relations are untyped:
   - `parents:` only;
   - no patch, amendment or supersession field;
   - no cross-build unit edge;
   - no cycle check.
8. MED. Annotations have no grammar, no tags and no index:
   - 0 tag lines in 91,661 comment lines;
   - the guide was read once in 60 days;
   - follow-through to a cited record is 2.5%.
9. MED. memory-recall indexes no code, and its chunks arm scores 0.00. 5.5% of its answers are read
   through.
10. MED. The lexicon gate absorbs debt: its pin rose from 412 to 1,087, with one real drain.
11. LOW. Memory records contradict the code:
    - the map README names a missing path;
    - `backlog.py` says it ships dark;
    - the DEPL section of `DECISIONS.md` holds 81 rows of other families;
    - three ids are duplicated;
    - the spec template demands a security model in the log, where 0 rows have one;
    - 9 READMEs type their status.

New area `Tooling`:
1. MED. Gate legs are declared twice: 81 of 140 exist only in `gate-legs.json`. Owner: dWitnessedBar.
2. MED. Wiring is judged three ways, and version lockstep four ways. Owner: dShippedRelease.
3. MED. The hook surface spans five kits. Owner: dWellOiledMachine, since the runtime layer
   (RT-3).
4. LOW. 73 files carry hand-kept inline copies of `resolve_python`, where the copy-install could
   generate them. Owner: dShippedRelease.
5. LOW. Dead or undogfooded tools: the deploy-governance Skill, and pytest-parallel-guardrails.
   Owner: dConvergedCharter.
6. LOW. `.claude/rules/product.md` misdescribes the gates: check-wiring is not a leg, and 14 checks
   run as legs. Owner: dConvergedCharter.

**Already registered, now with a fix designed here:**
- `gap-plan-06`: asks without an acceptance;
- `gap-design-01`: the map is an inventory;
- `gap-maint-06`: stale dossiers;
- `gap-found-14`: memory instructs outside the ladder.

Their owners stand, but their fixes are dTotalRecall's units, and dDeclaredLoop, `gap-design-01`'s
owner, is dTotalRecall's parent. v2's `[owed]` carries the order to the re-cut.

## [forks] Asked, 2026-10-15

**F4-1. "The decision index holds 200 rows. 14% of them are the major decisions and reusable features
you meant it for, and none carries a reuse instruction. What should it become?"**
- Offered:
  - Split by kind (Recommended): reuse entries as ranked instruction units beside each feature,
    rendered into work orders when a build's needs match; the log keeps major decisions only; every
    other row goes to its true home.
  - One index with a major tier: `DECISIONS.md` stays, and a tier of rows carries directives with a
    rank, read on demand.
  - A separate feature registry: one catalog entry per feature, apart from the dossiers.

**F4-2. "Code comments carry 1,121 build ids and no tags, and the style guide refuses any grammar. How
should annotations work?"**
- Offered:
  - A voluntary `gov:note` grammar (Recommended): a head line with tags, a short description, an
    action pointer and references, checked for shape when present; `gov:feature` required on code a
    reuse entry points to; a generated index queried by tag.
  - Required on every block: every comment block carries the head line.
  - Pushed when a file is read: no grammar, and a hook injects the records anchored to an opened
    file.

**F4-3. "The reuse lookup solved 0 of 24 cases and ranks test helpers first. memory-recall is used,
but 5.5% of its answers are read through, and it holds no code. What happens to them?"**
- Offered:
  - Retire the lookup, narrow recall (Recommended): the reuse scout reads a generated house index,
    the shape that solved 16 of 24, and recall stays as a record finder for "why" questions.
  - Retire both.
  - Keep both, redesigned under the new conventions.

**F4-4. "Roles got their own chain build. Where do the memory contract and Knowledge's stores get
built?"**
- Offered:
  - Its own chain build (Recommended): `dTotalRecall`, a child of dDeclaredLoop, owning the memory
    gaps.
  - Spread over the step builds.
  - Decide at the re-cut.

**F4-5. "You want agents to enter a build at its README and go deeper only when needed. Today 77.9%
of agents never read it. Under P29 each agent's work order is cut from the build's records. Which is
an agent's root?"**
- Offered:
  - The work order (Recommended): the executor cuts it from the records, and the README is the root
    for you and the orientation scout, routing by purpose.
  - The README: every agent reads it first, then what it routes to.

**F4-6. "132 open asks lack an acceptance, because filing without one only lowers a grade. What
happens to an ask filed without one?"**
- Offered:
  - Refused at filing (Recommended): every core filer can state one mechanically.
  - Filed and graded not ready, as today.

**F4-7. "Slugs stay a node letter and one to three humorous CamelCase words. Should a build's name
carry a date by default?"**
- Offered:
  - No date (Recommended).
  - Shown beside the slug: rendered from `opened` in every view, never part of an id.
  - Inside the slug: it breaks six to ten id readers until all of them read one grammar.

**F4-8. "The naming gate's offender pin rose from 412 to 1,087, with one real drain in 60 days. How
should it move?"**
- Offered:
  - Shrink-only (Recommended).
  - Absorb, as today.
  - Retire the gate and keep the vocabulary.

### Settled after F4-1 to F4-8, 2026-10-15

All eight were answered with the recommended option.

| Fork | Answer | Key | Default | Also allowed |
|---|---|---|---|---|
| F4-1 | Split by kind | `reuse.delivery` (the decisions split as `[decisions]` designs) | `rendered` | `on-demand` |
| F4-2 | Voluntary `gov:note` | `annotations.grammar` | `voluntary` | `required`, `pushed-at-read` |
| F4-3 | Retire the lookup, narrow recall | none: the choice is structural | — | — |
| F4-4 | Its own chain build | none: dTotalRecall, a child of dDeclaredLoop | — | — |
| F4-5 | The work order | `builds.agent-root` | `work-order` | `readme` |
| F4-6 | Refused at filing | `asks.acceptance` | `refuse` | `grade` |
| F4-7 | No date | `builds.slug-date` | `none` | `shown`, `in-slug` |
| F4-8 | Shrink-only | `lexicon.pin` | `shrink-only` | `absorb`, `no-gate` |

- **`gov:feature` stays required** on code a reuse entry points to, whatever `annotations.grammar`
  says.
- **dTotalRecall owns** the memory contract and Knowledge's stores, with `gap-mem-01` to
  `gap-mem-11`. The lexicon review since moved `gap-mem-10`, the lexicon pin and the lexicon's
  re-engineering to dMindYourWords.
- **The owner's words set two more keys:**
  - `builds.slug-words`: 1 to 3;
  - `builds.slug-style`: `humorous`, with `descriptive` allowed.

**Presets.** `velocity` grades an ask without an acceptance instead of refusing it, and lets the
lexicon pin absorb. Every other new key holds its default in all four presets.

**What changed elsewhere:**
- **v2:**
  - P30 is added.
  - The eight keys join the catalogue and every preset.
  - The chain gains dTotalRecall's row and becomes twelve builds. Later layers added more, and v2's
    `[chain]` holds the roster.
  - `[owed]` gains two items: dTotalRecall's place in the re-cut, and the tooling order.
- **The register** gains `gap-mem-01` to `gap-mem-11` and `gap-tool-01` to `gap-tool-06`. The
  tooling gaps go to dWitnessedBar, dShippedRelease, dDeclaredLoop and dConvergedCharter.

## [instrument] The comparison, as run 2026-10-15

`ro_compare.py` reuses `role_orientation.py`'s functions, which are recorded in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md` (`[instrument]`):

```python
"""Compare the memory round's five briefed researchers, whose briefs handed settled facts as content,
with every earlier gov-researcher spawn, using role_orientation.py's classes and flags unchanged."""
import collections, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import role_orientation as ro

NEW = {"ad130bc5b0b446984", "a683df94188e34f7a", "aa631366c077d00d1", "a0f40dd21c9243c66", "aaba36be47df28242"}
agg = {"handed (22-26)": collections.Counter(), "earlier researchers": collections.Counter()}
per = []
for meta in glob.glob(ro.ROOT + "/C--projects-coding-governance*/*/subagents/**/agent-*.meta.json", recursive=True):
    m = json.load(open(meta, encoding="utf-8"))
    if m.get("agentType") != "gov-researcher":
        continue
    aid = os.path.basename(meta)[len("agent-"):-len(".meta.json")]
    fwd = meta.replace(chr(92), "/")
    calls, first = ro.calls_of(meta[:-len(".meta.json")] + ".jsonl")
    had = ro.parent_reads(fwd.split("/subagents/")[0] + ".jsonl", m.get("toolUseId")) if "/workflows/" not in fwd else None
    g = "handed (22-26)" if aid in NEW else "earlier researchers"
    c = agg[g]
    c["agents"] += 1
    for _, name, inp, rlen in calls:
        k = ro.klass(name, inp)
        c["calls"] += 1
        c[k] += 1
        c["bytes"] += rlen
        c["bytes_" + k] += rlen
        for f in ro.files_read(name, inp):
            c["reads"] += 1
            if had is not None:
                c["reads_known"] += 1
                c["parent"] += f in had
            c["dclosed"] += f.startswith("memory/builds/dClosedLoop/")
    if aid in NEW:
        per.append((aid, len(calls)))
print("| group | agents | calls | calls/agent | state % | locate % | method % | orient bytes % | parent-had % of reads | reads of dClosedLoop records |")
print("|---|---|---|---|---|---|---|---|---|---|")
for g, c in agg.items():
    o = c["state"] + c["locate"] + c["method"]
    ob = c["bytes_state"] + c["bytes_locate"] + c["bytes_method"]
    print(f"| {g} | {c['agents']} | {c['calls']} | {c['calls']/c['agents']:.1f} | {100*c['state']/c['calls']:.1f} | "
          f"{100*c['locate']/c['calls']:.1f} | {100*c['method']/c['calls']:.1f} | {100*ob/c['bytes']:.1f} | "
          f"{100*c['parent']/max(1,c['reads_known']):.1f} | {c['dclosed']} |")
print("per handed agent (calls):", sorted(per, key=lambda x: x[0]))
```

Run as `python ro_compare.py`, it printed:

```text
| group | agents | calls | calls/agent | state % | locate % | method % | orient bytes % | parent-had % of reads | reads of dClosedLoop records |
|---|---|---|---|---|---|---|---|---|---|
| handed (22-26) | 5 | 245 | 49.0 | 2.4 | 15.9 | 13.9 | 38.5 | 41.3 | 0 |
| earlier researchers | 21 | 692 | 33.0 | 1.0 | 12.1 | 19.7 | 30.2 | 25.8 | 24 |
per handed agent (calls): [('a0f40dd21c9243c66', 40), ('a683df94188e34f7a', 57), ('aa631366c077d00d1', 40), ('aaba36be47df28242', 49), ('ad130bc5b0b446984', 59)]
```

## [revised] Revised 2026-10-16: the two Tier-2 rounds, folded

Two Tier-2 rounds reviewed this record at blob `bb5dd4e2`. The comparison record places their findings
on 73 defects (`build/2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared.md`, `[map-memory]`),
and its map's `disposition` cells point here. Each defect's fix sits in place, in the sections named:
- **amend:** this record, or a sibling record, now states the fix;
- **gap:** the owning chain build carries it in the register;
- **owed:** v2's `[owed]` carries it to the chain re-cut;
- **fork:** the owner answered it, in the comparison record's `[answers]`;
- **none:** every finding on it was refuted.

| Defect | Disposition | Where the fix sits |
|---|---|---|
| `stale-lexicon-owner` | amend | the settlement after F4-8, `[knowledge]` and `[tools]`: dMindYourWords |
| `stale-gap-tool-03` | amend | `[gaps-proposed]` Tooling 3: dWellOiledMachine |
| `stale-chain-count` | amend | the settlement after F4-8: v2's `[chain]` holds the roster |
| `stale-map-tokenizers` | amend | `[map]`: the map owns extraction, with the definitions' context fields |
| `stale-runlog-unchanged` | amend | `[tools]`: runlog re-engineered, its journal grammar in the core |
| `slug-date-text-stale` | amend | `[names]`: `none` by F4-7, and what `shown` and `in-slug` do |
| `record-idempotence` | amend | `[contract]`: `record` is idempotent and content-addressed |
| `record-concurrent-mint` | amend, gap | `[contract]`: `entry.claim`'s claim ref, then the build's lease; `gap-mem-13` owes the refs |
| `kind-list-incomplete` | amend | `[contract]`: each layer registers its kinds; the run record, the backlog row and the witness class added |
| `ref-homed-kinds` | amend | `[contract]`: a home is a path or a ref |
| `generated-kinds-door` | amend | `[contract]`: one door per kind, generators for generated kinds |
| `scaffold-seams` | amend | `[contract]`: `record` extends `--new-build` and `--new-spec` |
| `runlog-schema-seam` | amend | `[contract]`: `RECORD_SCHEMA` and the run record |
| `hygiene-render-seam` | amend | `[contract]`: the registry feeds the existing `--render` |
| `hygiene-checks-not-schema` | amend | `[contract]`: only schema checks are generated |
| `check-numbers-stable` | amend | `[contract]`: each check's number stays its alias |
| `legacy-population` | amend | `[contract]`: a schema binds records after its cutoff |
| `frozen-refs-resolve` | amend | `[contract]`: an append-only or frozen record's references are checked when written |
| `new-stores-concurrency` | amend | `[contract]`: reconciled additively or re-rendered, and registered in `--dispatch` |
| `relation-target-unlanded` | amend | `[relations]`: a target on another node's branch resolves through the remote's refs |
| `authority-keys-via-record` | none | refuted |
| `derived-keys-front-matter` | amend | `[build]`: derived keys leave the front matter |
| `readme-root-vs-views` | amend | `[views]`: the orientation scout's exception, and `builds.agent-root=readme` |
| `id-grammar-seam` | amend | `[names]`: the parser moves into memory-tree |
| `slug-re-carrier` | amend | `[names]`: `BUILD_SLUG_RE` is derived |
| `flip-acceptance-unfailable` | amend | `[names]`: each reader must turn green, over a predicate population |
| `flip-values-unnamed` | amend | `[names]`: the flips are named |
| `grammar-change-existing-ids` | amend | `[names]`: a changed grammar binds new mints only |
| `slug-style-unenforceable` | amend | `[names]`: the style is the minting source |
| `v14-refusal-exists` | amend | `[current]` and `[asks]`: V14 is the seam; F4-6's premise corrected |
| `ask-filer-coverage` | fork, amend | LR-5 and LR-7; `[asks]`: a form for every core ask kind, and an `accept` line for every other filer |
| `refused-ask-fate` | amend | `[asks]`: a refused ask returns to its filer |
| `decisions-layer-placement` | amend | `[contract]`'s refinement covers major decisions; v2's `[layers]` |
| `decisions-readers-unnamed` | amend | `[decisions]` 2: the log keeps its path, and its carriers are re-pointed |
| `decisions-append-only` | amend | `[decisions]` 2: rows leave only by rotation |
| `decision-id-readers` | amend | `[decisions]` 2: readers by value move with the rows |
| `kappa-below-threshold` | amend | `[decisions]` 3: the raters, and the route below 0.8 |
| `supersession-seam` | amend | `[decisions]` 2: check 27 and `derive_supersession_map` |
| `amends-vs-frozen-spec` | amend | `[relations]`: `amends` names a new unit, and `@rev-N` is dropped |
| `reuse-entry-two-doors` | fork, amend | LR-6; `[decisions]` 1 and `[contract]`: the instruction command is the one door |
| `reuse-entry-proposal-path` | fork, amend | LR-6; `[decisions]` 1: proposed with the build, and the owner's three dispositions |
| `reuse-entry-level` | none | refuted |
| `reuse-entry-should` | amend | `[decisions]` 1: a MUST with its trigger, ranked by a field |
| `reuse-affordance-seam` | amend | `[decisions]` 1 extends the `## Reuse affordance` block; `gap-mem-03` |
| `core-needs-knowledge` | amend | `[decisions]` 1: the clause rendered only where Knowledge was installed; since KN-1 it renders on every install |
| `reuse-field-seam` | amend | `[reuse]`: the task card's `**Reuse:**` field |
| `reuse-slot-states` | amend | `[reuse]`: three states |
| `house-index-evidence` | amend | `[reuse]`: the index takes M1c's shape |
| `reuse-benchmark-rerun` | amend | `[reuse]`: the benchmark re-run is dTotalRecall's acceptance |
| `on-demand-no-mechanism` | amend | `[reuse]`: what `on-demand` does |
| `foundation-home` | amend | `[decisions]` 1: conventions under `memory/map/conventions/` |
| `lookup-name-inventory` | amend | `[reuse]`: the readers by name |
| `spec10-token` | amend | `[reuse]`: check 12's §10 arm |
| `lookup-map-cli` | amend | `[reuse]`: `MAP_CLI` re-pointed |
| `reuse-probed-readers` | amend | `[reuse]`: the `reuse-probed` item and M5 read the scout's record |
| `reuse-obligation-witness` | none | refuted |
| `ratchets-seam` | amend | `[knowledge]`: shrink-only is one RATCHETS row |
| `method-callers-floor` | amend | `[map]`: method calls resolve through classes, or ship as mentions |
| `map-cost-untimed` | amend | `[map]`: both probes timed, the pipeline's ceiling declared |
| `callers-restale` | amend | `[map]`: callers generated on demand, never tracked |
| `dossier-anchor-seam` | amend | `[map]`: dossiers extend `[claims]` and `measure_dossier_staleness` |
| `inventory-counts` | amend | `[current]`'s tooling counts; `gap-tool-06` |
| `annotation-green-vacuous` | amend | `[annotations]`: a gate leg with three planted red cases owed; a non-empty population once one lands |
| `dangling-ids-exist` | amend | `[annotations]`: 35 ids, each class an exemption row |
| `resolve-check-seam` | amend | `[annotations]`: a gate leg on drift-audit's function, since its signal is report-only |
| `lexer-blind-spots` | amend | `[annotations]`: a shebang profile, and docstrings |
| `annotation-grammar-inputs` | none | refuted |
| `feature-anchor-cases` | amend | `[annotations]`: one anchor per tag; no anchor without a pack |
| `annotation-style-overturned` | amend | `[annotations]`: the guide and its template change with it |
| `follow-through-test` | amend, gap | `gap-mem-12`: its threshold, sample and window are dTotalRecall's |
| `pushed-at-read-no-hook` | amend | `[annotations]`: the read hook is a pack of memory's optional components in Runtime's dispatcher (KN-1) |
| `gap-owner-order` | owed | v2 `[owed]`: the re-cut orders dTotalRecall ahead of the gaps' owners, or moves the gaps to it |
| `recall-boundroles-order` | none | refuted |
