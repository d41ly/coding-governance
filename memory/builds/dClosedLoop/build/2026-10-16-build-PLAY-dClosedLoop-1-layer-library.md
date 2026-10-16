# Layer review: memory's library side, which replaces the Knowledge layer

**Serves:** research PLAY-dClosedLoop-1

This round was meant to design Knowledge as an expansion. Before it opened, the owner asked why
Knowledge stands apart from memory at all, and answered KN-1: it folds into the memory layer as its
library side. This record holds:
- the owner's words;
- the reasoning put to them;
- the fork and its answer;
- what the answer changed;
- what the library round still owes.

## [words] The owner's words, 2026-10-16

> Let's understand the knowledge layer first - why does it have to be logically separate from the
> memory layer in the first place? Technically, those are just extra tools over the same entity.

## [why] Where the split came from, and what it bought

- **It was a packaging test, not a property of the entity.** Layers round one sorted core from
  expansion by one test: the core alone carries a build from request to landing (layer-instruction
  `[forks]`, L1 and L2). Knowledge failed the test and became an expansion. The owner's memory words,
  a round later, list decisions, the codebase map, reuse and annotations as memory, and layer-memory
  `[settled]` bridged the two: "the owner's memory layer spans both".
- **What the split bought:**
  - optional install under P28, which holds for the heavy generated tools: the map's per-language
    extractors and the recall index;
  - a trust line: the trail is proof that `next` reads, and the consulted side is advice, which the
    charter's `[memory]` rule keeps from instructing. P29 already classes every handed fact as
    witnessed, decided or claimed, so that line needs no layer either.
- **What it cost:**
  - the owner's own example, the media-picker reuse directive, was a Knowledge-filled slot that a
    core-only install never rendered;
  - one store had two contracts: core items wrote decisions and research, and Knowledge held their
    consulting, though dTotalRecall builds both;
  - the bug-class catalogue was classed Knowledge, while its engine, `gotchas.py`, ships in
    memory-tree, the core memory kit;
  - "where knowledge is installed" clauses ran through the step definitions, the instruction layer's
    slots and the work orders;
  - most of the would-be layer was already designed in layer-memory: `[reuse]`, `[map]`,
    `[decisions]`, `[knowledge]` and `[tools]`.
- **The line that holds is lifecycle.** The trail records what happened in a build. The library holds
  what generalizes beyond one: major decisions, reuse entries, bug classes and research. The machinery
  between them is distillation:
  - a finding becomes a class through left-shift;
  - a feature becomes a reuse entry;
  - a decision becomes a log row;
  - a build's research joins the library.

## [forks] Asked, 2026-10-16

**KN-1. "How should Knowledge relate to the Memory layer?"**
- Offered:
  - One layer, two sides (Recommended): Memory holds the trail (what happened) and the library (what
    generalizes: decisions, reuse entries, bug classes, research). The map, recall and lexicon kits
    become optional memory components, with P28 applied per component. Four expansions become three,
    and the next round designs the library side.
  - Keep it, recut it: Knowledge stays an expansion, but holds only the consult tools: the map, recall
    and the lexicon. Reuse entries, bug classes and research move into core memory, so reuse
    directives render on a core-only install.
  - Keep as designed: Knowledge stays an expansion holding the map, recall, gotchas, the lexicon and
    research consulting. Reuse entries render only where Knowledge is installed.
- Answer: One layer, two sides (Recommended).

The answer reopens layers round one's L2, whose answer was all four expansions.

**LB-1. "A confirmed finding that fits no bug class gets a `none` disposition. What must that `none`
carry?"**
- Offered:
  - A stated reason (Recommended): the reason is the record, the review report lists every `none`, and
    nothing waits on the owner.
  - Your ruling on each: each `none` becomes an owner item, held as `run.on-owner-question` says.
  - A class or a gate, always: `none` is refused, and every confirmed finding files a class or names a
    gate, the charter's left-shift rule taken literally.
- Answer: A class or a gate, always.

