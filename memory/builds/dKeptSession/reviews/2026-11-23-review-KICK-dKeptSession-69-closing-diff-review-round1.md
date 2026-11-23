**Serves:** diff-review KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69

# dKeptSession — Tier-2 CLOSING DIFF review, round 1

*Node `d`, 2026-11-23. dKeptSession is the Session build of the dClosedLoop chain, run unattended. This review is an adversarial pass over the whole landed diff of the Tier-2 units built from their specs and merged into the run branch. KICK-dKeptSession-69 is the build's close-time unit and is not yet built. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 1 spec document supplied as `specs`, read beside the range's commit messages. The checklist had 157 items, acquired by the harness from `--for-diff c2a407b0390f3d57a118b58e376c326aeb207c13..bcecefcfc654040f2577e20b76a99afa8bdac530`, each assigned to exactly one lens: security 32, correctness 32, seams 31, verification 31, intent 31. By design: the caller's byDesign, plus 3 invariants from the checklist's by-design block. The full merge bar and every new arm's RED-first observation run once at the build's close, after this review.*

**Range reviewed: `c2a407b0390f3d57a118b58e376c326aeb207c13...bcecefcfc654040f2577e20b76a99afa8bdac530`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER, and none is HIGH.
Five items are MEDIUM and three are LOW, one confirmed finding per item.
The most serious item: the item-boundary interrupt line renders fetched mail fields unvalidated into the main session's hook context (finding 1).
A refused transition can still land irreversible acks on the remote (finding 2).
A failed mail fetch defeats the fetch interval (finding 3).
A shadowed `unread` drops or misattributes owner progress lines (finding 4).
The mail hook's card binding has no suite arm (finding 6).
I recommend folding all five MEDIUM items before the landing, each with its arm observed RED first.
The three LOW items can be folded or filed.

## Review shape

Intensity full, raw 8, confirmed 8, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 8 items, 0 BLOCKER, 0 HIGH, 5 MEDIUM, 3 LOW.
Adjudicated tally by raw confirmed finding: 8 findings, 0 BLOCKER, 0 HIGH, 5 MEDIUM, 3 LOW.
No findings were merged, so the two tallies agree.
Every finding keeps its binding grade.
The skeptic re-graded two findings: finding 3 from low to medium and finding 4 from high to medium.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded.
- 0 duplicates.
- Fixes on confirmed findings: 6 judged SOUND, 1 judged UNSOUND (finding 3), 1 judged INSTANCE-ONLY (finding 2), 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twin is flagged.
- Dispositions: unclassed is refuse; 157 class slugs and 224 leg names were handed.

Every lens and every skeptic batch returned, so the finding set is complete for this run's checklist.

## MEDIUM

### M1. Fetched mail fields reach the main session's instruction channel unvalidated (finding 1)

**Where:** `tools/loop/position.py@1a1c4a92:756`, in `read_mail_interrupts`.
The reader is `read_mailbox` at `tools/unattended/unattended.sh@7397fa8b:4052`.

**What is wrong:** `read_mail_interrupts` formats `interrupt — mailbox · <id> <kind> from <from-build>` from a fetched mail record's fields.
It never checks their shape.
`read_mailbox`'s awk `flush()` accepts a record when its header equals `gov-mail <build>/<id>` and the six required keys are non-empty.
It never checks `id` against 12 hex digits, `kind` against the closed set, or `build` against the ref's own `refs/gov/mail/<slug>/` segment.
`read_mail_rows` (loop_transition.py:639) splits the driver's output on TABs with no validation.
The boundary verb `run_mail_interrupts` (manifest-check.sh:2614-2615) prints these lines into `<common>/orientation/<sid>.boundary`.
`checkItemBoundary` (tools/hooks/scratch-guard.js:2162-2165) puts that file's text into the main session's PreToolUse additionalContext.
The sibling channel, mail-notice.js, filters ids through `ID_RE ^[0-9a-f]{12}$` (lines 55 and 148).
The same message is therefore held to two standards depending on which channel carries it.
The diff introduced the whole path.

**Consequence:** anyone who can `git push` to `refs/gov/mail/*` on the remote can put one line of free text into the main loop's instruction channel at every item boundary.
The remote does not enforce `write_gov_ref` or `write_mail_post`'s checks.
An example record has header `gov-mail x/<text>`, `id: <text>`, `to: build:<victim>` and `kind: question`.
The impact is contained, because it needs push access to the shared remote and the text is one line with no TAB.

