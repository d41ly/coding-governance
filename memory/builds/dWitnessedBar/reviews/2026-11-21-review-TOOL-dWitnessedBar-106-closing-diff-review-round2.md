**Serves:** diff-review TOOL-dWitnessedBar-106 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108

# dWitnessedBar — Tier-2 CLOSING DIFF review, round 2

*Node `d`, 2026-11-21. This round reads only the fold of round 1: units TOOL-dWitnessedBar-106, -107 and -108 (two passes, plus the red fix 2648b26dd), which close round 1's six confirmed findings. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 4 spec documents supplied as `specs`, read beside the range's commit messages. The checklist had 75 items, acquired by the harness from `--for-diff a7f2fe03f177..HEAD`, each assigned to exactly one lens: security 15, correctness 15, seams 15, verification 15, intent 15. By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block. Units run no gates and the full bar runs once at the close, so OWED acceptance lines are by design. Product code and its suites were read first.*

**Range reviewed: `a7f2fe03f1775b5e26accacfa88c91c1a70c1a2f...113974a433a11452d4dce7c272cc153e75fef1cc`**

**Round: 2.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER.
One item is HIGH: the new commit-attribution check admits a message whose agent trailer is followed by any plain line, including the drifted `Opus 5.5` value (findings 2, 6, 9).
That item leaves round 1's L2 trailer-drift finding open for every message with text after its trailer.
Round 1's H2 (verify-peer publishing a slot it did not write) is closed for stale slots but not for a concurrent writer (finding 1, MEDIUM).
Round 1's H1 (the policy fail-open) is closed, with one accepted spelling left unarmed (finding 8, LOW).
No confirmed finding stands against the folds of round 1's M1, M2 or L1.
I recommend folding the HIGH item and both MEDIUMs before the landing, each with its arm seen red first.
The three LOWs can be folded or filed.
The review-round line below records this round as NON-CONVERGENT, since the fold introduced new confirmed defects.

## Review shape

