**Serves:** diff-review PLAY-dClosedLoop-1

# Tier-2 review: the dClosedLoop execution plan and its schedule script (run A of two)

Reviewed by five finder lenses and five skeptic batches. Synthesis by gov-synthesizer. Round 1.

Range: 4592ab001272de0f7aacfbee4b625bd03e9041d4...d82cee1a2e7ca76ca9304e706088474fbf9346cd

## Verdict: CLEAN WITH FIXES

No blocker survived the skeptics, so the plan's structure holds and the fixes below can be made in place. Three high items must be fixed before phase 0 opens: the instrument blob pin, the byte-compare `--check`, and the extra unit's "once" guard. Each of the three would leave a check certifying something it does not check.

## Review shape

Intensity full, raw 35, confirmed 31, refuted 4, unverified 0 (0 uncertain), precision 0.89.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 7 | 6 | 1 | 0 | 0 | 0.86 |
| seams | yes | 9 | 8 | 1 | 0 | 0 | 0.89 |
| verification | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| intent | yes | 6 | 4 | 2 | 0 | 0 | 0.67 |

The adjudicated tally by item is 0 blocker, 3 high, 13 medium and 8 low, for 24 items. By raw confirmed finding it is 0 blocker, 3 high, 15 medium and 13 low, for 31 findings. Some items merge several findings.

Run integrity:
- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 31 judged sound, 0 judged unsound, 0 none proposed, 0 not judged.
- Severity: 0 confirmed findings ungraded by the skeptic. 3 were re-graded (ids 10, 17 and 30).
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-diff-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 11 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 18 items, each assigned to exactly one of the 5 lenses (security 4, correctness 4, seams 4, verification 3, intent 3).
- By design: the caller's byDesign.

The run is complete on these counts.

Four findings were refuted. Ids 7, 14 and 34 were duplicates or misreadings of confirmed findings. Id 33 read the dTrueNorth decision cite as a widening; it follows from an owner answer.

Every fix below was judged sound by a skeptic.

## High

### H1. The packet's guard against instrument edits re-pins the edited blob (id 1)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:137`. The recovery rule that undoes the guard is at lines 478 and 589-591.
- **What is wrong:** P0.1 row 10 guards against a run editing the instruments by having the packet pin each instrument's blob, so the next `packet.py --check` reds. But the plan lists "an instrument's blob moves" as an ordinary cause of staleness, and its recovery rule on red is "re-render and commit". So a run that edits `carries.py` or `deviations.py` sees the red, follows the plan, and the re-rendered packet pins the edited blob. `packet.py` itself pins only its version, not its blob. The owner's check, "a product path in a spec run's diff", does not flag an edit under `memory/builds/dClosedLoop/build/`.
- **Consequence:** this is the TOOL-aStandingWrit-7 class the row claims to close. Until dTrueNorth lands, and on through dIndexedDesign and dScopedBuild, these instruments are the only spec-to-design check. A weakened instrument would land green, and the packet would then certify the weakened blob.
- **Fix:**
  - Make `packet.py --check` compare each instrument's blob, `packet.py`'s included, against `git rev-parse origin/main:<path>`. It reds on any difference that is not itself a dClosedLoop landing.
  - Make "an instrument's blob moved" a stop, not a re-render cause, in [handoffs] and in the phase-2 step at line 478.
  - Plant: edit one byte of `carries.py` on a run branch, follow the re-render step, and confirm `--check` still reds.
- **Left-shift gate:** a P0.1 red test that plants an instrument edit and then runs the plan's own recovery step.

### H2. P0.2's `--check` byte-compare cannot red a generator defect (id 8)

- **Where:** plan:180. `--check` is defined at line 175, and D10 makes its claim at lines 976-977.
- **What is wrong:** `--check` re-renders the report and compares the bytes. Suppose the generator drops a `Decided:` trailer, or fails to put a `widens:` or `relaxes:` choice first. It then writes the same wrong bytes under `--write` and under `--check`, so the check stays green. Every P0.2 red test plants into the written report, so each one catches only a hand edit, which line 185 already covers. D10 still says P0.2's red cases cover the ordering.
- **Consequence:** the ordering the owner's answers require (ER:284-285 and ER:347-348) goes ungated while the plan says it is gated. The builder will be misled.
- **Fix:**
  - Give `--check` (or `--fixture`) semantic arms independent of the render. Parse the written report and assert that every `widens:` and `relaxes:` mark appears before the first other entry.
  - Assert that every trailer in the range appears, and that every `relaxes:` record names a tier and a reason.
  - Plant generator-side defects, such as a renderer that skips or reorders, and observe red.
- **Left-shift gate:** a bug-class checklist entry: "a check defined as re-render and compare cannot red a defect of the renderer".

### H3. The extra unit's "once" guard has no cross-run source, and its spec-run test is wrong (id 31)

- **Where:** plan:412, with lines 404-418.
- **What is wrong:** the extra unit promises that the build run's second deferral of a carried unit is refused (red case 3). Its spec is told to use "the starting roster and the defer and add rows". Those inputs cannot carry red case 3:
  - In the build run, the carried unit is already on the starting roster. `baseline_units` reads the current `RUN.md` (`lib-unattended.sh:1950`), and term 2 (`unattended.sh:5177-5184`) passes any unit on that roster.
  - The spec run's add row sits in a `RUN.<phase>.<blob8>.md` that preflight has rotated out (PROTOCOL:153-158).

  The spec-run test "a run that closes no unit" also matches a build run that closes nothing. The README rule uses a different test: a roster unit MISSING at start.
