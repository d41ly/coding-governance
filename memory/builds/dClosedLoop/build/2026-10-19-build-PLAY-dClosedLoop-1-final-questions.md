# Final questions: the whole design audited, held to its specs, its deviations logged, and the product documented

**Serves:** research PLAY-dClosedLoop-1

The owner closed the design pass with five questions: whether an adversarial review can walk the whole design before
speccing, how speccing will be held to the design, how deviations will be logged and carried into what ships, how the
product will be documented for its human owners, and how an atlas of the product will live in the repository. Five
researchers each took one question, and their returns are saved verbatim beside this record. This record answers the
five, shows the one mechanism that runs under questions 2 to 5, sets the order of work from here to the first chain
spec, and puts eight forks to the owner.

## [words] The owner's questions, 2026-10-19

> We're wrapping this design pass, final questions to resolve:
>
> 1. Can we run a thorough adversarial workflow to review the entire design step by step and ensure no critical gaps
>    were left, before we move on to speccing it?
> 2. How are we going to control and verify that the entire design was specced as planned? There have been numerous
>    precedents before - agents can lose the chain of thought and start deviating from design. A control mechanism
>    is required.
> 3. How are we going to ensure that the specs are not deviated from without reason and any deviation is accurately
>    logged and reflected in the final artifact.
> 4. Human-readable help - the product needs to be fully documented (for human owners) and should not be a black box
>    when the build is complete. What is the current plan in this regard?
> 5. Once the build is fully complete, another version of the Atlas should be maintained _in the repo_ (not an
>    online artifact) alongside help pages to visualize product's design and architecture, and should be maintained
>    through all the future updates.

## [questions] Five researchers, one question each

| Dispatch | Question | Return |
|---|---|---|
| 155 | What earlier audits covered, what a critical gap is, and the workflow that reviews the whole design step by step. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-audit.md` |
| 156 | How speccing is controlled and verified to carry the whole design. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-coverage.md` |
| 157 | How a deviation is refused without a reason, logged, and reflected in what ships. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-deviation.md` |
| 158 | Today's documentation, the plan as designed, and when its gate lands. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-help.md` |
| 159 | What an in-repository atlas shows, where it reads from, and how it stays current. | `build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-atlas.md` |

## [answer] The five questions, answered

1. **Yes, but not in the shape the earlier audits had.** They sliced the design by lens. Their four whole-design reads
   cite no item of the design, test, deploy, probe, lifecycle or adopt steps, and 41% of the design records' lines
   were read by no review (dispatch 155, its instrument re-run at `930120e45`). The audit walks scenarios through every
   step, twice and sliced two ways, after mechanical checks and before a closing pair, and it grades itself on past
   defects planted back into a copy of the records. It runs after these answers are folded and before any chain spec
   ([audit]).
2. **Nothing joins a design clause to the spec that carries it today.** No spec of 1,322 binds to a design, and 218
   of the 498 design nodes a build owns are named in none of its own clauses (dispatch 156). The control gives each of
   the 484 clauses a minted id, has every spec declare the clauses it carries pinned to each clause's text hash, and
   joins the two both ways at each chain build's Design exit, where the owner reads a coverage report ([coverage]).
3. **Deviations are recorded in four places and gated in none.** 176 spec revisions in 105 specs came after their
   unit's code started, and 1 spec audit of 669 pins the revision it read (dispatch 157). The design freezes at a
   baseline after the audit; every later change is a typed deviation record, approved by its risk; and an as-built
   view generated from the baseline and its deviations is what help and the atlas render ([deviation]).
4. **The plan has the right end, switched on last.** Help pages rendered from each user-facing unit's `usage` field,
   with a docs leg, land in dConvergedCharter, the chain's last build, while every earlier build ships its surfaces
   under a prose rule that 6 of 216 product commits followed (dispatch 158). The leg moves to dSafePassage, the second
   build, reference pages are generated from the registries, and concept and task pages are written and tested
   ([help]).
