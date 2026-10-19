**Serves:** diff-review PLAY-dClosedLoop-1

# Tier-2 review: the flow and roles adoption of PLAY-dClosedLoop-1 (run A)

Provenance: run A of two independent runs on the same diff. Round 1. Finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Range: 67995cb6ff1fe6d6730a714f7900aeaae8daacac...e1a54ac672b37d558bf5095608e9b378827b414a

## Verdict: CLEAN WITH FIXES

There are no blockers.
Two items are high: role effort has two live homes from dBoundRoles to dConvergedCharter, and the composition's fixed set has no check that refuses an `amends` or `supersedes` on it.
By item, the tally is 0 blocker, 2 high, 8 medium and 1 low (11 items).
By raw confirmed finding, it is 0 blocker, 5 high, 8 medium and 1 low (14 findings).
This was a light-intensity run, so it is not a full review.
The security and intent lenses did not run, and their classes were covered only through the checklist items shared out to the other lenses.

## Subjects reviewed

The diff is e1a54ac67 over 67995cb6f: the flow and roles adoption, designed and settled, reviewed as a design change.
caca7a636 records three researchers' returns (dispatches 123 to 125) and the design record `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`.
cf6f1434c folds the owner's FA-1 to FA-7 into v2, the systems record, the memory plan, the register, the fates and the design record.
dbabaa1fd records the fold's final checks.
e1a54ac67 adds the `workflow` and `lens` namespaces to the systems record.

## Review shape

Intensity light, raw 14, confirmed 14, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| seams | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

Adjudicated tally: 11 items (0 blocker, 2 high, 8 medium, 1 low), covering 14 raw confirmed findings (0 blocker, 5 high, 8 medium, 1 low).
Findings 1 and 7 describe one defect and form one item.
Findings 2, 9 and 12 describe one defect and form one item.
Every other item holds one finding.

## Run integrity

Lenses: 3/3 returned, 0 died.
Skeptic batches: 5/5 returned, 0 died.
Verdict hygiene: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
Fixes on confirmed findings: 11 judged sound, 3 judged UNSOUND, 0 with none proposed, 0 not judged.
Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic.
Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
Lens notes: none supplied, so every lens ran on the kit's generic brief.
Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
Intensity: light. The security and intent lenses were not run, so this is not a full review.
Intent: 22 spec documents supplied as `specs`, beside the range's commit messages.
Checklist: 21 items, each assigned to one lens: correctness 7, seams 7, verification 7.
By design: the caller's byDesign.

## Items

### H1 — Role effort has two live homes from dBoundRoles to dConvergedCharter (ids 1, 7) — HIGH

Where: `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1506` (the dBoundRoles row), with the catalogue rows at v2:979-980, v2:926, the dConvergedCharter row at v2:1519, and the systems record's effort bullet (`2026-10-16-...-systems.md:432-435`).

What is wrong: the FA-6 fold made the dBoundRoles row land `roles.effort.<role>`, `roles.effort.<workflow>.<stage>` and `roles.model.<role>`, and the catalogue names dBoundRoles as their Owner.
The same row still says effort is "kept in `tools/roles/house/policy.toml` by workflow and stage until dConvergedCharter folds it (M7)".
The systems record says the same: effort stays in `[effort.roles]`/`[effort.stages.<workflow>]`, read by `resolve_stage_efforts` (`roles_lib.py:561`), until dConvergedCharter folds it.
A later dBoundRoles clause reads effort from `roles.effort.<role>`, so the key has a reader while the house file is still the stated home.

Consequence: between the two builds, an owner's `roles.effort.gov-builder` and the house file's `gov-builder = "xhigh"` can disagree, and no record says which one wins.
If dBoundRoles adds no reader, dGroundRules' arm ("red when a key whose Owner build has landed has no reader") fails the bar.
If it does add a reader, every role has two readers that can disagree.
dShippedRelease's `adopt.declarations` then copies an adopter's house-file efforts into `roles.effort.*` while the house file is still read, so the same value lives in two places.
This will mislead whoever builds dBoundRoles.

