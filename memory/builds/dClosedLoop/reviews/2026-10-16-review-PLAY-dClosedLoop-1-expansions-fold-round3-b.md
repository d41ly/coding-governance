**Serves:** diff-review PLAY-dClosedLoop-1

# Review: dClosedLoop expansion fold, round 3, run B

Tier-2 diff review, round 3, run B. Finders: gov-diff-reviewer. Skeptic batches: gov-skeptic. Synthesis: gov-synthesizer.

Range: 67c79f7cc466ae2d077eca7cc99111e897dd46db...5e139d3775c2b8b5c80879d6cb13a29b1b83b420 (the fold commit 5e139d377). Every line cited below is the line at the worktree's later HEAD.

## Verdict: CLEAN WITH FIXES

No blocker. There is 1 high item. By item: 0 blocker, 1 high, 11 medium, 1 low (13 items). By raw confirmed finding: 0 blocker, 1 high, 19 medium, 1 low (21 findings).

This run is not a full review. It ran at light intensity, and the security and intent lenses were not run, so their classes were swept only through the checklist's shares.

Review shape: intensity light, raw 22, confirmed 21, refuted 1, unverified 0 (0 uncertain), precision 0.95.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 8 | 7 | 1 | 0 | 0 | 0.88 |
| seams | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| verification | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |

Run integrity:
- Lenses: 3/3 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 21 judged sound, 0 unsound, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded. The skeptic re-graded 2, ids 3 and 17, both from high to medium. The binding grades are used below.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 8 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 25 items, each assigned to one lens: correctness 9, seams 8, verification 8.
- By design: the caller's byDesign.

Refuted: id 6 claimed the supervisor's `build.release-ceiling` sweep has no driver in an idle fleet. The skeptic showed the finding inverts layer-runtime:365. The node tick starts the supervisor when none beats under a live run lease, so the sweep does run.

## High

### H1. kits.offer and gap-deploy-13 miss a sixth target-side execution site: the `[[contract]]` parity probe (id 18)

- **Where:**
  - `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:450` (kits.offer)
  - `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:240` (gap-deploy-13)
  - `memory/gotchas/foreign-code-runs-on-the-ambient-credential.md:48-50`
- **What is wrong:** All three say govkit's update runs "five kinds" of target-side code and that the offer mode refuses "all five". There is a sixth.
  - `_cmd_update` calls `derive_parity_lines` (tools/govkit/govkit.py:9658) whenever the receipt has adopter-owned rows.
  - That calls `measure_contract_parity` (:6111).
  - `measure_contract_parity` substitutes the adopter's own file for `{own}` and runs it with `subprocess.run(..., cwd=str(target))` (:6064-6065).
  - tools/memory-tree/kit.toml declares such probes: `python3 {own} --check` at :385, and `bash {own} ...` at :407, :418 and :428.
  - `GOVKIT_RERENDER` does not gate this site.
- **Consequence:** The offer's "runs nothing from the adopter's tree" mode, as designed, still runs adopter-authored code on every adopter with an adopter-owned memory-tree row. The gotcha's fixture plants payloads in only the five named kinds, so it stays green. dShippedRelease would build its sandbox from a wrong execution surface. The gotcha's own probe (list every subprocess call whose cwd is the target) would have listed :6065, so "all five" was recorded without running it.
- **Fix (skeptic judged it sound):**
  - Name the `[[contract]]` parity probe (`derive_parity_lines` :9658 → `measure_contract_parity` :6065) as a sixth kind in kits.offer, gap-deploy-13 and the gotcha.
  - Record that the offer mode does not run it.
  - Add a fixture case that plants a payload in an adopter-owned file a contract probes.
  - Run the cwd=target enumeration over govkit.py and record its output.
- **Gate:** add a gate leg that greps govkit.py for `cwd=str(target)` and fails on any call site the gotcha's site list does not name.

## Medium

### M1. The corrected both-runs probe exempts three rows it never checks, and counts them as matched (ids 1, 10, 17)

