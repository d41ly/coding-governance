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
  - codebase-map, lexicon and memory-recall belong to Knowledge.
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
- **Missing acceptance.** 132 OPEN asks lack an acceptance. Filing without one only lowers a grade:
  READY rule R5 is a grade, not a verdict.
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
  out of 1,997. All three languages took 7.8 seconds.
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
- **The population:** 19 kits, 30 top-level checks, 9 Skills and 140 gate legs.
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
| All lifecycle memory | the core trail plus Knowledge's stores, with conventions spread over `HYGIENE.md` (58.5 KB), the spec template, the guides and 21 memory-tree legs | one memory contract over both, sorted core and Knowledge by P28 (`[contract]`) |
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
- **home:** its path, its filename grammar and its id rule, with ids minted, never typed;
- **schema:** its fields, their types, and which are required. Its template is rendered from the
  schema;
- **writer and readers:** the item or command that writes it, and the items whose work orders hand
  its fields;
- **lifecycle:** append-only, current-state (edited in place), or frozen at a transition;
- **check:** generated from the schema, and run both ways. Every reference resolves, and every
  declared inverse exists.

One write command, `record`, is the only writer of record structure, as R-I's command is for
instructions:
- it mints the id;
- it renders the template;
- it refuses an invalid value at the write boundary.

Agents supply field values. `HYGIENE.md`'s checks become generated checks, and its prose becomes a
view rendered from the registry.

The kinds sort by P28:
- **Core:** intake, card, plan, seams, feature design, spec, research, review, ask, the witness
  records (acceptance, verdict, attribution, transition, landing), work order, major decision.
- **Knowledge:** dossier, reuse entry, gotcha, the lexicon, and the generated stores: symbols,
  callers, the annotation index and the recall index.

**One refinement to layers round one.** Research records are written by core items (`plan.research`,
`design.research`), so the kind is core. Knowledge holds the consulting of past research, not the
records.

### [build] The build: one root for the owner, one for each agent

- **The README stays the build's root for the owner and for the orientation scout.**
  - Its front matter gains a declared schema, dispatch 22's pick D. Unknown keys are refused.
    `node`, `roster` and `streams` become derived, since nearly every README already matches the
    derivation.
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

- **The grammar is policy values, read from one parser.** The memory contract exports it once:
  - `builds.slug-words`, 1 to 3 by the owner's words;
  - `builds.slug-style`, humorous, which is the product's foundation;
  - `builds.slug-date`, asked as F4-7.

  Every slug and id reader then reads the export. The eleven measured readers come first, then the
  thirteen id parsers that share their character classes.
- **The test that prices it** is dispatch 22's. Flip the grammar in a scratch clone and run every
  reader. Each must turn green, or be named.
- **A date is safest as a derived property.** It can be rendered from `opened:` beside the slug in
  every view, never inside an id, so no id parser changes. A date inside the slug costs the six to
  ten readers that break today, until all of them read the one grammar.
- **The record command mints the slug.** It checks the grammar and collisions, so a slug is never
  typed.

### [relations] Typed relations between builds

| Relation | Means | Inverse rendered in the target |
|---|---|---|
| `depends-on <slug>` | today's `parents:`, kept as an alias | depended on by |
| `patches <unit-id>` | a patch build's target unit | patched by |
| `amends <unit-id>@rev-N` | a spec revision made from another build | amended by |
| `supersedes <slug>` | P20's superseded ending | superseded by |
| `implements <reuse-entry>` | a build that creates or changes a feature or convention | implemented by |

- **Checks:** every relation's target must exist, and `depends-on` must form no cycle. Unit edges may
  cross builds.
- **Views:** the generated graph feeds the plan view, so a feature can be traced from the build that
  made it, through its patches and amendments, to its current entry.

### [asks] The ask register

- **Kept as the core kind it already is:** the row grammar, the disposition verbs, the order-free fold,
  severity rows and READY grading.
- **One change: an acceptance at filing.** Every core filer can state one mechanically:
  - a red: a later green of the same leg;
  - an unverified finding: a review round that rules on it;
  - a stray: the path claimed or reverted;
  - a repair: the producer's record corrected.

  Whether filing without one is refused or only graded is asked as F4-6.
- **Labels, family views and rotation stay optional bookkeeping.**
- **The parked asks are triage's.** Draining 297 parked asks is Plan's job (`gap-plan-02`, dRankedPlan).

### [decisions] Decisions, split by what each one is

The owner's intended entry, "a decision with an INSTRUCTION, with an appropriate ranking", is two
records. Neither may instruct by being recalled.