Fix (both finders' fixes were judged UNSOUND by the skeptic; this is the skeptic's corrected fix): dBoundRoles alone lands the move.
In the same unit, it re-points `resolve_stage_efforts`, R12, and `handoff.py`'s `stage-efforts`/`harness-args` to the `roles.effort.*` keys.
The house file's `[effort]` is read only as a seed or declared-value fallback during the transition, with precedence stated (key first, then house file).
Amend the dBoundRoles "kept in house/policy.toml until dConvergedCharter folds it" clause, the systems record's "Effort stays in policy.toml" bullet and v2:926 to match.
dConvergedCharter keeps only the seed's retirement and its upgrade step.
See it red at dBoundRoles on a planted disagreement between the house file and a key.

Left-shift gate: a records check that reds when a key catalogue row's Owner build differs from the build a chain row names as the key's landing or fold point.

### H2 — The composition's fixed set has no check that refuses a patch or supersession (ids 2, 9, 12) — HIGH

Where: `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:190-214` (items 9 to 11), and v2's dOrderedCharter row mechanism at `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1501`, with the dDeclaredLoop (1503), dBoundRoles (1506) and dWitnessedBar (1512) rows.

What is wrong: item 9 fixes a gov item's tag, step, witness and outcome set, every floor item whole, each core role's write class and return schema, the prompt writer and driver whole, the shape kinds, the five lens slots and the canary's key set.
It says the class is "derived, never typed", and FA-5 permits widening only outside this set.
Only `instructions.exclude` (item 6) refuses a fixed row.
Items 4 (amends) and 5 (supersedes) have no fixed-target refusal, and item 11's checks (schema, owned, unique, graph, matrix and floor, typed inputs, shapes, seen-red) have none.
In v2, the derived fixed/open class and "a fixed unit refusing all three" cover instruction units only.
dOrderedCharter's row mechanism is "seen on a planted row of a fixture kind", with no fixed-class arm and no per-kind derivation.
The only row-level fixed red in the chain is dWitnessedBar's "a dropped fixed leg", which is an exclusion.

Consequence: a repository `amends=item.test.verdict@<hash>` that changes the witness, a patch to a core role's write class or the driver, or a `supersedes` of a floor item composes green.
A supersedes row answers to gov's tag, so the floor check still sees the tag present.
The FA-5 boundary and P2's computed-witness floor can be widened away with no failing check, though the design presents the fixed set as its headline guarantee.

Fix (judged SOUND by the skeptic): add a row-class clause to dOrderedCharter's row mechanism, and the same check to item 11's list.
Each registered kind declares its fixed rows and fields, derived from the principles, the floor and the parsers, with an undeclared class read as fixed.
An `amends` touching a fixed field, and a `supersedes` or `exclude` targeting a fixed row, are each refused and seen red on a planted row of a fixture kind, mirroring the units' "a fixed unit refusing all three".
Each kind's build declares its fixed fields and is seen red on a planted patch of one:

- dDeclaredLoop on a patch to a gov item's witness (for example `test.verdict`) and to a floor item.
- dBoundRoles on a patch to the driver and to a core role's write class or return schema.
- dWitnessedBar on a patched (not only a dropped) fixed leg.
- dFairHearing/dCalibratedLens on a sixth lens slot added by patch.

Left-shift gate: a records check that reds when a design record declares a fixed or forbidden class with no chain-row clause that plants a red against it.

### M1 — The house file's required `[effort] default` has no destination key (id 3) — MEDIUM

Where: v2:979 (catalogue), with the `adopt.declarations` clause at v2:1516 and the dConvergedCharter fold at v2:1519.

What is wrong: `tools/roles/roles_lib.py:46` lists `default` among `POLICY_EFFORT_KEYS`.
Lines 404-405 red when `effort.default` is absent (R12), and line 558 falls back to it.
Gov's seed sets `default = "medium"` for every role and stage it does not name.
FA-6 creates only per-role, per-stage and model keys, each defaulting to the role's declared effort, and neither the fold nor `adopt.declarations` says where `default` goes.

Consequence: when the seed retires, an adopter's `default = "low"` (or gov's own `medium`) is dropped without notice, and every unnamed role reverts to its declared value.
A `roles.effort.default` would also parse as a role named `default`.

Fix (judged SOUND by the skeptic): add a `roles.effort.default` key kept out of the `<role>` namespace, with its place in the resolution order stated.
Alternatively, have `adopt.declarations` expand `default` into one `roles.effort.<role>` value per unnamed role, and say so in the dShippedRelease and dConvergedCharter rows.

Left-shift gate: a fold check that lists every key of a folded legacy table and reds on one with no named destination.

