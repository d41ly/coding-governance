# The whole-design audit: the design walked step by step before any chain spec

**Serves:** research PLAY-dClosedLoop-1

The owner chose, at FQ-1, a whole-design audit before any chain spec: mechanical checks, a paired walk sliced two
ways and graded on past defects planted back into a sealed copy, then the paired closing review
(`build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md` `[audit]`, which designs it). This record runs it: the
owner's words, the order of work, each instrument as built and seen red, and, as the audit runs, its findings, its
fold and its witness.

## [words] The owner's words, 2026-10-19

> Session compacted. What're the next steps to conduct a whole-design audit as suggested + proceed with questions 2
> and 3?

The answer set out five steps, `[plan]`'s, and the owner replied:

> go

## [plan] The order of work

The final-questions record's `[sequence]` put the audit's instruments in its step 3, and its `[bootstrap]` puts three
more in this build: the carries join, the deviation population and the as-built renderer, which questions 2 and 3
rest on and which no step had scheduled. They are built beside the audit's, so the walk reads them and the closing
pair reviews them, and `[sequence]` now says so.

1. **The tooling, with no agents.** Stage 0's checks (`[stage0]`); the walk's briefs, its table and the critical
   rubric; the sealed seeding and a scorer that reads `[tag]` addresses; the carries join with its coverage report,
   the deviation population and the as-built renderer; and wall-time capture. Each is seen red before it is trusted.
2. **The owner's word on v2's four open readings,** SA-1, SA-5, CL-3 and `wait` (v2 `[open]`), so the walk reads
   one design.
3. **The audit,** as final-questions `[audit]` designs it: Stage 0, the paired walk over the seeded copy, the recall
   scored, the owner's forks, the fold, the paired closing review from `6ba4eaaa1`, which also covers the review
   debt, and Stage 0 again.
4. **The baseline,** on the owner's word that the design is whole: v2 frozen at that commit, and every later change a
   deviation record.
5. **The chain opened,** dTrueNorth first, each Design exit read through its coverage report.

"No critical gap left" is claimed only when Stage 0 is green with every check seen red, both walk tables are
complete, the recall bar is met, no critical finding is open, and the closing pair finds no new critical one.

**Step 1, built:** Stage 0 (`[stage0]`), the walk kit (`[scenarios]` to `[briefs]`), the scorer (`[recall]`), the three
instruments questions 2 and 3 rest on (`[instruments]`) and wall-time capture (`[walltime]`), each seen red. The sealed
copy is made after step 2's fold, so it carries the design the walk reads.

**Step 2, answered** (`[readings]`): all four readings confirmed as v2 `[open]` states them, and the locations settled.

**Step 3, under way** (`[walk]`): the sealed copy made, Stage 0 run on it and on the tree, and the walk dispatched.

## [stage0] Stage 0: the mechanical checks

`build/2026-10-19-build-PLAY-dClosedLoop-1-stage0.py` runs five new arms, one per class research-final-audit `[2]`
says a table can check, and re-runs the design's existing checks in the same tree.

| Arm | Reads | Red on | Left to the walk |
|---|---|---|---|
| K1 items | the 90 flow items and the 26 expansion items | an actor of no declared kind or role, or a core item naming an expansion role; a missing Needs cell, or a dash there off its step's first item; a need naming no item; a cycle among needs; no witness; no Then or Routes cell; an owner that is no chain build | whether a witness is actor-typed (P2), and whether an outcome is the right one |
| K2 routes | every Then and Routes cell, branch by branch | a route to an item-shaped tag that is neither an item nor a key; a target in no declared form; an item that ends nowhere; an item no entry reaches; and, through the reconciliation probe's `--all-routes`, a route target that neither its source's owner nor an ancestor builds | whether a terminal, return, wait, owner, ask, policy or program target does end; a policy's routes per value; the `[transitions]` join `gap-flow-15` owes |
| K3 kinds | the map's record kinds against layer-memory's kind table | a kind with no row; a row naming no writer item; a kind no item waits on or names, and no other build's clause names | a reader or writer that is a gate, a renderer or a hook |
| K4 keys | the catalogue's keys against every chain clause and item | a key read by none, marked guard-bearing where one of its values loosens | whether an unread key bears a guard beyond its values' words |
| K5 principles | v2's `[enforcement]` against `[chain]`'s minted ids | a principle with no row, or a row naming no clause; an id no clause carries, or a retired one; a clause citing a principle by id outside that principle's row | whether a named clause enforces its principle |

The re-runs are the design map, the atlas, fold state, the reconciliation probe, the clause scan, the clause ids, the
gap join, the preset check, the critical path, line coverage and the review debt. Seven of them lived only in the
session's scratchpad or inside a record: each is promoted beside the map, byte for byte but for its Serves line and
one note, so Stage 0 runs in any tree, the walk's seeded copy among them. Line coverage now reads the shape audits'
`Subjects (round N):` line, where it had stopped (research-final-audit `[1b]`).

A finding stands unless a row of `[stage0-classes]` names its arm, its node and a class from that arm's closed set,
and a row no finding needs is itself a finding. The audit's fold fixes each red or classes it there; the walk takes
the reds and each arm's "left out" lines as its leads.

**Seen red.** Each arm's plants, on an in-memory copy, turn it red for their own reason, and the run is in the night
pass's instruments record, `[stage0]`. The reconciliation probe's default run passes a plan item planted with a route
to `deploy.land`, and its `--all-routes` run reds it.

**The first run,** on the folded tree before its commit: 184 findings, K1 4, K2 46, K3 79,
K4 55 and K5 none, every re-run green. They are the audit's first leads, listed whole in the instruments
record's `[stage0]`:
- K1: three expansion items whose actor cell opens "the owner", where the kind is `owner`; and `design.streams`,
  whose Needs cell names the policy key that shares its spelling, read as needing itself;
