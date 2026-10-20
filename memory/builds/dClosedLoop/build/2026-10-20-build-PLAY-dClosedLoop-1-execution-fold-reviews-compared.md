# Research: the execution plan's fold, reviewed twice and compared

**Serves:** research PLAY-dClosedLoop-1

Two independent full diff reviews, runs A and B, read the range `fde10e6be` over `8d33694d7`, the fold of the
execution plan's first paired review. This record compares the two runs defect by defect, as the last pair was
compared, and gives each defect its disposition.

## [runs] The two runs

- **Subject:** `fde10e6be` over `8d33694d7`, the fold of the first pair. The range covers:
  - the 36 fold rows of the first pair's comparison record, applied to the plan and its schedule script;
  - the owner's two fork answers, `[answers-4]`;
  - the writer's return and the session log's rows.
- **Harness:** `tools/workflows/tier2-review.js`, a full diff review. Each run had five `gov-diff-reviewer` lenses
  (security, correctness, seams, verification, intent), five `gov-skeptic` batches and one `gov-synthesizer`, every
  role at the owner's medium. The intent inputs were 14 records: the plan, the first pair's comparison record and two
  reports, the execution record, the five returns, the instruments record, v2, final-questions and the gap register.
  `gotchas.py --for-diff` gave the 18-class checklist.
- **Runs and reports:**

  | Run | Dispatch | Workflow | Report |
  |---|---|---|---|
  | A | 226 | `wf_13a913fe-7dc` | `reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-fold-a.md` |
  | B | 227 | `wf_06650e2e-9f6` | `reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-fold-b.md` |

- **The args:** `build_args_fold_review.py` wrote both. The runs differ only in the run label, the report path and the
  scratch path, and they ran one after the other.
- **Independence:** run A's report was moved out of the tree before run B started and restored byte for byte after
  it. The session log took no row for either run until run B had returned.

## [method] How the runs were compared

The last pair's `[method]` applies unchanged
(`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan-reviews-compared.md`). Every finding of both runs,
confirmed or refuted, is placed on the defect it names, and a finding naming two defects lands on both. Where a
skeptic judged a finder's fix unsound, the skeptic's corrected fix folds. Where the reviewers offered two routes, the
`[fold]` row names the one taken and why. A fold does not re-argue an owner answer in the execution record's
`[answers]` to `[answers-4]`. The plan and its schedule script are unchanged between `fde10e6be` and HEAD, so no row
is closed by a later commit.

## [map] Every finding, placed

