**Serves:** diff-review TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4

# aHastenedSweep — Tier-2 diff review, round 1: four exact-verdict speed-ups of the memory-hygiene runner

2026-11-16 · Tier-2 · on `branch/zealous-kalam-1911a4` · adversarial fan: finders `gov-diff-reviewer` (5 lenses), skeptic batches `gov-skeptic` (5), synthesis `gov-synthesizer`. The range holds four units of `tools/memory-tree/check-memory-hygiene.sh` and its Python delegates. TOOL-aHastenedSweep-1 reorders check 25's by-name test. TOOL-aHastenedSweep-2 memoizes in `gotchas.selectable` and `corpus_ids.walk`. TOOL-aHastenedSweep-3 hands the index set down on stdin (`GOV_INDEX_SET_STDIN=1`). TOOL-aHastenedSweep-4 runs checks 13-16 and 17-19 in one interpreter via `gotchas.py --check-with-ids`.

**Reviewed range:** `f25308f019b4fbd05964a81c70ff85d3599ea51b...cf64f39dfe9bea15960a521919497c3710b91588`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker. One HIGH defect sits on a narrow path. A target that owns an older `gotchas.py` gets a wrong red on checks 13-19, because the shell now calls a verb that no kit contract names. Four MEDIUM items are test and spec-coverage gaps around the unit 3 and unit 4 arms. Four LOW items are comments, docs and an unobserved branch. On the live tree the shipped verdicts match the base: the main loop's A/Bs were cmp-identical, and no finding shows a wrong verdict on gov's own tree.

## Review shape

Intensity full, raw 10, confirmed 10, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by item: 0 BLOCKER, 1 HIGH, 4 MEDIUM, 4 LOW, which is 9 items.
- Adjudicated tally by raw confirmed finding: 0 BLOCKER, 1 HIGH (id 3), 4 MEDIUM (ids 1, 5, 6, 8), 5 LOW (ids 2, 4, 7, 9, 10), which is 10 findings.
- Every finding keeps its binding grade. I regraded none.
- One merge was made at synthesis: ids 1 and 7 are one defect (M1), the assertion floor left five below unit 3's arms. M1 takes MEDIUM from id 1. Id 7 keeps its binding LOW.
- Intent: 4 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 55 items, acquired by the harness from `--for-diff f25308f019b4fbd05964a81c70ff85d3599ea51b..cf64f39dfe9bea15960a521919497c3710b91588`, each assigned to exactly one of 5 lenses: security 11, correctness 11, seams 11, verification 11, intent 11.
- By design: the caller's byDesign.
- Refuted findings shown to synthesis: 0. Same-address pairs shown: 0.
- Dispositions: unclassed refused; 55 class slugs handed; 175 leg names read from `tools/gate-legs.json`.
- The security lens returned zero findings. It returned, so the zero is its result. That result is bounded by a generic brief and a local-tool security model with no network and no new write path.

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified. 0 orphaned duplicate refutations demoted to unverified. 0 duplicate refutations counted as merged confirmations. 0 spurious verdicts discarded. 0 duplicates.
- Fixes on confirmed findings: 6 judged sound, 2 judged UNSOUND (ids 2 and 6), 2 judged INSTANCE-ONLY (ids 3 and 8), which cure the cited instance and leave the class standing, 0 none proposed, 0 NOT JUDGED. Where a fix was judged unsound, only the skeptic's corrected fix appears below. Where a fix was judged instance-only, the skeptic's class-level fix is the fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- The non-zero integrity counts are the unsound and instance-only fixes. Nothing died and nothing is unverified, so the finding set is whole. The caveat that stands is the generic lens brief.

## Twins

No refuted findings and no same-address pairs were shown, so there is nothing to flag.

## HIGH

### H1 — The shell calls a private `gotchas.py` verb that no kit contract names (id 3)

`tools/memory-tree/check-memory-hygiene.sh@71e199ce:3226`, against `tools/memory-tree/kit.toml@692d0917:443`.