- **Consequence:** a carried unit can be deferred again. A build run that closes nothing can also carry forward units it added itself. Both break M4's "built by its own build run, once, never deferred again", which is the condition the owner accepted (ER:208-209, ER:314-316).
- **Fix:**
  - Name the cross-run witness. Either use the add rows in the build's rotated `RUN.*.md`, or put a `carried-once` marker in the unit's spec header, and refuse a DEFERRED unit that carries it.
  - Identify a spec run by the README's MISSING-unit test.
  - Add two red cases: a build run that closes no unit and re-defers a carried unit is refused, and one that adds and defers its own unit is refused.
- **Left-shift gate:** those two red cases, written into the extra unit's spec.

## Medium

### M1. The schedule pins a stale claim to its dead holder (ids 11, 15, 24)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:132` (lines 131-150).
- **What is wrong:** `claims()` pins any cached claim whose raw `status:` is `live` or `held` and never reads `beat-utc`. The driver derives `stale` from beat age past RESUME_STALE_BOUND (5400 s, `unattended.sh:2177-2186`), while the raw status stays `live`.
- **Consequence:** a dead node's run stays pinned to that node at time 0 and prints as "live". The node loop (plan:602-604) tells each node to take the run shown on its own row, so no other node is offered the run. The takeover rule (plan:612-613) never fires, and that build and every descendant stall. The `--claims` step does print the stale verdict, but nothing routes a node from it.
- **Fix:**
  - Take the verdict from `unattended.sh --claims`, or apply the same beat-age bound.
  - Print a stale claim as "stale on <node>: take over per [coordination]" and do not pin it.
- **Left-shift gate:** a P0.4 plant: a `live` claim with a beat older than 5400 s is reported stale and left unpinned.

### M2. The plan claims `--close` refuses cross-build writes, but no gate does (id 2)

- **Where:** plan:592.
- **What is wrong:** the plan cites fail 66 (`unattended.sh:10531-10541`) as the refusal. Fail 66's set comes from `derive_carry_set` (`push-main.sh:548-560`), which takes the commits that are in both HEAD and the local default branch and that the remote lacks. A run's own branch commit writing `memory/builds/<other>/` or a dClosedLoop instrument is not in that set, because runs never merge into local main (plan:607). There is no other path-based refusal: `--dispatch --writes` only refuses two passes claiming one file.
- **Consequence:** writes to another build's packet, BACKLOG or README, or to the shared instruments, land unrefused, and the plan tells three nodes that the driver prevents them. This feeds H1.
- **Fix:**
  - Correct the sentence: no gate stops these writes, and the rule is a README policy line checked at the closing review.
  - Then either list every path under `memory/builds/<other>/` in the departures report, or file a dPlacedRequest path-exclusion unit in [cannot].
- **Left-shift gate:** the departures-report arm. Probe it with `git diff --name-only <base>..HEAD | grep -v '^memory/builds/<slug>/'`.

### M3. The fork ladder has no rung for a veto-2 fork outside the grant (id 3)

- **Where:** plan:41, with lines 506-525 and line 1007.
- **What is wrong:** METHOD veto 2 covers a new external dependency, install location, public surface or governance-carrier change (BUILD-METHOD.md:91), and such a fork parks (METHOD:93-97). The grant (ER:177-181) lifts veto 2 only for the changes the build's own [chain] clauses name. The ladder covers only veto 3, the goal bound and veto 1, yet the plan says three times that nothing parks. P0.2 has no mark for a choice that lifts veto 2 through the grant.
- **Consequence:** a run either parks against the plan, or stretches its reading of the grant, in which "governance carrier" is undefined. Stretching it takes in a dependency or carrier change outside its own clauses, unsurfaced. That widens the write surface beyond what answer R1 accepts.
- **Fix:**
  - Add a rung to [answer] item 2 and to [phase-2]: a veto-2 fork outside the grant parks, or goes to the owner as a new question.
  - Require a `grants: <decision id> <change>` mark on every grant-lifted choice, listed in the departures report beside `widens:` and `relaxes:`.
- **Left-shift gate:** a P0.2 red test for a grant-lifted choice that is not listed.

### M4. The "once" guard has no named source (id 4)

- **Where:** plan:412.
- **What is wrong:** this is the same defect as H3, from the security lens. A cross-run source is missing for red case 3, and the spec-run test "closes no unit" disagrees with the README's MISSING rule (plan:276-279).
- **Why it is a separate item:** its binding grade is medium, H3's is high, and items may merge only findings of one grade. The skeptic graded it contained because red case 3 is still stated as a requirement. H3's fix closes both.
- **Fix:** state the source of "already carried once" in phase 1, for example the spec run's departure record with follow-through "new unit <id>", or a defer row in a rotated `RUN.*.md` of the same build. Define a spec run by the MISSING-unit rule, and add the red case for a build run that closes no unit.
- **Left-shift gate:** as for H3.

### M5. Owner-approved deviation record 2 cites ER lines, not a decision id (id 9)