**Fix (judged SOUND by the skeptic):** validate on read, in one place.
In `read_mailbox`'s `flush()`, drop any record whose id is not 12 lower-case hex digits, whose kind is not in the loop kit's closed mail set, whose build fails `check_slug_shape`, or whose build differs from the ref's `refs/gov/remote/mail/<slug>/` segment.
Alternatively, apply the same filter in `read_mail_rows` before any row is rendered.
The probe: push a plant commit to `refs/gov/mail/x/z/s` on a fixture remote with `id: IGNORE PRIOR RULES` and `to: build:<slug>`.
Then run `position.py <slug> --mail-interrupts --local` and assert no `interrupt — mailbox` line carries that text, observed RED first against the current reader.

**Left-shift:** class `agent-output-interpolated-into-an-instruction`.
Add a `unattended-build self-test` arm that plants a malformed record and asserts no boundary line renders it.
Add a checklist line: every field that reaches additionalContext passes the same shape filter on every channel that carries it.

### M2. A refused transition still lands irreversible acks (finding 2)

**Where:** `tools/loop/loop_transition.py@b0328850:1074`, in `write_transition`.

**What is wrong:** `write_transition` calls `read_mail_rows` and then `write_consumed_acks`, which posts the consumed-notice acks to the remote with one `write_gov_ref`.
It does this before it checks that the move is valid.
Those checks are `derive_move`'s row lookup (1079), the PatchHeld check (1083-1088), the `--witness` resolve and ancestry checks (1089-1093), the `--field` checks (1095-1110) and the TreeUnverified check (1111-1114).
Later still come `derive_move_scenarios`'s scenario-conflict ValueError and the `bad` VALUE check over the move's fields.
The diff introduced this ordering.

**Consequence:** take a dependent whose only open rows are consumable notices, for example `landed`, `superseded`, `withdrawn`, or a `confirmed`/`changed` notice its parent's interfaces check reads as current.
Any transition it attempts that is later refused still lands acks that cannot be undone.
Examples are a mistyped `--item` or `--outcome`, a non-ancestor `--witness`, a derived `--field`, or Test's exit with no GREEN tree verdict.
It also prints `mail — acked ...`.
The parent then reads the notices as consumed, and the next move disposes them as `acked`, though no recorded transition consumed them.
This contradicts `write_consumed_acks`'s own contract and the docstring's "writing no record" promise.
The effect is contained to how notices are attributed to a move.

