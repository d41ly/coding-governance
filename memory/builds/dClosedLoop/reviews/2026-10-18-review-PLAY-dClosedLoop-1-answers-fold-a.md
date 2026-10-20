**Serves:** diff-review PLAY-dClosedLoop-1

# Review: the away pass's answers fold, run A

Tier-2 diff review, round 1, run A of two independent runs on the same diff. Synthesis by gov-synthesizer from the skeptic-confirmed findings.

Range: a9b00addda62eb4d3b3dd5fc77b9dff3139a9cc4...fe3d09aba3a34e46d1651a941af94f3772c99b0d

## Verdict: CLEAN WITH FIXES

No finding is a blocker. Two high findings must be fixed before dSafePassage or dWellOiledMachine is specified: the inverted transient-auth route (item H1) and the early retirement of the PEP 701 ban (item H2). Each of the other nine items is contained to design text or to one record.

This run is not complete as a full review. Its intensity was light, so the security and intent lenses were not run, and their classes were swept only through the checklist shares.

## Review shape

Intensity light, raw 15, confirmed 11, refuted 4, unverified 0 (0 uncertain), precision 0.73.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 8 | 6 | 2 | 0 | 0 | 0.75 |
| seams | yes | 4 | 3 | 1 | 0 | 0 | 0.75 |
| verification | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |

Adjudicated tally by item: 11 items (0 blocker, 2 high, 5 medium, 4 low). By raw confirmed finding: 11 (0 blocker, 2 high, 5 medium, 4 low). Each item covers exactly one finding. Findings 4 and 14 describe the same stale [final] block. They stay as two items because their binding grades differ (medium and low), and findings are merged only within one grade. Item L4 is limited to what finding 14 adds, the missing atlas guard.

