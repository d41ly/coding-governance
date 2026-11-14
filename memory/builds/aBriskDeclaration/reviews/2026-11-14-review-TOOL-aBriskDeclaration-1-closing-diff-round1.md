**Serves:** diff-review TOOL-aBriskDeclaration-1

# Closing diff review, round 1: the cumulative diff of TOOL-aBriskDeclaration-1 landing on main

Provenance: a Tier-2 diff review at intensity full, run on 2026-11-14 on `branch/inspiring-mahavira-6b2db9`. Five finder lenses ran first (gov-diff-reviewer). Five skeptic batches followed (gov-skeptic), then this synthesis (gov-synthesizer). Neither `specs` nor `context` was supplied, so the lenses had only the range's commit messages to judge intent.

**Reviewed range:** `846d51d39de6bd14174032a338234604273afd8d...35127e6179811a32fdd136669dfd883a477be5cd`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No blocker or HIGH survived. One medium and two low items stand, and each has a fix a skeptic judged sound. None of them changes runtime behaviour. The medium item is a stale exemption in the sidecar pin registry: arm A5 now exercises a branch the registry still calls unarmable. The two low items are a self-contradicting sentence in the `--dispatch` guide paragraph and a missing fixture for the new order-verb reader's unterminated last line.

## Review shape

The review ran at intensity full: raw 5, confirmed 4, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.80.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |

Adjudicated tally by item: 3 items, 0 blocker, 0 high, 1 medium, 2 low.
Adjudicated tally by raw confirmed finding: 4 findings, 0 blocker, 0 high, 1 medium, 3 low.
The two counts differ because ids 1 and 5 describe one defect and form one item.

## Run integrity

The run is complete.
Lenses: 5/5 returned, 0 DIED.
Skeptic batches: 5/5 returned, 0 DIED.
Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
Fixes on confirmed findings: 4 judged sound, 0 judged UNSOUND, 0 judged INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED.
Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
Lens notes: none supplied, so every lens ran on the kit's generic brief.
Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
Intent: neither `specs` nor `context` was supplied, so the lenses had only the range's commit messages.
Checklist: 51 items, acquired by the harness from `--for-diff 846d51d39de6bd14174032a338234604273afd8d..35127e6179811a32fdd136669dfd883a477be5cd`, split across the five lenses as security 11, correctness 10, seams 10, verification 10, intent 10.
By design: 1 invariant from the checklist's by-design block.
Shown to synthesis: 1 refuted finding, 0 same-address pairs.
Dispositions: unclassed refuse; 51 class slugs handed; 175 leg names read from `tools/gate-legs.json`.

## MEDIUM

### M1 — Arm A5 exercises the `--dispatch` no-usable-python refusal, but the pin registry still exempts that branch as unarmable (id 2)

- **Where:** `tools/unattended/unattended.test.sh@ba1ce4cb:8036` (arm A5, lines 8031-8036), the refusal at `tools/unattended/unattended.sh@cf37c7ce:14517`, and the pin row `unattended.sh 49 15` at `tools/unattended/unarmed-branches.txt@f118c2c1:70`, whose reason is at lines 56-58.
- **What is wrong:** This diff adds A5. It overrides `resolve_python` in a subshell, drives `init_spec_token_check` and `run_spec_token_check` to `state=nopython`, and asserts the refusal. The branch is therefore now exercised from the suite's fixture. The pin's reason says `resolve_python` "cannot be made to fail from the suite's fixture without hiding every python launcher from PATH", and that is now false. A5 asserts only `the inline resolver found no usable python`, without the `--dispatch: ` prefix. `check-arms.py` takes the whole literal run before `$SPEC_TOKENS_CLI` as the signature and tests `b["sig"] in l`, so A5 does not arm the branch. The STRANDED check compares only the first 24 characters, `--dispatch: the inline r`, and that text is not on A5's line either, so check-arms does not even report the arm as stranded.
- **Consequence:** The arm and the pin are two disconnected records. The shrink-only registry keeps a permanent exemption, with a false reason, for a branch that is armed. If the refusal is reworded so that it drops the shared phrase, A5 becomes the only check, and the registry still describes the branch as unarmable. That misleads whoever next touches the pin file or this refusal. No wrong result ships, so the effect is contained (binding grade medium).
- **Fix (judged SOUND by the skeptic):** In A5, assert the full signature text, `--dispatch: the inline resolver found no usable python: none of its candidates runs, so the declared spec-token checker cannot run`. In the same change, remove the row `unattended.sh 49 15` and its reason prose from `tools/unattended/unarmed-branches.txt`, because check-arms enforces pinned-and-armed as a red. Run check-arms and confirm that the branch reads ARMED.
- **Left-shift gate:** Widen the `harness arms (fail branches armed or pinned)` leg's STRANDED check. It should report a pinned or unarmed branch when any 24-character window of its signature appears in the suite, not only the signature's head. A partial quote like A5's would then surface as stranded, and the pinned-and-armed red would follow once the quote is completed.