| Defect | What | A | B | Disposition |
|---|---|---|---|---|
| `pin-check-arm-missing` | P0.3's `--check` (plan:250-252) has no arm comparing a carried instrument pin with the instrument's blob, so under the keep-pins rule ([handoffs] :698-701) a moved instrument can read green; row 10's plant (:148) never re-renders, and no step names who lands a new pin | 20, 23 | 8, 13 | fold: B's skeptic's corrected fix |
| `pin-overclaim` | [handoffs] :701 says "a run that edits an instrument cannot re-pin it away", but the pin sits in the run's own packet (:229), which README rule 7 (:340) lets the run write, against row 10's own "narrows the escape and does not close it" | 1 | 1, 8 | fold: B's skeptic's corrected fix |
| `whole-run-read-as-spec-run` | the extra unit's new spec-run test (:481-483) plus the authored-roster fallback (:492-498) classes dTrueNorth's whole run as a spec run, and :491 dropped the explicit whole-run refusal, so a promoted unit can be carried forward against M4 (:532) | 5, 22 | 19 | fold |
| `marks-arm-two-readings` | README rule 6 (:336-339) and P0.2 (:181-184) require both `widens:` and `relaxes:`, but the validating arm (:204-208) reds only a trailer carrying neither, never says whether `none` is an entry, and rung 5 (:626) and D7 (:1104-1107) list every standing-ruling choice first | 3, 6, 18, 21, 25 | 3, 5, 22 | fold |
| `ruling-list-two-wordings` | README rule 6 (:337) names ER:240, ER:388 and ER:328, while P0.2 (:182) adds P0.8 row 5 | — | 7 | fold |
| `owner-ask-mints-chain-slug` | P0.6 rule 5 (:397-398) mints the owner's ask under the departing build's slug, against rule 2 (:389-390) and rule 4 (:394), so it can collide with that build's live run | 2, 12, 26 | — | fold |
| `owner-ask-reaches-no-packet` | P0.6 rule 5 (:399-400), :534 and [owner] :1033 say the next chain run's packet names an ask filed in dClosedLoop's `BACKLOG.md`, but no P0.3 field, `--check` arm or staleness trigger reads that file | 13, 26 | 24 | fold |
| `field9-records-no-source` | P0.3's acceptance (:257-258) still has field 9 carry "the two owner-approved records its run writes", which no field source names and which do not exist when the packet is rendered | 14 | 24 | fold |
| `outside-paths-range-undefined` | P0.2's `git diff --name-only <base>..HEAD` (:179) and "the build's range" (:205) never define `<base>`, so on the prepared merge they list other builds' landed paths and trailers as this run's | 17 | 2, 9, 12, 21 | fold: B's skeptic's corrected fix |
| `outside-paths-no-product-source` | the outside-paths block (:195) and README rule 7 (:340) exclude "its product paths", which nothing in the plan defines | 4 | — | fold |
| `rule7-forbids-shared-renders` | README rule 7 (:340-342) forbids the `LIVE.md` and ledger re-renders the shared-records rule (:737) has every run write, and the outside-paths block then lists them on every run | 27 | — | fold |
| `once-witness-counts-aborted` | the once-guard's witness (:488-490) reads defer rows from any rotated `RUN.<phase>.<blob8>.md`, an aborted one included, so a re-run spec run is refused its own defers | 7 | — | fold |
| `red-case5-plant-unreachable` | red case 5's plant (:509-511) defers one unit, so `--close` refuses before and after the change for reasons unrelated to the roster fallback and cannot show "carries all its units" | 8, 28 | 14, 25 | fold |
| `fallback-refusals-unplanted` | no red case stages a run-added unit under the authored-roster fallback, so the fallback's split of roster units from added units is never seen | 28 | — | fold |
| `baseline-units-caller-miscited` | the extra unit (:494-495) calls `unattended.sh:13257` "the checker's caller", which is the driver's rescope-add arm; the checker calls at `check-unattended.sh:3907` and the carry-forward close at `unattended.sh:5173` | 19 | 6, 11, 15, 23 | fold: B's skeptic's corrected fix |
| `baseline-units-callers-untested` | the fallback inside `baseline_units` changes check 24's ADD arm and the rescope-add arm too, on non-chain builds as well, and red cases 1-7 exercise neither | — | 11, 15, 23 | fold: B's skeptic's corrected fix |
| `retirement-report-edit-no-route` | the retirement table (:559-567) and [sync-points] (:900, :902) switch what `deviations.py --report` reads, but no step makes that edit, and an edit moves a pinned blob with no re-pin route | 24 | 20 | fold: B's skeptic's corrected fix |
| `deviation-record-shape-stale` | [deviations] "What is recorded where" (:923-925) defines a record by `deviations.py:6-16`'s fields, which lack the bound, tier and surface the validating arm (:206-207) now joins on | 10 | — | fold |
| `schedule-b-claim-phantom-node` | `run()` (schedule.py:267-270) tests `n not in speed`, so under `with_b=False` a node-b claim adds b at full pace and the "a and d alone" figure (:360-361) is a three-node figure | 15, 16 | 4, 17 | fold: B's skeptic's corrected fix |
| `stale-claim-printed-fresh` | a stale claim (schedule.py:157-159) is shown in the table and first wave as a plain start, and the node loop (plan:715-716) starts it fresh, against the take-over rule (:722-725) | — | 10 | fold |
| `unreadable-beat-pinned-untested` | a live claim with a missing or unparseable `beat-utc` (schedule.py:151-156) stays pinned with no reason printed, no docstring line and no P0.4 plant | — | 18 | fold |
| `ordering-plants-cannot-red` | P0.2's ordering red tests (:212-214) plant into the sources, which a correct renderer orders, so the ordering arm is never seen red | — | 16 | fold |
| `surviving-option-misread` | rung 5's "every surviving option passes veto 1" (:621) would leave a mixed fork with no rung | 9 | — | no fold: refuted, veto 1 discards an option before it survives |
| `packet-runs-retired-coverage` | P0.3's packet built from `carries.py`'s `design()` (:225-226) would keep the retired coverage join in service | 11 | — | no fold: refuted, `design()` is the clause parser, not the join |

