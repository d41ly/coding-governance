**Serves:** diff-review PLAY-dClosedLoop-1

# Review: dClosedLoop's away pass, closing review (round 1)

Tier-2 diff review of everything design-bearing since the night pass's closing review: the night pass's folded answers, the walk's four waves, the map's new arms and the away pass. It was run by the gov-diff-reviewer finders and gov-skeptic batches and written by gov-synthesizer, 2026-10-18.

Range: 15cec9200c95a828acf2a4c7a53d47a0847a0371...a66c855f3ee6839fee8877e47e56b0673a5396e0 (round 1)

## Verdict: CLEAN WITH FIXES

There is no blocker. There are 2 high items, each covering 1 confirmed finding. Every item is a defect in a design record or in the build's instruments, and each one is fixable in place. The away pass's weak spots are three:

- the memory plan's [chain] table disagrees with v2 [chain] about who owns three units;
- the deprecation window and the shim-call key have no unit that builds them, and the window's presets contradict its own rule;
- the atlas's new Memory view and the map's no-stale-facts arm pass rows they cannot read.

## Review shape

Review shape: intensity light, raw 16, confirmed 15, refuted 1, unverified 0 (0 uncertain), precision 0.94.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| seams | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |
| verification | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

The adjudicated tally by item is 0 blocker, 2 high, 6 medium and 5 low, for 13 items. By raw confirmed finding it is 0 blocker, 2 high, 8 medium and 5 low, for 15 findings. Finding 9 was refuted and is not reported.

Run integrity:

- Lenses: 3/3 returned, 0 died.
- Skeptic batches: 4/4 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 11 judged sound, 4 judged UNSOUND, 0 none proposed, 0 NOT JUDGED. Where a fix was judged unsound, the item carries the skeptic's corrected fix.
- Severity on confirmed findings: 0 ungraded, 2 re-graded by the skeptic (findings 1 and 4).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

The run is not complete in every respect, because 4 fixes were judged unsound and 2 grades were changed.

Roles: the finders were gov-diff-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.

Intensity is light. The security and intent lenses were not run, so their classes were swept only through the checklist shares. This is not a full review.

Intent came from 27 spec documents supplied as `specs`, beside the range's commit messages. The checklist holds 32 items, each assigned to exactly one lens: correctness 11, seams 11, verification 10. By design: the caller's byDesign.

## High

### H1. The memory plan's [chain] table puts three units on builds v2 does not (finding 7)

- **Where:** memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:268, :275, :276-279, :281; against memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1369, :1379, :1380.
- **What is wrong:** Plan line 268 says each line is one planned unit "added to its build's row in v2 [chain]". The plan puts the edge leg and the commit-key leg on dWitnessedBar (275), the promotion route writing `promoted-from` on dLinkedLibrary (281), and four units on dTotalRecall. In v2, the edge checks and `promoted-from` written by `instructions.edit` sit on dOrderedCharter (row 1369), the commit-key leg sits on dWellOiledMachine (row 1379), dWitnessedBar's row (1380) has neither, dLinkedLibrary's row has no promotion unit, and dTotalRecall gets 2 units. The away pass's [chain-impact] agrees with v2, not with the plan.
- **Consequence:** The plan is the record P34 and the atlas name as the memory design. A chain builder who reads it builds the edge leg in dWitnessedBar and the promotion route in dLinkedLibrary, so the same leg gets two owners or none. The plan's 17 lines do not add up to v2's counts.
- **Fix (judged SOUND by the skeptic):** Rewrite the plan's [chain] table so it lists the units exactly as v2 [chain] holds them: the edge checks and `promoted-from` on dOrderedCharter, the commit-key leg on dWellOiledMachine, and dTotalRecall's two merged units. Or drop the table and point to v2 [chain]. Then fix line 268's claim, or say that some lines were merged and moved.
- **Left-shift gate:** A map arm that matches each memory-plan [chain] line's key phrase against v2 [chain] rows and reds when the phrase is owned by a different build, or by none.
- **Related:** Finding 2 (M2) is the same defect, seen by the correctness lens at a binding medium grade. It is kept as its own item because items merge only within one binding grade. I would grade it high with this one, because both describe the same misleading owner.

### H2. No unit builds the deprecation window or the shim-call behaviour (finding 8)