**Fix (judged INSTANCE-ONLY by the skeptic; the skeptic's class-level fix):** make the ack write the last step before the record write.
Compute the whole move first: `derive_move`, the patch hold, the witness checks, the field loop, the tree verdict, the stand-in, the composition, `derive_move_scenarios` and the VALUE check, with `disposed` derived from the pre-ack rows.
Then run `write_consumed_acks` and the MailHeld raise.
Add a plant per refusal class (a bad witness, a derived `--field`, a scenario conflict) that asserts no ack commit lands and the row still reads open.
The finder's proposal cures the cited instance alone.
It moves only the checks up to `check_tree_verdict` ahead of the acks, and leaves the scenario-conflict and VALUE refusals after the ack point.

**Left-shift:** class `destructive-step-before-its-precondition`.
Add a `loop transition record` fixture per refusal class that asserts the mail ref's tip is unchanged after the refusal.

### M3. A failed mail fetch defeats the fetch interval (finding 3)

**Where:** `tools/unattended/mail-notice.js@12122193:173`, with `print_mail_notice` in `tools/unattended/unattended.sh@7397fa8b:4354-4366`.

**What is wrong:** the hook starts a detached `--mail notice <slug>` whenever the stamp is older than `mailbox.fetch-seconds` (`checkFetchDue`, lines 116-119).
`runDetachedFetch` (127-143) refuses only while a `.fetching` marker exists and is no older than 2*seconds.
When the fetch fails, `print_mail_notice` leaves the stamp untouched on both the local-copy fallback and the rc!=0 path.
It still removes `<stamp>.fetching` unconditionally at the function's end.
The stamp stays overdue and no marker remains.
The diff introduced this.

**Consequence:** while the remote is unreachable, the first tool call after each failed fetch spawns another bash driver and another bounded git fetch, up to REMOTE_BOUND seconds each.
The fetches run back to back for the whole offline period, which is spawn-heavy on a node where process creation is the main cost.
The marker only stops fetches overlapping; it does not space them.
Nothing is lost and no result is wrong, so the effect is contained.

**Grade:** binding MEDIUM; the finder graded it low and the skeptic re-graded it medium for the repeated spawn and fetch cost.

**Fix (the finder's fix was judged UNSOUND by the skeptic; the skeptic's corrected fix):** on any path that does not rewrite the stamp (the local-copy fallback or rc!=0), leave `<stamp>.fetching` in place with its mtime set to the attempt time instead of removing it.
In the hook, spawn nothing while the marker is younger than fetch-seconds.
Keep the 2*seconds stale-marker removal only for a marker older than that.
Add the unreachable-remote fixture: two hook calls inside fetch-seconds after a failed fetch, and the second spawns nothing.

**Left-shift:** class `concurrency-is-not-a-budget`.
Add the unreachable-remote fixture to the `unattended-build self-test` suite.

### M4. A shadowed `unread` drops or misattributes owner progress lines (finding 4)

**Where:** `tools/loop/loop_transition.py@b0328850:1170`, in `write_transition`.

**What is wrong:** lines 1058 and 1060 set `unread` from the notify.owner read, a use KICK-dKeptSession-11 added.
In the pinned-composition branch, `orders, unread = write_ended_orders(root, build, before)` at 1170 overwrites it.
Line 1174 already reports the composition's `unread`.
Line 1261 then reads the same variable as if it were the progress refusal.

**Consequence:** the path is any move whose composition is pinned and whose pin differs from HEAD's revision.
If notify.owner reads fine and the composition is unread, line 1261 prints `loop: progress · unread · <the composition's why>`, which blames the wrong cause.
The owner's `progress — <slug> · transition · …` line is then never emitted.
If notify.owner was refused and `write_ended_orders` succeeds, the `progress · unread` line is silently dropped and the owner gets no line.
The move itself stands, so the effect is limited to owner-facing progress lines.

**Grade:** binding MEDIUM; the finder graded it high and the skeptic re-graded it medium, since only progress lines are lost or misattributed.

**Fix (judged SOUND by the skeptic):** rename the notify.owner pair, for example `events, progress_unread = …` at 1058/1060, and read `progress_unread` at 1261.
Alternatively, rename the composition's variable to `orders_unread` at 1170/1174.
Then add a `write_transition` plant: a pinned composition whose compose exits non-zero, with notify.owner selecting `transition`.
Assert the `progress —` line is present and no `progress · unread` line names the composition's cause.

**Left-shift:** class `a-new-local-collides-in-a-long-function`.
The plant goes into the `loop transition record` fixtures.

### M5. The mail hook's card binding has no suite arm (finding 6)

**Where:** `tools/unattended/mail-notice.js@12122193:161`, which calls `readCardBuild` (lines 93-99).

**What is wrong:** KICK-dKeptSession-44 S9's card binding has no suite arm.
Every KDS21 hook arm in tools/unattended/unattended.test.sh (lines 21828-21868) binds session k21 through the lease fixture's RUN.md `session:` fact.
No fixture writes `.claude/orientation-card.md`.
No suite names `card-owner` or `readCardBuild`.
The resolve-python drift check compares only the inline copies of `extract_route_units_js` and `card_file_rel_js`.
AC7 and AC16 are discharged only by one-off probes recorded as DERIVED in memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-44-1-acceptance-ledger.md:76,85.

**Consequence:** deleting the card branch, returning '' from `readCardBuild`, or breaking the `card-owner —` regex leaves every suite green.
An attended session routed only by its card would then silently hear no mail, which is AC7's Red-when.
AC16's no-spawn guarantee on the card path is also unguarded.

**Fix (judged SOUND by the skeptic):** add an arm to the KDS21/KDS44 block.
Write `$LF/c1/.claude/orientation-card.md` with `card-owner — k44` and a `## route` holding `- build: tFix`, and give k44 no RUN.md session fact.
Assert that `run_notice_hook` for k44 prints the additionalContext with the stamp's ids, and that another session prints nothing.
Run the same call again with logging `git` and `bash` stubs first on PATH, and assert both logs are empty.
Observe it RED with `readCardBuild` stubbed to return ''.

**Left-shift:** class `observed-by-claim-no-arm-discharges`.
Add a checklist line: an acceptance criterion closed DERIVED by a one-off probe owes a suite arm before the unit closes.

## LOW

### L1. `measure_context_fill`'s documented return names the wrong second element (finding 5)

**Where:** `tools/runlog/extract.py@4e37041a:1400`, and tools/runlog/README.md:268-269.

**What is wrong:** the docstring and the README say `measure_context_fill` returns `(share, tokens, source)`.
Line 1419 returns `(share, window, source)`, where the second element is the window from `derive_context_window`, not the context tokens.
The diff introduced the function.

**Consequence:** none today.
Both callers read it correctly: runlog.py:415 unpacks `fill, window, source`, and selftest.py:2104 takes only `[0]`.
A future caller following the documented contract would take the window size, such as 200000 or 1000000, as the context used.

**Fix (judged SOUND by the skeptic):** correct the docstring and README:269 to say `(share, window, source)`.
Alternatively, return the tokens as documented and update runlog.py to match.

**Left-shift:** new class `docstring-misnames-a-returned-value`.
Add a checklist line: a function's documented return tuple is read against its return statement and every caller's unpacking.

### L2. The detached spawn's argv and `windowsHide` have no suite arm (finding 7)

**Where:** `tools/unattended/mail-notice.js@12122193:139`, in `runDetachedFetch`.

**What is wrong:** KICK-dKeptSession-44 AC28 requires the detached spawn's argv[1] to be the driver beside the hook, with `windowsHide: true`.
No suite arm checks either.
unattended.test.sh has 0 occurrences of `windowsHide`.
The KDS21 AC4 stub at line 21847 replaces spawn with a no-op that ignores its arguments, and line 21848 checks only that no fetch happens.
The only observation is the ledger's one-off DERIVED probe (acceptance ledger line 97).

**Consequence:** dropping `windowsHide: true` or changing the driver path keeps every arm green.
On Windows nodes each detached fetch would then flash a console window.
A wrong driver path would make the fetch fail silently, and only KDS21 AC4's 20-second timing loop would notice, for that one path.

**Fix (judged SOUND by the skeptic):** add an arm that requires a copy of mail-notice.js with `child_process.spawn` replaced by a recorder, using the same sed technique as line 21847 but recording the arguments to a file.
Run it over a stamp older than fetch-seconds.
Assert one call whose argv[1] ends with `unattended/unattended.sh` and whose options hold `windowsHide:true` and `detached:true`.
Observe it RED with `windowsHide` removed.

**Left-shift:** class `observed-by-claim-no-arm-discharges`, the same checklist line as M5.

### L3. The mail hook's header misstates why it is registered on every tool (finding 8)

**Where:** `tools/unattended/mail-notice.js@12122193:12`, lines 12-16.

**What is wrong:** the header says the PostToolUse registration "exists only to cover the tools that matcher does not route, the non-Bash tools such as Read, Grep, Glob and Agent".
The registration's matcher is `*` in both .claude/settings.json (line 104) and tools/unattended/mail-notice.fragment.json (line 4), so the hook fires on every tool.
KICK-dKeptSession-21 S5 asks for exactly that.
scratch-guard.js carries no mail notice: `grep -n mail` there hits only the comment at line 1003.
The header follows KICK-dKeptSession-44 S6's wording (spec lines 65-68), which itself contradicts KICK-dKeptSession-21 S5.

**Consequence:** none today, because the matcher really is `*`.
A maintainer who follows the stated rationale could narrow the matcher to Read|Grep|Glob|Agent.
Sessions that only run Bash or edit files would then stop hearing about unread mail, and no arm would catch it.

**Fix (judged SOUND by the skeptic):** rewrite lines 12-16 to match S5 and the registration.
The hook is registered on every tool (matcher `*`) and is the only carrier of the unread-mail line.
scratch-guard's PreToolUse additionalContext carries the card pointers (KICK-dKeptSession-13 S7) and no mail.
Amend KICK-dKeptSession-44 S6's wording to match, so the two specs stop contradicting each other.
The probe: `grep -n 'mail' tools/hooks/scratch-guard.js` prints only the comment line, and `grep -n '"matcher": "\*"' tools/unattended/mail-notice.fragment.json` prints one line.

**Left-shift:** new class `header-rationale-contradicts-the-registration`.
Add a checklist line: a hook header's stated coverage is read against its registered matcher.

## Refuted, not counted

No finding was refuted, and no twin is flagged.

review-shape kind=diff-review round=1 intensity=full at=synth raw=8 confirmed=8 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=5 low=3 agents=10 out-tokens=73820 trigger=owed shape=- efforts=- role-sha=-
review-round round=1 limit=3 prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/loop/position.py:756 | medium | medium | confirmed | I read read_mailbox at tools/unattended/unattended.sh:4016. Its awk flush() accepts a record when `hdr == "gov-mail " v["build"] "/" v["id"]` and the six wanted keys are non-empty. It never checks the shape of id, kind or build, and never compares build with the ref's slug segment. Its own comment says it does not check "a message's id against its fields". read_mail_rows (loop_transition.py:639) splits the driver's stdout on TABs with no validation. read_mail_interrupts (position.py:728-761) formats `%s %s from %s` over r[id], r[kind] and r[from-build] for every open row. manifest-check.sh:2614-2615 calls run_mail_interrupts at the boundary. scratch-guard.js:2162-2165 reads `<sid>.boundary` into the hook's context. By contrast, mail-notice.js:55/148 filters ids through ID_RE ^[0-9a-f]{12}$, so the same message is held to two standards. At the base none of this existed: read_mailbox was only probed with `declare -F`, and read_mail_interrupts and read_mail_rows were absent, so the diff introduced the path. The consequence is contained: it needs push access to the shared remote's refs/gov/mail/*, a principal who can already push code, and the text is limited to one line with no TAB. That makes it a real defect of medium consequence, not a blocker. | sound | agent-output-interpolated-into-an-instruction | class:agent-output-interpolated-into-an-instruction |
| 2 | correctness | tools/loop/loop_transition.py:1074 | medium | medium | confirmed | In tools/loop/loop_transition.py, write_transition calls read_mail_rows and then write_consumed_acks (around line 1074), which posts the acks with one write_gov_ref. Only after that does it run read_definition and derive_move (row lookup), the PatchHeld check, the --witness resolve and is-ancestor checks, the --field loop and check_tree_verdict (1077-1114). Later still come derive_move_scenarios and the VALUE check. A mistyped --item or --outcome, a non-ancestor witness, a derived --field, or a Test exit with no GREEN verdict therefore raises after the acks have already landed on the remote. Those acks cannot be undone, and the next move disposes the rows as `acked`. This contradicts write_consumed_acks's contract ("that the dependent's transition has consumed") and the docstring's "ValueError on a value, witness ... writing no record". At the base neither read_mail_rows nor write_consumed_acks existed (grep count 0), so the diff introduced the ordering. The effect is contained to how notices are attributed to a move, so it is medium. The fix is graded instance because it cures the cited checks but names an incomplete list: derive_move_scenarios's scenario-conflict ValueError and the `bad` VALUE check over move fields also refuse after the ack point, and would still leave stray acks. | instance | destructive-step-before-its-precondition | class:destructive-step-before-its-precondition |
| 3 | correctness | tools/unattended/mail-notice.js:173 | low | medium | confirmed | Confirmed. In tools/unattended/mail-notice.js:116-119, checkFetchDue returns due whenever the stamp's age is over fetch-seconds. runDetachedFetch (:127-143) refuses only while a `.fetching` marker exists and is no older than 2*seconds. In tools/unattended/unattended.sh print_mail_notice, a soft read that falls back to the local copy sets `why`, and that branch never calls write_mail_notice, so the stamp is not refreshed. The rc!=0 branch skips the write too. Both paths then reach the unconditional `rm -f "$st.fetching"` at the function's end. So while the remote is unreachable, the next tool call after each failed fetch finds an overdue stamp and no marker, and spawns another detached driver and bounded fetch. fetch-seconds no longer spaces the attempts. This is new in the diff. The cost is extra process spawns and fetches; nothing is lost and no result is wrong, so I grade it medium. | unsound | destructive-step-before-its-precondition | class:concurrency-is-not-a-budget |
| 4 | seams | tools/loop/loop_transition.py:1170 | high | medium | confirmed | Confirmed by reading tools/loop/loop_transition.py. Lines 1058 and 1060 set `unread` from the notify.owner read. In the PINNED branch, `orders, unread = write_ended_orders(...)` at :1170 overwrites it. Line 1174 already reports the composition's `unread`, and line 1261 then reads the same variable as the progress refusal. (a) When notify.owner reads fine and the composition is unread, a second `progress · unread · <composition why>` line names the wrong cause, and the `transition` progress line is suppressed. (b) When notify.owner is refused and write_ended_orders returns None, the progress refusal line is dropped. Unit 11 introduced the progress use of the name in this diff, so the defect is in scope. The path needs a pinned composition whose pin differs from HEAD's revision, and the move itself stands. The effect is limited to owner-facing progress lines, which are lost or misattributed, so I grade it medium. | sound | - | class:a-new-local-collides-in-a-long-function |
| 5 | seams | tools/runlog/extract.py:1400 | low | low | confirmed | At tools/runlog/extract.py:1399-1419, the docstring opens with `(share, tokens, source)`, but line 1419 returns `derive_context_fill(...), window, source`, where `window` comes from derive_context_window. tools/runlog/README.md:268-269 repeats the wrong `(share, tokens, source)` contract. The base c2a407b0 has no measure_context_fill, so this diff introduced it. Both callers read it correctly today: runlog.py:415 unpacks `fill, window, source`, and selftest.py:2104 takes only [0]. The only effect is a contract that would mislead a future caller, which is low. | sound | - | new:docstring-misnames-a-returned-value |
| 6 | verification | tools/unattended/mail-notice.js:161 | medium | medium | confirmed | readCardBuild (tools/unattended/mail-notice.js:93-99, called at :161) is new in this diff. I grepped the test, fixture and Python files under tools/ and skills/ for `card-owner` and `readCardBuild`. No unattended suite matches either. The only hits are the scratch-guard and manifest-check files, which serve their own kits and never run mail-notice.js. Every run_notice_hook call in unattended.test.sh (21828-21868) binds k21 through the lease, and no suite writes an orientation card. The card-store plant mail-notice-boundary drives the engine's notice line, not the hook. The resolve-python.test.sh drift check compares only the inline copy of extract_route_units_js and card_file_rel_js. It does not cover readCardBuild's `card-owner —` regex or its owner comparison. The ledger at lines 76 and 85 records AC7 and AC16 only as DERIVED one-off probes. So deleting the card branch, or making readCardBuild return '', leaves every suite green. A session routed only by its card would then hear no mail. That is a real coverage gap, and its effect is contained. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 7 | verification | tools/unattended/mail-notice.js:139 | low | low | confirmed | runDetachedFetch in tools/unattended/mail-notice.js (about lines 127-145) passes `windowsHide: true` and the driver from path.join(__dirname,'unattended.sh'). `grep -c windowsHide tools/unattended/unattended.test.sh` prints 0. The only spawn stub, at test line 21847, uses sed to replace `spawn(bash, ` with a no-op lambda that ignores its arguments, and line 21848 checks only that the diff is one line. Nothing in the suite observes the argv or the options, so either could regress while every arm stays green. The file is new in this diff. The effect is a console flash or a silent failed fetch that the next stale-stamp call retries, so it is contained and low. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 8 | intent | tools/unattended/mail-notice.js:12 | low | low | confirmed | The mail-notice.js header at lines 12-16 says the PostToolUse registration 'exists only to cover the tools that matcher does not route, the non-Bash tools such as Read, Grep, Glob and Agent'. Its own line 3 says 'a PostToolUse hook on every tool', and the registration's matcher is "*" in both mail-notice.fragment.json (line 4) and .claude/settings.json. In scratch-guard.js, `grep -n mail` hits only the comment at line 1003, so scratch-guard carries no mail notice. The stated rationale is false, and a maintainer who follows it could narrow the matcher. The header does follow KICK-dKeptSession-44 S6's wording (spec lines 65-68), which is itself wrong against S5 of KICK-dKeptSession-21. This is only a comment with no effect on behaviour today, so low. | sound | - | new:header-rationale-contradicts-the-registration |