- K2: prose targets the forms do not read, most in the expansions' Routes cells; the release and distribution
  programs ending only through them; fourteen items reached from no entry, since a prose need names no item: the
  Build step's five from `build.recommend` on, `maintain.levels`, `maintain.record`, `loop.record` and six of
  distribution's; and 21 routes into a build that comes later in the chain;
- K3: 36 kinds whose row names no writer item, and 43 no item waits on or names;
- K4: keys that no clause and no item reads, 18 of them guard-bearing.

**K5's leads.** Two principles have rows that name clauses carrying only part of them: no clause builds P3's
remote-CI verdict slot, and none names P18's ranking of a fork's options, the most feature-rich and then the most
expandable.

## [scenarios] The seven scenarios

Each walker walks its items through its scenarios (final-questions `[audit]`, research-final-audit `[5]`):

| Scenario | Name | Walks | Injected or probed |
|---|---|---|---|
| S1 | a solo attended feature build on gov | The owner, attending one session on one node, asks for a feature that changes a kit under `tools/`. The build runs from `entry.intake` through Plan, Design, Build, Test and Deploy to `deploy.close`, with the announcements, the confirmations at breakpoints and the live questions attendance adds. | the owner's answers arriving late; a spec audit the owner declares; the closing review's findings arriving as new units |
| S2 | an unattended build across two nodes | Build X runs unattended on node d. Node x, on another account and harness, takes one of X's units by lease. Build Y on node x depends on X's interface and asks through X's mailbox, and both land in order. | node d's session limit mid-unit and its lease handed over; a lease whose beat goes stale; two nodes racing on the remote's refs; node x's clock skewed; a mailbox question unanswered past its deadline |
| S3 | a patch build of a landing | A landed build's post-merge bar, or a Maintain reading, goes red. Maintain files a patch intake, `entry.place` places it `patch`, and it is claimed with its lease and runs from Design to landing on the originating build's rework budget. | the patch's own landing red again; the originating build's budget spent |
| S4 | an adopter's update | An adopter two releases behind runs `update` to the newest: two upgrade steps, one moving a hook path behind a shim; its overlay amending a gov unit; its receipt's schema migrating; a new check seeded by `test.seed`; its declarations proposed as overlay rows. | a step killed after its first write; an adopter-edited file that gov retires; a step whose witness passes without its work; gov's code running in the adopter's tree |
| S5 | a withdrawal or a supersession | The owner withdraws build X mid-Build, with units in flight and leases held, while build Y waits on X's interface. Separately, X is superseded by Z. | a queued claim replayed after the withdrawal; Y's wait outlasting its deadline |
| S6 | a failure at every stage | One build meets a failure at each stage in turn: a refused lease at `entry.claim`, the owner's silence on Plan's ratification, a red unit at `build.acceptance`, a flake at Test, a landing conflict at `deploy.land`, an unreachable remote, a review at its CEILING, and its rework budget spent. | each failure's route to an outcome, its witness, and what it draws from the budget |
| S7 | the bootstrap | Chain build k is specced and built with only the builds before it landed, for k from dTrueNorth to dConvergedCharter: what its Design exit, its gates and its items run on, today's tools standing in for every later build. | a clause needing a node of a later build; a gate that does not exist yet when k lands; dTrueNorth's own specs checked by this build's instruments |

## [slicing] The two runs' slices

Run A slices by scenario, run B by step band, and each run gives every build and every principle one verdict. Run C slices the chain's clauses by build, five contiguous slices of the copy's `[chain]` balanced by the length of their rows, and gives every build one verdict and every clause one row (`[walk-run-c]`).
`build/2026-10-19-build-PLAY-dClosedLoop-1-walk.py` renders each walker's brief from this table and checks each
return against it. The steps are flow-steps' sections, and `expansions` is the expansions' items.

| Run | Walker | Scenarios | Steps | Builds | Principles |
|---|---|---|---|---|---|
| A | 1 | S1 | all | dRankedPlan, dIndexedDesign, dScopedBuild, dWitnessedBar, dOrderedCharter | P1, P2, P11, P12, P13, P14, P15, P17, P24 |
| A | 2 | S2 | all | dPlacedRequest, dKeptSession, dWellOiledMachine, dBoundRoles, dFurnishedOrders | P5, P21, P22, P23, P25, P26, P27, P29, P36, P40 |
| A | 3 | S3, S5 | all | dTendedCadence, dDeclaredLoop, dCalibratedLens, dTotalRecall | P6, P7, P9, P19, P20, P30, P33, P34, P35 |
| A | 4 | S4, S7 | all | dTrueNorth, dGroundRules, dSafePassage, dShippedRelease, dConvergedCharter, dMindYourWords | P3, P8, P10, P16, P28, P37, P38, P41, P42 |
| A | 5 | S6 | all | dFairHearing, dLinkedLibrary | P4, P18, P31, P32, P39 |
| B | 1 | all | entry, plan | dPlacedRequest, dRankedPlan, dKeptSession, dGroundRules | P4, P10, P11, P15, P21, P22, P23, P40 |
| B | 2 | all | design, build | dIndexedDesign, dScopedBuild, dBoundRoles, dFurnishedOrders, dTrueNorth | P12, P17, P18, P19, P24, P25, P26, P41 |
| B | 3 | all | test, deploy | dWitnessedBar, dShippedRelease, dSafePassage, dConvergedCharter | P2, P3, P8, P9, P16, P37, P38, P42 |
| B | 4 | all | breakpoint, probe, lifecycle | dFairHearing, dDeclaredLoop, dWellOiledMachine, dCalibratedLens | P1, P5, P7, P20, P27, P29, P31, P36, P39 |
| B | 5 | all | adopt, expansions | dLinkedLibrary, dTotalRecall, dTendedCadence, dMindYourWords, dOrderedCharter | P6, P13, P14, P28, P30, P32, P33, P34, P35 |
| C | 1 | clauses | clauses | dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter | none |
| C | 2 | clauses | clauses | dFairHearing, dDeclaredLoop, dPlacedRequest, dKeptSession | none |
| C | 3 | clauses | clauses | dBoundRoles, dFurnishedOrders, dTotalRecall, dLinkedLibrary, dMindYourWords | none |
| C | 4 | clauses | clauses | dWellOiledMachine, dWitnessedBar | none |
| C | 5 | clauses | clauses | dRankedPlan, dIndexedDesign, dScopedBuild, dShippedRelease, dTendedCadence, dCalibratedLens, dConvergedCharter | none |