- **Where:**
  - `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md:619-626` (the probe's `check()`)
  - `memory/gotchas/one-run-claim-recorded-as-agreed.md:44-49`
  - `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:77`, `:112`, `:120`, `:672-673`
- **What is wrong:** `check()` adds a row to `matched` first. It then returns without checking any citation when "re-measured here" appears anywhere in the row. Three `[agreement]` rows credit both runs in their 'Both runs' cell and cite neither run: Readings (:77), Versions (:112) and Inline copies (:120). In each, the phrase sits in another cell, about a one-run figure.
  - Run at HEAD, the probe prints "rows read: 52; rows the predicate matched: 44" and 0 findings.
  - With the phrase blanked out, it reports exactly these 3 rows.
  - The class rule (gotcha:35-36) scopes the exemption to the 'Both runs' cell. layer-expansions:65 limits re-measuring to "a claim one run made".
- **Consequence:**
  - Three agreed claims rest on no cited line.
  - The gotcha's and [follow-up]'s "green once each row cited each run's line" is false.
  - layer-expansions:672-673 is false for these three rows.
  - The printed 44 includes 3 rows that were never checked (41 were checked). This is the same certify-what-it-skips defect round 2's H1 fixed.
  - The skeptic re-graded id 17 from high to medium: the damage is three uncited record rows plus an over-reported count.
- **Fix (skeptic judged it sound):**
  - Test the phrase only in `row[header.index('Both runs')]`, and in the [cross] 'Found by' cell.
  - Count exempted rows separately and print "exempted: N" beside "matched".
  - Run the probe and record it red on these 3 rows.
  - Then cite research-observability-a/b and research-distribution-a/b on them, or move the claims out of 'Both runs', and rerun to green.
  - Correct the gotcha's and [follow-up]'s "green" line.
- **Gate:** make the probe a repo checker over every `[agreement]` table, scoped to the cell, that prints matched and exempted separately. Add it to the project's bug-class checklist under fixture-passes-by-finding-nothing.

### M2. gap-deploy-13 and the gotcha say `GOVKIT_RERENDER=0` leaves the hole probes running, but it declines them (ids 2, 9)

- **Where:**
  - `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:240`
  - `memory/gotchas/foreign-code-runs-on-the-ambient-credential.md:31-35`
- **What is wrong:** gap-deploy-13 says the switch "declines only the last three" kinds (regenerate, hook wiring, adopters). The gotcha says update "still runs ... each `[[hole]]` discharge probe". Neither is true of the tree:
  - In `_cmd_update`'s per-kit loop, `if not _rerender_on: ... continue` at govkit.py:10926 comes before the first `run_hole_probes` call at :10953.
  - The second call (:11799-11800) iterates `_hu_late`, which is filled only at :11036, inside the same gated loop.
  - Only `run_kit_check` (:10015, :11214) runs whatever the switch says.
- **Consequence:** The design records misstate what the switch already declines: of the five kinds they name, it declines four and leaves only `[check]`. Whoever builds kits.offer's no-execution mode may build a separate refusal for hole probes, or a fixture that expects them to run under RERENDER=0. Such a fixture would never go red.
- **Fix (skeptic judged it sound):** Reword both places as follows. `GOVKIT_RERENDER=0` declines the hole probes, the regenerate argvs, the hook wiring and the adopters, and leaves only each kit's `[check]` argv running. Cite :10926, :10953, :11036 and :11800. The confirming probe is a read of govkit.py:10880-11040.
- **Gate:** add a checklist entry: for every claim that a switch gates a site, list each call site and the nearest `_rerender_on` test that dominates it.

### M3. The node tick's secret scan has no expected population, so an empty enumeration reads green (ids 3, 15)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:787-792`, and the fixture at `:1040-1041`
- **What is wrong:** The fix replaced the blanket rule "an empty population is a dead probe" with expected populations. It declares them only for the two push boundaries ("the pushed range's paths at the prepare, the one ref at the ref-push path"). The node tick's journal and transcript scan (:787-788) declares none. So the new test, "a zero against a non-empty expected population", cannot fire there. The `secret-scan` fixture's broken-enumerator case names no boundary.
- **Consequence:** A broken enumerator at the node tick reads zero matches over nothing, and the witness can read clean. That population holds the most secret-shaped text.
  - The skeptic re-graded id 3 from high to medium. Its claim about the prepare and ref-push boundaries does not hold as written.
  - A node-tick hit only raises an owner item and refuses no push, so the effect is contained.
- **Fix (skeptic judged it sound):**
  - Declare the node tick's expected population: the journal files and transcripts present on the node, counted apart from the scanner's own walk.
  - Rule that an expected population a boundary cannot produce is a dead probe.
  - Add a node-tick broken-enumerator case to `secret-scan` that stubs only the scanner's enumerator and expects red.
- **Gate:** add a checklist entry under zero-witness-over-an-unnamed-population: every scan population names its expected population and the source it comes from.

### M4. The prepare's expected population comes from the same range the scan reads (id 22)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:782-783`, `:789-792`, `:1040-1043`
- **What is wrong:** The prepare scans "the commits in the pushed range and the tracked files and memory/ they carry". Its expectation comes from "the pushed range's paths", which is the same range. An empty expectation now reads "none carried" and passes. The fixture cases this diff added (:1041-1043) are both green paths. The broken-enumerator case (:1040) does not say whether the expectation breaks with the enumerator.
- **Consequence:** A wrongly computed range (for example, a base resolved to HEAD) empties both sets. The prepare then reads green while the push still sends commits. Before the fix this case was a dead probe. The guard shares state with what it guards.
- **Fix (skeptic judged it sound):**
  - Derive the expectation independently of the scanner's enumerator, for example from the refspec's old and new object ids as the push will send them. Those are non-empty whenever the push carries commits.
  - Add a fixture: the range enumerator is stubbed empty while the push carries one commit, and the witness must read a dead probe.
- **Gate:** add a checklist entry: a witness's expectation may not be computed by the code path it checks.

### M5. life.quiesce no longer refuses a withdraw or supersede of a landed build (id 4)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:453`, and the transition table at `:493-494`
- **What is wrong:** The base text refused every request once a push had been made. HEAD refuses only a pause, with an exception for a build waiting at deploy.released. A withdraw or supersede of any other landed build falls through to "withdraw or supersede → life.notify". That covers a build mid-Deploy (deploy.distill to deploy.unlease) and a build under at-landing or at-landing-maintain-owns.
- **Consequence:** life.notify posts "withdrawn" for code already on main. life.close records a transition the table allows only "before the push". The build's Deploy items and its life.* items run toward two different terminal transitions.
- **Fix (skeptic judged it sound):** Restore "a push already made → refused: the build has landed" for every request, with the deploy.released hold as its only exception. Add a fixture: withdraw a build at deploy.distill and expect the refusal, not life.notify.
- **Gate:** add a checklist entry: every life.* arm is checked against the transition table's preconditions.

### M6. The release hold's owner item has three keys, and the withdraw path names a lease with no producer (ids 5, 12, 21)

- **Where:**
  - `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:333`, `:452-453`
  - `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:429-430`, `:1044-1047`
- **What is wrong:** The same owner item is keyed three ways:
  - life.quiesce opens it "unless one is open", keyed by (build, request).
  - The supervisor's sweep raises it "once per (build, landed SHA)" and does not check for an open item.
  - deploy.released's non-verified arm says "the same owner item" and names no key.

  life.quiesce also says life.* runs "under the request's own run lease" after deploy.unlease. No lease grammar or `[schedule]` entry produces that lease, and the actor is still "executor", which no longer exists under close-only. None of life.quiesce's new arms has a fixture: the landed-pause refusal, the waiting-build withdraw, and the post-unlease lease.
- **Consequence:** Take a withdraw during the wait, then the ceiling passing. The result is two open owner items for one wait, which the owner can resolve differently. That contradicts the event-wait fixture's "only one", and the fixture plants no withdraw, so it cannot see the duplicate. The post-unlease withdraw path has no lease producer and no driver, so round 2's C10 finding is still partly standing.
- **Fix (skeptic judged it sound):**
  - Key the item once, by (build, landed SHA), at life.quiesce, deploy.released and the sweep. Carry the request as a field, not part of the key. Each producer checks for an open item first.
  - Have the supervisor take the request's run lease when it reads a life.request for a build that has no lease, and declare that lease in layer-runtime `[schedule]` beside the event wake.
  - Extend event-wait with three cases:
    - a withdraw during the wait, then the ceiling passing, leaves one owner item;
    - a pause of a landed build is refused;
    - a withdraw after deploy.unlease runs under the request's lease.
- **Gate:** add a checklist entry under append-without-an-idempotence-key: every owner item kind declares one key, and every producer cites it.

### M7. The release-verify-failed ask is keyed two incompatible ways (ids 7, 11)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:225`, `:241-244`, `:382`
- **What is wrong:** maintain.file keys every ask "by (reading, offender key)" and sets the offender key to (SHA, environment). Maintain's key is therefore (release-verify-failed, SHA, E). release.route keys its ask by (SHA, E) alone. Yet :225 says the ask "joins release.route's", and :241-243 says Maintain uses "the key release.route files its own ask under".
- **Consequence:** One red verify under roll-forward or roll-back leaves two open asks. The promised "seen" row join cannot happen, and the owed one-ask fixture would be red against the design as written. Round 2's second-key finding is fixed only in part.
- **Fix (skeptic judged it sound):** Pick one key and use it at both writers. Either release.route files under (release-verify-failed, SHA, E), or maintain.file drops the reading from this ask's key. State the key once and cite it from the other site.
- **Gate:** the same checklist entry as M6: one declared key per record kind, cited by every writer.

### M8. A second keep of the same row cannot be written, so a re-kept row is proposed every week (ids 8, 13)

- **Where:**
  - `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:211`, `:258-259`, `:262-263`
  - `layer-memory.md:329-331`
- **What is wrong:** The keep record is one "per (ledger kind, id)", keyed "(ledger kind, id) with its date", and written through `record`. `record` refuses a different value under an existing key unless the kind's lifecycle versions it, and the keep record declares no lifecycle. loop.propose proposes a kept row again once review.loop.window-days have passed, so a second keep with a later date is reachable, and `record` refuses it.
- **Consequence:** loop.price keeps deriving the row's state from the first keep. The row is proposed again every week, and loop.file adds a `seen` row each week. The owner's later keep has nowhere to go.
- **Fix (skeptic judged it sound):** Key the keep record by (ledger kind, id, disposition date), or declare it versioned per (ledger kind, id) with the newest date in force. Have loop.price read the newest keep. Add a case to the keep fixture: keep, pass the window, keep again, and expect no proposal.
- **Gate:** add a checklist entry: every new record kind written through `record` declares its key and whether it is versioned.

### M9. deploy.released's witness is keyed by SHA alone, against the runtime's per-build witness (id 14)

- **Where:**
  - `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:333` (Proven by)
  - `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:713-714`
- **What is wrong:** layer-runtime keys each event-wait instance by (event, SHA, build) and witnesses it by build. deploy.released's 'Proven by' cell still names "the slot's exit record, keyed by SHA, with its outcome", and that carries no build. The exit record may also be for a later SHA than the one the build landed.
- **Consequence:** The position engine reads one exit record as deploy.released done for every build its SHA contains, whether or not that build's instance ran. A skipped build then shows deploy.released done, and deploy.close has no driver.
- **Fix (skeptic judged it sound):** Make the witness per build: the wake's record keyed by (build, exit record's SHA), with the outcome, citing the exit record. Keep the landing record under the other two `build.closes` values.
- **Gate:** add a checklist entry: an item's witness key carries every component of its runtime instance key.