5. **The atlas becomes generated pages under `help/atlas/`,** Markdown with Mermaid diagrams that GitHub renders, read
   from the product's own node table rather than the design records, owned by dTotalRecall, and refused when stale by
   the generated-output check the merge bar already runs (dispatch 159). A scratch render was 275 KB against today's
   13.4 MB page ([atlas]).

## [spine] One mechanism under questions 2 to 5

The four answers share their parts, so each is designed once:

| Part | Question | What it is |
|---|---|---|
| clause ids | 2, 3, 5 | `cl-<minting-slug>-NNNN` at the end of each of v2's 484 clauses, in backticks, never renumbered or reused, with a `[clause-ids]` section listing retired ids |
| carries | 2 | each spec's `**Carries:** <clause-id>@<hash8>` lines, each marked whole or `part k/n`, and `node:<ns>.<key>` for each owned node it builds, or `**Derived:** <decision-id>` |
| baseline | 3 | the design commit taken after the audit's fold; from then on v2 takes no `Revised:` paragraph |
| deviations | 3, 5 | one typed record per departure, each carrying an `amends` or `supersedes <clause-id>@<hash8>` row in dOrderedCharter's overlay grammar |
| as-built view | 3, 4, 5 | generated from the baseline and its deviations, each changed clause citing its record; never hand-edited |
| coverage join | 2 | reads the as-built view and every spec's carries, at each Design exit and at each spec's revision |
| help pages | 4 | rendered from each surface's declared `usage` and the registries, and linked to the atlas by tag |
| atlas pages | 5 | rendered from the product's node table, with a design-against-built page reading the clause ids and deviations |

## [audit] Question 1: the whole-design audit

**What earlier audits covered** (dispatch 155 `[1a]` to `[1c]`). Fifty review reports ran 499 agents and 9.58M output
tokens and confirmed 1,601 findings. One run of a pair finds 58% to 88% of what both find, and every pair's Chapman
estimate leaves defects that neither run found. By exact token match, a floor:
- the design, test, deploy, probe, lifecycle and adopt steps are cited by no finding of a whole-design read;
- P6, P12, P14, P17, P21, P25 and P31 are named by no confirmed finding;
- 12,458 of 30,353 lines in 48 design records were read by no review: project-map and ownership-verify whole,
  ownership 97%, the audit-fold record 54%, and the 265 lines the parked debt's fold wrote at `930120e45`.

The session model's walk (`build/2026-10-14-build-PLAY-dClosedLoop-1-session-model.md` `[holes]`) found scenario-shaped
holes, missing witnesses, actors, routes and timing, where the lens reviews' top classes are two answers to one
question and amendments that leave their other half standing. The two methods find different things.

**A critical gap** is a finding graded high or blocker whose consequence is one of: a chain build that cannot be
specced or land in order; a scenario that cannot reach a terminal, or reaches one without its witness; a guard that
silently loosens or certifies what it does not check; built work or adopter data overwritten or lost; a principle no
clause enforces. Of its ten classes, K1 to K10 in dispatch 155 `[2]`, two are checked in full today, gap ownership
and the presets; seven can be checked mechanically and are checked in part or not at all; and the last needs a
reader: a fail-open, a trust boundary, a race across nodes, a migration across a drain.

**The workflow** (dispatch 155 `[5]`, candidate D):
1. **Stage 0, mechanical, seconds.** Instruments in this build folder, each seen red on a plant first: the item
   matrix over all 90 items' needs, witness and route; every route target and a terminal's reachability, red on a
   planted route to `deploy.land` that today's reconciliation probe passes; record kinds joined to writers and
   readers; keys joined to the units that read them; a declared enforcing clause per principle; and the existing
   gap join, preset check, map, clause scan, line coverage and review debt re-run. Each red is fixed or classed, and
   each line no check reads becomes a named target for the walkers.
