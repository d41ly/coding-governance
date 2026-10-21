# Research: the execution plan's review, run twice and compared

**Serves:** research PLAY-dClosedLoop-1

Two independent full diff reviews, runs A and B, read the range `d82cee1a2` over `4592ab001`, which holds the
dClosedLoop execution plan and its schedule script with everything they rest on. This record compares the two runs
defect by defect, as the last pair was compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `d82cee1a2` over `4592ab001`. The range covers:
  - the owner's execution question;
  - the five execution researchers' returns and their instruments, with the main loop's two checks;
  - the owner's three sets of answers;
  - the plan and its schedule script, written and then folded twice.
- **Harness:** `tools/workflows/tier2-review.js`, a full diff review. Each run had five `gov-diff-reviewer` lenses
  (security, correctness, seams, verification, intent), five `gov-skeptic` batches and one `gov-synthesizer`, every
  role at the owner's medium. The intent inputs were 11 records: the plan, the execution record, the five returns, the
  instruments record, v2, final-questions and the gap register. `gotchas.py --for-diff` gave the 18-class checklist.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 222 | `wf_90c57682-307` | `reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-a.md` |
  | B | 223 | `wf_81bf7db4-c19` | `reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-b.md` |

- **The args:** `build_args_plan_review.py` wrote both. The runs differ only in the run label, the report path and the
  scratch path, and they ran one after the other.
- **Independence:** run A's report was moved out of the tree before run B started and restored byte for byte after
  it. The session log took no row for either run until run B had returned.

## [method] How the runs were compared