**LB-2. "Which units must state a reuse line (proposed <tag>, or none with a reason) when they
close?"**
- Offered:
  - Units that built a new seam (Recommended): only a unit whose spec's reuse audit says "no existing
    seam fits", today 256 specs in 67 builds, about 1.6 proposals per such build.
  - Every unit: every unit closes with `proposed <tag>` or `none` with its reason.
  - Only when you ask: no line is owed, and the owner names the features to enter.
- Answer: Units that built a new seam (Recommended).

**LB-3. "Who declares a decision major, so that it enters the decision log when its build lands?"**
- Offered:
  - Its author; you ratify at landing (Recommended): the author declares the class by the rubric, and
    each major row waits for the owner's ratification at `deploy.distill`.
  - Its author, by the rubric: no owner step, and the rubric and the class check decide.
  - Only you: only the owner's rulings can be major.
- Answer: Its author, by the rubric.

**LB-4. "The measurements point to two placements. Confirm them?"**
- Offered:
  - Both as measured (Recommended): dossiers stay with the map, an optional component, and the
    annotation index stays out of the core, where only `gov:feature` anchors are read, by a one-marker
    scan.
  - Merge dossiers into reuse entries: dossiers become core library records.
  - Make the annotation index core: a persisted index ships in the core.
- Answer: Both as measured (Recommended).

## [settled] What KN-1 changed, 2026-10-16

- **The layer model** (v2 `[layers]` and P28):
  - five core layers, and three expansions: observability, integrations and distribution;
  - memory is the trail and the library;
  - P28 governs a core layer's optional components as it governs expansions. One attaches only at an
    extension point its layer declares, a core render it fills is an optional slot, and the core
    never depends on it.
- **The sort:**
  - the trail, unchanged;
  - the library, core: major decisions, reuse entries, bug classes (the gotcha kind and its
    catalogue) and research records;
  - the optional components: the codebase-map kit, with its symbols, callers and dossiers; the
    memory-recall kit, with its index and journal; the lexicon kit, with its vocabulary and canon.
- **What moved with it:**
  - reuse entries render on every install, and `implements <reuse-entry>` is a core relation
    (layer-memory `[decisions]` and `[relations]`);
  - bug classes ride the builder's and reviewers' work orders in the core. The bug-class checklist is
    no longer a Build extension point, and `review.lens` and `review.left-shift` class findings from
    the catalogue (the step definitions);
  - the reuse slot's "not searched" state loses its "not installed" reason. Without the map, the house
    index holds the reuse entries alone, and the slot says so (layer-memory `[reuse]`);
  - the read hook under `annotations.grammar=pushed-at-read` is a pack of memory's optional components
    in Runtime's dispatcher;
  - `policy.on-missing-expansion` also covers a preset value whose optional component is absent;
  - `gap-found-17`'s evidence keeps the map's dossiers, and drops bug classes;
  - the chain is unchanged: dTotalRecall already owned the memory contract and Knowledge's stores, and
    dMindYourWords the lexicon.
- **Older records' wording.** Records written before 2026-10-16 that say Knowledge mean the library
  side and these optional components. Revision notes mark the live ones, and dated history keeps its
  words.

## [research] Dispatched, 2026-10-16

Dispatch 49 sent one researcher over the four filling paths and the two open placements. Its return is
saved verbatim in `build/2026-10-16-build-PLAY-dClosedLoop-1-research-library-paths.md`, and its
question is in `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-18-researcher.md`.

## [current] How the library fills today, measured 2026-10-16

Every path is filled by hand, and nothing notices when one is skipped:

| Path | Writer today | What lets it be skipped | Measured |
|---|---|---|---|
| A finding becomes a bug class | a class record, hand-written in a fold commit under the build method's prose rule | no check joins confirmed findings to classes | 183 of 907 confirmed findings in the 36 review appendices with a classes column carry a class; 13 of 124 class records cite the review or finding that filed them |
| A built feature becomes a reuse entry | nothing; the spec's reuse audit, dossier seams and the card's `**Reuse:**` field come nearest | nothing proposes an entry, and the card is untracked | 256 specs in 67 of 163 builds say "no existing seam fits" or "no seam fits", 236 the exact phrase; 4 of 20 stored cards fill `**Reuse:**`; `gov:feature` marks 0 code lines |
| A decision becomes a log row | hand edits to `memory/DECISIONS.md` | no rule requires a row, and nothing defines a major decision | 160 rows added in 60 days, beside 1,829 `Decided:` trailers |
| A build's research joins the library | the researcher's record, bound by `**Serves:** research` and graded by check 21 | across builds only recall reaches it, and recall is optional | 59 research returns in 10 builds, 8 of them cited from another build; the binding alone also covers design records, logs and registers, 179 records |

- **Dossiers hold little of what a reuse entry needs.** Their reuse-shaped part, `## Reuse affordance`,
  is 7.1% of their text. No dossier carries a directive or an owner's disposition, and 28 of 31 are
  stale by path ancestry.
- **No annotation index exists.** drift-audit builds a cited-id map at report time, which gates
  nothing, and each `gov:` marker kind is read by its own gate with a one-marker scan. A scan for
  `gov:feature` takes 0.048 s.
- **Two records contradict the code.** `ANNOTATION-STYLE.template.md` says no gate reads comment
  citations, though drift-audit's report-only signal does. `HYGIENE.md` lists a `note` kind that the
  catalogue never uses.

## [design] The library side, as proposed

**The library fills only at declared flow points.** Each path is an item, or a field of one, with a
witness a check reads. The views over the library are derived.

| Path | Where | Actor | Witness |
|---|---|---|---|
| A finding becomes a bug class | the review breakpoint: `review.report`, then `review.dispose` | the synthesizer gives each disposition; the fold's spec writer or the fix unit's builder files a new class | every confirmed finding carries one left-shift disposition, and each one resolves |
| A built feature becomes a reuse entry | Build: `build.unit-pass` | the builder proposes, and the owner disposes as LR-6 says | each unit that owes a reuse line carries one, and an accepted entry has its `gov:feature` anchor in code |
| A decision becomes a log row | Build: `build.distill`, before `build.exit`; Deploy's `deploy.distill` confirms the rows at the landed SHA | the command, from the build's resolved forks whose class is major | a one-to-one join between the build's classed forks and the rows of its major ones |
| A build's research joins the library | a derived view | none: the view renders from the research returns | the research-return kind's check, and the view's byte comparison |

### [left-shift] A finding becomes a bug class

- At `review.report`, the synthesizer gives every confirmed finding one left-shift disposition:
  - `class:<slug>`, an existing class;
  - `new:<slug>`, a class to file, with its symptom in one line;
  - `gate:<leg>`, a leg that already catches it;
  - `none`, with its reason, which `review.unclassed` refuses by default (LB-1): every confirmed
    finding files a class or names a gate.

  The harness's bare `C<n>` label is refused.
- `review.report`'s witness gains a join. Each confirmed finding carries one disposition, `class:`
  resolves to a record under `memory/gotchas/`, and `gate:` resolves to a leg in the legs manifest.
  `new:` names a slug no record held at the report's pinned SHA, or whose record carries `from:` this
  report and finding, so the join stays true once the class is filed. Under `reason` or `owner-rules`,
  `none` carries its reason, and under `owner-rules` each `none` is an owner item before dispose.
- At `review.dispose`, each `new:` is filed with the item that owes its record, and the join sits at
  that item. On an unbuilt spec, `review.fold`'s spec writer writes the class beside the fold. On built
  work, the builder of the fix unit writes it, in its write set. A finding that becomes an ask carries
  its `new:` slug, and the ask is accepted once the class record exists. The
  new class carries `from: <review>#<finding id>`, which `gotchas.py --check` resolves, and where the
  map is installed, the dossier of the feature it guards claims it.
- `review.left-shift` keeps its job: it decides when a class earns a gate, at its second occurrence by
  default.

### [reuse-proposal] A built feature becomes a reuse entry