**What is wrong.** Every unscoped run now launches `$HERE/gotchas.py --check-with-ids`. The `memory-tree/gotchas` contract in `kit.toml` still has one clause, the `--for-paths` probe, and its consumers are kickoff and unattended. No clause names `check-memory-hygiene.sh` as a consumer. That leaves both the new `--check-with-ids` verb and the existing `--check` verb uncontracted. The only `kit.toml` edit in the range adds `main` to the corpus_ids imports. Spec 4 §5 covers an adopter-owned `corpus_ids.py` and not an adopter-owned `gotchas.py`.

**Consequence.** A target that declares `gotchas.py` adopter-owned keeps its own copy. If that copy predates this change, it does not know the verb. The finder ran the base `f25308f0` `gotchas.py` with `--check-with-ids`: it printed `usage: gotchas.py [--check|--write|...]` and exited 2. In the shell, `_both=$(...)` then fails. The fallback at `:3233`-`:3234` sets `ids` to the usage text with `_idsrc=1` and `got=""` with `_gotrc=1`. It also sets `_onepy=1`, so the separate 17-19 launch at `:3257` is skipped. Checks 13-16 and 17-19 both go red on a tree whose two `--check` verbs pass when run alone. That breaks the owner's byte-identical constraint, and `govkit update`/`check` never names the clause the owned program now has to keep. The path is narrow, which is why this is HIGH and not BLOCKER: the target must own `gotchas.py` and keep a copy older than this change.

**Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix).** Give the `memory-tree/gotchas` contract one clause with `consumer = "check-memory-hygiene.sh"` for each `gotchas.py` verb the shell calls. That means `--check`, already uncontracted at the base, and `--check-with-ids`. Use an `imports = ["cmd_check_with_ids", "main"]` clause, or a read-only probe whose `expect` matches the two-frame shape. Keep spec S6's loud red; do not add a silent two-launch fallback. The finder proposed adding a single probe or imports clause for `--check-with-ids` alone, or falling back to two launches on a usage exit. That cures the cited instance only and leaves the uncontracted `--check` call standing. The build should still run the finder's probe: install the base `gotchas.py` beside the new shell in a fixture and confirm govkit names the missing clause.

**Left-shift.** New class `private-verb-call-without-a-kit-contract-clause`. The gate is a leg that collects every `$HERE/<program> --<verb>` the kit's shells launch and requires a contract clause whose consumer is that shell and which names the verb. It would sit beside `govkit selfcheck`.

## MEDIUM

### M1 — The assertion floor sits five below the count it pins, because unit 3's arms were never counted (ids 1, 7)

`tools/memory-tree/check-memory-hygiene.test.sh@4a13ab30:4812`.

**What is wrong.** Unit 3 (commit `c0008f704`) added five top-level, never-skipped `n=$((n+1))` assertions at `:3356`-`:3389`. They are the hand-down arm, the plain and exported checks 1-5 refusal arms, the `--only 16` arm and the standalone-CLI ask. That commit did not touch `FLOOR_ASSERTIONS`, and spec 3's three New-arm rows record `· none` for the floor. Unit 4 added two assertions and raised the floor 708 -> 710. Its RAISED comment at `:4810` credits unit 4 alone. Every earlier RAISED entry at `:4759`-`:4811` pins an exact count made by reading, so the floor is meant to equal the count.

**Consequence.** The floor exists to catch arms stranded past an `exit` or a `return`. If the whole TOOL-aHastenedSweep-3 block were stranded, `n` would drop by five to 710, which still meets the floor, and the suite would print PASS. The arms that protect the `_IXH` eligibility predicate could vanish with no red. The damage stays inside the suite's reachability guard.

**Grades.** Id 1 is MEDIUM and id 7 is LOW, both binding and kept. The item takes MEDIUM.