- **Where:** architecture-v2.md:1060-1061 (the keys), :1328-1329 (the presets), :1368 (dGroundRules' row); memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md [p6-distribution] item 4.
- **What is wrong:** `install.deprecation-window` (0, 1, 2, 4) and `install.on-shim-call` (warn, journal, refuse) are owned by dGroundRules, and the presets select window values and `journal`. dGroundRules' four new units cover only the step kind, the `update` walk, the down steps and the release-0 fixture. Nothing forwards a moved command or hook path. The only other shim mentions are dShippedRelease "reading … shim calls" and dConvergedCharter "every shim removed when its window closes". The gap register has no gap for forwarding or deprecation.
- **Consequence:** A preset that selects `journal`, or any window length, has nothing that honours it. The mechanism behind the owner's seamless-supersession direction, which [p6] item 4 promises, has no owning build.
- **Fix (finder's fix judged UNSOUND; the skeptic's corrected fix):** Add the dGroundRules unit as proposed: a forwarding shim for a moved command or hook path, honouring `install.on-shim-call` for `install.deprecation-window` releases, with an arm per value on a planted retired path. Also add a gap owned by dGroundRules. Then update away-pass [chain-impact] (dGroundRules 5 units, 31 in all, 40 gaps) and re-run critical_path.py, since dGroundRules is on the critical path.
- **Left-shift gate:** Class policy-value-with-no-route. Add a map arm that reds when a [policies] key with an owner build is named by no unit clause in that build's v2 [chain] row.

## Medium

### M1. The deprecation window's presets contradict its own rule (finding 1)

- **Where:** architecture-v2.md:1328 (the `install.deprecation-window` presets 1, 2, 2, 4), :1060 (its rule), :1235 (`currency.max-behind` presets 4, 2, 1, 2).
- **What is wrong:** The catalogue says the window is "equal to `currency.max-behind`, so an adopter inside its currency budget never meets a removed surface". The two preset rows agree only under standard. No check ties the two keys together.
- **Consequence:** Under velocity, an adopter 4 releases behind is inside its budget, but surfaces are removed after 1 release. It meets a removed command or hook path, which P38 and the key's own Why say cannot happen.
- **Fix (judged SOUND by the skeptic):** Either set the deprecation-window preset row to max-behind's values (4, 2, 1, 2), or restate the rule as "at least `currency.max-behind`" and raise velocity to 4 or more. Then register a constraint arm over the preset table that fails when window < max-behind in any preset, and see it red on today's velocity row.
- **Left-shift gate:** Class rule-stated-with-no-check-that-fails. The preset-constraint arm above, with a planted violating row.
- **Grade:** The finder graded high and the skeptic medium. Medium binds, because the text is design and nothing implements it yet.

### M2. The memory plan's [chain] places the edge leg, the commit-key leg and `promoted-from` wrongly (finding 2)

- **Where:** memory-plan.md:268, :275, :281; architecture-v2.md:1369 (clause 28), :1379 (clause 33), :1380.
- **What is wrong:** This is the same defect as H1, seen by the correctness lens. A grep for "edge leg" in v2 matches nothing, and "commit-key leg" matches only line 1379. The plan's placement is also wrong in itself: dWitnessedBar's only parent is dDeclaredLoop, so a commit-key leg "reading the binding" there would read a node that dWellOiledMachine, a later build, creates.
- **Consequence:** Two defining records give different owners for the same units, and the plan's placement sets a clause on a later build's node.
- **Fix (judged SOUND by the skeptic):** Rewrite memory-plan [chain] to match v2: edge checks on dOrderedCharter, the commit-key leg on dWellOiledMachine, `promoted-from` on dOrderedCharter. Or drop the per-build table and point at v2 [chain]. Then grep both records for each unit's phrase and confirm exactly one owner. One edit closes both this item and H1.
- **Left-shift gate:** Class amendment-leaves-its-other-half-standing. The H1 arm, plus an arm that reds when a clause on build B reads a node created by a build that is not B or an ancestor of B.
- **Grade:** Medium binds. I would grade it high with H1, for the reason given there.

### M3. No edge type carries a commit to a unit or an item (finding 3)

- **Where:** memory-plan.md:193 ([cycle] hop "commit → unit and item"), :166 (`serves`), :167 (`made-by`), :136 ([sites], `Gov-Item:`).
- **What is wrong:** The hop uses `serves` (through `Gov-Unit:`) and `made-by`. The [edges] table limits `serves` to "record, work order → unit or build" and `made-by` to "commit, record → act or the owner". `decides` takes a commit only as a target. So no type in the closed set has a commit source and a unit or item target, and the `Gov-Item:` trailer that [sites] maps to "its edge type" has none.
- **Consequence:** The plan's own rule, that an edge whose source or target sits outside its row's namespaces reds, would reject every `Gov-Unit:` trailer, and `Gov-Item:` cannot be registered. The cycle's commit hop stays open while the atlas draws it as closed.
- **Fix (judged SOUND by the skeptic):** Widen `serves` to "record, work order, commit → unit, item or build", or add a typed edge for commit → unit/item. Update [sites], [cycle] and P33's list to match, and add a planted `Gov-Item:` trailer case to the edge leg's fixtures.
- **Left-shift gate:** An atlas or map arm that checks each [cycle] hop's source and target namespaces against the declared source and target of every edge type it names, and reds on a mismatch.

### M4. The Memory view does not refuse a record kind it cannot place (findings 5, 13)

- **Where:** memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:568-575; atlas.html:1524; memory-plan.md:321 ([view]).
- **What is wrong:** Kind placement keeps only writer tags that resolve to a flow step or program item (`if t in place`). A kind whose writer cell is prose, names a build, or names a non-item tag is kept with no place and no refusal, and is filed under "named by no flow item". Running derive() gives 36 of 76 kinds unplaced. They include all six kinds the away pass added (commit, view, registry, archive, instrument, witness) and kinds with real writers (transition, act, journal, lease, run record, work order). Six writer cells hold tags that resolve to no item (charter.override, attendance.scope, design.forks, adopters.toml, build.worktree, observability.run-record), and each is dropped at rc 0.
- **Consequence:** The plan's [view] says each kind is "placed on the step or program its writer belongs to", and the generator's comment says the run stops on what it cannot read. Instead nearly half the registry is shown as written by no item, which looks exactly like a real gap, and a mistyped item tag can never turn the view red.
- **Fix (both finders' fixes judged UNSOUND; the skeptics' corrected fixes, combined):** First amend the layer-memory [contract] rows whose writer cell is prose or names a build. Each must either name its writer item's tag or carry a declared no-writer marker, as "design record" does ("a core memory kind with no writer item"). Split the writer tags three ways: item tags resolved against the steps and programs, key tags resolved against the v2 [policies] catalogue, and file-name tags (a token with a file extension such as `.toml`) resolved against the tree or exempted. Refuse any tag that resolves in none of the three. Then make derive() exit on a kind with no place that lacks the marker, and amend the plan's [view] to say that a kind carrying the no-writer marker is shown unplaced. Plant an unplaceable kind and a writer cell with a ghost item tag, and see each go red at rc 1. The edge-status half of finding 5 is fixed under M5.
- **Left-shift gate:** The planted unplaceable kind and ghost-tag cell above, registered as atlas plants.

### M5. The Memory view files any unreadable edge status as P33 and drops undeclared hop edges (findings 10, 12)

- **Where:** atlas.py:557 (status), :564-565 (hop edges).
- **What is wrong:** The status is `"derived" if r[4].startswith("derived") else "new" if r[4].startswith("new") else "P33"`, so a misspelt, blank, retired or reworded status becomes P33 with no refusal. The pockets regex (line 544) and the hops regex (line 563) do stop the run. Separately, line 564 keeps only the backticked edges found in `names` and refuses a hop only when none is left, so an undeclared edge beside a declared one vanishes. Probes: a status patched to "retired, folded into `amends`" derived as P33, and a hop edge "`follows`, `answered-by-typo`" derived as ['follows'], both with no exit. Today's cells read 12 P33, 11 new and 1 derived, so the status arm has never been seen red and cannot fail.
- **Consequence:** The "declared edge types" chip and the edge table's Status column can count a type the record does not declare, and the diagram can certify a cycle the record does not hold, all at rc 0.
- **Fix (judged SOUND by the skeptics):** Match the status with `re.match(r"(P33|new|derived)\b", r[4])` and call sys.exit naming the row when it does not match. In the hop loop, refuse a hop where any backticked lowercase token in the edge cell is not in `names`, not only one with no known edge. Plant a status rewritten to `nwe` and a hop with an undeclared edge, and observe rc 1 for each.
- **Left-shift gate:** The two plants above, registered with the atlas's existing plants.
- **Related:** The hop half is also finding 14 (L4), kept apart because its binding grade is low. This item's fix closes both.

### M6. The no-stale-facts arm witnesses its own zero over an unnamed population (finding 16)

- **Where:** memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:550-567, :738-739.
- **What is wrong:** `unpinned_counts`, new in this diff, returns only its findings. It counts no files and no quotes, prints no figure and asserts no floor. An opening ``` fence with no closing one mutes every later line of its file silently. A DATED substring that comes to match a design record, or a glob that reads nothing, also gives a green run that looks like a clean one. The probe found 21 quotes, all pinned, no unclosed fence and 78 dated files skipped, but the arm emits none of these figures.
- **Consequence:** The night pass's "21 quotes" figure is not one the check witnesses, and a blind arm cannot be told apart from a clean one.
- **Fix (judged SOUND by the skeptic):** Have unpinned_counts return the files read and the quotes seen, print both on the summary line, and red when the quote count falls below a declared floor or a file ends with a fence still open. Add plants `unclosed-fence` (a ``` appended to the gap register above a planted unpinned quote) and `no-records`, and observe each at rc 1.
- **Left-shift gate:** Class zero-witness-over-an-unnamed-population. The two plants above.