The last pair's `[method]` applies unchanged
(`build/2026-10-20-build-PLAY-dClosedLoop-1-audit-closing-reviews-compared.md`, itself the parked-debt comparison's
method). Every finding of both runs, confirmed or refuted, is placed on the defect it names, and a finding naming two
defects lands on both. Where a skeptic judged a finder's fix unsound, the skeptic's corrected fix folds. Where the
reviewers offered two routes, the `[fold]` row names the one taken and why. A fold does not re-argue an owner answer
in the execution record's `[answers]`, `[answers-2]` or `[answers-3]`.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `instrument-pin-rerendered` | P0.1 row 10 (plan:137) guards the instruments by a packet pin, but [handoffs] (:585-591) and the spec-run step at :478 tell a run to re-render the packet when an instrument's blob moves, so an edited instrument gets re-pinned and passes | 1 | 1 | fold: B's skeptic's corrected fix |
| `close-cross-build-unrefused` | [handoffs] (:592-593) says `--close` refuses a commit belonging to another build, but fail 66 grades only commits carried through local main, so a run's own writes to another build's folder or to the instruments land unrefused | 2 | — | fold |
| `veto2-fork-unruled` | the fork ladder (:506-525) and "Nothing parks" (:525, :1007) leave out a fork whose only options trip veto 2 outside the grant, and no mark lists a choice the grant lifted | 3 | 3 | fork: does a fork whose only options trip veto 2 outside the grant park, or does the standing ruling take it? |
| `rung5-drops-only` | rung 5 (:518) admits options that "fail veto 3 or the goal bound", dropping ER:240's "only", so an option failing veto 1 as well is taken unmarked | — | 2 | fold |
| `base-roster-unreadable` | the carry-forward term reads the starting roster from the README's generated units region, which names no unit while a build has no spec, so every chain spec run fails `build-complete` at `--close` (plan:409, :271, :481-483) | — | 13 | fold: B's skeptic's corrected fix |
| `once-guard-no-source` | the extra unit's "deferred again: refused" (red case 3, :418) has no cross-run source, since the build run's starting roster already holds the carried unit (:412-413) | 4, 7, 14, 31 | 6 | fold |
| `spec-run-closes-no-unit` | the extra unit defines a spec run as "a run that closes no unit" (:402, :412), which a build run closing nothing also meets, against the README's MISSING rule (:276-279) | 4, 7, 31 | 20 | fold |
| `report-order-unchecked` | P0.2's `--check` only re-renders and compares bytes (:174-175), so a generator that drops a `Decided:` trailer or lists a `widens:`/`relaxes:` choice late stays green, while D10 (:976-977) claims the ordering is covered | 8 | 25 | fold |
| `relaxes-completeness-unchecked` | P0.2's red test for a `relaxes:` record with no tier and no reason (:183) cannot red under a byte compare, and the member fields (:168) have no tier | 26 | 9, 25 | fold |
| `unmarked-ruling-choice` | no arm reds a rung-5 or rung-6 resolution that carries no `widens:` or `relaxes:` mark, so it is not listed first (:175, :180-185, :833) | — | 5, 19 | fold |
| `report-sources-no-arm` | P0.2 names rescope rows and divergence hand-backs as report sources (:155-156), but `deviations.py` reads neither and P0.1 adds no arm or plant for them | — | 18 | fold: B's skeptic's corrected fix |
| `departures-name-collides` | a build's spec run and build run write the same departures report name (:174), so a same-date build run overwrites the spec run's report | 19 | — | fold |
| `report-check-no-caller` | no step after P0.2's own red tests calls `deviations.py --report --check` (:284, :439, :487, :504), so a hand edit of a written report goes unseen | 19 | — | fold |
| `record-step-prose-only` | [deviations] (:814) says a member "recorded by nobody" gets its record before `--close` as a README rule, but no README rule or phase table has that step | 30 | — | fold |
| `report-before-prepare` | the departures report is written before `--prepare` (:439, :487-489, :504), so a reconcile merge adds members after it, against P0.1 row 9's placement on the prepared merge | — | 26 | fold |
| `retirement-misses-report` | the retirement table (:461-467) and sync points (:783, :785) retire the instruments the departures report reads, and :554 gives a third account, leaving the report's later runs undefined | — | 8 | fold |
| `dead-before-truenorth-clauses` | ":485 Before dTrueNorth lands" and ":554 until dTrueNorth lands" can never apply, since Policy J starts no spec run before dTrueNorth lands | — | 11 | fold |
| `disagreement-ask-sink` | instrument/product disagreements go to dTrueNorth's BACKLOG.md (:458), which has no later close to dispose of them | 16 | — | fold |
| `approver-cites-er-line` | deviation record 2 (:845) and dWellOiledMachine's record (:848) name the owner as approver citing ER lines, not the decision id P0.1 row 6 requires | 9, 21 | — | fold |
| `owner-approver-any-row` | P0.1 row 6 (:133) accepts an `owner` approver citing any landed decision row, so a run can label its own departure owner-approved by citing P0.8 row 1 or 5 | — | 4 | fold: B's skeptic's corrected fix |
| `welloiled-in-flight-unapproved` | dWellOiledMachine's row (:848) credits the owner with approving an in-flight test no answer covers, and :782's "under D1's test" points at nothing | — | 24 | fold |
| `owner-reject-no-route` | the owner reads each departures report after its landing (:898-900, :440), but the plan gives no route for the owner's "no" | — | 21 | fold: B's skeptic's corrected fix |
| `override-row-778` | the dKeptSession row (:778) sets both deviation overrides, while `deviation.gate` lands only with dScopedBuild (:785) and the other rows set each at its own key's landing | 32 | 27 | fold |
| `override-after-key-live` | the owner writes each deviation key's chain value only after the landing that adds the key (:775, :785, :902), so that build's own close and runs in flight meanwhile run at `by-risk` and `refuse` | — | 27 | fork: should each deviation key's chain value land in the same landing that adds the key, and who writes it? |
| `opening-gate-constant` | P0.7's gate on `deviations.py` (:337) checks only exit 0, which `--policy report` (:140-142) makes constant | 27 | — | fold |
| `field9-no-source` | P0.3's acceptance (:219-221) has packet field 9 carry the extra unit, its decision row and two records, but no input names them and no arm checks them | 18 | — | fold |
| `bare-id-predicate-grammar` | P0.6's bare-id predicate (:301-303) skips any id after `:`, while the generator joins every `\b`-anchored id but the `missing:` form | 28 | 23 | fold |
| `p08-acceptance-omits-answers3` | P0.8's acceptance (:364) names only ER `[answers]` and `[answers-2]`, while rows 1 and 5 quote `[answers-3]` | 5, 10, 17, 29, 34 | 12, 15, 28 | fold |
| `phase1-precondition-omits-row2` | phase 1's precondition (:425) names decision rows 1 and 3, but dTrueNorth's `may:` line also cites the grant row, row 2 | — | 12 | fold |
| `python-check-cannot-fail` | P0.9's step `bash tools/lib/resolve-python.sh` (:377) only defines a function and exits 0, and the schedule invocations (:231, :602) call a bare `python` | 12 | 10 | fold |
| `fetch-leaves-claim-cache-stale` | :231, :429, :496 and the script's docstring run the schedule after a plain `git fetch`, which never fills the claim cache the script reads | — | 7, 17 | fold |
| `schedule-stale-claim-pinned` | `claims()` (schedule.py:131-150) pins a `live` claim without reading its beat, so a dead holder's run stays pinned to its node and no node is offered it | 11, 15, 24 | 14 | fold |
| `claim-pin-bypasses-spec-only` | `run()` (schedule.py:241) pins a claim's next phase without testing SPEC_ONLY, so a node-b claim can put a build run on b | 23 | — | fold |
| `spec-only-untested` | no P0.4 red test (:240-248) exercises SPEC_ONLY, so a regression of the owner's node-b rule passes every re-run | 25 | — | fold |
| `offfleet-claim-dropped` | `run()` (schedule.py:242) drops a claim from a node outside `speed` (tag c) silently and offers its run to a or d | 22 | — | fold |
| `schedule-extra-doc-stale` | the script's docstring (:3-4, :20-23) and EXTRA comment (:56) describe the extra unit by its `[answers-2]` scope, "review-promoted units" | 13, 20, 35 | 16, 29 | fold |
| `whole-landed-doc-looser` | the docstring (schedule.py:40-41) and P0.4's 'Not checked' (:248-249) say a WHOLE build reads landed once its clauses' specs close, while `tree_state` requires every spec, the extra unit's included | 13 | 22 | fold |
| `shared-path-rate-caveat` | :627's "of 34 unordered build pairs, 3 name a shared path" drops the coordination return's lower-bound caveat | 6 | — | fold |
| `truenorth-extra-cite` | dTrueNorth's `may:` line citing the extra unit's decision row beside the grant row (:266) widens the grant | 33 | — | no fold: refuted, the cite follows the owner's approval of the extra unit |