Intensity full, raw 9, confirmed 8, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.89.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 6 items (0 blocker, 1 high, 2 medium, 3 low).
Adjudicated tally by raw confirmed finding: 8 (0 blocker, 2 high, 3 medium, 3 low).
The two tallies differ because findings 2, 6 and 9 describe one defect and form one item.
Every confirmed finding keeps its bracketed binding grade.
Finding 1's binding grade is the skeptic's MEDIUM, re-graded from the finder's HIGH.
The refuted finding 5 shares an address with finding 2 but is a different defect (an unread exit status, not the parse's scope), so no twin is flagged.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 8 judged sound, 0 judged UNSOUND, 0 judged INSTANCE-ONLY, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (finding 1, HIGH to MEDIUM).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 1. Same-address pairs shown: 1.
- Dispositions: unclassed is `refuse`; 75 class slugs handed; 219 leg names read from tools/gate-legs.json.

Every count above is zero where it would mark the run incomplete, so this run is complete.

## HIGH

### H1. The attribution check reads `none` when any plain line follows the agent trailer (findings 2, 6, 9)

**Where:** `tools/lib/commit_trailers.py@253aca4e:308`, in `check_message_attribution` (the parse at :305, the `none` return at :309-310).
The inlined copies carry the same code: `tools/unattended/commit_trailers.py@97f03da5:306` and `tools/memory-tree/commit_trailers.py@8485bb36:306`.
The arm that should catch it is `tools/unattended/unattended.test.sh@d85005ad:9792`.

**What is wrong:** the function picks agent lines only from the stdout of `git interpret-trailers --parse`.
That parse reads only the message's final trailer paragraph.
Once any non-trailer line follows the agent's `Co-Authored-By:` line, git sees no trailer block, `agent` is empty, and the function returns `none` before the value check or the last-line check runs.
`main()` maps `none` to exit 0, and `check_commit_message` (`tools/unattended/unattended.sh@ca417ff0:15565-15578`) admits exit 0.
The skeptics reproduced it on four shapes, each returning `('none', 'no Co-Authored-By: trailer naming <noreply@anthropic.com>')`:
the `Opus 5.5` trailer followed by `see above`;
the `Opus 5.5` trailer, a blank line, then prose;
the correct trailer followed directly by prose;
the correct trailer, a blank line, then prose.
The same `Opus 5.5` trailer as the last line is refused, so the check works only when the trailer is last.
Spec 108 §4 defines agent trailers as git's parse, so the code matches its spec text, but together they miss round 1's L2 class-level fix, which asked for a gate on both value and position.
Spec 108 also says a line after the trailer is refused and that AC9 is red when "a trailer that is not last is admitted".
The suite's refusal arms (the AC10 arm at :9792 and the AC9 probe) only ever plant a following line that is itself a trailer (`Commit-Checked:`), so they stay green.
The function's "WHAT IT DOES NOT CHECK" note does not name the gap.

**Consequence:** check 49 admits a commit carrying the exact wrong-value, wrong-position trailer it exists to refuse, as long as text follows the trailer.
Round 1's L2 trailer-drift finding stays open on that path.
Findings 2 and 6 bind at HIGH: a gate misses part of what it claims to check, on the narrower path where the trailer is not last.
Finding 9 binds at MEDIUM: its skeptic weighed the same defect as contained to commit-message metadata, since a commit with no agent trailer is admitted by design.
The item takes the highest grade, HIGH.

**Fix (judged SOUND by the skeptic for each of 2, 6 and 9; merged here):** choose agent lines by scanning the raw message, not by git's trailer parse.
Use the same rules the last-line check uses: CRs stripped, `#` and blank lines dropped, nothing read past the scissors line.
Take every line matching `(?i)^<key>:\s*` that contains the charter's `<address>`.
Return `none` only when no such line exists anywhere in the message.
Otherwise run the value check and the last-line check over those lines, whether or not git parses them as trailers.
Finding 9's fix also treats a non-zero exit from `git interpret-trailers` as exit 2, never as `none`.
The refuted finding 5 found no reachable path where that call alone fails, so this clause is hardening, not a confirmed defect.
Correct spec 108 §4's definition of agent trailers to match, and remove the gap from the function's note.
Add arms to the unattended suite's S10 block and to the AC9 probe, each expecting exit 1 under check 49:
`Co-Authored-By: Fx 2 <fx@example.invalid>` followed by a plain line;
`Pass: none`, then `Co-Authored-By: Fx 2 <fx@example.invalid>`, a blank line and a prose line;
`<expected>`, a blank line, then prose;
`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` followed by prose.
Add a matching case to `commit_trailers.py --fixture`.
Show each case red against the current code first.

**Left-shift gate:** the four arms above in tools/unattended/unattended.test.sh, plus the fixture case, so every refusal clause the spec names has an arm whose following line is not a trailer.
Record the class (a trailer selected through `git interpret-trailers --parse` sees only the final block) in the project's bug-class checklist, so any future trailer reader is reviewed for it.

## MEDIUM

### M1. verify-peer still publishes a slot written by a concurrent bar run (finding 1)

**Where:** `tools/run-gates/verdict_backends.py@d895f6c6:690`, in `run_verify_peer` (the pop at :682, the check at :690, the publish at :705).

**What is wrong:** unit 107 treats any change in the slot's `run_id` between before and after the bar as proof that this run wrote it.
Line 682 pops `GATE_RUN_ID`, so verify-peer never knows the id its own bar will write.
run-gates.sh writes `gate-verdict/<RUN_TREE>` into the common dir, which every worktree of the clone shares (`tools/run-gates/run-gates.sh` 6239-6277).
A concurrent full bar on the same tree that writes last therefore passes the checks at 690, 695 and 702, and its `run_id` is published at 705.
This happens when verify-peer's own bar wrote nothing, failed early, or ran first and was overwritten.
The docstring at 630-632 and spec 107 §5's risk line ("can make S1 refuse a candidate it could have published") both say this case can only cause a refusal.
That is wrong: the reachable outcome is a publish.
The F3 re-read catches a rewrite after the read, not one before it.

**Consequence:** the signed `refs/gov/verdict/<sha>` tag names a run_id that verify-peer did not produce.
The skeptic bounded the effect.
The slot is written only by a run that started clean and did not move (6252-6255), under the same RUN_TREE key, so the other run tested identical file content.
The finder's red-then-GREEN case cannot happen, because a red own bar gives a non-zero rc and line 695 refuses a GREEN slot under a non-zero rc.
So the published verdict always agrees with verify-peer's exit code and comes from a real full bar on the same tree.
The defect is wrong provenance, not a wrong verdict, so MEDIUM (re-graded by the skeptic from the finder's HIGH).
Round 1's H2 is closed for a stale slot and stays open for a concurrent writer.

**Fix (judged SOUND by the skeptic):** give each verify-peer bar a fresh, unpredictable id in place of dropping `GATE_RUN_ID`, for example `nonce = f"vp-{secrets.token_hex(8)}"; env['GATE_RUN_ID'] = nonce`.
run-gates.sh honours it as TS_RUN (line 1645) and unsets it before any leg runs (line 2816).
Require `after == nonce` and `again == nonce` in place of `after and after != before`.
A fresh nonce never repeats, which also settles spec 107 §8 F2.
Extend the peer-stale-slot plant with a stub mode that writes the slot under a run id other than the `GATE_RUN_ID` it was given, and assert `not published`.
Correct spec 107 §5's risk line and the docstring at 630-632.

**Left-shift gate:** the concurrent-writer stub mode above, in the peer-stale-slot plant that the `run-gates gov canary` leg runs, seen red against today's before/after test first.

### M2. `--check-commit` swallows `ATTRIBUTION unarmed`, so a switched-off check reads as passed (finding 4)

**Where:** `tools/unattended/unattended.sh@ca417ff0:15568`, the `0) ;;` branch of `check_commit_message` (15565-15578).

**What is wrong:** `commit_trailers.py attribution` exits 0 for `ok`, `none` and `unarmed` alike (tools/lib/commit_trailers.py@253aca4e:384-385).
`read_charter_trailer` (:272-287) returns an empty expected line, which reads as `unarmed`, when `$ROOT/AGENTS.md` is absent or unreadable, has no `- **Commit trailer:**` line, or has that line with no backticked span.
`check_commit_message` captures the verb's one line in `_at`, and the exit-0 branch drops it.
Exit 2 (`*)`) does echo, so `unarmed` is the only outcome swallowed.
Spec 108 says "a charter with no fact line reads `unarmed` and says so"; the verb says so, but its only consumer drops the line.
The S10 arms assert exit 0 only for messages with no agent trailer, so they cannot see this.

**Consequence:** in a bound run whose charter was renamed, or whose fact line is spelled differently, every agent commit is admitted with the attribution check off, and nothing in the hook output distinguishes it from an `ok` commit.
Nothing wrong is written to the repository, and the effect is contained to attribution, so MEDIUM.

**Fix (judged SOUND by the skeptic):** under `0)`, echo the line when it starts with `ATTRIBUTION unarmed`, for example `case "$_at" in "ATTRIBUTION unarmed"*) echo "unattended: --check-commit did not check attribution: ${_at#ATTRIBUTION unarmed · }" ;; esac`.
Add an arm to tools/unattended/unattended.test.sh that removes the fixture's AGENTS.md fact line and asserts `hit "$out" "did not check attribution"`.
Watch that arm fail first.

**Left-shift gate:** the arm above in the unattended suite; it is an instance of the swallowed-delegate-reads-as-clean class, so a review of any new delegate's exit-0 branch should check every state that shares exit 0.

## LOW

### L1. A trailing space on a correct trailer is refused by the last-line check (finding 3)

**Where:** `tools/lib/commit_trailers.py@253aca4e:322`, in `check_message_attribution`.

**What is wrong:** the value check compares trailer values after `.strip()` (:306-311).
The last-line check strips only CR from the last line and compares it to `expected` exactly (:315-322).
A correct trailer with a trailing space or tab passes the first and is refused by the second, although git's commit cleanup would remove that whitespace before the commit is written.
The consumer comment at tools/unattended/unattended.sh@ca417ff0:15540-15545 says the hook reads the editor's file before cleanup; `-m` and `-F` messages are already stripped, so only editor-composed messages reach this.

**Consequence:** a false refusal (fail 49) whose repair text shows the offending space invisibly.
No wrong admission follows, so LOW.

**Fix (judged SOUND by the skeptic):** normalise the last line the way git's cleanup does, with `line.rstrip()`, before comparing it to `expected`, and keep `expected` stripped as `read_charter_trailer` already does.
Add a planted case with a trailing space that must read `ok`.

**Left-shift gate:** that planted case in the `commit_trailers.py --fixture` set, so the two comparisons inside the function cannot again answer one question two ways.

### L2. The RED half of verify-peer's exit-code agreement has no arm (finding 7)

**Where:** `tools/run-gates/verdict_backends.py@d895f6c6:695`; the plant's stub bar at 1178-1194 and its only RED scenario at 1226.

**What is wrong:** the publish predicate accepts `v.state == "RED" and rc != 0`.
The stub bar's modes are reused, disagree (GREEN, rc 1), red (RED, rc 1) and clean.
No mode writes RED with exit 0, so dropping `and rc != 0` would leave the plant green.

**Consequence:** a later edit could remove that half of the agreement silently, and verify-peer would then sign a RED slot from a bar that exited 0.
The tag would still say RED, and today's code refuses correctly, so this is a test gap only: LOW.

**Fix (judged SOUND by the skeptic):** add a `redok` mode to the plant's stub (verdict RED, rc 0) and a `run_scenario` expecting exit 1 with `['not published', 'the bar exited 0', 'reads RED']`, placed before the 'no verdict published' count.

**Left-shift gate:** the `redok` arm in the peer-stale-slot plant run by the `run-gates gov canary` leg, seen red with `and rc != 0` removed.

### L3. The root dotted-key spelling in `scan_policy_bytes` has no fixture row (finding 8)

**Where:** `.githooks/pre-push@b5c2ab04:1582`, in `scan_policy_bytes`; the FL floor harness at `.githooks/pre-push.test.sh@9fa63b3d:3071-3101`.

**What is wrong:** outside a table header, `scan_policy_bytes` accepts the lhs `"$2.$3"` (a root dotted key such as `verdict.blocks = "every-red"`) or `"$2"` with a `{` value (an inline table).
Revision A holds only `[runtime]`, R uses `[verdict]`/`[hooks]` tables, and R3 uses inline tables.
No revision spells a root dotted key, so breaking the `"$2.$3"` arm would leave every row green.
The finder's probe shows the branch works today.

**Consequence:** if that arm broke, a root dotted key at R would read as "no mention", and with a missing or failing reader `hooks.bypass` and `verdict.blocks` would fall back to the loose default: the fail-open unit 106 closed.
This is a coverage gap on a working branch, so LOW.

**Fix (judged SOUND by the skeptic):** add a revision R4 to the FL harness whose policy file is `verdict.blocks = "every-red"\nverdict.held = "push-selected"\nhooks.bypass = "refused"`, plus the row `AC1 nopy R4 every-red push-selected refused`.
Show it red with the `"$2.$3")` arm removed.

**Left-shift gate:** the R4 row in the `pre-push self-test` leg, so every spelling `scan_policy_bytes` accepts has a row that fails when its arm breaks.

review-shape kind=diff-review round=2 intensity=full at=synth raw=9 confirmed=8 refuted=1 merged=0 unverified=0 blocker=0 high=2 medium=3 low=3 agents=11 out-tokens=99560 trigger=owed shape=- efforts=- role-sha=-
review-round round=2 limit=- prior=2 count=2 state=NON-CONVERGENT

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/run-gates/verdict_backends.py@d895f6c6:690 | high | medium | confirmed | The race is real. In verdict_backends.py, line 682 pops GATE_RUN_ID and line 690 refuses only when `not after or after == before`. Any change of run_id therefore counts as 'this run wrote it', which is what the docstring at 630-632 claims. run-gates.sh writes gate-verdict/<RUN_TREE> into the common dir, which every worktree of the clone shares (6239-6277). So a concurrent full bar on the same tree that writes last passes lines 690, 695 and 702, and its run_id is published at 705. Spec 107 §5's risk line, which says such a run can only cause a refusal, is wrong. The finder overstates the consequence, though. The slot is written only for a run that started clean and did not move (6252-6255), and the RUN_TREE key is the same, so the other run tested identical file content, not 'whatever checkout'. The finder's red-then-GREEN case cannot happen: if verify-peer's own bar ran red, rc is non-zero, and the check at 695 refuses a GREEN slot under a non-zero rc. So the published state always agrees with verify-peer's own exit code and comes from a real full bar on the same tree on the same node. What goes wrong is provenance: the tag names a run_id that verify-peer did not produce, against the docstring and the spec. The verdict itself is never wrong. The effect is contained, so I grade it medium. The fold introduced this, because unit 107 wrote the before/after test that claims to prove authorship. | sound | decision-re-derived-by-a-second-process | class:decision-re-derived-by-a-second-process |
| 2 | correctness | tools/lib/commit_trailers.py@253aca4e:308 | high | high | confirmed | I reproduced it. I imported tools/lib/commit_trailers.py and called check_message_attribution with 'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>' followed by 'see above'. It returned ('none', 'no Co-Authored-By: trailer naming <noreply@anthropic.com>'). The correct trailer followed by a blank line and 'late note' also returned 'none'. The same wrong trailer as the last line is refused, so the check works only when the trailer is last. The cause is line 305: agent lines are chosen from `git interpret-trailers --parse`, which reads only the final trailer block. The last-line check at 314-323 never runs, because 'none' returns first at 309-310. In unattended.sh, --check-commit (15565-15578) treats exit 0 as admitted and fails 49 only on exit 1. So a message carrying the wrong-value, wrong-position trailer that the check exists to refuse is admitted. This is new code from unit 108 (absent at a7f2fe03f). It is the check's own target class, reachable whenever any plain line follows the trailer, so it is a gate that misses part of what it claims to check. I grade it high rather than blocker because the common shape, trailer last, is caught. | sound | - | new:trailer-parse-reads-only-the-final-block |
| 3 | correctness | tools/lib/commit_trailers.py@253aca4e:322 | low | low | confirmed | The fold added this. At tools/lib/commit_trailers.py@253aca4e:306-311, check_message_attribution strips each parsed trailer value before comparing it to the value. At :315-322 it strips only CR from the last line, then compares it to `expected` exactly. So a correct trailer followed by a trailing space or tab passes the value check and is refused by the last-line check. The case is reachable: the consumer comment at tools/unattended/unattended.sh@ca417ff0:15540-15545 says the hook reads the editor's file before git's cleanup, and cleanup would strip that trailing whitespace from the committed message. -m and -F messages are already space-stripped before the hook runs, so the hole is limited to editor-composed messages. The result is a false refusal (fail 49) whose repair text shows the space invisibly. No wrong admission follows, so low. | sound | - | class:two-guards-one-question-two-answers |
| 4 | seams | tools/unattended/unattended.sh@ca417ff0:15568 | medium | medium | confirmed | The fold added this. In check_commit_message (tools/unattended/unattended.sh@ca417ff0:15565-15578), the verb's output goes into _at and the `0) ;;` branch drops it. tools/lib/commit_trailers.py@253aca4e:384-385 returns 0 for ok, none and unarmed alike. read_charter_trailer (:272-287) returns an empty expected line, which reads as unarmed, when AGENTS.md is absent or unreadable, has no `- **Commit trailer:**` line, or has that line with no backticked span. In each of those cases --check-commit admits the commit with no attribution check and prints nothing to tell it from `ok`. Spec 108 line 360 says 'a charter with no fact line reads `unarmed` and says so'. The verb prints the line, but its only consumer swallows it. Exit 2 (`*)`) does echo, so the unarmed case is the only one swallowed. Nothing wrong is written to the repository, but a check that switched itself off reads as passed. The effect is contained to attribution, so medium. | sound | swallowed-delegate-reads-as-clean | class:swallowed-delegate-reads-as-clean |
| 5 | seams | tools/lib/commit_trailers.py@253aca4e:305 | low | - | refuted | The returncode is indeed never read (tools/lib/commit_trailers.py@253aca4e:305), but I could not find a way to reach the fail-open case. With a malformed trailer.* value (I tried `git -c trailer.ifexists=bogus` and `git -c trailer.where=bogus` on interpret-trailers --parse), git only prints a warning, exits 0 and still parses the trailer. A config that git cannot read at all also breaks the earlier `GIT symbolic-ref -q HEAD` in check_commit_message (tools/unattended/unattended.sh ~15532), and that makes the check return 0 before the attribution step runs. A missing git raises FileNotFoundError, exits 1 and is reported as a refusal, so that case fails closed. I found no path where interpret-trailers alone fails, and the finder graded this low, so it is refuted. | instance | swallowed-delegate-reads-as-clean | - |
| 6 | verification | tools/lib/commit_trailers.py@253aca4e:309 | high | high | confirmed | I re-ran the probe by importing tools/lib/commit_trailers.py and calling check_message_attribution with the expected value 'Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>'. Three messages each returned ('none', 'no Co-Authored-By: trailer naming <noreply@anthropic.com>'): the right trailer, a blank line, then prose; the right trailer directly followed by prose; and the 5.5 trailer, a blank line, then 'more'. The 5.5 trailer on its own correctly returned refused. The cause: `agent` is built only from git's trailer parse (lines 305-310), and that parse finds no trailer block once a non-trailer line follows. In check_commit_message, exit 0 falls into `0) ;;`, so the message is admitted. Unit 108 introduced this code, and the base had no check_message_attribution. It contradicts the spec, which says a line after the trailer is refused and that AC9 is red when 'a trailer that is not last is admitted'. The check therefore certifies an attribution rule it does not enforce, but only for messages with text after the trailer. That is a narrow path, so high. | sound | rule-stated-with-no-check-that-fails | class:rule-stated-with-no-check-that-fails |
| 7 | verification | tools/run-gates/verdict_backends.py@d895f6c6:695 | low | low | confirmed | The claim holds. tools/run-gates/verdict_backends.py@d895f6c6:695 publishes when `(v.state == "RED" and rc != 0)`. The stub bar in run_stale_slot_plant (lines 1178-1194) has only the modes reused, disagree (GREEN, rc=1), red (RED, rc=1) and clean. No mode writes RED with exit 0. The only RED scenario, at line 1226, expects the tag to be published, and it would still publish if `and rc != 0` were dropped. Nothing else in the plant covers RED with rc 0, so that mutation stays green. Both the predicate and the plant are new in this range: the base a7f2fe03f has no peer-stale-slot plant and no rc agreement. The consequence is a test gap only. Today's code refuses correctly, and a regression would still be tagged RED, so the grade is low. | sound | - | class:refusal-branch-with-no-arm |
| 8 | verification | .githooks/pre-push:1582 | low | low | confirmed | The claim holds. In .githooks/pre-push:1582, scan_policy_bytes outside a table header accepts lhs `"$2.$3"` (a dotted key at the root) or `"$2"` with a `{` value (an inline table). In the FL harness in .githooks/pre-push.test.sh (3071-3101), A holds only [runtime], R uses the [verdict]/[hooks] tables (the hdr branch), and R3 uses inline tables. R3 exercises the `"$2"` arm: its `{` value reads `?` and raises. No revision spells `verdict.blocks = ...` at the root, so breaking the `"$2.$3"` arm would leave every row green. If it broke, a root dotted key would read as 'no mention', and the nopy or nokit plants would fall back to the loose default. That is the fail-open unit 106 closed, but this is only a coverage gap on a currently working branch, so the grade is low. scan_policy_bytes is new in this range (the base has 0 occurrences). | sound | - | new:accepted-spelling-with-no-fixture-row |
| 9 | intent | tools/lib/commit_trailers.py@253aca4e:309 | medium | medium | confirmed | I read tools/lib/commit_trailers.py@253aca4e:290-324, which the fold added; it is absent at a7f2fe03f. check_message_attribution builds `agent` only from the stdout of `git interpret-trailers --parse`, and that command reads only the final trailer block. The function never reads proc.returncode. When `agent` is empty it returns `none` before either the value check or the last-line check runs, and main() maps `none` to exit 0. I re-ran the finder's probe against tools/unattended/commit_trailers.py using a scratch charter naming `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. The message `subj / Pass: none / Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> / blank / later note` printed `ATTRIBUTION none · no Co-Authored-By: trailer naming <noreply@anthropic.com>` and exited 0. A control message that ends with the correct trailer printed `ok`, so the probe is valid. Spec 108 §4 does define the agent trailers as git's parse, so the code matches its spec text. Even so, the spec and the code together miss round 1's L2 class-level fix, which asked for a gate on both value and position. Here a message carries the exact drifted value and does not end with the charter trailer, yet it is admitted silently. A git failure is also read as `none` and fails open. The effect is limited to commit-message metadata, and a commit with no agent trailer at all is admitted by design anyway, so medium. | sound | - | new:trailer-parse-reads-only-the-final-block |
