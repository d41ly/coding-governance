**Serves:** spec-audit PLAY-dClosedLoop-1

# Tier-2 review, run B: the flow layer's design records for dClosedLoop

Provenance: a Tier-2 spec audit with five lenses (finders gov-spec-reviewer), five skeptic batches (gov-skeptic) and synthesis (gov-synthesizer). It was run on 2026-10-15 as run B of the two independent rounds the owner asked for on layer 2, the flow layer. ROUND 1.

Reviewed: memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md@7031c90f195ce746943196d2dc570b84dd753b63, memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@43e9cf4b27292b535aa24a2680a73cd663a62e34

## Verdict: CLEAN WITH FIXES

No finding is a blocker. Three confirmed findings are high, in three items. One high lets a red that carries the build's own offenders be filed as an ask. One leaves the Design spec audit with no fold, so multi-round rules re-review an unchanged spec. One lets an unattended supervisor self-resolve the owner's landing gate. Fix all three before the records are settled.

Review shape: intensity full, raw 46, confirmed 45, refuted 1, unverified 0 (0 uncertain), precision 0.98.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| reuse | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 43 items, of which 0 are blockers, 3 high, 31 medium and 9 low.

Adjudicated tally by raw confirmed finding: 45 findings, of which 0 are blockers, 3 high, 32 medium and 10 low.

Every confirmed finding keeps its binding grade. Items merge only findings that share a grade: M1 (ids 1, 25) and L2 (ids 9, 46). Where one defect was confirmed at two grades, it appears as two items that point at each other: H1 (id 14) and M2 (id 2), H2 (id 28) and M6 (id 7), M7 (id 10) and L7 (id 26), and M18 (id 22) and L2 (ids 9, 46).

Run integrity:

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdict hygiene: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 43 judged sound, 2 judged UNSOUND (ids 14 and 31, whose corrected fixes are the ones written below), 0 none proposed, 0 not judged.
- Severity: 0 confirmed findings were left ungraded by the skeptic, and 8 were re-graded (ids 1, 5, 9, 34, 35, 38, 41, 46).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 8 spec documents were supplied as `specs`, as sibling context.
- Checklist: 11 items, each assigned to exactly one lens (coherence 3, grounding 2, reuse 2, blast-radius 2, failure-envelope 2).
- By design: the caller's byDesign.
- Move check: no checked subject moved.

The run is complete on these counts.

Findings about this layer's relations to the other layers (H3, M7, M15, M18, M22, M23, L2, L7, L9 among them) are reported as input to the owner's revisit of those relations.

## High

### H1. `test.attribute` files MIXED, CONTENDED and DEAD PROBE reds as asks whatever `verdict.blocks` says (id 14)

- **Where:** flow-steps [test] `test.attribute` Then column; layer-flow [settled] "The bar's labels MIXED, CONTENDED and DEAD PROBE route to asks".
- **What is wrong:** The row routes "inherited, mixed, contended or a dead probe → an ask", keyed on the tester's typed class. In run-gates.sh, MIXED means the run holds offenders not in the base (S(L) not a subset of S(R)), CONTENDED means the leg's ceiling fired, and a DEAD PROBE is read "as not inherited". Only an all-INHERITED red set is landable (`ATTR_LANDABLE`, run-gates.sh:5053-5055). Under strict (`every-red`) and guarded (`own-mixed-contended`), the policy says these reds block, yet the step files them as asks. Under the default `own-only`, routing MIXED and CONTENDED to an ask is the owner's settled T1 answer and is not a defect.
- **Consequence:** Built as written, a red carrying the build's own offenders stops blocking Test. Either the build ships its own regression, or the pre-push hook refuses the non-all-INHERITED red set and `deploy.land` has no route for that refusal.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Route each bar-computed label as `verdict.blocks` says. A label the policy blocks goes to a fix pass in Build, or holds Test's exit. A label it does not block goes to an ask. Key the route on the bar's `GATE_ATTRIBUTE` row, with the tester's class only annotating it. Give `deploy.land` a route for the hook refusing a red set that is not all INHERITED, or make the hook read `verdict.blocks`.
- **Gate:** a staged leg that adds one new offender to an inherited red set, run under guarded. The bar must read it MIXED, and Test must refuse to exit.
- **See also:** M2 (id 2) is the missing route out of Test under the same presets.

### H2. The Design spec audit has no fold, so its round rules re-review an unchanged spec (id 28)

- **Where:** flow-steps [breakpoint] `review.dispose` row; [design] Breakpoints; [open] S-1.
- **What is wrong:** `review.dispose` turns every confirmed finding "into new units or asks", at every breakpoint. At Design the specs are not built, and P19 freezes only built specs. No item amends an unbuilt spec, and `design.ready` derives READY only from MISSING, THIN and FORKED. The fold that does this today (the `disposal` stage in tools/roles/workflows.toml, run by gov-spec-writer, and the fold re-invoke in unattended-build.js) has no item, although layer-roles gives the spec writer "folds".
- **Consequence:** A spec-audit finding becomes a new unit or an ask, and the flawed spec stays as authored. Under strict's `until-no-high` (guarded's is `until-no-blocker`), the next round re-reviews the same spec and finds the same defect. It never terminates, or it reaches the count with the defect still in the spec.
- **Fix (skeptic judged SOUND):** Add a fold path at the Design breakpoint. Either add a `design.fold` item (actor: spec writer, one per affected unit) that amends the unbuilt spec at a new SHA and routes back to `review.pin` for the next round, or make `review.dispose`'s outcome set depend on the breakpoint: fold for unbuilt specs at Design, new units or asks for built work. Name the `disposal` stage and the fold re-invoke args as the carriers it succeeds.
- **Gate:** a fixture spec set with a planted HIGH under `review.design.rounds=until-no-high` must reach a clean round, with the spec's blob changed between rounds.
- **See also:** M6 (id 7) is the same gap seen from the policy reads.

### H3. Owner breakpoints are not kept out of `run.on-owner-question` (id 37)

- **Where:** flow-steps [breakpoint] owner breakpoint; [deploy] `deploy.mandate` and Breakpoints.
- **What is wrong:** flow-steps parks a build at an owner breakpoint "until the owner's disposition is hook-written". The runtime layer, settled later, says the supervisor raises owner items "or resolves them as `run.on-owner-question` says", and that key defaults to best-effort-recorded (v2:490). No flow item has the owner as its actor, so the only owner-disposed things are the breakpoints, and runtime's sentence reads as covering them. Neither record excludes gates. flow-steps also names only a hook as the disposition's writer, and no hook fires in an unattended run.
- **Consequence:** Unattended, under three-gates or every-stage, the supervisor can self-resolve the Plan ratification or the landing gate as best effort and land without the owner.
- **Fix (skeptic judged SOUND):** In [breakpoint], state that an owner breakpoint is never resolved by `run.on-owner-question`, which governs forks and questions only (FR-4). Name the disposition's write path when unattended: a mailbox reply through the guarded command, hook- or CLI-witnessed. Raise this at the layer-relations revisit, so runtime [act] "Owner items" excludes gates.
- **Gate:** an unattended run with `autonomy=three-gates` and `run.on-owner-question=best-effort-recorded`, asserting that `deploy.land` never runs without an owner disposition.

## Medium

### M1. Two shipped presets fail the policy check on a core-only install (ids 1, 25)

- **Where:** flow-steps [consequences] and [deploy] tail (`build.closes`), against v2 [presets].
- **What is wrong:** flow-steps says `build.closes`'s two non-core values "exist only with their expansions, and the policy check refuses them otherwise". v2:688 sets `after-release-verifies` under both strict and guarded. The same holds for the strict and guarded values of the expansion-owned `deploy.promotion`, `deploy.on-verify-fail` and `maintain.*` keys. No absent-expansion fallback exists in the preset preamble or [floor].
- **Consequence:** dDeclaredLoop's preset completeness check and the policy check contradict each other. The check either refuses two of the four shipped presets on a core-only repository, or certifies a value whose engine is not installed.
- **Fix (skeptic judged SOUND, both proposals):** Make expansion-owned preset values fall back to their core value (`at-landing`) when the expansion is absent, or give strict and guarded the core value with an expansion overlay that raises it. Alternatively, have the policy check skip, or resolve with a warning, keys whose owning expansion is not installed. State the rule in [consequences] and fold it into v2 [presets].
- **Gate:** validate each shipped preset against a core-only policy schema.

### M2. Under strict or guarded, a blocking red filed as an ask leaves no route out of Test (id 2)

- **Where:** flow-steps [test] `test.attribute` routes and Exits, against `verdict.blocks`.
- **What is wrong:** Test exits only when no red blocks. `test.attribute` sends inherited, mixed, contended and dead-probe reds to an ask. Under strict (`every-red`) and guarded (`own-mixed-contended`) those reds still block, filing an ask does not clear them, and no resume row is declared.
- **Consequence:** A build with one MIXED or CONTENDED red (or under strict an INHERITED one) sticks at Test, and the engine can only answer stuck. [rules] "every outcome routes" fails.
- **Fix (skeptic judged SOUND):** Make `test.attribute`'s ask routes depend on `verdict.blocks`. A red the active value makes blocking needs a route that can clear it: a fix pass, a new unit, a conflict resolution or an owner breakpoint. Alternatively, state that the ask parks the build and declare the resume row in the build transition table.
- **Gate:** a transition-table check that every Test outcome under every preset reaches an exit or a declared park-and-resume row.
- **See also:** H1 (id 14).

### M3. `test.attribute` hard-codes the red route that `verdict.red-route` governs (id 3)