2. **Stage 1, a paired walk.** Two independent runs at the owner's medium effort, one after the other, run A's report
   held out of the tree while run B runs. Seven scenarios: a solo attended build; an unattended build across two nodes;
   a patch build of a landing; an adopter's update; a withdrawal; a failure injected at every stage; and the bootstrap,
   chain build *k* specced and built with only the builds before it landed. Run A slices by scenario, run B by step
   band, and each run gives every build and principle a verdict. Each run is five walkers, four skeptic batches and
   one synthesizer. Each walker returns its findings and a walk table, one row per item and scenario (actor, needs,
   witness, route, verdict), and the synthesizer is red on an empty cell. The walk opens with a pre-mortem line,
   reads failure mode, effect and detection per item, and reads trust boundaries per data flow on the multi-node and
   adopter scenarios.
3. **Stage 2.** Fold the findings, then the paired full closing review over the fold, as the parked debt's ran, then
   Stage 0 again.

**How it is dispatched.** The hooks admit a `Workflow` only for a declared harness (`tools/hooks/agent-cap.js`
`checkHarnessCall`), and a new harness is product code this build does not write. So Stage 1 runs as direct role
dispatches in waves of at most five: `gov-spec-reviewer` walkers, each handed its walk brief as its `input:spec`,
then `gov-skeptic` batches, then one `gov-synthesizer`. Stage 2 runs `tools/workflows/tier2-review.js` unchanged.

**Its recall, measured.** Twelve fixed past defects are reverted into a sealed clone outside the repository, among
them the session model's H1, H2 and H6, the failure route, the supervisor restart and a dropped kind writer, the key
sealed and its sha256 pinned in the run's brief before launch. Each run must find at least two thirds of them and
both together at least ten of twelve, and Stage 0 must catch the two mechanical plants every time. Today's replay
scorer refuses design reports, since it scores only `§<n>` addresses (`tools/workflows/review_replay.py:36-44`), so a
`[tag]`-address scorer is written first, as an instrument here.

**The witness for "no critical gap left":** Stage 0 green with every check seen red; both walk tables complete; the
recall bar met; no critical finding open; and a closing pair that finds no new critical one. Chapman over the
critical defects is reported as a trend, never as the gate, since an estimate from two inspectors is not reliable.

**Cost:** about 600k to 800k output tokens and 20 agents for Stage 1, about 365k and 22 agents for Stage 2, seconds for
Stage 0. The runs record their wall time, which no review has recorded yet (`gap-rt-26`).

**What must exist before it runs:** these answers folded; the Stage 0 instruments, each seen red; the seven scenarios'
briefs and the walk table's schema; the critical rubric; the sealed seeding and its scorer.

## [coverage] Question 2: the control that the whole design is specced as planned

**Precedents** (dispatch 156 `[1]`, fifteen rows). An owner's answer reversed in a draft, caught a day later; a clause
moved to a new key while a sibling record still named the retired one; 13 records overtaken by later rounds, found
days later by a model pass; a ratified spec's dropped carrier reproduced by the next spec "without ever seeing the
diagnosis"; and a drop control that joined ids by mention, so a foreign id exempted a dropped unit. Each was caught
late, by a review that happened to run, and 47 of 167 builds ever had a spec audit.

**Today:** no join from a design clause to its spec exists. The write gate checks that a unit is specced, not what the
spec carries; spec audits are opt-in and probabilistic; `spec-tokens` checks a spec's own names and its siblings',
nothing upstream of them; and this build's instruments join builds to gaps, never clauses to specs.

**The unit of control** is the clause plus the owned node. Positions cannot be ids: over v2's history, 297 clauses
changed position and 72 moved to another build's row. Text hashes cannot be ids: 924 clause texts were new at their
commit. So ids are minted once and the hash is each clause's revision, as in OpenFastTrace and Doorstop. An id at the
clause's end leaves the chain echo, the clause scan, the gap join and the critical path unchanged, measured on a
scratch copy.