## [summary] The two runs side by side

```text
$ python compare_rounds.py execution-fold-a.md execution-fold-b.md execution-fold-reviews-compared.md session-log.md wf_13a913fe-7dc wf_06650e2e-9f6
== runs
A: raw 28, confirmed 25, refuted 3, precision 0.89, high findings 3, agents 12, out 159.0k (sum of returned lines)
B: raw 25, confirmed 25, refuted 0, precision 1.00, high findings 3, agents 12, out 159.3k (sum of returned lines)
== defects
map rows 24, confirmed defects 22, refuted-only 2
both 10, A only 6, B only 6
A alone covers 16 of 22 (73%)
B alone covers 16 of 22 (73%)
overlap (Jaccard) 0.45
Chapman estimate of the population: 25.3, so about 3 found by neither
A only: owner-ask-mints-chain-slug, outside-paths-no-product-source, rule7-forbids-shared-renders, once-witness-counts-aborted, fallback-refusals-unplanted, deviation-record-shape-stale
B only: ruling-list-two-wordings, field9-records-no-source, baseline-units-callers-untested, stale-claim-printed-fresh, unreadable-beat-pinned-untested, ordering-plants-cannot-red
== severity (a defect takes its highest confirmed grade per round)
high defects 4: pin-check-arm-missing, whole-run-read-as-spec-run, outside-paths-range-undefined, retirement-report-edit-no-route
  pin-check-arm-missing: A 3 B 2
  whole-run-read-as-spec-run: A 3 B 3
  outside-paths-range-undefined: A 2 B 3
  retirement-report-edit-no-route: A 2 B 3
shared defects graded alike 7 of 10
== lenses behind the defects one round alone found
A: correctness 3, intent 3, security 2
B: verification 3, intent 2, seams 2, correctness 1
== refuted findings and their twins
A9 (surviving-option-misread): confirmed twin none
A11 (packet-runs-retired-coverage): confirmed twin none
A14 (field9-records-no-source): confirmed twin B24
```

## [fold] The fold plan

Six places take more than one fold:
- **The extra unit (phase 1, :478-513)** takes `whole-run-read-as-spec-run`, `once-witness-counts-aborted`,
  `red-case5-plant-unreachable`, `fallback-refusals-unplanted`, `baseline-units-caller-miscited` and
  `baseline-units-callers-untested`. Its red cases become thirteen, numbered as the rows below give them, and 'What the
  pilot proves' item 4 (:542) reads "the carry-forward condition's thirteen red cases".
- **P0.2 (:165-221)** takes `marks-arm-two-readings`, `ruling-list-two-wordings`, `outside-paths-range-undefined`,
  `outside-paths-no-product-source`, `rule7-forbids-shared-renders`, `ordering-plants-cannot-red` and
  `deviation-record-shape-stale`. The block of outside paths is read from one range, minus the run's product paths and
  the named shared renders.
- **P0.3, P0.1 row 10 and [handoffs]** take `pin-check-arm-missing`, `pin-overclaim`, `owner-ask-reaches-no-packet` and
  `field9-records-no-source`.
- **The owner's re-pin command** named under `pin-check-arm-missing` is the one `retirement-report-edit-no-route` uses.
- **P0.6 rule 5 (:395-400)** takes `owner-ask-mints-chain-slug` and `owner-ask-reaches-no-packet`.
- **The schedule script and P0.4's table (:279-290)** take `schedule-b-claim-phantom-node`, `stale-claim-printed-fresh`
  and `unreadable-beat-pinned-untested`.