- **Where:** plan:845. [defaults] is at lines 978-980.
- **What is wrong:** P0.1 row 6 (line 133) requires an approver naming the owner to cite a decision id the default branch holds. Record 2 cites "ER:232 and ER:320", and [defaults] says only "citing the answer". Record 1 (line 844) cites P0.8 row 3, so the records behave differently.
- **Consequence:** as written, record 2 fails the hardened approval arm. Under `report` it becomes a standing approval failure that buries real unapproved departures. Under `refuse` it reds.
- **Fix:**
  - Cite P0.8 row 1 for record 2.
  - Align [defaults] with P0.1 row 6.
  - Plant: an owner approver citing only an ER line reds.
- **Left-shift gate:** that plant in P0.1.

### M6. P0.9's Python check cannot fail (id 12)

- **Where:** plan:377.
- **What is wrong:** `bash tools/lib/resolve-python.sh` only defines `resolve_python()`. Running it prints nothing and exits 0.
- **Consequence:** a node whose only `python3` is the MS-Store stub passes preparation, then fails at the first schedule-script or instrument call.
- **Fix:** use `. tools/lib/resolve-python.sh && PY=$(resolve_python) && "$PY" --version`, and require a non-empty launcher.
- **Left-shift gate:** observe the step red with PATH stripped of every python.

### M7. Instrument/product disagreements go to a BACKLOG no one reads (id 16)

- **Where:** plan:458, with line 271 and lines 629-631.
- **What is wrong:** disagreements are routed to an ask in dTrueNorth's BACKLOG.md. But dTrueNorth runs once, whole, with no BACKLOG and no later close. `asks-disposed` grades only at the owning build's own close (ASKS:128-143).
- **Consequence:** the cross-check meant to catch a product-join regression ends in a sink no one reads.
- **Fix:**
  - Route the ask to the not-yet-landed build that owns the succeeding clause (dIndexedDesign, dScopedBuild, dDeclaredLoop or dOrderedCharter), or surface it in the departures report's first block.
  - State that an ask may be filed only in a build whose build run has not landed.
- **Left-shift gate:** a bug-class checklist entry: "an ask routed to a build with no later close".

### M8. A claim pin bypasses SPEC_ONLY and can put a build run on node b (id 23)

- **Where:** `schedule.py:241`.
- **What is wrong:** `run()` picks `('build', b)` when the build's spec phase reads done, and pins it to the claim's node without testing SPEC_ONLY. The filter applies only in `simulate`'s dispatch (line 204). In the window between a b spec run's `--land` and `--landed`, or while a b run is held after landing, the table names a build run as b's next run.
- **Consequence:** this breaks the owner's "Spec runs only" rule for node b (ER:219). The finder reproduced it in a scratch clone: the table printed "b: build dFairHearing at 0".
- **Fix:** pin a node-b claim only to a spec run. Otherwise report the claim, and either leave it unpinned or exit 1.
- **Left-shift gate:** a P0.4 red test: a live agent5 claim on a build whose specs are DEFERRED puts no build run on b.

### M9. No P0.4 red test exercises SPEC_ONLY (id 25)

- **Where:** plan:240, with the plant table at lines 242-248.
- **What is wrong:** with `SPEC_ONLY = set()`, the 0.25 table, the loads, the first wave, the 43 starts and the landings come out byte-identical. Only the pace-sweep lines for 0.30, 0.45 and 0.50 change.
- **Consequence:** a regression that drops or inverts the owner's rule passes every red test that phase 0 re-runs.
- **Fix:** add a plant with `--b 0.5`, with and without SPEC_ONLY, and assert that b's output names no build run. Alternatively, have the script exit 1 if any build run lands on b.
- **Left-shift gate:** that plant in P0.4.

### M10. The `relaxes:` completeness red test cannot red under a byte compare (id 26)

- **Where:** plan:183, against line 175.
- **What is wrong:** a re-render of a `relaxes:` record with no tier and no reason reproduces the same bytes. No other validation of the record is specified.
- **Consequence:** this is the only guard left on rung 6 ("which bound, its tier, and why"), since the tier judgement is listed under "What nothing catches". As specified it cannot fail, so a relaxed bound without a tier or reason lands green. This is related to H2 but kept separate: it is a distinct missing validation at a different grade.
- **Fix:** have `--report` validate each `relaxes:` and `widens:` record and exit 1 under both `--write` and `--check` when the record lacks the bound, its tier or a reason. Make the red test plant the incomplete record, not a stale report.
- **Left-shift gate:** that planted incomplete record.

### M11. P0.7's opening gate on `deviations.py` is constant (id 27)

- **Where:** plan:337, with lines 140-142.
- **What is wrong:** P0.1 makes `--policy report` the default, and report always exits 0. P0.7's gate checks only the exit code, while P0.1's acceptance names "0 members".
- **Consequence:** members created by the phase-0 edits land with the opening while the gate reads as a pass.
- **Fix:**
  - Run `deviations.py --policy refuse` at P0.7, or assert that the printed member count is 0. Do the same for phase 1's by-hand run at dTrueNorth's Design exit.
  - Keep `report` for the chain runs.
- **Left-shift gate:** a bug-class checklist entry: "a gate's exit code made constant by a default set in the same phase".

### M12. The "record before close" step exists only in prose (id 30)

The finder graded this high; the skeptic graded it medium.