## [summary] The two runs side by side

```text
$ python compare_rounds.py execution-plan-a.md execution-plan-b.md execution-plan-reviews-compared.md session-log.md wf_90c57682-307 wf_81bf7db4-c19
== runs
A: raw 35, confirmed 31, refuted 4, precision 0.89, high findings 3, agents 12, out 141.7k (sum of returned lines)
B: raw 29, confirmed 27, refuted 2, precision 0.93, high findings 2, agents 12, out 167.5k (sum of returned lines)
== defects
map rows 39, confirmed defects 38, refuted-only 1
both 12, A only 13, B only 13
A alone covers 25 of 38 (66%)
B alone covers 25 of 38 (66%)
overlap (Jaccard) 0.32
Chapman estimate of the population: 51.0, so about 13 found by neither
A only: close-cross-build-unrefused, once-guard-no-source, departures-name-collides, report-check-no-caller, record-step-prose-only, disagreement-ask-sink, approver-cites-er-line, opening-gate-constant, field9-no-source, claim-pin-bypasses-spec-only, spec-only-untested, offfleet-claim-dropped, shared-path-rate-caveat
B only: rung5-drops-only, base-roster-unreadable, unmarked-ruling-choice, report-sources-no-arm, report-before-prepare, retirement-misses-report, dead-before-truenorth-clauses, owner-approver-any-row, welloiled-in-flight-unapproved, owner-reject-no-route, override-after-key-live, phase1-precondition-omits-row2, fetch-leaves-claim-cache-stale
== severity (a defect takes its highest confirmed grade per round)
high defects 5: instrument-pin-rerendered, base-roster-unreadable, once-guard-no-source, spec-run-closes-no-unit, report-order-unchecked
  instrument-pin-rerendered: A 3 B 3
  base-roster-unreadable: A 0 B 3
  once-guard-no-source: A 3 B 0
  spec-run-closes-no-unit: A 3 B 2
  report-order-unchecked: A 3 B 2
shared defects graded alike 10 of 12
== lenses behind the defects one round alone found
A: seams 6, security 3, verification 3, intent 2, correctness 1
B: correctness 4, security 3, intent 3, seams 2, verification 2
== refuted findings and their twins
A7 (once-guard-no-source): confirmed twin A4, A31
A14 (once-guard-no-source): confirmed twin A4, A31
A33 (truenorth-extra-cite): confirmed twin none
A34 (p08-acceptance-omits-answers3): confirmed twin A5, A10, A17, A29, B12, B15, B28
B6 (once-guard-no-source): confirmed twin A4, A31
B19 (unmarked-ruling-choice): confirmed twin B5
```