### M2 — The stage effort default skips the role's own key (id 4) — MEDIUM

Where: v2:980, the adoption record's item 8 (lines 187-188) and the dBoundRoles clause at v2:1506.

What is wrong: the default of `roles.effort.<workflow>.<stage>` is "the role's declared effort".
At v2:979 that phrase is the default of `roles.effort.<role>`, so it means the role definition's own field, which skips the owner's role-level override.
Today `resolve_stage_efforts` (`roles_lib.py:561-566`) falls back to `resolve_effort(policy, slot)`, the role's configured level.

Consequence: an owner who sets `roles.effort.gov-builder = low` gets low only outside workflow stages.
Every stage the builder fills runs at its declared effort unless each stage key is also set.
This inverts today's resolution order without notice, including for values `adopt.declarations` migrates.

Fix (judged SOUND by the skeptic): state the stage key's default as `roles.effort.<role>` for the stage's role, then that role's declared effort.
Make the same change in the catalogue row, item 8 and the dBoundRoles clause.
Test it with a planted role-level override that a stage must inherit.

Left-shift gate: a catalogue check that each defaulted key's default names a resolvable chain of keys, and a fixture comparing the new resolution order with today's resolver.

### M3 — dBoundRoles' widening-report clause rests on a later build (id 5) — MEDIUM

Where: v2:1506 (dBoundRoles), against v2:1501 (dOrderedCharter) and v2:1516 (dShippedRelease).

What is wrong: dBoundRoles lists "a widening patch named in the update's report".
dOrderedCharter's report covers units only, and its row mechanism never extends the report to rows or widenings.
The extension to "every kind... every repository row and every widening" is a dShippedRelease deliverable, and dShippedRelease depends on dBoundRoles.

Consequence: when dBoundRoles lands, no report lists a role widening.
The clause is checked vacuously, or it pulls dShippedRelease's work forward, breaking the rule that a clause sits on its own build or an ancestor.

Fix (judged SOUND by the skeptic): move the widening-report clause to dShippedRelease, where it is already listed.
Alternatively, extend dOrderedCharter's row mechanism so the unit report covers every registered kind's rows and widenings, with its own seen-red, and leave dShippedRelease only the release-side wiring.

Left-shift gate: a chain check that reds when a clause names a deliverable first owned by a descendant build.

### M4 — The `load_policy` re-point gives the gates half two targets (id 8) — MEDIUM

Where: v2:1519 (dConvergedCharter), the DA-H5/DA-M6 clause and the new FA-6 clause.

What is wrong: the older clause re-points `roles_lib.load_policy` with `check_roles.py`, `handoff.py` and `render_agents.py` to dGroundRules's reader.
The FA-6 clause sends the house file's `[gates]` into each role definition's gate grant, "never the policy file".
`load_policy` reads both `[effort]` and `[gates]` (`roles_lib.py:48`, gates parsed at 442-474).

Consequence: the reader inventory has no single correct target for the gates half.
A builder following the older clause routes the gate grant through the policy reader, which FA-6 rules out.

Fix (judged SOUND by the skeptic): narrow the DA-H5/DA-M6 re-point to `load_policy`'s `[effort]` reads, re-pointed to the `roles.effort.*` keys.
State that its `[gates]` reads, with `check_roles.py` R12 and `render_agents.py`, re-point to the role definition's grant field.
See it red on a planted reader that still reads `[gates]` from the house file.

Left-shift gate: the reader-inventory arm extended to name each folded table's destination and red when one reader has two.

### M5 — The widened `instructions.exclude` refusal has no failing check (id 10) — MEDIUM

Where: v2:1027 (the `instructions.exclude` catalogue row), the adoption record's item 6, and the dDeclaredLoop (1503) and dBoundRoles (1506) rows.

What is wrong: the catalogue row refuses excluding a fixed row or one another active row needs, names as its actor or grants.
Item 6 adds that a role left acting in no item is excluded with it, and the scenarios table promises "excludes an item another needs → refused".
dOrderedCharter gives only "`instructions.exclude` over any registered kind's tags", and no kind's row plants an exclusion of a needed item, an actor role or a granted leg.

Consequence: an exclusion that cuts a gov item's `needs`, leaves an item with an excluded actor, or drops a leg a role is granted composes without a refusal.

Fix (the finder's fix was judged UNSOUND by the skeptic, because it put the grant refusal on dWitnessedBar, an ancestor of the build that brings the gate grant; this is the skeptic's corrected fix):