- **Where:** flow-steps [test] `test.attribute` Then column, against `verdict.red-route`.
- **What is wrong:** The row hard-codes "code misses its spec → a fix pass in Build; spec wrong → a new unit through Design". `verdict.red-route` is in Test's policy list, and strict sets it to `always-new-unit`.
- **Consequence:** An engine built from the table sends a strict build's reds to in-place fix passes, which strict forbids.
- **Fix (skeptic judged SOUND):** State the route as "as `verdict.red-route` says": `fix-pass-or-design` gives today's two routes, and `always-new-unit` sends every own red to a new unit through Design.
- **Gate:** a policy-read check that every item whose policy list names a key branches on it, or carries no hard-coded value of it.

### M4. Several items are unreachable, and no table declares dependencies (id 4)

- **Where:** flow-steps [build] and [test] tables; [breakpoint]; [rules] "every outcome routes".
- **What is wrong:** No route reaches `build.scope`, `build.recommend`, `test.recommend` or `review.cost`. `build.acceptance`'s "the unit built" names no next item; `build.scope` routes "onward"; `test.flakes` and `test.seen-red` route only on a quarantine or a missing record; `review.dispose` routes to "released". layer-flow F-C and the P24 settlement require every item to declare its dependencies and fan-out, and no table carries a depends-on column.
- **Consequence:** The record is the draft dDeclaredLoop declares. Built from it, the engine cannot derive the order of these items, and Test's recommendation and the review it triggers are unreachable.
- **Fix (skeptic judged SOUND):** Add a depends-on column (and fan-out) to every step table. Alternatively, give every outcome an explicit next item, e.g. `build.acceptance` pass → `build.scope`, `build.scope` in scope → `build.recommend`, `test.flakes`/`test.seen-red` done → `test.recommend`.
- **Gate:** a reachability check that every non-entry item is routed to or depended on.

### M5. Step Breakpoints omit the owner gates `autonomy` declares (id 6)