## [fold] The fold plan

Five places take more than one fold:
- **The extra unit (phase 1, :400-419)** takes `base-roster-unreadable`, `once-guard-no-source` and
  `spec-run-closes-no-unit`. Its red cases become seven, numbered as the rows below give them.
- **P0.2** takes `report-order-unchecked`, `relaxes-completeness-unchecked`, `unmarked-ruling-choice`,
  `report-sources-no-arm`, `departures-name-collides` and `report-check-no-caller`. One validating arm, separate from
  the byte compare, carries the first three.
- **The close sequence** (README rule 4 at :284, phase 1 at :439, the phase-2 tables at :487-489 and :504, and
  [deviations] at :814) takes `record-step-prose-only`, `report-before-prepare` and `report-check-no-caller`. After
  the fold every run does this, in order: after the final successful `--prepare`, on the prepared merge,
  `deviations.py --report <slug>`; then a record for each member listed "recorded by nobody"; then
  `--report <slug> --write` and commit; then `--report <slug> --check`; then `--close`.
- **The approvals table in [deviations] (:842-848) and P0.1 row 6** take `approver-cites-er-line`,
  `owner-approver-any-row` and `welloiled-in-flight-unapproved`. dWellOiledMachine's record leaves the owner-approved
  set, so `owner-approver-any-row`'s list of owner-citable rows does not include it.
- **[handoffs] (:585-593)** takes `instrument-pin-rerendered` and `close-cross-build-unrefused`.

The two forks touch rows that also fold. `rung5-drops-only` follows the answer to `veto2-fork-unruled`, and
`override-row-778` follows the answer to `override-after-key-live`.