**Fix (judged SOUND by the skeptic for ids 1 and 7).** Raise `FLOOR_ASSERTIONS` to 715 (708 + 5 + 2). Add a RAISED comment that names both TOOL-aHastenedSweep-3 and TOOL-aHastenedSweep-4. Run the suite once and confirm the printed `PASS (<n> assertions)` equals 715. Then strand the unit 3 block behind an early `exit` and watch the floor go red.

**Left-shift.** New class `assertion-floor-left-below-the-added-arms`. The gate is a suite-side check that counts the top-level, unconditional `n=$((n+1))` sites and reds when `FLOOR_ASSERTIONS` is below that count. A unit that adds arms without raising the floor would then fail its own suite.

### M2 — The unit 4 split arm cannot see the two exit codes read into the wrong variables (id 5)

`tools/memory-tree/check-memory-hygiene.test.sh@4a13ab30:3392`, gating `tools/memory-tree/check-memory-hygiene.sh@71e199ce:3228`.

**What is wrong.** The only shell arm that drives `--check-with-ids` (`:3392`-`:3416`) uses a fixture where both verbs are red. `ORPHAN_ID_PIN=0` with an orphan id reds check 14, and an ungated gotchas record reds check 18. `_idsrc` and `_gotrc` are therefore both 1. A mutation that swaps or cross-reads the rc fields at `:3228`-`:3229` produces the same status and the same `add_offender_keys` calls. The finder ran the split on a two-red frame (`...\x1d1\r\n...\x1d1\r\n`): the real split and the swapped split both gave `idsrc=1 gotrc=1`. The gotchas selftest checks the frame Python writes in the order `0 1`, not the shell's parse of it.

**Consequence.** The shipped code is correct today. A later regression that sends the gotchas rc to check 13-16 would, on a run where only 17-19 is red, key check 13-16 with the green corpus_ids notices under `--offenders`. It would key nothing under 17-19 and exit with the same aggregate code. The merge bar grades by `--offenders`, and no arm would catch it.

**Fix (judged SOUND by the skeptic).** Add one unscoped `--offenders` arm where exactly one verb is red, for example a gotchas record that names no gate while the 13-16 pins stay blank. Assert that check 17-19 carries the check 18 key and that no `check 13-16` row appears. Add the mirror case: an orphan under `ORPHAN_ID_PIN=0` with no gotchas record, and no `check 17-19` row. Watch both arms go red with `_idsrc` and `_gotrc` swapped in the split, and raise `FLOOR_ASSERTIONS` by the new count.

**Left-shift.** New class `both-red-fixture-hides-a-swapped-rc`. Wherever one capture carries two verdicts, the suite should hold a one-red arm for each side. A staged swap of the two rc reads is the check that such arms are present.

### M3 — No arm exercises the frame-failure fallback, so its loud red is unguarded (id 6)

`tools/memory-tree/check-memory-hygiene.sh@71e199ce:3234`.

**What is wrong.** The fallback `[ "$_onepy" = 1 ] || { ids=$_both; _idsrc=1; got=""; _gotrc=1; _onepy=1; }` is new in this range. The comment above it promises that a frame that does not split "reds LOUDLY under 13-16 with the whole capture, never as a silent second launch". A grep of `tools/memory-tree` finds only the well-formed-frame shell arm and the gotchas selftest. Nothing drives a malformed or missing frame through the shell.

**Consequence.** The fallback also sets `_onepy=1`, so the separate 17-19 launch never runs. If a mutation set `_idsrc=0`, or left `_gotrc` at 0, a broken frame would turn checks 13-19 into a green, silent skip, and the suite would stay green. A broken frame can come from a `gotchas.py` import error, a `SystemExit` that escapes `cmd_check_with_ids`'s `except Exception`, or a nonzero interpreter exit. This is a coverage gap rather than a shipped wrong verdict.