| Defect | Where it folds |
|---|---|
| `pin-check-arm-missing` | P0.3 (:250-252): `--write` re-renders keeping the instrument pins the packet carries. `--check` gains a pin arm, separate from the byte compare: for each field-1 instrument it compares the pinned blob with `git rev-parse HEAD:<instrument>` and exits 1 on a mismatch, whatever the byte compare says, naming the cause "instrument <path> moved". P0.1 row 10's plant (:148): edit one byte of `carries.py`, make the packet stale by another cause (an `[owed]` line), re-render with pins kept; the pin arm reds while the byte compare stays green. Two controls, each seen green on the same plant: `--check` with the pin arm removed, and a `packet.py` variant whose `--write` re-pins. [handoffs] (:699-701) and [owner] (:1032-1033) name the owner's re-pin step: `packet.py --repin <instrument>`, refused inside a chain run, run by dClosedLoop's session in an owner-asked landing that lands nothing else, recorded as a decision row. Checklist entry: "a guard's plant must exercise the escape the guard names, with a control variant that turns it green". |
| `pin-overclaim` | [handoffs] :701 and 'What nothing catches' (:960-962) read: a pin-keeping re-render cannot re-pin a moved blob away, but a hand edit of the packet's pin line, or of `packet.py`, can; until a chain unit's merge-bar check, the only guard is the owner's landing-diff check. That check, in 'What the owner sees' (:657-660) and [owner] :1032 and :1033, covers every path under `memory/builds/dClosedLoop/build/*.py` and every pin line changed in a `*-packet.md`. [cannot] :1078 adds "a run edits its own packet's pin line". Row 10's plant keeps the re-render scope only. A hand-edited pin is tried once and its result, green, is recorded in that [cannot] row, never planted as a red. Route taken: the reword, not A's route of reading pins from git at the opening landing commit, because `packet.py` itself sits under `memory/` and a run can edit it too. Checklist entry: "a claim must match the row it cites". |
| `whole-run-read-as-spec-run` | The extra unit's spec-run bullet (:481-483): a run is a spec run only when the build's `BACKLOG.md` at the run's baseline commit holds an open ask, which the opening files in every chain build but dTrueNorth (P0.5), and its starting roster has a unit `MISSING`. The ask test applies first and is read at the baseline commit, so an ask the run files itself does not count. :491 reads "a unit added by a build run or a whole run is refused as today: it is built in that run". Red case 8: a whole-run fixture with every authored unit `MISSING` at its start, whose closing review promotes a unit that it then defers, is refused before and after the change. Route taken: the baseline ask, not a README marker, because a new front-matter key would have to be known to dTotalRecall's schema ([sync-points] :897). Checklist entry for `amendment-leaves-its-other-half-standing`: a widened definition gets a red case for every case the old wording excluded. |
| `marks-arm-two-readings` | P0.2's marks (:181-184) and the validating arm (:204-208) state that a `none` value is no entry: only a non-`none` `widens:`, `relaxes:` or `grants:` value orders first or joins a record. The arm exits 1 on: a trailer citing ER:240, ER:388, ER:328 or P0.8 row 5 that lacks either key; one citing ER:388 whose `widens:` is `none`; one citing ER:328 whose `relaxes:` is `none`. Rung 5 (:626-627) and D7 (:1104-1107): a choice that widens a surface or makes a veto-2 change carries `widens:` and is listed first; a goal-bound-only choice carries `widens: none` and is listed with the other forks (ER:284-285). Plants beside :217: `relaxes:` only, red; `widens:` only, red; `widens: none` citing ER:388, red; `widens: none relaxes: none` citing ER:240, green; a rung-6 trailer with `widens: none` and a full `relaxes:` record, green and listed first. 'What nothing catches' (:958-959) names the residual: a veto-3 choice under ER:240 marked `widens: none`, or a choice citing no ruling. An ER:240 trailer marked `none` passes because a goal-bound-only choice is legitimate. Run A's route of redding every ER:240 `widens: none` is not taken. Checklist entry for `policy-value-with-no-route`: every enumerated value of a mark, `none` included, gets a planted case. |
| `ruling-list-two-wordings` | README rule 6 (:337) reads "ER:240, ER:388 or ER:328, or P0.8 row 5", the same set as P0.2 (:182) and the arm under `marks-arm-two-readings`. Checklist entry: "a rule restated in two places drifts". |
| `owner-ask-mints-chain-slug` | P0.6 rule 5 (:397-398): dClosedLoop's session mints the ask under dClosedLoop's slug, as it mints the decision row, and files it as a foreign-ask row with its `SEV` row in the departing build's `BACKLOG.md`, as rule 3 does. ASKS §6 scopes asks-disposed to every ask in that build's `BACKLOG.md`, so it still binds the next close. Route taken: the filer's own slug, not a named exception to rules 2 and 4, because it needs no claim check. Checklist entry for `two-answers-to-one-question`: a new mint route is checked against every mint-authority rule in its section. |
| `owner-ask-reaches-no-packet` | P0.3 field 9 (:244-245) adds every open ask in dClosedLoop's `BACKLOG.md` that names a chain build. `--check` (:250-252) gains an arm requiring each such ask to appear, red on a planted omission. [handoffs]' staleness list (:693-696) gains "an ask lands in dClosedLoop's `BACKLOG.md`". P0.6 rule 5 (:400), :534 and [owner] :1033 cite field 9. Route taken: the packet field, not filing the ask in a named unlanded build. Checklist entry: every "the packet names X" sentence cites a P0.3 field and its `--check` arm. |
| `field9-records-no-source` | P0.3's acceptance (:257-258) drops "and the two owner-approved records its run writes ([deviations])". dTrueNorth's run writes those records after the opening renders the packet, and field 9 already names P0.8 row 1, the row approving the extra unit's record. |
| `outside-paths-range-undefined` | P0.2 defines the range once, beside its sources (:170-179). P is the prepared merge's first parent, the advertised origin/main tip `check_prepared_merge` reads (`tools/push-main.sh:505-538`). Paths come from `git diff --name-only P..HEAD`, which keeps paths written in a conflict resolution. Trailers come from `git log --format=%B P..HEAD`, which gives the run's own commits plus those stacked on the prepared merge. :174-175, :179, :195 and :205 use it. Red plant beside :219: another build lands a path in its own folder and a `Decided:` trailer on origin/main between the run's base and `--prepare`; neither is listed or required, while the run's own write to another build's packet is listed; the plant is seen red against `<base>..HEAD` first. The two spellings the skeptics gave, `T...HEAD` from the advertised tip and `T^1..HEAD` from the prepared merge, name this same set. Checklist entry: "a range on a prepared merge read from the run's base". |
| `outside-paths-no-product-source` | P0.2's sources (:179) and README rule 7 (:340) take a build run's product paths from the `--dispatch --writes` sets its units recorded in `RUN.md`; a spec run has none. Plant: a build-run commit writing a product path outside every recorded `--writes` set is listed. Route taken: the recorded write sets, not paths declared in spec prose, because the driver records them. Checklist entry: every filter the plan names cites its source. |
| `rule7-forbids-shared-renders` | README rule 7 (:340-342) and the outside-paths block (:195-196) exempt the named shared renders, `memory/LIVE.md`, the ledgers and re-rendered generated files ([coordination] :737, :733), and ask rows in dClosedLoop's `BACKLOG.md`. Plant: a `LIVE.md` re-render is not listed, and a write to another build's packet is. Checklist entry: a new write-scope rule is checked against the plan's shared-records rule. |
| `once-witness-counts-aborted` | The witness (:488-490) reads defer rows only from a rotated `RUN.<phase>.<blob8>.md` whose phase is the landed one. Red case 9: a spec run aborted after its defer rows, rotated, then re-run, defers the same units and is carried. Checklist entry: a witness read from rotated records names which phases count. |
| `red-case5-plant-unreachable` | Red case 5's plant (:509-511) follows README rule 1 in full: spec every roster unit, defer each with a `DEFERRED` spec carrying `advances <the opening's ask>` and a defer row, with the ask filed, then run `--close`. Before the change it expects the term-2 message ("the roster this run started with … cannot be read"), naming the units read as added. After it, it expects a met carry-forward term with every unit in `BC_CARRIED`. It is seen red with the fallback removed. A one-unit variant stays only as a separate case with its own stated verdict. Checklist entry: "a fixture red before and after for an unrelated reason"; every red case states its before and after messages. |
| `fallback-refusals-unplanted` | Red case 10: red case 5's fixture plus one unit the spec run added. The spec run carries it as an added unit, not a roster unit, and the build run that then re-defers it is refused. Checklist entry for `staged-break-substitutes-a-synthetic-value`. |
| `baseline-units-caller-miscited` | :494-495 read: the fallback goes inside `baseline_units` (`lib-unattended.sh:1950-2018`), so all three callers take it: `unattended.sh:5173` (the carry-forward close, condition 2), `unattended.sh:13257` (the driver's `--rescope add` arm, fail 48, no fallback commit) and `check-unattended.sh:3907` (check 24, the checker). The sentence states each caller's expected verdict under the fallback. Checklist entry: a cited caller is re-grepped at fold time, never copied from the fold row. |
| `baseline-units-callers-untested` | Red case 5's standing fixture also runs check 24 over the same scratch-clone run and requires it to agree with the driver. Red case 11: check 24 with an empty generated region at base, an authored roster naming units, and one unit added without an `add` row: skipped before the change, fail 24 after. Red case 12: `--rescope --act add` of a unit absent from the authored roster but present in today's generated region: fail 48 "cannot be derived" before, accepted as a LATE record after. Red case 13: a build with an empty generated region and an empty or absent authored roster still skips check 24's ADD arm. Checklist entry: "a shared-function change tested at one caller only". |
| `retirement-report-edit-no-route` | The retirement table's last column (:561-567), for every row whose report reading switches, names the landing and the re-pin. The successor's landing build files an ask in dClosedLoop's `BACKLOG.md` (P0.6 rule 3). Under it, dClosedLoop's session edits `deviations.py --report` to read the successor, or to stop running the retired instrument, and re-pins every packet with `packet.py --repin <instrument>` (`pin-check-arm-missing`). The edit and the re-pin land together in an owner-asked landing that lands nothing else, recorded as a decision row, so no packet goes red between them. [sync-points] :889, :891, :892, :900 and :902 and a new [owner] row name the same step. Checklist entries: every "from then on" switch in a retirement table names its landing and its re-pin step; "a pinned instrument that a later step must edit". |
| `deviation-record-shape-stale` | [deviations] "What is recorded where" (:923-925) names the extra fields in `deviations.py`'s bold-key form: a `relaxes:` record carries `**Bound:**` and `**Tier:**`, and a `widens:` record carries `**Surface:**`, beside `**Reason:**`. The validating arm (:206-207), its red test (:216), the member fields (:191) and README rule 6 (:338) read those exact keys. Checklist entry for `a-folded-field-leaves-its-row-shape-docs-behind`. |
| `schedule-b-claim-phantom-node` | `run()` (schedule.py:263-274): a claim whose node is in `NODES` but absent from `speed` is skipped first, with the note "<build> claimed on <node>, absent from this run: left unpinned". The off-fleet arm then tests `n not in NODES` and never adds a `NODES` member to `speed`. P0.4's table (:279-290) gains: with a fresh `agent5` claim, "a and d alone" equals the run with the claim dropped and is produced by a and d only; the plant is seen red on the current code. Route taken: unpinned, not a hidden `speed['b*']` key, because "a and d alone" is a two-node figure. |
| `stale-claim-printed-fresh` | The script marks a stale build's run "take over (stale)" in its table cell and its first-wave line (schedule.py:315-333), from the stale set `claims()` (:157-159) returns. The node-loop row at plan:715 adds that a run the script prints as stale is taken over under the [coordination] stale-claim rule (:724-725), never started in a fresh worktree. P0.4's stale-beat row (:286) also asserts the first-wave line says take-over. Route taken: marked on the tables, not kept off them, so a node is still offered the take-over. |
| `unreadable-beat-pinned-untested` | `claims()` (schedule.py:151-156) prints "<build> beat unreadable on <node>: kept pinned" in the claims line. The docstring (:19-24) states the case. P0.4's table gains: a cached `live` claim with no `beat-utc` line is pinned and printed with that reason. |
| `ordering-plants-cannot-red` | P0.2's ordering red tests (:212-214) each use a renderer stub that emits the marked choices in source order after a member, as the trailer test (:215) does. Each is seen red with the arm on and green with the arm removed. Route taken: the stub, not a source the renderer misclassifies. Checklist entry: "a validating arm downstream of a correct generator needs a stub to be seen red". |