## [walk-table] The walk table's grammar

A walker returns one row per item and scenario of its slice:

| Item | Scenario | Actor | Needs | Witness | Route | Verdict |
|---|---|---|---|---|---|---|
| `plan.input` | S1 | = | = | = | = | holds |

- **Item:** the item's tag as flow-steps or layer-expansions writes it. **Scenario:** S1 to S7.
- **Actor, Needs, Witness, Route:** what the scenario finds there, `=` where it reads as declared. Never empty.
- **Verdict:** `holds`; the ids of the findings the cell shows, `A1-F3` or `A1-F3, A1-F7`; or `not on path: <reason>`
  where the scenario never reaches the item.
- **Build and principle verdicts:** `| <build> | holds |` or the finding ids, and likewise `| P<n> | ... |`.
- **A finding id** is `<run><walker>-F<n>`, unique across both runs, and heads its finding as `### <id> — <title>`,
  its address `<record> [<section tag>]` with the clause id or item tag that carries it.

`walk.py check` reds a missing row, an empty cell, a verdict outside the grammar, a finding id no heading carries, a
cell outside the slice, two rows for one cell, and a build or principle with no verdict. A run's joined table, the
synthesizer's, is checked whole: every item in every scenario, every build and every principle.

## [rubric] The critical rubric

A finding is critical when its severity is blocker or high and its consequence is one of these
(research-final-audit `[2]`):
- **c1:** a chain build cannot be specced, or cannot land, in order;
- **c2:** a scenario cannot reach a terminal, or reaches one without its witness;
- **c3:** a guard or a check silently loosens, or certifies what it does not check;
- **c4:** built work or adopter data is overwritten or lost (P19, P38);
- **c5:** a principle has no clause that enforces it.

| Class | What it is | What checks it mechanically |
|---|---|---|
| K1 | a step item with no actor, input, witness, route or owner | Stage 0's K1 |
| K2 | a scenario that cannot reach a terminal | Stage 0's K2 |
| K3 | a record kind with no writer or no reader | Stage 0's K3 |
| K4 | a key no unit reads | Stage 0's K4 |
| K5 | a principle no clause enforces | Stage 0's K5 |
| K6 | a clause reading what no ancestor registers | the reconciliation probe, on backticked citations |
| K7 | a bootstrap hole | the reconciliation probe, for named shapes only |
| K8 | a gap owned by no build, or by two | the gap join |
| K9 | a preset or catalogue hole | the preset check |
| K10 | a judgement class: a fail-open, a trust boundary, a race across nodes, a migration across a drain, a retirement by value | none |

**Severity.** Blocker: the design cannot be specced as written. High: a scenario fails, or a guard certifies what it
does not check. Medium: a defect a spec writer would trip over. Low: wording, a stale count, a dead pointer.

## [briefs] The briefs