- A unit whose spec's reuse audit records a new seam has built one. The audit's outcome becomes one
  token that the spec template, the hygiene check and this witness read through one predicate
  (`gap-design-05`), where today three phrasings pass the hygiene check. Its builder's
  return carries a reuse line: `proposed <tag>`, filed through the instruction command as LR-6 says,
  or `none` with its reason. Units that built a new seam owe the line (`reuse.propose: new-seam`, LB-2).
- `build.unit-pass`'s witness gains that line for each unit `reuse.propose` selects: under `every-unit`
  every unit, and under `owner-asks` a unit building a feature an owner-filed reuse ask names.
- A memory check reads the anchors. An accepted entry has at least one `gov:feature <tag>` in code, and
  a `removal-pending` entry has none left once its patch build lands. The check scans one marker, as
  each `gov:` gate does today.

### [log] A decision becomes a log row

- Each resolved fork's record carries its decision and its declared class: one of layer-memory
  `[decisions]`' classes, or major. Design writes the fork records, and `build.distill` checks each class.
- `build.distill`, a command before `build.exit`, appends a log row for each major fork to the log in
  the build's own branch, so the rows land with the build, and a withdrawn build's never do. Each row
  carries its date, its build, the decision, a pointer to its rationale, and the reuse entry it
  created, if any. It is idempotent: a row keyed by build and fork is never written twice.
- Its witness is a one-to-one join between the build's resolved forks and the rows of the major ones.
  A fork with no class is red, and so is a second row for one key. An empty set passes only where no
  fork was resolved. At landing, `deploy.distill` confirms the rows at the landed SHA. Its author declares a decision major, by the rubric (`decisions.major: author-rubric`,
  LB-3).

### [research-view] A build's research joins the library

- The research returns are the library. The `**Serves:** research` binding also covers design records,
  logs and registers, so the memory contract gives research returns their own kind, written by
  `plan.research` and `design.research`, and the view selects that kind.
- A generated research view lists them by build, date and question, beside the other views in
  layer-memory `[views]`. It is the planner's core source, and recall stays the optional slot that
  searches it.
- Its witness is the kind's check, seen red on a planted design record bound as research, and the view
  is byte-compared after rendering, like every view.

### [placements] The two placements, confirmed by LB-4

- **Dossiers stay with the map,** an optional component. A reuse entry would use 7.1% of a dossier's
  text. Where the map is installed, a dossier's `seam:` paragraph may seed a reuse proposal and cite
  the entry's tag.
- **The annotation index stays with the map and drift-audit.** The core needs only the `gov:feature`
  anchors, which a one-marker scan reads.

### [gaps-proposed] Registered 2026-10-16, after LB-1 to LB-4

- `gap-review-10` (MED, dFairHearing): left-shift has no witness. 724 of 907 confirmed findings carry
  no class and no disposition, and 13 of 124 class records cite the review that filed them.
- `gap-mem-15` (MED, dTotalRecall): no research view. Research is found across builds only through
  recall or by its file name, and 8 of 59 research returns are cited from another build.
- Extended:
  - `gap-mem-02`: nothing defines a major decision;
  - `gap-mem-03`: nothing proposes an entry, and `gov:feature` marks 0 code lines;
  - `gap-mem-11`: the two records above that contradict the code;
  - `gap-design-07`: its count of 7 research records predates the count of 59 research returns.

## [settled-lb] What LB-1 to LB-4 settled, 2026-10-16

Each answer is a policy whose default is the owner's answer. LB-4's placements are structural, so it
has no key:

| Fork | Key | Allowed values | Default |
|---|---|---|---|
| LB-1 | `review.unclassed` | refuse, reason, owner-rules | refuse |
| LB-2 | `reuse.propose` | new-seam, every-unit, owner-asks | new-seam |
| LB-3 | `decisions.major` | author-rubric, author-owner-ratifies, owner-only | author-rubric |

- **The step definitions:**
  - `review.report` gives every confirmed finding a left-shift disposition, and its witness joins each
    one to a class record or a leg. `review.dispose` files each new class with its fix;
  - `build.unit-pass`'s witness carries the reuse line of each unit that built a new seam;
  - `deploy.distill`, a new command after `deploy.record`, appends the build's major decisions to the
    log, and Deploy exits only once they are there. After the round's review, `build.distill` appends them
    before Test, and `deploy.distill` confirms them at the landed SHA (`[review-fold]`).
