# The night pass: the owner's eight points, worked unattended

**Serves:** research PLAY-dClosedLoop-1

During the walk, after wave 1 was presented, the owner handed over eight points, to be reviewed, checked against
the design, and worked into it where needed. The owner then stepped away for the night. This record holds the words,
what the design already held on each point, the research, the design worked in, and the forks parked for the
owner's return.

## [words] The owner's words, 2026-10-18

> I need several important pieces of the architecture reviewed, clarified if they're currently part of the design, and worked into it if necessary. I'm stepping away for the night, so this design pass is continuing unattended. Do what's necessary to go through each of my points step by step, understand their viability and work them into the project. Use medium effort agents and workflows as necessary to assist you and speed things up:
> 1. By default, UNATTENDED should be the state enforced by Gov. Currently, 'unattended' is one of the kits, invoked independently at any point in a session by the owner. However, as a separate kit it seems to be superfluous in the new state of the product, and should be part of the core flow. The owner should still be able to go attended by using an override request or a policy flag (but that should only affect owner confirmations and interactions, not the flow or role use), at which point Gov should explain to user which step and role at the flow its going to take. Slug or playbook (but the unattended drive should still keep playbook functionality and we will later expland on it) unattended modes are no longer necessary, all builds are prompt-driven - its the job for the driver to figure out the state of a loop and pick the right step or action (playbook mode using playbooks to perform repeatable/cyclic workflows should still be a part of the flow).
> 2. the 'testing' step doesn't seem to be correctly represented in the flow - it currently bounces between 'deploying' and 'building', however, a testing step may be necessary anywhere in th flow, depending on the user request. Examples: user's observations may need to be verified visually or in the code, which is part of the testing step; an experiment may have to be performed (eg. reuse workflow shapes from aScoutedSeam) prior to establishing a build's baseline, etc. Testing scenarios may be necessary at any point of the flow and the driver must be aware of that, roles need to be able to work a problem out by testing and hand their results further down.
> 3. Memory structure and its mandatory parts - holistic high level project map we reviewed previously and its connection to codebase-map kit - seems to be mandatory to integrate it with the core and use it to shape the map mechanically + an agent workflow on top of it to enrich. One of the bigger problem this kit hasn't solved yet is constant and consistent orientation - a spec-writer, or a builder should not be blind to the existing code a feature they're working on touches. Orientation scounts, prompt writers, researchers should have a clear, full-picture view to the codebase and its internal relations when understanding a user's request.
> 4. The way memory interconnects between itself and instructs the agents that read it - with intruction layer, code annotations, builds, decisions, codebase map, generated indices and tags - should be establish a clear relational syntax across the entire memory? If relevant parts scattered across a large repo were wrapped in the relational tags, instructions, and pointers that were feature-unique, short and efficient - orienting quickly would be a matter of pulling a tag and reading the enclosed regions and the instructions that come with them.
> 5. https://jsmanifest.com/claude-code-session-compaction-2026 this article talks about creating memory that survives session compaction - are there any practices we can inherit from it to keep the most important pieces (orientation card, map, build instructions) surviving no matter what? Are there any reliable solutions to memory management?
> 6. Anthropic has recently released an AI-native SDLC playbook: https://claude.com/resources/articles/the-ai-native-sdlc-playbook which seems to be relevant to the Gov rearchitecture we've committed to. Can any of the described practices be useful to this product?
> 7. Atlas still shows Lexicon and Review System as 'in review' - is that the case?
> 8. The inventory and mapping of the current Gov tools and their functionality - has it been done at any stage, is it helpful? We need a clear understanding of how the current kit is getting rebuilt under the new architecture - what functions stay and different shape, which functions go, what tools will stay, what tools with disappear?
>
> Don't stop until you've worked out each step, once you have - prepare a report for me on this and a resulting state of the project, and park all the forks for me to go at once when I return.

- **How the pass runs:** each point is checked against the design first, researched where it needs evidence from
  outside the records, then worked in. A choice the owner's words leave open becomes a parked fork, with its options
  and a recommendation, never an answer. The walk's wave 1 stays open: the owner has not yet given a read on it.
- **What the pass does not do:** no product code, no merge, no push, and no status change to a build or an ask. The
  build's exit still waits for the owner's word that the design has its full shape.

## [research] Dispatched, 2026-10-18

Five researchers ran at the owner's medium effort, read-only, one point each. Points 5 to 7 were worked in this session
directly. Each handoff is in `prompts/`, and each return is saved verbatim beside this record.

| Dispatch | Point | Handoff | Return | Outcome |
|---|---|---|---|---|
| 100 | 1, unattended as the core flow | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-4-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-unattended-core.md` | one driver with attendance on the breakpoint seam; playbook mode seated by `repeat` |
| 101 | 2, testing anywhere | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-5-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-testing-anywhere.md` | one probe program with two ways in; four other mechanisms each lost a test |
| 102 | 3, code depth in the core | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-6-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-code-orientation.md` | a core code record, a per-item code slot, `git grep` as the floor |
| 103 | 4, one relational syntax | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-7-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-relational-syntax.md` | declare at the site, derive the rest; four other mechanisms each lost a test |
| 104 | 8, today's tools and their fates | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-8-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-tool-fates.md` | 118 function rows, 11 undecided; the kit-level map stale in nine rows |