- **Where:** plan:814, with lines 275-288, 474-490 and 494-504.
- **What is wrong:** [deviations] says a member listed as "recorded by nobody" gets its record before `--close`, as "a step in the README's rules". P0.5's README rules and the phase-2 tables have no such step. They write the report and then close.
- **Consequence:** the owner's chosen option (ER:251-252) is not carried. A build with an unrecorded member lands it with no record. A record written afterwards also leaves the committed report stale.
- **Fix:**
  - Add a README rule and a row to both phase-2 tables, in this order: `deviations.py --report <slug>`, a record for each unrecorded member, then `--report <slug> --write` and commit.
- **Left-shift gate:** a P0.2 red test: a report written before a member's record is added fails `--check`.

### M13. Two answers to when the deviation overrides are set (id 32)

- **Where:** plan:778, against lines 775, 785 and 902.
- **What is wrong:** the dKeptSession row (t=135) says both deviation values become overrides on `standard`. But `deviation.gate` (cl-0412) lands only with dScopedBuild at t=247, and the other rows set each override when its own key lands.
- **Consequence:** a node either tries to set an override on a key that does not exist yet, or stops running the instrument's `--policy report`.
- **Fix:** rewrite the dKeptSession row. Presets only make the override mechanism available. The approval override stays with dDeclaredLoop, and the gate override waits for dScopedBuild.
- **Left-shift gate:** a bug-class checklist entry: "a sync-point row restating a step another row owns".

## Low

### L1. P0.8's acceptance omits `[answers-3]` (ids 5, 10, 17, 29)

The skeptics graded ids 10 and 17 down from medium to low.

- **Where:** plan:364.
- **What is wrong:** the acceptance requires every row to quote its answer in ER `[answers]` or `[answers-2]`. Rows 1 and 5 quote ER:320 and ER:328, which are in `[answers-3]` (ER:306-350). Line 951 already names `[answers-3]`.
- **Consequence:** cosmetic. Rows 1 and 5 also quote `[answers-2]` lines, and no gate reads the rows (line 367). But the acceptance leaves the owner's riskiest quotes outside what it names.
- **Fix:** change the line to "in ER `[answers]`, `[answers-2]` or `[answers-3]`".
- **Left-shift gate:** a checklist entry for the amendment-leaves-its-other-half-standing class.

### L2. The schedule script's docstring is stale after the `[answers-3]` fold (ids 13, 20, 35)

- **Where:** `schedule.py:3`, lines 20-23, lines 40-41 and lines 55-56.
- **What is wrong:**
  - EXTRA is described as "the carry-forward condition for review-promoted units", citing only `[answers]` and `[answers-2]`. `[answers-3]` item 1 (ER:320, ER:346) widened it to any unit a spec run adds.
  - Lines 40-41 say a WHOLE build reads landed once the specs of its v2 clauses are closed. The code (line 118) requires every spec in the folder, the extra unit's included, to be CLOSED or WONTDO.
- **Consequence:** comments only. No numeric effect.
- **Fix:** cite `[answers-3]` item 1 and say "any unit a spec run adds (review or discovery)". State the landed rule as the code applies it.
- **Left-shift gate:** the checklist class a-folded-field-leaves-its-row-shape-docs-behind.

### L3. The shared-path rate drops its denominator and its lower-bound caveat (id 6)

- **Where:** plan:627.
- **What is wrong:** "Of 34 unordered build pairs, 3 name a shared path". The coordination return (`research-exec-coordination.md:100`) calls the 3 a lower bound, because rows mostly name keys rather than files.
- **Consequence:** the collision risk reads as measured and small.
- **Fix:** "Of the 34 build pairs the chain does not order, at least 3 name a shared path in v2 (a lower bound: rows mostly name keys, not files)".
- **Left-shift gate:** the checklist class rate-quoted-without-its-denominator.

### L4. Packet field 9's extra-unit content has no stated source (id 18)

- **Where:** plan:220, with lines 189-190, 204 and 213-215.
- **What is wrong:** the acceptance requires field 9 to carry the extra unit, its decision row and two records. None of these is in v2 or in the packet's named inputs, and no completeness arm checks them.
- **Fix:**
  - Name the source in P0.3: the opened README's roster units and the P0.8 row 1 id.
  - Add an arm: every roster unit, Derived ones included, appears in the packet.
- **Left-shift gate:** that completeness arm.

### L5. A departures report can be overwritten, and `--check` has no caller (id 19)

- **Where:** plan:174, with lines 284, 439, 487 and 504.
- **What is wrong:** a spec run and a build run of one build share the name `<date>-build-<first unit>-departures.md`, and the schedule runs them back to back on one node. No step calls `--report --check`.
- **Consequence:** a same-date build run overwrites the spec run's report, and a hand edit of a written report goes undetected.
- **Fix:**
  - Put the run kind in the name (`-departures-spec.md` and `-departures-build.md`).
  - Add `deviations.py --report <slug> --check` after the `--write` commit in phases 1 and 2.
- **Left-shift gate:** the `--check` call in the close steps.

### L6. dWellOiledMachine's record cites ER:248 without a decision id (id 21)

- **Where:** plan:848.
- **What is wrong:** this is the same rule as M5 (P0.1 row 6, line 133). The sibling at line 847 cites P0.8 row 6.
- **Why it is a separate item:** its binding grade is low, while M5's is medium.
- **Fix:** cite "ER:248 and P0.8's row 6".
- **Left-shift gate:** M5's plant.