- On dDeclaredLoop's row: excluding an item another active item `needs` is refused and names the requirer.
- On dBoundRoles's row: excluding a role an active item names as its actor is refused.
- On dBoundRoles's row: a role left acting in no item is excluded with it or reds at the matrix arm.
- On dBoundRoles's row: excluding a leg that a role's gate grant names is refused.

Each is seen red on a planted overlay.

Left-shift gate: a records check that every "→ refused" row in a design record's scenarios table maps to a chain-row seen-red.

### M6 — The four new step-gate joins arm no failing case (id 11) — MEDIUM

Where: v2:1518 (dCalibratedLens), with v2:1503 (dDeclaredLoop), v2:1506 (dBoundRoles) and v2:1512 (dWitnessedBar), against dSafePassage's contract at v2:1500.

What is wrong: dSafePassage requires each later class's build to arm its join "and plant its red", as dTotalRecall does.
dCalibratedLens's lens-tag join is seen only on a planted repository lens swapped into a run, with no red.
The item, role/workflow and leg tag joins on the other three rows have no red of their own; their seen-red lists name other arms only.

Consequence: renaming or removing a gov item, role, workflow, lens or leg can reach adopters with no change record and no red.
Item 14's re-pointing depends on exactly that rename, split and retire path.

Fix (judged SOUND by the skeptic): each of the four clauses adds "seen red on a planted <item|role|workflow|lens|leg> tag removed with no change record, and green on one naming its successor", matching dOrderedCharter's unit-tag join.

Left-shift gate: a chain check that every clause joining dSafePassage's step gate carries a planted red.

### M7 — FA-5's "every widening reported" has no check that can fail (id 13) — MEDIUM

Where: v2:1506 (dBoundRoles), v2:1516 (dShippedRelease), and the adoption record's items 4 and 10 (line 203).

What is wrong: dBoundRoles' widening-report clause is outside its seen-red list (shape kind, actor template, harness path).
dShippedRelease's report is only "seen on a planted release", a positive fixture.
No record defines which direction of a scalar change (a ceiling, an allowance, an effort) counts as widening.

Consequence: a report that omits a widening, or a composer that classes a raised ceiling as a narrowing, passes every listed check.
FA-5's condition for allowing widenings, that the owner sees each one, can fail silently.

Fix (judged SOUND by the skeptic): each kind declares, for every open field, which direction widens: for a set field `add` widens, and for a scalar field an order over its values.
dBoundRoles and dShippedRelease are each seen red on a planted widening patch (a gate grant `add` and a raised ceiling) that the report fails to name.

Left-shift gate: a records check that reds on a clause whose only fixture is positive ("seen on") where the clause states a guarantee.

### M8 — An exclusion named by a policy value composes green (id 14) — MEDIUM

Where: the adoption record's item 6 (line 181) and v2's `instructions.exclude` row (v2:1027), against `review.breakpoints` and `probe.points` (v2:1029-1030) and `review.opt-in` (v2:996).

What is wrong: the exclude refusal covers rows that another row needs, names as actor or grants, but not policy values that name the excluded tag.
Item 14 re-points those values only on a rename, and no clause resolves a breakpoint, probe point or opt-in name against the composition.
FA-1 extends exclude to every kind, items and lenses included, so this path is newly reachable.

Consequence: a repository that excludes a gov item named in its `review.breakpoints`, or a lens its `review.opt-in` selects, composes green.
The breakpoint or lens then never fires, which is the failure item 14 guards against for renames.

Fix (judged SOUND by the skeptic): widen `instructions.exclude`'s refusal, and the dOrderedCharter clause, to any policy value that names the excluded tag, naming the key.
Alternatively, resolve every boundary-naming and lens-naming policy value against the composition and red on one that does not resolve.
Either way, see it red on a planted exclusion of an item that `review.breakpoints` names.

Left-shift gate: the bug-class checklist entry policy-value-with-no-route, armed as a composition check that resolves every tag-valued policy key.

### L1 — The dConvergedCharter clause says effort folds "never [into] the policy file" (id 6) — LOW

Where: v2:1519 (dConvergedCharter), against v2:920, v2:926, v2:979-980 and the fates row.