**The join's arms** (candidate G, prototyped on fixtures, each planted case red and the clean set green):
- per spec: a ghost id; an unbound spec carrying nothing; a stale pin after the clause changed; two specs carrying one
  clause whole and disagreeing; a revision that stopped carrying a clause with no decision;
- per build: an uncarried clause or owned node; a token of the clause missing from its carriers;
- a run that measured no spec is never green.

Its blind side: a carrier that keeps every token and contradicts its clause. That is the semantic lens's, which reads
each carried clause and its sections at the Design exit.

**The owner's report at each Design exit:** clauses carried whole and split, those moved, retired or deferred each
with its decision, uncarried 0, stale 0, ambiguous 0; owned nodes unnamed 0; specs derived from no clause, each with
its decision; and the clauses the token arm cannot see, with the lens's verdict on them.

## [deviation] Question 3: deviations refused without a reason, logged, and reflected in what ships

**Precedents** (dispatch 157 `[1]`). A review's blockers folded into a unit already built; amendments leaving their
other half standing; a fold creating 42 of the next round's 62 findings; an owner's ruling carried into v2 and
layer-memory but not the ownership table, so that 11 of 39 shared kind owners now disagree between two tables; and
1,925 free-text `Decided:` trailers that nothing classifies. None of it reaches what a reader of the finished product
reads.

**The deviation at each hand-off:**

| Hand-off | Legitimate | Drift | Approver |
|---|---|---|---|
| design to spec | a design defect with evidence; an owner's ruling; a reuse probe that changes the mechanism | a silent narrowing, a dropped red case, a renamed key | by risk |
| design revised under a spec | an audit fold; an owner's ruling | an edit in place | the owner, for a change of meaning |
| spec to revised spec | a builder's discovery handed back; a review finding before close | a fold into a built unit; the other half left standing | the spec writer with a re-audit of the changed sections, or the owner |
| spec to code | none without a spec revision first | building to a different criterion | nobody at build time: it routes back to the spec writer |
| code to landed record | none: after landing, a change is a new unit (P19) | a ledger, README or help page that disagrees with the code | none |

**Approval by risk:** an editorial change, by dOrderedCharter's classifier, its author, the record still written; an
additive or stricter one, the spec writer and a re-audit at the new revision; a loosening, a dropped or weakened
criterion or a narrowed scope, the owner; a breaking one, an interface, a principle, a policy key or a gap's owner,
the owner; an owner's ruling as cause, the owner, quoted.

**The record:** its id; the hand-off; what it departs from, `<clause-id>@<hash8>` or `<unit>@rev-N` and the section;
before and after; the cause class (design defect, owner ruling, builder discovery, review finding, external); the
reason; the evidence; the risk class; the approver and where the approval is recorded; the follow-through (an overlay
row, a new unit, a gap, an ask, a `usage` edit); and its cause (P35).

**The population is computed, never declared:** every revision after a unit's first attributed pass commit or after
its pinned audited revision, every AMENDED acceptance line, every divergence hand-back, every rescope row and every
clause-hash move must join a record whose approver meets its risk class. Planted reds: a revision after a pass with no
record; an AMENDED line with no record; a mismatched pin; an approver below the risk; and a status-only edit green.

**Reflected in what ships:** the baseline stays fixed, as a deviation permit leaves the configuration it departs from
fixed, and the as-built view is generated from it with each changed clause citing its record. Help and the atlas
render from the view. Amending the design record in place, the other candidate, is rejected on this build's own
evidence: 104 commits touched v2 in six days, and 21 builds sharing one 1,784-line record would contend on it.

## [help] Question 4: human-readable help

**Today** (dispatch 158 `[1]`): `help/` holds two pages; 17 kit READMEs hold 6,767 lines; the agent runbook holds
2,177. Nothing reads `help/`, and no leg names it. A page covers one Skill of eight, one kit of 17 and one command;
no wired hook and no configuration file has one, and `help/` names the scripts of 4 legs of 140. The prose `[docs]`
rule reaches one role of ten.