`walk.py brief --run A|B --seeded <copy> --leads <file> --out <dir>` renders the run's five walker briefs from
`[scenarios]` and `[slicing]`. Each names the sealed copy as the only place its walker reads the design, Stage 0's
leads (the run on the working tree, never on the copy, whose two mechanical plants Stage 0 must catch on its own),
the pre-mortem line, the FMEA columns on every item a failure reaches, the STRIDE reading of S2's and S4's trust
boundaries, the K1 to K10 checklist and this rubric, and the return's order: the pre-mortem line, the findings, the
walk table, the build verdicts and the principle verdicts. Each walker is a `gov-spec-reviewer` handed its brief as
its `input:spec` (the audit's dispatch, final-questions `[audit]`). A brief renders only with the sealed key's SHA-256
(`--key-sha`), which it states.

`walk.py skeptic` renders the run's four skeptic briefs: the walkers' findings sorted by their full address and cut into
four contiguous batches, the largest as small as whole addresses allow, never one address split, each batch with eight
clean cells to attack, drawn the same way on every render. `walk.py synth` renders the synthesis brief, naming the
report's path under `reviews/` and its `Subjects (round 1):` line, which the line-coverage instrument reads. Skeptics
are `gov-skeptic` and the synthesizer `gov-synthesizer`, each handed its brief the same way.

## [recall] The recall: the sealed copy and its scorer

The walk reads a copy of the design with twelve fixed past defects reverted into it, and each run is graded on how
many it finds (final-questions `[audit]`).
- **The copy** is made from the commit that folds step 2, as a fresh repository holding that tree in one commit, so no
  history shows what changed, kept in the session's temp root, outside the repository and its scratchpad. Every sentence of the copy's
  records that names a candidate plant is cut from the copy too.
- **The plants** are escapes: defects a later review found after an earlier one had passed them, each fixed by a fold
  since, and each reverted into today's text. Two are mechanical, and Stage 0 must catch both on the copy itself (`stage0.py --root <copy> --arms K3,K5`), as it must
  every time.
- **The key,** the plants and the seeding script stay outside the repository until both runs are scored. The key's
  SHA-256 is pinned in every walker's brief before launch, and the scorer refuses a key whose hash moved. After the
  scoring all three are committed here, and the instruments record carries the script.
- **The scorer,** `build/2026-10-19-build-PLAY-dClosedLoop-1-score.py`, reads each run's confirmed findings by their
  `[tag]` addresses, where today's replay scorer reads only `§<n>`, and prints each run's recall, the union's, Mills's
  estimate of the real defects left from the share of plants found, and Chapman's over the two runs as a trend, never
  the gate. Each hit is read by hand too, since an address can carry a neighbour of the plant.
- **The bar:** each run finds at least eight of the twelve, and the two together at least ten. A run under the bar
  comes to the owner before anything is folded.
- **The bar, as scored** (fixed 2026-10-20, before any score was read): Stage 0 caught both mechanical plants on the
  copy (`[walk]`), so `score.py --stage0-caught` counts both in each run, and the walkers' hits on the ten judgement
  plants make the rest. Each run needs six of them, and the two together eight. A walker's hit on a mechanical plant
  is shown and adds nothing, since the copy's own records name the arms that catch them.

## [instruments] The instruments questions 2 and 3 rest on

dTrueNorth builds the product controls; until it lands, these check its specs and every chain build's after it
(final-questions `[bootstrap]`). Each is green on a fixture built in memory and red on each of its plants, and on the
tree each says it measured nothing and is never green until its input exists.
- **`build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`, the carries join and its coverage report** (FQ-2, clauses
  `cl-dClosedLoop-0001` to `cl-dClosedLoop-0003`). A spec declares what it carries, one line each:
  `**Carries:** <clause-id>@<hash8> whole` or `... part k/n`, `**Carries:** node:<namespace>.<key>`,
  `**Derived:** <decision id>`, and `**Moved:**`, `**Retired:**` or `**Deferred:** <clause-id> ... by <decision id>`.
  A clause's hash is the first eight hex digits of the SHA-256 of its text, its id cut off and its whitespace folded.
  It reds a ghost id, an unbound spec, a stale pin, a clause carried whole twice or pinned to two hashes, a revision
  that drops a clause with no move recorded, a token of a clause missing from its carriers, and, at a Design exit, an
  uncarried clause or owned node; a run that measured no spec exits 2. `--report <build>` renders the owner's report.
- **`build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`, the deviation population and its join** (FQ-3, clauses
  `cl-dClosedLoop-0004` and `cl-dClosedLoop-0005`). A record departs from `<clause-id>@<hash8>` or `<unit>@rev-N`, and
  names its hand-off, before and after, cause, reason, evidence, risk, approver and follow-through. The population is
  each clause whose hash moved since the baseline, each spec revision after its unit's first pass but a status-only
  one, and each `AMENDED` acceptance line, which names its record; each joins a record whose approver meets its risk.
- **`build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py`, the as-built view** (FQ-3, clause `cl-dClosedLoop-0006`):
  `[chain]` at the baseline with each record's `amends` or `supersedes` row applied, each changed clause citing its
  record, re-rendered and compared byte for byte, red on a hand edit, a record with no row and a changed clause with
  no citation.
- **The baseline** is recorded as ``Baseline: `<sha>` `` in v2's `[clause-ids]`, which the last two read.
- **Where the records and the view live** (the owner, 2026-10-20, `[readings]`): a deviation record in its departing
  build's `build/` folder, and the as-built view beside v2 in this build's folder, re-rendered there whenever a record
  lands, after this build closes too.

## [walltime] Wall time

`build/2026-10-19-build-PLAY-dClosedLoop-1-walltime.py` reads each agent's transcript for its first and last timestamp
and prints each agent's wall and each stage's span, from its first agent's start to its last agent's end. No review
had recorded its wall time (`gap-rt-26`), and the audit records every stage's.

## [readings] The owner's word on the open readings, 2026-10-20

Asked as step 2, each with v2 `[open]`'s reading as the recommendation. The owner's answers, verbatim:
- **SA-1**, the layered owner proof at "a layer date", read as "a later date": "A later date (Recommended)".
- **SA-5**, the usage field named `usage` since `help` holds the rationale: "Keep `usage` (Recommended)".
- **CL-3**, "a new headless-first planner role", read as Plan's planner with `design.streams` as its Design item:
  "Same planner, new item (Recommended)".
- **`wait`**, `run.on-owner-silence: wait` read as waiting parked: "Wait parked (Recommended)".
- **Where deviation records and the as-built view live** once this build closes: "With builds; view by v2
  (Recommended)", each record in its departing build's `build/` folder and the view beside v2, re-rendered there.

v2 `[open]` marks the four confirmed, with a revision note.

## [found] Defects found while building the tooling

Each goes to the walk as a lead beside Stage 0's reds, and to the audit's fold:
- **The deviation record is no registered kind.** dTrueNorth's `cl-dClosedLoop-0004` builds it, but layer-memory's kind
  table, the memory plan and the map name no `deviation` kind, so Stage 0's K3, which reads registered kinds, cannot see
  it: no owner, writer or reader is declared for it.

## [walk] The walk, as dispatched

- **The sealed copy** was made 2026-10-20 from `747a2af22`, a fresh repository at one commit (`d316e78a3`) in
  the session's temp root, outside the repository. The key's SHA-256, pinned in every walker's brief before launch, is
  `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`.
- **Stage 0 on the copy** caught both its mechanical plants, by K3 and K5, and its run on the working tree is the
  walkers' leads, beside the copy's design as `stage0-leads.md`.
- **The order:** run A's five walkers, then run B's five, so neither run's walkers read the other's findings; then
  each run's four skeptics and its synthesizer, whose briefs are rendered once both walks are back. The walkers'
  returns stay outside the repository until both walks are back.
- **Effort:** the walkers are `gov-spec-reviewer` at medium, the skeptics `gov-skeptic` and the synthesizers
  `gov-synthesizer` at high, each its role definition's setting, none below the owner's medium.
- **Dispatches** 160 to 164 are run A's walkers and 165 to 169 run B's, their handoffs
  `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-1-spec-reviewer.md` to `...-10-spec-reviewer.md`, each handed its brief,
  `build/2026-10-20-build-PLAY-dClosedLoop-1-walk-brief-<run><walker>.md`, as its `input:spec`.
- **A breach in run A,** disclosed by its walker 5: before it switched to the copy, it read this record in the working
  tree from `[scenarios]` on, where `[recall]` then named the two mechanical plants' kinds, which the copy's record
  had cut. That sentence is cut here too before run B, and run B's briefs forbid reading anything under `memory/` in
  the working tree but the brief itself. The scoring reports walker 5's hits with this noted. Run A's returns wait
  outside the scratchpad, where run B's walkers keep their own scratch folders.

### [walk-run-a] Run A, returned

Five walks, 73 findings, every walk table complete: walker 1 11, walker 2 11, walker 3 20, walker 4 20 and walker 5 11.
A read audit of each walker's transcript (`read_audit.py`, every Read, Grep, Glob and Bash call) found that walker 3
read nothing outside the copy but folder listings and its own brief. Walker 1 also read lines of two of the copy's
comparison records, the parked-debt and the layers ones, which run A's brief allowed and which describe earlier findings
and their fixes. Walkers 2, 4 and 5 read the working tree's round record, whose `[recall]` then named the two
mechanical plants' kinds, and only walker 5 said so. No walker of run A read the sealed key, its script or another
walker's return, none read the copy's reviews, and none read anything in the scratchpad but its own files. The two mechanical plants are
therefore scored as Stage 0's, which caught both on the copy, and the walkers' recall over the ten judgement plants.

### [walk-run-b] Run B's first dispatch, and the seal repaired

Walker 2 walked its band, 20 findings over 168 cells, disclosing that it read the working tree's round record first.
Walkers 1, 3, 4 and 5 reviewed their briefs instead of walking: the reading rule added before run B drew them to the
brief's seal, and they found its holes, each real.
- The key, the seeding script and run A's returns sat in the temp root beside the copy. Walkers 4 and 5 listed them and
  hashed the key, and walker 4 read the plant labels in the script; none of them walked.
- The copy's reviews and comparison records describe the plants' original findings and their fixes, so a walker that
  reads the history can find a plant without walking to it.
- The scratchpad held Stage 0's run on the copy, unplanted copies of the design from dry runs, and older snapshots,
  beside the walkers' scratch folders.
- The brief named no item tags, so the expansions' items, and `test.seed`'s place in the adopt step, were guesses.
- The walk's failure-mode and STRIDE readings have no slot in the return and no check.

Repaired before the re-dispatch: the key, the script and every return, and run A's scratch folders, moved out of the
temp root, and the scratchpad's dry-run trees, snapshots, atlas pages and Stage 0's run on the copy with them. The
brief now opens with its task, lists the only places a walker may read (the copy's design records but its comparison,
instruments and session-log records, its reviews and its prompts; the map; Stage 0's leads; code; the walker's own
scratch folder, outside the scratchpad), names every item its table owes, and asks for a line naming any read outside
the list. Walkers 1, 3, 4 and 5 walk again as dispatches 170 to 173, their handoffs
`prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-11-spec-reviewer.md` to `...-14-spec-reviewer.md`, on the same copy. The
missing failure-mode and STRIDE slots are the walk kit's defect, for the fold to route to dFairHearing's walk preset.

The working tree is an unplanted copy of every design record, and no move can take it out of a walker's reach, so the
seal is the allow-list and the read audit, not distance. The audit gained two classes for it: any path into the
scratchpad, and any path into the temp root outside `seed-dcl/`, where the copy and the walkers' scratch now live. Both
red on walkers 4 and 5's brief reviews, which listed the temp root and found the key there. The four brief reviews are
kept apart from the walk returns, so the walks take the returns' names, and are committed beside them after the scoring.

### [walk-run-b-again] Run B, walked again

Walkers 1, 3 and 5 walked as dispatches 170, 171 and 173: 12, 13 and 15 findings, every table complete. Each disclosed
what it read outside its list before it took the brief as its instructions: the working tree's round record (walker 1
lines 90 to 328, walker 3 whole, walker 5 from `[scenarios]` on), diffs against sibling briefs, and folder listings.
The read audit agrees, and none of them read the key, the script, a return or the copy's reviews. Walker 4 reviewed
its brief a second time (172) and found six defects, each now answered:
- **Review history the list admits:** fold and review records, and revision notes inside design records, describe the
  fixes the plants revert. Recall stays an upper bound, as `[recall]` says, and each hit is read by hand for a
  revision note as its evidence.