1. **A reuse entry is an instruction unit.**
   - **Kind and placement:** level 3, kind `reuse`. Its statement type is a directive or a constraint,
     and its strength (MUST or SHOULD) is the owner's ranking. It carries a policy tag, so the owner
     can switch it.
   - **Fields:**
     - the feature's tag;
     - the needs that trigger it, as tags or phrases, such as "media selection" or "a new page";
     - its code anchors (`[annotations]`);
     - its date;
     - the build that made it;
     - the decision that created it.
   - **Home:** beside its feature's dossier, as dispatch 23's pick C4′, a sidecar
     `<feature>.reuse.toml`. A convention that crosses features lives in `FOUNDATION`.
   - **Lifecycle:** it is written once and edited in place, so it says what holds now. It changes only
     through the instruction layer's write path (R-I, `instructions.edit`).
   - **The owner's examples:**
     - the media picker becomes "MUST reuse the media picker wherever an image, video or media
       selector is needed", triggered by the need, anchored to `gov:feature media-picker`;
     - screen-reader support becomes a `FOUNDATION` convention: "MUST support screen reading on every
       new page", with its convention's anchor.
2. **The decision log keeps major product decisions only.** That is about 12 of today's rows. Each row
   carries:
   - its date;
   - its build;
   - the decision;
   - a pointer to its rationale;
   - the reuse entry it created, if any.

   Supersession is a typed relation, and a generated "holds now" view replaces walking chains.
3. **Every other row goes to its true home:**

   | Class | Home |
   |---|---|
   | Owner rulings | policy values, since every behaviour is a policy |
   | Process and tooling rules | method or protocol text, in the instruction layer |
   | Waivers | the gates' row registries |
   | Minor choices and findings | the build's own records, or a gotcha when they name a bug class |

   The 200 live rows are routed once, by two raters. Their agreement must reach kappa 0.8 before the
   migration counts.
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
  matches fill the card's `reuse` slot, a core extension point that Knowledge fills, and every work
  order of the build renders them. Delivery by path is rejected, because "anywhere a media selector
  is needed" is a need, not a path.
- **`reuse_lookup.py` retires as a ranker.** Its readers are rewritten: 24 code readers, 7 document
  citations and its agent file.
- **memory-recall narrows to a record finder for "why" questions,** inside Knowledge. It leaves the
  reuse obligation, since it holds no code. Its chunks arm is fixed or dropped.

### [map] The map: symbols and callers, generated

The map extends the existing seam, dispatch 24's pick A:
- **Definitions:** every Python definition, including methods, nested and private functions, through
  `ast`.
- **Python callers:** import-aware resolution.
- **Shell and JavaScript callers:** through the lexicon kit's tokenizers, scoped to sourced files and
  the caller's kit. Their ambiguity must fall below 10%, or they ship as "mentions", and the record
  says so.
- **Cross-language edges:** from interpreter-and-path invocations.
- **Freshness:** a generated callers file, under the freshness check the map already runs.
- **Cost:** about 8 seconds on this tree, stdlib only.

Around it:
- **Dossiers** stay the authored layer above: feature to symbols, paths, seams and the reuse sidecar.
  They are anchored to generated symbol keys, so a moved symbol turns its dossier red. 28 of 31 are
  stale today.
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
  ways with the entry: the entry's anchor resolves, and every feature tag has an entry. This is the
  owner's "code tag references".
- **A generated annotation index** comes from the map's comment lexer, which today strips comments.
  It is queried by tag and never loaded whole. References must resolve: 0 dangle today, so the check
  is green on its first run.
- **Tests owed by the build:**
  - a 30-block mutation probe, since a reference-only gate cannot see that a comment has drifted from
    its code;
  - the load the head lines add;
  - follow-through after landing, against today's 11.0%, its 6.1% control and the 2.5% exact.

  If follow-through does not rise, the runner-up is a hook that pushes records anchored to a file when
  it is opened, with per-session dedupe.

### [knowledge] Gotchas, the lexicon and recall

- **Gotchas** stay, as the bug-class kind behind the Build extension point.
  - They are handed in builder and reviewer work orders by the unit's write set, instead of run by
    agents.
  - The six universal classes ride the role's static block.
- **The lexicon** keeps its vocabulary and `--suggest`, handed to builders for new names. Its offender
  pin should only ever fall, since a pin that rises is a waiver. Asked as F4-8.
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
- the gotcha index.

Agents never read a view to work. Their work orders hand them fields.

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
| Re-engineer | lexicon | its pin becomes shrink-only (F4-8) |
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
| Keep | push-main.sh, session-kickoff, process-monitor, runlog, settings-merge.py | live and needed |
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
3. MED. The hook surface spans five kits. Owner: dDeclaredLoop, until Runtime gets its build at the
   re-cut.
4. LOW. 73 files carry hand-kept inline copies of `resolve_python`, where the copy-install could
   generate them. Owner: dShippedRelease.
5. LOW. Dead or undogfooded tools: the deploy-governance Skill, and pytest-parallel-guardrails.
   Owner: dConvergedCharter.
6. LOW. `.claude/rules/product.md` misdescribes the gates: check-wiring is not a leg, and 15 checks
   run as legs. Owner: dConvergedCharter.

**Already registered, now with a fix designed here:**
- `gap-plan-06`: asks without an acceptance;
- `gap-design-01`: the map is an inventory;
- `gap-maint-06`: stale dossiers;
- `gap-found-14`: memory instructs outside the ladder.

Their owners stand.

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
