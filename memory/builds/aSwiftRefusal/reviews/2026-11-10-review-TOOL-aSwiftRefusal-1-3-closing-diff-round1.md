**Serves:** diff-review TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3

# Closing diff review, round 1: aSwiftRefusal units 1 to 3, the cheap refusals first, the order gate's deferral, and the open-pass release

2026-11-10 · Tier-2 · on `branch/clever-babbage-44839c` · the cumulative diff landing on main · adversarial fan through `tier2-review.js`: 5 finder lenses (gov-diff-reviewer), then 5 skeptic batches (gov-skeptic), then this synthesis (gov-synthesizer).

**Reviewed range:** `ae6735c1f237423022016714b3da193f8ed971b7...17308b6c30a624c929cac714c19d756f51d2c1c6`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No blocker or high survived. Four medium and three low items stand, and each has a fix. The largest is that the new deferral predicate disagrees with two other readers of the same question: `--rescope`'s idempotence (M1) and check 23 of `check-unattended.sh` (M4). The other mediums are coverage gaps: ten region-3 assertions carry no floor (M2), and the `--audit` half of the deferral skip has no arm (M3).

## Review shape

The review ran at intensity full: raw 9, confirmed 9, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 blocker, 0 high, 4 medium, 3 low (7 items).
Adjudicated tally by raw confirmed finding: 0 blocker, 0 high, 6 medium, 3 low (9 findings).
Ids 2, 3 and 6 are merged into one item (M2). All three say the -1 and -2 region-3 arms raised no floor.
Every id keeps its bracketed binding grade. Id 7 was re-graded by its skeptic from medium to low, and that binding low stands.

No finding was refuted, so no twin is flagged.

## Run integrity

