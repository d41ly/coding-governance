# Research: The whole-design audit: what earlier audits covered, critical-gap classes and a proposed workflow

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 155's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-28-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md`.

---

**The whole-design audit: what earlier audits covered, critical-gap classes, methods, and a proposed workflow (owner's question 1)**

**Answer.** Yes, an adversarial workflow can review the whole design step by step, but not with the shape the earlier audits used. I recommend the design run in three stages:

- **Stage 0, no agents:** mechanical completeness checks over the records.
- **Stage 1, two agent runs:** two independent scenario walks, sliced in two different directions (one by scenario, one by step). Each run is graded by its recall on real past defects planted back into a copy of the records.
- **Stage 2:** the existing paired closing review over the fold.

It runs after the other four questions' folds land and before the first chain build's spec. No method can prove that zero critical gaps remain. What this one can give the owner is a filled coverage table, a measured recall, and a check that the last round found no new critical.

All counts below were measured on this branch at `930120e45` on 2026-10-19 unless marked otherwise. The tree is unchanged. I deleted my scratch folder, and the untracked `...-research-final-atlas.md` that appeared during my run is another researcher's file, not mine. One side effect to disclose: running `query.py` rebuilt the recall cache under `<git-common-dir>/recall/cache/` (`tools/memory-recall/recall_conf.py:181`). Nothing in the working tree changed.

---

## 1. What the earlier audits covered

### 1a. Every review, grouped

Figures come from each report's `review-shape` line, and the Chapman estimates come from the `*-reviews-compared.md` records `[summary]`. All 50 reports together:

- 499 agents, 9.58M output tokens.
- 1,864 raw findings, of which 1,601 were confirmed.

No record states wall-clock time for any review. The register's own `gap-rt-26` says "an act records no cost or duration".

| Review (reports) | Kind, lenses, slicing | Subject | Raw / confirmed | Chapman, found by neither | Agents / out | What it could not see |
|---|---|---|---|---|---|---|
| Layer audits ×5 pairs, 10-15 (10) | spec audit, full, 5 fixed lenses; sliced by layer record | each layer record whole, at its blob | 551 / 481 | 35 over 265 defects (layers-reviews-compared `[summary]`) | 110 / 2,239k | v2 and the chain did not exist in their final form; cross-layer seams |
| Expansions pair (2) | full diff | `ee2eee6..f56e80f` | 99 / 83 | 3 over 38 | 22 / 509k | the core layers' later folds |
| Lexicon + review system pairs (4) | spec audit, full | lexicon at `424d2a7de`, review system at `40738693d` | 201 / 176 | 7 and 3 (debt-reviews-compared `[summary]`) | 44 / 871k | the rest of the design |
| Light fold reviews, 10-16 (13) | light diff, 3 lenses | fold ranges | 333 / 278 | 2 to 6 per pair | 117 / 1,812k | the security and intent lenses; anything outside each range |
| Debt folds (1), systems-retrofit (1) | full diff; spec audit | ranges; the systems and retrofit records | 94 / 84 | not paired | 22 / 620k | v2 whole |
| Chain order (1) | spec audit, full | v2 `a8038f04e` + re-cut | 35 / 32, 10 high | not paired | 11 / 341k | step walks; prose dependencies |
| **Declared whole-design audit** (1) | spec audit, full, 5 lenses, seven questions | v2 `535c0e058` + gap register `9a05621f4` whole, with 18 records as context | 34 / 33, 6 high | not paired | 11 / 218k | missed the dShippedRelease to dWellOiledMachine edge, which the main loop had logged before it ran (session-log, 2026-10-18 entries) |
| Audit-fold closing (1) | full diff | `dc97a1b25..159b4d467` | 38 / 26 | not paired | 11 / 275k | the fold's later commit `7e3d5d5b1` (454 lines, still unreviewed) |
| Night-pass and away-pass closing (2) | light diff | ranges | 47 / 45 | not paired | 17 / 265k | the security and intent lenses |
| Answers fold pair (2) | light diff | `a9b00add..fe3d09ab` | 32 / 23 | 4 over 17 | 18 / 231k | same |
| **Shape audit pair** (2) | spec audit, full; each lens carried one shape question as its `lensNotes` | v2, register and memory plan at `89e44048f`, with 28 records as context | 105 / 98, 66 defects, 9 high | **15 over 66; overlap 0.39, the lowest of any pair** | 22 / 551k | the stage walk (see 1b) |
| Folds-closing, flow-adoption, night-pass-two, NT answers pairs (8) | light diff | four ranges | 213 / 172 | 5, 6, 6, 6 | 72 / 1,288k | the security and intent lenses |
| Parked-debt pair (2) | full diff, 5 lenses | `320c796..6ba4eaa` | 82 / 70, 35 defects, 8 high | 6 over 35 | 22 / 365k | the fold it produced (`930120e45`) |

Across every pair, one run alone finds 58% to 88% of what the pair finds, and the overlap between runs is 0.32 to 0.54. Twelve pairs recorded a Chapman estimate (the ten in the table plus the two layer pairs the table groups); every one of them leaves defects that neither run found.

### 1b. Coverage mapped onto the design's parts

I attributed each of the 1,601 confirmed findings by exact token match on its `ref` and `reason` cells: the 116 item names from the design map's `--ns item`, the 21 chain build names, and `P1` to `P40`. These counts are floors. 1,216 findings name no item, 1,091 name no build, and 1,463 name no principle.

The "whole" column below is the four whole-design reads: the design audit, the chain-order review and the two shape-audit runs.

| step.* | whole | record audits | diff reviews | high | | chain build | all | of which whole |
|---|---|---|---|---|---|---|---|---|
| entry | 13 | 22 | 19 | 14 | | dIndexedDesign | 8 | 1 |
| plan | 5 | 18 | 15 | 6 | | dFurnishedOrders | 10 | 2 |
| **design** | **0** | 17 | 14 | 5 | | dTendedCadence | 12 | 6 |
| build | 1 | 44 | 41 | 5 | | dKeptSession | 16 | 5 |
| **test** | **0** | 42 | 30 | 6 | | dScopedBuild | 16 | 4 |
| **deploy** | **0** | 52 | 69 | 18 | | dCalibratedLens | 19 | 6 |
| breakpoint | 2 | 31 | 22 | 5 | | (highest) dWellOiledMachine | 142 | 41 |
| **probe** | **0** | 0 | 5 | 1 | | dDeclaredLoop | 129 | 45 |
| **lifecycle** | **0** | 0 | 24 | 6 | | dOrderedCharter | 116 | 45 |
| **adopt** | **0** | 5 | 1 | 0 | | | | |

- **Principles:** P6, P12, P14, P17, P21, P25 and P31 are named by no confirmed finding at all. P12, P17 and P25 are among the principles the brief says bind this answer. Only P28 (37), P38 (17) and P39 (12) are named more than 9 times.
- **Layers, by the record each finding cites:** no whole-design read ever took a layer record as its subject. The layer records were read whole only at their 10-15 and 10-16 audits.
- **Parts no audit has read end to end.** I re-ran the build's own line-coverage instrument from `2026-10-16-build-PLAY-dClosedLoop-1-state.md [revisit-instrument]` at HEAD. Its regex was extended to read the shape audits' `Subjects (round 1):` line.
  - **Totals:** 12,458 of 30,353 lines (41%) in 48 design records have been read by no review.
  - **v2 and the gap register:** 3% and 0% unreviewed.
  - **Whole records never read:** project-map 100%, ownership-verify 100%, ownership 97%.
  - **Under-read records:** audit-fold 54%, flow-steps 15%, layer-expansions 14%.
  - **The latest fold:** `930120e45` wrote 265 lines that no review has read.
  - **No step walked end to end since its layer audit:** flow-steps was last read whole at blob `43e9cf4b` on 10-15. The shape audit's own defect `cycle-walk` says "nothing walks the owner's cycle end to end" (shape-reviews-compared `[map]`).

### 1c. The session model's walk against the lens reviews

- **The walk.** One author, no agents, walked a pre-v2 design end to end and found 14 holes (`2026-10-14-...-session-model.md [holes]`), plus H15 and H16 later. All are scenario-shaped:
  - missing witnesses (H1, H2);
  - missing actors or launch (H3, H4);
  - missing routes (H5, H10, H13);
  - concurrency (H6, H7);
  - timing and notification (H9, H12);
  - an owner for a check (H11); session loading (H14).
- **The lens reviews' dominant classes are different.** Across the 1,601 classes cells:
  - `two-answers-to-one-question` 71;
  - `amendment-leaves-its-other-half-standing` 62;
  - `policy-value-with-no-route` 32;
  - `rule-stated-with-no-check-that-fails` 32;
  - `retirement-inventory-misses-readers-by-value` 27.
- **Lens use.** Security confirmed 23 findings and intent 43, against correctness at 259.
- **They complement each other.** The walk found H1, the owner-proof hole. Its fix (`tty-cli`) was later found forgeable by a lens review (shape `owner-proof-forgeable`, fork SA-1).

---

## 2. Critical-gap classes and what checks each today

I define a finding as **critical** when the skeptic grades it high or blocker **and** its consequence is one of these:

- **(c1)** a chain build cannot be specced, or cannot land, in order;
- **(c2)** a scenario cannot reach a terminal, or reaches one without its witness;
- **(c3)** a guard or check silently loosens, or certifies what it does not check;
- **(c4)** built work or adopter data is overwritten or lost (P19, P38);
- **(c5)** a principle has no enforcing clause.

| Class | Existing mechanical check | Measured today | Only an adversarial reader finds |
|---|---|---|---|
| K1 a step item with no actor, input, witness, route or owner | role matrix, actor arm only (`layer-roles [instrument]`) | My probe of flow-steps: 90 of 90 items have Actor, Proven by, Then and Owner. 10 have Needs "—", all step-entry items. **The record's count is stale:** layer-roles:417 says "81 items", and the matrix is not in the night-pass instruments' last `[final]` re-run. | whether the witness is actor-typed (P2), and whether the outcome is the right one |
| K2 a scenario that cannot reach a terminal | reconciliation rule 6 only: each disposition routed through `entry.claim` has a `none` row (`reconcile.py:25`). The static termination check is planned (v2:1588, dDeclaredLoop). | 39 of 90 Then cells carry no `→` route. A planted plan item routed to `deploy.land` (owned by dShippedRelease, not an ancestor) read **findings 0, rc 0**: only routes into the breakpoint program are checked (`reconcile.py:15-17, 135`). | failure and interrupt routes (shape `walk-failure-route`, high) |
| K3 a record kind with no writer or no reader | none. The registry's writer and readers fields are planned (v2:1593, dTotalRecall). | layer-memory:397-477 lists 79 kinds: 34 say "writer item not named" and 1 "no writer item". The table has no reader column at all. | whether a non-item writer is real |
| K4 a key no unit reads | none at design time. dKeptSession's reader join (v2:1590) and dGroundRules' no-reader arm (v2:1584) are planned. | 33 of the 254 catalogue keys my parse found (the record says 261) are cited by no `[chain]` row and no item. All 33 appear in layer or system records. v2:1590 already accepts unnamed keys as a shrink-only population. | whether one of them is guard-bearing |
| K5 a principle no clause enforces | none. The principle registry and meta-check are planned (v2:821, v2:1586, dOrderedCharter). | `[chain]` cites only 12 of 40 principles by id. | whether a cited clause actually enforces |
| K6 a clause reading what no ancestor registers | reconciliation rules 1, 4 and 5, on backticked citations | rc 0 at HEAD, 22 non-ancestor dependencies classed. It does not read: prose (118 plain-word mentions), systems cited in prose, and 5 points of another layer. | prose dependencies (design-audit H1) |
| K7 a bootstrap hole | reconciliation rules 1 to 3 plus the class table | the H1, H2 and dShippedRelease edges are now gated, but only for named shapes | a mechanism named in plain words |
| K8 a gap owned by no build, or by two | gap join | 378 keys, 21 builds, clean | — |
| K9 a preset or catalogue hole | preset check | 235 of 235 presettable keys | — |
| K10 a judgement class: fail-open, trust boundary, multi-node race, in-flight migration across a drain, retirement by value | none | Of the 15 high defects in the design audit and the shape pair, about 7 are mechanizable at least in part (H1 to H5, the journal rename, the orientation card). About 8 need judgement (H6, owner proof, step gate, failure route, off-node bindings, receipt schema, supervisor restart, rows-lack-steps). | all of it |

The design map's ownership plants (`orphan`, `no-owner`, `two-owners`) each return rc 1. So owner completeness for items, keys and record kinds is mechanical today.

---

## 3. Adversarial design-review methods

All sources were read 2026-10-19.

| Method | What it catches, with its evidence | Where it fits here |
|---|---|---|
| ATAM, scenario-based architecture evaluation | Across 18 ATAMs, twice as many risk themes were risks of omission as of commission ([SEI TR-2006-012](https://sei.cmu.edu/library/risk-themes-discovered-through-architecture-evaluations/)) | Scenario walks are where omissions show (1c). |
| Scenario-based reading against checklist and ad hoc | The scenario method had a higher detection rate than ad hoc or checklist, and checklist reviewers were no more effective than ad hoc ([Porter, scenarios page](https://www.cs.umd.edu/~aporter/html/scenarios.html); [Porter, Votta and Basili 1995](https://drum.lib.umd.edu/items/96204769-6905-4196-b903-709ad81148ee/full)). I did not obtain the exact percentages. | Supports giving each finder a distinct systematic slice. |
| Fagan inspection with checklists | IBM data: 38 defects per KLOC found by inspection against 8 by unit test, and 82% of released-product defects found by inspection ([arXiv 2005.09217](https://arxiv.org/pdf/2005.09217), secondary; original [IBM SJ 1976](https://ieeexplore.ieee.org/document/5388086), full text not read) | The bug-class checklist the harness already hands its finders. |
| Capture-recapture (Chapman) | Accuracy depends on the number of inspectors: with fewer than 4, no model was accurate enough. Chapman suits two inspectors of unequal skill ([Briand et al.](https://pure.ul.ie/en/publications/a-comprehensive-evaluation-of-capture-recapture-models-for-estima/), [ISERN-98-11](https://ehealthinformation.ca/web/default/files/wp-files/isern-98-11.pdf)) | Our pairs' Chapman figures are a trend to watch, not a gate. |
| Defect seeding (Mills 1972) | Estimates remaining defects from the share of seeded ones found. It only holds if seeded defects are as detectable as real ones, and it is weakest for hard defects ([arXiv 1009.2785](https://arxiv.org/pdf/1009.2785)) | Seed real past escapes, not synthetic ones. |
| FMEA | No empirical comparison with design review found ([NASA NTRS](https://ntrs.nasa.gov/citations/20040086890), qualitative only) | Its failure mode, effect and detection columns become the failure walk's table. |
| Pre-mortem | Prospective hindsight raised the number of reasons people generated by about 30%; quantity only, not accuracy ([Klein, via the PHF copy](https://archive.phf.org/resourcestools/Documents/Pre_Mortem_Analysis.pdf); [critique](https://corporate.jasoncollins.blog/premortem)) | A cheap opening frame for each walker. |
| STRIDE per element or interaction | Measured on precision, recall and productivity in an academic setting ([replication, arXiv 2208.01524](https://arxiv.org/pdf/2208.01524)). An industrial case documented no incorrect threats ([arXiv 1910.03422](https://arxiv.org/pdf/1910.03422)). | The multi-node and adopter walkers' trust boundaries. Only 23 security-lens findings so far. |
| Red teaming | Doctrinal and case-based evidence only ([UK MOD handbook 2021](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1027158/20210625-Red_Teaming_Handbook.pdf)) | The skeptic stage already does this. |
| Model checking and table checks | TLA+ at AWS found subtle design bugs that "deep design reviews" missed in S3, DynamoDB and EBS ([Newcombe et al., CACM](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods); [summary](https://blog.acolyer.org/2014/11/24/use-of-formal-methods-at-amazon-web-services/)). I did not verify the 35-step trace claim. SCR table checking found missing cases and nondeterminism in specs that human teams had already reviewed ([Heitmeyer et al. 1996](https://apps.dtic.mil/sti/tr/pdf/ADA465574.pdf)). | Table checks become Stage 0. Full model checking is deferred (candidate E). |
| Multi-agent LLM review, measured | A code-review agent system reached 33.9% precision and 20.0% recall ([arXiv 2608.09290](https://arxiv.org/pdf/2608.09290), not independently verified). LLM requirements QA showed high recall with variable precision ([arXiv 2408.10886](https://arxiv.org/pdf/2408.10886)). | The best evidence for this design is our own pairs: 58% to 88% per run. |

---

## 4. Candidates

Each candidate below carries its mechanism, the test that would make it lose, that test's result, and its owning chain build.

**A. Repeat the lens audit pair on the whole design** (`tier2-review.js` spec audit, the shape audit's mechanism).
- **Losing test:** do lens-sliced whole reads walk the steps, and can the harness emit a per-cell coverage witness?
- **Result: it loses.**
  - The four whole reads, 163 confirmed findings, cite design, test, deploy, probe, lifecycle and adopt items zero times.
  - The lens set is a fixed literal, and agent-cap denies a registry of lens sets (`tier2-review.js:741-773`). A note can only be added beside each lens brief through `lensNotes` (`:111`), not replace it.
  - The output is findings only, so a clean cell leaves no trace.
- **Kept for** Stage 2, the closing review of the fold.

**B. The main loop walks the design itself, session-model style, with no agents.**
- **Losing test:** can its recall be measured?
- **Result: it loses.** There is only one capture, so no Chapman estimate. The author knows any plants, so seeding is void. The precedent: H1's own fix was later shown forgeable.
- **Rejected.**

**C. Instruments only.**
- **Losing test:** how many of the 15 past high defects are in mechanizable classes?
- **Result: it loses alone.** About 7 of 15 are; about 8 are judgement-only (K10).
- **Kept as Stage 0.**

**E. Model-check the flow's state machine now.**
- **Losing test:** can a model be derived from the records mechanically?
- **Result: no.** 39 of 90 Then cells carry no `→` route, so a model would have to be written by hand, a second source that would drift, against P22.
- **Routed** to the lease protocol's unit specs (dPlacedRequest) as an FMEA or TLA-style acceptance. Not a pre-speccing gate.

**D. Recommended: Stage 0, then a paired walk sliced two ways, recall-graded by seeding, then the existing closing pair.** Detailed in section 5.
- **Its own losing test (not run here; it needs model calls):**
  - Each run must find at least 2/3 of the seeded defects, the union at least 10 of 12, and each critical class must be found by at least one run.
  - The scenario-by-step slicing must also beat same-slicing pairs: lower overlap on real defects at equal or better seeded recall. Otherwise both runs slice by scenario.

---

## 5. The proposed workflow (candidate D)

**Stage 0, mechanical, no agents, seconds.** Each check below is a design-time instrument in the build folder, as `reconcile.py` is. Each must be seen red on a plant before it is trusted.
- **Re-arm the role matrix:** add Needs, Proven by and Then arms over all 90 items (K1).
- **Extend reconciliation rule 3** to every route target and to reachability of a terminal (K2). It must go red on the `deploy.land` plant that passes today.
- **Record-kind writer and reader join** (K3).
- **Key-to-unit join** with a guard-bearing filter (K4).
- **A declared "enforced by" column for principles** and its join (K5).
- **Re-run the existing checks:** gap join, preset check, design map, clause scan, line coverage (with the subjects regex fix) and `review_debt.py`.
- Each red row is either fixed or classed. Each "left out" line becomes a named target for the walkers.

**Stage 1, the adversarial pair.** Two independent runs at the owner's medium effort (NT-12), one after the other, with run A's report held out of the tree while run B runs, as the earlier pairs did. Each run uses 5 walkers, 4 skeptic batches and 1 synthesizer: 10 agents, 4 of them verify agents. If "at most 5 verify agents in total" means across both runs, use 2 skeptic batches per run; the brief is ambiguous on this.

- **The scenarios:**
  - S1, a solo attended feature build on gov;
  - S2, an unattended build across two nodes (leases, mailbox, node profile, fleet);
  - S3, a patch build of a landing (Maintain to patch);
  - S4, an adopter's update (upgrade walk, receipt, overlay);
  - S5, a withdrawal or supersession;
  - S6, a failure injected at every stage (refused lease, owner silence, red unit, flake, landing conflict, unreachable remote, review CEILING);
  - S7, a bootstrap: chain build *k* specced and built with only builds before *k* landed.
- **Run A, sliced by scenario:** walker 1 takes S1; walker 2 S2; walker 3 S3 and S5; walker 4 S4 and S7; walker 5 S6.
- **Run B, sliced by step band, each band walked through every scenario:** entry and plan; design and build; test and deploy; breakpoint, probe and lifecycle; adopt and the 26 expansion items.
- **Builds and principles are split across the walkers** so that each run gives every one of the 21 builds and 40 principles one verdict.
- **The walk lenses:**
  - FMEA columns per item: failure mode, effect, detection, route;
  - STRIDE on S2 and S4's trust boundaries;
  - a pre-mortem opening line ("the chain shipped and failed in this scenario: why?");
  - the K1 to K10 checklist.
- **What each walker reads:**
  - flow-steps whole (98 KB);
  - the `[chain]` rows, `[policies]` keys and `[principles]` its slice names;
  - the design map at level 0 (32 KB) as its index;
  - its scenario's records: S2 reads layer-runtime, cloud-and-scale and stall-and-loop; S4 reads adopter-instructions, flow-roles-adoption, fates and layer-expansions;
  - Stage 0's red and left-out lines.
  - v2 whole is 335 KB, which is why the reading is sliced by section.
- **Output:** findings, plus a walk table with one row per item and scenario (actor, needs, witness, route, verdict, with "not on path" plus a reason allowed).
  - The skeptics refute findings, and they also try to refute a sample of clean cells.
  - The synthesizer joins both tables and goes red on any empty cell.
- **Why not `tier2-review.js` for this stage:** its lens briefs, its output schema and its agent-cap dialect do not fit the walk.

**Stage 2.** Fold the findings, then run `tier2-review.js` as a full diff review, paired, over the fold. This is the parked-debt shape: 22 agents, about 365k output tokens. Then re-run Stage 0.

**The witness for "no critical gap left":**
- Stage 0 is all green, and each check was seen red on its plant;
- both runs' coverage tables are complete;
- the seeded recall bar is met;
- zero critical findings stay open;
- the closing pair finds no new critical (P39's converged state);
- Chapman over the critical defects is reported as a trend, never as the gate, because of Briand's under-four-inspectors result.

**Cost:**
- **Stage 1:** about 600k to 800k output tokens and 20 agents. The shape runs measured 260k and 290k each, and the walkers read more.
- **Stage 2:** about 365k output tokens and 22 agents.
- **Stage 0:** seconds. The line-coverage instrument alone took 11.6 s.
- **Total:** about 1.0M to 1.2M output tokens. Wall time is unmeasured, so the runs must record it (`gap-rt-26`).

**The recall test.**
- **The seeded copy.** Following the blind-replay isolation in `review-system [design]`, a clone is made outside the repository from a bundle.
- **The plants.** Twelve fixed past defects are reverted into it, for example:
  - H1 and H2 (bootstrap);
  - H6 (fail-open);
  - M13 (unreachable remote);
  - M15 (migration across the drain);
  - `walk-failure-route`, `supervisor-restart`, `declined-retirement`, `intake-ratification`, `journal-rename`;
  - one dropped kind writer and one dropped principle clause, which Stage 0 must catch 100% of.
- **The key.** It is sealed and its sha256 is pinned in the run args before launch.
- **The scorer.** A `[tag]`-address scorer must exist first. Today `review_replay.py` refuses design reports: `REFUSED ... no-scorable: 45 item(s), none with a file-and-section location`, because its spec mode reads only `§<n>` (`tools/workflows/review_replay.py:36-44`).
- **The estimate.** A Mills estimate of what remains is cross-checked against Chapman.

**When it runs.** After the folds from questions 2 to 5 and the `930120e45` debt land, because each new surface opens at the first-audit rate again (state `[revisit-converging]`). Before any chain build's spec.

**Owning chain builds for the product version:**
- dFairHearing: the walk preset as a catalogue row, the coverage output, the `[tag]` scorer and the clean-cell refutation;
- dDeclaredLoop: K2 (v2:1588);
- dTotalRecall: K3 (v2:1593);
- dKeptSession and dGroundRules: K4 (v2:1590, :1584);
- dOrderedCharter: K5 (v2:821, :1586);
- dCalibratedLens: per-stage lenses calibrated on these replays.

**What must exist before speccing starts:**
- the Stage 0 instruments, each seen red;
- the walk script with its walk-table schema, as a build-folder instrument;
- the scenario record for S1 to S7;
- the critical rubric;
- the `[tag]` scorer and the sealed seeding procedure;
- wall-time capture;
- the folds from questions 2 to 5 landed.

**Proposed policy keys** (the recommended value is the default; the others are its allowed values):

| Key | Default | Other allowed values |
|---|---|---|
| `review.design-audit.slicing` | **orthogonal** | scenario, step, lens |
| `review.design-audit.runs` | **2** | 1, 3 |
| `review.design-audit.seed` | **reverted-escapes** | synthetic, none |
| `review.design-audit.cell-refute` | **sampled** | all, none |
| `review.design-audit.gate` | **no-critical** | no-high, recorded |

Effort stays the owner's existing setting (NT-12), so no key is proposed for it.

**Where the records and the code disagree:**
- The role matrix's record says 81 items; flow-steps has 90 today.
- The line-coverage instrument exits on the shape audits' `Subjects (round 1):` header.
- The review-shape line in shape audit A says 11 agents and 260.6k output tokens; its comparison says 12 and 291.7k, summed over returned lines including the resume probe.

**For the other researchers, one line each:**
- Question 2: the coverage table is a ready input for checking the design is specced as planned.
- Question 3: the K5 "enforced by" join is the natural anchor for a deviation log.
- Question 4: help sits under P12, P17 and P25, which no finding has ever named.
- Question 5: the design map and atlas generators are the seams.

**Files:**
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-state.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-review-system.md
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/workflows/tier2-review.js
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/workflows/review_replay.py

Sources:
- [SEI, Risk Themes Discovered Through Architecture Evaluations](https://sei.cmu.edu/library/risk-themes-discovered-through-architecture-evaluations/)
- [Porter, scenario-based inspections](https://www.cs.umd.edu/~aporter/html/scenarios.html)
- [Porter, Votta and Basili 1995, UMD record](https://drum.lib.umd.edu/items/96204769-6905-4196-b903-709ad81148ee/full)
- [Fagan 1976, IEEE Xplore](https://ieeexplore.ieee.org/document/5388086)
- [arXiv 2005.09217](https://arxiv.org/pdf/2005.09217)
- [Briand et al., capture-recapture evaluation](https://pure.ul.ie/en/publications/a-comprehensive-evaluation-of-capture-recapture-models-for-estima/)
- [ISERN-98-11](https://ehealthinformation.ca/web/default/files/wp-files/isern-98-11.pdf)
- [arXiv 1009.2785, Mills seeding](https://arxiv.org/pdf/1009.2785)
- [NASA NTRS 20040086890](https://ntrs.nasa.gov/citations/20040086890)
- [PHF, Pre-Mortem Analysis](https://archive.phf.org/resourcestools/Documents/Pre_Mortem_Analysis.pdf)
- [Jason Collins, The premortem](https://corporate.jasoncollins.blog/premortem)
- [arXiv 2208.01524, STRIDE replication](https://arxiv.org/pdf/2208.01524)
- [arXiv 1910.03422](https://arxiv.org/pdf/1910.03422)
- [UK MOD Red Teaming Handbook](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1027158/20210625-Red_Teaming_Handbook.pdf)
- [Amazon Science, How AWS uses formal methods](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods)
- [the morning paper, Use of Formal Methods at AWS](https://blog.acolyer.org/2014/11/24/use-of-formal-methods-at-amazon-web-services/)
- [Heitmeyer, Jeffords and Labaw 1996](https://apps.dtic.mil/sti/tr/pdf/ADA465574.pdf)
- [arXiv 2608.09290, OpenCodeReview](https://arxiv.org/pdf/2608.09290)
- [arXiv 2408.10886](https://arxiv.org/pdf/2408.10886)