**Fix (judged UNSOUND by the skeptic; this is the skeptic's corrected fix).** Point `GOV_PYTHON` at a wrapper script that execs the real interpreter for every argument list except one containing `--check-with-ids`. For that one it prints a line with no `\x1d` byte and exits 0; a second variant exits 1. The wrapper must pass everything else through, because `resolve_python` (`:476`-`:496`) RUNS each candidate with `-I -c` and requires a major.minor at or above the floor. A wrapper that answered every call with the bad line would make the run exit 2 at `:615` before reaching the block. Run the gate unscoped with `--offenders` on a fixture that is otherwise clean. Assert rc != 0, assert the wrapper's line is printed, and assert it is keyed under `check 13-16`. Watch the arm go red with the fallback's `_idsrc=1` changed to 0, and raise `FLOOR_ASSERTIONS` by the new count.

**Left-shift.** The `harness arms (fail branches armed or pinned)` leg should catch a new fail branch that has no arm. The fallback assignment block is the branch to register with it.

### M4 — Spec 4's AC1 claims a stderr red-case its command cannot produce (id 8)

`memory/builds/aHastenedSweep/spec/2026-11-15-spec-TOOL-aHastenedSweep-4.md@d0b92f69:273`, with the frame at `tools/memory-tree/gotchas.py@776abcc6:703`.

**What is wrong.** AC1 (spec 4 `:269`-`:274`) says it goes red when "a verb's stderr is dropped". The spec's own evidence (`:118`-`:122`) says neither `--check` path writes to `sys.stderr`. The F1/F2 fixtures and the selftest's with-ids tree (`gotchas.py:1269`-`:1314`) reach only those clean paths. The selftest's `want` is built with the same err-first formula, so err is always empty. The one stderr writer in the verb, `traceback.print_exc`, is never triggered by a fixture. §5 risks (`:253`) makes the same claim about an edit that prints before a stderr write.

**Consequence.** The stderr-first frame order `f"{err.getvalue()}{out.getvalue()}..."` and the rule that a verb's stderr survives are never checked. Dropping `err.getvalue()`, or putting stdout first, would leave AC1's probe at `frame F1 same 0 1` and the arm at `with-ids 0 1 same · ls-files 2`. The ledger records AC1 as observed without saying it could not show this red-case. The effect is contained because no shipped `--check` path writes stderr today.

**Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix).** Give the selftest arm a verb that writes stderr. In `load_counted`, wrap the loaded module's `main` so it writes one line to `sys.stderr` and one to `sys.stdout`, then returns 3. Assert its frame is exactly `<err line><out line>\x1d3\n`, and show the arm red by dropping `err.getvalue()` at `gotchas.py:702`. If the build instead drops the clause from AC1's Red-when, it must also strike the matching stderr-ordering claim in §5 risks (`:253`) and list both under "What it does not check". The finder offered either the monkeypatched fixture or the AC1 edit alone. That cures the cited instance only and leaves the §5 claim of the same class standing.

**Left-shift.** Class `criterion-asserts-what-its-own-command-cannot-show`. The gate is a spec-audit pass that requires each Red-when clause to name the staged break that shows it, and the fixture input that reaches that break.

## LOW

### L1 — The in-process frame's crash text is not the standalone bytes its comments claim (id 2)

`tools/memory-tree/gotchas.py@776abcc6:700`.

**What is wrong.** When a verb raises a non-`Problem` exception, `cmd_check_with_ids` (`:676`-`:705`) catches `Exception`, calls `traceback.print_exc()` inside the redirect, sets rc 1 and writes err before out. The traceback therefore starts at the in-process `rc = verb(argv)` frame, not at the standalone `<module>`/`sys.exit(main(sys.argv))` frame. All of stderr goes ahead of all of stdout. The old `2>&1` capture could show 8 KiB block-buffered stdout chunks before a late traceback. The text is also written through the process's utf-8 stream, where a node without `PYTHONUTF8` used the locale codec with backslashreplace. The inline comment ("the traceback is this verb's output, as it was standalone") and the docstring ("stderr first as the two-process 2>&1 capture put it") overstate what the crash path prints.