### L7. An off-fleet claim is dropped silently and offered to a or d (id 22)

- **Where:** `schedule.py:242`.
- **What is wrong:** a claim from fleet tag c (`agent-0`, `fleet.toml:35-40`) passes the fleet check at line 133, but `run()` skips it because c is not in `speed`. The run is then scheduled on a or d, while the "claims cached" line lists it as held.
- **Consequence:** preflight refuses the run if the claim is live, but takes it over silently if the claim is stale.
- **Fix:** treat a claim whose node is outside `speed` as removing that run from dispatch, and print "held off-fleet on <tag>".
- **Left-shift gate:** a P0.4 plant with a tag-c claim.

### L8. The bare-id predicate's grammar differs from the roster join (id 28)

- **Where:** plan:301.
- **What is wrong:** the predicate skips any id that follows ":". The generator blanks only the `missing:` form (`tree_lib.py:179-194`) and otherwise matches `\b(FAM)-slug-\d+\b` (`gen_build_index.py:820`). So `x:missing:TOOL-dTrueNorth-1` joins a roster while the gate stays silent. The two agree on today's tree, so the gap is latent.
- **Fix:** run the generator's own `extract_roster_ids(text, build_roster_id_re(families))` over the tracked `memory/` files and keep the 22 chain slugs.
- **Left-shift gate:** plant `x:missing:TOOL-dTrueNorth-1` and see it print.