## Low

### L1. layer-runtime still states the stale Codex hook set beside its revision (finding 4)

- **Where:** memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:797-798.
- **What is wrong:** The away pass added a "Revised 2026-10-18" bullet saying Codex documents SessionStart, Stop and PostCompact. It left the capability-table bullet above it, "it has no SessionStart, PostToolUse, Stop or PostCompact", unchanged. The cited return (research-harness-cli.md:52) itself calls that line "now stale". PostToolUse's status is left unstated.
- **Consequence:** A capability table described as "measured and never claimed" makes two opposite claims, and a reader who stops at the bullet list takes the stale one.
- **Fix (judged SOUND by the skeptic):** Replace the stale bullet with the measured set (twelve events, naming them, trusted by hash), and keep the revision note as provenance rather than as a second claim. Then grep the runtime and instruction records for "no SessionStart" to find any other copy.
- **Left-shift gate:** Class amendment-leaves-its-other-half-standing. A bug-class checklist entry: a revision note must replace the line it revises, and the fold greps for the old claim's phrase.
- **Grade:** The finder graded medium and the skeptic low. Low binds, because the adjacent revision note limits the harm to a reader who skims.

### L2. The commit and registry kinds have two owning builds (finding 6)

- **Where:** memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:467 (`commit` on dDeclaredLoop), :469 (`registry` on dWitnessedBar); architecture-v2.md:1376 (dTotalRecall, clause 18); memory-plan.md:260, :278.
- **What is wrong:** v2's dTotalRecall row builds "the commit, view, registry, archive, instrument and witness kinds", and the plan also puts the registry kind under dTotalRecall, while layer-memory's owner column names other builds for commit and registry.
- **Consequence:** Each of the two kinds has two owners, against the one-owner rule the away pass restates. Whichever build registers the kind first decides its schema.
- **Fix (finder's fix judged UNSOUND; the skeptic's corrected fix):** Narrow v2 dTotalRecall's clause to view, archive, instrument and witness. Name the commit kind in dDeclaredLoop's commit-node unit and the registry kind in dWitnessedBar's row. In the same edit, remove "registry" from memory-plan [integration] (line 260) and [chain] (line 278). Or move both registry owners to dTotalRecall and leave the plan as it is.
- **Left-shift gate:** A map arm that reds when a kind's owner in layer-memory's registry differs from the build whose v2 [chain] clause names that kind.