## LOW

### L1 — The `--dispatch` paragraph still says the spec-token checker runs after every cheap refusal, two lines above the new text that says it starts before two of them (ids 1, 5)

- **Where:** `memory/guides/UNATTENDED-VERBS.md@714f43b8:238` and its byte-equal kit copy `tools/unattended/VERBS.template.md@714f43b8:238`. The same stale order is in the arm header at `tools/unattended/unattended.test.sh@ba1ce4cb:7934`, which reads "THE SPEC-TOKEN CHECKER RUNS AFTER EVERY CHEAP REFUSAL".
- **What is wrong:** Line 238 is unchanged and still says "After every cheap refusal and before the claim read it runs the DECLARED spec-token checker". At base it matched the next sentence, "It runs last because it costs a tree-wide scan". This diff (S5, and S8 in 4fed38fe1) moved the start: `init_spec_token_check` is called at `tools/unattended/unattended.sh@cf37c7ce:14828`, before `read_open_passes`. Two cheap refusals now sit between the start and the read: the generator pairing at :14877 and condition 1, the sibling-path refusal, at :14894. Each now waits for the started checker in `remove_spec_token_check`. The diff replaced the next sentence with lines 240-244, which say the checker is "started just before the open-pass reader", so the kept sentence now contradicts them. S7/S8 promised to make every comment that states the old order true, and these three places were missed. AC8 greps only the one retired sentence, so it cannot catch them.
- **Consequence:** A reader who trusts line 238 will think a generator-pairing or condition-1 refusal returns without any checker running. The next change that moves a refusal inherits the old order from that sentence. Runtime behaviour is unchanged, so this is prose only. Both findings carry binding grade low.
- **Fix (judged SOUND by the skeptic, for both id 1 and id 5):** In both guide copies, reword line 238 so that it says the checker's verdict is read, or applied, after every cheap refusal and before the claim read. For example: "After every cheap refusal and before the claim read it applies the verdict of the DECLARED spec-token checker". Alternatively, drop "After every cheap refusal" and leave the ordering to the new sentence. Make the same correction to the header comment at `tools/unattended/unattended.test.sh@ba1ce4cb:7934`. Keep the two guide copies byte-equal past line 1.
- **Left-shift gate:** When an amendment retires a sentence that states an order, the acceptance grep should cover every phrasing of that order in the paragraph, both guide copies and the arm header, not only the retired sentence. Here that means extending AC8's grep to `After every cheap refusal .* runs the DECLARED` and `RUNS AFTER EVERY CHEAP REFUSAL`. Record it as a further instance of the checklist class `amendment-leaves-its-other-half-standing`.

### L2 — No fixture covers the order-verb reader's unterminated last line (id 3)