- **A harness notice on two returns.** The returns of dispatches 100 and 104 matched the harness's instruction-shaped
  patterns, one for naming `--dangerously-skip-permissions` and one for naming `.claude/settings.json`. Both are
  findings, not instructions. The first is `tools/unattended/resume-tick.sh`'s launch line, which layer-runtime
  `[current]` already records and which has never run (0 launches). The second is the hook wiring the fates table
  cites. Nothing in either was acted on as an instruction.

## [p1-unattended] Point 1: unattended by default, as the core flow

**What the design held** (dispatch 100):
- `autonomy: plan-only` with `plan.ratification: request`: the request is the mandate, and the default flow has no
  owner turn.
- Almost every function of the unattended kit already had a home:
  - its position ladder in dDeclaredLoop's position engine, and in dWellOiledMachine's `next`;
  - its transitions and claims in the loop kit;
  - its hold, resume and abort in the owner's controls;
  - `resume-tick.sh` as the supervisor's seam, and its hooks as dispatcher packs;
  - its asks in Plan's triage, and its guides as rendered views.
- Three parts had none: the recipe half (playbook mode), `--attest`, and the mandate's ANCHOR_SCOPE and AUTH_PARAM.

**Where the design broke the owner's rule.** It let attendance change the driver and the binding:
- `layer-runtime` `[terms]` and `[decide]` made the owner's session the driver while the owner attended;
- `layer-runtime` `[act]` let an attended owner's session keep its freedom from act binding and allowances, so P25
  went unenforced while the owner attended;
- today's code shows the cost. Attended builds lose five of the driver's checks
  (`tools/workflows/unattended-build.js:49-61`), and the closing review ran on 29 of 59 attended builds against 86 of
  89 unattended ones (gap-build-02).

**Worked in:**
1. **Unattended is the state, and the kit dissolves into the core.**
   - Every run is a placed request. The driver derives the build's position from witnesses (`next`, P22) and picks
     the step and the action.
   - No slug, playbook or ask mode starts a run.
   - The kit's parts go to the loop kit (dDeclaredLoop) and to the runtime's own kit (dWellOiledMachine).
   - `/unattended` stays a thin client of `run` until dConvergedCharter retires it (NP-4).
   - P4, P20 and P25 now say so.
2. **Attendance is one switch, and only an interaction switch.**
   - `attendance` is `unattended` by default, in the owner's words. It is set in the policy file, or by an attend
     request, which writes an `override` record scoped by `attendance.scope`.
   - While the owner attends, gov announces each act's step and role, confirms at the breakpoints the value
     places, and asks owner questions live.
   - The attendance rule's arm refuses any value that changes an item's actor, the driver or a binding
     (dDeclaredLoop).
   - Dispatch 100's three candidates:
     - **one driver, with attendance on the breakpoint seam:** passed its losing test on the records;
     - **attended as a kind of session:** lost to the runtime text and the code above;
     - **a bundle of owner-valued keys:** lost. About 30 keys carry an owner option, and `placement: owner-places`
       swaps an item's actor.
3. **One driver, bound the same way in every mode.**
   - The supervisor drives every build, and the owner's session is its client.
   - Until dWellOiledMachine lands, the owner's session hosts the same driver program, bound as an act session
     (NP-1).
   - The platform spike is its owed test (v2 `[owed]`).
4. **The announcement.** Before each act while attended, and once when attendance begins, gov prints
   `step — <build> · <step> · <item> · <role> · <why> · writes <set>`. It is rendered from `next` and the item's
   declaration, and never typed by a model.
5. **Prompt-driven placement covers every start.** `entry.place` already places every request. Two additions:
   - the `repeat` disposition, onto a playbook;
   - intake for a prompt that reaches no owner session.
6. **Playbook mode stays in the flow.**
   - A playbook is a design record kind carrying dScriptedRepeat's canon (dIndexedDesign).
   - Following one is the `repeat` disposition. It enters Design as a patch build does, and the playbook supplies
     the feature design.
   - Its pieces are built as units (dScopedBuild), and Test runs the set check (dWitnessedBar).
   - A cyclic playbook is a cadence item that files `repeat` intakes (dTendedCadence).
   - The owner will expand it later; this is its seat.
7. **Rejected from dispatch 100: dropping "attended briefs gated" from dRankedPlan.** That clause gates attended
   briefs as run-built ones are (gap-plan-07), which is the owner's rule, not an exception to it.
8. **Terms.** The session binding record now says "owner" for the session the owner types in, since attendance is a
   mode and not a kind of session. The other overloads, of attended, playbook and baseline, are gap-lex-09's.

Gaps: gap-flow-16, gap-flow-17, gap-rt-22, gap-orient-16, gap-orient-17, gap-lex-09 and gap-tool-08.

## [p2-testing] Point 2: testing wherever the work needs it

**What the design held** (dispatch 101). Testing happened in four places:
- Test's landing verdict;
- the read-only research items;
- the skeptic's refute probes;
- the executor's acceptance re-runs.