### L3. The Memory view groups a kind under a step that only names it (finding 11)

- **Where:** atlas.py:575; atlas.html:1519.
- **What is wrong:** Every item tag in the writer column with a known place is read as a writer, and the view groups each kind under the alphabetically first place. "release exit" ("`release.record` writes it and `deploy.released` names it") is grouped under deploy, which only names it. The finder's second example, "routing", is not a defect: `release.route` does write it.
- **Consequence:** The section "Record kinds, by the step or program whose item writes them" misstates where some kinds are written. The effect stays within the drawing.
- **Fix (judged SOUND by the skeptic):** Take writers only from tags in the writer clause (for example "its writer is/its writers are …" or "`x` writes it"). Or group by the step of the first writer named rather than the sorted first place. Refuse a row whose writer column names tags but whose writer cannot be parsed.
- **Left-shift gate:** A planted writer cell that names a reading step before the writing step, asserting the kind's group.

### L4. A two-edge cycle hop drops a mistyped edge silently (finding 14)

- **Where:** atlas.py:564-565; memory-plan.md:193 (`serves`, `made-by`), :201 (`part-of`, `implements`).
- **What is wrong:** A hop is refused only when none of its edges resolves, so a mistyped second edge is dropped at rc 0. This is the hop half of M5.
- **Consequence:** The plan's claim that every hop's edge is a registered type is unchecked for every hop with more than one edge. The only effect is a wrong label in the view.
- **Fix (judged SOUND by the skeptic):** Compute `unknown = [e for e in found if e not in names]` and sys.exit when it is non-empty, rather than requiring only `used` to be non-empty. Plant a hop edge `serve` and observe rc 1. The M5 fix covers this.
- **Left-shift gate:** The planted `serve` hop.