- **The copy's `[recall]` names Stage 0's arms for the mechanical plants.** Both runs count those plants as Stage 0's,
  which `score.py --stage0-caught` now does, a walker's hit on one adding nothing (`[recall]`, the bar as scored).
- **A build verdict can rest on items its walker does not walk,** since `[slicing]` deals builds by scenario and band,
  not by the items they own. The report joins build verdicts as the walkers gave them, and the fold reads each against
  its items' owners.
- **`findings_of` handed a batch's last finding the walker's whole table** when the table sat under no heading. It now
  ends a finding at any table row or numbered bold label, seen red first on all four of run A's dry-rendered batches
  (127 to 252 table lines each) and on none after.
- **The walkers' scratch folders share a parent the read audit did not watch.** A class for it is added.
- **The protocol files the charter names sat outside the list:** `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`
  are on it now, for the skeptics too.

The cause, which walkers 1 and 5 named as well: the spec-reviewer role reviews the spec it is handed, and the walk
brief is handed as `input:spec`. Walker 4 walked a third time (174), its handoff's goal and non-goals rendered from
`build/2026-10-20-build-PLAY-dClosedLoop-1-walk-handoff-brief.md`, which names the sealed copy's records as the specs
and the brief as the lens. It walked: 15 findings, its table complete, and the only walker of either run whose read audit is clean. The audit now reads a relative path by where its call stands, which cleared two false hits on it.