What it could not do:
- 61 of the 81 items have no role that could ask for a test;
- no role could run an experiment that writes, and no tester agent exists;
- the unattended driver's pre-spec TESTING position (`tools/unattended/unattended.sh:852`) never reached the design;
- today's visual check of the atlas was done by hand, and recorded as prose.

**Worked in** (P31; flow-steps `[probe]`):
1. **One probe program, with two ways in.**
   - Placed at any item boundary, as a breakpoint is placed: by the driver, the owner or a policy (`probe.points`,
     `probe.observations`).
   - Raised by any role as the outcome of its item, as research is routed (`probe.raise`).
   - `next` returns the probe as the frontier while the asker waits, so the driver always knows a test is owed.
2. **Three kinds:**
   - a verification checks a claim at a pinned SHA, such as an owner's observation, in the code or on screen;
   - a reproduction makes a reported bug red before its fix;
   - an experiment compares variants over a pre-registered corpus, and yields the measured reference later
     acceptance cites.
3. **Its record is handed down.** The probe record holds:
   - the question, the kind and the subject's SHA;
   - the method, and the losing outcome, committed before the run;
   - the outputs by hash;
   - the verdict, from a closed set, and who judged it.

   It returns to the asking item as an input (P26).
4. **Its witness is computed** (P2). The executor re-runs the commands, or the scorer re-derives an experiment's
   figures. An agent's judgment, of a screenshot say, is claimed, and routes only to an owner item.
5. **Test stays the landing verdict,** the one test that gates a landing.
6. **The experiment shape comes from aScoutedSeam's benchmark,** designed in and never counted on.
   - Its parts: a pinned corpus with controls and decoys, blinding, variants on one schema, a bounded fan, a
     deterministic scorer, a blind judge, and re-runs keyed by variant and effort.
   - It registers as a fifth shape kind, `experiment`.
   - Its scorer becomes a factory, because `review_replay.py` is a second instance of it (dFairHearing).
7. **Visual verification.**
   - Each harness adapter's capability table gains a measured `browser` row, and dWellOiledMachine adds a visual
     capture adapter.
   - The witness is a set of deterministic DOM, console and layout assertions, re-runnable at the pinned SHA.
8. **The tester agent** is defined by dBoundRoles. Every role's return template gains the `probe` outcome.

**Dispatch 101's candidates,** each against its losing test:
- **a boundary point alone:** lost. A role mid-item cannot obtain a result and continue.
- **Test as a re-entrant step:** lost. Its program needs a built range.
- **static items in every step:** lost. They cover only declared positions.
- **a role-raised probe alone:** lost. 61 items have no role.
- **the two ways in together:** survived.

**Two choices made against the return:**
- seen-red stays Test's own record kind, not a probe kind, which leaves gap-test-06's recorder where it is;
- an experiment's probe record is the measured reference, so no second kind is minted, and "baseline" keeps
  retrofit's meaning (gap-lex-09).

Gaps: gap-flow-18, gap-roles-21, gap-rt-23 and gap-test-18.

## [p3-code] Point 3: every role sees the code its item touches

**What the design held** (dispatch 102):
- **Code depth was optional.** The level-0 map sat in core memory (PM-2). But code depth (symbols, callers and
  dossiers) came only through an optional slot, `map.code`, which no chain row and no slot list declared.
- **Few roles saw code.**
  - Only the reuse scout was designed to see callers, and only with the optional kit installed.
  - The researcher and the prompt writer got no map at all.
  - A spec writer and a builder got no neighbourhood of the code their unit changes. One recent unit's spec writer
    made 80 code lookups, and its builder 45.
- **Today's code index is thin.**
  - `symbols.json` holds 4,670 public module-level names, with no line ranges.
  - No caller index is committed.
  - 25 of the 31 dossiers are stale.