Run integrity:
- Lenses: 3/3 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 10 judged sound, 1 judged unsound (finding 13, whose skeptic's corrected fix is written below), 0 with none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 2 re-graded by the skeptic (13 from high to medium, 14 from medium to low).
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 27 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 19 items, each assigned to exactly one of 3 lenses (correctness 7, seams 6, verification 6).
- By design: the caller's byDesign list.

Because security and intent were not run, a zero count in those classes is not evidence of absence.

## High

### H1. The transient-auth failure now skips its credential, and the measured contention case has no route (finding 1)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1076`. The same text is in the dWellOiledMachine row at v2:1403 and in the away-pass record's [folded-answers] at `2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:489`.
- **What is wrong:** AP-14's fold turned the transient-auth class into "a transient-auth failure moves to the next" credential. At the base, that class was a same-credential relaunch that does not count against RESUME_ATTEMPTS. It exists because run 1 died on OAuth refresh contention (`research-harness-cli.md:80`). The owner's answer ("setup-token by default, oauth-shared fallback, with api-key as the last owner-selectable option") sets an order of credentials. It does not say a transient failure skips its credential.
- **Consequence:** With the default list `setup-token, oauth-shared`, refresh contention on `oauth-shared` has no next entry, so the measured case now fails the act. A credential that is absent or rejected, such as a node with no setup token, also has no stated route. dWellOiledMachine's spec would inherit the inverted trigger.
- **Fix (judged sound by the skeptic):** Split the two failure classes in v2:1076, the dWellOiledMachine clause and [folded-answers]:
  - An absent, expired or rejected credential moves to the next entry in `runtime.act-auth`'s order.
  - A transient failure relaunches on the same credential under its own cap, outside RESUME_ATTEMPTS, and only then moves on.
  - Add a planted arm for each class: a node with no setup token reaches `oauth-shared`, and OAuth refresh contention relaunches on `oauth-shared`.
- **Left-shift gate:** Add a bug-class checklist entry: "a fold that rewrites a measured failure class must cite the measurement and keep a planted arm for it."

### H2. dSafePassage retires the PEP 701 ban before anything enforces the floor (finding 9)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392`, the dSafePassage floor-step clause.
- **What is wrong:** The clause retires the PEP 701 text ban in `tools/memory-tree/merge-rows.test.sh` "since the floor admits the syntax". The ban exists because `resolve_python` imposes no version floor (merge-rows.test.sh:347-352). dSafePassage adds only a preflight, which `update` runs once. The resolver's below-floor refusal is on dWitnessedBar (v2:1404), the 14th row of the chain, while dSafePassage is the 2nd. The research (`research-python-floor.md:217`) put the ban inside dWitnessedBar's floor arm, so the fold also misstates its own return.
- **Consequence:** Between dSafePassage and dWitnessedBar, a nested same-quote f-string can land in merge-rows.py and pass the bar. On a node below the floor, such as WSL's Ubuntu 22.04 resolving 3.10, the merge driver then fails to start. Git keeps OURS-only content with no markers, so merged data is lost silently. The path is narrow, but the clause misleads dSafePassage's builder.
- **Fix (judged sound by the skeptic):** Choose one:
  - Move the ban's retirement out of dSafePassage's clause and into dWitnessedBar's interpreter-floor-arm clause, worded as the research put it: absorbed by the arm that runs a real interpreter at the floor, and retired only in the unit where the resolver refuses below the floor.
  - Or move the resolver's below-floor refusal into dSafePassage's floor step.

  Required probe: on a node whose resolver returns 3.10 or 3.12, remove the ban, plant a PEP 701 line in merge-rows.py, and show that `merge-rows.test.sh` and a real merge both go red.
- **Left-shift gate:** Under the existing class retirement-inventory-misses-readers-by-value, add a checklist entry: "a retired guard names the condition it guards and the unit whose reader now enforces that condition, and that unit must come no later in the chain."

## Medium

### M1. [final] certifies a pre-retitle run as "re-run at the commit" (finding 4)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:9796`, the [final] block.
- **What is wrong:** fe3d09aba itself wrote [final]'s values: map 2373 nodes, 30877 B, purposes declared 1605, and atlas 2869 sections with 190 decision sections. Those are the counts from before the retitle that the same commit made. Its own message says the map "reads 189 decision sections again". At HEAD, `atlas.py --check` prints 167 records, 2870 sections and 189 decision sections, and `map.py --check` prints 2371 nodes, 30799 B and purposes declared 1603.
- **Consequence:** The block is titled "Every check, re-run at the commit", and the away-pass [folded-answers] cites it as "all green". It certifies a tree state that never existed at the commit. The effect is limited to that one record.
- **Fix (judged sound by the skeptic):** Re-run every [final] check at fe3d09aba and replace the design-map and atlas blocks with the current output. Make the instruments writer refuse to emit [final] unless the run's HEAD equals the commit it names.
- **Left-shift gate:** The writer's HEAD-equals-named-commit refusal is the gate. Plant a [final] written against a stale HEAD and see it red.

### M2. `Gov-Session:` is a rule that no check can fail (finding 5)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:311`, the commits arm in [gates]. The rule is in dWellOiledMachine's clause at v2:1403.
- **What is wrong:** This diff added the `Gov-Session:` trailer ([sites]:136), widened `runs-in` to take a commit ([edges]:171), and required the trailer to be written "as `trace.identity` says". The commits arm still plants only three cases: a missing `Gov-Act:`, an unbound `Gov-Act:` and a mis-typed `Gov-Item:`.
- **Consequence:** Under `act-only`, a commit carrying a harness session id passes every gate, so the privacy setting binds nothing. Under `session`, a commit without the trailer also passes, and `runs-in` from commit to session goes silently empty.
- **Fix (judged sound by the skeptic):** Add two planted arms to the commits gate in [gates] and to dWellOiledMachine's commit-key leg, each seen red:
  - A `Gov-Session:` trailer on a commit made under `trace.identity: act-only` is refused.
  - An act-made commit under `session` without the trailer is refused.
- **Left-shift gate:** This is the class rule-stated-with-no-check-that-fails. Add a checklist entry: "every new trailer or key value in the plan adds a planted arm to [gates] in the same commit."

### M3. [planned]'s macOS trigger widens the owner's AP-34 answer (finding 6)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1425`. The same text is in the instruments record at about line 8076.
- **What is wrong:** The trigger reads "a node registers darwin, or an adopter asks". The owner answered AP-34 with "On a registered node (Recommended)" (away-pass:457). "An adopter asks" comes from the research's trigger (research-python-floor:144). The seven interpretations do not list it.
- **Consequence:** A later reader will take an adopter's request as enough to schedule macOS work, which the owner did not authorise.
- **Fix (judged sound by the skeptic):** Restate the trigger as the owner gave it: "a node registers darwin, and only after dWellOiledMachine dissolves `unattended/`". If the adopter route is wanted, list it in [folded-answers]' interpretations for the owner to confirm.
- **Left-shift gate:** Add a checklist entry: "every folded clause that adds a condition not in the owner's chosen option text appears among the interpretations."

### M4. The AP-31 interpretation lets later builds rely on a floor nothing enforces at launch (finding 10)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:552`.
- **What is wrong:** The interpretation says dSafePassage raises the floor "before any later build, so each may rely on 3.15". The only refusal dSafePassage gives the floor is its step's preflight, run once by `update`. The every-launch refusal (gap-tool-12) is on dWitnessedBar (v2:1404), which lands after dOrderedCharter, dFairHearing and dDeclaredLoop. `tools/lib/resolve-python.sh` checks no version today.
- **Consequence:** A unit in one of those three builds that uses a feature from 3.12 to 3.15 fails with a SyntaxError or ImportError on any node or clone whose resolver picks an older interpreter. The defect is in design text, but it invites that reliance.
- **Fix (judged sound by the skeptic):** Choose one:
  - Put the resolver's below-floor refusal in dSafePassage's floor-step clause, and leave dWitnessedBar the arm that runs a real interpreter.
  - Or restate the interpretation: builds before dWitnessedBar may rely on 3.15 only for code run under the step's preflight, and the resolver's refusal lands on dWitnessedBar.
- **Left-shift gate:** This shares H2's checklist entry, since both come from the floor's declaration and its enforcement landing in different builds.

### M5. Gov's own remote CI gets no 3.15 interpreter when the floor moves (finding 13)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392`, together with `.github/workflows/remote-ci.yml`.
- **What is wrong:** dSafePassage raises gov's floor to 3.15. No unit before dWitnessedBar gives `remote-ci.yml` an interpreter at that floor. The workflow runs `windows-latest` with no setup-python step, and its jobs call `resolve_python` on whatever is on PATH. gap-tool-21 records the missing setup but sits on dWitnessedBar. dShippedRelease's setup step (v2:1408) is for the CI emitted to adopters, not for this workflow.
- **Consequence:** For the three builds before dWitnessedBar, the one CI layer no node can skip checks code written to a 3.15 floor on an older interpreter.
- **Severity:** The finder graded this high. The skeptic re-graded it medium because the claim that every push goes red is not established, which leaves a contained gap that is recorded and closed later. The binding grade is medium.
- **Fix (the finder's fix was judged unsound; this is the skeptic's corrected fix):**
  - Add to dSafePassage's floor-raise clause a setup-python step at the floor, read from its one declaration and pinned by full commit SHA like the workflow's other actions.
  - Put that step in every `remote-ci.yml` job that runs Python: history-audit, bar, held-plan and held.
  - Witness it with a remote-CI run at the raise commit in which each job's log prints the interpreter `resolve_python` chose, at the floor.
  - Move gap-tool-21's remote-CI half to dSafePassage, and leave its floor-arm and parse halves on dWitnessedBar.
- **Left-shift gate:** Add a checklist entry: "a floor raise names every executor of gov's own code (local bar, remote CI jobs, hooks) and the unit that provisions each at the new floor."

## Low

### L1. [planned] says pwsh-launch's gaps wait for its trigger, but they are already in the register (finding 7)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1423`. The matching seventh interpretation says the same.
- **What is wrong:** The sentence says neither plan's gaps join the register until its trigger holds, and cites research sections 3 and 4. Section 4's port-15 to port-17 are already in the register as gap-tool-20 and gap-rt-32 under AP-33. The pwsh bullet (v2:1431-1433) also schedules the resolver and the refusal now.
- **Consequence:** The prose is inaccurate, and a reader might file the same gaps again when the pwsh trigger fires, so each would be owned twice.
- **Fix (judged sound by the skeptic):** Narrow the sentence. macOS's gaps wait for its trigger. pwsh-launch's measured gaps already joined as gap-tool-20 and gap-rt-32 under AP-33, and only its runner adapter waits.
- **Left-shift gate:** Have the register's checker refuse a design sentence that defers a gap id or research gap already present in the register.

### L2. dDeclaredLoop's commit-node clause lost a separator (finding 8)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1395`.
- **What is wrong:** The clause now reads "mapped to `serves` `Gov-Act` to `made-by` and `Gov-Session` to `runs-in`".
- **Consequence:** A reader or an extractor can pair a key with the wrong edge type. The effect is cosmetic, because [sites] states the mapping correctly.
- **Fix (judged sound by the skeptic):** Restore the separator: "`Gov-Unit` and `Gov-Item` mapped to `serves`, `Gov-Act` to `made-by` and `Gov-Session` to `runs-in`".
- **Left-shift gate:** None fits. Add a checklist entry: "a mapping list that grows by one entry is re-read for its separators."

### L3. gap-maint-15's evidence describes a different gap (finding 12)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:353`.
- **What is wrong:** The row cites 3.10 reaching end of life on 2026-10-01 while WSL still resolves it. The floor is 3.11 (end of life 2027-10) or 3.15 (end of life 2031-10), never 3.10. A resolved 3.10 is an interpreter below the floor, which is gap-tool-12's class.
- **Consequence:** A reader sizing dTendedCadence's end-of-life detector from this row is misled about what it closes. The effect is limited to the row's evidence.
- **Fix (judged sound by the skeptic):** Restate gap-maint-15 against the floor itself: nothing files an intake before the floor's end of life, using 3.11's 2027-10 from the research's end-of-life table. Leave the 3.10/WSL observation to gap-tool-12, or cite it there.
- **Left-shift gate:** Add a checklist entry: "a gap's evidence sentence measures the condition its owning unit's detector watches."

### L4. The atlas has no guard against a section wrongly counted as a decision (finding 14)

- **Where:** `memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:9796`, together with the atlas check (`atlas.py:109`, `atlas.py:510-512`).
- **What is wrong:** Like M1, [final] records a green run of the misread state (2869 sections and 190 decision sections, against 2870 and 189 at the tip). Finding 14 adds the point that `--check` has no refusal for a section wrongly picked as a decision. Its only decision guard catches the opposite error, an answer with no decision section. The misread was fixed by retitling one section, with no gate.
- **Consequence:** The next section whose title matches DECISION_TITLE ("answers," or "owner's answers") passes `--check` silently.
- **Severity:** The finder graded this medium. The skeptic re-graded it low because the DECISION_TITLE class predates this diff and the in-scope consequence is a stale transcript with no behaviour affected. The binding grade is low.
- **Fix (judged sound by the skeptic):**
  - Re-run `record_instruments.py` at the tip so [final] shows 189 and 2870. This is shared with M1.
  - In `atlas --check`, refuse a decision section picked from a record outside a declared set of design records. For example, refuse when the record's name matches `instruments` or its Serves kind is not a design record, or pin the decision count against a declared list.
  - Plant the retitle's case, the section titled "The owner's answers, folded" in the instruments record, and record the plant red in [plants].
- **Left-shift gate:** The atlas refusal with its plant is the gate.

review-shape kind=diff-review round=1 intensity=light at=synth raw=15 confirmed=11 refuted=4 unverified=0 blocker=0 high=2 medium=5 low=4 agents=9 out-tokens=101034

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1076 | high | high | confirmed | At the base, v2's dWellOiledMachine row carried 'a transient-auth relaunch class under `runtime.act-auth`' (v2@a9b00addd:1387). That class comes from research-harness-cli.md:80: run 1 died on OAuth refresh contention, and a fresh relaunch needs a transient class that does not count against RESUME_ATTEMPTS. The fold replaced it with 'a transient-auth failure moving to the next' (v2:1076), 'a transient-auth failure relaunching on the next in order (AP-14)' (v2:1403) and 'a transient-auth failure moves to the next' (away-pass:489). The instruments script at 8046-8049 shows this edit directly. The owner's AP-14 words (away-pass:436) are 'setup-token by default, oauth-shared fallback, with api-key as the last owner-selectable option'. They set an order, not a rule that a transient failure skips its credential. Under the default list `setup-token, oauth-shared`, OAuth refresh contention on the last entry now has no next entry, so the measured same-credential relaunch is gone. The case of an absent or rejected credential has no stated route either. dWellOiledMachine's spec would inherit this, which misleads the next change. | sound | - |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:474 | medium | - | refuted | AP-30's option text (away-pass:322) is 'the lander runs each new step on gov first, recorded in its source-mode receipt; gov's own diff is its migration'. The owner chose it. dSafePassage is a gov build that lands in gov's own tree. Its floor step raises the one declaration in that tree, and its up step is a preflight that refuses an interpreter below the floor (v2:1392). The raise therefore reaches gov through gov's own landing diff first, which is the path AP-30 itself names, before any adopter's `update` walks it. dShippedRelease's lander unit (v2:1408) is where the general mechanism gets automated, not the only way gov migrates. No adopter sees the step before gov does, so the 'gov first' claim holds and there is no wrong result or unnamed path. At most the line is loose about which unit it cites. | none | - |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:477 | medium | - | refuted | The window this finding describes is not one the dropped arm would have closed. The research placed the TOML 1.0 arm in dWitnessedBar (research-python-floor.md:217, 'dWitnessedBar ... new TOML 1.0 arm'; gap port-10 owned by dWitnessedBar, :230). That is the same build that carries the below-floor resolver refusal (v2:1404). Keeping the arm would not cover the dSafePassage-to-dWitnessedBar interval, so dropping it opens no exposure. Once the floor is 3.15 at both ends, the floor and the newest interpreter read the same dialect. The research's own premise ('a node running 3.15 accepts files that gov's floor refuses', :11) then no longer holds, so the drop follows from the owner's AP-31. A 3.14 peer before every node has upgraded is the owner's stated direction ('all the nodes will upgrade') and the AP-31 interpretation, not a defect in the fold. The point that the stated reason does not fit the floor-raise template is only about wording: the template's drop does not depend on that sentence. | unsound | - |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:9796 | medium | medium | confirmed | At HEAD the instruments record's [final] (line ~9789) reads 'map: 2373 nodes ... 30877 B ... declared 1605' and 'atlas: derived — 167 records, 2869 sections, 190 decision sections'. `git show fe3d09aba` shows that commit itself wrote those values: it changed 2371/30799/1603 to 2373/30877/1605 and 189 to 190. So the finder is wrong that the commit left [final] unchanged, but that does not matter. The same commit's message says that after the retitle 'the map reads 189 decision sections again'. That commit also added the fence_probe `###` section, so 2869 sections cannot hold at HEAD either. [final] therefore records the pre-retitle run under the title 'Every check, re-run at the commit'. The away-pass [folded-answers] points readers at that block as 'all green'. The effect stays inside one record, which certifies a state that no longer holds. | sound | - |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:311 | medium | medium | confirmed | This diff added `Gov-Session:` to the plan's [sites] commit row (memory-plan:136), widened `runs-in` to commit (memory-plan:171), and added 'with `Gov-Session` written as `trace.identity` says (AP-8)' to dWellOiledMachine's clause in v2:1403. At the base `runs-in` was 'act, claim → session' and had no trailer. The [gates] commits arm (memory-plan:311-312) still plants only a missing `Gov-Act:`, an unbound `Gov-Act:` and a mis-typed `Gov-Item:`. Nothing in the plan's armed gates fails on a missing `Gov-Session:` under `session`, or on one present under `act-only`. The edges arm catches only a trailer whose target resolves nowhere. The [gates] list says it enumerates every check the plan arms, each seen red, so this is a design-level omission the diff made reachable, not unit detail. | sound | rule-stated-with-no-check-that-fails |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1425 | medium | medium | confirmed | The AP-34 fork row (away-pass:326) offers 'on a registered node, after dWellOiledMachine dissolves `unattended/`; now'. The owner's answer, verbatim at away-pass:457, is 'On a registered node (Recommended)'. v2:1425 [planned] reads 'Trigger: a node registers darwin, or an adopter asks, and only after...'. The 'or an adopter asking' arm comes from the research's trigger (research-python-floor:144), not from the answer. The seven interpretations (away-pass ~541-555) do not list it; the only [planned] one concerns AP-17's units and gaps. So the fold widens the owner's trigger without flagging it, and the instruments record (8076) carries the same text. | sound | - |
| 7 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1423 | low | low | confirmed | v2:1422-1424 says neither plan's gaps join the register until its trigger holds, and cites research sections 3 and 4. Section 4's table (research-python-floor.md:207-209) maps port-15 and port-16 to dWitnessedBar and port-17 to the hook shell. The register already holds them as gap-tool-20 (line 215, citing section 4) and gap-rt-32 (line 258, citing section 4), added by this fold under AP-33. The pwsh bullet (v2:1431-1433) also says the resolver and refusal are scheduled now, so the blanket sentence contradicts its own section and the register. The pwsh bullet lists no gaps-once-triggered, which limits how far it misleads, so the effect is a prose inaccuracy. | sound | - |
| 8 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1395 | low | low | confirmed | v2 now reads "`Gov-Unit` and `Gov-Item` mapped to `serves` `Gov-Act` to `made-by` and `Gov-Session` to `runs-in`". The base read "mapped to `serves` and `Gov-Act` to `made-by`". Adding the third mapping dropped the separator after `serves`. The meaning is still recoverable, and [sites] states the mapping correctly, so this is cosmetic. | sound | - |
| 9 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392 | high | high | confirmed | v2:1392's dSafePassage clause retires the PEP 701 text ban in merge-rows.test.sh "since the floor admits the syntax". The ban's own comment (merge-rows.test.sh:347-352) says it exists because `resolve_python` imposes NO version floor. A driver that fails to start leaves OURS-only content with no markers. dSafePassage adds only a preflight in its upgrade step's up. The resolver's below-floor refusal is dWitnessedBar's clause (v2:1404: "refusing below it"). In the chain order dWitnessedBar is the 14th row and dSafePassage the 2nd. That leaves a window where the ban is gone and the condition it guards still holds on any node that has not upgraded. gap-maint-15 names WSL's Ubuntu 22.04 resolving 3.10 as one such node. The owner's "all the nodes will upgrade" (AP-31) is a direction, not an enforcement at merge-driver time. The research (research-python-floor.md:217) has dWitnessedBar's floor arm absorb merge-rows.test.sh:347-356, so the fold also misstates its return. The path is narrow (a nested same-quote f-string landed in the window, run on a node below the floor), but the consequence is silent merge loss, and the clause misleads dSafePassage's builder. | sound | retirement-inventory-misses-readers-by-value |
| 10 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:552 | medium | medium | confirmed | The text is new in this diff: the base away-pass record has no 'rely on 3.15'. dSafePassage's clause (v2:1392) makes the floor's only refusal the step's preflight, run by `update`. The every-launch refusal, the resolver 'refusing below it' with gap-tool-12, sits on dWitnessedBar's row (v2:1404). dWitnessedBar's parent is dDeclaredLoop, so it lands after dOrderedCharter and dFairHearing. `tools/lib/resolve-python.sh` has no floor, minor or version check (grep is empty). gap-tool-21 adds that remote CI sets up no Python. So the claim that 'each later build may rely on 3.15' rests on a floor that no launch-time reader enforces until dWitnessedBar. The defect is contained to design text, but it invites unsafe reliance. | sound | - |
| 11 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:217 | medium | - | refuted | The count is supported by the cited evidence. research-python-floor.md section 2 ('The floor', lines 15-110) states at line 93, under raising the floor now: 'Edits: 8 files, 9 lines, `README.md:90`, `tools/govkit/govkit.py:104-111` and `map_lib.py:17` among them.' So 'eight files at 3.11' paraphrases a census in the cited section, and the finder's claim that the section holds no such count is false. The finder's own grep found 7 files under a narrower pathspec. That does not show the research's measured 8 is wrong; it shows the probes differ. Calling those sites 'declared' matches how the research itself treats them, as edit sites for raising the floor. | unsound | - |
| 12 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:353 | low | low | confirmed | gap-maint-15 is new in this diff: it is absent at the base. The row reads: 'Nothing watches the interpreter floor's end of life: Python 3.10 reached its end on 2026-10-01, and WSL's Ubuntu 22.04 still resolves it.' gov's floor is 3.11 (research section 2 end-of-life table: 3.11 ends 2027-10) or 3.15 after AP-31. It is never 3.10. A 3.10 that WSL still resolves is an interpreter below the floor, which is gap-tool-12's class. A detector watching the floor's end of life would not catch it. The cited fact therefore does not support the gap it names. The effect is limited to the row's evidence. | sound | - |
| 13 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392 | high | medium | confirmed | I checked v2:1392 at fe3d09aba. dSafePassage raises the floor to 3.15, has every reader read the one declaration, and has its up preflight refuse a lower interpreter. No unit in that row gives remote CI an interpreter. The workflow (.github/workflows/remote-ci.yml) runs windows-latest with no setup-python step, and its held-plan and held jobs call resolve_python on whatever is on PATH. gap-tool-21 (gap register:216) records that remote CI sets up no Python, but dWitnessedBar owns it (v2:1404). dShippedRelease's 'Linux job in emitted CI that sets up Python at the floor' (v2:1408) is adopter CI, not this workflow. In the chain table dOrderedCharter, dFairHearing and dDeclaredLoop all come before dWitnessedBar. Across those builds, gov's unskippable CI layer runs below the declared floor. At the base it ran at or above it, because the floor was 3.11 and the bar imports tomllib. So the defect is real and this diff introduced it. The claim that every push goes red is not established: nothing in the plan shows the bar running the up preflight, and the resolver's refusal below the floor only arrives with dWitnessedBar. The established harm is narrower. For a few builds CI checks code written to a 3.15 floor on an older interpreter, and the gap is recorded and closed later. That is contained, so medium. | unsound | - |
| 14 | verification | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:9796 | medium | low | confirmed | fe3d09aba itself rewrote [final]'s atlas line from '2851 sections, 189 decision sections' to '2869 sections, 190 decision sections'. Yet its commit message says the map 'reads 189 decision sections again'. 190 is the count with the old title 'The owner's answers, folded', which matches DECISION_TITLE's 'owner's answers' alternative (atlas.py:109). So the writer ran the checks before the retitle took effect. At the tip that title is gone and the commit added one '### fence_probe.py' heading, so the counts should be 189 and 2870, as the finder says. [final] is labelled 're-run at the commit' and so records a state that does not exist at the commit. atlas.py:510-512 also confirms that the only decision guard refuses an answer that has no decision section, and nothing refuses a wrongly picked one. The DECISION_TITLE class itself predates this diff, however. The consequence that is in scope is a stale transcript inside a record, with no behaviour affected, so low. | sound | - |
| 15 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1077 | medium | - | refuted | The defect predates this diff. At a9b00addd, v2's `platforms.supported` row already listed 'any subset of windows-gitbash, linux, macos, pwsh-launch' ('pending AP-17'), and the base file names no macOS or pwsh adapter unit in any build: a search of the base for macos and pwsh finds only that row. So the fold did not move routing units out of a build. Values with no route existed unchanged at the base, and the diff only added [planned] with its triggers, which carry out the owner's AP-17 and AP-34. [planned]'s statement that neither plan counts in a build is the owner's direction, which the BY DESIGN list covers. | unsound | policy-value-with-no-route |