review-shape kind=diff-review round=1 intensity=full at=synth raw=35 confirmed=31 refuted=4 unverified=0 blocker=0 high=3 medium=15 low=13 agents=11 out-tokens=120833

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:137 | high | high | confirmed | The plan is new in this diff. P0.1 row 10 (plan:137) guards against instrument edits by having the packet pin each instrument's blob, and `--check` re-renders the packet and compares bytes (plan:197, :214). The plan also lists 'an instrument's blob moves' as an ordinary cause of staleness (plan:589). Its recovery rule is 're-render and commit' on red (plan:478, :590-591). So a run that edits carries.py or deviations.py sees the red, follows the plan, and the packet then pins the edited blob. The guard reads the state it guards. Field 1 pins only 'the generator's version' for packet.py, not its blob. The consequence is a check certifying what it does not check, reachable whenever a run edits an instrument. That path is narrow. | sound | - |
| 2 | security | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:592 | medium | medium | confirmed | Plan:591-592 says `--close` refuses a commit belonging to another build (VERBS:860-862). That refusal is check_landing_carry's fail 66 (unattended.sh:10531-10541). It runs the lander's carry set, derive_carry_set (push-main.sh:548-560): the commits in both HEAD and the local default branch that the remote lacks. Its own message says the set is commits that 'rode in through the local default branch'. A run's own branch commit that writes memory/builds/<other>/... is not in that set, and runs never merge into local main (plan:607). Grepping unattended.sh for 'another build' found no path-based refusal. So the plan tells nodes the driver enforces a boundary it does not enforce. | sound | - |
| 3 | security | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:41 | medium | medium | confirmed | METHOD:91 veto 2 covers a new external dependency, install location, public surface or governance-carrier change. METHOD:93-97 says a fork whose only survivor trips veto 2 parks. The grant (ER:177-181) lifts veto 2 only for the governance-carrier and public-surface changes the build's own [chain] clauses name. The ladder (plan:506-525) and the bad-news item (plan:41-46) cover only veto 3, the goal bound and veto 1, under the standing ruling and relax-the-weakest-bound. The standing-ruling question (ER:233-240) also names only those three cases, yet the plan says 'Nothing parks' (plan:525, :1007). A veto-2 fork outside the grant is therefore unaddressed: the run either parks against the plan or stretches the grant. P0.2 has no mark for choices that lift veto 2 through the grant. | sound | - |
| 4 | security | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:412 | medium | medium | confirmed | check_carry_forward term 2 (unattended.sh:5174-5184) tests id_in against baseline_units. baseline_units (lib-unattended.sh:1950-1990) reads the README roster at this run's first live-phase commit and filters to this run's base. In the build run, a unit the spec run added and landed is on that starting roster, so today's term passes it again. The plan names only 'the starting roster and the defer and add rows' (plan:412-413) and gives no cross-run source for red case 3 (plan:418). The plan's own definition also conflicts: a spec run is 'a run that closes no unit' (plan:402, :412), while the README rule (plan:276-279) uses 'any roster unit MISSING'. Under the first definition, a build run that closes nothing qualifies to carry its own added units. That is a real gap in the specified M4 'once' guarantee. Its effect is contained, because red case 3 is still stated as a requirement for the dTrueNorth spec to satisfy. | sound | - |
| 5 | security | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:364 | low | low | confirmed | Plan:364 requires every P0.8 row to quote its answer 'in ER [answers] or [answers-2]'. ER's [answers-3] runs from line 306 to 352, so ER:320 (row 1) and ER:328 (row 5) are [answers-3] quotes. Plan:951 says '[answers-2] or [answers-3]'. The acceptance wording is inconsistent with the rows it governs. Rows 1 and 5 also quote [answers-2] lines, so the effect is cosmetic. | sound | two-answers-to-one-question |
| 6 | security | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:627 | low | low | confirmed | Plan:627 says 'Of 34 unordered build pairs, 3 name a shared path in v2'. The coordination return (research-exec-coordination.md:100) says '34 pairs of builds the chain does not order' and states 'This is a lower bound, because rows mostly name keys rather than files.' The plan drops the lower-bound caveat, and 'unordered' is ambiguous. The effect is limited to how the risk reads: the plan still names the hot shared files and handles them at the prepare conflict. | sound | rate-quoted-without-its-denominator |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:412 | high | - | refuted | Duplicate of finding 4: the same line (plan:412), the same defect and the same fix. The substance is confirmed under id 4, where I checked it against unattended.sh:5174-5184 and lib-unattended.sh:1950-1990: term 2 reads only this run's starting roster, there is no cross-run source for red case 3, and 'closes no unit' conflicts with the README's MISSING rule. | sound | - |
| 8 | correctness | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:180 | high | high | confirmed | Plan line 175 defines --check as render-again-and-compare-bytes. Read against that, every P0.2 red test (lines 180-185) plants into the written report, so it can only catch a hand edit, which line 185 already covers. A generator that drops a trailer or misorders a widens:/relaxes: choice writes the same bytes under --write and --check, so it stays green. D10 (lines 976-977) still says P0.2's red cases cover the ordering ER:284-285/:347-348 requires, so the plan claims a gate it does not specify. The instrument is not built yet, so this is graded high (it will mislead the builder) rather than blocker. | sound | - |
| 9 | correctness | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:845 | medium | medium | confirmed | P0.1 row 6 (line 133) requires an approver naming the owner to cite a decision id the default branch holds. In [deviations], record 1 (line 844) cites P0.8's row 3 and dPlacedRequest's cites row 6. Record 2 (line 845) cites only 'ER:232 and ER:320', and dWellOiledMachine's (line 848) only 'ER:248'. Both are execution-record line numbers, not decision ids, so written as specified those records fail the hardened approval arm, or show up as approval failures under report. [defaults] line 978-980 says only 'citing the answer'. The three records are inconsistent. | sound | - |
| 10 | correctness | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:364 | medium | low | confirmed | ER's [answers-3] heading is at line 306, so ER:320 and ER:328 sit in [answers-3], and P0.8's acceptance (line 364) still names only [answers] or [answers-2]. The claimed impact is overstated: rows 1 and 5 also quote ER:232 and ER:240, which are in [answers-2], so they do not fail as written. The plan also says no gate reads the rows (line 367). What remains is a stale acceptance line that leaves the [answers-3] quotes outside what it names, so the effect is cosmetic. | sound | - |
| 11 | correctness | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:132 | medium | medium | confirmed | schedule.py:132 pins any claim whose raw status: is live or held. unattended.sh:2177-2186 derives 'stale' only from beat age against RESUME_STALE_BOUND, and the raw status stays live. So a dead node's stale claim stays pinned to that node at time 0, and the script reports it as live. The node loop (plan line 603) tells each node to take only the run shown on its own row, so nobody picks up the stale run from the schedule. The --claims step earlier in the loop does print stale, which softens this somewhat, but the schedule never routes it to the claim rules. | sound | - |
| 12 | correctness | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:377 | medium | medium | confirmed | tools/lib/resolve-python.sh only defines resolve_python(), and its header says 'source it, then call it'. I ran `bash tools/lib/resolve-python.sh`: it printed nothing and exited 0. So P0.9's step (line 377) cannot fail, and a node with only the MS-Store stub passes preparation, then fails at the first instrument call. The plan file is new in this diff. | sound | - |
| 13 | correctness | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:21 | low | low | confirmed | The docstring at schedule.py:21-22 and the EXTRA comment at line 55 describe the extra unit as 'the carry-forward condition for review-promoted units' and cite only [answers-2]. They miss the [answers-3] widening at ER:320. Lines 40-41 say a WHOLE build reads landed once the specs of its v2 clauses are CLOSED or WONTDO, but tree_state (line 118) requires every spec in the folder to be CLOSED or WONTDO. The comments are stale; the numbers are unaffected. | sound | a-folded-field-leaves-its-row-shape-docs-behind |
| 14 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:412 | high | - | refuted | The plan's line 411-413 names the starting roster and the defer/add rows as the inputs for telling a run that closes no unit and a unit the run added. That is the spec-run side of the carry. It does not name them as the inputs for refusing a second deferral. Red case 3 (line 418) separately requires that the next run deferring a carried unit is refused, and that each case is seen as stated after the change. A build that, as the finder shows (check_carry_forward term 2 at unattended.sh:5177-5184 sees the unit on the starting roster), cannot make case 3 red has not met the plan's spec; the plan does not permit that outcome. How the cross-run fact is read is unit-level detail, which by design is owed to dTrueNorth's spec. So the claim that the plan specifies the rule from inputs that cannot enforce it misreads the text. | sound | - |
| 15 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:132 | medium | medium | confirmed | schedule.py:132-150 claims() pins any cached claim whose message reads `status: live` or `held`, and never looks at beat-utc. unattended.sh:2177-2186 derives the verdict `stale` from beat age past RESUME_STALE_BOUND, while the raw status stays `live`. The plan's node loop (602-604) says the run the table shows at time 0 is the node's next run. So a dead holder's build stays pinned to that node on every re-run, and no other node's table ever offers it. Step 1 of the loop does run --claims, which prints the stale verdict, so the staleness can be seen. But nothing in the loop sends a node from that verdict to the takeover rule (612-613), and the script's table contradicts it. The effect is contained to one stalled path. | sound | - |
| 16 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:458 | medium | medium | confirmed | Plan 457-458 routes every instrument/product disagreement to 'an ask in dTrueNorth's BACKLOG.md'. Those disagreements arise at other builds' closes, after dTrueNorth has landed. P0.5 (271) gives dTrueNorth no BACKLOG because it runs whole and once. [coordination] (628-631) relies on the owning build's 'next close' disposing of an ask, and dTrueNorth has no next close. So the cross-check feeds into a backlog that no later step ever reads or disposes. | sound | - |
| 17 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:364 | medium | low | confirmed | P0.8's acceptance (364-365) says each row quotes its answer in ER [answers] or [answers-2]. But row 1 quotes ER:320 and row 5 quotes ER:328, and both lie in ER [answers-3] (ER:306-350). [defaults] (951) does name [answers-3]. The acceptance text was missed in the fold. No gate reads it (366 says so), so the effect is a miscalibrated manual check, not a wrong result. | sound | - |
| 18 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:220 | low | low | confirmed | Field 9 is defined (204) as v2's [owed]/[open]/[enforcement]/[policies] lines naming the build. The packet's stated inputs (189-190) are the handoffs probe, carries.py design() and asbuilt.py's view. The --check completeness arms (213-215) cover only v2 row ids, gaps, parents and [owed]. Yet the acceptance (219-220) requires field 9 to carry the extra unit, its decision row and two records, none of which is in v2 or the named inputs. The source is unstated and no arm checks it. | sound | - |
| 19 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:174 | low | low | confirmed | P0.2 (174) names the report <date>-build-<first unit>-departures.md. A spec run (487) and a build run (504) of one build share both slug and first unit, so a same-date build run overwrites the spec run's report, which then survives only in history. --check is called only in P0.2's own red tests. README rule 4 (284) and phases 1 and 2 (439, 487, 504) call only --write, so a hand edit to a written report goes unchecked. | sound | - |
| 20 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:22 | low | low | confirmed | schedule.py:21-23 and :56 still say 'the carry-forward condition for review-promoted units' and cite only [answers-2]. The plan (400-405) and ER:314-320 ([answers-3] item 1) widened the condition to any unit a spec run adds, from a review or a discovery. The wording is stale, and the EXTRA value of 1 is unaffected. | sound | - |
| 21 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:848 | low | low | confirmed | At 848, dWellOiledMachine's record names 'approver owner citing ER:248' with no decision id. P0.1's row 6 (133) hardens the instrument so that an owner-named approver must cite a decision id the default branch holds, and 'owner' with no id reds. The sibling row at 847 cites 'P0.8's row 6', and P0.8 row 6 (360) also covers ER:248. As written, the record would fail the hardened approval arm. | sound | - |
| 22 | seams | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:242 | low | low | confirmed | fleet.toml:35-40 declares tag c (user agent-0). claims() at schedule.py:133 accepts any fleet user, so held[slug] = ('c', status). run() at :242 pins only when `n in speed`, and speed holds only a and d (b too when with_b), so the c claim is dropped silently. simulate() then offers that run to a or d at time 0, while the 'claims cached' line still prints '<slug> live on c'. The script is new in this diff. Reaching it needs a chain claim from node c, which is outside the owner's three nodes, so the path is narrow and preflight's live-claim refusal limits the effect. | sound | - |
| 23 | verification | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:241 | medium | medium | confirmed | schedule.py:241 picks ('build', b) whenever state[b][0] (the spec phase reads done) and pins it to the claim's node with no SPEC_ONLY test. SPEC_ONLY is applied only in simulate's dispatch filter (:204), which pinned runs skip. A b spec run's claim stays live from --land until --landed while its specs already read done on origin/main, so in that window the table puts the build run on b at time 0, and the node loop (plan [coordination]) treats the table's time-0 run as the node's next run. P0.4's red-test table has no row for this case: its only claim plant pins a spec run. The window is narrow, so the effect is contained. | sound | - |
| 24 | verification | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:132 | medium | medium | confirmed | claims() (schedule.py:131-136) reads only the stored status and node keys and pins any 'live' claim. The driver turns a 'live' status into the stale verdict once the beat age passes RESUME_STALE_BOUND (unattended.sh:2178-2185, computed from beat-utc). The script therefore pins a dead holder's run at time 0 and prints it as live, so no other node is offered it, and the plan's stale-takeover rule (plan:612-613) gets no prompt from the table. The node loop does run `--claims` first, which prints the verdict, but the plan has the node act on the table's time-0 run. | sound | - |
| 25 | verification | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:240 | medium | medium | confirmed | I re-ran the probe. I copied the script with SPEC_ONLY = set() and diffed its output against the original at HEAD. Only the pace-sweep lines for 0.30, 0.45 and 0.50 changed: build dRankedPlan, build dFurnishedOrders and build dScopedBuild now appear on b. The 0.25 table, the loads, the first wave and the order were identical. None of the five plants in P0.4's red-test table (plan:242-248) exercises the SPEC_ONLY filter, so a regression of the owner's rule would pass every re-run red test. | sound | - |
| 26 | verification | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:183 | medium | medium | confirmed | plan:175 defines --check only as 'renders it again and compares the bytes'. The red test at plan:183 expects a `relaxes:` record with no tier and no reason to red --check. A re-render of the same records reproduces the same bytes, so as specified this test cannot go red, and the plan names no other validation of the record's completeness for rung 6. | sound | - |
| 27 | verification | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:337 | medium | medium | confirmed | P0.1 (plan:140-142) makes --policy report the default: it prints every member and exits 0. P0.7's gate row (plan:337) checks only that `deviations.py` exits 0, which report makes constant whatever the population holds. P0.1's acceptance names '0 members', but the opening gate does not assert it. Under refuse, today's main (deviations.py:220-221) exits 1 only on findings (an unjoined member or an approver below its risk), so running refuse at the opening and at dTrueNorth's by-hand Design exit would not red on members that are joined. | sound | - |
| 28 | verification | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:301 | low | low | confirmed | The plan's predicate (plan:301-302) skips any id preceded by ':'. The generator blanks only the `missing:` form (tree_lib.py:181-194, MISSING_PREFIX) and then matches `\b(FAM)-slug-\d+\b` (gen_build_index.py:812-829), and the colon is a word boundary. An id written as `x:missing:TOOL-dTrueNorth-1` therefore joins a roster while the predicate stays silent. The finder reports that the two agree on today's tree, so the mismatch is latent. Its effect is limited to the opening gate's coverage. | sound | - |
| 29 | verification | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:364 | low | low | confirmed | Plan line 364 reads 'Every row quotes its answer in ER `[answers]` or `[answers-2]`'. Row 1 (line 347) quotes 'Carry it too (Recommended)' (ER:320) and row 5 quotes 'Relax the weakest bound' (ER:328). Both are under ER's '## [answers-3]' heading at line 306. So the acceptance leaves out the source of two of its own rows. The effect is confined to how the decision log is checked. | sound | - |
| 30 | intent | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:814 | high | medium | confirmed | [deviations] says a member listed as 'recorded by nobody' gets its record before --close, and calls this 'a step in the README's rules'. P0.5's six build-level rules have no such step. Rule 4 says only to write the report with `deviations.py --report <slug> --write` before --close. The spec-run table writes the report and then goes straight to --close, and the build-run table does the same ('The departures report, then the close'). Owner answer 8 (ER:251-255) chose 'a step before the close gives each a record'. That step appears only in prose, not in the rules a cold run follows, so on a build with an unrecorded member it can land with no record. The end report still lists the member as unrecorded, which limits the harm, but the plan claims a carried step that does not exist. | sound | - |
| 31 | intent | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:412 | high | high | confirmed | Plan lines 404-412 tell the extra unit's spec to tell runs apart 'from the starting roster and the defer and add rows'. The spec run is defined as 'a run that closes no unit'. In the build run, the carried unit is already in the roster that run started with. baseline_units reads the current RUN.md (lib-unattended.sh:1950), and term 2 (unattended.sh:5177-5184) passes any unit in that roster. The spec run's add row is in a RUN.<phase>.<blob8>.md that preflight retired (PROTOCOL.template.md:153-158). So the named inputs cannot carry red case 3's 'refused on second deferral'. 'Closes no unit' also matches a build run that closes nothing, and that run could then carry forward units it added itself, against M4's intent and ER:314-316. Red case 3 would catch the first gap when the unit is built. No red case covers the build run that closes nothing. That run is a narrow path, but it has the full consequence. | sound | - |
| 32 | intent | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:778 | medium | medium | confirmed | The dKeptSession row at line 778 (landing at t=135) says 'The chain's two deviation values become overrides on `standard`'. The dDeclaredLoop row (775) sets the author-recorded override when deviation.approval lands. The dScopedBuild row (785) sets the report override when deviation.gate (cl-0412) lands at t=247 (line 721). [owner] line 902 places the setting at the dDeclaredLoop and dScopedBuild landings. At t=135, deviation.gate does not exist yet, so the plan gives two answers for when the overrides are set. A node is likely to notice and stop, so the effect is contained. | sound | - |
| 33 | intent | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:266 | low | - | refuted | All 22 may: lines still cite the one grant row, as ER:181 requires. dTrueNorth's extra cite is to row 1, the decision recording the owner's own approval of the extra unit, which changes the carry-forward term in tools/unattended/ (ER:224-232, :320). The grant row covers only what [chain] clauses name, so a unit the owner approved outside them needs its own decision cite. That cite follows from an answer the owner gave; it does not widen past it. P0.5's table states it openly, and the [owner] walk includes reading 'every decision row' in the opening diff. | none | - |
| 34 | intent | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:364 | low | - | refuted | This duplicates finding 29: the same line (364), the same stale '[answers] or [answers-2]' acceptance, and the same rows 1 and 5 resting on ER:320 and :328. The defect is confirmed under id 29. | none | amendment-leaves-its-other-half-standing |
| 35 | intent | memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:20 | low | low | confirmed | The schedule.py docstring cites only '[answers] and [answers-2]' (line 3). At line 20 it describes EXTRA as 'the carry-forward condition for review-promoted units'. [answers-3] item 1 (ER:310-320, :346) widened the unit to any unit a spec run adds, from a review or a discovery. This is a comment only, and EXTRA's unit count is unchanged. | sound | amendment-leaves-its-other-half-standing |