| Defect | Where it folds |
|---|---|
| `instrument-pin-rerendered` | [handoffs]: "an instrument's blob moves" leaves the staleness causes (:589). A packet that is red on a moved instrument blob is a stop and is never re-rendered (:591, and the spec-run step at :478). A re-render for any other cause keeps the instrument pins the packet already carries, so a moved blob stays red until the owner lands a new pin. P0.1 row 10 (:137) stops claiming the escape is closed. Its plant edits one byte of `carries.py` on a run branch, follows the plan's recovery step, and sees `packet.py --check` still red. 'What the owner sees' (:551-553) and the [owner] spec-landing and build-landing rows (:899-900) gain one check: any path under `memory/builds/dClosedLoop/build/*.py` in a chain run's diff. 'What nothing catches' (:827-838) gains the same line. [cannot] gains a row saying that no merge-bar check outside `memory/` compares each instrument's blob with its blob at the opening landing commit. It is **Cannot** in phase 0, which writes no product code, and the owner's landing-diff check stands in until a chain unit adds it. Checklist entry: "a guard whose pin is stored in state the guarded actor rewrites". Route taken: B's skeptic's. A's route was `packet.py --check` against `origin/main`, but `packet.py` lives under `memory/`, and a run that edits an instrument can edit it too. |
| `close-cross-build-unrefused` | [handoffs] :592-593: the clause "since `--close` refuses a commit belonging to another build (VERBS:860-862)" becomes "no gate refuses a run's own commit to another build's paths; the README rule forbids it, the departures report lists it, and the closing review reads it". P0.5's build-level rules gain one rule: a run writes under its own `memory/builds/<slug>/` (product paths too, in a build run), and outside it only an ask row in another build's `BACKLOG.md` (P0.6 rule 3). P0.2's report gains a block listing every path the run's range writes outside its own build folder and its product paths, an instrument under `memory/builds/dClosedLoop/build/` included, from `git diff --name-only <base>..HEAD`. Its red test plants a commit writing another build's packet and sees it listed. [cannot]'s "No path exclusion between builds" row (:922) cites that block as the interim check. Route taken: the report's block. A's other route, filing a dPlacedRequest path-exclusion unit, is already in that [cannot] row. |
| `veto2-fork-unruled` | **Fork.** Question: a fork whose only surviving options trip veto 2 outside the grant (a new external dependency or install location, or a governance-carrier or public-surface change that none of the build's own [chain] clauses names) — does it park, or does the standing ruling take it? Option (a): it parks as BUILD-METHOD:91-97 has it, and :525 and :1007 read "nothing parks but an ungranted veto-2 fork". Both runs' fixes take this option. Option (b): the standing ruling reaches it. Rung 5 takes the most capable such option, records it as a departure and marks it `widens: <change>`, so the report lists it first. Option (c): each such fork goes to the owner as a new question while its unit waits. Recommended: (b). Your "nothing is parked or blocked" (ER:103-104) and "Standing ruling" (ER:240) already accept a security surface widened unreviewed and surfaced first, and a veto-2 change would be surfaced the same way. Whichever is chosen, these places name it: [answer] item 2 (:35-49), rungs 3 and 5 (:514-521), :525, D7 (:968-969), [cannot]'s residual-fork row (:943), [disagreements] :1007 and P0.8 row 5. Under every option, a choice that lifts veto 2 through the grant carries `grants: <decision id> <change>` in its §8 mark and `Decided:` trailer. P0.2 lists it beside `widens:` and `relaxes:`, and a P0.2 red test reds a grant-lifted choice the report omits. |
| `rung5-drops-only` | Rung 5 (:518-519) reads "where every surviving option fails ONLY veto 3 or the goal bound, and passes vetoes 1 and 2 as the grant reads them, the run takes the most capable of them". An option that also fails veto 1 goes to rung 6 first. Line 43, D7 (:968) and P0.8 row 5 (:356) carry the same sentence, quoting ER:240's "fails only the security veto or the goal bound". The veto-2 half follows the answer to `veto2-fork-unruled`. Checklist class "two-answers-to-one-question": every restatement of an owner answer is grepped against the ER quote. |
| `base-roster-unreadable` | The extra unit (:400-413) also changes `baseline_units` (`lib-unattended.sh:1950-2018`). When the generated `gen:build-units` region at a spec run's baseline commit names no unit, the starting roster is read from the authored `roster:units` pair at that same commit. The checker's caller at `unattended.sh:13257` takes the same change, so the driver and the checker agree. :409's "The other four terms are unchanged" names this reading as part of the change. Red case 5: a base README with `roster:units` rows and no spec is refused before the change and carries all its units after it. A scratch-clone plant opens one build as P0.5 specifies, preflights it, defers one unit and runs `--close`. It is kept as a standing fixture in the driver's test leg. P0.8 row 1 (:348-350) and deviation record 2's row (:845) name the roster reading as part of the unit. The stub-spec alternative is not taken. |
| `once-guard-no-source` | The extra unit's spec sentence (:412-413) names the witness for "already carried once". The witness is the spec run's add and defer rows, in the same build's rotated `RUN.<phase>.<blob8>.md`, which preflight keeps (PROTOCOL:153-158). At the close, the driver refuses a `DEFERRED` unit that an earlier run of the same build carried, and names that unit. Red case 3 reads: "the build run, with the spec run's `RUN.md` rotated, deferring either carried unit again: refused". Route taken: the rotated `RUN.*.md`. It already holds those rows and P0.2 already reads it, so no new field is needed. A's other route, a `carried-once` marker in the spec header, would add one. |
| `spec-run-closes-no-unit` | The extra unit's condition (:402, :407, :412) identifies a spec run by the README's rule (:276-279): a run whose starting roster, read by `baseline_units` at the run's start, has any unit `MISSING`. "A run that closes no unit" leaves the definition. Red case 6: a build-run fixture that closes zero units and defers a unit it added is refused, before and after the change. Red case 7: a build run that closes no unit and re-defers a unit the spec run carried is refused. 'What the pilot proves' item 4 (:448) reads "the carry-forward condition's seven red cases". |
| `report-order-unchecked` | P0.2 gains a validating arm, separate from the byte compare, that runs under `--write` and `--check`. It parses the rendered report and asserts two things: every `widens:` and `relaxes:` entry (and `grants:`, per `veto2-fork-unruled`) comes before every other entry, and every `Decided:` trailer in the build's range appears. The red tests at :180-182 plant into the sources, not into the written report: a fixture whose sources render a `widens:` choice after a member, and a renderer that drops a trailer, each seen red. The byte compare keeps only the hand-edit test (:185). D10 (:976-977) says that the validating arm covers the ordering. Checklist entry: "a check defined as re-render and compare cannot red a defect of the renderer". |
| `relaxes-completeness-unchecked` | P0.2's member fields (:168-169) gain `tier:` and the dropped bound. The validating arm exits 1, under both `--write` and `--check`, on a `relaxes:` mark that joins no record carrying the bound, `tier:` and `reason:`. It does the same for a `widens:` mark whose record names no surface or reason. The red test at :183-184 plants the incomplete record in the sources and sees exit 1. |
| `unmarked-ruling-choice` | README rule 6 (:286-288) and rungs 5 and 6 require every resolution under either rung to declare itself. Its `Decided:` trailer cites ER:240 or ER:328 (or P0.8 row 5) and carries both `widens: <surface>\|none` and `relaxes: <bound>\|none`. The validating arm reds a trailer that cites the standing ruling but carries neither key. Plant: such a trailer, seen red. 'What nothing catches' (:833-835) then names only a choice that cites no ruling at all. |
| `report-sources-no-arm` | P0.1 gains a population arm for rescope `add`, `retire` and `supersede` rows, read from `RUN.md` and every rotated `RUN.*.md`, and a second arm for divergence hand-backs. The planned `defer` rows a spec run writes for its own roster units are excluded. Plants: an add row with no record is listed as unjoined, and so is a hand-back with no record, while a spec run's routine defer rows are not listed. P0.2's acceptance (:177) requires those plants. Checklist entry: "every source a report names has an arm and a plant in its acceptance". |
| `departures-name-collides` | P0.2 (:174): the report's name carries the run kind, `<date>-build-<first unit>-departures-spec.md` for a spec run and `-departures-build.md` for a build run or dTrueNorth's whole run. README rule 4 and the phase tables use the same names. |
| `report-check-no-caller` | README rule 4 (:284), phase 1 (:439) and both phase-2 tables (:487, :504) call `deviations.py --report <slug> --check` after the `--write` commit and before `--close`, in the close sequence above. |
| `record-step-prose-only` | README rule 4 (:284), phase 1 (:439) and both phase-2 tables (:487-489, :504) gain the step [deviations] (:814) describes, in the close sequence above: a record for each member that `--report <slug>` lists as "recorded by nobody", written before `--write`. P0.2 gains a red test: a report written before a member's record is added fails `--check`. |
| `report-before-prepare` | The close sequence above moves after the final successful `--prepare`, on the prepared merge. README rule 4 states that order, and the reconcile step at :619-620 runs the sequence again after any reconcile. `check_prepared_merge` (`tools/push-main.sh:505-538`) accepts single-parent commits stacked after the prepared merge, so the report commit does not invalidate it. [cannot]'s departures-report row (:944) adds that nothing checks the report's base against the final prepared merge until the landing record (`cl-dClosedLoop-0413`). Route taken: move the sequence after the final `--prepare` rather than re-run it after a reconcile, because P0.1 row 9 already places the instruments on the prepared merge. |
| `retirement-misses-report` | The retirement table (:461-467) gains rows for the departures report (P0.2), the packet's instrument pins (P0.1 row 10, P0.3 field 1) and README rule 4. For each retired instrument it states what the report reads instead: the README's coverage region for `carries.py`, the product as-built view for `asbuilt.py`, and `deviation.gate`'s output for the join. Where nothing replaces a reading, it states that the report mode outlives the join. :554 and [sync-points] :783 and :785 are made to agree with the table. The inventory is taken by value, by grepping every plan line that names `carries.py`, `asbuilt.py` or `deviations.py`. Checklist class "retirement-inventory-misses-readers-by-value". |
| `dead-before-truenorth-clauses` | :485 drops "Before dTrueNorth lands, `deviations.py` too". :554's "until dTrueNorth lands" is restated under `retirement-misses-report`'s row. |
| `disagreement-ask-sink` | :457-458: a disagreement between an instrument and the product becomes an ask in the `BACKLOG.md` of the build that lands that instrument's successor in the retirement table: dOrderedCharter, dDeclaredLoop, dIndexedDesign or dScopedBuild. That build's next close disposes of it (ASKS:128-143). [coordination]'s ask rule (:629-631) adds that an ask may be filed only in a build whose build run has not landed. Route taken: the successor build, not the departures report's first block, because only a later close grades an ask, and the successor has not landed while its instrument still runs. Checklist entry: "an ask routed to a build with no later close". |
| `approver-cites-er-line` | Deviation record 2's approver (:845) reads "owner, citing ER:232, ER:320 and P0.8's row 1". [defaults]' "two records' placement and wording" (:978-980) reads "naming the owner as approver and citing the decision row that records the answer, as P0.1 row 6 requires". P0.1 row 6 gains the plant "an owner approver citing only an ER line: red". dWellOiledMachine's record (:848) folds under `welloiled-in-flight-unapproved`. |
| `owner-approver-any-row` | P0.1 row 6 (:133) accepts `owner` only when the cited decision row names this record's own departure: row 3 for the `cl-dClosedLoop-0004` record, row 1 only for the extra unit's deviation-2 record, row 6 for dPlacedRequest's, or a row naming the record's Departs-from clause id. An `owner` record citing row 5, or citing row 1 for any later added unit, reds. [deviations] :846 says that a later departure's approver is the run's author role, citing the ruling, never `owner`. Plants in `deviations.py --fixture`: an owner approver citing row 5 reds, and one citing row 1 for a unit a spec run added reds. |
| `welloiled-in-flight-unapproved` | dWellOiledMachine's in-flight test (:848) leaves the owner-approved table. Its spec run records it as a stricter departure from `cl-dClosedLoop-0306`, with the run's author role as approver under `author-recorded`, citing P0.8 row 6 as the ruling it serves. [sync-points] :782's "under D1's test" becomes "under the in-flight test its spec carries". Route taken: `author-recorded` rather than a new owner question, because the departure is stricter and the chain's approval value needs no owner turn (ER:103-104). Checklist class "amendment-leaves-its-other-half-standing": after a fold, grep the plan for every term a dropped option introduced. |
| `owner-reject-no-route` | [owner]'s rows at :898-900 and phase 1's owner row (:440) gain the outcome of a "no". An owner's "no" to a listed departure becomes an ask, minted under the departing build's own slug and filed in that build's `BACKLOG.md` with its `SEV` row. If that build's build run has already landed, the ask goes in dClosedLoop's `BACKLOG.md` under dClosedLoop's slug, and the next chain run's packet names it. P0.6's minting rules (:320-330) gain this case. The plan names the decision row that supersedes the P0.8 row-5 choice being rejected. Checklist class "owner-item-without-its-reject-outcome". |
| `override-row-778` | The dKeptSession row (:778) says only that named presets make an override on `standard` expressible, and that the `author-recorded` value already set at dDeclaredLoop is carried as that override. The `report` override waits for `deviation.gate` at dScopedBuild (:785). Its timing follows the answer to `override-after-key-live`. Checklist entry: "a sync-point row restating a step another row owns". |
| `override-after-key-live` | **Fork.** Question: `deviation.approval` (dDeclaredLoop) and `deviation.gate` (dScopedBuild) go live at `standard`'s `by-risk` and `refuse` in the landing that adds them, before you write the chain's value. Should the chain's value land in that same landing, and who writes it? Option (a): the build that adds each key writes the chain's value in its own landing, its spec carrying it under P0.8 row 3 and recording it as a departure. Option (b): you write the value through the guarded command on that build's branch before its landing, so the run waits on you once. Recommended: (a). Row 3 already records your approval of `report` and `author-recorded` for every run (ER:189), and nothing then waits on you. Whichever is chosen, [sync-points] :775 and :785, [owner] :902 and P0.8 row 3 state it, and so does `override-row-778`'s row. Checklist class "policy-value-with-no-route": every key a chain build adds has a stated route for its chain value at that landing. |
| `opening-gate-constant` | P0.7's gate row (:337) asserts that `deviations.py` prints 0 members, as P0.1's acceptance (:146) names, not just exit 0. Phase 1's by-hand run at dTrueNorth's Design exit (:436) runs `deviations.py --policy refuse`, which exits 1 on an unjoined member or an approver below its risk. `report` stays the chain runs' value. Route taken: a member count at P0.7, because `refuse` exits 1 only on findings and would pass joined members, and `refuse` at the Design exit, where dTrueNorth's own records make members expected. Checklist entry: "a gate's exit code made constant by a default set in the same phase". |
| `field9-no-source` | P0.3 (:189-190) names field 9's further source: the opened README's roster units, `**Derived:**` ones included, and P0.8 row 1's id. `--check` (:213-215) gains an arm requiring every roster unit to appear in the packet, red on a planted omission. |
| `bare-id-predicate-grammar` | P0.6's predicate (:301-303) is replaced by the generator's own grammar: `tree_lib.scan_missing_citations` with `gen_build_index.build_roster_id_re` and `extract_roster_ids`, run over the tracked files under `memory/` and filtered to the 22 chain slugs. P0.6's red test (:318) gains the plant `x:missing:TOOL-dTrueNorth-1`, which must print one line. P0.7's gate row (:337) names the new predicate. |
| `p08-acceptance-omits-answers3` | P0.8's acceptance (:364) reads "in ER `[answers]`, `[answers-2]` or `[answers-3]`". Checklist class "amendment-leaves-its-other-half-standing". |
| `phase1-precondition-omits-row2` | Phase 1's precondition (:425) reads "the three decision rows dTrueNorth reads (P0.8 rows 1, 2 and 3)". |
| `python-check-cannot-fail` | P0.9's row (:377) reads `. tools/lib/resolve-python.sh && PY=$(resolve_python) && "$PY" --version`, and it requires a non-empty launcher. Every schedule invocation (:231, :602, and the script's usage line) reads `"$PY" <script>`. P0.9's red test gains: the step is seen red with every Python stripped from PATH. |
| `fetch-leaves-claim-cache-stale` | :231, :429 and :496, and the script's usage line (schedule.py:6), read `git fetch; bash tools/unattended/unattended.sh --claims; "$PY" <script> --ref origin/main`. |
| `schedule-stale-claim-pinned` | `claims()` (schedule.py:131-150) reads each claim's `beat-utc` and applies RESUME_STALE_BOUND, read from `.unattended.conf` rather than typed. A claim whose beat is past the bound prints "stale on <node>: take over per [coordination]" and is not pinned. P0.4's red-test table (:240-246) gains: a cached `live` claim whose beat is older than 5400 s is reported stale and left unpinned. Route taken: the bound applied in the script, not the verdict column of `--claims`, so the script stays a reader of refs and files. |
| `claim-pin-bypasses-spec-only` | `run()` (schedule.py:236-243) pins a claim on a SPEC_ONLY node only to a spec run. Otherwise it prints the claim and leaves it unpinned. P0.4's table gains: a live `agent5` claim on a build whose specs read done puts no build run on b. Route taken: unpinned, not exit 1, because exit 1 would deny every node its table during a b spec run's normal window between `--land` and `--landed`. |
| `spec-only-untested` | P0.4's red-test table (:240-246) gains a plant run with `--b 0.5`. It asserts that b's lines name no build run, and that with the SPEC_ONLY filter at schedule.py:204 removed they name one. Route taken: the plant, not only an exit-1 self-check, because a self-check that reads SPEC_ONLY goes silent along with the set it guards. |
| `offfleet-claim-dropped` | `run()` (schedule.py:242) treats a claim whose node is outside `speed` as removing that run from dispatch, and prints "held off-fleet on <tag>". P0.4's table gains a plant with a tag-c claim. |
| `schedule-extra-doc-stale` | The docstring (schedule.py:3-4, :20-23) and the EXTRA comment (:56) read "the carry-forward condition for any unit a spec run adds, from a review or a discovery (`[answers-2]` item 5, widened by `[answers-3]` item 1, ER:320)", and the docstring's sources line names `[answers-3]`. |
| `whole-landed-doc-looser` | The docstring (schedule.py:40-41) and P0.4's 'Not checked' (:248-249) state the rule as `tree_state` (:118) applies it: a build is done only when every spec in its folder, the extra unit's included, is CLOSED or WONTDO. P0.4's table gains a plant: six clauses CLOSED and the extra unit's spec OPEN leave dTrueNorth not done. |
| `shared-path-rate-caveat` | :627 reads "Of the 34 build pairs the chain does not order, at least 3 name a shared path in v2 (a lower bound: rows mostly name keys, not files; coordination return, §2)". |