### L5. Only [pockets] is counted against its raw table lines (finding 15)

- **Where:** atlas.py:550-553, :140-153 (tables()); the module docstring, line 12.
- **What is wrong:** tables() stops a table at its first line that does not start with `|`, so a row separated from its table by a blank line is skipped. Only [pockets] is counted against its raw lines. [families], [sites], [edges], [cycle] and the [contract] kinds are not, though the docstring promises every population is.
- **Consequence:** An edit that splits the 24-row [edges] or the 14-hop [cycle] table loses its tail rows from the view and from its counts, at rc 0.
- **Fix (judged SOUND by the skeptic):** Apply the same raw-line count used for pockets to families, sites, edges and cycle (and to the [contract] kinds block), and sys.exit on a mismatch. Plant a blank line inside [edges] and observe rc 1. The skeptic checked that each section holds one table today, so the count would match now and turn red on a split table.
- **Left-shift gate:** The planted blank line inside [edges].

review-shape kind=diff-review round=1 intensity=light at=synth raw=16 confirmed=15 refuted=1 unverified=0 blocker=0 high=2 medium=8 low=5 agents=8 out-tokens=97052

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1328 | high | medium | confirmed | In v2, line 1060 says the deprecation window is 'equal to `currency.max-behind`, so an adopter inside its currency budget never meets a removed surface'. The preset row at line 1328 is 1/2/2/4, but max-behind's row at line 1235 is 4/2/1/2. The values are equal only under standard. Under velocity, the window (1) is smaller than the budget (4), so the key's own Why is false there. Both lines are new in the away pass, and the away-pass record (lines 214, 306) has nothing that ties the two keys together. AP-26 is pending, but the contradiction lies between two rows the fold wrote, which the harness allows as a finding. It is a design text, so the effect is contained until a chain build implements it. | sound | rule-stated-with-no-check-that-fails |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:275 | medium | medium | confirmed | Memory-plan [chain] (line 268) says each line 'is added to its build's row in v2 [chain]'. It puts 'the edge leg ... the commit-key leg at the push, reading the binding' on dWitnessedBar, and the promotion route writing `promoted-from` on dLinkedLibrary. v2 places them elsewhere. Row 1369, clause 28 (dOrderedCharter) holds '`promoted-from` written by `instructions.edit`, and the edge checks in the tags leg pack'. Row 1379, clause 33 (dWellOiledMachine) holds 'the commit-key leg at the push reading the binding'. dWitnessedBar's row 1380 has no edge or commit-key unit, and dLinkedLibrary's clause 24 has no `promoted-from`. dWitnessedBar's only parent is dDeclaredLoop, so in the plan's placement the leg reads a binding that a later build, dWellOiledMachine, creates. The plan is new in this diff. | sound | amendment-leaves-its-other-half-standing |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:193 | medium | medium | confirmed | In the memory plan's [edges] table, `serves` runs only from 'record, work order → unit or build' and `made-by` only from 'commit, record → act or the owner'. `decides` accepts a commit only as a target. Yet [cycle] gives the hop 'commit → unit and item' the edges `serves` (through `Gov-Unit:`) and `made-by`. [sites] says each trailer, `Gov-Item:` included, is 'mapped to its edge type', but no type in the set has a commit source with a unit or item target. The plan's own rule, 'an edge whose source or target sits outside its row's namespaces' reds, would therefore refuse these trailers. All of this text is new in the plan. | sound | - |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:797 | medium | low | confirmed | In layer-runtime, line 798 still says Codex 'has no SessionStart, PostToolUse, Stop or PostCompact'. The base 15cec9200 has the same line, but the diff left it in place. The 'Revised 2026-10-18' bullet it added two lines below states the opposite for SessionStart, Stop and PostCompact. The cited return (research-harness-cli.md:52) names this exact line as 'now stale'. The capability table, described as 'measured and never claimed', now makes two opposite claims, and PostToolUse's status is left unstated. The adjacent revision note limits the harm to a reader who skims. | sound | amendment-leaves-its-other-half-standing |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:574 | medium | medium | confirmed | Atlas lines 568-574 (added in this diff) keep only ITEM_TAG writers found in `place`, and nothing refuses a kind that resolves to no place. Line 557 maps any Status cell that does not start with 'derived' or 'new' to 'P33'. I loaded derive() and ran it: 36 of 76 kinds have places=[]. Among them are all six away-pass kinds (commit, view, registry, archive, instrument, witness) and kinds with real writers (transition, act, journal, recommendation). atlas.html:1524 files them under 'named by no flow item'. The comment above the code says each kind is 'placed on the step or program its writer item belongs to', and the brief asks whether the view refuses a row it cannot place. It does not. The damage is limited to the instrument's drawing, so medium. | unsound | - |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:469 | low | low | confirmed | layer-memory 467 gives `commit` to dDeclaredLoop and 469 gives `registry` to dWitnessedBar. v2 1376 (dTotalRecall) builds 'the commit, view, registry, archive, instrument and witness kinds'. memory-plan 260 and 278 also put the registry kind under dTotalRecall. So two records name different owners for two kinds. One reading, 'completing the registry with rows', would make the owners compatible, which softens the impact. The text still says one thing two ways. | unsound | - |
| 7 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:275 | high | high | confirmed | memory-plan 268 says each line is a unit added to its build's v2 row. Line 275 puts the edge leg and the commit-key leg on dWitnessedBar, and line 281 puts the promotion route and `promoted-from` on dLinkedLibrary. In v2, dWitnessedBar's row (1380) has the portability leg pack and the verdict tails but no edge or commit-key leg. dOrderedCharter's row (1369) holds 'promoted-from written by instructions.edit, and the edge checks in the tags leg pack'. dWellOiledMachine's row (1379) holds 'the commit-key leg at the push reading the binding'. dLinkedLibrary's row has no 'promot' text at all. Away-pass [chain-impact] agrees with v2, not the plan. The record the atlas and P34 name as the memory design would send a chain builder to the wrong build. | sound | - |
| 8 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1061 | high | high | confirmed | v2 1060-1061 give `install.deprecation-window` and `install.on-shim-call` to dGroundRules, and the presets at 1328-1329 select window values and `journal`. dGroundRules' row (1368) builds the upgrade-step kind, the `update` walk, the down steps, the fixture and the legacy homes as the translation window's population. Nothing in it forwards a moved command or hook path. The only other shim mentions are dShippedRelease 'reading ... shim calls' and dConvergedCharter 'every shim removed when its window closes'. The gap register has no gap for forwarding or deprecation. So the mechanism away-pass [p6] item 4 promises has no owning unit, and a preset value has nothing that honours it. | unsound | policy-value-with-no-route |
| 9 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1320 | medium | - | refuted | The finding holds that `commit-msg` has no route. The design gives it one. architecture-v2.md:1379, dWellOiledMachine's clause, ends with 'as `commits.edge-check` says', and that is the convention this record uses for every keyed behaviour (for example 'only as `runtime.attended-judge` says'). The clause's unit builds whatever the key's allowed values select, and AP-6 parks where the check runs. How each value is mechanised is unit-level detail, which by design is owed to the chain build. Line 1048 lists `commit-msg` as an allowed value owned by the same build, and memory-plan:334 lists it the same way. That makes the strict preset's `commit-msg` a value this unit's clause covers, not a value with no route. The finding cannot be established as more than unit-level detail, and the finder graded it medium, so it is refuted. | sound | policy-value-with-no-route |
| 10 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:557 | medium | medium | confirmed | Confirmed at atlas.py:557. The status is computed as `"derived" if r[4].startswith("derived") else "new" if r[4].startswith("new") else "P33"`, so any other text, including a retired or misspelt status, is filed as P33 with no refusal. At atlas.py:564, `used = [e for e in re.findall(...) if e in names]` silently drops an undeclared backticked edge, and the hop exits only when nothing at all is left in `used`. The pockets and hops tables do exit on a status they cannot read. The Memory view is new in this diff: the base atlas.py has no memory-plan reads. Today every one of the twelve P33 rows starts with 'P33', so the output is correct now. The defect is that the view would certify a set and a cycle the record does not hold, which is contained to the instrument. | sound | - |
| 11 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:575 | low | low | confirmed | Partly true. atlas.py:575 takes every ITEM_TAG in the writer column that has a known place as a writer, and atlas.html:1519 groups each kind under `places[0]` of a sorted list. 'release exit' (layer-memory [contract] row: '`release.record` writes it and `deploy.released` names it') therefore gets places ['deploy','release'] and is grouped under deploy, which only names it. That part is real. The 'routing' half is wrong: the row says '`release.route`, dShippedRelease's, also writes one', so release is a genuine writer there. The effect is confined to how the drawing groups kinds. | sound | - |
| 12 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:557 | medium | medium | confirmed | Same defect as finding 10's status arm, seen at atlas.py:557. The status falls back to P33 for any cell that starts with neither 'derived' nor 'new', and there is no sys.exit arm, unlike the pockets regex at line 544 and the hops regex at line 563, which do stop the run. The [edges] table I read has 12 rows whose status starts with 'P33', 11 'new' and 1 'derived', so this arm has never been seen red and cannot fail. The proposed regex `(P33\|new\|derived)\b` matches every current cell, including 'P33, its targets widened' and 'new: ...'. | sound | - |
| 13 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:575 | medium | medium | confirmed | The Memory view is new in this diff. At atlas.py:575 the writer tags are filtered with `if t in place`, and no step stops the run. I ran derive(): 36 of the 76 kinds come out with empty places. They include transition, lease, run record and work order. Six writer cells hold tags that resolve to no item (charter.override, attendance.scope, design.forks, adopters.toml, build.worktree, observability.run-record), and each is dropped silently. So a mistyped item tag goes through at rc 0. The plan's [view] says (memory-plan.md:321) that each kind is 'placed on the step or program its writer belongs to'. The view instead puts them in a 'named by no flow item' group (atlas.html:1524). The harness asks directly whether the view refuses a row it cannot place, and it does not. The effect is limited to an instrument view. | unsound | - |
| 14 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:564 | low | low | confirmed | At atlas.py:564, `used` keeps only the backticked names found in `names`, and line 565 refuses a hop only when `used` is empty. On a two-edge hop (memory-plan.md:193 serves/made-by, :201 part-of/implements), a mistyped second edge is dropped and the run exits 0. The Memory view is new in this diff. The only effect is a wrong label in a view. | sound | - |
| 15 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:553 | low | low | confirmed | tables() (atlas.py:140-153) stops a table at its first line that does not start with `\|`. A later `\|` row has no separator line after it, so it is skipped without error. In the new memory block, only [pockets] gets a raw-line count (atlas.py:550-552). [families], [sites], [edges] and [cycle], plus the [contract] kinds, are read only through table(). Docstring line 12 promises that each population is counted against its raw lines. I counted the tables: each of these sections holds exactly one table, and the [contract] block holds one table (77 `\| ` lines, which is the header plus 76 rows). So the proposed raw count would match today and would turn red on a split table. | sound | - |
| 16 | verification | memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:550 | medium | medium | confirmed | unpinned_counts (map.py:550-567) is new in this diff (it is absent at base). It returns only the findings it made. It counts no files and no quotes, emits no figure and asserts no floor (lines 738-739 only append findings). An opening fence with no closing one sets `fence` and suppresses every later line of that file without any signal. A DATED substring or an empty glob would likewise give the same green as a clean run. The unpinned-count and unpinned-path plants show the arm can catch one unpinned quote, but they cannot catch these blind spots. The effect is limited to a records-hygiene arm. | sound | zero-witness-over-an-unnamed-population |