**Consequence.** The path is reached only when `corpus_ids` or `gotchas` crashes. Old and new code both red there with rc 1 and `status=1`, so the verdict and exit codes match. Only the printed crash bytes differ. The live `--check` paths write nothing to stderr, and the finder's live-tree A/B (CRLF normalised) printed True.

**Fix (judged UNSOUND by the skeptic; this is the skeptic's corrected fix).** Reword both the docstring and the inline `except` comment at `gotchas.py:700`. Say that the traceback is the in-process one, starting at the `cmd_check_with_ids` frame, that it is written in this process's stream encoding, and that it is placed ahead of the verb's stdout. If byte identity on the crash path is wanted, have `cmd_check_with_ids` add a distinct crash marker to the frame, for example a separate rc sentinel. On that marker the shell re-runs only the crashed verb as its own launch and captures it with `2>&1`.

**Left-shift.** New class `in-process-fold-claims-standalone-bytes`. When two launches are folded into one process, the spec's byte-identity table should list the crash path as its own row, with what differs, instead of letting a comment assert identity.

### L2 — S4 claims AC6 observes the per-verb exception branch, and no arm reaches it (id 9)

`memory/builds/aHastenedSweep/spec/2026-11-15-spec-TOOL-aHastenedSweep-4.md@d0b92f69:40`, with the branch at `tools/memory-tree/gotchas.py@776abcc6:699`.

**What is wrong.** S4 says its exception route is "Observed by AC1, AC2 and AC6": an exception out of one verb prints its traceback into that verb's stderr buffer at rc 1. AC6 (`:297`) stages its `raise RuntimeError` as the first line of `cmd_check_with_ids`. That is before the per-verb loop at `gotchas.py:694`-`:701`, so it reaches only the shell's S6 fallback. AC1 and AC2 run verbs that do not raise, and the selftest New arm (`:324`) covers only AC1 and AC2.

**Consequence.** No behaviour changes today; the shipped branch looks right because `traceback.print_exc` writes to the redirected `sys.stderr`. A later edit could still break it unseen. It could catch too narrowly, print the traceback outside the redirect so it lands in the other block, or skip the second verb after the first crashes. A crash in `corpus_ids` could then be keyed under 17-19 or hide the gotchas verdict.

**Fix (judged SOUND by the skeptic).** Stage the break inside a verb: in the selftest arm, monkeypatch `ids.main` to raise `RuntimeError`. Assert that the first frame holds the traceback with `\x1d1\n`, that the second frame equals gotchas `--check`'s own standalone frame, and that the shell keys the traceback under 13-16 only. Or reword S4 so it no longer claims AC6 observes this branch.

**Left-shift.** Class `observed-by-claim-no-arm-discharges`. The gate is a check that each "Observed by AC*n*" claim names an AC whose staged break lies inside the code path the claim covers.

### L3 — The hand-down's exemption note and comments still name only the corpus_ids launch (id 4)

`tools/memory-tree/check-memory-hygiene.test.sh@4a13ab30:3068`, `tools/memory-tree/corpus_ids.py@d88903f1:17`, `tools/memory-tree/check-memory-hygiene.sh@71e199ce:3208`.

**What is wrong.** Test-file `:3068`-`:3069` says the shell sets `GOV_INDEX_SET_STDIN` only "on its own launch of corpus_ids.py --check". Since unit 4, an unscoped run sets it on the `gotchas.py --check-with-ids` launch (`check-memory-hygiene.sh:3226`). The `corpus_ids.py` docstring (`:17`-`:18`) and the shell comment at `:3208` say the index set is only asked for through the print modes. Neither mentions the stdin hand-down.

**Consequence.** There is no effect on behaviour. The next person changing the hand-down reads a note that names the wrong launch and the wrong direction. They can miss the `gotchas.py` launch, which forwards the variable to its child processes.

**Fix (judged SOUND by the skeptic).** Reword test-file `:3068` to "sets it on its own launch of corpus_ids.py --check, or of gotchas.py --check-with-ids on an unscoped run". Add to the `corpus_ids.py` docstring at `:18` and to the shell comment at `:3208` that the shell hands `--print-index-set`'s answer down on stdin (`GOV_INDEX_SET_STDIN=1`) when checks 1 to 5 ran clean.

**Left-shift.** Class `a-folded-field-leaves-its-row-shape-docs-behind`. When a unit folds two launches into one, its spec's Files-touched list should be built from a grep for every reader of the folded launch's name and environment variable.

### L4 — The dossier bullet places the index-set hand-down on a launch an unscoped run no longer makes (id 10)

`memory/map/features/memory-tree-hygiene.md@02cd1131:172`.

**What is wrong.** Unit 3 added a bullet saying the engine hands the index set down "On its own launch of `corpus_ids.py --check`". Since unit 4, an unscoped run never launches `corpus_ids.py --check`. The hand-down goes to `gotchas.py --check-with-ids`. The remaining `corpus_ids.py --check` launch runs only under `--only`, where `_IXH` is always empty (`check-memory-hygiene.sh:1190` requires `ONLY` to be empty), so it never receives the set. Spec 4 `:74` says this file needs no edit.

**Consequence.** There is no effect on behaviour. The dossier describes a mechanism the engine no longer has and never mentions the one-process launch. The next change to the 13-19 blocks or to `GOV_INDEX_SET_STDIN` will look for the hand-down on the wrong launch line.

**Fix (judged SOUND by the skeptic).** Edit the bullet to say that the index set is handed down on stdin to the unscoped run's single `gotchas.py --check-with-ids` launch, which runs corpus_ids' `--check` in-process. Also say that a scoped run's `corpus_ids.py --check` always asks the print mode. Remove spec 4's "No edit to memory-tree-hygiene.md" non-goal, or amend it.

**Left-shift.** Class `amendment-leaves-its-other-half-standing`. A spec's non-goal that excludes a map file should be checked against a grep of that file for the names the unit changes.

review-shape kind=diff-review round=1 intensity=full at=synth raw=10 confirmed=10 refuted=0 merged=0 unverified=0 blocker=0 high=1 medium=4 low=5 agents=11 out-tokens=111882
review-round round=1 limit=- prior=- count=1 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/memory-tree/check-memory-hygiene.test.sh:4812 | medium | medium | confirmed | Confirmed by reading the test file. Unit 3 (c0008f704) added five top-level, never-skipped increments at lines 3356-3389: the hand-down arm, two more in the plain/exported loop, the --only 16 arm and the standalone-CLI arm. Its commit does not touch FLOOR_ASSERTIONS. Unit 4 added two increments (the 13-16 and 17-19 split arms) and raised the floor 708 -> 710, and the comment at line 4810 credits only unit 4. Every earlier entry in that comment raises the floor by an exact count made by reading, so the floor is meant to pin the count. It now sits five low, so if the whole unit-3 block were stranded the suite would still pass. The damage stays inside the test suite's reachability guard, so medium. | sound | - | new:assertion-floor-left-below-the-added-arms |
| 2 | correctness | tools/memory-tree/gotchas.py:700 | low | low | confirmed | At gotchas.py:676-705, cmd_check_with_ids catches Exception, calls traceback.print_exc() inside the redirect, sets rc=1 and writes err before out. The traceback therefore starts at the in-process `rc = verb(argv)` frame, not at the standalone `<module>`/sys.exit(main(...)) frame. The stream encoding also differs from a standalone launch, so the crash text cannot be byte-identical. The inline comment says `the traceback is this verb's output, as it was standalone`, and the docstring says each verb is framed `stderr first as the two-process 2>&1 capture put it`. Both overstate what happens on the crash path. The rc and the verdict match, the crash path reds either way, and the live --check paths write nothing to stderr, so the only effect is a misleading comment and different crash bytes: low. | unsound | - | new:in-process-fold-claims-standalone-bytes |
| 3 | seams | tools/memory-tree/check-memory-hygiene.sh:3226 | high | high | confirmed | Checked against the code. check-memory-hygiene.sh lines 3226-3233 now run `$HERE/gotchas.py --check-with-ids` on every unscoped run. If that command exits non-zero or its output does not split, the fallback sets ids to the whole capture with _idsrc=1 and sets got="" with _gotrc=1. Line 3257 then skips the separate `--check` launch because _onepy=1, so both 13-16 and 17-19 go red. At the base f25308f0, gotchas.py main (line 1448 onward) knows no `--check-with-ids` mode and falls through to the usage line at 1498, so an older adopter-owned copy goes red where two `--check` launches would pass. In kit.toml, the gotchas contract (lines 441-446) still has only the `--for-paths` clause, with the kickoff and unattended consumers. The only kit.toml edit in this diff adds `main` to the corpus_ids imports. So govkit's adopter-owned report never names the new verb. Spec 4 lines 184-185 cover only an adopter-owned corpus_ids.py. The path is narrow: a target has to declare gotchas.py adopter-owned and keep a copy older than this change. The consequence is a wrong red verdict, so high fits. | instance | - | new:private-verb-call-without-a-kit-contract-clause |
| 4 | seams | tools/memory-tree/check-memory-hygiene.test.sh:3068 | low | low | confirmed | Checked against the text. check-memory-hygiene.test.sh lines 3068-3069 still say the shell sets GOV_INDEX_SET_STDIN 'on its own launch of corpus_ids.py --check'. Line 3226 of the shell now also sets it on the `gotchas.py --check-with-ids` launch. The corpus_ids.py docstring (lines 17-18) and the shell comment near line 3208 describe the index set only as 'asked for through its print modes' or 'PRINTS them on demand', and neither mentions the stdin hand-down. These are comments and an exemption note only, so behaviour is unaffected. | sound | a-folded-field-leaves-its-row-shape-docs-behind | class:a-folded-field-leaves-its-row-shape-docs-behind |
| 5 | verification | tools/memory-tree/check-memory-hygiene.test.sh:3392 | medium | medium | confirmed | Confirmed in the code. In check-memory-hygiene.test.sh, the only unit 4 shell arm (around line 3392) builds a fixture where both verbs fail: ORPHAN_ID_PIN=0 with an orphan id reds check 14, and an ungated gotchas record reds check 18. Both arms then assert only that each line is keyed under its own block. The split in check-memory-hygiene.sh around lines 3226-3229 reads _idsrc and _gotrc from the two rc fields. With both at 1, swapping or cross-reading those fields produces the same status and the same add_offender_keys calls, so the arm cannot see it. Swapping the text blocks (ids/got) would be caught; swapping the rc fields would not. The python selftest in gotchas.py near line 1313 checks the frame Python writes, not the shell's parse of it. No other shell arm drives --check-with-ids. The effect is a test gap: the code shipped today is correct, and only a later regression would slip through. Hence medium. | sound | - | new:both-red-fixture-hides-a-swapped-rc |
| 6 | verification | tools/memory-tree/check-memory-hygiene.sh:3234 | medium | medium | confirmed | Confirmed. Line 3234 `[ "$_onepy" = 1 ] \|\| { ids=$_both; _idsrc=1; got=""; _gotrc=1; _onepy=1; }` is new in this diff. A grep of tools/memory-tree for check-with-ids, 'does not split' and frame-failure arms finds only the well-formed-frame shell arm and the gotchas.py selftest. Nothing drives a malformed or missing frame through the shell. The fallback also sets _onepy=1, which suppresses the separate 17-19 launch. So if a mutation set _idsrc=0, a broken frame would leave 13-19 green and silent, and the suite would stay green. This is a coverage gap rather than a shipped wrong verdict: medium. The proposed fix is unsound as written. resolve_python (check-memory-hygiene.sh lines 476-496) RUNS each candidate with `-I -c` and requires a major.minor at or above the floor. A wrapper that just prints 'no frame' would fail that probe, and the run would exit 2 at line 615 before reaching the block. A wrapper that always exits 1 fails the same way. The wrapper must also serve checks 9 and 13-19, so it has to pass every other invocation through to the real interpreter. | unsound | - | gate:harness arms (fail branches armed or pinned) |
| 7 | verification | tools/memory-tree/check-memory-hygiene.test.sh:4812 | low | low | confirmed | Unit 3's commit c0008f704 adds five `n=$((n+1))` assertions to check-memory-hygiene.test.sh: the hand-down arm, two in the plain/exported loop, --only 16, and the standalone CLI ask. It does not touch FLOOR_ASSERTIONS. The only raise in the range is cf64f39df's 708 -> 710, and its comment names TOOL-aHastenedSweep-4's two assertions alone. Spec 3's three New arm rows (lines 220-222) end in '· none'. Every earlier unit that added arms raised the floor by its own count, as the RAISED history at test.sh:4759-4811 shows, so unit 3's five arms are not counted. If they were stranded they could vanish with no red. The effect is limited to test-suite coverage, so the grade is low. | sound | - | new:assertion-floor-left-below-the-added-arms |
| 8 | intent | memory/builds/aHastenedSweep/spec/2026-11-15-spec-TOOL-aHastenedSweep-4.md@d0b92f69:273 | medium | medium | confirmed | AC1 in spec 4 (lines 269-274) says it goes red when 'a verb's stderr is dropped'. The spec's own evidence (lines 118-122) says neither --check path reaches a sys.stderr write. corpus_ids.py has no stderr print apart from a reconfigure at 1825. Its Problem texts and check-16 notes are findings, and its recall stderr writes are in id_grammar, which the spec says walk never reaches. The selftest arm at gotchas.py:1269-1314 uses a fixture that only reaches those clean paths. Its `want` is built with the same err-first formula, so err is always empty. Dropping err.getvalue() at gotchas.py:702, or putting it after stdout, would therefore leave `with-ids 0 1 same · ls-files 2` green. The only stderr writer in the verb, traceback.print_exc on an exception, is never triggered by any fixture. The criterion claims a red its command cannot show. §5 risks (line 253) makes the same claim: 'a later edit that prints before a stderr write ... AC1's arm ... red'. The effect is contained because no shipped --check path writes stderr today, so the grade is medium. | instance | criterion-asserts-what-its-own-command-cannot-show | class:criterion-asserts-what-its-own-command-cannot-show |
| 9 | intent | memory/builds/aHastenedSweep/spec/2026-11-15-spec-TOOL-aHastenedSweep-4.md@d0b92f69:40 | low | low | confirmed | Spec 4 line 40 says S4, including 'an exception out of one prints its traceback into that verb's stderr buffer with rc 1', is 'Observed by AC1, AC2 and AC6'. AC6 (line 297) stages the raise as the first line of cmd_check_with_ids, which is before the per-verb loop at gotchas.py:694-701. That only reaches the shell's S6 fallback. AC1 and AC2 run verbs that do not raise, and the selftest New arm (line 324) covers only AC1 and AC2. So the except/print_exc/rc=1 branch is never exercised. The shipped code itself looks right, because traceback.print_exc writes to the redirected sys.stderr. The gap is in the spec's claim of coverage, with no effect on behaviour today, so it is low. | sound | - | class:observed-by-claim-no-arm-discharges |
| 10 | intent | memory/map/features/memory-tree-hygiene.md@02cd1131:172 | low | low | confirmed | check-memory-hygiene.sh:3219-3237 launches gotchas.py --check-with-ids on every unscoped run and launches corpus_ids.py --check only in the `--only` else-branch. There _IXH is always empty, because line 1190 requires ONLY to be empty. Dossier line 172, added by unit 3 (c0008f704) and not touched by unit 4, still says the hand-down happens 'On its own launch of `corpus_ids.py --check`'. Spec 4 line 74 excludes editing that file. The bullet is now stale documentation that points at the wrong launch line. It changes no behaviour, so it is low. No other map file names these launches. | sound | - | class:amendment-leaves-its-other-half-standing |