**The plan as designed** (v2 dConvergedCharter, SA-5): pages rendered from each user-facing unit's `usage` field, a
hand edit red at render parity, and a docs leg red on a landing that changes a surface the step gate counts with no
change to its `usage`; the units' `help` fields keep their rationale, which "never renders into a page"; dShippedRelease
derives a runbook and release notes, with no losing test named. All of it lands in the chain's last build.

**Gaps:** the timing; explanation renders nowhere a human reads once the guides retire; most of the docs leg's
population (policy keys, hook entries, legs, receipt files) are not instruction units and have no `usage` to carry;
the registries carry no human sentence (0 of 140 legs, 0 of 9 hook fragments and 0 of 29 kit descriptors have a
summary); no principle covers human documentation; and the derived runbook and release notes have no losing test.

**The proposal** (dispatch 158 `[6]`), sorted by what a reader needs (concepts, tasks, reference, explanation):
- **Reference, generated:** every command, policy key, preset, leg, hook, record kind, role and extension point, from
  its registry row, each row gaining required `summary` and `usage` fields, through one render-parity factory.
- **Concepts and tasks, written:** the loop, the stages, leases and nodes; one tutorial, adopting gov, run in an
  adopter fixture; and how-to pages for the owner's tasks: choose a preset, attend or leave a run, read why a build
  stopped, answer an owner item, recover. Every command on a page is run as a test.
