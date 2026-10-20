**Serves:** diff-review PLAY-dClosedLoop-1

# Review: dClosedLoop library round, follow-up run A (round 2)

Tier-2 diff review, round 2 of the library round, run A of two independent runs. Finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Every line cited is at the worktree's HEAD.

Range: d4fc4bb51d56c315afea4f3fdf18ea86f947c020...0dd96272468fb2487d51f362266f0ef46185859b (the fold commit 0dd962724). Round 1's report, the atlas, the generated map, memory/gotchas/INDEX.md and the build README were excluded.

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. 14 items carry 19 confirmed findings. By item: 0 blocker, 0 high, 10 medium, 4 low. By raw confirmed finding: 0 blocker, 0 high, 15 medium, 4 low. Every item is a defect in design records that a chain build would inherit, so the fixes belong in this build's records before a chain build cites them.

## Review shape

Intensity light, raw 24, confirmed 19, refuted 5, unverified 0 (0 uncertain), precision 0.79.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 8 | 6 | 2 | 0 | 0 | 0.75 |
| seams | yes | 8 | 6 | 2 | 0 | 0 | 0.75 |
| verification | yes | 8 | 7 | 1 | 0 | 0 | 0.88 |

### Run integrity

- Lenses: 3/3 returned, 0 died. Skeptic batches: 5/5 returned, 0 died.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 18 judged sound, 1 judged UNSOUND (id 6, whose skeptic's corrected fix is written below), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded, 4 re-graded by the skeptic (ids 9 and 23 medium → low; ids 17 and 18 high → medium).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- No lens notes were supplied, so every lens ran on the kit's generic brief.
- This was a light review. The security and intent lenses were NOT run, and their classes were swept only through the checklist shares, so this is not a full review. A zero in those classes is not evidence of absence.
- Intent: 8 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 21 items, each assigned to exactly one lens (correctness 7, seams 7, verification 7).
- By design: the caller's byDesign.

## Medium

### M1. The fork population `build.distill` reads has no writer that guarantees it (ids 1, 21)

- **Where:** flow-steps.md:213 (`build.distill`), :159 (`design.decompose`), :162 (`design.unit-spec`), :208 (`build.unit-pass`), :231-233 (Build's Memory line); layer-library.md:215-222 and its [review-fold] H1 row at :364.
- **What is wrong:** `build.distill` turns "a fork with no class" red, and it says "an empty set passes only where no fork was resolved". No upstream witness requires either a fork record or its class.
  - Only Design's Memory line (:174-176) writes a class.
  - `design.unit-spec`'s witness joins each raised fork only to its resolution.
  - `design.decompose` records feature forks under a witness that checks only the roster and the interface schema.
  - Build-time forks ("fork → as design.forks says", :208) appear in no Build Memory line.
- **Consequence:**
  - An unclassed fork is first caught in Build, after Design has exited. By [rules] (:29), that red returns the frontier, which is `build.distill` itself. That is a command, and a command cannot classify a fork, so the build sticks before Test.
  - A fork that was resolved but never recorded gives an empty population, and the witness passes vacuously. Round 1's H1 (vacuous population) is therefore fixed only in part.
- **Fix (judged sound by the skeptic):**
  - Put the check at the writer: `design.decompose`'s and `design.unit-spec`'s witnesses join every raised fork to a fork record with its class declared.
  - Add Build's fork records, with their class, to Build's Memory line.
  - Have `build.distill` read its population from those witnesses, not from a directory listing.
  - Give `build.distill` an explicit red route: an unclassed fork goes to the role that resolved it (unit re-entry), counted against `flow.route-backs`.
- **Probe:**
  - Walk a build with one Build-time fork resolved under `agents-feature-rich-expandable`, and name the item that writes its class.
  - Plant a fixture build whose design names a fork it never recorded, and confirm the chain build's check goes red.
- **Gate:** a design-records join that every route's named output has an item whose witness requires it (class route-names-an-output-its-actor-never-emits; vacuous-selector-empty-population).

### M2. `decisions.major`'s non-default values have no witness arms, and the ratification is stated two ways (ids 2, 10, 19)

- **Where:** flow-steps.md:213 (`build.distill`'s Does, witness and Then), :240-241 (Build's Breakpoints); v2:605 (the values), v2:801 (the strict preset).
- **What is wrong:**
  - Under `owner-only`, Does says "only a fork the owner resolved may be major", but the witness never checks who resolved the fork, and no route handles an agent-resolved major fork.
  - Under `author-owner-ratifies`, the witness never joins a row to a ratification. The ratification sits in Build's Breakpoints as "before `build.distill`" but in `build.distill`'s Then cell as a route, and `build.distill`'s Needs is only `build.core`. [rules] :26 reads waits from Needs alone.
  - The rejected outcome ("the fork re-classed as not major") names no writer. The fork record is Design's (layer-library:214-215), and no Build item or Memory clause rewrites it.
- **Consequence:**
  - Under `owner-only`, an author-declared major fork is logged and the witness stays green, so the value behaves like the default `author-rubric`. This effect is contained, because no preset selects `owner-only`.
  - Under the strict preset, a rejection leaves the fork classed major. The one-to-one join then demands a row the owner refused, so the reject outcome cannot settle.
- **Fix (judged sound by the skeptic):**
  - Give the witness one arm per value:
    - `author-rubric`: as now.
    - `owner-only`: each major fork's record names the owner as its resolver. A violation is red, and it routes to re-class the fork as not major or to an owner item.
    - `author-owner-ratifies`: each row joins an owner disposition record that reads ratified.
  - Declare the ratification once, as an owner item that `build.distill` lists in Needs, so no row is written before it.
  - Name the re-class writer: the owner item's resolution, recorded on the fork record. List that write in Build's Memory clause.
- **Probe:** plant an agent-resolved major fork under `owner-only` and confirm the witness goes red. Plant a rejected ratification under `author-owner-ratifies` and confirm the build settles with no row.
- **Gate:** a policy-catalogue join that each catalogued value of a policy an item reads has a witness arm or a route in that item (classes policy-value-with-no-route, owner-item-without-its-reject-outcome).

### M3. `build.distill` runs after `build.core`, so the core checks never grade the decision-log rows (ids 3, 13)

- **Where:** flow-steps.md:212-214 (`build.core` → clean → `build.distill` → `build.exit`), :202 (Build's exit criterion); check-memory-hygiene.sh:2826-2840 (check 27, `row_grammar.py --check-relations`); memory/HYGIENE.md:531.
- **What is wrong:** the fold put the decision-log append after the core checks. Check 27 requires each added decision row that near-matches an older record to name that record or to carry `supersedes`, `coexists-with` or `disputes`. The row `build.distill` writes declares no relation field.
- **Consequence:** a near-matching or ill-formed distilled row passes `build.exit`. Build certifies "no core red stands that the build's own commits introduced" before the build's last commit exists. The red first surfaces at Test's bar, where it is charged to a build already certified clean. This is contained, because Test still catches it.
- **Fix (judged sound by the skeptic):**
  - Order `build.distill` before `build.core`, with Needs `build.recommend` and the closing review. Alternatively, have `build.exit` require a core result keyed to the post-distill HEAD.
  - Add check 27's relation, or the named near-match, to the row's declared fields.
- **Probe:** plant a fork whose decision restates an existing DECISIONS.md row, then run `row_grammar.py --check-relations <base>` over the distilled commit.
- **Gate:** a flow-table check that no commit-writing item is ordered after the step's core-check item.

### M4. layer-memory still names `deploy.distill` as the writer of the decision log (id 4)

- **Where:** layer-memory.md:534-535 ([decisions]).
- **What is wrong:** the line still reads "`deploy.distill` appends the build's major decisions to the log when it lands (layer-library `[log]`)". The fold moved the append to `build.distill` in the build's branch. `deploy.distill` now only confirms the rows at the landed SHA (flow-steps:213, :330; layer-library:216-222). The diff edited this same file (:361-375, :714) and left the line standing. It contradicts the very section it cites.
- **Consequence:** the same fact is stated two ways. dTotalRecall builds the decision log from layer-memory, so it would wire the append at landing, which brings back the post-push write that round 1's M6 fixed.
- **Fix (judged sound by the skeptic):** reword :534-535 to "`build.distill` appends the build's major forks to the log in the build's branch before Test, and `deploy.distill` confirms them at the landed SHA (layer-library `[log]`, the library round's review)".
- **Gate:** class amendment-leaves-its-other-half-standing. When an amendment moves an actor, grep the old actor plus the moved verb across the build's design records.

### M5. dOrderedCharter's widened dependency check cannot pass until a descendant build lands (id 5)

- **Where:** architecture-v2.md:942 (dOrderedCharter's check), :944, :946 (dTotalRecall's units); gap-register.md:84 (`gap-found-17`); layer-library.md:312 ([consult]); tools/memory-tree/row_grammar.py:1007-1033 and :1043-1079.
- **What is wrong:**
  - The fold widened dOrderedCharter's check to "the core never depends on an expansion or an optional component".
  - It filed the recall-import fact under `gap-found-17`, which dOrderedCharter owns.
  - It placed the move of `build_index` and `derive_supersession_map` into memory-tree in dTotalRecall. dTotalRecall descends from dOrderedCharter by way of dDeclaredLoop.
  - Today, check 27 imports memory-recall's bench and refuses when it is absent, and the holds-now path imports `derive_supersession_map`.
- **Consequence:** dOrderedCharter's check is red over the real tree at that build. dOrderedCharter can neither close the gap it owns nor land its check without either a red leg or an exception for the very dependency the check exists to refuse. The gap-ownership join still reads clean.
- **Fix (judged sound by the skeptic):** do one of these:
  - Move the extraction of `build_index` and `derive_supersession_map` into memory-tree inside dOrderedCharter's planned units.
  - Give the check a dated exception that names dTotalRecall, and move the recall-import fact to a gap dTotalRecall owns (a `gap-mem-*` row).
- **Probe:** `grep -n resolve_kit_dir tools/memory-tree/row_grammar.py` at dOrderedCharter's base lists the imports the check would flag.
- **Gate:** a chain-plan join that a gap's owning build carries, in its own or an ancestor's units, every unit its closing check needs.

### M6. A `new:` slug judged at the artifact pin can collide with another review's slug (id 6)

- **Where:** flow-steps.md:428 (`review.report`), :425 (`review.pin`), :430 (`review.fold`).
- **What is wrong:** `new:` passes if "no record held [the slug] at the report's pinned SHA". `review.pin` pins the artifact (a plan revision, spec revisions or a commit range), not the memory tree. A class filed under the same slug after the pin, by another review's fold, still satisfies the arm.
- **Consequence:** two concurrent reviews that mint one slug both pass `review.report`. The second `review.fold` finds a record whose `from:` names the other review, so its witness goes red with no arm in its Then cell. If the other record is not yet merged, the clash surfaces as an add/add conflict on memory/gotchas/<slug>.md at landing. The path is narrow (two reviews minting one slug at once), and the effect is a stalled item or a conflict, not a wrong result.
- **Fix:** the finder's fix was judged UNSOUND. The skeptic's corrected fix:
  - Claim each `new:` slug at report time with a compare-and-swap ref on the remote, as `entry.claim` claims `refs/gov/claims/<slug>`, so the synthesizer sees slugs that other branches minted.
  - Record the claim in the report, so that re-derivation reads the claim and not a head.
  - Give `review.fold` a route for a slug already claimed or filed elsewhere: re-dispose the finding as `class:` that slug, or as a fresh slug within `flow.route-backs`.
- **Gate:** a fixture pair of reports minting the same `new:` slug must turn the claim step red for the second report.

### M7. Plan's core recall fallback selects by scope tags its sources do not carry (id 14)

- **Where:** flow-steps.md:126 (Plan's Memory clause, added by this diff); layer-library.md:305; layer-library.md:230 and layer-memory.md:718 (the research view); flow-steps.md:213 (the decision row).
- **What is wrong:** the read is "the research view and the decision log by the plan's scope tags". In these records, scope tags are instruction-unit load tags (v2:449, layer-instruction:388/409). Research returns are listed by build, date and question. The decision row carries date, build, decision, rationale pointer and reuse entry. Neither carries a scope tag.
- **Consequence:** the planner's fallback returns either nothing, which reads as a clean search (the state [consult] forbids), or everything. Round 1's L1 fix wires a read its source cannot serve.
- **Fix (judged sound by the skeptic):** do one of these:
  - Make scope tags a declared field of the research-return kind and of the decision row, filled at write by `plan.research`, `design.research` and `build.distill`.
  - Restate the read as by build and question, and drop "by the plan's scope tags" at :126 and at layer-library:305.
- **Gate:** a design-records join that each read's selector names a field its source kind declares.

### M8. A `new:` class record is checked only on unbuilt specs, and the ask path has no writer (ids 16, 18)

- **Where:**
  - flow-steps.md:208 (`build.unit-pass`), :210 (`build.scope`), :429 (`review.dispose`), :430 (`review.fold`).
  - layer-library.md:193.
  - layer-memory.md:471-475 ([asks]).
- **What is wrong:** round 1's M3 is fixed only for unbuilt specs.
  - On built work, `build.unit-pass`'s witness only lists the class records in the fix unit's write set. A write set is an allowance: `build.scope` refuses stray paths but never requires a listed path to be written.
  - `review.dispose`'s witness joins each slug to the item or ask that owes the record, not to the record itself.
  - On the ask path, `review.dispose` and layer-library:193 say the ask "is accepted once the class record exists". layer-memory [asks], unamended and declared a closed set, still gives that ask the form "its unit is built, or a review round rules it out". No item is named to write the record.
- **Consequence:**
  - A fix unit that commits its fix without the gotcha passes `build.unit-pass`, `build.acceptance` and `build.scope`.
  - An ask now carries two acceptances, and a rejected ask leaves the slug unfiled for good while `review.report`'s `new:` arm stays true.
  - The left-shift that gap-review-10 targets can be skipped silently on every built-work review. The effect is confined to left-shift record-keeping in a design.
- **Fix (judged sound by the skeptic):**
  - Add an arm to `build.unit-pass`'s witness: for each `new:` slug its findings owe, a record exists under memory/gotchas/ at the commit, with `from:` naming the review and the finding.
  - Amend [asks]' below-threshold form to "its unit is built and its `new:` class records exist, or a review round rules it out and the slug is re-disposed".
  - Name the unit that takes up the ask as the record's writer.
  - Give a rejected ask a re-disposal to `class:`, `gate:` or an owner-ruled none.
- **Probe:** the chain build sees the witness red on a fix-unit fixture whose commit omits the record.
- **Gate:** a join from every `new:` slug in a report to a record or to a live owing item, over built and unbuilt paths alike.

### M9. `build.distill`'s idempotence key names a fork no record defines (id 17)

- **Where:** flow-steps.md:213 and :330 (`deploy.distill`); layer-library.md:216-219; layer-memory [decisions].
- **What is wrong:** the skip, and the witness arm that turns "a second row for one key" red, are both keyed "by build and fork". The row declares no fork field, and no record defines a fork-id grammar: fork records carry option, alternatives and reason only. `deploy.distill` joins one to one to the build's major forks on the same missing key.
- **Consequence:**
  - The only key a row supplies is the build, which makes the join a set join.
  - Example: a retried run that writes fork A's row twice and fork B's row never reads as two rows for two forks and stays green. That is round 1's M5 again.
  - The skeptic graded this medium, not the finder's high: it is a missing field in a design record that a chain build must add, and nothing ships on it yet.
- **Fix (judged sound by the skeptic):** mint an id for each resolved fork in its record (the fork kind in layer-memory [contract]). Make that id a declared field of the decision row, and key the skip and both joins on (build, fork-id).
- **Probe:** the chain build's witness goes red on a fixture log that holds fork A's row twice and fork B's row not at all.
- **Gate:** class append-without-an-idempotence-key. A key named by a skip or a join must be a declared field of the row.

### M10. The reuse-line witness is still typed by the acting agent and cannot fail (id 22)

- **Where:** flow-steps.md:208 (`build.unit-pass`'s witness); [rules] :24; layer-library.md:201-205.
- **What is wrong:** round 1's last finding is left standing while the [review-fold] marks it fixed. The witness is still the builder's own reuse line, `proposed <tag>` or `none` with its reason.
  - Nothing joins `proposed <tag>` to the proposal filed through the instruction command.
  - `none` accepts any reason.
  - The fold changed only the population (M7) and the phrasing (M8).
- **Consequence:** under every `reuse.propose` value, `none: n/a`, or a `proposed <tag>` that was never filed, passes. The witness certifies that text is present, not that a proposal exists.
- **Fix (judged sound by the skeptic):**
  - Join `proposed <tag>` to a proposal record the instruction command wrote for that unit.
  - Admit `none` only with a reason from a closed set, or route it to an owner item.
  - If the owner keeps a typed `none`, record the exception to [rules] :24.
- **Gate:** a design-records check that no witness cell's evidence is the acting agent's own return.

## Low

### L1. The decision row declares neither the fork nor the decision id that its skip names (id 9)

- **Where:** flow-steps.md:213; layer-library.md:216-220.
- **What is wrong:** this is the statement side of M9. The skip is keyed by build and fork, but the declared fields omit the fork. They also omit the decision id that every memory/DECISIONS.md row leads with (for example `TOOL-cSpliceWarden-6`).
- **Consequence:** the key named is not among the fields declared. The rationale pointer may resolve to the fork record, so a double write is not certain.
- **Grade:** the skeptic graded this low, not the finder's medium. It stays a separate item from M9 because findings of different binding grades are not merged.
- **Fix (judged sound by the skeptic):** add the fork id and the minted decision id to the row's declared fields at both sites, and name them as the key that `build.distill`'s skip and `deploy.distill`'s join read.
- **Gate:** the same as M9.

### L2. Build's policy list omits `run.on-owner-question` (id 11)

- **Where:** flow-steps.md:229.
- **What is wrong:** `build.distill` routes "held → as `run.on-owner-question` says", but Build's policy list names only `decisions.major`, which this diff added. Plan (:123), Deploy (:368) and Review (:441) all list `run.on-owner-question`.
- **Consequence:** the step's declared policy set, which the load set and the planned step-policy join (gap-flow-15) read, misses a key that one of its routes branches on. The effect is limited to one declared list.
- **Fix (judged sound by the skeptic):** add `run.on-owner-question` to Build's policies at :229.
- **Gate:** the step-policy join of gap-flow-15, which is that every policy key an item's route reads is in its step's list.

### L3. The research-return count includes probe-script records (id 23)

- **Where:** layer-library.md:151, :249, :254; gap-register (gap-mem-15 :149 and gap-design-07 :208).
- **What is wrong:** "59 research returns in 10 builds" is selected by file name. Five of the 59 are `*-research-*-instruments.md` records that archive probe scripts and are not returns.
- **Consequence:** a wrong stated count. The skeptic graded this low, not the finder's medium, because the design does assign returns their own kind.
- **Fix (judged sound by the skeptic):**
  - Define the research-return kind by a declared field that `plan.research` and `design.research` write (for example a `kind: research-return` key or its own Serves token), not by file name.
  - Re-measure under that kind and correct 59/10/8 in all three places.
  - The red cases owed are a design record and an instruments record, each bound as research.
- **Gate:** class rate-quoted-without-its-denominator. Keep the probe command beside each figure.

### L4. gap-design-05 measures the migration against the wrong predicate (id 24)

- **Where:** gap-register.md:206; tools/memory-tree/check-memory-hygiene.sh:2474-2476.
- **What is wrong:** the gap quotes 236 specs carrying the exact phrase and 256 carrying "one of two". The hygiene check admits the substring "no existing seam", plus "no seam fits" and "reuse-first". "no existing seam|no seam fits" matches 328 specs in 77 builds (case-insensitive over memory/builds/*/spec/*).
- **Consequence:** about 72 admitted specs are missing from the figure, so the one-token migration the gap owes is understated. The defect is a figure in a gap row.
- **Fix (judged sound by the skeptic):** state the three populations, each with numerator, denominator and predicate: the trigger's 236/60, hygiene's 328/77 plus reuse-first, and their union. Keep the probe command beside the gap row.
- **Gate:** the same class as L3.

review-shape kind=diff-review round=2 intensity=light at=synth raw=24 confirmed=19 refuted=5 unverified=0 blocker=0 high=0 medium=15 low=4 agents=9 out-tokens=150890

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | At HEAD, flow-steps:213 (`build.distill`, added by this fold) turns 'a fork with no class' red, and its Then cell routes only to `build.exit` and the owner-ratification arm. The class is written only in Design's Memory line (:174-176, added by this fold). `design.unit-spec`'s witness (:162) checks 'every raised fork joined to its resolution' and never checks the class. A Build-time fork goes 'fork → as design.forks says' (:208), and Build's Memory line (:231-233) lists no fork records. By [rules] (:29), a red at `build.distill` returns the frontier, which is that same command, and a command cannot classify. Neither gap exists at the base, because `build.distill` did not exist there. | sound | route-names-an-output-its-actor-never-emits |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | flow-steps:213 says in Does 'Under `owner-only`, only a fork the owner resolved may be major'. The witness only joins forks to classes and major forks to rows, and nothing checks who resolved the fork. The Then cell routes only `author-owner-ratifies`. `owner-only` is a catalogued value (v2:605). Under it, an agent-resolved fork declared major is either written (and stays green) or skipped (red, with no route). This fold added the sentence without a witness arm or a route. The effect is contained: no preset selects `owner-only` (v2:801). | sound | policy-value-with-no-route |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | At HEAD, `build.core` routes clean → `build.distill` → `build.exit` (flow-steps:212-214), so the rows appended to the decision log land after the core checks ran. Check 27 (check-memory-hygiene.sh:2826-2840, `row_grammar.py --check-relations`) grades decision rows added since the merge-base and requires a relation token or a named match on a near-match. `build.distill`'s Does lists date, build, decision, rationale pointer and reuse entry, with no relation. A near-matching distilled row is therefore first red at Test's bar, after Build's exit criterion ('no core red stands that the build's own commits introduced') was certified. This placement was introduced by the fold. The effect is contained because Test's bar still catches it. | sound | - |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:534 | medium | medium | confirmed | layer-memory.md:534-535 at HEAD still reads '`deploy.distill` appends the build's major decisions to the log when it lands (layer-library `[log]`)'. The layer-library `[log]` section it cites now says `build.distill` appends in the build's branch and `deploy.distill` confirms the rows at the landed SHA (layer-library:216-222), and so does flow-steps:213/:330. This fold edited this same file (:361-375, :714) and left the line standing. It is body prose in the [decisions] section, not a dated revision note, so the same fact is now stated two ways and the line contradicts the very section it cites. | sound | amendment-leaves-its-other-half-standing |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:942 | medium | medium | confirmed | This fold extended dOrderedCharter's planned check (v2:942) to 'the core never depends on an expansion or an optional component', drawn from the kit-to-layer map's optional rows. It also appended the recall-import fact to `gap-found-17` (gap-register:84), which dOrderedCharter owns per v2:118. But the commit's own revision note places the move of recall's two functions into memory-tree in dTotalRecall (v2:946, 'recall importing them'). dTotalRecall's parent is dDeclaredLoop, whose parent is dOrderedCharter (v2:944, :946). The imports are real today: row_grammar.py:1007-1033 imports the memory-recall kit's bench (build_index) and refuses when it is absent, and :1043-1079 imports derive_supersession_map. So dOrderedCharter's check would be red over the tree, and its owned gap can only close in a descendant build. | sound | - |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:428 | medium | medium | confirmed | HEAD flow-steps:428 (introduced by 0dd962724; base :395 read 'names a slug no record holds') admits `new:` when 'no record held [the slug] at the report's pinned SHA'. `review.pin` (:425) pins the artifact's SHAs: the plan revision, spec revisions or commit range, all taken before the lenses run. A gotcha filed under the same slug after the pin, by another review's fold, still satisfies that arm. `review.fold`'s witness (:430) then wants a record whose `from:` names this review. Once the other record is visible on the branch, that witness is red, and the item's Then cell ('the next round ... or released') has no arm for it. Only the generic refusal default applies. Where the other record is not merged in yet, the clash surfaces as an add/add on memory/gotchas/<slug>.md at landing. The path is narrow (two reviews minting one slug at once), and the effect is a stalled item or a conflict, not a wrong result. | unsound | - |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:330 | low | - | refuted | [rules] (flow-steps:28-33) closes this by default. 'A refusal routes by default: it is recorded, and `next` returns the frontier', and 'Past `flow.route-backs` returns to the same item, the loop becomes an owner item, resolved as `run.on-owner-question` says'. A red at `deploy.distill` (:330) is therefore recorded, and a repeated return to the same item escalates to an owner item. The claim that the close 'stalls with no owner item' does not hold. Explicit routes are required only 'where a policy value decides them' (:31), and no policy value decides this outcome. Many sibling single-route command items (`deploy.record`, `deploy.recommend`) rely on the same default. At most this asks for a more specific route, which is a design preference graded low, not a defect the fold introduced. | sound | route-names-an-output-its-actor-never-emits |
| 8 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:195 | low | - | refuted | HEAD gap-register:206 (the finding cited :195 at the fold commit) says 'the hygiene check admits three phrasings of a new seam, while the reuse-line trigger reads one (236 specs carry the exact phrase, 256 one of two)'. The three phrasings match tools/memory-tree/check-memory-hygiene.sh:2475-2476 ('no existing seam', 'no seam fits', 'reuse-first'). My probe at 0dd962724, case-insensitive over memory/builds/*/spec/*.md, reproduces 236 for the exact phrase and 256 for it or 'no seam fits'. Both counts are true of what they state. The gap never claims 256 is the admitted population. The 'migration scoped to 256' impact is the finder's inference, not the gap's text. The finder's 328 is also a whole-file grep, while the check reads only §10 (s10p), so it is not the check's population either. Nothing here is wrong about the tree. | unsound | - |
| 9 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | low | confirmed | HEAD flow-steps:213 (new in 0dd962724) makes `build.distill` idempotent by 'a row already present, keyed by build and fork', and its witness reds 'a second row for one key'. The row's declared fields are 'its date, its build, the decision, a pointer to its rationale, and the reuse entry'. layer-library:216-219 repeats that list. Neither names the fork, or the decision id that every memory/DECISIONS.md row leads with (e.g. `TOOL-cSpliceWarden-6`). `deploy.distill` (:330) joins 'one to one to the build's major forks' on the same missing key. The rationale pointer may resolve to the fork record, so the key is derivable. That softens the consequence to a statement inconsistency: the key named is not among the fields declared. It is not a certain double write. | sound | - |
| 10 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | HEAD flow-steps:213 states the ratification inside `build.distill`'s Then cell ('under `author-owner-ratifies`, the owner's ratification comes first, an owner item'). Its Needs is only `build.core`, while Breakpoints (:240-241) place the ratification 'before `build.distill`'. [rules] (:26) says the Needs column names the items an item waits for, so the wait is stated two ways and missing from the one place the rules read. The finder's claim that the row is appended before the ratification is overstated, since 'comes first' / 'ratified → the row' orders it before the write. The rejected outcome, 'the fork re-classed as not major, kept in the build's records only', has no named writer, however. The fork records are Design's (layer-library:214-215), the command item names no re-class write, and Build's Memory clause (:231-234) lists none. Without that write, the one-to-one join still demands a row for a fork the owner refused. Under the strict preset the reject outcome cannot settle mechanically. | sound | - |
| 11 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:229 | low | low | confirmed | At HEAD, flow-steps:213 has `build.distill`'s route 'held → as `run.on-owner-question` says', and Build's policy list at :229 names `decisions.major` but not `run.on-owner-question`. Plan (:123), Deploy (:368) and Review (:441) all list it. At the base, no Build item routed on that key. The diff added both the route and the `decisions.major` entry and left this key out, so the gap is the diff's own. The effect is limited to one declared list in a design record. | sound | - |
| 12 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:330 | medium | - | refuted | I could not find a reachable path on which the witness goes red with nothing able to repair it. Every path the finder names goes back through Build, and `build.distill` (:213, idempotent, keyed by build and fork) runs again before `build.exit` and adds any missing row in the build's branch. A `test.merge` conflict routes to 'Build for a resolution pass' (:259). A Test route-back or an architect clash re-enters Design or Build. On a race, `deploy.land` refuses back to Test (:327). No Deploy item resolves a fork. A clean merge of an append-only log keeps both sides. Since I could not establish the red case and the finding is graded medium, it is refuted. | sound | - |
| 13 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:212 | medium | medium | confirmed | At HEAD, `build.core` routes clean → `build.distill` → `build.exit` (:212-214), and `build.distill` appends decision-log rows in the build's branch after the core checks have graded the range. Build's exit criterion (:202) is therefore met before that commit is graded. HYGIENE check 27 (memory/HYGIENE.md:531) grades exactly the added decision rows. Before this diff, `build.exit` followed `build.core` directly and no commit came after it. A red would still surface at `test.verdict`, so the effect is contained. | sound | - |
| 14 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:126 | medium | medium | confirmed | In the dClosedLoop records, 'scope tags' are instruction-unit load tags that name steps, items, roles, policies and layers (v2:449, layer-instruction:388/409, flow-steps:40). The research view lists returns by build, date and question (layer-memory:718). The decision row is date, build, decision, rationale pointer and reuse entry (flow-steps:213). Neither carries a scope tag, and nothing defines a plan's scope tags as a selector over them. The layer-library:305 cell was already at the base (base :291), but this diff copied the selector into Plan's Memory clause (:126) and so wired the core read to a key its sources do not hold. | sound | - |
| 15 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:227 | medium | - | refuted | The research-return kind is new in this diff (layer-memory:365; the base list lacks it). But the kinds list declares no selector or field set for any core kind (intake, card, plan, seams and the rest), and layer-library [research-view] says how it is selected: by the writer, since `plan.research` and `design.research` write it. Selector syntax and fields are unit-level detail, which this design-only build leaves to the chain builds by design. The witness's red case (a design record carrying the research binding, presented as a research return) is consistent with a writer-keyed kind. Whether it conflicts with HYGIENE's binding rule cannot be established from the design text. The finding is graded medium and is therefore refuted. | sound | - |
| 16 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:429 | medium | medium | confirmed | At HEAD, flow-steps:429 (`review.dispose`) and layer-library:193 both say an ask that comes from a finding 'is accepted once the class record exists'. layer-memory [asks] :471-472, which this diff left unchanged, still gives that ask the form 'its unit is built, or a review round rules it out', and :474-475 says the core forms are a closed set and 'a new core ask kind adds its form here first'. [rules] (flow-steps :37-38) also says the forms are cited from [asks] and never copied. So one ask now has two acceptances, and the new one was never added to [asks]. Dispose names only the fold's spec writer and the fix unit's builder as writers of the class record. On the ask path no fix unit exists yet, so no item owes the record. The diff introduced this. | sound | - |
| 17 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | high | medium | confirmed | At HEAD, flow-steps:213 and layer-library:219 key `build.distill`'s skip and its 'second row for one key is red' on 'build and fork'. The row's declared fields are date, build, decision, a rationale pointer and a reuse entry (flow-steps:213, layer-library:216-219, layer-memory [decisions] 2). None of them is a fork key. A grep across the build's design records finds fork records described only as option, alternatives and reason, with no fork-id grammar. Today's DECISIONS.md rows carry a per-build sequence id (e.g. TOOL-cSpliceWarden-6), not a fork reference. `deploy.distill` (:330) joins 'one to one to the build's major forks' on the same missing key. The key was introduced by this diff's M5 fix. Graded medium rather than high: this is a missing field in a design record that the chain build would have to add, and nothing ships on it yet. | sound | - |
| 18 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:208 | high | medium | confirmed | At HEAD, the only witness that ties a `new:` slug to an actual class record is `review.fold`'s (flow-steps:430), which runs on unbuilt specs. On built work, `build.unit-pass`'s witness (:208) says only that a fix unit 'carries the class records ... in its write set'. `build.scope` (:210) refuses stray paths and never requires that a listed path was written. `review.dispose`'s witness (:429) joins each slug to 'the item or ask that owes its record', not to the record itself. `review.report`'s `new:` arm (:428) passes while no record holds the slug. So on built work a fix unit that omits the gotcha passes every witness, and an ask's path has no check at all. This is a partial fix of round 1's M3, introduced by this diff. Graded medium: the effect is confined to left-shift record-keeping in a design. | sound | - |
| 19 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:213 | medium | medium | confirmed | At HEAD, `build.distill`'s Does (flow-steps:213) says 'Under `owner-only`, only a fork the owner resolved may be major'. Its witness is only the one-to-one join over declared classes, with no arm that checks the resolver, and no arm that joins a row to a ratification under `author-owner-ratifies`. The rejected outcome, 'the fork re-classed as not major', names no actor and no record. The class lives in Design's fork records (layer-library:214-215), and no Build item rewrites them. So after a rejection the witness still demands a row for that fork. All of this text is new in this diff. The placement mismatch is minor: Breakpoints :240 says 'before build.distill', while the Then cell says the ratification 'comes first'. The missing witness arms are real. | sound | owner-item-without-its-reject-outcome |
| 20 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:330 | medium | - | refuted | The 'stuck' consequence does not follow. [rules] (flow-steps:28-34) gives every refusal a default route: it is recorded, and `next` returns the frontier. It also bounds the loop: once `flow.route-backs` returns run to the same item, 'the loop becomes an owner item, resolved as `run.on-owner-question` says'. A red at `build.distill` therefore escalates to the owner rather than leaving the build stuck. The `deploy.distill` half is pre-existing. At base d4fc4bb (flow-steps:313), `deploy.distill` already had a failable witness ('a join both ways') and its only route was → `deploy.recommend`. This diff did not create that missing red route, and the same [rules] default covers it. | sound | - |
| 21 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:221 | medium | medium | confirmed | At HEAD, layer-library :215-222 says Design writes the fork records and that 'An empty set passes only where no fork was resolved'. The [review-fold] H1 row (:364) repeats that claim. At HEAD, design.decompose (flow-steps :159) says 'feature forks recorded', but its witness is only 'the roster and interface schema check'. design.unit-spec's witness (:162) joins each raised fork to its resolution, but it checks neither the class nor that a fork is recorded at all. build.distill (:213) reads its population from those records. A feature fork that was resolved but never recorded therefore gives an empty set that passes. The fix introduced this text, so the guarantee it states is not backed by any witness, and H1's vacuous-population class is fixed only in part. | sound | - |
| 22 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:208 | medium | medium | confirmed | At HEAD, build.unit-pass's witness column (flow-steps :208) still reads that each unit reuse.propose selects 'carries its reuse line, `proposed <tag>` or `none` with its reason'. That line is the builder's own return, against [rules] :24, 'No witness is typed by the acting agent'. Nothing joins `proposed <tag>` to the proposal filed through the instruction command (layer-library :201-205), and `none` takes any reason. The [review-fold] marks round 1's id 30 as M8 'fixed', but M8 only moves the phrasing to one token (gap-design-05), and M7 only changes the population. Round 1's typed-witness and cannot-fail halves are left standing while marked fixed, which is in scope as a round-1 finding the fix leaves standing. | sound | - |
| 23 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md:151 | medium | low | confirmed | I re-ran the probe at 0dd962724: git grep for '^**Serves:** research' under memory/builds, filtered to names containing 'research' and excluding prompts, gives exactly 59 files in 10 builds. Five of them are *-research-*-instruments.md. The memory one's head says it archives the researchers' probe scripts 'beside the returns', so it is not a return. The figure '59 research returns' at layer-library :151, :249 and :254 and at gap-design-07 therefore overcounts by 5 under a filename selector. The design text (:226-228) does assign returns their own kind, which leaves the defect at a wrong stated count. That effect is contained, so I grade it low. | sound | - |
| 24 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:206 | low | low | confirmed | tools/memory-tree/check-memory-hygiene.sh:2474-2476 admits the substrings 'no existing seam' and 'no seam fits', and 'reuse-first'. I re-measured over memory/builds/*/spec/* at 0dd962724, case-insensitive: 'no existing seam fits' matches 236 specs in 60 builds, the two exact phrases 256 in 67, and 'no existing seam\|no seam fits' 328 in 77. gap-design-05 (gap-register :206), added in this diff, quotes only 236 and 256. Its 'one of two' therefore leaves out about 72 specs that hygiene admits, so the size of the migration it owes is understated. The defect is a figure in a gap row, so I grade it low. | sound | - |