- **Memory:** layer-memory `[views]` gains the research view, `[decisions]` notes LB-3, and
  `[knowledge]` notes LB-1.
- **v2:** the three keys join the catalogue and every preset. The non-default presets were assigned by
  analogy with their neighbours: velocity takes the lighter value, and strict the heavier one.
- **The gaps:** `gap-review-10` joins dFairHearing and `gap-mem-15` joins dTotalRecall. `gap-mem-02`,
  `gap-mem-03`, `gap-mem-11` and `gap-design-07` are extended.
- **Corrected 2026-10-16** (the round's review, M11): LB-2's option said about 1.6 proposals per build
  that builds a new seam. The rate is about 3.8 per such build, 256 specs over 67 builds, and 1.6 per
  build overall, 256 over 163. The answer stands.

## [consult] The optional components, and the core without them

**Each component's own design is already settled.**
- The map's is layer-memory `[map]`: definitions for each declared language, import-aware Python
  callers, shell and JavaScript callers through extractor packs, cross-language edges, and freshness
  by tree hash.
- Recall's is layer-memory `[reuse]`: a record finder for "why" questions.
- The lexicon's re-engineering is dMindYourWords'.

This round adds what the core does when one is not installed.

**Every optional slot renders one of three states:** filled; searched with nothing found; or not
installed, with the core's fallback named. Absence never renders as an empty result, which would read
as a clean search.

| Component | Where the core reads it | Not installed: what the core does instead |
|---|---|---|
| The map | `design.seams`' sources | the reuse scout searches the plan's scope paths, with the reuse entries as its index, and the seams record names the map as absent |
| The map | the work order's `**Reuse:**` slot | the slot keeps its three states, and its index holds the reuse entries alone |
| The map | a new class's dossier claim, and a dossier `seam:` seeding a reuse proposal | nothing to claim or seed: a class reaches its population through its own anchors |
| The map | the owner's views `MAP.md`, `CARDS.md` and each symbol's callers | none rendered; `LIVE.md` and the build views stay |
| Recall | the planner's recall slot | the research view and the decision log, selected by the plan's scope tags |
| Recall | `design.seams`' recall sources | none; the scout's tree search stands |
| Recall | the read hook under `annotations.grammar=pushed-at-read` | the value cannot be served, so `policy.on-missing-expansion` refuses it, or under `fallback-reported` falls back to `required` and says so |
| Recall | the `/memory-recall` Skill and its journal | not rendered, and no journal is kept |
| The lexicon | naming at Design and Build | the core's tag-shape check stands alone, and the naming slot names the lexicon as absent |
| The lexicon | `lexicon.pin` | inert, and reported as inert when set |
| The lexicon | the `/lexicon` Skill | not rendered |
| Recall | check 27's near-match ranking of added decision rows and gotchas, and the decision log's holds-now view | no fallback is owed: both move into memory-tree, the core engine, as the id grammar's parser does (layer-memory `[names]`), and memory-recall imports them (dTotalRecall) |

- **Each component's own legs install with it.** Without the map, its coverage and freshness legs are
  absent from the legs manifest, not skipped.
- **The witness is the work order.** Each optional slot carries one of the three states, and a
  not-installed state names its fallback. The installed set is Distribution's, and dBoundRoles
  renders the slots (layer-instruction `[settled]`). `gap-found-17`'s fix covers the mechanism, so no
  new gap is owed.

## [review] Dispatched, 2026-10-16

Dispatch 50, run as `wf_9d4cc07b-2f2`: a light diff review over the round's four commits,
`1bc4883fe..aa9639d98`, at the closing-review roles' declared effort. Its context excludes the atlas
page and its generator by pathspec. Its args, verbatim:

```json
{
 "kind": "diff-review",
 "base": "1bc4883fec8a8d55147b586645f2709c3b023a3d",
 "head": "aa9639d98d0521dbfd8a8e0edc480f4e9ae361c8",
 "repo": "C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297",
 "intensity": "light",
 "reviewDir": "memory/builds/dClosedLoop/reviews",
 "roles": {
  "diffFinder": "gov-diff-reviewer",
  "skeptic": "gov-skeptic",
  "synthesis": "gov-synthesizer"
 },
 "efforts": {
  "diffFinder": "high",
  "skeptic": "high",
  "synthesis": "high"
 },
 "specs": [
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md",
  "memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-library-paths.md",
  "memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md"
 ],
 "context": "The diff is the library round of build dClosedLoop, a design-only build that re-architects gov onto one loop. It holds four commits. c7a2198f3 folds Knowledge into the memory layer as its library side after the owner's KN-1: v2's [layers] and P28, dated notes in the instruction, flow, step, runtime and memory records, and gap-found-17. 2fd75e8e2 records the atlas, dispatch 49 and the codebase map's claims for three bug classes. 3c34b82dc files dispatch 49's research and settles the owner's LB-1 to LB-4 into the step definitions (review.report, review.dispose, build.unit-pass and a new deploy.distill), layer-memory, v2's catalogue and presets, and the gap register. aa9639d98 adds the consult design. The round's design record is memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md: the owner's words, KN-1 and LB-1 to LB-4 with their answers in [forks], what each settled in [settled] and [settled-lb], the measurements in [current], and the design in [design] and [consult]. The research behind it is memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-library-paths.md. Read the diff without the atlas page and its generator, which are an owner-facing view outside this review: git -C C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297 diff 1bc4883fec8a8d55147b586645f2709c3b023a3d...aa9639d98d0521dbfd8a8e0edc480f4e9ae361c8 -- . ':(exclude)memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html' ':(exclude)memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py'. Review for four things: (1) a statement KN-1's fold left standing that still treats Knowledge as an expansion, or that contradicts the new layer model or P28 as amended; (2) a library flow point whose actor cannot produce its witness, or whose item, route or policy key the transition table, the step's policy list or a preset lacks; (3) a settled answer (KN-1, LB-1 to LB-4) misapplied, or a placement contradicted elsewhere; (4) design text that is wrong about the tree: a seam, file, line, key, check or count that does not exist or says otherwise. Write the report to memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md. Its head carries an H1, then, within its first twelve lines, the line `**Serves:** diff-review PLAY-dClosedLoop-1`. It carries exactly one `## Verdict:` line, whose token is CLEAN, CLEAN WITH FIXES or BLOCKED and nothing else.",
 "byDesign": "- The build is design-only: no product code and no unit specs. Unit-level detail is absent by design and owed to the chain builds.\n- The owner's settled answers (KN-1, LB-1 to LB-4, and the earlier F*, R-*, RT-* and LR-*) are decisions: a finding may show that one contradicts a record or the tree, but does not re-argue the owner's choice.\n- The non-default preset values of review.unclassed, reuse.propose and decisions.major were assigned by analogy, as layer-library [settled-lb] says: a finding may show one inconsistent with its preset, not that it is unasked.\n- Dated records keep what held when they were written: research returns (the library research record is dispatch 49's return, verbatim), snapshots, revision notes and the session log's past entries.\n- Generated files (memory/LIVE.md, the build README's generated regions and memory/map/generated/) are rendered and not under review.\n- The atlas page and its generator are an owner-facing view outside this review.",
 "checklist": "# recurring-bug-class checklist for 1bc4883fe..aa9639d98 (20 changed file(s))\n# 10 class(es) selected by an anchor + 6 universal\n# by anchor specificity: 3 path · 4 directory · 3 basename; a cut tier prints one line per class\n# invariants are read at 1bc4883fec8a; 0 that this subject adds, edits or takes out are listed as items, never by design\n\n- [ ] fixture-passes-by-finding-nothing (universal)\n      a test arm whose fixture never triggers the rule passes, and proves nothing\n      memory/gotchas/fixture-passes-by-finding-nothing.md\n\n- [ ] guard-above-a-fold-makes-its-fallback-dead (universal)\n      a guard added above a fold settles the predicate the fold's own fallback re-tests, leaving a dead arm that reads as coverage\n      memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md\n\n- [ ] heredoc-escape-reaches-the-regex (universal)\n      source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem\n      memory/gotchas/heredoc-escape-reaches-the-regex.md\n\n- [ ] inline-fence-swallows-the-rest-of-the-file (universal)\n      a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view\n      memory/gotchas/inline-fence-swallows-the-rest-of-the-file.md\n\n- [ ] staged-break-substitutes-a-synthetic-value (universal)\n      an arm that proves a mechanism by replacing the shipped value with a simpler one proves the mechanism for the simpler value\n      memory/gotchas/staged-break-substitutes-a-synthetic-value.md\n\n- [ ] two-answers-to-one-question (universal)\n      a fact stated in two places drifts, and the copies need not disagree loudly to be wrong\n      memory/gotchas/two-answers-to-one-question.md\n\n- [ ] parser-drops-rows-it-cannot-place (path)\n      a record-parsing instrument skips rows under a heading it does not know, or rows its pattern cannot read, and still prints a clean run, so its population shrinks without a word\n      memory/gotchas/parser-drops-rows-it-cannot-place.md\n\n- [ ] owner-item-without-its-reject-outcome (path)\n      a design hands a decision to the owner and routes only the yes, so a no leaves landed work with no route and a check that turns red on the default branch\n      memory/gotchas/owner-item-without-its-reject-outcome.md\n\n- [ ] route-names-an-output-its-actor-never-emits (path)\n      a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever\n      memory/gotchas/route-names-an-output-its-actor-never-emits.md\n\n- [ ] a-merge-of-the-default-branch-read-as-additions (directory)\n      a check that lists the files a range or a commit ADDS reads a merge of the default branch into a feature branch as adding every file the default branch gained, unless its git invocation is one of the shapes that cannot\n      memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md\n\n- [ ] amendment-leaves-its-other-half-standing (directory)\n      a criterion is amended and the clause, scope item or log line that only made sense under the old wording is left behind, so one rule now returns two verdicts\n      memory/gotchas/amendment-leaves-its-other-half-standing.md\n\n- [ ] ledger-token-wrapped-across-a-line-joins-nothing (directory)\n      hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered\n      memory/gotchas/ledger-token-wrapped-across-a-line-joins-nothing.md\n\n- [ ] retirement-inventory-misses-readers-by-value (directory)\n      an inventory of what reads a retired thing, built by searching for its name, misses every assertion on a count or a value that thing carries, because those name nothing\n      memory/gotchas/retirement-inventory-misses-readers-by-value.md\n\n- [ ] record-without-serves-or-with-a-round-counter (basename)\n      a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines\n      memory/gotchas/record-without-serves-or-with-a-round-counter.md\n\n- [ ] a-folded-field-leaves-its-row-shape-docs-behind (basename)\n      a review fold adds a key to a declared row shape in the code and its gate, and the spec body and the README that describe that shape keep the old key set\n      memory/gotchas/a-folded-field-leaves-its-row-shape-docs-behind.md\n\n- [ ] git-rm-cached-refuses-a-diverged-index-blob (basename)\n      `git rm --cached` refuses a path whose index blob differs from both HEAD and the worktree, so a fixture cleanup without `-f` silently leaves the file staged and the next arm measures the wrong fixture\n      memory/gotchas/git-rm-cached-refuses-a-diverged-index-blob.md\n\n# by design — 0 invariant(s) this selection touches\n"
}
```

## [review-fold] The round's review, folded 2026-10-16

Dispatch 50 reviewed the round's four commits, `1bc4883fe..aa9639d98`, at light intensity
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`): CLEAN WITH FIXES, 25 of 31 findings confirmed, in 19 items. Ids 16, 19,
20, 23, 27 and 31 were refuted. Each item went here:

| Item | Ids | Disposition | Where the fix sits | Its class |
|---|---|---|---|---|
| H1 | 12 | fixed | `build.distill` joins one to one over the build's resolved forks, each with its class declared, which Design's fork records carry; an empty set passes only where no fork was resolved | `vacuous-selector-empty-population` |
| M1 | 1, 17, 29 | fixed | `review.report` gains the `none` arm under `reason` and `owner-rules`, and the owner route under `owner-rules` | `policy-value-with-no-route`, new |
| M2 | 3, 13, 28 | fixed | the owner's ratification before `build.distill` under `author-owner-ratifies`, in Build's Breakpoints, each outcome routed | `owner-item-without-its-reject-outcome` |
| M3 | 2, 25 | fixed | the class record joins at `review.fold` or at the fix unit's `build.unit-pass`, and an ask carries its `new:` slug | `route-names-an-output-its-actor-never-emits` |
| M4 | 26 | fixed | `new:` is judged at the report's pinned SHA, or by the record's `from:` | `witness-graded-against-a-fact-written-after-it` |
| M5 | 5 | fixed | `build.distill` is idempotent, keyed by build and fork, and its join refuses a second row | `append-without-an-idempotence-key`, new |
| M6 | 14 | fixed | the rows are written in the build's branch before Test, `deploy.distill` confirms them at the landed SHA, and Deploy's Memory line reads them | `route-names-an-output-its-actor-never-emits` |
| M7 | 4 | fixed | `build.unit-pass`'s witness takes its population from `reuse.propose`, each value's arm named | `policy-value-with-no-route`, new |
| M8 | 30 | fixed, gap | the reuse audit's outcome becomes one token read through one predicate (`gap-design-05`) | `two-answers-to-one-question` |
| M9 | 7 | fixed | v2's dBoundRoles row renders bug classes as a core field | `amendment-leaves-its-other-half-standing` |
| M10 | 8 | fixed | v2 `[layers]` and layer-instruction state the slot's three states | `amendment-leaves-its-other-half-standing` |
| M11 | 10 | fixed | a dated correction in `[settled-lb]`: about 3.8 per build that builds a new seam, 1.6 per build overall; the answer stands | `rate-quoted-without-its-denominator`, new |
| M12 | 15 | fixed, gap | `[consult]` names check 27 and the holds-now view, both moving into memory-tree by v2's dTotalRecall row (`gap-found-17`) | `retirement-inventory-misses-readers-by-value` |
| M13 | 18, 24 | fixed, gap | the research view selects a research-return kind; 59 returns in 10 builds, 8 cited from another build (`gap-mem-15`, `gap-design-07`) | `two-answers-to-one-question` |
| M14 | 22 | fixed | five index rows moved from the session log's Dispatches table to its Records index, and the follow-up review's row, which a presence check never added, added | `insert-after-a-key-that-occurs-twice`, new |
| L1 | 6 | fixed | the Plan, Design, Build and Deploy Memory lines carry the library's reads and writes | `amendment-leaves-its-other-half-standing` |
| L2 | 9 | fixed | v2's dOrderedCharter row covers optional components, with a planted red case owed | `amendment-leaves-its-other-half-standing` |
| L3 | 11 | fixed | the register's re-measure block: Review=10, Memory=15, Deploy=9; LOW=22, MED=70, HIGH=79 | `two-answers-to-one-question` |
| L4 | 21 | fixed | layer-memory `[contract]` states LB-4's placement | `amendment-leaves-its-other-half-standing` |

- **The method held.** The fold states each contract. The tool-level detail sits in the owning
  builds' planned units and gaps: dTotalRecall's row, `gap-design-05`, `gap-found-17` and
  `gap-flow-15`.
- **The left-shift.** Four classes are new under `memory/gotchas/`, each claimed in its feature's
  dossier. `route-names-an-output-its-actor-never-emits` and `owner-item-without-its-reject-outcome`
  gained the review's checklist entries.
- **The fold is unreviewed text.** A follow-up round over it is the owner's call.

## [open] What the library round owes

- **A follow-up round** over `[review-fold]`, if the owner asks for one.