- **The docs leg, on dSafePassage:** an arm of its step gate over the same population, graded whole, each member's
  usage declared as a row (a verb and its flags, a key with its values and default, a hook's event and matcher, a
  leg's name and argv) and fingerprinted, red when a fingerprint moves and its page does not, with an offline link
  check. Today's undocumented members start on a shrink-only list. A planted stale page is red, and the real pages
  green, on the researcher's prototype over `help/roles.md`.
- **Explanation, rendered** into its own tree under `help/`, which no agent loads, beside the feature pages, with a
  check that no guide is deleted while a section of it maps to no unit's rationale. This departs from SA-5's "never
  renders into a page", so it waits for the owner (FQ-6).
- **Kit READMEs, the root README and the agent runbook** gain fate rows: generated reference plus a written how-to
  each.

## [atlas] Question 5: the atlas in the repository

**Today** (dispatch 159 `[1]`): the atlas reads design records only, carries every record whole (94% of its 13.4 MB),
loads two outside resources, and has a `--check` that compares its derivation with no published page. The design map
imports the atlas's derivation, so its parity arm shares state with what it guards for layers, builds and gaps. One
clause plans an in-repo view, "the atlas re-rendered from the same node table", and it sits on dLinkedLibrary while
the project map record gives the same item to dTotalRecall.

**Candidates** (each with its losing test and result in dispatch 159 `[3]`): a committed HTML page loses, since GitHub
serves a raw `.html` file as text; generated SVG loses on diff locality; C4 and D2 diagrams as code lose on a second
statement of the registries and on tooling; rendering on demand loses the owner's requirement. Generated Markdown
with Mermaid survives: a one-key change is a two-line diff, and the largest fence measured 1,876 characters and 53
edges, inside Mermaid's defaults of 50,000 characters and 500 edges. A chain diagram with its units would pass 500
edges, so units are tables.

**The recommendation:**
- pages under `help/atlas/`, one per namespace and the plan split per build, each opening with a generated-file header;
- read from the one index's node table, the table `gov map` reads, never the design records;
- a `[[generated]]` row in memory-tree's descriptor at regeneration stage 3, so the merge bar's existing stale-output
  refusal covers it, its check a byte comparison, and its parity arm reading the committed pages back against index
  rows read on their own, which closes today's circular check;
- planted reds: a catalogue default changed with no regeneration; a hand edit; a namespace registered and not rendered;
  a new step shown with no change to the renderer;
- a page budget, a page past it splitting by segment and never dropping a node;
- the design-against-built page reads the clause ids and the deviations; each node links to its help page by tag and
  back, one link check grading both ways;
- owned by dTotalRecall, beside the map's renderer, which takes dLinkedLibrary's clause; each adopter renders its own
  under distribution, which needs a help-root path token in the regeneration kit.

## [bootstrap] What must exist before speccing starts

The gates in [coverage] and [deviation] are product code, and this build writes none. They must stand before the first
chain spec, or most of the chain is specced ungated: dIndexedDesign and dScopedBuild, which own them in the end, finish
far down the critical path. Two halves:
- **In this build, records and instruments only:** the 484 clause ids minted; the coverage join and the deviation
  population as instruments here, each seen red on its plants; the as-built renderer as an instrument; and the audit's
  Stage 0 instruments, walk briefs and seeding.
- **In a bootstrap build at the chain's root, product code with today's tools:** the `carries` join as a ninth join
  of the `spec tokens` leg, behind a configuration cutoff as `SPEC_HANDOFF_CUTOFF` is; the coverage report rendered
  into each build README with an explicit "none" line; a hygiene refusal while a chain build's spec is in progress and
  its coverage is red; the deviation population joined at the commit, through `routed_commits.py`, and at the close;
  the deviation register's kind; spec audits pinning `@rev-N`; and `docs` added to the builder's and reviewers'
  rules. Its own specs are checked by the instruments, since the gate does not exist yet.

Each control then moves into the chain build that owns it in the product: the coverage join into dIndexedDesign, the
deviation joins into dScopedBuild and the approval route into dDeclaredLoop, each absorbing the bootstrap's code.

## [sequence] From here to the first chain spec

1. The owner's rulings on [forks].
2. The fold: v2's principles, keys, clauses and chain row for the answers; the gaps in [gaps]; the 484 clause ids.
3. The audit's instruments, each seen red: Stage 0, the walk briefs, the rubric, the seeding and its scorer.
4. The audit: Stage 0, the paired walk, the fold, the paired closing review, Stage 0 again.
5. The baseline: v2 frozen at that commit; every later change a deviation record.
6. The chain opened: its folders and rosters, the bootstrap build first, then dGroundRules onward, each Design exit
   read through its coverage report.

## [found] Defects the researchers found in the records

Routed to the audit's Stage 0 unless the fold settles them first:
- the atlas clause sits on dLinkedLibrary while the project map gives it to dTotalRecall (dispatch 159);
- v2's revision note at line 210 moves the retired guides' rationale "to `help/`", and dConvergedCharter's clause says
  "never into `help/`'s feature pages" (dispatch 158);
- two checks are both numbered 23, memory-tree's acceptance ledger and check-unattended's undeclared writes (dispatch
  157), which the tag grammar's `check` namespace would name apart;
- `build.acceptance` is dScopedBuild's in flow-steps and the ownership table, while the acceptance record is
  dDeclaredLoop's in v2 and layer-memory, and no clause of either build names the item (dispatches 156 and 157);
- 218 owned design nodes are named in no clause of their owner (dispatch 156);
- the role matrix's record counts 81 items where flow-steps has 90 (dispatch 155);
- the reconciliation probe checks only routes into the breakpoint program, so a route to another build's item passes
  (dispatch 155);
- the line-coverage instrument stops on the shape audits' subject header (dispatch 155);
- the design map's parity arm shares state with the atlas it checks, for layers, builds and gaps (dispatch 159).

## [gaps] Gaps this adds to the register

| Key | Stage | Sev | Gap | Owner |
|---|---|---|---|---|
| `gap-design-13` | Design | HIGH | Nothing joins a design clause to the spec that carries it: no spec of 1,322 binds to a design, and 218 of 498 owned design nodes are named in no clause of their owning build, so a dropped clause is found only if a review happens to run. | dTrueNorth |
| `gap-build-07` | Build | HIGH | A deviation is recorded but never gated: 176 spec revisions in 105 specs came after their unit's code started, and 1 spec audit of 669 pins the revision it read, so a spec and its code can move together with no reason or approver any check reads. | dTrueNorth |
| `gap-mem-47` | Memory | MED | The design is amended in place: 347 `Revised:` paragraphs across 34 records carry its changes, two tables of one fact disagree (11 of 39 shared kind owners), and no view gives the design as built. | dTrueNorth |
| `gap-found-35` | Foundation | HIGH | Help is gated only at the chain's last build: every earlier build ships user-facing surfaces under a prose rule that 6 of 216 product commits followed, and nothing reads `help/`. | dSafePassage |
| `gap-found-36` | Foundation | MED | The product cannot explain itself to a human: rationale renders nowhere once the guides retire, and no registry row carries a human sentence (0 of 140 legs, 0 of 9 hook fragments, 0 of 29 kit descriptors). | dConvergedCharter |
| `gap-mem-48` | Memory | MED | No atlas lives in the repository: the atlas is an online page derived from design records, and nothing renders the product's own registries for a human. | dTotalRecall |
| `gap-review-22` | Review | MED | Design audits slice by lens and never walk a scenario through every step: their whole-design reads cite no item of six steps, 41% of the design records' lines were read by no review, and no audit measures its recall. | dFairHearing |

dTrueNorth owns the three gaps whose first code it lands, under FQ-4. dIndexedDesign, dScopedBuild and dDeclaredLoop
then carry the controls into the product's stages.

## [forks] For the owner, 2026-10-19

| Fork | Question | Options, the recommendation first |
|---|---|---|
| FQ-1 | How is the whole design audited before speccing? | mechanical checks, a paired walk sliced by scenario and by step and graded on planted past defects, then the paired closing review, after these folds; the lens audit pair repeated on the whole design, as the shape audit ran; the checks and one walk run only |
| FQ-2 | How is speccing held to the design? | minted clause ids pinned by hash, every spec declaring what it carries, a join over clauses and owned nodes, a semantic lens and the owner's coverage report at each Design exit; a semantic review lens at each Design exit only; a join over owned nodes only |
| FQ-3 | How are deviations controlled and carried into what ships? | the design frozen at a baseline after the audit, every later change a typed deviation record approved by its risk, and a generated as-built view that help and the atlas render; the design records amended in place, each amendment logged; typed records only, with no baseline and no view |
| FQ-4 | Where are the speccing gates built? | a bootstrap build at the chain's root, built with today's tools before any chain spec; a first unit of dGroundRules; instruments only until dIndexedDesign and dScopedBuild land |
| FQ-5 | When does help become gated? | at dSafePassage, the second build, with generated reference, written concept and task pages and tested commands; at dOrderedCharter, the third; at dConvergedCharter, as designed |
| FQ-6 | Does rationale render into help? | into its own tree under `help/`, which no agent loads, beside the feature pages; never, as SA-5 settled |
| FQ-7 | Do the controls and docs become principles? | P41, the design is carried whole and every departure is a recorded deviation, and P42, every user-facing surface is documented from the fact that defines it; the charter's `[docs]` rule rewritten to name its gate, with no principle; neither |
| FQ-8 | What is the in-repository atlas? | generated Markdown and Mermaid pages under `help/atlas/`, from the product's node table, owned by dTotalRecall and refused when stale; a committed HTML page; rendered on demand, nothing committed |

The keys each recommendation brings, its answer the default and its options the allowed values:
- `design.coverage`: refuse, warn, off; default refuse; dIndexedDesign.
- `design.coverage.semantic`: every-exit, with-spec-audit, off; default every-exit; dIndexedDesign.
- `deviation.gate`: refuse, warn-and-ask, report; default refuse; dScopedBuild.
- `deviation.approval`: by-risk, owner-all, author-recorded; default by-risk; dDeclaredLoop.
- `help.enforce`: refuse, warn, off; default refuse; dSafePassage.
- `help.explanation`: rendered, registry-only; default as FQ-6 settles; dConvergedCharter.
- `help.atlas`: committed, on-demand, off; default committed; dTotalRecall.
- `review.design-audit.runs`: 1, 2, 3; default 2; dFairHearing.
- `review.design-audit.seed`: reverted-escapes, synthetic, none; default reverted-escapes; dFairHearing.

The researchers' finer keys (the coverage population, a stale pin's handling, derived specs, the atlas's page budget
and diagrams, the walk's slicing and cell sampling) are left to the owning units' specs, each a value of these or a
structural choice. `help.*` is used where the researchers wrote `docs.*`, since `doc` is a namespace word.

## [answers] The owner's answers, 2026-10-19

Put to the owner in two batches of four, each question with its recommendation first. The owner's words, verbatim:

| Fork | The owner's answer |
|---|---|
| FQ-1 | "Paired walk + checks (Recommended)" |
| FQ-2 | "Clause ids + join (Recommended)" |
| FQ-3 | "Baseline + records (Recommended)" |
| FQ-4 | "Bootstrap build (Recommended)" |
| FQ-5 | "At dSafePassage (Recommended)" |
| FQ-6 | "Render separately (Recommended)" |
| FQ-7 | "Add P41 and P42 (Recommended)" |
| FQ-8 | "Markdown + Mermaid (Recommended)" |

All eight took the recommendation as offered. FQ-6 departs from the owner's SA-5 by the owner's own word: rationale
renders, but only into its own tree, which no agent loads.

## [folded] Where the answers went, 2026-10-19

- **v2:** P41 and P42 join the principles. dTrueNorth opens the chain ahead of dGroundRules, whose parent it becomes,
  with six units: the clause ids and what each spec carries, the carries join, the coverage report, the deviation
  record and its population, audits pinned to the revision they read, and the as-built view. Nine keys join the
  catalogue and every preset: `design.coverage` and `design.coverage.semantic` on dIndexedDesign, `deviation.gate` on
  dScopedBuild, `deviation.approval` on dDeclaredLoop, `help.enforce` on dSafePassage, `help.explanation` on
  dConvergedCharter, `help.atlas` on dTotalRecall, and `review.design-audit.runs` and `review.design-audit.seed` on
  dFairHearing. Nine chain rows gain their part: dGroundRules' schema rows carry a summary and a usage; dSafePassage's
  step gate gains the docs leg; dOrderedCharter's registry names `usage` and `help`, and its renderer writes the help
  pages; dDeclaredLoop routes a deviation's approval; dIndexedDesign reads the coverage at each Design exit;
  dScopedBuild gates deviations at the Build exit; dTotalRecall renders the atlas, taking dLinkedLibrary's atlas
  clause; dFairHearing gains the walk; and dConvergedCharter renders rationale into its own tree and migrates the
  hand-written pages. `[open]`'s SA-5 reading follows FQ-6.
- **The gap register:** the seven gaps in [gaps], dTrueNorth owning the three whose first code it lands.
- **systems, fates and the memory plan:** the `usage` field named, the rationale's own tree, and the help pages' fate
  and node.
- **The chain:** 22 builds, the critical path growing from 263 units at `590305b02` to 272.
- **The clause ids, minted in a commit of their own:** 496, `cl-dClosedLoop-0001` to `cl-dClosedLoop-0496` in
  `[chain]` order, and v2's `[clause-ids]`, by `build/2026-10-19-build-PLAY-dClosedLoop-1-clause-ids.py`, whose check was seen red on the
  tree before the minting and on four plants: a clause with no id, an id minted twice, a retired id in use and a
  next number behind the ids. It joins the final checks.
- **Not yet folded:** the audit's instruments, the audit, and the baseline after it.