- **Where:** `tools/unattended/unattended.sh@cf37c7ce:4843`, the `|| [ -n "$line" ]` clause of `order_verb_of`'s new `while IFS= read -r line` loop, and the ten A1 plants at `tools/unattended/unattended.test.sh@ba1ce4cb:7978-7987`.
- **What is wrong:** This diff replaced the base's `grep -m1` reader with a builtin `read` loop. The `|| [ -n "$line" ]` clause is the only reason the loop sees a final line with no trailing newline. All ten A1 plants end in `\n`, and so does the only other order-verb fixture, `dispspec` at `tools/unattended/unattended.test.sh@ba1ce4cb:934`. The finder's probe ran `order_verb_of` on a file whose last bytes are `**Status:** SPECCED · rev-1 · order 7` with no newline. It printed `with=[7]`, and with the clause deleted it printed `without=[]`. No assertion in the suite notices that change.
- **Consequence:** If the clause is dropped, a `**Status:**` header on an unterminated last line reads empty. The code's own comment calls that the worst outcome, because it silently skips the whole order gate. In a real spec the header sits near the top with body text after it, so the path is unusual. The defect is a missing test, not wrong shipped behaviour (binding grade low).
- **Fix (judged SOUND by the skeptic):** Add an eleventh A1 plant written with no trailing newline, for example `printf '# t\n\n%s · order 7' "$bd_h" > "$TMP/.git/bd/p11"`, and add `p11=[7]` to the pinned expected string. Run it red once with the `|| [ -n "$line" ]` clause deleted, to confirm that the arm fails.
- **Left-shift gate:** Add a checklist entry for this class. Whenever a reader is moved onto `while read ... || [ -n "$line" ]`, its arm must include a plant whose last line has no newline, observed red with the clause removed. A shell-hygiene check could also flag a `read` loop whose arm fixtures are all newline-terminated.

## Refuted (1), for the record

- **id 4 (intent, refuted):** The finder claimed the spec was flipped CLOSED while AC3, AC4, AC12 and the red-then-green observation of arms A1 to A6 were still owed. The skeptic found the facts right but the sequence the one `memory/guides/BUILD-METHOD.md` requires: the main loop observes the owed arms after the closing diff review and before the bar and the land. It is not reinstated, regraded or counted. It is not a twin of any confirmed finding, because no confirmed finding concerns the acceptance ledger or the CLOSED flip.