### M10. The event-wait fixture does not exercise the arms it guards (id 19)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:1043-1047`
- **What is wrong:**
  - The fan-out case plants two builds landed in one SHA. The rule (:712-714) wakes builds whose landed SHA the record's SHA contains, and no case covers two builds at different SHAs.
  - The sweep case has no negative arm: no wait answered before the ceiling, and none still under it.
  - Unlike its siblings at :1032, :1035 and :1039-1040, the fixture names no stub it is seen red against.
- **Consequence:** These broken versions all pass the fixture:
  - a fan-out that matches the SHA by equality, which is round 2's M7 scenario;
  - a sweep that raises an item for every landing older than the ceiling;
  - a sweep that ignores the ceiling.
- **Fix (skeptic judged it sound):**
  - Plant build X at S1 and build Y at S2, a descendant of S1, write one exit record for S2, and assert that both close.
  - Add a wait answered within the ceiling and one still under it, and assert the sweep raises nothing for either.
  - Name the stubs it is seen red against: a fan-out keyed by SHA equality, and a sweep that ignores the wait's state.
- **Gate:** a design-fixture lint: every fixture names at least one stub it is seen red against.

### M11. The keep fixture checks only the first keep, not its expiry (id 20)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:262-263`, against `:258`
- **What is wrong:** The fixture checks only that a kept row is left out of the next loop.propose. loop.propose leaves a kept row out only until review.loop.window-days pass, or until the row records a new catch or false red. No case plants either condition.
- **Consequence:** A proposer that treats a keep as permanent passes the fixture. The keep's expiry rule has no check that can fail. This has the same shape as round 2's M5.
- **Fix (skeptic judged it sound):** Add two cases: a keep dated more than review.loop.window-days ago, and a kept row with a catch after the keep's date. Assert that loop.propose proposes both, seen red against a proposer that omits every row with a keep record.
- **Gate:** add a checklist entry: every "until X" clause in a rule gets a fixture case where X has happened.