The skeptic and synthesis briefs gained the walkers' list of what may be read and the line for any read outside it,
and the synthesis's shape line now leaves `agents` to the main loop, which counts every dispatch of the run from its
returned lines, where the template had typed eleven.

### [walk-scored] Both runs, scored

- **The reports:** run A's reads BLOCKED with 72 of 78 findings confirmed, and run
  B's reads BLOCKED with 69 of 84 confirmed. Each passes `walk.py check --report`
  over all 812 cells, 22 builds and 42 principles.
- **The recall bar is NOT MET.** Run A finds 3 of the ten judgement plants, run B 2, and the two together the same
  as run A. With Stage 0's two, that is 5, 4 and 5 of twelve, against eight a run and ten together. Chapman's
  trend over the two runs' real findings, matched by full address, is 396, 281 of them found by
  neither (62 and 62 real, 9 shared). The count is inflated, since one defect
  named at two addresses counts twice.
- **A hand reading of every unhit plant's near findings changes no count.** It finds a pattern in what the walk misses,
  and one true plant lost at a skeptic. Both stay sealed with the key until the owner's word, since one option before
  the owner is a third run on this copy.
- **Cost:** 25 dispatches and 1,190,395 output tokens, 1h30m26s from the first walker to the last report. Run A's walk
  spanned 14m07s, its skeptics 8m11s and its synthesis 10m14s. Run B's walk spanned
  41m18s over its ten dispatches, its skeptics 18m52s and its synthesis 9m30s.
- **By `[recall]`, a run under the bar comes to the owner before anything is folded.** The owner's word is asked.

### [walk-run-c] Run C, the clause walk, and a second look at refutations

The owner, 2026-10-20, asked what follows a walk under the bar, answered "Run C: a clause walk (Recommended)", and asked
whether refutations get a second look, answered "Second skeptic on refutations (Recommended)".
- **Run C** walks the same sealed copy, its key still sealed, sliced by chain build as `[slicing]`'s C rows say. Each
  walker reads every clause of its builds against the records that settle what the clause builds, and returns one row
  per clause, `| clause | build | read against | verdict |`, the verdict `holds` or the ids of its findings.
- **Run C's bar,** fixed before it is dispatched: each scenario run joined with run C, A with C and B with C, finds at
  least eight of the twelve with Stage 0's two, and the three runs together at least ten (`score.py --with`).
- **The second look:** every finding a skeptic refuted, in runs A, B and C, goes to a second skeptic, who sees the
  finding but not the first refutation. A refutation stands only when both refute it, and a split goes to the report
  as unverified, which the recall does not count. Runs A and B each take one more skeptic for it, five verify agents a
  run, and run C's four skeptics and its second look make five.
- **Afterwards** the three runs' confirmed findings fold together, and the key and the hand reading are committed.

### [walk-run-c-scored] Run C, scored with runs A and B

- **Run C's report** reads BLOCKED: 95 of 108 findings confirmed, 11 refuted and
  2 unverified after its second look, one of them a blocker. Its check over all 495 clauses and 22 builds
  is clean.
- **The second looks** left 3 of run A's refutations standing and moved 3 to
  Unverified. In run B, 10 stand and 5 moved. A refutation and an unverified
  finding are both outside the recall.
- **Run C's bar is NOT MET.** Run C alone finds 3 of the ten judgement plants. Joined with it, run A finds
  7 of twelve, run B 6, and the three runs together 7, against eight a joined run and ten
  together.
- **A hand reading,** sealed with the key, reads one of run C's hits as a neighbour of its plant. It also finds two
  plants whose deleted rule survives only in the review history the walkers' list excluded, which no walk inside its
  list could cross-reference.
- **Cost of the three runs:** 38 dispatches, the second looks among them, and 1,928,719 output tokens.
- **By `[recall]`,** the owner's word is asked again before anything is folded.

### [recall-scored] The recall, read plant by plant, and the fold's plan

The owner, 2026-10-20, asked what follows run C under the bar, and answered "Fold, re-measure after (Recommended)". The
seal is lifted: the key (`build/2026-10-20-build-PLAY-dClosedLoop-1-walk-key.json`, its SHA-256 the pinned one), the
seeding script (`...-walk-seed.py`), the five brief reviews and the detectability probe (`...-walk-detectability.py`)
are committed beside the walk. The key's pin is over its committed blob: a checkout that writes CRLF changes the
working copy's bytes, so check it with `git cat-file -p HEAD:<path> | sha256sum`.

| Plant | Where | What was reverted | The rule in allowed records | A | B | C | Read by hand |
|---|---|---|---|---|---|---|---|
| P01 | v2 `[chain]` 0019 | the step walk's failure route | only in excluded review history | none | none | none | unfindable by cross-reference; A4-F4 is a neighbour |
| P02 | v2 `[chain]` 0229, 0231; memory-plan | the `journal` alias | memory-plan, three times | none | none | C3-F14 | a hit |
| P03 | v2 `[chain]` 0284 | the restarted supervisor's reconciliation | only in excluded review history | none | none | none | unfindable by cross-reference |
| P04 | v2 `[chain]` 0305, 0377 | intake ratifying only from its owner origin | one research mention | none | none | none | missed; a run A walker cited the planted 0377 as its reference |
| P05 | v2 `[chain]` 0488 | the declined retirement's amended row | twice in v2 | none | none | none | missed |
| P06 | flow-steps `entry.claim` | the unreachable remote's route | `leases.offline`'s row | A5-F6 | refuted twice (B1-F7) | none | contestable: the policy row arguably answers the case |
| P07 | v2 `[chain]` 0283 | fallback witnesses kept readable across the drain | once in audit-fold | none | none | CS1-F1 scored | a neighbour: a different defect at its clauses |
| P08 | flow-steps `entry.intake` | the hook made a scout | an item row | A1-F1 | B1-F1 | C4-F4 | a hit in every run |
| P09 | flow-steps `plan.exit` | ratification as the planner records it | an item row | A1-F2 | B1-F2 | none | a hit |
| P10 | v2 `[chain]` 0289, 0318 | the commit queue | 37 mentions | none | none | none | missed by every run |
| P11 | layer-memory kind table | a kind's writer (mechanical) | n/a | Stage 0 | Stage 0 | Stage 0 | Stage 0's |
| P12 | v2 `[chain]` 0093 | P23's only clause (mechanical) | n/a | Stage 0, A1-F3 | Stage 0, B1-F3 | Stage 0, C2-F1 | Stage 0's, and every run's |

