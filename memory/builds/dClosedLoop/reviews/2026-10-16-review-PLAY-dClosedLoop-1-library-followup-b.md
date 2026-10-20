**Serves:** diff-review PLAY-dClosedLoop-1

# Tier-2 review — dClosedLoop library round, round 2 (follow-up, run B)

Range reviewed: d4fc4bb51d56c315afea4f3fdf18ea86f947c020...0dd96272468fb2487d51f362266f0ef46185859b (commit 0dd962724, the fold of round 1's library review). Round: 2.

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs: 14 medium items and 4 low items, covering 22 confirmed findings (18 medium, 4 low).
Every finding is a defect in design text that a chain build would implement, so none of them ships behaviour yet.
Each finding was checked against the file at the worktree's later HEAD, and the cited lines are HEAD's lines.
This is a light-intensity run, so it is not a full review. The security and intent lenses did not run.

## Review shape

Review shape: intensity light, raw 23, confirmed 22, refuted 1, unverified 0 (0 uncertain), precision 0.96.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| seams | yes | 10 | 9 | 1 | 0 | 0 | 0.90 |
| verification | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |

Tally by item: 0 blocker, 0 high, 14 medium, 4 low (18 items).
Tally by raw confirmed finding: 0 blocker, 0 high, 18 medium, 4 low (22 findings).

The skeptics refuted one finding (id 16, the placement of a gotcha claim in row-grammar.md). gotchas.py selects a class by the record's own anchors, not by a dossier's claims, so that placement has no effect on selection.

Run integrity:
- Lenses: 3 of 3 returned, 0 died.
- Skeptic batches: 5 of 5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 22 judged sound, 0 judged unsound, 0 with no fix proposed, 0 not judged.
- Severity: 0 confirmed findings ungraded by the skeptic, 2 re-graded by the skeptic (ids 8 and 9, both from high to medium).
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-diff-reviewer, the skeptic batches were gov-skeptic, and the synthesis was gov-synthesizer.
- Intensity: light. The security and intent lenses were not run, so their classes were covered only through the checklist items shared out to the three lenses that did run. This run is not a full review.
- Intent: 8 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 21 items, each assigned to exactly one lens (correctness 7, seams 7, verification 7).
- By design: the caller's byDesign.

All abbreviated paths below are under `memory/builds/dClosedLoop/build/`. `flow-steps` is `2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`, `layer-memory` is `2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`, and `layer-library` is `2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`.

## Medium

### M1. The owner's ratification is placed in two places that disagree (ids 1, 11)

- **What and where:** This applies under `decisions.major: author-owner-ratifies`. Build's Breakpoints (flow-steps:240-241) put the owner's ratification "before `build.distill`". But `build.distill`'s Needs is only `build.core` (flow-steps:213), and `build.core`'s clean arm routes straight to `build.distill` (:212). The ratification appears only in `build.distill`'s Then column, which holds the routes taken after the item has run: "the owner's ratification comes first, an owner item: ratified → the row; rejected → the fork re-classed as not major".
- **Consequence:** A position engine that derives the next item from Needs runs the append first. A fork the owner later rejects then has a row in the append-only log, and that row can only be superseded, never removed. The one-to-one join between major forks and rows goes red, and no route leads out of it.
- **Fix (judged sound by the skeptic):** Declare the ratification as an owner item, for example `build.ratify`, between `build.core` and `build.distill`.
  - Under `author-owner-ratifies`, `build.distill`'s Needs gains that item, and `build.core`'s clean arm routes to it.
  - `build.distill` appends only ratified rows.
  - Remove the ratification arm from `build.distill`'s Then column, which keeps only the `build.exit` route.
- **Probe:** Walk the strict preset through Build's table and confirm that no row is appended before the ratification's disposition record exists.
- **Left-shift gate:** A route-graph check that fails when a Breakpoints line names an item ordering that the Needs and routes do not encode.

### M2. A fork's class has no checked producer, and the red at `build.distill` has no route (ids 2, 12)

- **What and where:** Design's Memory line (flow-steps:176-177) now says Design writes each resolved fork with its declared class. No Design witness requires that class:
  - `design.decompose` is proven by "the roster and interface schema check" (:157).
  - `design.unit-spec` is proven by "every raised fork joined to its resolution" (:162).

  Forks met during Build (`build.unit-pass`, "fork → as `design.forks` says", :208) have no class writer in Build's Memory clause (:231-233). `build.distill`'s witness (:213) is red on "a fork with no class", but its Then column has no red arm.
- **Consequence:** A fork recorded without a class passes all of Design and all of Build. It is first caught at Build's last item, by a command that cannot supply the class, because only the author's declaration can. The frontier fallback in [rules] (:29) returns `build.distill` itself, so the build stalls.
- **Fix (judged sound by the skeptic):**
  - Add "each resolved fork carries its declared class" to the witnesses of `design.decompose` and `design.unit-spec`.
  - Name the writer of a Build-time fork's record in Build's Memory clause.
  - Give `build.distill` a red route: a fork with no class goes back to the role that resolved it, bounded by `flow.route-backs`.
- **Left-shift gate:** A check that every witness red outcome has a declared route arm. This finding falls in the class `rule-stated-with-no-check-that-fails`.

### M3. After the fold, `deploy.distill` only confirms the rows, and its red has no route (id 21)

- **What and where:** `deploy.distill` (flow-steps:330) now only confirms that the rows are at the landed SHA, and its only route is → `deploy.recommend`. It runs after `deploy.land`, so nothing after it can append a missing row. Deploy's Exits still require those rows at the landed SHA.

  This finding also restates the unrouted unclassed-fork red at `build.distill`. That half is the defect in M2.
- **Consequence:** If a row is lost between Build and landing, for example when `test.merge` resolves an append conflict on `memory/DECISIONS.md` by dropping a row, Deploy has no next item after the push. The frontier fallback returns this same command, and it goes red again.
- **Fix (judged sound by the skeptic):**
  - Route `deploy.distill`'s red to a repair: a patch build, or an owner item that appends the missing rows on the default branch, keyed by build and fork so the append stays idempotent.
  - Route `build.distill`'s unclassed-fork red back to the role that resolved the fork, bounded by `flow.route-backs`.
- **Left-shift gate:** The same red-arm route check as in M2. It covers items placed after `deploy.land`.

### M4. Round 1's typed-witness finding on `build.unit-pass` is fixed only in part (ids 3, 22)

- **What and where:** flow-steps:208's Proven-by column still reads "Each unit `reuse.propose` selects carries its reuse line, `proposed <tag>` or `none` with its reason". That line is the builder's own return, and [rules] (:23-24) says "No witness is typed by the acting agent".

  layer-library [review-fold] marks round 1's id 30 as fixed. But M7 (:371) changed only which units owe the line, and M8 (:372) changed only the trigger's phrasing.
- **Consequence:** A bare `none` with any reason passes under every `reuse.propose` value. The reuse-entry path (gap-mem-03) still rests on an assertion. Two texts now disagree: [rules] forbids agent-typed witnesses, and this item's witness is one.
- **Fix (judged sound by the skeptic):** Keep the line in the builder's return, and compute the witness instead.
  - For `proposed <tag>`, join the line to the filed instruction-command proposal record that carries that tag.
  - For `none`, join the line to something the agent does not type: the spec's reuse-audit token (gap-design-05), or a reason graded by the executor, a reviewer or the owner.
  - State in [review-fold] how id 30's typed-witness half is handled.
- **Probe:** A unit that returns `none` with an empty reason must turn the witness red.
- **Left-shift gate:** A check that fails when a "Proven by" cell names a builder's or actor's return as its evidence.

### M5. The `owner-asks` value now carries two meanings, and its population has no producer (id 4)

- **What and where:** The M7 fix (layer-library:207, and the same text at flow-steps:208) says that under `owner-asks`, "a unit building a feature an owner-filed reuse ask names" owes a reuse line. LB-2 offered the owner that value as "no line is owed, and the owner names the features to enter" (layer-library:84). The velocity preset selects this value (v2:797).
- **Consequence:** One value returns two verdicts. No item and no ask schema declares a "reuse ask", so the population the new text selects has no writer.
- **Fix (judged sound by the skeptic):** Choose one of these.
  - Use the definition as offered: under `owner-asks` no line is owed, and the owner's named features enter through the instruction command.
  - Or define the reuse-ask kind and its writer in the memory contract, and record the narrowed meaning as a dated note under LB-2.
- **Left-shift gate:** A check that every population a policy value selects names a producing item or kind. This finding falls in the class `amendment-leaves-its-other-half-standing`.

### M6. The decision-log contract in layer-memory still names the old writer and timing (ids 5, 13)

- **What and where:** layer-memory:534-535 still reads "`deploy.distill` appends the build's major decisions to the log when it lands (layer-library `[log]`)". The fold moved the append to `build.distill`, in the build's branch before Test, and left `deploy.distill` only confirming the rows (flow-steps:213, :330; layer-library:172, :216-224). The same commit edited layer-memory's kinds list (:364-374) and left this clause unchanged.
- **Consequence:** The record that owns the decision log's contract contradicts the record it cites. dTotalRecall reads layer-memory and would implement a post-landing append, which is an unlanded write to the default branch. That is the M6 defect the fold fixed elsewhere.
- **Fix (judged sound by the skeptic):** Re-word :534-535 to say:
  - `build.distill` appends each major fork's row in the build's branch before Test, keyed by build and fork.
  - `deploy.distill` confirms the rows at the landed SHA.
  - Cite layer-library `[log]` as amended by `[review-fold]`.
- **Left-shift gate:** When a fold moves a writer, grep the fold's records for the old writer's name and the fact's anchor. This finding falls in the class `amendment-leaves-its-other-half-standing`.

### M7. The decision log's idempotence key has no fork field (id 8)

The finder graded this high. The skeptic re-graded it medium because it is a design-text defect owed to a chain build, not shipped behaviour.

- **What and where:** `build.distill` skips "a row already present, keyed by build and fork" and is red on "a second row for one key" (flow-steps:213). layer-library [log] repeats the key. Every statement of the row shape has no fork field: flow-steps:213, layer-library:216-219 and layer-memory:526-532 all list only date, build, decision, a pointer to the rationale and the reuse entry.
- **Consequence:** The skip test and the duplicate red cannot be computed from the log. A retried run that rewords a row appends a duplicate, and the witness stays green, which is the defect M5 meant to close. dTotalRecall would build the row grammar without a key column.
- **Fix (judged sound by the skeptic):**
  - Add the fork's id, or the fork record's path#anchor, as a declared row field in all three shape lists, in one commit.
  - State that the join keys on (build, fork-id).
- **Probe:** A fixture log with one row duplicated under reworded prose must turn the witness red.
- **Left-shift gate:** A check that every key an idempotence clause names is a declared column of the row shape. The fold's own gotcha `append-without-an-idempotence-key` covers this class.

### M8. The planned move of recall's code into memory-tree names two functions, but check 27 imports eight names (id 9)

The finder graded this high. The skeptic re-graded it medium because it is design text, and the chain build's own probe would surface the failure.

- **What and where:** Two passages say only "two functions" move:
  - v2:280: "dTotalRecall moves recall's two core-read functions into memory-tree".
  - v2:946: dTotalRecall's unit, "check 27's near-match index builder and the supersession map".

  The [consult] row at layer-library:312 is phrased by capability. It is less wrong, but it is still incomplete. In the tree, check 27 imports eight names from the recall kit:
  - `tools/memory-tree/row_grammar.py:1029` requires bench's `build_index`, `match_expr`, `terms` and `ALIAS_WEIGHT`.
  - `tools/memory-tree/row_grammar.py:1055` requires extract's `corpus_inputs`, `extract_records`, `extract_supersessions` and `derive_supersession_map`.
  - `tools/memory-tree/row_grammar.py:1018` refuses check 27 when the recall kit is absent.
- **Consequence:** After the move as planned, the core check still imports six names from the optional recall kit, against [consult]'s "no fallback is owed". dOrderedCharter's check that core never depends on an optional component would go red on dTotalRecall's own output.
- **Fix (judged sound by the skeptic):** Choose one of these, in [consult]:312, the v2:280 note and dTotalRecall's planned unit.
  - Name all eight symbols.
  - Or state that the whole of bench's index and match surface and extract's corpus-walk, record-extraction and supersession path move.
- **Left-shift gate:** When design text describes the tree's imports, require the cited symbol list to be generated from the source, for example by a grep of the `require` calls, rather than paraphrased.

### M9. Build's policy list omits `run.on-owner-question`, although its route reads that key (id 10)

- **What and where:** `build.distill`'s route ends "held → as `run.on-owner-question` says" (flow-steps:213). Build's Instruction policy list (:229) gained `decisions.major` but not `run.on-owner-question`. Plan, Deploy and Review all list that key.
- **Consequence:** The work order loads "the policy values the item reads" ([rules] :41-42) from this list. Under `author-owner-ratifies`, the held branch has no loaded value to route by. This brings back the gap-flow-15 class: a step's policy list disagrees with the keys its routes read.
- **Fix (judged sound by the skeptic):** Add `run.on-owner-question` to Build's Instruction policy list at flow-steps:229.
- **Left-shift gate:** A check that every policy key named in a step's routes appears in that step's policy list.

### M10. The class-record acceptance for an ask is not in layer-memory's closed set of ask forms (id 14)

- **What and where:** The M3 fix adds "the ask is accepted once the class record exists" (layer-library:193, and `review.dispose` in flow-steps). layer-memory [asks] (:457-474) is the whole set of core filers' forms, and it says "a new core ask kind adds its form here first". Its form for this ask is "its unit is built, or a review round rules it out", with no class-record arm. [rules] (flow-steps:38-39) says these forms are cited from [asks], never copied.
- **Consequence:** One ask has two acceptance statements. Under the catalogued form, a ruling-out closes the ask while the `new:` class record is never written. A filing check built from [asks] would refuse the new form.
- **Fix (judged sound by the skeptic):**
  - Amend [asks]'s sub-threshold-finding form to add "and, where it carries a `new:` slug, the class record exists with `from:` this review and finding".
  - Cite that form from `review.dispose` instead of restating it.
- **Left-shift gate:** A check that every acceptance phrase outside layer-memory [asks] resolves to a form in [asks].

### M11. Plan's new memory read selects by scope tags that no source record carries (id 15)

- **What and where:** The L1 fix has Plan read "the research view and the decision log by the plan's scope tags" (flow-steps:125-126). Scope tags exist only on instruction units (layer-instruction:388, :409-412). The research view lists returns "by build, date and question" (layer-library:230, layer-memory:718). A decision row holds date, build, decision, a rationale pointer and the reuse entry (layer-memory:526-532).
- **Consequence:** The selector has no key column in either source, so the planner's core source loads everything or nothing.
- **Fix (judged sound by the skeptic):** Choose one of these.
  - Add scope tags as a declared field of the decision row and of the research-return kind, written by `build.distill`, `plan.research` and `design.research`, and list them among the view's columns.
  - Or drop "by the plan's scope tags" and state the real selector.
- **Left-shift gate:** A check that every "by <field>" selector in a Memory read names a declared field of the population it reads.
- **Related:** Low item L2 (id 7) reports the same defect at the same lines and is bound low.

### M12. The research-return kind's witness either cannot go red or goes red on the default branch (id 18)

- **What and where:** The M13 fix gives research returns their own kind, written only by `plan.research` and `design.research`. Its witness is "the kind's check, seen red on a planted design record bound as research" (layer-library:227-233). No record in today's tree carries the kind. No item backfills the 59 existing returns: v2:946 names a migration for the decision rows but none for this kind.
- **Consequence:** The outcome depends on what the check reads.
  - If it reads the declared kind, the planted record is simply not that kind, so nothing fails. The view also renders empty for all 59 returns, and the byte comparison passes the empty render.
  - If it reads the `**Serves:** research` binding, it goes red on the more than 200 non-research records that carry the binding today. `grep -rlE '^\*\*Serves:\*\* research' memory` found 270-274 files, only 65 of them research-named.
- **Fix (judged sound by the skeptic):**
  - State the kind's discriminator. It must be a field or a path shape.
  - Either owe a dated backfill of the 59 existing returns in dTotalRecall's planned units, naming them as its population, or have the check read the discriminator while the existing non-research bindings are re-bound or listed.
  - Require the view to render at least the 59 backfilled returns, so an empty render fails.
- **Left-shift gate:** A check that every new kind with existing instances in the tree has a backfill unit and a minimum render population. This finding falls in the class `two-answers-to-one-question`.

### M13. On the built path, nothing checks that a fix unit's owed class record was written (id 19)

- **What and where:** `build.unit-pass`'s witness (flow-steps:208) requires only that a fix unit carry its owed class records "in its write set". `build.scope` (:210) refuses paths outside the write set but never checks that declared paths were written. `review.dispose` (:429) joins each `new:` slug only to "the item or ask that owes its record".

  The other paths are checked: the unbuilt path joins the slug to the record and its `from:` at `review.fold` (:430), and the ask path waits for the record to exist.
- **Consequence:** A fix unit that declares `memory/gotchas/<slug>.md` but never writes it passes Build and Deploy. The `new:` class never lands, and the left-shift M3 meant to close stays open for every finding that becomes a built unit.
- **Fix (judged sound by the skeptic):** Add a computed join to the witness of the fix unit's last pass, or to `build.core`. Each `new:` slug the unit owes must resolve to a record under `memory/gotchas/` at the unit's commit, and that record's `from:` must name the review and finding.
- **Probe:** Plant a fix unit that omits the record and observe the join turn red.
- **Left-shift gate:** A symmetry check that every path producing a `new:` class ends in the same record-and-`from:` join.

### M14. The `owner-only` rule has no witness arm that can fail (id 20)

- **What and where:** `build.distill` says "Under `owner-only`, only a fork the owner resolved may be major" (flow-steps:213). Its witness checks only that each fork has a class and that each key has one row. A fork record carries only "its decision and its declared class" (:174-176), with no field naming who resolved it.
- **Consequence:** Under `decisions.major: owner-only`, an agent-resolved fork classed major gets a row, and the witness stays green. That is exactly what the value exists to prevent.
- **Fix (judged sound by the skeptic):**
  - Add the resolver (a role or the owner) to the fork record's schema in Design's Memory line.
  - Add a witness arm under `owner-only`: a major row whose fork the owner did not resolve is red.
- **Probe:** Plant an agent-resolved major fork and observe the arm fail.
- **Left-shift gate:** A check that every policy value's distinct behaviour has a witness arm that reads it. The fold filed this class as `policy-value-with-no-route`.

## Low

### L1. The ratification's ordering is ambiguous, and no writer is named for the re-class on rejection (id 23)

- **What and where:** This is the same placement conflict as M1, at flow-steps:240-241 and :213. This finding adds one point: neither placement names who writes the fork's re-class when the owner rejects.
- **Grade:** It is bound low. The synthesizer judges that it is part of M1's medium defect, but the binding grade stands.
- **Fix (judged sound by the skeptic):**
  - State the ratification once, either in `build.distill`'s Needs under `author-owner-ratifies` or as its route.
  - Name the writer of a rejected fork's re-class: the command, acting on the owner item's verdict. The one-to-one join then reads the updated class.
- **Left-shift gate:** As in M1. This finding falls in the class `two-answers-to-one-question`.

### L2. Plan's scope-tag read has no key in its sources (id 7)

- **What and where:** This is the same defect as M11, at flow-steps:126 and the [consult] row at :305.
- **Grade:** It is bound low because its effect is limited to a fallback read.
- **Fix (judged sound by the skeptic):** Choose one of these.
  - Add scope tags to the research-return kind's schema and to the decision row, written by `plan.research`, `design.research` and `build.distill`.
  - Or select by a field those records already carry, and use the same wording in the flow-steps :126 line and the [consult] :305 row.
- **Left-shift gate:** As in M11.

### L3. A missing row at the landed SHA strands `deploy.distill` (id 6)

- **What and where:** This is the same defect as M3. `deploy.distill` (flow-steps:330) confirms only, its sole route is → `deploy.recommend`, and Deploy's Exits require the rows.
- **Grade:** It is bound low because the path is narrow: a row lost in the merge, or a fork re-classed after `build.distill`.
- **Fix (judged sound by the skeptic):** Add a red arm: rows missing at the landed SHA lead to a patch build through the entry-point table's post-close row, as `deploy.core`'s red arm does, or to an owner item.
- **Left-shift gate:** As in M3. This finding falls in the class `route-names-an-output-its-actor-never-emits`.

### L4. The fix unit's write set omits the claiming dossier (id 17)

- **What and where:** flow-steps:208 puts only the owed class records in the fix unit's write set. layer-library:194-195 also requires that, where the map is installed, the guarded feature's dossier claims the new class. That claim is an edit under `memory/map/features/`, outside the write set.
- **Consequence:** On a tree with the map installed, the claim is a stray at `build.scope`, which warns, reports or refuses it depending on policy. The builder may skip the claim instead.
- **Fix (judged sound by the skeptic):** Add "and, where the map is installed, the claiming dossier" to the fix unit's write set, in `build.unit-pass`'s witness and in layer-library [left-shift].
- **Left-shift gate:** A check that every edit a unit's Does clause requires falls inside the write set its witness declares.

review-shape kind=diff-review round=2 intensity=light at=synth raw=23 confirmed=22 refuted=1 unverified=0 blocker=0 high=0 medium=18 low=4 agents=9 out-tokens=100141

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | This text was added by 0dd962724 and HEAD still carries it. Build's Breakpoints (flow-steps:240-241) place the owner's ratification 'before `build.distill`'. But at :213, build.distill's Needs is only `build.core`, and build.core's clean arm (:212) routes straight to `build.distill`. The ratification appears only in build.distill's Then column ('the owner's ratification comes first, an owner item: ratified → the row'), so no Needs entry or route puts it ahead of the append. The closing review, by contrast, is named in build.core's Needs. The same fact is stated two ways, and a Needs-derived frontier would run the append first. The effect is contained to the strict preset, which design-only text does not yet execute. | sound | route-names-an-output-its-actor-never-emits |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | Design's Memory line (:176-177), added by this diff, says Design writes each resolved fork with its declared class. Yet design.decompose's witness is 'the roster and interface schema check' (:157) and design.unit-spec's is 'every raised fork joined to its resolution' (:162), so neither requires the class. build.distill's witness (:213) is red on 'a fork with no class', but its Then column routes only to build.exit and the ratification outcomes. [rules] (:28) says every outcome routes, so this red has no declared route, and the only fallback is the frontier, which returns build.distill itself. The gap is caught only after Build has finished, by a command that cannot supply the class. | sound | - |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:208 | medium | medium | confirmed | Round 1's id 30 had two halves: the typed-witness half and the trigger phrasing. layer-library [review-fold] M8 (:372) marks it 'fixed, gap' and addresses only the trigger (one token, gap-design-05); M7 (:371) changed only the population. At HEAD, flow-steps:208's 'Proven by' still makes the builder's own return ('carries its reuse line, `proposed <tag>` or `none` with its reason') part of the witness. That contradicts [rules] :23-24 ('No witness is typed by the acting agent'), and a bare `none` still cannot turn it red. The round-1 finding is left standing in part while its disposition says fixed. | sound | - |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:207 | medium | medium | confirmed | The base had no 'reuse ask' text; 0dd962724 added the owner-asks arm at layer-library:207 and flow-steps:208 ('a unit building a feature an owner-filed reuse ask names' owes the line). LB-2 offered the owner that value as 'Only when you ask: no line is owed, and the owner names the features to enter' (layer-library:84). v2:797 makes owner-asks the velocity preset's value, so one value now carries two meanings. A grep of the build's records finds no producer or kind for an 'owner-filed reuse ask' outside these two lines, so the population has no writer. | sound | amendment-leaves-its-other-half-standing |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:534 | medium | medium | confirmed | At HEAD, layer-memory:534-535 still says `deploy.distill` 'appends the build's major decisions to the log when it lands'. The text is unchanged from base (:530). The M6 fold in this diff moved the append to build.distill in the build's branch before Test, and made deploy.distill only confirm the rows (flow-steps:213 and :330, layer-library [log] :216-224). The fix therefore left the memory contract stating the decision log's writer and timing differently from the flow, and the same commit edited this file's kinds list (:364-374) without touching this clause. It is contract body text rather than a dated revision note, so the dated-records exemption does not cover it. | sound | amendment-leaves-its-other-half-standing |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:330 | low | low | confirmed | At HEAD, flow-steps:318 makes `deploy.distill` a confirm-only command whose witness is 'the rows at the landed SHA, joined one to one to the build's major forks'. Its only route is '→ `deploy.recommend`'. Deploy's Exits (:301) require 'its major decisions' rows are in the decision log at the landed SHA'. The fold introduced this: at base, :313 had the item write the rows itself. Nothing after `deploy.land` writes and lands a row. A red witness falls to the [rules] :29 default ('next returns the frontier'), and that returns this same unwitnessable item again. The path is narrow (a row dropped in the merge, or a fork re-classed after `build.distill`), so the grade is low. | sound | route-names-an-output-its-actor-never-emits |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:126 | low | low | confirmed | The fold added flow-steps:125-126 at HEAD: 'the research view and the decision log by the plan's scope tags'. In the design, scope tags exist only on instruction units (layer-instruction R-A :388, R-B :409, where selectors decide who loads a unit). The research view lists returns 'by build, date and question' (layer-library :230). The decision row is date, build, decision, rationale pointer and reuse entry (flow-steps :213, layer-library [log], layer-memory :527-532). So the new Memory read selects on a key that no record carries. The [consult] :305 row already had this wording at base (:291), but the flow-steps read is the fold's own addition, made as round 1's fix. The effect is contained to a fallback read, so the grade is low. | sound | - |
| 8 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | high | medium | confirmed | At HEAD, flow-steps:213 says 'A row already present, keyed by build and fork, is skipped', and 'a second row for one key, is red'. layer-library [log] repeats 'a row keyed by build and fork is never written twice'. Yet every row-shape list (flow-steps :213, layer-library [log], layer-memory :527-532) carries date, build, decision, a pointer to its rationale and the reuse entry, and no fork field. The key is not a declared column. The fold's own gotcha (append-without-an-idempotence-key) asks to 'Declare the key that makes a row unique'. The rationale pointer may happen to resolve to the fork record, but nothing declares it as the key, and dTotalRecall would build the grammar from layer-memory's shape. This is a design text defect owed to a chain build, not shipped behaviour, so medium rather than high. | sound | - |
| 9 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:312 | high | medium | confirmed | The fold added two passages at HEAD: v2:280 ('dTotalRecall moves recall's two core-read functions into memory-tree') and v2:946's dTotalRecall unit ('check 27's near-match index builder and the supersession map moved into memory-tree'). Both are wrong about the tree. tools/memory-tree/row_grammar.py:1029 requires bench's build_index, match_expr, terms and ALIAS_WEIGHT, and it uses match_expr, ALIAS_WEIGHT and terms at :1271, :1299 and :1413. :1055 requires extract's corpus_inputs, extract_records, extract_supersessions and derive_supersession_map. :1018 refuses check 27 when the recall kit is absent. A move scoped to 'two functions' leaves the core check importing the optional kit, against [consult]'s 'no fallback is owed'. The [consult] row at :312 is phrased by capability and is less wrong, but the v2 copies will mislead dTotalRecall. Severity is medium because it is design text, and the chain build's own probe would surface the failure. | sound | - |
| 10 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:229 | medium | medium | confirmed | At HEAD, `build.distill`'s route (flow-steps:213) ends 'held → as `run.on-owner-question` says'. Build's Instruction policy list at :229 lists `decisions.major` but not `run.on-owner-question`. Plan (:123), Deploy and Review all carry it. At base the Build list (:224) had neither key, and the fold added the held branch and `decisions.major` only. [rules] :41-42 loads 'the policy values the item reads' into the work order, so the held route reads a value that Build's declared list omits. The fold introduced this, and its effect is contained. | sound | - |
| 11 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:240 | medium | medium | confirmed | At HEAD, flow-steps:213 has `build.distill`'s Does append 'a row for each of its resolved forks whose class is major'. Its Then column then says 'under `author-owner-ratifies`, the owner's ratification comes first, an owner item: ratified → the row; rejected → the fork re-classed as not major, kept in the build's records only'. Build's Breakpoints (:240) instead place the ratification 'before `build.distill`'. In this table, Then holds the post-item routes, and `review.report` uses the same 'owner item first' pattern after its actor has acted. So the rows are already appended when a rejection arrives, which contradicts both 'ratified → the row' and the Breakpoints placement. `build.distill` is new in this diff (the base had only `deploy.distill`), so the diff introduced the defect. | sound | - |
| 12 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:176 | medium | medium | confirmed | This diff added the class requirement: `build.distill`'s witness (:213) is red on 'a fork with no class', and Design's Memory clause (:176-177) now says Design writes 'each resolved fork with its decision and its declared class'. `design.unit-spec`'s witness (:162) is still only 'every raised fork joined to its resolution', and `design.decompose`'s is 'the roster and interface schema check', so neither item is held to produce the class. `build.unit-pass` routes 'fork → as `design.forks` says' (:208), and Build's Memory clause (:231-233) names no writer for a fork's record or its class. `build.distill`'s Then column has no red arm. By [rules] (:29), a refusal returns the frontier, which is `build.distill` itself, a command that cannot write a class. A missing class is therefore first caught at Build's exit, with no route back to the role that resolved the fork. | sound | rule-stated-with-no-check-that-fails |
| 13 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:534 | medium | medium | confirmed | At HEAD, layer-memory:534-535 still reads '`deploy.distill` appends the build's major decisions to the log when it lands (layer-library `[log]`)'. The layer-library record it cites now says the opposite: :172 puts the append at 'Build: `build.distill`, before `build.exit`; Deploy's `deploy.distill` confirms the rows at the landed SHA', and :216 and :272-273 agree. The line was accurate at the base, and this diff moved the writer while editing the same layer-memory record (:364-368) without touching :534. So the fold left one fact stated two ways, in the record that owns the decision log's contract. | sound | - |
| 14 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:193 | medium | medium | confirmed | This diff introduced 'the ask is accepted once the class record exists' (layer-library:193 and flow-steps `review.dispose`; absent at the base). layer-memory [asks] (:457-474) is the core filers' 'whole set' of forms, and 'a new core ask kind adds its form here first'. Its form for this ask is 'a confirmed finding filed below `review.findings`' threshold: its unit is built, or a review round rules it out', and it has no class-record arm. [rules] (flow-steps:38-39) says the forms are 'cited from there, never copied'. The new acceptance is therefore an uncatalogued form that contradicts the catalogued one: under the catalogued form, the ask closes on a ruling-out without the `new:` class ever being written. | sound | - |
| 15 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:125 | medium | medium | confirmed | This diff wrote the selector into flow-steps:125-126, where Plan's Memory clause reads 'the research view and the decision log by the plan's scope tags'. The phrase pre-existed only in layer-library's [consult] table (base :291); here the flow step itself now uses it. Scope tags are defined only for instruction units, as R-A's unit-row field and as selector namespaces (layer-instruction:388, :409-412). A decision row carries date, build, decision, rationale pointer and reuse entry (layer-memory:526-532). The research view lists returns 'by build, date and question' (layer-library:230, layer-memory:718). Neither source carries a scope-tag field, so the selector has no key to match. | sound | - |
| 16 | seams | memory/map/features/row-grammar.md:18 | low | - | refuted | The claimed consequence does not happen. gotchas.py does not select a class through a dossier's claims. It selects through the record's own anchors (selectable() at tools/memory-tree/gotchas.py:340, substring match both ways). The class record names `tools/memory-tree/` as an anchor. Running `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/corpus_ids.py` selects `append-without-an-idempotence-key (directory)`. So the class does reach reviewers of the real appenders, and putting the claim in row-grammar.md has no effect on selection. That leaves a cosmetic placement question, which a low grade cannot carry. | sound | - |
| 17 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:208 | low | low | confirmed | At HEAD, flow-steps:208 lists the fix unit's write set as only 'the class records its findings' `new:` dispositions owe'. layer-library:194-195 (already at the base, :191) requires that, where the map is installed, the guarded feature's dossier claims the new class. That claim edits memory/map/features/, which the write set leaves out, and build.scope (:210) treats a path outside the write set as a stray: warned, reported or refused. This fold added the write-set clause, so the defect is new in this diff. The fix is partial: on a map-installed tree the builder must either stray or skip the claim. The default handling only warns, so the effect is contained. | sound | - |
| 18 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:233 | medium | medium | confirmed | At HEAD, layer-library:227-232 gives research returns their own kind, written only by plan.research and design.research. Its witness is 'the kind's check, seen red on a planted design record bound as research'. :151 itself counts 179 non-research records carrying the binding. `grep -rlE '^\*\*Serves:\*\* research' memory` printed 274 files today, only 65 of them research-named. No item backfills the kind onto the 59 existing returns: v2:946's dTotalRecall row says only 'the research view, over the research-return kind'. By contrast, the same row does name a migration for the 200 decision rows. No item re-binds or lists the existing non-research bindings either. So a check that reads the binding goes red on the tree, and a check that reads the new kind renders the existing returns as an empty view, which still passes the byte comparison. This fold introduced the defect (the M13 fix). | sound | two-answers-to-one-question |
| 19 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:208 | medium | medium | confirmed | At HEAD, build.unit-pass's witness (flow-steps:208) requires only that a fix unit carry the class records 'in its write set'. build.scope (:210) checks paths against the write set in one direction only, and it refuses strays. review.dispose's witness (:429) joins each `new:` slug only to 'the item or ask that owes its record'. The ask path is gated: 'the ask is accepted once the class record exists'. The unbuilt path joins the slug to the record and its `from:` at review.fold (:430). No built-path item checks that the record exists, so the two paths are checked unequally, and this fold introduced that asymmetry. | sound | - |
| 20 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | This fold added the sentence 'Under `owner-only`, only a fork the owner resolved may be major' at flow-steps:213; the base flow-steps contains no 'owner-only'. build.distill's witness checks only that each fork has a declared class and that each key has one row. Design's Memory line (:174-176) gives a fork record only 'its decision and its declared class', with no field naming who resolved it, and grep finds no resolver field in the layer records. So the owner-only rule has no check that can fail. The value is in v2's catalogue (:605) and is not the default, so the effect is contained. | sound | - |
| 21 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:330 | medium | medium | confirmed | At HEAD, flow-steps :330 `deploy.distill` only confirms the rows at the landed SHA, and its sole Then is `deploy.recommend`. Under the base (d4fc4bb51 :313) it was the writer, so the fold introduced a confirm-only item that runs after `deploy.land` with no arm for its red. Nothing after the push can append a missing row: `build.distill` (:213) is in Build. Deploy's Exit (:315) still requires the rows at the landed SHA. By [rules] :28-30 a refusal returns the frontier, and here the frontier is `deploy.distill` itself, which re-reds. `build.distill`'s red for 'a fork with no class' (:213) likewise has no route arm. Design's Memory clause (:176) says the class is written, but no Design witness checks it, and nothing routes back to declare it. Both reds are reachable, for example through a lost append in `test.merge`, and both stall. The effect is contained to one build's close, so the grade is medium. | sound | - |
| 22 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:208 | medium | medium | confirmed | At HEAD, the Proven-by column of flow-steps :208 still reads 'Each unit `reuse.propose` selects carries its reuse line, `proposed <tag>` or `none` with its reason'. That is the builder's own typed return, against [rules] :24 'No witness is typed by the acting agent', and nothing can fail the `none` arm. The layer-library [review-fold] rows M7 (:371) and M8 (:372) changed only the population and the audit token. Round 1's typed-witness complaint (item 30) is mapped to M8, which does not address it. The fix is therefore partial, and the partial fix is in this diff's scope. The effect is limited to the reuse-entry path. | sound | - |
| 23 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:240 | low | low | confirmed | At HEAD, Build's Breakpoints (:240-241) place the owner's ratification 'before `build.distill`', but `build.distill`'s Needs (:213) list only `build.core`. Its Then column instead makes the ratification an inner outcome: 'the owner's ratification comes first, an owner item: ratified → the row; rejected → the fork re-classed as not major'. Neither spot names who writes the re-class on a rejection. Both texts came in with the fold (M2, layer-library :366). The ordering is ambiguous, which is a documentation inconsistency in a design record with a contained effect, so low. | sound | two-answers-to-one-question |