## Low

### L1. Runtime's reader table omits the sweep's keys (id 16)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:429-430`, `:717`, and the table at `:851-863`
- **What is wrong:** The new `[supervise]` sweep reads `build.release-ceiling`, and through it `build.closes`. The table "Existing keys Runtime reads, without re-declaring them" lists neither key. `[contract]` (:826) names that table as Runtime's reads, and the `policy-and-journal` invariant (:812) requires a reader for every behaviour.
- **Consequence:** A coverage check derived from Runtime's declared reads misses this dependency, so a change to either key passes Runtime's checks unnoticed. The effect is limited to a record's table.
- **Fix (skeptic judged it sound):** Add a row: release hold ceiling, `build.release-ceiling` and `build.closes`, carried by v2's catalogue.
- **Gate:** a lint that every policy key named in a layer's prose appears in that layer's reader table.

review-shape kind=diff-review round=3 intensity=light at=synth raw=22 confirmed=21 refuted=1 unverified=0 blocker=0 high=1 medium=19 low=1 agents=9 out-tokens=129908

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/gotchas/one-run-claim-recorded-as-agreed.md:44 | medium | medium | confirmed | The probe's check() (compared record :619-626 at HEAD) adds the row to `matched` and then returns early when 're-measured here' appears anywhere in the row. In layer-expansions at HEAD, rows :77 (Readings), :112 (Versions) and :120 (Inline copies) have a non-empty 'Both runs' cell and no research-<layer>-a/b.md citation. In each, 're-measured here' sits only in another cell, beside a one-run figure. So the probe counts these three rows and checks none of them, and the gotcha's 'green once each row cited each run's line' (:44-49) overstates what was checked. The gotcha's own fix line requires that 'every "both runs" cell cites ... or says "re-measured here"'. That puts the exemption on the cell, and layer-expansions:65 limits re-measuring to 'a claim one run made'. The probe was rewritten in this diff, so the defect is in scope. The effect is contained to three record rows. | sound | fixture-passes-by-finding-nothing |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:240 | medium | medium | confirmed | At HEAD, govkit.py:10926 runs `if not _rerender_on: ... continue` before the early hole probe at :10953. The only other update-path probe, :11800, iterates `_hu_late`, which is filled only at :11036 inside that same gated loop. (The call at :5454 is in a different command.) So GOVKIT_RERENDER=0 also declines the hole probes, and leaves only the [check] argv running. This diff changed gap-deploy-13 (gap-register:240) from 'the last two' to 'declines only the last three', which lists hole probes among the sites the switch does not decline. It also added the gotcha's 'Update still runs ... each [[hole]] discharge probe (run_hole_probes, near lines 10953 and 11800)'. Both statements are wrong about the tree. | sound | - |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:790 | high | medium | confirmed | The headline mechanism is not established. layer-runtime:790-792 derives each push boundary's expected population 'from what the push carries: the pushed range's paths at the prepare, the one ref at the ref-push path'. Nothing says that comes from the scanner's own enumerator. Under the rule as written, a broken enumerator gives a zero against a non-empty expected population, which is a dead probe. That matches the fixture at :1040, so the prepare and ref-push parts do not hold. The node-tick part is real and the diff introduced it. The base rule 'an empty population is a dead probe' covered every population, the node tick's journal and transcripts included. The replacement declares expected populations only for the two push boundaries. The node tick has no declared expectation, so no rule makes its zero a dead probe, and a broken enumerator there can read green over nothing. A hit at the node tick only raises an owner item and refuses no push, so the effect is contained: medium, not high. | sound | zero-witness-over-an-unnamed-population |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:453 | medium | medium | confirmed | At base, life.quiesce's Then said 'a push already made → refused: the build has landed' for every request. At HEAD (flow-steps:453) it says 'a push already made → a pause is refused', and makes an exception only for a build waiting at deploy.released. A withdraw or supersede of a landed build not at that wait therefore falls to 'withdraw or supersede → life.notify'. That covers a build mid-Deploy and a build under at-landing or at-landing-maintain-owns. life.notify then posts 'withdrawn' to dependents for code already on main, and life.close records a transition that the table at :493-494 allows only 'before the push'. The diff introduced this regression. | sound | - |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:453 | medium | medium | confirmed | At HEAD, life.quiesce (flow-steps:453) opens the hold's owner item 'unless one is open ... keyed by (build, request)'. The supervisor's sweep (layer-runtime:429-430) raises it 'once per (build, landed SHA)' and does not check for an open item. deploy.released's non-verified arm names no key. So a withdraw followed by the ceiling passing yields two owner items, against the event-wait fixture's 'only one' (:1047). A grep of layer-runtime, layer-memory, v2 and flow-steps finds 'the request's own run lease' only at flow-steps:453. No [schedule] entry or lease grammar produces it, and life.quiesce's actor is still 'executor'. This diff introduced all of it. | sound | - |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:429 | medium | low | refuted | The finding inverts the condition at layer-runtime:365. The line says the node tick 'starts the supervisor when none beats under a live run lease'. In the idle fleet the finding describes, no supervisor beats under a live lease, so the node tick STARTS one, and that supervisor's beat runs the build.release-ceiling sweep (:424-431). Nothing in [supervise] or [schedule] says the supervisor exits or is withheld when no build lease exists. The design needs it running with no build lease anyway: it fires cadence items whose os-scheduler host is the node tick (:697-707), and it observes the exit record's event to run the wait 'under its wake's own run lease' (:713-716). So the sweep has a driver in the idle case too. | unsound | - |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:225 | medium | medium | confirmed | At HEAD, layer-expansions:225 keys maintain.file's ask 'by (reading, offender key)' and sets only the offender key to the exit record's (SHA, environment). Maintain's key is therefore (release-verify-failed, SHA, E). release.route (:382) keys its ask 'by (SHA, E)', with no reading. The paragraph at :241-243 says Maintain files 'keyed by (SHA, environment)' and calls that 'the key release.route files its own ask under'. That is a third statement, and it contradicts :225's. The diff introduced both the :225 witness clause and the :241 paragraph, so the one ask key is now stated in two incompatible ways, and the promised join into a 'seen' row does not follow from the keys as written. | sound | - |
| 8 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:259 | medium | medium | confirmed | The keep record is new in this diff. :211 makes it 'per (ledger kind, id)', and :259 keys it '(ledger kind, id) with its date'. layer-memory:329-331 says `record` is idempotent: a different value under an existing key is refused, or versioned only where the kind's lifecycle says so. No lifecycle is declared for the keep record. loop.propose (:258) proposes a kept row again once review.loop.window-days have passed since the disposition. A second keep then carries a new date under the same (kind, id) key, so `record` refuses it, and loop.price keeps deriving the row's state from the first keep. The owed fixture (:262-263) covers only a first keep. | sound | - |
| 9 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:240 | medium | medium | confirmed | I verified this against govkit.py at HEAD. In _cmd_update's per-kit loop, `if not _rerender_on: ... continue` at :10926 comes before the first run_hole_probes call at :10953. _hu_late is filled only at :11036, inside that same gated loop, so the second call (:11799-11800) iterates an empty dict when GOVKIT_RERENDER=0. Only run_kit_check (:10015, :11214) runs whatever the switch says. Base gap-deploy-13 said 'declines only the last two' and did not mention hole probes. The diff's text adds two wrong claims: the register's 'declines only the last three' of five kinds, with hole probes among the ungated ones, and the gotcha's 'Update still runs ... each [[hole]] discharge probe' (foreign-code-runs-on-the-ambient-credential.md:31-34). Both claims are new, and both are wrong about the tree. | sound | foreign-code-runs-on-the-ambient-credential |
| 10 | seams | memory/gotchas/one-run-claim-recorded-as-agreed.md:46 | medium | medium | confirmed | I extracted the corrected probe from the compared record (:587-680) and ran it against layer-expansions.md at HEAD. It printed 'rows read: 52; rows the predicate matched: 44' and 0 findings. Its check() increments `matched` first and then returns whenever 're-measured here' appears anywhere in the row (:620-623). With that phrase blanked out, it reports exactly 3 findings: Readings (:77), Versions (:112) and Inline copies (:120). In each of those rows the phrase qualifies a count in another cell, and the 'Both runs' cell cites neither run. The class's own rule (gotcha:36) says 'Every "both runs" cell cites a line in each return, or says "re-measured here"', so it is scoped to the cell. That makes the gotcha's new claim at :46-47, 'green once each row cited each run's line', false for three rows, and the printed 'matched' count includes those rows. | sound | one-run-claim-recorded-as-agreed |
| 11 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:225 | medium | medium | confirmed | At HEAD, layer-expansions.md:225 still gives maintain.file's witness as 'the ask, keyed by (reading, offender key)'. The fix only adds that for release-verify-failed the offender key is (SHA, environment). Taken literally, Maintain's key is (release-verify-failed, SHA, E). release.route's row at :382 keys its ask by (SHA, E). Yet :225 says the ask 'joins release.route's', and :241-243 says Maintain uses 'the key release.route files its own ask under'. Both tuples were added by this diff (base :225 had no release clause), so it is a partial fix of round 2's two-key finding. The two writers' keys do not match, so the owed one-ask fixture cannot hold as written. The effect is contained to one ask kind. | sound | - |
| 12 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:452 | medium | medium | confirmed | At HEAD, flow-steps.md:452 (life.quiesce) opens the owner item 'unless one is open', keyed by (build, request). layer-runtime.md:429-430 (the supervisor's sweep) raises the owner item 'once per (build, landed SHA)'. flow-steps:333 calls the ceiling arm's item 'the same owner item', and states no key for the outcome arm. Both keys are new in this diff. The sweep's once-per key does not cover an item life.quiesce opened, so a withdraw followed by the ceiling yields two items for one wait. The event-wait fixture (layer-runtime:1045-1047) plants no withdraw, so it cannot catch this. | sound | append-without-an-idempotence-key |
| 13 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:259 | medium | medium | confirmed | The keep record is new in this diff. It is declared 'per (ledger kind, id)' (layer-expansions:211), and loop.file writes it 'keyed by (ledger kind, id) with its date' (:259). layer-memory.md:330-331 says record refuses 'a different value under an existing key', or versions it only where the kind's lifecycle says so, and no lifecycle is declared for the keep record. loop.propose (:258) re-proposes a kept row once review.loop.window-days have passed since the disposition, so a second keep of the same row is reachable. That write is refused, the state stays derived from the first date, and the row is proposed again each week. The owed keep fixture (:262-263) covers only a single keep. | sound | append-without-an-idempotence-key |
| 14 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:333 | medium | medium | confirmed | At HEAD, flow-steps.md:333's Proven-by cell for deploy.released is still 'the slot's exit record, keyed by SHA, with its outcome', which carries no build. This diff made layer-runtime.md:713-714 say each event-wait instance is 'keyed by (event, SHA, build) and witnessed by build, so a skipped key never skips a second build'. The diff also widened the Does cell to fan out 'once for each waiting build', but it left the witness keyed by SHA alone. So the item's declared witness contradicts the runtime's per-build witness, and one exit record reads as done for every build its SHA contains. | sound | - |
| 15 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:790 | medium | medium | confirmed | At base, the rule was 'An unresolved value or an empty population is a dead probe', which covered every population. At HEAD, layer-runtime.md:789-792 says each boundary declares its expected population 'from what the push carries: the pushed range's paths at the prepare, the one ref at the ref-push path'. Only a zero against a non-empty expected population is now a dead probe. The node tick's journal and transcript scan (:787-788) is not a push and declares no expected population, so an empty enumeration there has no rule that makes it dead. The secret-scan fixture's broken-enumerator case (:1040-1041) names no boundary. This diff introduced the gap. | sound | - |
| 16 | seams | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:430 | low | low | confirmed | At HEAD, layer-runtime.md:429-430 ([supervise]) has the supervisor read `build.release-ceiling` to raise a waiting build's owner item, and :717 says the same. The table 'Existing keys Runtime reads, without re-declaring them' at :851-863 lists neither `build.release-ceiling` nor `build.closes`. [contract] at :826 names that table as the keys Runtime reads, and the `policy-and-journal` invariant at :812 asks for a reader for every behaviour. The sweep is new in this diff, so the gap is in scope. Its effect is limited to a record's reader table. | sound | - |
| 17 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md:622 | high | medium | confirmed | I extracted the probe from the compared record (lines 587-680) and ran it on layer-expansions.md at HEAD. It printed 'rows read: 52; rows the predicate matched: 44', then 'findings: 0'. On a copy with the phrase 're-measured here' blanked out it reported 3 findings: Readings (:77), Versions (:112) and Inline copies (:120). In each of these rows the 'Both runs' cell carries no return citation, and the phrase sits in a different cell. check() at :622 tests the phrase anywhere in the row, after it has already counted the row as matched. As a result layer-expansions:672-673 ('Every [agreement] row that credits both runs cites each run's line') is false for these rows. The gotcha's rule (one-run-claim-recorded-as-agreed.md:35) only lets the 'Both runs' cell say 're-measured here'. The probe and that claim are new in this fold. The damage is three uncited rows in a design record plus a probe that over-reports what it matched, so I grade it medium rather than high. | sound | - |
| 18 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:450 | high | high | confirmed | At HEAD, _cmd_update (it starts at govkit.py:8777) calls derive_parity_lines at :9658 whenever tally has adopter-owned rows. derive_parity_lines calls measure_contract_parity at :6111. That function substitutes the adopter's file for `{own}` and runs it through subprocess.run(..., cwd=str(target)) at :6064-6065. No GOVKIT_RERENDER guard sits around it. tools/memory-tree/kit.toml declares such probes, for example `python3 {own} --check` and `bash {own} --print-index-set`, so the adopter's own code runs. layer-expansions:450 (kits.offer) and gap-register:240 both say update runs 'five kinds' and that the mode refuses 'all five'. Neither names this sixth site. The gotcha's fixture list (foreign-code-runs-on-the-ambient-credential.md:48-50) plants nothing in a contract-probed file. The sandbox design therefore misstates the execution surface that dShippedRelease will build from. | sound | - |
| 19 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:1044 | medium | medium | confirmed | At HEAD, the `event-wait` fixture (layer-runtime.md:1043-1047) plants only 'Two builds landed in one SHA both close on one exit record'. The rule at :712-714 fans out to builds whose landed SHA the record's SHA contains, so a fan-out that matches by SHA equality passes. The ceiling case asserts that 'one owner item opens ... and only one' when no record arrives. It has no case for a wait answered before the ceiling or still under it, so a sweep that ignores the wait's state passes. Unlike its siblings at :1032, :1035 and :1039-1040, it names no stub it is seen red against. The fixture is new in this fold. The effect stays inside a design fixture's coverage. | sound | - |
| 20 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md:262 | medium | medium | confirmed | At HEAD, layer-expansions.md:262-263 says the keep fixture only checks that a kept row is omitted from the next loop.propose, seen red against a pricer that ignores keep records. loop.propose at :258 omits a kept row only until review.loop.window-days have passed since the disposition, or until the row records a new catch or false red. No case plants a lapsed keep or a new catch, so a proposer that treats a keep as permanent passes. The fixture sentence is absent at base 67c79f7 and was added in this diff. The effect is contained to fixture coverage. | sound | - |
| 21 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:453 | medium | medium | confirmed | At HEAD, flow-steps:453 (the life.quiesce row, added in 5e139d377) has life.quiesce open deploy.released's owner item 'unless one is open', keyed by (build, request). layer-runtime:429-430, also added in this diff, has the supervisor's sweep raise the same wait's owner item 'once per (build, landed SHA)', and it has no 'unless one is open' clause. So a withdraw during the wait and the later ceiling sweep produce two items under two keys. The event-wait fixture at layer-runtime:1044-1047 plants only the unlease, two builds in one SHA, and no exit record. It plants no withdraw or supersede and no pause of a landed build. A grep of the build's records finds no other fixture for the lifecycle controls' new arms. | sound | two-answers-to-one-question |
| 22 | verification | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:792 | medium | medium | confirmed | layer-runtime:782-783 (HEAD) has the prepare scan 'the commits in the pushed range and the tracked files and memory/ they carry'. :789-792, added in this diff, derive the expected population from 'the pushed range's paths', which is the same range. An empty expectation now reads 'none carried' and passes. Before the fix (base text) an empty population was always a dead probe. So a range computed wrong, which empties both sets, now reads green while the push still sends commits. The fixture cases this diff added at :1041-1043 are both green paths. The broken-enumerator case at :1040 does not say whether the expectation breaks with the enumerator. That is the guard sharing state with what it guards, which the charter's [class] rule forbids. | sound | - |