review-shape kind=diff-review round=1 intensity=full at=synth raw=5 confirmed=4 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=1 low=3 agents=11 out-tokens=54932
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/guides/UNATTENDED-VERBS.md:238 | low | low | confirmed | The cited line is unchanged in the diff. It was accurate at the base, where the base text said the checker 'runs last' after every refusal. The diff then moved the start: tools/unattended/unattended.sh@cf37c7ce:14828 calls init_spec_token_check before read_open_passes. That puts two refusals between the start and the read, the generator pairing at :14877 and the sibling-path refusal (condition 1) at :14894, and each now calls remove_spec_token_check, which waits for the started checker. The diff also added lines 240-244 saying 'started just before the open-pass reader'. So line 238's 'After every cheap refusal ... it runs the DECLARED spec-token checker' now contradicts the lines two below it. That holds in memory/guides/UNATTENDED-VERBS.md:238 and the identical tools/unattended/VERBS.template.md:238. The test header at tools/unattended/unattended.test.sh@ba1ce4cb:7934 ('THE SPEC-TOKEN CHECKER RUNS AFTER EVERY CHEAP REFUSAL') is now just as stale. The diff made all three inaccurate, so the finding is in scope. Runtime behaviour is unaffected, which makes this low: prose only. | sound | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 2 | seams | tools/unattended/unattended.test.sh@ba1ce4cb:8036 | medium | medium | confirmed | This diff adds A5 (tools/unattended/unattended.test.sh@ba1ce4cb:8031-8036). It overrides resolve_python inside a subshell, drives init_spec_token_check and then run_spec_token_check to state=nopython, and asserts the refusal text from tools/unattended/unattended.sh@cf37c7ce:14517. So the branch is now exercised from the suite's fixture. The pin reason at unarmed-branches.txt:56-58 says resolve_python 'cannot be made to fail from the suite's fixture without hiding every python launcher from PATH', and that is now false. check-arms.py signature() takes the longest literal run before $SPEC_TOKENS_CLI, so the signature is the whole '--dispatch: the inline resolver ... cannot run'. armed_signatures/run test `b["sig"] in l`, and A5's line holds only 'the inline resolver found no usable python', so it does not arm the branch. The stranded head is the first 24 characters, '--dispatch: the inline r', which is also absent from that line, so check-arms does not even report it as stranded. The pin row 'unattended.sh 49 15' (line 70) stays in force with a stale reason, and the arm and the pin are not linked to each other. The effect is contained to a misleading registry, with no wrong result, so the grade is medium. | sound | - | gate:harness arms (fail branches armed or pinned) |
| 3 | verification | tools/unattended/unattended.sh@cf37c7ce:4843 | low | low | confirmed | order_verb_of at tools/unattended/unattended.sh@cf37c7ce:4843 now reads the file with a `while IFS= read -r line \|\| [ -n "$line" ]` loop. This diff introduced that loop in place of the base's grep-based reader (base line 4833). The `\|\| [ -n "$line" ]` clause is the only thing that makes the loop see a final line with no trailing newline. All ten A1 plants at tools/unattended/unattended.test.sh@ba1ce4cb:7978-7987 are written with a trailing `\n`. I grepped the suite for any other order-verb fixture that lacks a final newline and found none: dispspec at tools/unattended/unattended.test.sh@ba1ce4cb:934 ends its file with `\n` too. So deleting the clause would leave every assertion green, and the coverage gap is real. Grading it low: in a real spec the `**Status:**` header sits near the top with body text after it, so a header as the unterminated last line is unusual. The finding is a missing test, not wrong behaviour in the shipped code. | sound | - | new:unterminated-last-line-left-unplanted |
| 4 | intent | memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md:3 | medium | - | refuted | The facts are right, but the sequence they describe is the one the build method requires, so it is not a defect. The acceptance ledger does list AC3, AC4 and AC12 as owed to the main loop, along with the red-at-base-then-green observation of each new arm. Commit 35127e617 does change only the spec's status cell, the README and LIVE.md. But memory/guides/BUILD-METHOD.md (line 285, 'Observe the owed arms before the bar') gives that observation to the main loop as a step after the build passes and the closing diff-review. In that step the main loop observes each `New arm:` red on its staged break and green once restored, and records both in the unit's acceptance ledger under a `Pass: none` commit, before the bar and the land. The ledger also says the second pass setting the spec CLOSED as its last change is the expected handoff, once F1 and F2 carry their RESOLVED marks. This diff is the pre-land subject of that closing review, and nothing has landed on main. The claim that the suite 'reds on main' unnoticed does not hold either: the bar (run-gates.sh, wired into remote CI) runs the suite legs before the lander pushes. The risk of an arm passing vacuously is exactly what the still-owed red/green observation covers. The finder reports a scheduled later step of the close as a defect in the diff. | unsound | staged-break-substitutes-a-synthetic-value | - |
| 5 | intent | tools/unattended/VERBS.template.md:238 | low | low | confirmed | Line 238 of tools/unattended/VERBS.template.md, and the byte-equal memory/guides/UNATTENDED-VERBS.md, still says 'After every cheap refusal and before the claim read it runs the DECLARED spec-token checker'. At base that sentence matched the next one, 'It runs last because it costs a tree-wide scan'. This diff (4fed38fe1, S8) replaced that next sentence with 'It is started just before the open-pass reader and read after condition 1 ... a refusal between the two waits for it'. That makes the kept sentence false about when the checker runs, so the paragraph now contradicts itself. The diff introduced the contradiction, so it is in scope. It is prose in a guide with no effect on behaviour, so it is low. AC8 greps only the retired sentence and cannot catch it. | sound | - | class:amendment-leaves-its-other-half-standing |