- Lenses 5/5 returned, 0 DIED.
- Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 8 judged sound, 0 judged UNSOUND, 1 judged INSTANCE-ONLY (id 8, curing the cited instance and leaving its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (id 7).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: neither `specs` nor `context` was supplied, so the lenses had only the range's commit messages.
- Checklist: 51 items, acquired by the harness from `--for-diff ae6735c1f237423022016714b3da193f8ed971b7..17308b6c30a624c929cac714c19d756f51d2c1c6`, each assigned to exactly one of 5 lenses (security 11, correctness 10, seams 10, verification 10, intent 10).
- By design: 1 invariant from the checklist's by-design block.
- Refuted findings shown: 0. Same-address pairs shown: 0.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Every stage returned and every counter that could mark a hole is zero, so this run is complete. The security lens's zero is evidence of absence within its 11 checklist items.

## MEDIUM

### M1. A same-reason re-defer after a re-dispatch writes no row, so the unit stays undeferred (id 1)

- **Where:** `tools/unattended/unattended.sh:14166` (`check_unit_deferred`), against `verb_rescope`'s idempotence loop at `:14000-14006`.
- **Defect:** `check_unit_deferred`, added by this diff, decides deferral from the LAST dispatch-or-defer row for the unit. `verb_rescope` treats `rescope · item defer <unit> · reason <r>` as already recorded when any earlier row matches it exactly, whatever the row order. After the rows dispatch, defer 'set aside', dispatch, a second `--rescope --act defer --reason 'set aside'` prints "amendment already recorded, unchanged" and writes nothing. The last row stays a dispatch, and the predicate answers "not deferred".
- **Impact:** the spec reads DEFERRED and the operator is told the deferral is recorded. The order gate (`:14371`) still refuses every later-order unit, and `read_open_passes` (`:14116`) keeps all of the unit's keys reserved, so siblings get condition-1 refusals. A fresh reason works around it.
- **Fix** (judged SOUND): make the two rules agree. Either have `verb_rescope`'s idempotence skip the defer act when a dispatch row for the unit follows the matching defer row, so a fresh defer row is appended, or keep the idempotence and refuse with text saying the deferral needs a new `--reason`. Add a test arm for defer, re-dispatch, then a same-reason re-defer.
- **Left-shift:** the new arm is the gate for this instance. The class `two-answers-to-one-question` belongs on the checklist, so the next predicate over RUN.md rows is checked against every writer's idempotence rule.

### M2. The -1 and -2 region-3 arms add 10 assertions that no floor pins (ids 2, 3, 6)

- **Where:** `tools/unattended/unattended.test.sh:7653-7708` (the arms), `:19172` (`FLOOR_ASSERTIONS`), `:19378` (`FLOOR_SHARD_3`).
- **Defect:** the TOOL-aSwiftRefusal-1 arm adds hit, miss, hit, hit, miss, and the -2 arm adds five hits, all unconditional inside region 3's new `if in_shard 3` block. `FLOOR_SHARD_3` stays at 405. `FLOOR_ASSERTIONS` rose 3256 -> 3266 and `FLOOR_SHARD_4` 383 -> 393, both credited only to -3's region-four arm. The -1 and -2 commit messages name no floor. The file's convention is to raise the floor for every arm group, and -3 did so for its own.
- **Impact:** the floor is a shrink-only `-ge` pin on the executed count (`:19440-19443`). If these 10 assertions are deleted or become unreachable (an early `fi`, a moved seam like the `fi`/`if in_shard 3` cut this diff adds, a shard guard), both floors stay green. These arms are the only coverage that the spec-token checker runs after the cheap refusals and that a deferred sibling is admitted. They are also the stated reason commit 3e8ef1ab2 removed the order-gate pin (check 49 ordinal 22) from `unarmed-branches.txt`.
- **Fix** (judged SOUND for all three ids): raise `FLOOR_SHARD_3` 405 -> 415 and `FLOOR_ASSERTIONS` 3266 -> 3276, each with a RAISED comment naming TOOL-aSwiftRefusal-1 (5) and -2 (5), counted off the arms' own lines. Confirm the counts in a sharded run. Then delete one region-3 hit and run `GATE_JOBS=1 bash tools/unattended/unattended.test.sh` with shard 3 selected, to see the floor go red.
- **Left-shift:** a new class, `arm-group-added-without-its-floor`. Its gate is a check that every hunk adding `hit`/`miss` lines in a region also moves that region's `FLOOR_SHARD_<n>` and `FLOOR_ASSERTIONS` in the same range.

### M3. The `--audit` half of the deferred-unit skip has no arm (id 5)

- **Where:** `tools/unattended/unattended.sh:14116-14119` (the skip in `read_open_passes`), read by `print_audit` at `:8657`.
- **Defect:** the -3 commit and its spec say `--audit` stops counting a deferred unit's keys, through the shared reader. Every `left out as deferred` assertion (`unattended.test.sh:9117`, `:9121`, `:9126`) runs through `--dispatch`. The suite's `item defer` rows (`:7690`, `:9112`, `:17957`, `:18049`) never feed `run --audit` (`:9206-9394`). The terminal skip, by contrast, has an `--audit` arm (about `:9281-9290`).
- **Impact:** the code is correct today. If `--audit` stopped using the shared reader, or the `current` filter interacted badly with the deferral, the suite would still pass. The keepalive could then be handed a STALLED kill order for a set-aside unit.
- **Fix** (judged SOUND): in region four, on the same fixture, dispatch ARCH-tRun-1, append the `rescope · item defer` row and set the spec to DEFERRED, then assert the audit output lists ARCH-tRun-1 as neither open nor STALLED. Set the spec to INPROGRESS and assert it is listed again. Raise `FLOOR_ASSERTIONS` and `FLOOR_SHARD_4` by the arm's count.
- **Left-shift:** the class `observed-by-claim-no-arm-discharges`. Every verb a commit body says a shared-reader change affects gets its own arm.

### M4. Check 23 charges a sibling's admitted write to the deferred unit (id 8)

- **Where:** `tools/unattended/unattended.sh:14116` (`read_open_passes` releases a deferred unit), against check 23 in `check-unattended.sh` (about `:4497-4541`).
- **Defect:** after -3, condition 1 admits sibling B on deferred unit A's path. Check 23 still treats A's window as open. A has no next anchor, so the window runs to HEAD. `pass_commit` finds no commit naming A, and the dodged-join scan (`git log anchor..HEAD -- path`) finds B's non-ABSORB `Pass: B` commit. It prints "the only join this check has was dodged: A wrote work/held" on stdout, the channel the leg's header says must stay silent on a conforming tree. Before this diff A's open key made condition 1 refuse B, so the diff made this reachable. Spec -3 calls check 23 "the stricter direction", but the outcome is a misattributed red, not a stricter one.
- **Impact:** this is the scenario the build exists for (dOrderedCharter units 31 and 37). The leg goes red on a conforming tree and blames a unit that wrote nothing. The path is narrow: it needs a deferral plus an overlapping sibling.
- **Fix** (judged INSTANCE-ONLY; this is the skeptic's class-level fix): have check 23's no-commit branch ask the same release question `read_open_passes` asks, terminal by spec status or `check_unit_deferred`. Move `check_unit_deferred` into the shared kit library so `check-unattended.sh` can call it. For a released unit, end its window at the release (its defer row, or the status flip), so no path a sibling was legally admitted to after that point is charged to it. Add `check-unattended.test.sh` arms for both a DEFERRED unit and a WONTDO unit whose path a sibling then writes, and assert that no dodged-join line names the released unit.
- **Finder's proposal (cures the cited instance alone):** have only the dodged-join branch ask `check_unit_deferred`, or end only a deferred unit's window at its defer row, with one DEFERRED arm. It leaves the terminal (WONTDO) release unhandled.
- **Left-shift:** the class `two-guards-one-question-two-answers`. The shared predicate in the kit library is the gate: both guards call one function, so they cannot answer differently.

## LOW

### L1. The -1 ordering arm has no positive control for its stub checker (id 7)

- **Where:** `tools/unattended/unattended.test.sh:7672` and `:7679`.
- **Defect:** neither ARCH-tRun-5 dispatch made under the `swift-stub.py` key gets past a cheap refusal, and the ARCH-tRun-4 dispatch runs under a blank key. No line shows the stub refusing when it is reached. The two `miss` lines (a plain `grep -qF`) pass whether or not it runs.
- **Impact:** binding grade low, re-graded down from medium by the skeptic. The `hit` lines still fail if the checker block moves back above the order gate, and the F3 group exercises the same key-read path with its own stub (hit at `:7636`). The arm passes vacuously only if the key goes entirely unread.
- **Fix** (judged SOUND): add a positive control. With the stub declared, run a dispatch that clears every cheap refusal (for example ARCH-tRun-5 on a disjoint path once ARCH-tRun-4 is dispatched) and `hit` the spec-token refusal text. Count it in `FLOOR_SHARD_3`.
- **Left-shift:** the class `fixture-passes-by-finding-nothing`. Every `miss` arm pairs with a `hit` that proves the missed text can appear.

### L2. `--check-commit`'s header claims an agreement the deferral skip broke (id 4)

- **Where:** `tools/unattended/unattended.sh:14212-14218`, with the verb body at `:14223-14231`.
- **Defect:** the header says `--check-commit` asks the same openness predicate as `--dispatch` and `--audit`, "so this verb cannot call a pass open that they call closed". It still calls `check_pass_open` alone and prints `o` for a deferred unit's pass, which `read_open_passes` now releases. The comment explains only the terminal exception.
- **Impact:** no behaviour change, since the base also printed `o`. The false invariant misleads the next change. A records commit naming a deferred unit without a Pass trailer is refused as an open dispatched pass that the dispatch verb says reserves nothing.
- **Fix** (judged SOUND): add a sentence beside the terminal exception saying the deferred skip is left out on purpose, and why (a `Pass:` trailer naming a deferred unit is still graded against its declaration). Or, if the hook should agree with the other verbs, have it ask `check_unit_deferred` for `o` rows and add a check-commit arm for a deferred unit.
- **Left-shift:** the class `amendment-leaves-its-other-half-standing`. A change to a shared reader greps for every comment that claims parity with it.

### L3. The `--audit` contract still says only "not terminal" (id 9)

- **Where:** `tools/unattended/VERBS.template.md:130-131` and its byte-equal copy `memory/guides/UNATTENDED-VERBS.md`.
- **Defect:** the `--audit` entry lists a unit whose rows are open "and whose spec is not terminal". The diff updated only the `--dispatch` paragraph, and `--audit` now drops a deferred unit too, noting it only on stderr.
- **Impact:** documentation drift with no runtime effect. An operator or the idle-wake reading the contract expects a PROGRESSING or STALLED line for a DEFERRED unit with open rows, and gets none.
- **Fix** (judged SOUND): extend the `--audit` sentence in both copies to "whose spec is neither terminal nor deferred (DEFERRED with its latest defer row after every dispatch row)", keeping the two files byte-equal past the marker line.
- **Left-shift:** the class `amendment-leaves-its-other-half-standing`. The existing parity check keeps the two copies equal, but nothing ties the contract to the reader's callers.

review-shape kind=diff-review round=1 intensity=full at=synth raw=9 confirmed=9 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=6 low=3 agents=11 out-tokens=62658
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/unattended/unattended.sh:14166 | medium | medium | confirmed | I read unattended.sh:14000-14006. verb_rescope's idempotence loop returns 0 ('amendment already recorded, unchanged') when any earlier rescope row matches `rescope · item defer <unit> · reason <r>` exactly. It does not look at row order. The new check_unit_deferred (14166-14172, added by this diff) uses awk to keep only the LAST dispatch-or-defer row for the unit. So with the sequence dispatch, defer 'set aside', dispatch, a second `--rescope --act defer --reason 'set aside'` writes no row, the last matching row stays a dispatch, and the predicate returns 1. The diff's new paths make this reachable: the order gate (14371) and read_open_passes (14116) both call the predicate. The unit therefore stays blocking and keeps its keys reserved, even though the operator was told the deferral is recorded. The effect is wrong refusals on one path, and a fresh reason works around it, so medium. | sound | - | class:two-answers-to-one-question |
| 2 | correctness | tools/unattended/unattended.test.sh:7653 | medium | medium | confirmed | I read the diff of unattended.test.sh. The -1 arm adds hit, miss, hit, hit, miss and the -2 arm adds five hit lines. All 10 are unconditional inside region 3's new `if in_shard 3` block. FLOOR_SHARD_3 is still 405 (line 19378). FLOOR_ASSERTIONS went 3256 -> 3266, and its RAISED comment credits only -3's region-four arm. The check at line 19443 is `-ge FLOOR`, so if these 10 arms became unreachable (for example through the region seam this diff adds), the floor would not catch it. Spec -1 section 7 says 'the floor is a minimum, and these arms only add to it'. That is a choice, but it is not on the by-design list, and it differs from how -3 pinned its own arm. The test still runs; the only loss is that the gate would not notice these arms going missing, so medium. | sound | - | new:arm-group-added-without-its-floor |
| 3 | seams | tools/unattended/unattended.test.sh:19172 | medium | medium | confirmed | The diff adds two arms to region 3 of tools/unattended/unattended.test.sh (just after the F3 if/else, before the `end REGION 3` fi). They run unconditionally in shard 3. -1 has 5 assertions (hit, miss, hit, hit, miss) and -2 has 5 more (run_swift_case followed by five hits), so 10 in all. The only floor edits in the range are FLOOR_ASSERTIONS 3256->3266 and FLOOR_SHARD_4 383->393, and both name only TOOL-aSwiftRefusal-3. FLOOR_SHARD_3 is still 405. The -1 and -2 commit messages say nothing about a floor. The floor is a shrink-only pin on the executed count (line 18854), so deleting the 10 region-3 assertions would leave the count at the new pin and stay green. Those arms are the stated reason commit 3e8ef1ab2 removed the order-gate pin from unarmed-branches.txt. The effect is contained to coverage, so medium. | sound | - | new:arm-group-added-without-its-floor |
| 4 | seams | tools/unattended/unattended.sh:14212 | low | low | confirmed | read_open_passes (unattended.sh ~14116) now calls check_unit_deferred and drops a deferred unit's keys. --check-commit (~14223-14231) still calls check_pass_open alone and prints 'o' for such a pass. Its header comment still says 'this verb cannot call a pass open that they call closed' and explains only the terminal-status skip, so for a deferred unit the comment is now false. A later line says the verb 'answers which declaration grades this commit, not which paths are reserved', but the comment never names the deferred case. Behaviour is unchanged from base, where a deferred pass was also 'o'. The only effect is a misleading comment, so low. | sound | - | class:amendment-leaves-its-other-half-standing |
| 5 | verification | tools/unattended/unattended.sh:14116 | medium | medium | confirmed | print_audit (unattended.sh:8657) reads `read_open_passes "$rel" current`, and -3 added the check_unit_deferred skip inside that reader (:14116-14119). The commit body and spec -3 both say --audit stops counting a deferred unit's keys. The only `item defer` rows in the suite are at test.sh:7690 (the -2 order-gate arm), 9112 (the -3 --dispatch arm) and 17957/18049 (the tCarry rescope arms). None of them feeds `run --audit` (:9206-9394). The terminal skip, by contrast, does have an --audit arm (around :9281-9290, the CLOSED unit that used to read STALLED). So the audit half of this change has no arm. The code is correct today, so the gap is contained. | sound | - | class:observed-by-claim-no-arm-discharges |
| 6 | verification | tools/unattended/unattended.test.sh:19378 | medium | medium | confirmed | The diff adds 10 assertions at test.sh:7668-7704, after the STC if/else closes and inside the newly opened `if in_shard 3` block: the -1 group is hit, miss, hit, hit, miss and the -2 group is five hits. They are unconditional within region 3. The only floor change in the diff is FLOOR_ASSERTIONS 3256 -> 3266 plus FLOOR_SHARD_4 383 -> 393, both commented as -3's 10 region-four assertions. FLOOR_SHARD_3 stays at 405. The floor is a minimum on the executed count (FLOOR=${!_fv} at :19440-19441), and the file's convention is to raise it for every arm group. Without that, these 10 assertions can vanish without tripping the pin. | sound | - | new:arm-group-added-without-its-floor |
| 7 | verification | tools/unattended/unattended.test.sh:7672 | medium | low | confirmed | True as stated, but the effect is smaller than claimed. In unattended.test.sh, the -1 arm (the lines after the F3 block, about 7650-7680) declares swift-stub.py. Neither ARCH-tRun-5 dispatch made under that key gets past a cheap refusal, and the ARCH-tRun-4 dispatch runs under a blank key. So no line in the arm shows the stub refusing when it is reached, and the two `miss` lines (miss() at line 264 is a plain grep -qF) pass whether or not the stub ever runs. However, the `hit` lines are not independent of order. At ae6735c1 the checker block came before the order gate and its refusal returned first, so the order-gate and condition-1 texts could not appear. The diff moved the whole block below the sibling loop, including the `[ -f "$ROOT/$SPEC_TOKENS_CLI" ]` refusal. A PFX path that does not resolve would therefore still fail these `hit` lines if the block were moved back up. The arm passes vacuously only when the key goes entirely unread, and the F3 group runs that same read path in gov's tree with its own stub (stub-tokens.py, hit at 7636). What remains is a missing positive control, contained to the test's power. That is low. | sound | - | class:fixture-passes-by-finding-nothing |
| 8 | intent | tools/unattended/unattended.sh:14116 | medium | medium | confirmed | Traced through the code. After -3, read_open_passes (unattended.sh about 14116) drops a unit for which check_unit_deferred holds, so condition 1 admits sibling B on A's path. In check-unattended.sh, check 23 then sets dstop to HEAD because A has no next anchor (about 4497). pass_commit finds no commit naming A. The dodged-join scan (4524-4541) runs `git log anchor..HEAD -- path`, finds B's `Pass: B` commit, which is not ABSORB, and prints the dodged-join line naming A on stdout with printf, not report. The header (line 15) says anything printed on that channel is a violation, so the leg goes red and blames A, which wrote nothing. Before this diff the sequence could not happen for a deferred A, because A's open key made condition 1 refuse B. So the diff made it reachable. Spec -3 line 54 says only that a deferred unit's window 'still counts there, the stricter direction'. It does not consider a sibling's admitted write being charged to the deferred unit, and none of the harness's BY DESIGN items covers it. Graded medium: the result is a visible false red on a narrow path (deferral plus an overlapping sibling), not a silent wrong pass. | instance | two-guards-one-question-two-answers | class:two-guards-one-question-two-answers |
| 9 | intent | tools/unattended/VERBS.template.md:130 | low | low | confirmed | The `--audit` entry at tools/unattended/VERBS.template.md:130-131 still says it lists a unit whose rows are open "and whose spec is not terminal". The diff leaves that sentence alone in both copies and changes only the `--dispatch` paragraph. In the code, `--audit` (unattended.sh:8657) reads `read_open_passes "$rel" current`. After this diff, `read_open_passes` (14103-14123) runs `check_unit_deferred` after its terminal skip, leaves out every key of a deferred unit, and only reports it on stderr. So a DEFERRED unit with open rows no longer gets a PROGRESSING or STALLED line, and the contract no longer matches what the verb prints. This diff introduced the mismatch. It is a documentation drift with no runtime effect, so the grade is low. | sound | - | class:amendment-leaves-its-other-half-standing |