What is wrong: the clause folds the house file's `[effort]` into `roles.effort.*`, then calls the house file "the one legacy home that folds into role definitions, never the policy file".
`roles.effort.*` are policy-file keys (v2:920: "Every key lives in `.governance/policy.toml`").
v2:926 and the fates row state the destination correctly.

Consequence: wording only, but a builder could drop the effort keys' reader re-pointing.

Fix (judged SOUND by the skeptic): reword to "`[gates]` and gov's default efforts fold into the role definitions, and a repository's efforts into the `roles.effort.*` policy keys".

Left-shift gate: none fits a single wording slip beyond H1's Owner-versus-fold check.

review-shape kind=diff-review round=1 intensity=light at=synth raw=14 confirmed=14 refuted=0 unverified=0 blocker=0 high=5 medium=8 low=1 agents=9 out-tokens=73513

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1506 | high | high | confirmed | Confirmed in the current tree and introduced by this diff. The v2 dBoundRoles row (line 1506) still says 'with effort kept in `tools/roles/house/policy.toml` by workflow and stage until dConvergedCharter folds it (M7)'. The same row now also lands '`roles.effort.<role>`, `roles.effort.<workflow>.<stage>` and `roles.model.<role>` ... (FA-6)'. The base row had only the first clause, so the diff appended the second without amending the first. The catalogue rows at lines 979-980 make dBoundRoles the keys' Owner. The systems record (lines 432-435, revised 2026-10-19 for FA-6) says 'Effort stays in `policy.toml` ... which `resolve_stage_efforts` already reads ... until dConvergedCharter folds them into `roles.effort.<role>`'. The dConvergedCharter row and v2 line 926 fold `[effort]` into `roles.effort.*` at dConvergedCharter. A later commit (night pass two, point 2) added a clause to dBoundRoles that reads effort from `roles.effort.<role>` and must be seen red on a planted below-medium effort. That clause gives the key a reader at dBoundRoles while the house file stays the stated home, so effort has two homes from dBoundRoles to dConvergedCharter and no record says which one wins. No later commit fixed this. | unsound | amendment-leaves-its-other-half-standing |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:205 | high | high | confirmed | Confirmed. In the adoption record, item 9 (lines 190-203) defines the fixed rows and fields, including an item's tag, step, witness and outcome set, floor items whole, the prompt writer and driver whole, and the five lens slots. Item 10 permits widening 'an open field'. Item 6 refuses a fixed row only for `instructions.exclude`. Item 4 (amends) and item 5 (supersedes) have no fixed-target refusal, and item 11's list of checks (lines 207-214) has none either. In v2, dOrderedCharter's 'row mechanism for every kind' clause (amends, supersedes, exclude, pins, re-apply) also has no refusal of a fixed row or field. The unit-level 'a fixed unit refusing all three' covers instruction units only, and the only row-level fixed seen-red in the chain rows is dWitnessedBar's 'a dropped fixed leg' (line 1512), which is an exclusion. Nothing stated would refuse an `amends` of a gov item's witness or a `supersedes` of a floor item or the driver, yet FA-5's widening relies on that boundary. This is new surface from this diff, and the gap will mislead the chain builds. | sound | - |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:979 | medium | medium | confirmed | Confirmed. tools/roles/roles_lib.py:46 lists `default` among POLICY_EFFORT_KEYS. Lines 404-405 red when `effort.default` is absent (R12), and line 558 falls back to `effort["default"]`. The seed tools/roles/house/policy.toml sets `default = "medium"` for 'every role and stage this file does not name'. FA-6's destination keys (adoption record item 8, v2 catalogue lines 979-980) are only per-role, per-stage and model, each defaulting to the role's declared effort. The adopt.declarations clause in dShippedRelease ('the house file's efforts as `roles.effort.*` values') and the dConvergedCharter fold ('`[effort]` folded into `roles.effort.*`') do not say where `default` goes. A `roles.effort.default` would also parse as a role named 'default'. The effect is contained: one tunable silently changes meaning at the fold. | sound | a-folded-field-leaves-its-row-shape-docs-behind |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:980 | medium | medium | confirmed | The diff adds this; base v2 has no roles.effort keys. In v2:979, 'the role's declared effort' is the default of `roles.effort.<role>`, so the phrase must mean the role definition's own field. The same phrase at v2:980, used as the default of `roles.effort.<workflow>.<stage>`, therefore skips the owner's `roles.effort.<role>` override. The adoption record's item 8 (line 187-188, 'each defaulting to the role's declared value') and the dBoundRoles clause at v2:1506 say the same. Today's roles_lib.py:561-566 resolve_stage_efforts falls back to resolve_effort(policy, slot), which reads the house file's [effort.roles] entry, and adopt.declarations (v2:1516) turns those entries into `roles.effort.<role>` values. Read as written, an adopted role-level override no longer reaches the role's stages, which inverts today's resolution order. The records stand unchanged at HEAD, so no later commit fixed it. The record is design-only, so the effect is contained. | sound | - |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1506 | medium | medium | confirmed | The dBoundRoles row (v2:1506) lists 'a widening patch named in the update's report' as a deliverable but gives it no seen-red. dOrderedCharter's report clause covers units ('composition and its report'). Its row-mechanism clause ('the overlay's row mechanism for every kind a later build registers: owned..., amends, supersedes, exclude, pins, change records, instructions.stale') never extends that report to rows or widenings. The extension, 'the update's report extended to every kind... every repository row and every widening... seen on a planted release (FA-2, FA-5)', is a dShippedRelease deliverable (v2:1516). dShippedRelease lists dBoundRoles among its dependencies, so it is a later build. As written, the dBoundRoles clause rests on a later build's deliverable, or two builds own the same work with no check at the earlier one. It is introduced by this diff and still stands at HEAD. | sound | - |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1519 | low | low | confirmed | This text is new in this diff: the base v2 has no 'never the policy file'. The dConvergedCharter clause (v2:1519) folds the house file's `[effort]` into `roles.effort.*`. The same clause then calls the house file 'the one legacy home that folds into role definitions, never the policy file'. The catalogue (v2:920, 'Every key lives in `.governance/policy.toml`'; rows 979-980) makes `roles.effort.*` policy-file keys. The clause therefore contradicts itself and the catalogue, though v2:926 and the fates row state the destination correctly. The defect is wording only. | sound | - |
| 7 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1506 | high | high | confirmed | At HEAD, architecture-v2.md:1506 (dBoundRoles) still says "with effort kept in `tools/roles/house/policy.toml` by workflow and stage until dConvergedCharter folds it (M7)". The same row now also lands `roles.effort.<role>`, `roles.effort.<workflow>.<stage>` and `roles.model.<role>` (FA-6), and the key catalogue in the diff names dBoundRoles as their Owner. The FA-6 revision in systems.md ("Effort stays in `policy.toml` ... which `resolve_stage_efforts` already reads (`roles_lib.py:561`), until dConvergedCharter folds them into `roles.effort.<role>`...", revised 2026-10-19) says the keys arrive only at dConvergedCharter, and dConvergedCharter's row folds `[effort]` into `roles.effort.*`. So the records disagree on which build lands the keys, and between the two builds one effort has two homes with no stated precedence. The fold wrote this text, so the defect is in scope. It will mislead whoever builds dBoundRoles, which makes it high. | unsound | - |
| 8 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1519 | medium | medium | confirmed | At HEAD, architecture-v2.md:1519 (dConvergedCharter) still re-points "`roles_lib.load_policy` with `check_roles.py`, `handoff.py` and `render_agents.py`" to dGroundRules's reader in the DA-H5/DA-M6 clause, which is unchanged from base. The same row's new FA-6 clause sends the house file's `[gates]` "into each role definition's gate grant, ... never the policy file". Because `load_policy` reads both `[effort]` and `[gates]`, the row now gives the gates half of the reader two contradictory targets. The new clause made the contradiction reachable. The effect stays within one row's unit planning, so medium. | sound | - |
| 9 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1501 | high | high | confirmed | Design item 9 of the adoption record fixes floor items whole, every gov item's tag, step, witness and outcome set, each core role's write class and return schema, the shape kinds and the lens slots. FA-5 allows widening only outside that set. In v2, the derived fixed/open class (an undeclared class read as fixed, a fixed unit refusing amends, supersedes and exclude) is stated only for instruction units. dOrderedCharter's new row-mechanism clause (line 1501) lists owned, amends, supersedes, exclude, pins, change records and re-apply "each seen on a planted row of a fixture kind", but has no class derivation and no refusal of a patch on a fixed field. dDeclaredLoop (1503) says only that a gov item's needs and routes are changed by a pinned patch, and its reds are a planted repository item, not a patch on a fixed field. dBoundRoles (1506) reds a shape-kind mismatch, a missing template and a missing harness path, but no patch on a write class or return schema. dWitnessedBar (1512) reds a dropped fixed leg, not a patched one. Exclude of a fixed row is refused (item 6), but amends and supersedes on fixed fields have no check that can fail. A grep of the gap register and systems record for a fixed-set gap found none. This is a stated rule with no failing check and will mislead the chain builds, so high. | sound | rule-stated-with-no-check-that-fails |
| 10 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1027 | medium | medium | confirmed | The `needs` and actor parts are placed correctly. The grant part is not. The gate grant is a role field that dBoundRoles brings (design item 8 and the chain's dBoundRoles entry). dWitnessedBar is an ancestor of dBoundRoles (1506 lists it as a dependency), so a dWitnessedBar clause checking role grants would read a later build's kind, which breaks the rule that a clause sits on its own build or an ancestor. That refusal belongs on dBoundRoles. | unsound | rule-stated-with-no-check-that-fails |
| 11 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1518 | medium | medium | confirmed | dSafePassage's step-gate clause (v2:1500) says each later class joins when its build lands it, 'that build's row arming the join and planting its red'. dTotalRecall does this: 'seen red on a planted kind's schema removed with no row'. All four joins are new in this diff (none exist at 67995cb6f). dCalibratedLens has 'lens tags joined ..., seen on a planted repository lens swapped into a run', with no red. On dDeclaredLoop (1503), dBoundRoles (1506) and dWitnessedBar (1512), the 'each seen red on' lists name only other arms: a planted repository item, a role in an undeclared shape kind, an unsourced row, and so on. None plants a gov tag removed with no change record. So none of the four joins is ever seen red, against the contract and against design item 14. Nothing at HEAD fixes this. | sound | rule-stated-with-no-check-that-fails |
| 12 | verification | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:190 | high | high | confirmed | Design item 9 (adoption record:189-202) fixes, among other things, a gov item's tag, step, witness and outcome set, every floor item whole, each core role's write class and return schema, and the canary's key set. It says the class is 'derived, never typed'. The checks in item 11 (schema, owned, unique, graph, matrix, floor, typed inputs, shape kinds, seen-red) include no refusal of a patch on a fixed row or field. In v2 at HEAD, the only fixed-class enforcement is for units: 1501's 'an undeclared class read as fixed ... a fixed unit refusing all three'. The row mechanism on the same row says only 'each seen on a planted row of a fixture kind', with no fixed-row red. Grepping rows 1503, 1506, 1512, 1516 and 1518 for 'fixed' finds only dWitnessedBar's 'a dropped fixed leg', which covers exclude, not `amends` or `supersedes`. No build is given the per-kind derivation of the fixed set. The fixed set is the design's headline guarantee and has no owning unit, so a chain build implemented from its row would ship patches that widen the set. That misleads the next change. | sound | - |
| 13 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1506 | medium | medium | confirmed | In v2 line 1506, dBoundRoles lists 'a widening patch named in the update's report' as a clause, but its seen-red list covers only three cases: a role in an undeclared shape kind, an actor patch whose role lacks the template, and a missing harness path. A widening is not among them. dShippedRelease's report clause at line 1516 is only 'seen on a planted release', which is a positive fixture with nothing that can go red. Adoption item 10 (line 203) and item 4 say a set field takes add/remove and a scalar takes a value. None of v2, the adoption record or the other build records defines which direction of a scalar change (a ceiling, an allowance, an effort) counts as widening. The widening grant is new in this diff (FA-5), so a report that omits a widening passes every check that is listed. | sound | - |
| 14 | verification | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md:181 | medium | medium | confirmed | Adoption item 6 (around line 181) and v2's `instructions.exclude` catalogue row refuse only a fixed row or a row that another active row needs, names as its actor, or grants. `review.breakpoints` and `probe.points` are 'a set of named item boundaries', and `review.opt-in` holds named lenses. Item 14 re-points those values only on a rename. I grepped v2 and the systems record for a check that a breakpoint, probe point or opt-in name resolves against the composition, or refuses an exclusion it names, and found none. The one breakpoint hit, at line 1503, is about repository stages being reviewed through breakpoints. Extending exclude to every kind, items and lenses included, comes from this diff (FA-1), so the stale-reference path is newly reachable. | sound | policy-value-with-no-route |