- **The pattern:** every plant on a flow-steps item row was found, and the clause deletions were missed. The two whose
  rule survives only in excluded history were unfindable by any walk inside its list, a defect of this seal's design.
  The others survive in allowed records, P10 in 37 places, and were missed: the walks read clauses and items, not the
  records' settled rules looking for the clause that carries each.
- **The fold** takes all three runs' confirmed findings, 236 across the three reports, before anything else. The
  shortfall, the seal's defect and the blind spot are recorded as this audit's known limits.
- **The re-measure,** before the baseline: a fresh sealed copy, new plants, none whose rule lives only in excluded
  history, and a record-to-clause slice beside the scenario and clause slices, scored against a bar fixed first.

## [fold] The fold, its forks and the owner's answers

The fold ran as six writers, each one script applied in order to a copy and checked there by the build's ten final
checks (`dry_run.sh` in the session's scratch, recorded in the instruments). Writers 1 to 3 took v2's `[chain]` rows by
build, writer 4 flow-steps and writer 5 the other records (`fold-brief-w1` to `-w5`). Writer 6 took the requests the
five listed for one another's records and the reconciliation probe's lines their folds raised (`fold-brief-w6`). Their
returns are `fold-return-w1` to `-w6`.

- **The main loop's amendments, each a comment in the script it touches:** writer 2's place 68 ranked a fork "under
  `design.forks`' default", a key of dIndexedDesign, which dBoundRoles does not descend from, so the ranking is stated
  as the core's own; writers 1 and 4 named the new states differently, so the terminal is `incomplete` and the hold
  `parked`, since the atlas reads one-word terminals.
- **The dry run, through writer 6:** nine of the ten checks green; the probe's four remaining lines rest on FK-6-1 and
  FK-6-2.
- **The forks:** 35 raised; two pairs merged, FK-1-4 with FK-3-1 and FK-4-12 with FK-5-2; 33 questions
  asked through the question tool, each recommendation first. The owner answered all 33 on 2026-10-20, and
  5 chose an option the question did not recommend: FK-1-3, FK-1-5, FK-4-2, FK-4-12 + FK-5-2 (two writers, merged), FK-4-13.

| Fork | Asked | The owner's answer, verbatim |
|---|---|---|
| FK-1-1 | Where do the override record and the exception register live, and through which door are they written? | "In the build folder (Recommended)" |
| FK-1-2 | How are clause ids and a spec's Carries relation typed in the map's closed address and edge sets? | "New id class + edge (Recommended)" |
| FK-1-3 | Which file is the one declaration of each cap's value? | "budgets.* now" |
| FK-1-4 + FK-3-1 (two writers, merged) | which values stay for install.retired-edits (order, keep, delete) and install.on-shim-call (warn, journal, refuse)? | "Drop delete and refuse (Recommended)" |
| FK-1-5 | Where does a patch build's draw on its root's rework budget land once the root has closed? | "Reopen root record" |
| FK-1-6 | While the card-import fixture is red, which wins: cl-0150's fresh-session rule or resume.context? | "Fixture wins (Recommended)" |
| FK-1-7 | A retry from a new session must be refused as a duplicate. Does a message's id keep its sender's session? | "Drop the session (Recommended)" |
| FK-2-1 | Does the landing push release the build's lease, or does the lease live until deploy.unlease? | "Live until unlease (Recommended)" |
| FK-2-2 | Which clock corrects a lease holder's stamp, who measures the offset, and how do the two expiry rules combine? | "Supervisor, 'or' (Recommended)" |
| FK-2-3 | How do the event-wait sweep and the landing's release arms run before dShippedRelease lands? | "Generic sweep, arms move (Recommended)" |
| FK-2-4 | How does lease expiry tell a fence beat from a renewal? | "Beats mark renewal (Recommended)" |
| FK-3-2 | roles.model.<role> holds one model, but a role may run on several harnesses. How does the key fit? | "Per-harness key (Recommended)" |
| FK-3-3 | design.streams is both the planner's item and a policy key. Rename the key? | "Rename to design.streams-when (Recommended)" |
| FK-4-1 | Does run.on-owner-question decide an owner item that attendance raises at the moment it is raised, and where does a late answer go? | "Hold, then amend (Recommended)" |
| FK-4-2 | Can best-effort-recorded fill your landing gate and design gate under three-gates and every-stage? | "Yes, as LR-3 reads" |
| FK-4-3 | What do deps.on-parent-withdrawn's adopt-parent-work and withdraw-too do? | "Inventory + owner item (Recommended)" |
| FK-4-4 | How does your mid-build "audit the specs" reach review.trigger? | "Placement disposition (Recommended)" |
| FK-4-5 | Where does a loop's open work go past flow.route-backs, and which bound wins against review.max-rounds? | "Units, then exhaustion (Recommended)" |
| FK-4-6 | What happens to a decision candidate the two raters disagree on? | "Stays reconstructed (Recommended)" |
| FK-4-7 | Does landing.order order landings across nodes? | "Yes, landing-turn ref (Recommended)" |
| FK-4-8 | What does deploy.distill do before dScopedBuild's build.distill writes any rows? | "Unarmed (Recommended)" |
| FK-4-9 | Where are the interim stand-ins for routes into later builds declared? | "Rules bullet + rows (Recommended)" |
| FK-4-10 | What is a paused build's deadline, and what happens when it passes? | "Wait, then owner item (Recommended)" |
| FK-4-11 | What puts a leg into quarantine under verdict.flakes? | "Split the key (Recommended)" |
| FK-4-12 + FK-5-2 (two writers, merged) | who writes the seen-red record that test.seen-red reads? | "build.acceptance" |
| FK-4-13 | How does a best-effort descope remove a failing unit that is already in Test's tree? | "Revert row, no draw" |
| FK-5-1 | kits.install and kits.update each have two actors. How do they split, and what closes their outcomes? | "Command + attended items (Recommended)" |
| FK-5-3 | How is a mail, lease or tombstone write bound to the identity it names? | "Refuse at record's door (Recommended)" |
| FK-5-4 | Who answers a mailbox question addressed to a build that runs unattended? | "A flow item (Recommended)" |
| FK-5-5 | What do maintain.tiers: bands and maintain.on-breach's red-leg and report do? | "Declared edges (Recommended)" |
| FK-5-6 | How is environment E's promotion lease declared, and how is a stale holder's promote or rollback fenced? | "Cadence lease + CAS (Recommended)" |
| FK-6-2 | Which build owns patch.ratify, now that entry.claim reads it for every patch, and what stands in before it lands? | "Move to dPlacedRequest (Recommended)" |
| FK-6-1 | Before dPlacedRequest lands leases.offline, what does dFairHearing's review.report do when the remote is unreachable at a new: slug's claim? | "Refuse (Recommended)" |

The answers are folded by two writers in parallel, after the six (`fold-brief-w7`, `-w8`). A new clause carries a
placeholder id, and the main loop's mint step numbers them on from `[clause-ids]`' next free id.

## [fold-applied] The fold applied: the later answers, the integration and the checks

The answers were folded by writers 7 and 8 in parallel and writer 9 integrated what they left (`fold-brief-w7` to
`-w9`; returns `fold-return-w7`, `-w8`, `-w9`, and `-w9b` for writer 9's resumed pass with FK-9-1 and FK-9-2). Each
pass's tally, derived from its return and its script when it returned, is its dispatch row in the session log, rows
204 to 207.

Their folds raised 4 forks after `[fold]`'s round, answered as they came:

| Fork | Asked | The owner's answer, verbatim |
|---|---|---|
| FK-7-1 | Once a cap's row moves under budgets.* (your FK-1-3 answer), may a run still raise it? | "Run may raise, per the file's rules (Recommended)" |
| FK-8-1 | Before dRankedPlan and dIndexedDesign land, a placement routed to Plan or Design has two stand-ins: cl-0123 files an owner item carrying the claim, while FK-4-9's new [rules] bullet sends a route into a role item to the attended session's agent. Which governs? | "The clause's own wins (Recommended)" |
| FK-9-1 | Before dScopedBuild lands, where does dDeclaredLoop's build.recommend route when decisions.major: author-owner-ratifies sends it to the owner item build.ratify? (The window only opens between dLinkedLibrary and dScopedBuild, and only under a non-default value.) | "Own owner gate (Recommended)" |
| FK-9-2 | Between dSafePassage's step moving caps under budgets.* and dDeclaredLoop's guard landing, cl-0012's minimal guard refuses every agent write to the policy file. How does a run raise a cap in that window? (cl-0036's raise, in dOrderedCharter, falls inside it.) | "Guard admits one shape (Recommended)" |

In all, 39 forks were raised and 37 questions asked; 5 answers chose an option the
question did not recommend: FK-1-3, FK-1-5, FK-4-2, FK-4-12 + FK-5-2 (two writers, merged), FK-4-13.

- **The probe widened.** The reconciliation probe's docstring kept rule 3 to the breakpoint program "until the audit's
  fold classes what it finds"; the owner's FK-4-9 asked for a tolerance row per forward route, so every run now reads
  every route, and writer 9 classed what the widened run found. The readings before and after, and a dropped row seen
  red, are in the night pass's instruments record, `[fold-probe]`.
- **The mint step** numbered the writers' placeholder ids in their order of first use in `[chain]`:
  `cl-dClosedLoop-W8-1` → `cl-dClosedLoop-0503`, `cl-dClosedLoop-W8-2` → `cl-dClosedLoop-0504`, `cl-dClosedLoop-W7-2` → `cl-dClosedLoop-0505`, `cl-dClosedLoop-W8-3` → `cl-dClosedLoop-0506`, `cl-dClosedLoop-W8-4` → `cl-dClosedLoop-0507`, `cl-dClosedLoop-W7-1` → `cl-dClosedLoop-0508`, `cl-dClosedLoop-W7-3` → `cl-dClosedLoop-0509`; the next free id is `cl-dClosedLoop-0510`. It leaves an agent's saved
  return verbatim, a defect writer 8 found in its first version.
- **The K5 step,** the main loop's: `cl-dClosedLoop-0004` joins P35's row; `cl-dClosedLoop-0016` joins P38's row. Writer 1 folded both citations, and Stage 0's K5 arm reds a
  clause citing a principle by id outside that principle's `[enforcement]` row; each clause enforces what it cites, so
  it joins the row (`k5_rows.py`). It was found when the instruments recorder's Stage 0 plant `k5-cited` could not red
  for its own reason over the folded tree.
- **The checks:** applied to the tree and run on a copy of it, design map rc 0, atlas rc 0, fold state rc 0, reconciliation probe rc 0, clause scan rc 0, clause ids rc 0, gap join rc 0, preset check rc 0, critical path rc 0, first-segment probe rc 0;
  `ALL rc 0`.

## [stage0-classes] Stage 0's classes

Empty until the audit's fold classes what it does not fix.

| Arm | Node | Class | Reason |
|---|---|---|---|