**Worked in** (P32; v2's dTotalRecall, dBoundRoles, dDeclaredLoop and dOrderedCharter rows):
1. **A core `code` record,** derived mechanically per blob and cached by tree hash.
   - It holds files, definitions with their ranges and body hashes, imports, resolved calls, cross-language and
     registry edges, tests and kit membership.
   - It replaces the optional symbols and callers.
   - Measured on this tree with no new dependency: 13.1 s cold and 941 KB, under its losing test's 30 s and 1 MB.
2. **A `code` slot per item,** computed from the item's declared seed: its write set, its scope paths, or its
   question's paths.
   - It holds the seed's definitions with their ranges, their callers, callees and tests, and their kit's siblings.
   - It hands ranges, never bodies, under `memory.code-budget`.
   - On the unit dispatch 102 replayed, the one-hop neighbourhood held, in 5 KB, 16 of the 20 files its spec writer
     read and all 12 of its builder's.
3. **An agent workflow enriches it.**
   - Purposes come first from docstrings and headers, which 69% of definitions have.
   - An agent's pass writes the rest.
   - Each purpose is keyed to its definition's body hash. Keyed by file, it would rot: 60% of files change in a
     week, against 3.4% of definition bodies.
4. **`git grep` is the floor,** for any language with no extractor and for the population hunts no map answers.
5. **Who gets it:** the spec writer, builder, researcher, architect and reviewer, and the prompt writer through its
   actor (`memory.code-roles`). The map's delivery table now includes the researcher and the prompt writer.
6. **Level 0 holds one counted `code` line,** never a line per file. The map stands at 31,133 of its 32,768 B.

**This partly reverses KN-1,** which made the codebase map an optional component.
- The owner's words make code depth mandatory, so this pass reads them as the decision.
- The map's owner views and the dossier's prose stay optional, as do recall and the lexicon.

Gaps: gap-mem-28, gap-mem-29, gap-mem-30 and gap-roles-22.

## [p4-relations] Point 4: one relational syntax across memory

**The answer is yes, and half of it was already built.** Dispatch 103 measured today's pointers:
- section tags: 563 definitions, none outside dClosedLoop, and a third of their 3,696 citations ambiguous;
- item tags and ids;
- five region-marker families, with five separate parsers;
- paths, and 10,655 file:line citations, of which a sample found 6 in 60 still on their line;
- dossier claims, and the map's relation keys.

Orienting on one feature, `roles`, took about 42 calls and 734 KB read whole. Its bare name hit 44 code files, of
which 16 were real readers.

What the designed tag system already gives: one grammar, one index and one resolver (`gov tag show`, `where`,
`refs`). What it lacked: a bundle, region extents in code, feature-scoped instructions, and a closed set of typed
edges.

**Worked in** (P33; v2's dOrderedCharter, dTotalRecall, dBoundRoles, dWitnessedBar, dIndexedDesign and dTendedCadence
rows):
1. **Declare at the site, derive the rest.**
   - Each fact's edge is declared once, where the fact lives: a dossier's globs, `gov:feature` and `gov:note`, a
     record's `## [tag]`, an instruction unit's scope, a leg's fields, a decision row.
   - Every inverse is derived, and so are spans, uses, citations and bundles.
2. **One closed edge set.** Twelve are declared: `part-of`, `implements`, `tests`, `decides`, `instructs`,
   `enforces`, `after`, `supersedes`, `amends`, `patches`, `owner` and `layer`. One, `cites`, is derived. An
   unregistered type reds.
3. **Spans.** A region is its definition's extent where one derives, and an explicit `gov:end <tag>` closes it only
   where none does. The other span mechanisms each lost a test:
   - **wrapping every region by hand** lost. 32 of the 57 outside spans of `roles` are single-line uses the map
     derives, and wrapping them costs 114 marker lines around 212 lines of code;
   - **spans from definitions alone** lost. 68% sit in no derivable definition;
   - **line spans in a sidecar** lost hardest. 88.9% had shifted within 30 days.

   NP-12 keeps the owner's own idea, explicit regions everywhere, as an option.
4. **`gov tag bundle <tag>`** returns one manifest.
   - The node comes first, then every inbound edge grouped by type.
   - Each row reads `path:span · type · bytes`, and its content is pulled per row.
   - The `roles` bundle runs about 44 rows unfolded, and 39 with its kit folded.
5. **Instructions attach to a tag.** `feature` becomes an instruction selector, armed by dTotalRecall when it
   registers the namespace. Pulling a feature's tag brings its instructions with its regions.
6. **file:line citations** join the positional population. New text cites `path#symbol` or a blob-pinned line, as
   NP-17 settles.

Gaps: gap-found-24, gap-found-25, gap-found-26, gap-mem-31, gap-mem-32 and gap-mem-33.

## [p5-compaction] Point 5: memory that survives a compaction

**The article** (`https://jsmanifest.com/claude-code-session-compaction-2026`, read 2026-10-18 through the fetch tool's
summary, never verbatim):
- **Its claims about the mechanics:** automatic compaction near 80% of the window, the opening and the most recent
  turns kept, the middle summarized by a smaller model that drops qualifiers, rejected approaches, analysed edge cases
  and conversational configuration.
- **Its practices:** a structured constraints file read at every start, a decision log, snapshots at milestones, tests
  as executable documentation, pruning, manual compaction at phase boundaries under a retention policy, a test
  question after each compaction, logging compaction events, and token discipline.
- **What it lacks:** it names no harness hook, and its compaction event and retention API are illustrative, with no
  documentation cited. The author discloses a commercial interest.

**What the design already holds:**

| The article's practice | The design | Where |
|---|---|---|
| A constraints file read at every start | the charter at level 0, which the harness re-reads from disk after a compaction; the build's card | P15; dOrderedCharter; dDeclaredLoop unit 16 |
| A decision log | every owner word recorded verbatim; decision records; `DECISIONS.md` narrowed to major decisions | dTotalRecall; `build.distill` |
| Snapshots at milestones | the card as a ref on the remote, snapshotted and re-keyed; witnesses in git | dDeclaredLoop unit 16 |
| Tests as executable documentation | gates, each seen red | `[gate]`; dWitnessedBar |
| Pruning | memory keeps only what cannot be derived; shrink-only pins | `[memory]`; hygiene |
| Rejected approaches lost | forks recorded with the options offered; the card's pointers carry the open forks | `card.pointers` (CX-1) |
| Manual compaction at a phase boundary | a session ends at the next item boundary past `context.threshold` and continues fresh from the card | `context.on-full: fresh-at-boundary` (RT-1) |
| A retention policy | the keep-list and the PreCompact flush | dWellOiledMachine unit 12 |
| A test question after each compaction | position re-derived from witnesses; a summary is a lead, never a source | P22, P23; dDeclaredLoop unit 29 |
| Token discipline | load is precise; budgets per reader | `[tokens]`, P27 |

The design's own experiment went further than the article (`2026-10-15-build-PLAY-dClosedLoop-1-compaction-results.md`).
It measured what a summary keeps, decisions, and what it drops, evidence: 1 of 7 identifiers and 1 of 9 numbers came
back. It found that only the hook's replay came back exact.

**Reliable memory management, the answer.** Three channels survive a compaction by construction, because the harness
re-sends them from disk rather than from the summary. All three came back after this session's own compaction on
2026-10-18:
- the instruction files, `CLAUDE.md` and its import of `AGENTS.md`;
- the auto-memory index;
- a SessionStart hook's output under the `compact` matcher, which here re-injected the card.

Everything else rides the summary, which the experiment measured as lossy, and the project map's
`[reload-summary]` caught rewriting 3 of the map's 355 lines. So "surviving no matter what" means two things:
- everything that must survive is rendered from disk into one of those channels at the moment of the compaction;
- everything else is a pointer to a record.

A memory server or a vector store does no better. Retrieval needs the session to know what to ask for, and the
experiment's losses are facts the session no longer knows it lacks.

**What the pass adds:**
1. **The replay carries the whole default load.** The compact and resume hooks render `memory.default-load`'s set from
   disk at that moment, the card and the level-0 map by default (PM-7), not the card alone. Today the map comes back
   only because the owner's standing ask makes the session regenerate and read it by hand. dWellOiledMachine's units 12
   and 23 join: the session-start hook loads the set at startup, at resume and at a compaction.
2. **The replay ends with `next`'s line, computed at that moment.** The first position the session reads after a
   compaction is derived, not summarized (P22). dWellOiledMachine, which owns `next`.
3. **A compaction is journaled.** The compact hook writes a journal line: the session, the build, the item in flight
   and the trigger. The Loop Review counts compactions per item kind, because an item that compacts mid-flight is
   sized wrong (the experiment's conclusion 8). The line is dWellOiledMachine's, and the count dCalibratedLens's.
4. **Owed, a measurement.** The hook channel's size cap, measured with a 32 KiB map, so the default load is sized to
   come back whole. It joins CX-3's owed checks in v2 `[owed]`.
5. **The keep-list names what the experiment lost:** handles (SHAs, ids, file:line), each decision's condition,
   rejected options and open forks.

Each addition serves a key the owner has answered (`memory.default-load`, PM-7; `context.on-full`, RT-1), so none is a
fork.

## [p6-sdlc] Point 6: Anthropic's AI-native SDLC playbook

**The playbook** (`https://claude.com/resources/articles/the-ai-native-sdlc-playbook`, read 2026-10-18 through the
fetch tool's summary):
- **Its stages:** six, not run in a fixed order: Plan, Design, Build, Test, Deploy and Maintain.
- **Its hand-off:** each stage commits an artifact that the next one reads: the intent, the spec, the plan, the diff
  and its tests, the review's findings, the incident record. Git history is the audit trail.
- **Its people:** human judgment stays at named checkpoints.
- **Its controls:** skills advise, and hooks enforce.
- **Its scale and maintenance:** parallel sessions run in worktrees, bounded by what review can keep up with.
  Configuration gets regression evals. Maintain's deterministic detection feeds new intents back into Plan.
- **Its end state:** a loop in which each accepted artifact fires the next gate. It has no maturity model.

**The verdict: it validates the architecture rather than redirecting it.** Its loop is gov's loop:
- the same six stages, in the same order;
- the same hand-off, by a committed artifact (P2, P26);
- the same end state, each accepted artifact firing the next gate (P1, P20, P24).

Where it differs, gov differs on purpose, and offers the playbook's stance as an allowed value:
- **A person decides between design and build.** In gov, `autonomy: three-gates` places that gate. The default runs
  unattended past the request, as point 1 asks.
- **Review findings only advise.** In gov, `review.blocks: none` gives that. The default lets a review block.

| # | The playbook's practice | The design | Verdict |
|---|---|---|---|
| 1 | Intent committed as a proto-spec: problem, outcome, affected systems, constraints, open questions | `entry.intake` verbatim; the plan record's problem, goal, cut-line, acceptance as observations, priority and parents | held; inherit affected systems and open questions (S3) |
| 2 | Requirements and design in one session, with policy applied while writing | practices rendered per step into work orders (P14); the design-audit lenses | held |
| 3 | A person decides between design and build | `autonomy: three-gates`; the default differs by point 1 | differs on purpose |
| 4 | A written plan before any code | spec before code; specs are structured contracts (P12) | held |
| 5 | Auto mode once the guardrails mature | `runtime.attended-judge: classifier-or-person` (RT-4) | held |
| 6 | One source of truth per artifact | `[one-fact]`; one door (P30) | held |
| 7 | A short shared instruction file, corrected after a repeated mistake | the charter's level-0 envelope; `[left-shift]` makes each confirmed finding a gate or a checklist entry | held; the playbook's one page is tighter than gov's 32 KiB ceiling |
| 8 | Skills advise; must-hold rules are hooks | P16; the guard packs | held |
| 9 | Hooks fast and scoped to the changed file | each hook pack declares a budget | held |
| 10 | Parallel sessions in worktrees, added only while review keeps up | `[isolate]`; leases; agent-cap | partly; no bound by review capacity (NP fork) |
| 11 | First-pass merge rate, plan-to-merge time, rework cycles, the merged diff against the plan | the Loop Review gathers cycle times, yield, catches, cost and flakes | inherit the named metrics (S4) |
| 12 | The agent verifies its own work: tests, build, screenshot; a failing test first for a bug | `[verify]`; seen-red | inherit through point 2: the `reproduction` and `verification` probes, and the visual witness |
| 13 | A hook blocks edits to test files during a fix | not designed: a fix pass may edit the check that reds it | inherit (S1) |
| 14 | Evals over 20 to 50 real tasks, run when instructions, skills or hooks change; each incident becomes a case | the review presets' replays; instruction effectiveness | partly; no eval suite over instruction units (S2) |
| 15 | AI review of every change against a guide; findings never approve alone; an author never approves its own work | the closing review, skeptics, and no role reviewing its own work | held; blocking on purpose |
| 16 | Hooks as approval gates; non-negotiable hooks in managed settings; blocks explain themselves | one enforcement surface; refusals carry remedies today, unchecked; managed settings not designed | inherit the refusal text (S5); managed settings as a fork |
| 17 | Headless runs for judgment steps; scoped tokens; autonomy tiered by environment; a rehearsed rollback | act sessions are headless; grants per adapter; `deploy.promotion`; `release.route` rolls back | held |
| 18 | DORA measures; gate wait times; violations reaching production | not named | inherit with 11 (S4) |
| 19 | Monitoring triggers an agent, and its finding re-enters as an intent | P6: Maintain files into Plan's triage, and patch builds | held |
| 20 | Deterministic detection on rolling baselines, with tiers: log, diagnose read-only, act | readings with pins; `maintain.file`'s severity; `maintain.direct` and `maintain.patch` | partly; tiers by deviation as a fork |
| 21 | Recurring security scans | not designed | a fork |
| 22 | Incidents in a channel; post-mortems to a lessons file | notification adapters; bug classes | held |

**Worked in:**
- **S1, the fix pass keeps its check.** A fix pass's allowance excludes the red leg's own test files and gate script.
  Changing them takes the tester's judgment that the spec or the test is wrong, which routes to Design as a new unit
  (P19). Owner dWitnessedBar.
- **S2, instruction evals.** A replay suite of recorded items with known outcomes is re-run when an instruction unit
  changes: the charter, a role file, a Skill or a hook pack's text. It runs as a held leg under `verdict.held`, on the
  experiment shape point 2 adds. A confirmed finding whose cause is an instruction may add a case (`[left-shift]`).
  The ledger prices it. Owner dCalibratedLens.
- **S3, the plan record's intent fields.** The plan record gains "affected systems", derived from the code map
  (point 3) and checked, and "open questions" as fork tags. Owner dRankedPlan.
- **S4, delivery metrics.** The Loop Review's metric set names:
  - lead time, from intake to landing, and landing frequency;
  - change failure rate: landings followed by a default-branch red or a failed release verify;
  - time to restore;
  - first-pass verdict rate, and route-backs per build;
  - scope drift: landed paths outside the plan's affected systems.

  Owner dCalibratedLens.
- **S5, a refusal explains itself.** A hook pack's contract carries its refusal text, naming the rule and the remedy,
  checked at registration. Owner dWellOiledMachine.

Four practices are policies the owner has not chosen, so they are parked as forks in `[forks]`: the bound on parallel
work by review capacity, a recurring security review, managed settings for the core guards, and tiers by deviation in
Maintain.

## [p7-atlas] Point 7: the atlas's "in review" pills

- **The answer: no.** Both designs were reviewed twice at Tier 2 and folded:
  - the lexicon by dispatches 61 and 62 at `424d2a7de` (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-lexicon-a.md`
    and `-b.md`). Its `[debt-fold]` folded their 52 map rows on 2026-10-17, and LX-1 to LX-3 settled its forks;
  - the review system by dispatches 63 and 64 at `40738693d` (`-review-system-a.md` and `-b.md`). Its `[debt-fold]`
    folded their 38 map rows, and RV-1 settled its fork;
  - the debt folds' closing review then read both folds (`reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md`).
- **Why the atlas said otherwise.** The atlas derives each row's state from its records. A row was folded when one of
  its records held `## [revised]`, or a `Revised:` line naming Tier-2. The debt round recorded its folds as
  `## [debt-fold]`, under a `Revised:` line that names the debt round instead. So both rows read as reviewed and
  unfolded, and the page drew "in review".
- **The fix.** A section whose tag ends in `fold` now counts as a fold too. The fold-state probe (`[instrument]`) read
  2 rows unfolded despite a fold section before the fix, rc 1, and 0 after it, rc 0. Every other row is unchanged.
- **What it does not check.** A fold section shows that a fold was recorded, not that every finding was disposed. The
  debt comparison's map rows and the folds' closing review carry that.

## [p8-fates] Point 8: today's tools and their fates

- **Had it been done? Partly.**
  - Dispatch 26's census, and memory's tooling map (`layer-memory` `[tools]`), gave 25 kit-level verdicts on
    2026-10-15.
  - Later rounds overtook at least nine of them.
  - No inventory was at function level with a fate.
- **Now it is,** in `build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`.
  - 131 parts: 28 stay, 69 are reshaped, 20 are merged and 14 retired. None is left undecided.
  - Dispatch 104 derived 118 rows.
  - The night pass split some rows, and added the unattended kit's dissolution and its modes. It also decided
    playbook mode's home.
  - It proposed a fate for each of the 11 parts no record decided (NP-22).
  - Every line-number citation in the table was resolved to the section it pointed at. Tonight's fold had
    already moved most of those lines, which is gap-found-26's own point.
- **What stays and what goes, by kit:**
  - **kept as kits:** hooks, lib, memory-tree, playbook, process-monitor, roles, run-gates and workflows;
  - **kept as optional kits:** branch-reconcile, codebase-map, drift-audit, gate-lint, govkit, lexicon, memory-recall,
    pytest-parallel-guardrails and runlog;
  - **absorbed:** agent-instructions and unattended;
  - **new:** the loop kit, and the runtime's own kit.
- **What retires.** Among the 14 retired functions:
  - `reuse_lookup.py`, the deploy-governance Skill, and the hand-written guides;
  - the unattended desktop restart and its keepalive, its slug and ask modes, and `--attest`;
  - `/unattended` itself.
- **It stays true by check.**
  - The design map reads the fates record, and each kit line shows its fate.
  - Six arms hold every kit to a row, every row to a known kit, every fate to its set, and every destination to a
    chain build. Each arm was seen red on a plant.
  - The atlas's tools view reads it too.
- **The kit-level map is marked superseded.** The thirteen places where records disagreed are settled in the fates
  record's `[stale]`.

Gap: gap-tool-09. dConvergedCharter runs the table's join as convergence's exit check.

## [chain-impact] What the night pass did to the chain

| Build | Units before | Units after | Added |
|---|---|---|---|
| dGroundRules | 8 | 8 | 0 |
| dOrderedCharter | 22 | 27 | 5 |
| dFairHearing | 11 | 12 | 1 |
| dDeclaredLoop | 43 | 47 | 4 |
| dWitnessedBar | 20 | 24 | 4 |
| dBoundRoles | 30 | 34 | 4 |
| dTotalRecall | 32 | 39 | 7 |
| dIndexedDesign | 9 | 11 | 2 |
| dRankedPlan | 11 | 13 | 2 |
| dWellOiledMachine | 24 | 31 | 7 |
| dScopedBuild | 9 | 11 | 2 |
| dTendedCadence | 10 | 12 | 2 |
| dMindYourWords | 16 | 17 | 1 |
| dCalibratedLens | 8 | 11 | 3 |
| dShippedRelease | 20 | 20 | 0 |
| dConvergedCharter | 12, of which 11 meant | 14 | 3 |

- **Units: 285 to 331.** dConvergedCharter's old count held a quoted clause split in two, the same defect as
  dFairHearing's before the walk. The clause scan now reads double quotes too, and was seen red on it.
- **The critical path: 181 to 213 units.**
  - It now runs dGroundRules, dOrderedCharter, dDeclaredLoop, dWitnessedBar, dTotalRecall, dWellOiledMachine,
    dTendedCadence, dCalibratedLens and dConvergedCharter.
  - The Maintain and Review builds' additions (instruction evals, delivery metrics, a cyclic playbook's filer, a
    bundle detector) put them ahead of dShippedRelease, which finishes at 195.
- **dDeclaredLoop grows from 43 to 47 units.** It holds the attendance rule, the `repeat` disposition, the probe
  program and the code seed. The walk's offer to price a split stands, and NP-24 asks it.
- **No edge changed.** Every new dependency on a later build either waits in a slot that renders "not installed",
  or is classed in the re-cut's `[reconciled-order]`: three new rows, one each for `feature` and `code` from
  dBoundRoles, and one for `code` from dOrderedCharter.

## [forks] Parked for the owner, 2026-10-18

Each fork's first option is the recommendation, and the design as folded shows it, marked pending.
- **Defaults.** Where the answer sets a key's default, the options become the key's allowed values (P10).
- **Structural choices.** Where the answer is a structural choice, it is a decision.
- **New keys.** Points 1 to 4's keys are in the catalogue, since their mechanism is the owner's word. Point 6's four
  candidate keys wait for an answer that adopts them.

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| NP-1 | Who drives a build while the owner attends? | the supervisor always, the owner's session its client, hosting the same driver, bound as an act session, until dWellOiledMachine lands; the owner's session drives, under the same act binding; the owner's session drives entry and Plan only | a structural decision: layer-runtime `[terms]` and dWellOiledMachine's row |
| NP-2 | What does attending turn on? | each act announced, a confirmation at every step's exit, owner questions asked live; announcements only; announcements and a confirmation before every act | the value of `attendance` a bare attend request selects; all three become its allowed values beside `unattended` |
| NP-3 | How long does an attend or unattend request hold? | until the build's terminal state; until the session ends; until revoked, repository-wide | `attendance.scope`'s default |
| NP-4 | When does `/unattended` go? | a client of `run` until dConvergedCharter retires it; retired as soon as dWellOiledMachine's driver lands | a structural decision |
| NP-5 | Who verifies a probe? | the tester, cold; the asking role; the researcher | `probe.verifier`'s default |
| NP-6 | Who authorizes an experiment's agents? | the owner opts in, each time; any experiment within the agent cap; free | `probe.experiment.authority`'s default |
| NP-7 | When is an owner's observation verified? | before the request is placed; at Plan; only when asked | `probe.observations`'s default |
| NP-8 | How large is the `code` slot? | 8 KB; 4 KB; 16 KB | `memory.code-budget`'s default |
| NP-9 | Which roles get the `code` slot? | the working roles: spec writer, builder, researcher, architect, reviewer, and the prompt writer through its actor; every role; the structural roles only | `memory.code-roles`'s default |
| NP-10 | Which languages does the core extract? | Python, shell and JavaScript, others at file level with `git grep`; file level only; require ctags, absent on this node | `memory.code-languages`'s default |
| NP-11 | Where do code purposes live? | in record slots keyed by each definition's body hash, derived first; in-code `gov:note` only; derived only, with no agent pass | `memory.code-enrich`'s default |
| NP-12 | How is a region marked? | derived from a definition's extent, `gov:end` only where none derives; explicit `gov:region` and `gov:end` around every region; point anchors with no spans | a structural decision: P33 and the annotation grammar |
| NP-13 | Can an instruction be scoped to a feature? | yes, `feature` becomes a selector; no, features stay descriptors, reaching instructions through reuse entries | a structural decision |
| NP-14 | What does `gov tag bundle` return? | a manifest of ranges, content pulled per row; content inlined under a byte budget; both, by flag | `tags.bundle`'s default |
| NP-15 | How many edge types? | the closed set, twelve declared and one derived; a minimal six, lifecycle relations left to `record` | a structural decision |
| NP-16 | What becomes of the dossier? | its header becomes the feature node, its prose moving into units and records; kept as it is; folded into the reuse entry | a structural decision |
| NP-17 | How does new text cite code? | `path#symbol` or a blob-pinned line, file:line joining the positional population; file:line kept, its staleness reported | a structural decision, read through `tags.positional` |
| NP-18 | Should parallel work be bounded by the owner's review capacity? | measure first: the Loop Review reports the owner queue's depth, with no bound; new claims wait while more than a set number of owner items are open | a new key, `runtime.owner-queue`, only on a bound |
| NP-19 | Should a security review recur? | weekly, as a Maintain cadence item running the security lens over the landed tree; at every landing; off | a new key, `maintain.security-review` |
| NP-20 | Should the core guards install into managed settings? | project settings, managed settings where the operator opts in; managed settings by default | a new key, `install.guards` |
| NP-21 | Should Maintain tier its readings by deviation? | defer: pins with a severity, as today, until the Loop Review has rolling baselines; bands now: log, diagnose read-only, act | a new key, `maintain.tiers`, only on bands |
| NP-22 | The fates proposed for the parts no record decided? | approve them as proposed; review them row by row | the fates record's rows marked proposed |
| NP-23 | The night's new nodes and their owners? | approve them as proposed; review them | the ownership record's night-pass amendment |
| NP-24 | dDeclaredLoop now holds 47 units, and the critical path runs through dTendedCadence and dCalibratedLens at 213 | price a split of dDeclaredLoop, and a lighter dCalibratedLens, before the walk resumes; keep the chain as it stands | a structural decision about the chain |

The walk is not a fork: wave 1 still waits for the owner's read, and wave 2 follows it.

## [instrument] The checks, as run

The night pass's scripts and probes, and their runs, are in
`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md`. As committed:
- **The design map** derives 2,232 nodes in 30 namespaces, 31,133 of 32,768 B, rc 0.
  - Its new layer arm read 19 kits joined to no layer before the fix, rc 1, and none after it.
  - Its six fates arms each red on their plant.
- **The atlas** derives 154 records and 33 principles, rc 0.
  - The fold-state probe read 2 rows unfolded despite a fold section before point 7's fix, and 0 after it.
- **The reconciliation probe** reads 19 classed dependencies, rc 0.
  - Its cites rule now reads a namespace cited through a wildcard. It was red on dBoundRoles' `feature.*` until the
    class row landed.
  - Every one of its plants still reds.
- **The clause scan** finds 0 splits. It was red on dConvergedCharter's quoted clause before the join.
- **The gap join** reads 250 keys against 16 chain rows, each owned exactly once, rc 0.
- **The preset check** reads 206 keys, 193 presettable, and 193 preset rows, with no findings.
