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