- **Where:** flow-steps [design], [build], [test] Breakpoints; [deploy] Breakpoints.
- **What is wrong:** `autonomy` is the default declaration of owner breakpoints, yet the steps declare them only at `plan.exit` and Deploy. The Design gate ("the design go") under three-gates, and the Design, Build and Test gates under every-stage (strict's value), are missing. [deploy] writes "under `three-gates` and `strict`", mixing an autonomy value with a preset name.
- **Consequence:** A repository on three-gates or strict runs Design, Build and Test without the gates its `autonomy` value promises. A repository setting `autonomy = every-stage` under another preset gets no landing gate.
- **Fix (skeptic judged SOUND):** In each step's Breakpoints line, declare the owner breakpoint `autonomy` puts at the step's exit for each value: plan-only for Plan; three-gates for Plan, Design and Deploy; every-stage for all five. Replace "`strict`" with "`every-stage`".
- **Gate:** a join of v2 [contracts]' gate list per `autonomy` value against the Breakpoints lines.

### M6. The breakpoint program cannot express the Design audit's round rules (id 7)

- **Where:** flow-steps [breakpoint] `review.dispose` and Instruction; [design] Breakpoints.
- **What is wrong:** `review.dispose` only makes new units or asks and loops by `review.follow-up`, a closing-review policy. No item reads `review.design.rounds` or `review.design.round-count`; they appear only in Design's Breakpoints prose. The breakpoint's policy list omits `review.unverified`, which `review.dispose` uses.
- **Consequence:** `until-no-high` (strict) and `until-no-blocker` (guarded) have no mechanism, and the load set for `review.dispose` lacks `review.unverified`.
- **Fix (skeptic judged SOUND):** Make disposal stage-dependent: at Design a confirmed finding sends the unit back to `design.unit-spec` for revision and the next round fires as `review.design.rounds` says; at Build and later findings become new units by `review.findings`. Add `review.design.rounds`, `review.design.round-count` and `review.unverified` to [breakpoint]'s Instruction policies.
- **Gate:** a check that every key a row cites is in its section's policy list.
- **See also:** H2 (id 28).

### M7. layer-flow names the deployer as Deploy's reasoning role, and Build's recommendation has no reasoning (id 10)

- **Where:** layer-flow [settled] Consistency fixes, "The recommendation's reasoning"; flow-steps [build] `build.recommend`.
- **What is wrong:** layer-flow names "the planner, architect, tester or deployer". flow-steps says core Deploy has no role and its recommendation is signals-only. `build.recommend` runs only where the closing review is not owed and carries no reasoning field, though P7 says every transition carries one.
- **Consequence:** Two settled records answer one question differently. dCalibratedLens built from layer-flow would wire a core Deploy role that the roles layer places in integrations, and a Build transition with the closing review owed carries no recommendation.
- **Fix (skeptic judged SOUND):** Amend layer-flow [settled] to name the planner, architect and tester, with Deploy signals-only in the core. In [build], give `build.recommend` the builder's reasoning field and run it on every Build exit, or state that Build is exempt from P7.
- **Gate:** a check that every step exit has a recommendation item.
- **See also:** L7 (id 26).

### M8. Work sent back "as new units through Design" has no Design input kind (id 8)

- **Where:** flow-steps [design] `design.input`; [build] closing review; [breakpoint] `review.dispose`.
- **What is wrong:** `design.input` admits four kinds: plan record, amendment, plan revision and patch. The closing review, `build.core`, `deploy.core` and `test.attribute` all send work back as new units through Design, which is none of them. layer-flow routes landing-review findings by "the entry-point table's post-close row", which flow-steps [entry] does not have.
- **Consequence:** The engine refuses any transition its table lacks, so these paths would be refused.
- **Fix (skeptic judged SOUND):** Add a fifth `design.input` kind, "a new unit from a finding or red", routed to `design.unit-spec`. Declare the Build→Design and Test→Design backward rows. Reconcile the landing-review path with [entry]: add the post-close row, or state that its findings become asks or patch builds.
- **Gate:** a check that every route target names an input kind or row the target step declares.

### M9. `test.verdict` names a hook as the verdict's writer, but no hook fires in Test (id 15)

- **Where:** flow-steps [test] `test.verdict` (actor, Does, Proven by) and the Memory line.
- **What is wrong:** The row reads "the hook writes the verdict for the tree", and [rules] requires a hook-written witness. Test pushes nothing, so pre-push never fires there, and `pre-push --decide` runs no bar. Today run-gates.sh writes the verdict and `gate-full-green`; the hook only reads them.
- **Consequence:** The item cannot be built without a new hook event or a redefinition. Falling back to the runner's own record gives a witness the acting session can rewrite.
- **Fix (skeptic judged SOUND):** State which mechanism writes Test's verdict before any push (a dispatcher-owned post-bar hook, the supervisor running the bar as a command item, or `pre-push --decide`) and which store the acting session cannot write. Alternatively, define the witness as the runner's record re-checked by pre-push at `deploy.land`, and say Test's own exit is not hook-witnessed.
- **Gate:** a check that every witness naming a hook names an event in runtime's enforcement-surface event list.

### M10. "The turnstile" does not serialize landings (id 16)

- **Where:** flow-steps [deploy] `deploy.land` ("the lander, through the turnstile") and the Runtime line ("the turnstile queue").
- **What is wrong:** The turnstile is a host-wide semaphore admitting `slots` concurrent bars (run-gates README:431-446). push-main.sh never takes it; its only lock is the claim-push lock, scoped to one git dir.
- **Consequence:** Concurrent landings across nodes are not ordered by it, so gap-flow-08 is not met by it. Only the non-fast-forward check and the "tip moved → Test" route contain the effect.
- **Fix (skeptic judged SOUND):** Drop "through the turnstile" as the serializer. Name a landing lock or lease that `deploy.land` takes around merge, re-verify and push, scoped to the remote, or state that serialization is the push's fast-forward check plus the tip-moved route.
- **Gate:** two staged landings from two clones against one remote; the second must re-enter Test, never land on a stale verdict.

### M11. The recommendation's reasoning comes from a return that is absent or written before the score (id 17)

- **Where:** flow-steps [rules] "A recommendation is scored by a command…"; [test] `test.recommend`; [plan] `plan.recommend`; [design] `design.recommend`.
- **What is wrong:** The tester acts only in `test.attribute`, which runs only on red, so on green there is no tester return for `test.recommend`. The planner's last act (`plan.record`) and the architect's (`design.decompose`) run before the scoring items, so their reasoning cannot speak to the score or the overlaps found later. layer-roles says with no item there is no role work.
- **Consequence:** The reasoning field is empty or stale, and the review trigger reads it.
- **Fix (skeptic judged SOUND):** Add one reasoning item per step, owned by the producing role and depending on the scoring item. Otherwise declare the recommendation signals-only wherever the role has not acted after the score, which `review.recommendation.source: signals-only` allows. State which applies to green Test.
- **Gate:** a dependency check that each recommendation's reasoning item follows its scoring item.

### M12. Test and Deploy re-specify the landing merge instead of the lander's `--prepare`/`--land` split (id 20)

- **Where:** flow-steps [test] `test.merge`; [deploy] `deploy.current`, `deploy.land`, `deploy.core`.
- **What is wrong:** `test.merge` merges onto the tip and `deploy.land` "merges `--no-ff` and pushes" again. push-main.sh `--prepare` already makes that merge, folding in kit-version mint and regen; `--land` pushes "that prepared merge, and nothing else" and refuses a second stacked merge; and it starts the GATE_POST_MERGE bar.
- **Consequence:** If `test.merge` is a plain merge, the verified tree lacks the mint and regen commits and `deploy.current` never finds the verdict current. If `deploy.land` merges again, push-main refuses it. `deploy.core` duplicates the post-merge bar.
- **Fix (skeptic judged SOUND):** Define `test.merge` as `push-main.sh --prepare --slug <slug>` in Test's worktree, `deploy.land` as `push-main.sh --land` with no second merge, and `deploy.core` as an extension of the GATE_POST_MERGE start, made blocking for the close. Name all three seams in the rows.
- **Gate:** a reuse check that every flow item touching the default branch names its lander seam.

### M13. The reviewer program rebuilds tier2-review.js as separate role acts (id 21)

- **Where:** flow-steps [breakpoint] `review.lens`, `review.refute`, `review.report`, `review.cost`.
- **What is wrong:** These are separate items with actors reviewer, skeptic and synthesizer, plus a cost recorder. The runtime layer, settled later, runs "a review's fan" as one multi-agent harness act, and an act session lives for one act. tier2-review.js already holds the finder, skeptic-batch and synthesis phases and prints agents and out-tokens.
- **Consequence:** A review would cost three bound act sessions and duplicate the harness's orchestration, durability and cost line.
- **Fix (skeptic judged SOUND):** Declare the reviewer breakpoint's work as one role act whose harness is tier2-review.js, with lens set, skeptic batches and synthesis as args and the report as its return. Keep `review.trigger`, `review.pin` and `review.dispose` as command items. Have `review.cost` read the harness's agents and out-tokens fields.
- **Gate:** a matrix check that each harness registered in runtime is the actor of exactly one item.

### M14. Flake quarantine re-invents the bar's nondeterminism record with the opposite meaning (id 23)

- **Where:** flow-steps [test] `test.flakes`; layer-flow [settled] "Flake records are a flow record kind".
- **What is wrong:** `test.flakes` records flakes and quarantines them past a threshold, a quarantine that changes what blocks. The bar already classifies a red-then-green leg as `nondeterministic` and writes `quarantine.<key>`, meaning "never reused until its manifest row changes" (run-gates.sh:5148-5187, :3586).
- **Consequence:** Two detectors and two stores both called quarantine, with opposite effects. Readers cannot tell which is meant, and the flake signal ignores the bar's own classification.
- **Fix (skeptic judged SOUND):** State that `test.flakes` extends the bar's nondeterministic classification as its detection source. Give the flow's blocking exemption a distinct name, or rename one of the two. List the reuse-cache quarantine among the flake record's inputs.
- **Gate:** a lexicon check refusing one term defined with two meanings across the tree and the records.

### M15. Review findings are tagged from a "registered core set" no record defines (id 24)

- **Where:** flow-steps [breakpoint] `review.lens` witness; `review.dispose` (`review.left-shift`); Extension points ("the bug-class catalogue (knowledge)").
- **What is wrong:** Every finding must carry a class from "the registered core set", and left-shift counts by that tag, yet no record defines the set. The existing catalogue, memory/gotchas/ (122 tracked files) rendered by tools/memory-tree/gotchas.py, is demoted to an optional extension, though v2 places "gotchas handed by write set" in core memory.
- **Consequence:** A second class registry is invented, and `review.left-shift: second-occurrence` cannot match a finding to its existing gotcha.
- **Fix (skeptic judged SOUND):** Define the core class set as the gotcha records' ids, or state what the core set is and how it maps to them. Name gotchas.py as the seam the tag is checked against.
- **Gate:** a witness check that every finding's class tag resolves to a gotcha id.

### M16. `placement`'s owner-places and declared-checked values have no item or route (id 29)

- **Where:** flow-steps [entry] `entry.place`; layer-flow [settled] "The placement disposition".
- **What is wrong:** `entry.place` fixes the orientation scout as placer, and [entry] has no policy list. strict sets `placement` to owner-places and guarded to declared-checked. declared-checked's meaning was flagged UNVERIFIED by the item audit and is still unresolved.
- **Consequence:** Under strict the scout still places every request, silently weakening the preset. declared-checked has no defined behaviour.
- **Fix (skeptic judged SOUND):** Add an Instruction list to [entry] reading `placement`, `placement.check` and `kickoff.runs`. Route `entry.place` by value: agent-places returns the scout's disposition; owner-places raises an owner item or breakpoint with the scout's return as evidence; declared-checked gets a defined meaning or is removed.
- **Gate:** a policy-check join of each key's allowed values against the items that read it, which must flag `placement=owner-places` as unreached today.

### M17. Triage can neither refuse nor retire, and nothing selects an ask (id 30)

- **Where:** layer-flow [settled] "Dispositions"; flow-steps [plan] `plan.triage-rule`, `plan.triage-judge`; [open] S-2.
- **What is wrong:** The closed disposition set maps only defer and duplicate; flow.md's "refused as out of scope" is unmapped. Both triage items route only to `plan.record`. S-2 says an ask waits until triage "selects it or retires it", but no item selects or retires, and `plan.input` pins an already-selected ask.
- **Consequence:** Every input reaching triage becomes a drafted plan record. Out-of-scope requests and stale asks cannot be refused or retired, contrary to [how].
- **Fix (skeptic judged SOUND):** Map the retired refuse to a member of the closed set (e.g. `none` with the reason recorded). Give the triage items closed outcomes: select → `plan.record`, defer → ask stays filed, retire → ask closed with its reason. Add or name the selecting item (e.g. kickoff offering the next item, v2 dRankedPlan).
- **Gate:** a fixture ask that fails triage must leave Plan without a plan record.

### M18. gap-flow-10 ignores the existing unattended verbs and names a stale owner (id 22)

- **Where:** layer-flow [uncovered] gap-flow-10; [recommendations] F-E; [settled] "A build ends landed, withdrawn or superseded" and "The register gains five gaps".
- **What is wrong:** gap-flow-10 says the owner has no command to pause, resume or withdraw, and F-E routes these through a new guarded command owned by dDeclaredLoop. unattended.sh already dispatches `--hold`, `--resume` and `--abort` (:14314-14319). The runtime layer says the controls extend those verbs, supersede being new, and moved gap-flow-10 to dWellOiledMachine.
- **Consequence:** A dDeclaredLoop builder would build a fresh control family beside the existing verbs, and believe the gap is theirs.
- **Fix (skeptic judged SOUND):** Reword gap-flow-10 to say pause, resume and withdraw exist only for unattended runs, as `--hold`, `--resume` and `--abort`, with no build-level supersede. Name those verbs as the seam F-E extends. Amend [settled] so gap-flow-10 is owned by dWellOiledMachine.
- **Gate:** a check that every gap's owner in a layer record matches v2's chain row.
- **See also:** L2 (ids 9, 46).

### M19. The one-actor rule is broken in five Actor cells and unchecked (id 31)

- **Where:** flow-steps [rules] "One actor per item"; Actor cells of `entry.intake`, `build.unit-pass`, `build.acceptance`, `build.core`, `test.verdict`.
- **What is wrong:** [rules] says every multi-actor item is split, yet these five cells name two kinds ("command: the prompt-submit hook", builder commits "queued by the executor", "command: the executor", "command: the bar, through the hook"). role_matrix.py fails only on an unmatched cell, never on two kinds.
- **Consequence:** Runtime dispatches by kind (command and executor run, hook awaited), so `entry.intake` and `test.verdict` are ambiguous. The matrix certifies a rule it never tests.
- **Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Make `entry.intake` "hook" (awaited on the prompt event). Keep `test.verdict` "command" (the supervisor runs the bar) and add that its witness is hook-written. Make `build.acceptance` and `build.core` "executor", and `build.unit-pass` "builder", naming the commit queue as runtime machinery. Add to role_matrix.py a failure on any item whose Actor cell names more than one kind.
- **Gate:** that role_matrix.py check, whose seen-red probe runs on today's record and expects exit 1 naming the five items.

### M20. Release notes are placed in distribution, the deployer in integrations (id 32)

- **Where:** flow-steps [deploy] Extension points; [expansions]; [consequences] "Core Deploy has no role".
- **What is wrong:** flow-steps lists "versions and release notes (distribution)" and has the deployer do release notes and verify judgment. layer-roles registers the deployer under integrations alone, acting in release notes, and says an expansion role acts only in its expansion's items.
- **Consequence:** With distribution but not integrations, the release-notes item's only role is unregistered. With both, the roles check refuses the deployer on a distribution item.
- **Fix (skeptic judged SOUND):** Name in [consequences] the expansion that registers the deployer for each duty. Either split the role (a release-notes writer under distribution, the deployer under integrations) or move release notes to integrations in [deploy] and [expansions].
- **Gate:** the matrix check's expansion rule, extended to extension points.

### M21. The prompt-submit hook is load-bearing but absent from runtime's enforcement surface (id 34)

- **Where:** flow-steps [entry] `entry.intake`; [plan] Runtime; [breakpoint] owner breakpoint and `review.trigger`.
- **What is wrong:** The hook carries intake, the mandate, owner dispositions and owner-requested review triggers. Runtime's event list and owner-pack table have no UserPromptSubmit, and its fail-closed invariant does not cover the event. `entry.intake` is typed "command", a kind the supervisor runs.
- **Consequence:** If the hook crashes or is not wired, the prompt passes with no intake entry, the mandate and any breakpoint disposition are lost, and nothing reports it. The effect mostly stalls the flow rather than landing wrongly.
- **Fix (skeptic judged SOUND):** Make `entry.intake` actor kind "hook". State that UserPromptSubmit is a dispatcher event with an owner pack, and give it a row in runtime [enforce]'s cannot-fail-closed table with a witness and a reader: a missing intake entry for an attended prompt is detected at `entry.orient`.
- **Gate:** kill the prompt-submit hook and assert the session refuses to place the request.

### M22. The intake mandate does not bound which sessions' prompts it records (id 35)

- **Where:** flow-steps [entry] `entry.intake`; [plan] Exits; [deploy] `deploy.mandate`.
- **What is wrong:** The hook records "the owner's prompt verbatim" with no rule on which session's prompts count. Act sessions are launched with `claude -p` and supervisor-composed prompts, and `record` has no rule on who may write the intake kind. `deploy.mandate` takes the intake record as landing authority under plan-only. The orientation scout's placement being a bound act of the attended binding narrows the path.
- **Consequence:** A work-order prompt or an agent-written intake entry could become a forged mandate.
- **Fix (skeptic judged SOUND):** Only the prompt-submit hook writes intake, and only in a session whose binding is attended. Act-session and supervisor prompts are refused or recorded as another kind. `record` refuses the intake kind from any other caller. `deploy.mandate` checks the intake entry's binding was attended.
- **Gate:** stage an act session whose prompt contains "build X" and assert no mandate results.

### M23. Owner prompts are committed verbatim with no secret scan (id 36)

- **Where:** flow-steps [entry] `entry.intake`; [plan] Memory.
- **What is wrong:** Intake records hold the owner's words verbatim in the tracked build folder, pinned by SHA in `plan.input`. Neither record mentions secrets or redaction, though tools/runlog/runlog_lib.py ships `scan_secrets` and redaction.
- **Consequence:** A token pasted into a prompt is committed and pushed, contrary to the charter's "keep secrets out of files".
- **Fix (skeptic judged SOUND):** Pass the prompt through runlog's `scan_secrets`/redact (or a shared core copy) before the write; the redacted form is the witness and the redaction count is recorded.
- **Gate:** seed a prompt with a fake AWS key and assert the committed intake entry holds `<redacted:...>`.

### M24. Withdraw, supersede and pause are unspecified for work in flight (id 38)

- **Where:** layer-flow [recommendations] F-E; [settled] "A build ends landed, withdrawn or superseded"; flow-steps [deploy].
- **What is wrong:** The controls are specified only by end effects. Nothing covers running act sessions, unit worktrees, a prepared merge, an open review fan, or a build between `deploy.land`'s push and `deploy.close`. F-D's refusal of undeclared transitions mitigates, but the rows are not designed.
- **Consequence:** A withdraw after the push leaves commits on main, records the build "withdrawn", and has dependents' default `replan` discard landed work. A mid-Build withdraw orphans worktrees and sessions.
- **Fix (skeptic judged SOUND):** Add F-D rows for each control against each state. Withdraw and supersede are refused once the push witness exists, and the build closes as landed. In-flight act sessions are killed with returns persisted, workspaces swept as on release, and a paused build finishes its in-flight item first.
- **Gate:** issue withdraw between the push and `deploy.close` and assert the terminal state is landed.

### M25. `deploy.parents` has no route for a superseded or paused parent (id 39)

- **Where:** flow-steps [deploy] `deploy.parents`; layer-flow [settled] `deps.on-parent-withdrawn`.
- **What is wrong:** `deploy.parents` routes only landed and withdrawn, and the policy covers only withdrawn. Runtime raises `stuck` only with no frontier. (The finder's "read at only one item" clause is overstated: the mailbox is read at every item boundary.)
- **Consequence:** A dependent of a superseded parent holds forever, the defect gap-flow-10 was raised to close. A paused parent holds dependents with no owner item.
- **Fix (skeptic judged SOUND):** Route every state in `deploy.parents`: landed, withdrawn, superseded (follow the replacement's landing), and paused (hold, with an owner item after `leases.expiry-hours`). State in [rules] that a `withdrawn` or `superseded` message read at any boundary triggers the policy at once.
- **Gate:** a transition-table check that every parent terminal and lifecycle state has a dependent route.

### M26. A paused build's leases are neither renewed nor released by rule (id 40)

- **Where:** layer-flow [settled] "The owner pauses, resumes …"; flow-steps [plan] `plan.lease`, [build] `build.unit-lease`.
- **What is wrong:** Pause has no lease clause, and the supervisor expires leases past `leases.expiry-hours` (24, 12 under guarded).
- **Consequence:** Unrenewed, a long pause lets another build take overlapping write sets and resume collides. Renewed, a paused build holds its write sets forever.
- **Fix (skeptic judged SOUND):** Either the supervisor renews a paused build's leases, marked paused on the card, with an owner item past a declared pause ceiling; or they are released on pause and re-taken by compare-and-swap on resume, refusal routed as `leases` says.
- **Gate:** pause a build past the expiry and assert the declared lease outcome.

### M27. Every back-route is unbounded (id 41)

- **Where:** flow-steps [entry] `entry.place`; [plan] `plan.dedupe`; [deploy] `deploy.land`; [test] `test.verdict`; [open] S-1.
- **What is wrong:** A failed `placement.check`, a duplicate from `plan.dedupe`, a stale verdict and a moved tip all route back with no count. `review.design.rounds`' until-* values and `review.follow-up while-finding` have no ceiling. Runtime mints a new instance per route back and answers `stuck` only with no frontier; existing caps bound relaunches, acts and retries, not cycles.
- **Consequence:** An unattended run can loop without end, paying scouts and bar runs, and no owner item is raised.
- **Fix (skeptic judged SOUND):** Add a per-route cycle bound in [rules], a policy key such as `flow.route-cap`, that raises an owner item when reached. Add a round ceiling under every until-* value in S-1. Bound `deploy.land`'s tip-moved route by queue position.
- **Gate:** stage a `placement.check` that always fails and assert an owner item after N cycles.

### M28. `review.unverified=block` has nothing that can unblock (id 42)

- **Where:** flow-steps [open] S-2 `review.unverified`; [breakpoint] `review.dispose`.
- **What is wrong:** An unverified finding's acceptance is that "a review round confirms or refutes it", but no item schedules that round and the owner has no disposition for it. strict sets `block`.
- **Consequence:** Under strict, one inconclusive skeptic verdict blocks the build permanently, short of withdrawal.
- **Fix (skeptic judged SOUND):** Name the unblock route under `block`: a capped re-refute round by a fresh skeptic, then an owner disposition of confirm or refute through the guarded command, recorded as the finding's verdict.
- **Gate:** a fixture with one unverified finding under strict must reach a disposition or an owner item.

### M29. `build.scope=refuse` refuses a commit that already exists (id 43)

- **Where:** flow-steps [build] `build.scope`.
- **What is wrong:** `build.scope` checks history after the commit, and its route "or refused, as `build.scope` says" declares no refuse route, though [rules] and the item audit require one. Runtime's write gate refuses only unowned product code, not paths outside this unit's write set.
- **Consequence:** Under strict, a stray commit wedges the build in a refuse loop over unchanged history, or rides the branch to landing.
- **Fix (skeptic judged SOUND):** Define the refuse route as an executor item that reverts the stray commit or sends a fix pass naming the stray paths. Alternatively, move the refusal before the commit, into the commit queue's write gate.
- **Gate:** stage a commit outside the write set under refuse and assert the branch ends without it.

### M30. A red after the push has no route, and `deploy.close` bundles four effects (id 44)

- **Where:** flow-steps [deploy] `deploy.core` and `deploy.close`.
- **What is wrong:** A red `deploy.core` means the build "cannot close until a new unit fixes it", yet Deploy declares no route to Design or a patch build. `deploy.close` bundles lease release, the `landed` post, the snapshot commit and the transition, with no order or reconcile key, though runtime requires command items to be idempotent or reconcile.
- **Consequence:** A red landed tree sits on main with leases held, while other builds file it as inherited. A partial `deploy.close` re-run finds a half-present witness or double-posts `landed`.
- **Fix (skeptic judged SOUND):** Add a `deploy.core` red route (a patch unit through Design on the same build, or a patch build) and say whether leases are kept. Split `deploy.close` into ordered, individually witnessed items (post `landed`, commit the snapshot, release leases last), or declare its reconcile probe keyed by build and SHA.
- **Gate:** kill `deploy.close` after each effect and assert the re-run converges with one `landed` post.

### M31. `wait-for-expansion` is undefined, and slower test levels have no time bound (id 45)

- **Where:** flow-steps [test] `test.select`; [open] S-3 `tests.without-cadence`.
- **What is wrong:** The key governs only the case where observability's Maintain is absent, and there "wait for the expansion" has no defined behaviour. Under `run-at-landing`, end-to-end and performance levels join every Test run with no timeout; `runtime.act-ceiling` covers acts, not the bar.
- **Consequence:** The levels are either silently never run or Test is held forever. A long bar widens the moved-tip window that feeds M27's loop.
- **Fix (skeptic judged SOUND):** Define `wait-for-expansion` in S-3: unrun levels recorded on the verdict without holding land, or land held with an owner item. Give the selected slower levels a declared timeout whose expiry routes to an ask.
- **Gate:** a policy check that every allowed value has a defined behaviour in the record that declares it.

## Low

### L1. Two item tags are spelled like policy keys (id 5)

- **Where:** flow-steps [build] `build.scope`, [design] `design.reentry`.
- **What is wrong:** Both strings are policy keys and item tags, and rows cite both senses with one string. layer-flow [settled] claimed audit F21 (which named `build.scope`) was fixed. R-B separates the namespaces mechanically, so what remains is prose ambiguity and a lexicon collision.
- **Consequence:** Readers cannot tell which sense is meant, and R-B's lexicon check sees a duplicate name.
- **Fix (skeptic judged SOUND):** Rename the items (e.g. `build.scope-check`, `design.classify`), or require namespace-qualified tags everywhere they are cited.
- **Gate:** a conformance check in dDeclaredLoop refusing an item tag equal to a policy key.

### L2. layer-flow still assigns gap-flow-10 to dDeclaredLoop, and registers two gaps it never states (ids 9, 46)

- **Where:** layer-flow [uncovered] gap-flow-10; [settled] "The register gains five gaps" and Units.
- **What is wrong:** The runtime layer moved gap-flow-10's pause, resume, withdraw and supersede to dWellOiledMachine, keeping only the terminal states in dDeclaredLoop; v2's chain rows agree. gap-flow-13 and gap-flow-14 appear by id only in [settled], their substance only in [audit].
- **Consequence:** A reader of this record puts the owner's controls in dDeclaredLoop. The chain is already correct, so the effect is a stale line in a dated record.
- **Fix (skeptic judged SOUND):** Amend [uncovered] and [settled]: gap-flow-10's controls go to dWellOiledMachine; terminal states, the guarded command and `deps.on-parent-withdrawn` stay with dDeclaredLoop. Add dWellOiledMachine to the Units list or a forward note. Add gap-flow-13 and gap-flow-14 to [uncovered] with their text.
- **Gate:** the gap-owner check of M18.
- **See also:** M18 (id 22).

### L3. gap-flow-12 counts three driver items in [uncovered], four in [audit] (id 11)

- **Where:** layer-flow [uncovered] gap-flow-12.
- **What is wrong:** [uncovered] says "three items" at Plan, Design and Test; [audit] and the gap register list Plan, Design, Test and Deploy.
- **Consequence:** A builder working from [uncovered] would miss Deploy; wording only, since flow-steps makes `deploy.recommend` signals-only.
- **Fix (skeptic judged SOUND):** Change item 3 to four items, or note that the audit widened it.
- **Gate:** a check that a gap's scope in a layer record matches the gap register.

### L4. Breakpoint positions are stated two ways (id 12)

- **Where:** flow-steps [plan], [design], [build] breakpoint positions.
- **What is wrong:** [design] puts the spec audit at `design.exit`, but `design.recommend` routes to it before `design.ready`. [build] puts the closing review "at `build.core`", while `build.recommend` routes to "`build.core`, or the closing review".
- **Consequence:** `review.breakpoints` declarations and the transition table cannot both match the step tables.
- **Fix (skeptic judged SOUND):** Name each default breakpoint's boundary once (e.g. between `design.recommend` and `design.ready`; between `build.recommend` and `build.core`) and make Breakpoints lines match the Then columns.
- **Gate:** a check that each Breakpoints line's position equals a route in its table.

### L5. [design] omits guarded's value for when the spec audit is owed (id 13)

- **Where:** flow-steps [design] Breakpoints.
- **What is wrong:** It says "opt-in by default and owed under `strict`"; v2 sets `review.design` to `owed-above-tier` under guarded.
- **Consequence:** A reader of the step alone treats guarded as opt-in.
- **Fix (skeptic judged SOUND):** Write "opt-in by default, owed under `strict`, owed above the tier under `guarded`", or "as `review.design` says".
- **Gate:** a join of per-preset prose against v2's preset table.

### L6. S-2 types status and severity on the ask row (id 19)

- **Where:** flow-steps [open] S-2 "What an ask is".
- **What is wrong:** Under `BACKLOG_MODE=builds`, this repository's mode, status is folded from disposition rows and severity is a separate `SEV` row (HYGIENE.md:120-122).
- **Consequence:** A builder copying the shape would type status on the row, which HYGIENE forbids.
- **Fix (skeptic judged SOUND):** Restate S-2: an ask row carries its id, filed date, text with evidence and acceptance; status and severity are disposition rows in the same BACKLOG.md, folded into the generated view.
- **Gate:** a hygiene check that record shapes quoted in specs match the live row grammar.

### L7. layer-flow's reasoning roles and [deploy]'s gate condition contradict flow-steps (id 26)

- **Where:** layer-flow [settled] "Consistency fixes", the recommendation's reasoning; flow-steps [deploy] Breakpoints.
- **What is wrong:** layer-flow still names the deployer among the reasoning roles after flow-steps made Deploy signals-only. [deploy] keys the landing gate on "`three-gates` and `strict`", mixing an autonomy value with a preset name.
- **Consequence:** A dCalibratedLens builder following layer-flow routes Deploy's reasoning to a role core Deploy lacks. The [rules] signals-only clause governs behaviour, so the effect is mostly a misleading statement.
- **Fix (skeptic judged SOUND):** Amend the [settled] bullet to "the planner, architect or tester; Deploy is signals-only in the core", and write "under `autonomy` three-gates or every-stage" in [deploy].
- **Gate:** a check that an amendment's sibling statements are swept in the same change.
- **See also:** M7 (id 10) and M5 (id 6).

### L8. `build.scope` names no seam to check 23's write-set grading (id 27)

- **Where:** flow-steps [build] `build.scope`.
- **What is wrong:** check 23 of check-unattended.sh already grades a declared write set against what a pass committed, with exclusions in lib-unattended.sh's `read_brief_paths` and `pass_commit`.
- **Consequence:** A second grader would re-learn the exclusions those functions carry.
- **Fix (skeptic judged SOUND):** Name check 23, `pass_commit` and `read_brief_paths` as the seam `build.scope` generalises from passes to units.
- **Gate:** the reuse check of M12, extended to every history-reading item.

### L9. R-B's example tags and display numbers contradict flow-steps' retired numbers (id 33)

- **Where:** flow-steps head, line 15, "checklist numbers are retired".
- **What is wrong:** layer-instruction R-B keeps numbers as "display order only" (v2:751 agrees) and gives example tags `plan.intake` and `build.unit-commit`, neither of which exists among the defined items.
- **Consequence:** A dOrderedCharter builder registers tags that match no item and keeps a field flow-steps calls retired. Naming only.
- **Fix (skeptic judged SOUND):** State in flow-steps' head that R-B's example tags are superseded (`plan.intake` → `entry.intake`/`plan.input`, `build.unit-commit` → `build.unit-pass`), and whether display numbers survive as order only.
- **Gate:** a check that every item tag cited in any record resolves to a defined item.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=46 confirmed=45 refuted=1 unverified=0 blocker=0 high=3 medium=32 low=10 agents=11 out-tokens=220133

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[consequences] / [deploy] (`build.closes`), against v2 [presets] | high | medium | confirmed | flow-steps.md:321-322 says `build.closes`'s two other values "exist only with their expansions, and the policy check refuses them otherwise". In the working-tree v2, :688 sets `build.closes` to after-release-verifies under strict and guarded, and :685-686 and :690-694 set non-default values for the expansion-owned `deploy.*` and `maintain.*` keys. Neither the preset preamble (:575-590) nor [floor] has an absent-expansion fallback; the grep for 'not installed\|absent\|only with' found none. So on a core-only install the shipped strict and guarded presets fail their own check. The effect is contained: a preset is refused, not a wrong landing. | sound | - |
| 2 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[test] `test.attribute` routes and Exits, against `verdict.blocks` | medium | medium | confirmed | flow-steps.md:194-196 lets Test exit only when 'no red blocks'. :204 sends inherited, mixed, contended and dead-probe reds to an ask. v2 :508 and :667 set `verdict.blocks` to every-red under strict and own-mixed-contended under guarded, so those reds still block. No row clears a red that was filed as an ask, and no resume row is declared. Under those presets the build has no declared route out of Test, contrary to [rules] 'every outcome routes'. | sound | - |
| 3 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[test] `test.attribute` Then column, against `verdict.red-route` | medium | medium | confirmed | flow-steps.md:204 hard-codes 'code misses its spec → a fix pass in Build; spec wrong → a new unit through Design', and :216 lists `verdict.red-route` among Test's policies. v2 :514 and :673 give it always-new-unit under strict. The table never makes the route conditional on that value, so a draft built from it sends strict's reds to fix passes. | sound | - |
| 4 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[build] and [test] tables; [rules] "every outcome routes" | medium | medium | confirmed | I re-read the tables. In build.acceptance (:157), 'the unit built' names no next item. build.scope (:158) routes 'onward', and no row routes to build.scope or build.recommend. test.flakes (:205) and test.seen-red (:206) route only on a quarantine or a missing record, so test.recommend (:207) is never reached. review.dispose (:288) routes to 'released', and review.cost (:289) is never reached. layer-flow F-C (:158-168) and the P24 settlement (:296-297) require every item to declare its dependencies and fan-out, yet [rules] :37 depends on dependency order and no table carries a depends-on column. The record presents itself as dDeclaredLoop's draft (:14). | sound | - |
| 5 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[build] `build.scope`, [design] `design.reentry` | medium | low | confirmed | v2 :521 has the policy key `build.scope` and :433 has `design.reentry`. flow-steps uses both strings as item tags (:158, :111). The rows cite both senses with one string, for example the build.scope row reads 'as `build.scope` says' and the design.reentry row reads 'a `design.reentry` trigger'. F21 (research-flow-items-a :193-195) named build.scope and asked for distinct forms. R-B (layer-instruction :349) does separate the `item` and `policy` namespaces, so the registry can tell them apart mechanically. What remains is prose ambiguity and a lexicon-check collision, which is low. | sound | two-answers-to-one-question |
| 6 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[design], [build], [test] Breakpoints; [deploy] Breakpoints | medium | medium | confirmed | v2 [contracts] :730-734 gives the owner gates under three-gates as plan ratification, 'the design go' and landing authorization. v2 :594 sets strict to every-stage. flow-steps Design Breakpoints (:133-136) names only the spec audit, and Build and Test declare no owner breakpoint under every-stage. deploy.mandate (:242) is keyed on plan-only correctly, but the Breakpoints line :260 says 'under `three-gates` and `strict`', which mixes an autonomy value with a preset name. | sound | - |
| 7 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[breakpoint] `review.dispose` and Instruction; [design] Breakpoints | medium | medium | confirmed | In flow-steps :288, review.dispose only makes new units or asks and loops by `review.follow-up`. No item reads `review.design.rounds` or `review.design.round-count`; they appear only in Design's Breakpoints prose (:135-136), and Design's policy list (:127) has only `review.design`. The breakpoint's policy list (:294) omits `review.unverified`, although :288 uses it. Nothing sends an audited, unbuilt spec back for revision between rounds, so until-no-high and until-no-blocker (v2 :662) have no mechanism. | sound | - |
| 8 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[design] `design.input`; [build] closing review; [breakpoint] `review.dispose` | medium | medium | confirmed | design.input (:99-103, :110) admits four kinds: plan record, amendment, plan revision and patch. Yet the closing review (:165-166), build.core (:160), deploy.core (:245) and test.attribute (:204) all send work back as 'new units through Design', and none of those is one of the four kinds. layer-flow :306-307 routes landing-review findings by 'the entry-point table's post-close row'. A grep for 'post-close' across the build directory finds only that line and a research return, and flow-steps [entry] (:47) has no such row. | sound | - |
| 9 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[uncovered] gap-flow-10; [settled] "The register gains five gaps" and Units | medium | low | confirmed | layer-flow :110 and :317 assign gap-flow-10 to dDeclaredLoop. layer-runtime :874-880 moves gap-flow-10, and the owner's pause, resume, withdraw and supersede, to dWellOiledMachine, and keeps only the terminal states in dDeclaredLoop. v2 :751 (the dDeclaredLoop row) no longer lists gap-flow-10, and :755 (the dWellOiledMachine row) does. The authoritative chain is already correct, so what is left is a stale ownership line in a dated settlement record. | sound | - |
| 10 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[settled] Consistency fixes, "The recommendation's reasoning" | medium | medium | confirmed | layer-flow :300-301 names 'the planner, architect, tester or deployer' as the roles that reason the recommendation. flow-steps :247, :250 and :314 say core Deploy has no role and its recommendation is signals-only, and flow-roles places the deployer only at release and verify. build.recommend (:159) runs only 'where the closing review is not owed' and carries no reasoning field. v2 P7 (:258-261) says every transition carries a recommendation whose reasoning is returned by the step's producing role. | sound | two-answers-to-one-question |
| 11 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[uncovered] gap-flow-12 | low | low | confirmed | At blob 7031c90f, layer-flow.md:120-121 says 'The driver reasons in three items' at 'Plan, Design and Test'. The same record's [audit] at :220-221 says 'Plan, Design, Test and Deploy', and gap-register.md:97 also lists four. [recommendations] at :300 names the deployer too. So the record states the gap's scope two ways. The effect is on wording only, because flow-steps already makes deploy.recommend signals-only. | sound | two-answers-to-one-question |
| 12 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[plan], [design], [build] breakpoint positions | low | low | confirmed | At blob 43e9cf4b, flow-steps.md:118 has design.recommend route 'a review → the Design breakpoint, the spec audit' before design.ready (:119). Yet :133 places 'the spec audit at `design.exit`'. In Build, :159 routes build.recommend to '`build.core`, or the closing review', and :163 says the closing review is 'the breakpoint at `build.core`'. [breakpoint] :274 says a position is one item boundary or a step's exit. So each default breakpoint's position is stated two ways. | sound | - |
| 13 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[design] Breakpoints | low | low | confirmed | flow-steps.md:133 says 'opt-in by default and owed under `strict`'. The v2 preset table, whose header at :592 is velocity \| standard \| strict \| guarded, has at :697 '\| `review.design` \| opt-in \| opt-in \| owed \| owed-above-tier \|'. The guarded value is left out of the step. Test's line at :220 does match `review.test` at v2:699. | sound | two-answers-to-one-question |
| 14 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[test] `test.attribute` Then column; also layer-flow.md [settled] 'The bar's labels MIXED, CONTENDED and DEAD PROBE route to asks' | high | high | confirmed | Re-probed run-gates.sh:4337-4352. Rule 5 is INHERITED only when S(L) ⊆ S(R), so MIXED carries the run's own offenders. CONTENDED means the ceiling fired, and :4360 says a cut run is DEAD PROBE, 'read as not inherited'. :5053-5055 sets ATTR_LANDABLE only when every red leg is INHERITED. flow-steps.md:204 routes 'inherited, mixed, contended or a dead probe → an ask' on the tester's class, whatever `verdict.blocks` says. v2:667 sets `verdict.blocks` to every-red under strict and own-mixed-contended under guarded. Under those presets, the step files as an ask a red the policy says blocks. On any preset, the tree's pre-push refuses a non-all-INHERITED red set, and deploy.land has no route for that refusal. Under the default (own-only), routing MIXED and CONTENDED to an ask is the owner's settled T1 answer (walkthrough:302, 'MIXED and CONTENDED are reported and filed, not blocking'), so that part is not a defect. | unsound | - |
| 15 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[test] `test.verdict` (actor, Does, Proven by) and the Memory line | medium | medium | confirmed | flow-steps.md:203 reads 'the bar, through the hook ... the hook writes the verdict for the tree', and [rules] :20 requires a hook-written witness. Test pushes nothing (deploy.land is the first push), so pre-push never fires in Test. pre-push --decide 'runs no bar either' (pre-push:2091). The bar writes its own verdict files at run-gates.sh:5596-5597 ('gate-full-green'), and the hook only reads them (check_verdict_record, green_candidates). Neither the runtime layer nor flow-steps names a hook event that fires in Test. | sound | - |
| 16 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[deploy] `deploy.land` ('the lander, through the turnstile') and the Runtime line ('the turnstile queue') | medium | medium | confirmed | tools/run-gates/README.md:431-446 says the turnstile admits 'slots' bars per HOST, in ~/.gov/gate-turnstile, shared across repositories. It is a semaphore for bars, not a landing queue. grep for 'turnstile' in push-main.sh finds only the TOOL-aFrugalTurnstile-8 provenance tags (:43, :399) and no use of the turnstile. push-main's only lock is the claim-push lock, scoped to one git dir. So 'through the turnstile' at flow-steps.md:244 and 'the turnstile queue' at :257 do not order landings across nodes, and gap-flow-08 is not met by them. The non-fast-forward check and the 'tip moved → Test' route still contain the effect. | sound | - |
| 17 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[rules] 'A recommendation is scored by a command. Its reasoning is a field in the return of the step's producing role'; [test] `test.recommend`; [plan] `plan.recommend`; [design] `design.recommend` | medium | medium | confirmed | In flow-steps.md, test.attribute (:204), the tester's only item, is entered only on 'red → test.attribute' (:203). On a green verdict, no tester return exists, yet test.recommend (:207) reads 'the tester's reasoning field'. [rules] :35-36 allows signals-only only 'where the step has no such role', and Test does have the tester. In Plan, plan.record (:71) runs before plan.lease and plan.recommend (:74-75). In Design, design.decompose (:114) runs before design.overlaps (:116) and design.recommend (:118), so the reasoning cannot speak to overlaps found later. roles.md:259 says 'With no item, there is no role work.' | sound | - |
| 18 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[build] `build.base`, `build.scope`, `build.core`; [test] `test.merge` conflict route and `test.seen-red` | medium | - | refuted | BY DESIGN: the git shape of each range check is unit-level implementation detail, which the design-only build leaves to each chain build's specs. The subject prescribes no shape. flow-steps.md:154-160 says only 'from history' and 'the build's range', and names neither the frozen-base log shape nor --first-parent. The premise that the resolution pass merges the default branch into the build branch is not stated either: :201 says only 'Build for a resolution pass'. The push-main reconcile cited at :1067 merges onto the default branch at landing, not into the build's range. The trap is a possible implementation choice, not something the spec asks for. | sound | a-merge-of-the-default-branch-read-as-additions |
| 19 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[open] S-2 'What an ask is' ('The row carries: its own id; a status and a severity; ...') | low | low | confirmed | .memory-tree.conf:729 sets BACKLOG_MODE="builds". HYGIENE.md:120-122 says the view's 'status is FOLDED from disposition rows and spec header verbs rather than typed'. memory/builds/aBenchedProbe/BACKLOG.md:4 has the ask row with id, filed date, text, seen and accept. Severity is a separate '- SEV · ...' row (:7) and status a '- CLOSED · ...' row (:8). flow-steps.md:349 says the row carries 'a status and a severity'. | sound | - |
| 20 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[test] test.merge; [deploy] deploy.current, deploy.land, deploy.core | medium | medium | confirmed | flow-steps.md:201 has test.merge merge the build onto the current tip, and :244 has deploy.land 'merges `--no-ff` and pushes', a second merge. deploy.current (:241) compares against 'the prepared merge', and layer-flow.md:36 names the prepared merge as Test's input. Neither record names push-main's --prepare or --land. In the tree, push-main.sh:17-19 has --prepare merge onto the advertised tip and --land 'push that prepared merge, and nothing else'. :26-38 says --prepare folds the mint and regen into the merge. :43-45 says it starts the GATE_POST_MERGE bar. The refusal text in the 500-530 range says 'a second merge stacked on the prepared one' is refused. Built as written, the merge is specified twice and the mint, regen and post-merge seams go unnamed. | sound | - |
| 21 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[breakpoint] review.lens, review.refute, review.report, review.cost | medium | medium | confirmed | Both blobs match the pins. In flow-steps.md:285-289, review.lens, review.refute and review.report are separate items, with the actors reviewer, skeptic and synthesizer, and review.cost is a fourth recorder. The runtime layer, settled later, has a different shape. At layer-runtime.md:484-485 'a review's fan' is one multi-agent harness act run in-session. Its [act] section, at :441, says 'A role act is the roles cycle, in one call', and :476-477 says the act session 'lives for one act'. Read together, each role item becomes its own act, so the review splits into three acts instead of one harness call. I re-ran the tree evidence: tier2-review.js:11-12 holds the Verify (skeptic batches) and Synthesize phases, and :82 already prints agents= and out-tokens=. The flow record names no seam to that harness. The effect is duplicated orchestration and cost, which is contained. The fix is sound: it makes the review harness the actor of one item, the role-act shape runtime [act] already describes. | sound | - |
| 22 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[uncovered] gap-flow-10; [recommendations] F-E; [settled] 'A build ends landed, withdrawn or superseded' and 'The register gains five gaps' | medium | medium | confirmed | layer-flow.md [settled] says 'gap-flow-10, gap-flow-13 and gap-flow-14, owned by dDeclaredLoop'. v2's revision after the runtime layer says dWellOiledMachine takes 'the owner's pause, resume, withdraw and supersede ... with gap-flow-10' from dDeclaredLoop, and v2's chain row for dWellOiledMachine lists gap-flow-10 while dDeclaredLoop's row does not. layer-runtime.md says these controls 'extend unattended's `--hold`, `--resume` and `--abort`; supersede is new'. I re-ran the grep: unattended.sh:14314, :14318 and :14319 dispatch --resume, --abort and --hold. layer-flow names no existing verbs and gives the gap a stale owner. Taken at build level, 'no command to pause ... a build' is partly defensible, but the ownership contradiction holds on its own. | sound | - |
| 23 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[test] test.flakes; layer-flow [settled] 'Flake records are a flow record kind' | medium | medium | confirmed | flow-steps.md:205 has test.flakes 'records flakes, and quarantines them past the threshold', with no seam named. The item audit, research-flow-items-b F-T8, says this quarantine 'changes what blocks'. In the tree, run-gates.sh:5148-5187 and README:351 classify a red-then-green leg as `nondeterministic` and write `quarantine.<key>`, which (run-gates.sh:3586) means 'quarantined until its manifest row changes', so the leg is never reused. The two meanings of quarantine are opposite, and the record names neither the seam nor the distinction. The bar detects nondeterminism only in its reuse sample, so the overlap is partial, but the naming collision and the missing seam are real. | sound | - |
| 24 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[breakpoint] review.lens witness ('a class from the registered core set'); review.dispose (`review.left-shift`); Extension points ('the bug-class catalogue (knowledge)') | medium | medium | confirmed | I grepped every dClosedLoop build record for 'core set' or 'registered class'. The only hits are flow-steps.md:285 and the research proposal F-R2 (research-flow-items-b:182), which proposes 'a registered core set' and defines none. review.dispose counts left-shift by that tag (:288), and :295 demotes 'the bug-class catalogue' to a knowledge extension. In the tree, `git ls-files memory/gotchas \| wc -l` printed 122 and tools/memory-tree/gotchas.py exists. v2's dTotalRecall row places 'gotchas handed by write set' in core memory. So the left-shift counter keys on a class set no record defines, beside an existing catalogue. | sound | - |
| 25 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[consequences] '`build.closes`'s two other values exist only with their expansions, and the policy check refuses them otherwise'; [deploy] tail | medium | medium | confirmed | flow-steps.md:321-322 says `build.closes`'s two other values exist only with their expansions 'and the policy check refuses them otherwise'. v2:688 sets `build.closes` to after-release-verifies for both strict and guarded (column order from :592: velocity, standard, strict, guarded). v2's preset prose at :570-590 overrides only `verdict` for a solo repository and has no core-only override for build.closes. So strict and guarded on a core-only install fail their own policy check. The owner can override the value, so the effect is contained. | sound | - |
| 26 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[settled] 'Consistency fixes', the recommendation's reasoning | low | low | confirmed | The two subjects contradict each other. layer-flow [settled] says the recommendation's reasoning comes from 'the planner, architect, tester or deployer'. flow-steps.md:247 says deploy.recommend is 'signals only, since core Deploy has no producing role', and :250 says 'Roles: none in the core'. flow-steps.md:260 says 'under `three-gates` and `strict`', mixing an autonomy value with a preset name. v2:434 lists the autonomy values, and v2:594 sets strict to every-stage. The [rules] signals-only clause already governs behaviour, so the effect is mostly a misleading statement. | sound | amendment-leaves-its-other-half-standing |
| 27 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[build] build.scope | low | low | confirmed | flow-steps.md:158 defines build.scope with no existing seam named, and no dClosedLoop build record mentions check 23's write-set grading (only the session log and research mention check 23, for other reasons). In the tree, check-unattended.test.sh has a check 23 case grading a declared write set against what the pass committed, and lib-unattended.sh:888 and :932 define read_brief_paths and pass_commit. This is a reuse omission. Its effect is the risk of re-learning the exclusions, so it is low. | sound | - |
| 28 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[breakpoint] `review.dispose` row; [design] Breakpoints; [open] S-1 | high | high | confirmed | flow-steps.md:288 disposes every confirmed finding 'into new units or asks', with no distinction by breakpoint. At Design (:118, :133-136) no item amends an unbuilt spec, and design.ready (:119) derives READY only from MISSING, THIN and FORKED, so a finding never sends a spec back. The sibling flow.md:235 says 'the spec audit is run and folded', and the item audit (research-flow-items-a:57) maps 'Each finding → a spec-writer revision'. P19 freezes only built specs, and layer-roles.md:365 gives the spec writer 'folds'. So the fold was dropped, and multi-round rules (strict's until-no-high; guarded's is until-no-blocker, not until-no-high as the finder says) re-review an unchanged spec. In the tree, unattended-build.js:9 has the Disposal stage and :8 the fold re-invoke, and workflows.toml:37 has disposal = gov-spec-writer. | sound | - |
| 29 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[entry] `entry.place` row; layer-flow [settled] 'The placement disposition' | medium | medium | confirmed | flow-steps.md:47 fixes the actor of entry.place as the orientation scout, and [entry] (:39-52) has no Instruction or policies list, unlike every step section. v2:451 lists `placement` with three values, and v2:611 sets strict to owner-places and guarded to declared-checked. No item or route serves either value. The [rules] clause on routes declared only where a value refuses does not cover a change of actor. research-flow-items-a:204 lists the meaning of declared-checked as UNVERIFIED, and the subjects leave it unresolved. | sound | - |
| 30 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[settled] 'Dispositions'; flow-steps [plan] `plan.triage-rule`, `plan.triage-judge`; flow-steps [open] S-2 | medium | medium | confirmed | layer-flow [settled] maps only defer (to ask) and duplicate (to continue) into the closed set, and leaves flow.md's 'refused as ... out of scope' unmapped. flow-steps.md:69-70 routes plan.triage-rule and plan.triage-judge only to plan.record. S-2 (:354-355) says an ask waits 'until Plan's triage selects it ... or retires it', but no item selects or retires. plan.input (:67) pins an already-selected ask. Sources at :49-52 enter triage directly with no selector. A request at entry could take `none`, but asks, filings and proposals have no refuse or retire outcome. | sound | - |
| 31 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[rules] 'One actor per item'; Actor cells of `entry.intake`, `build.unit-pass`, `build.acceptance`, `build.core`, `test.verdict` | medium | medium | confirmed | I re-read flow-steps.md at blob 43e9cf4. Line 19 says 'One actor per item. Every item the audit found with several actors is split.' Yet line 45 reads 'command: the prompt-submit hook', :156 has a builder whose commits are 'queued by the executor', :157 and :160 read 'command: the executor', and :203 reads 'command: the bar, through the hook'. The roles layer's own derived matrix (layer-roles.md:335-336) lists build.unit-pass, build.acceptance and build.core under both executor and command or builder, and entry.intake and test.verdict under both hook and command. It counts '55 items, 60 actor-item pairs', and its check (role_matrix.py at :898+) fails only on an unmatched cell, never on two kinds, so the rule is unenforced. Runtime [terms] (layer-runtime.md:313) dispatches by kind: command and executor items are run, hook items are awaited. That makes entry.intake and test.verdict ambiguous. build.acceptance and build.core are harmless, because the supervisor runs both kinds. The effect is contained, so medium. | unsound | - |
| 32 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[deploy] Extension points; [expansions]; [consequences] 'Core Deploy has no role' | medium | medium | confirmed | flow-steps.md:262 lists 'versions and release notes (distribution)' as a Deploy extension point. :308-309 groups 'Distribution's and integrations' Deploy extensions: kit versions and release notes'. :314-315 says 'The deployer works only in the expansions: release notes and verify judgment.' The later roles layer, at layer-roles.md:371, registers '\| deployer \| integrations \| release notes; verify dispositions \|'. At :347 it adds 'an expansion role acts only in its expansion's items'. The two records therefore disagree on which expansion owns release-notes work and registers its role. v2:760 puts release notes in dShippedRelease without settling which expansion owns them. Release notes are an extension point here, not a declared item, so the matrix check would not fail today. The disagreement is real but contained: medium. | sound | - |
| 33 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:head, line 15 'checklist numbers are retired' | low | low | confirmed | flow-steps.md:15 says 'checklist numbers are retired'. layer-instruction.md:357-358 (R-B) gives the example tags `plan.intake` and `build.unit-commit` and keeps numbers as 'display order only', and v2:751 agrees ('its number only display order'). Running grep over the build records found those two tags only at layer-instruction.md:357 and in research-flow-items-a.md, the audit's pre-fix names. Neither tag exists among flow-steps' defined items: entry.intake is at :45 and build.unit-pass at :156. The defect is the stale examples plus an unreconciled retired-versus-display-order statement. It affects naming only: low. | sound | - |
| 34 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[entry] entry.intake; [plan] Runtime; [breakpoint] owner breakpoint and review.trigger | high | medium | confirmed | In layer-runtime.md, the event list at :537-543 names PreToolUse and PostToolUse, SessionStart, SubagentStart and SubagentStop, Stop and StopFailure, PreCompact, PostCompact and SessionEnd, and the git hooks. It has no UserPromptSubmit. The owner-pack table at :546-557 has no prompt-submit hook either. Running grep for 'UserPromptSubmit\|prompt-submit' over the runtime record printed nothing, and the same grep over tools/ and skills/ printed nothing. flow-steps nonetheless relies on that hook for entry.intake (:45), the Plan runtime (:88), owner dispositions (:278-279) and review.trigger (:283). flow-roles.md:188 calls it 'load-bearing'. The runtime's fail-closed invariant (:764) does not cover the event. entry.intake is also typed 'command:', a kind the supervisor runs. A missing intake mostly stalls the flow rather than landing wrongly: plan.input and deploy.mandate have no witness to pin. So the consequence is contained: medium, not high. | sound | - |
| 35 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[entry] entry.intake; [plan] Exits; [deploy] deploy.mandate | high | medium | confirmed | flow-steps.md:45 has the hook record 'the owner's prompt verbatim', with no rule on which session's prompts count. deploy.mandate (:242) takes 'the intake record' as the landing authority under plan-only. v2:757 says 'an unattended prompt placed the same way', and the hook writes 'each owner prompt' to 'the session's intake log'. Runtime launches act sessions as `claude -p` with supervisor-composed prompts (layer-runtime.md:371-381). Its SessionStart binding record distinguishes act from attended (:466-468), but nothing makes the intake writer consult it. `record` is the one door (:764), but no rule says who may write the intake kind. The path is narrowed because the orientation scout's placement is 'a bound act of the attended binding' (:471), so an act-session prompt is not obviously placed as a new build. The gap is real but the exploit path is narrow and partly mitigated: medium. | sound | - |
| 36 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[entry] entry.intake; [plan] Memory | medium | medium | confirmed | flow.md:137 places the intake records at Build level, holding 'the owner's words verbatim', inside the tracked build folder. plan.input pins them by SHA (flow-steps.md:67). Running grep -n -i 'secret\|redact' on flow-steps.md and layer-flow.md printed nothing, and the same grep over v2, runtime, flow-roles and layer-memory printed nothing either. The tree already ships tools/runlog/runlog_lib.py:522 'def scan_secrets' and :554 (redaction to '<redacted:<id>>'). The charter (AGENTS.md:39) says 'keep secrets out of files, memory and chat'. A secret pasted into a prompt would be committed and pushed. The effect is contained to that record: medium. | sound | - |
| 37 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[breakpoint] owner breakpoint; [deploy] deploy.mandate and Breakpoints | high | high | confirmed | flow-steps.md:278-279 says 'An owner breakpoint parks the build until the owner's disposition is hook-written.' layer-runtime.md:473-474 says 'Owner items need no session. The supervisor raises them ... or resolves them as `run.on-owner-question` says'. v2:490 sets that key's default to best-effort-recorded. In the derived matrix (layer-roles.md:322-336) no flow item has the owner as its actor. The only owner-disposed things are therefore the breakpoints: the Plan ratification gate and the landing gate under three-gates (:260). That makes runtime's 'owner items' sentence read naturally as covering them. Neither record excludes gates from run.on-owner-question. layer-flow.md:153-154 says only that FR-4's no-park rule 'still governs forks'. flow-steps also names only a hook as the disposition's writer, with no unattended path. The landing gate could be self-resolved on an unattended run: high. | sound | - |
| 38 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[recommendations] F-E; [settled] 'A build ends landed, withdrawn or superseded'; flow-steps [deploy] | high | medium | confirmed | layer-flow.md:178-185 (F-E) specifies a withdrawal only by its end effects: leases released, snapshot committed, `withdrawn` sent. :291-294 settles only the terminal states and deps.on-parent-withdrawn. layer-runtime.md:347-349 says 'The supervisor honours each at its next beat' and nothing more. No record defines the effect on in-flight act sessions, unit worktrees, or a build between deploy.land's push (flow-steps.md:244) and deploy.close (:248). F-D (layer-flow.md:170-176) does make the engine refuse any transition its table lacks, which mitigates the risk. But the table's rows for these controls against each state are not designed, so a post-push withdraw is unspecified. The resulting wrong terminal state is a contained defect on a narrow path: medium. | sound | - |
| 39 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[deploy] deploy.parents; layer-flow [settled] deps.on-parent-withdrawn | medium | medium | confirmed | flow-steps.md:243 routes deploy.parents only on 'landed' and 'a parent withdrawn'. v2:502 has only deps.on-parent-withdrawn. layer-flow F-E (:179-185) gives a superseded build's replacement its kept work, but says nothing of the superseded build's dependents. A paused parent has no route either, and runtime raises `stuck` only with no frontier (layer-runtime.md:332). So the superseded and paused cases hang at deploy.parents. One part of the finding does not hold. The mailbox is read at every item boundary (flow-steps.md:31-32), and F-E says dependents act on `withdrawn` without limiting that to Deploy. So the 'read at only one item' clause is overstated. The superseded and paused gap stands: medium. | sound | - |
| 40 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[settled] 'The owner pauses, resumes ...'; flow-steps [plan] plan.lease, [build] build.unit-lease | medium | medium | confirmed | layer-flow.md:181 and :292 introduce pause and resume with no lease clause. flow-steps' plan.lease (:74) and build.unit-lease (:155) say nothing of pause either. layer-runtime.md:427 has the supervisor expire leases past `leases.expiry-hours`, which v2:443 defaults to 24 (12 under guarded, v2:603). Whether a paused build's leases are renewed or expire is undefined, so it is left to the builder. The effect is contained: medium. | sound | - |
| 41 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[entry] entry.place; [plan] plan.dedupe; [deploy] deploy.land; [test] test.verdict; [open] S-1 | high | medium | confirmed | Re-read flow-steps blob 43e9cf4b. :47 sends a failed check back to `entry.place`, :68 sends a duplicate back to `entry.place`, :203 sends a stale verdict to `test.merge`, and :244 sends a moved tip to Test. None of these routes has a count or a cap. v2:503 lists the `review.design.rounds` values with no ceiling key, and :493 has `review.follow-up while-finding`, which is also open-ended. layer-runtime.md:332 answers `stuck` only when there is no frontier, and :335-342 mints a new instance on each route back ('the flow's loops still loop'). The caps that do exist are `RESUME_ATTEMPTS`, which covers relaunches of one act (:391), `runtime.act-ceiling`, which covers each act, and `roles.retries`. None of them bounds a cycle across items. A grep over the dClosedLoop build records found no route-cap or round-ceiling key. So the claim is true. The consequence is that an unattended run keeps spending scouts and bar runs and never raises an owner item. That is not a wrong result, a security hole or data loss, so I grade it medium. | sound | - |
| 42 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[open] S-2 review.unverified; [breakpoint] review.dispose | medium | medium | confirmed | flow-steps :288 files each unverified finding 'as `review.unverified` says', and :356-357 make its acceptance 'a review round confirms or refutes it'. :375 has strict block, and v2:664 confirms strict=block. No item in [breakpoint] (:281-289) schedules a re-refute round. The owner has no defined disposition for an unverified finding, and the only owner disposition defined is for owner breakpoints (:278). layer-memory.md:381 also says only 'a review round that rules on it'. Under `block`, nothing declared clears the block apart from withdrawing the build. The effect stays within builds run under strict, so medium. | sound | - |
| 43 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[build] build.scope | medium | medium | confirmed | flow-steps :156 commits the pass, then :158 checks the commit's paths from history. Its route reads 'stray → warned with an ask, or refused, as `build.scope` says', which declares no route for refuse. The record's own [rules] (:23-24) promise an explicit route wherever a policy value refuses. The item audit it applies (research-flow-items-a.md:71 'refuse: **no route**', :149 'Add an explicit route only where a policy value refuses: ... `build.scope`') asked for exactly that route, and it was not added. The write gate in runtime (:470-471) refuses only product code that no specced unit owns, not paths outside this unit's write set, so a stray commit can still reach `build.scope`. v2:682 confirms strict=refuse. | sound | - |
| 44 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[deploy] deploy.core and deploy.close | medium | medium | confirmed | flow-steps :245 says a red after the push means 'the build cannot close until a new unit fixes it or it is excepted', and Deploy declares no route to Design or to a patch build. The build sits at Deploy with its leases held, because `deploy.close` (:248) never runs. :248 bundles four effects into one item: lease release, the `landed` post, the snapshot commit and the transition. layer-runtime.md:408-414 requires every command item to be idempotent or to reconcile, with the adapter's witness contract declaring which. The adapter would declare that later, but this bundled item gives no order or key for a partial re-run. The red-route gap stands on its own. | sound | - |
| 45 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:[test] test.select; [open] S-3 tests.without-cadence | medium | medium | confirmed | A grep across memory/builds/dClosedLoop (excluding reviews) finds `wait-for-expansion` only at flow-steps :368 and :371-372 and at v2:506, and none of them defines it. v2:506 scopes the key to 'when observability's Maintain is not installed'. In exactly that case, waiting for the expansion has no defined behaviour: whether the levels are skipped and reported, or Test is held. For the slower levels selected at :202, no timeout is declared in [test]. runtime's `runtime.act-ceiling` covers act sessions, not the bar's command run. | sound | - |
| 46 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md:[settled] 'The register gains five gaps' | medium | low | confirmed | layer-flow blob 7031c90f :317 assigns `gap-flow-10` to dDeclaredLoop. layer-runtime.md:1035 says it 'moved to dWellOiledMachine', and :878-880 keep only its terminal states with dDeclaredLoop. v2:755 lists `gap-flow-10` in the dWellOiledMachine row, so the flow record's statement is stale. The second part of the claim is only partly true. `gap-flow-13` and `gap-flow-14` appear by id only at :317 and are absent from [uncovered] (:107-125, 'Three new gaps'). Their substance is stated in [audit] (:224-243: items with more than one actor, witnesses typed by the acting agent). v2's chain row and runtime are the authority, and both are correct, so the effect is limited to a reader of this record: low. | sound | - |
