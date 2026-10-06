# TOOL-aMendedFleet-7 — the daily held job's red suites, by root cause

**Serves:** journal TOOL-aMendedFleet-7

Read once, read-only, on 2026-10-04 at 22:10 UTC (2026-10-05 local), node a, at HEAD `b566f3459`.
Every log line below is quoted from `gh run view <run> --log-failed`, saved to the session
scratchpad, CR-stripped and split by the job name in its first field. No suite was run on any host.

## The census runs

The three most recent COMPLETED scheduled runs of `remote-ci.yml` on `main`, from
`gh run list --workflow remote-ci.yml --branch main --event schedule --status completed --limit 3`:

| Run | Created (UTC) | Head sha | Held jobs | Held red |
|---|---|---|---|---|
| `37196051126` | 2026-10-04 10:39 | `c2ffcf878c385d01012c29915906dd880fdf3c83` | 83 | 15 |
| `37114721791` | 2026-10-03 09:56 | `a587e82dc6180a9a720560e1633995e47734803a` | 83 | 18 |
| `36996269983` | 2026-10-02 10:35 | `4e0057a76af2d602678d219b4284250ee8d67ec7` | 82 | 19 |

**Liveness (AC1).** Run `37196051126`: 15 jobs named `held …` with conclusion `failure` in
`gh run view --json jobs`, and 15 suite rows below marked `R` in its column. Run `37114721791`: 18
and 18. Run `36996269983`: 19 and 19. The union is 19 suite names, every one a row below.

**Empty states.** No log had expired: all three `--log-failed` calls returned, 800 to 940 KB each.
No run had zero held failures. Every failed held job split out of its run's log under its own name.

## The suites

`R` = red in that run, `g` = passed. Cause ids are the cause table's. A suite with two mechanisms
carries both, each with its class.

| Suite | 10-04 | 10-03 | 10-02 | Cause | Class | First failing line | Where it lands |
|---|---|---|---|---|---|---|---|
| `codebase-map kit selftest` | R | R | R | C1 | host | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97 in position 247: invalid start byte` | `tools/codebase-map/selftest.py:537`, `got.stdout` is None after the reader thread died |
| `govkit selftest` | R | R | R | C1 | host | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97 in position 22: invalid start byte` | `tools/govkit/selftest.py:909`, `check_epoch_verb`, `TypeError` on a None stdout |
| `foreign-prefix parity (every self-test at three prefixes)` | R | R | R | C8, C1 | tree, derived | `[scripts] review-replay selftest · probe · rc 0 · 1s · RED, an undeclared whole run: it printed no probe marker, so it ran every arm` | `tools/run-gates/foreign-prefix.gov.test.sh:248`; its other two red rows re-run `row-grammar selftest` and `settings-merge selftest`, both C1. On 10-02 the review-replay row was absent and the first red row was row-grammar's |
| `manifest-check self-test` | R | R | R | C3 | host | `fatal: failed to create link '…/mfcheck.Zzkgl0/card-clone/.git/objects/pack/pack-c84681db….idx': Improper link` | `skills/session-kickoff/manifest-check.test.sh:699`, `git clone -q --local` from the D: checkout into the C: temp root; 103 FAIL lines follow from the missing fixture |
| `process-monitor adopter selftest` | R | R | R | C3 | host | `FAIL test_shipped_conf_is_accepted` | `tools/process-monitor/adopt-process-monitor.sh:142`, `[ ! -d "$_r" ]` over `.process-monitor.conf:31`, whose roots are `C:/projects/coding-governance`; the arm sends `--check` to /dev/null, so the log cannot show the line, and push run `37220352485` printed `GATE ok    process-monitor wiring` from a clone AT that path |
| `lexicon selftest` | R | R | R | C2 | host | `- scaffold: and says the seed is unratified … Windows Subsystem for Linux has no installed distr` | `tools/lexicon/selftest.py:947`, `subprocess.run(["bash", …])`; all 22 failed arms of 789 carry the WSL message, most of them in UTF-16 |
| `memory-hygiene self-test` | R | R | R | C1, C7 | host, tree | `FAIL a green check 20 run swallowed its NOT MEASURED line, so an unarmed live-row pin is silent again` | `tools/memory-tree/check-memory-hygiene.test.sh:1935` greps for a UTF-8 em dash that `row_grammar.py` wrote as 0x97 (C1); its second FAIL, `.memory-tree.conf.example does not declare GRAMMAR_WHERE`, is `:2529`'s `_pyexempt` (C7) |
| `python resolver (behaviour + inline parity + idiom ban)` | R | R | R | C6 | tree | `FAIL inline copy of 'resolve_kit_dir' drifted from …/tools/lib/resolve_kit_dir.py: tools/memory-tree/backlog.py (block 1 of 1)` | `tools/lib/resolve-python.test.sh:204`; the second FAIL names `tools/memory-tree/transition_audit.py` |
| `settings-merge selftest` | R | R | R | C1 | host | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97 in position 2523: invalid start byte` | `tools/settings-merge.py:995`, `_selftest`, `TypeError: argument of type 'NoneType' is not iterable` |
| `runlog selftest` | R | R | R | C1 | host | `UnicodeEncodeError: 'charmap' codec can't encode character '\u2713' in position 59: character maps to <undefined>` | `tools/runlog/selftest.py:339`, the suite's own `print` of a check mark to a cp1252 stdout |
| `spec-tokens self-test` | R | R | R | C1 | host | `arm FAIL  a post-cutoff §6 bullet naming the flagged bar REDS as [bar] — expected output to carry: …` | `tools/check-spec-tokens.test.sh` expectations against `tools/check-spec-tokens.py` output: all 34 failed arms print the expected text with `�` where `—` or `·` stands |
| `row-grammar selftest` | R | R | R | C1 | host | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x97 in position 85: invalid start byte` | `tools/memory-tree/row_grammar.py --selftest`, arm `--check grades the tree it is RUN IN`, `got: rc=1 None` |
| `unattended gate selftest shard 2/8` | R | R | R | C4 | host | `fatal: unable to auto-detect email address (got 'runneradmin@runnervmfi6oq.(none)')` | `tools/unattended/check-unattended.test.sh:1386`, `git --git-dir="$ORIGIN" commit-tree` builds the ghost tip with no identity, so the arm reads `fatal: : not a valid SHA1` |
| `unattended driver selftest` | R | R | R | C10, C1 | lost, host | `FAIL dispatch: the refusal does not carry the checker's [bar] line -- UNATTENDED check 49 FAILED — --dispatch refuses: …` | the views arms, from `FAIL F4 the views helper is called once per filing call: expected [1], got [0]` on, are the dropped `write_ask_views` (C10); the `[bar]` arm is `tools/unattended/unattended.sh:10060`, whose `grep -vE 'live spec\(s\) ·\|bar join ·'` cannot drop lines carrying a cp1252 0xB7, so `head -3` keeps those and loses the `[bar]` row (C1) |
| `unattended gate selftest shard 8/8` | R | R | R | C5 | tree | `FAIL the TOOL-dDerivedDocket-19 G0 fixture did not build its four records, so every arm below would grade a missing one` | `tools/unattended/check-unattended.test.sh:5323`, `:5346` and `:5355` write `may: tools\/lander-granted.sh` by `sed`, while `:5333` and every expected message read `bin/lander-granted.sh` |
| `process-monitor census selftest` | g | R | R | C9 | host | `FAIL test_live_tree_dies_completely (got ([], [2612], [(2612, 1, 'kill: 1197: Permission denied')]), wanted ([], [], []))` | `tools/process-monitor/selftest.py`, `test_live_tree_dies_completely`; no commit touches `tools/process-monitor` between `a587e82dc` and `c2ffcf878`, so the 10-04 pass is not a fix |
| `unattended adopter e2e` | g | R | R | C13 | tree | `held: unattended adopter e2e KILLED at its 210s bound, exit 124` | the suite printed no line before the kill; the step ran 211 s in both red runs and 60 s green at `c2ffcf878`, and `ac184eb96` is the only commit between the heads touching `tools/unattended/adopt-unattended.test.sh` |
| `unattended gate selftest shard 1/8` | g | R | R | C11 | tree | `FAIL a dispatched verb is absent from a surface an agent reads, so no run can learn it exists: --heartbeat(usage) --heartbeat(refusal) --task(usage) --task(refusal)` | the verb-surface arm counted two arguments of `--register-task` as verbs; `ac184eb96` says so and changed it |
| `run-gates canary` | g | g | R | C12 | tree | `canary: attribution — AC5 the diff touches the runner: wanted …OWN · KF3…, got: GATE attr  same  INHERITED · offenders 1 · at 0d7c965f` | the two `Killed` lines before it are the canary's own staged kills; `68d6c009c` fixed the runner's KITREL under an MSYS mount, which it records as red on node a too |

## The causes

| Cause | Class | Mechanism | Suites | Disposition |
|---|---|---|---|---|
| C1 | host | Python's stdio codec on the hosted runner is cp1252, where node a runs with `PYTHONUTF8=1` (`sys.flags.utf8_mode` 1, read on node a this pass), so a Python child's `—` or `·` reaches a UTF-8 reader as 0x97 or 0xB7 and a suite printing `✓` cannot encode it | codebase-map kit selftest, govkit selftest, row-grammar selftest, settings-merge selftest, runlog selftest, spec-tokens self-test, memory-hygiene self-test, unattended driver selftest; foreign-prefix parity by derivation | NEW, `TOOL-aMendedFleet-97`. Units 4, 5 and 6 name `tools/govkit/matrix.py`, `tools/memory-tree/transition_audit.py` and `tools/lexicon/lexicon_conf.py`, and none of these suites fails in any of them |
| C2 | host | a Python suite spawns a bare `bash`, which Windows process creation resolves from System32, the WSL launcher, before the Git-Bash on PATH, and the runner has no WSL distribution | lexicon selftest | NEW, `TOOL-aMendedFleet-98`. Unit 6 lists `tools/lexicon/selftest.py`, but for its codec arm; its spec names no spawn |
| C3 | host | the held job runs from `actions/checkout`'s `D:/a/coding-governance/coding-governance/tree`, while the bar job clones to the primary-tree path `C:/projects/coding-governance` the tracked conf names and the temp root shares a volume with | manifest-check self-test, process-monitor adopter selftest | NEW, `TOOL-aMendedFleet-99` |
| C4 | host | the runner has no global git identity, and the shard 2/8 ghost-tip fixture commits in a bare origin that sets none | unattended gate selftest shard 2/8 | NEW, `TOOL-aMendedFleet-100` |
| C5 | tree | a `tools/` to `bin/` rewrite of the G0 fixture's grant path missed the three `sed` lines that spell it with an escaped slash | unattended gate selftest shard 8/8 | NEW, `TOOL-aMendedFleet-101` |
| C6 | tree | the inline `resolve_kit_dir` blocks in `backlog.py` and `transition_audit.py` call `.resolve()` where the canonical block calls `.absolute()`; re-observed at `b566f3459` with the suite's own `blk` extractor, which reads `merge-rows.py`'s copy as identical | python resolver | NEW, `TOOL-aMendedFleet-102`. Unit 5 lists `transition_audit.py` but not `backlog.py`, and its spec is the codec, not this block |
| C7 | tree | `corpus_ids.py` reads `GRAMMAR_WHERE` through `globals()`, and the hygiene suite's python-parity arm exempts `GRAMMAR_DIR` beside it but not `GRAMMAR_WHERE` | memory-hygiene self-test | NEW, `TOOL-aMendedFleet-103` |
| C8 | tree | `tools/workflows/review_replay.py --selftest` neither prints `foreign-prefix-probe: stopped after 1 arm` under `FOREIGN_PREFIX_PROBE` nor is declared in `WHOLE_RUN` | foreign-prefix parity | NEW, `TOOL-aMendedFleet-104` |
| C9 | host | the census live-tree arm's kill of a staged member is refused `Permission denied` on the runner in two of three runs, with no tree change between the red runs and the green one | process-monitor census selftest | NEW, `TOOL-aMendedFleet-105` |
| C10 | lost | merge `01c22e155` dropped `write_ask_views`, so the driver files an ask and never re-renders the views | unattended driver selftest | EXISTING, `TOOL-aMendedFleet-1`, whose spec lists `tools/unattended/unattended.sh`, the file the helper lands in. It is CLOSED on this branch at `fa55c1465`, which no census run's head carries |
| C11 | tree | the verb-surface arm counted `--task` and `--heartbeat`, arguments of `--register-task`, as verbs | unattended gate selftest shard 1/8 | GREEN-SINCE `37196051126`, cleared by `ac184eb96` |
| C12 | tree | the runner's prefix strip left KITREL absolute for a fixture under an MSYS mount, so the canary's AC5 attribution read INHERITED | run-gates canary | GREEN-SINCE `37114721791`, cleared by `68d6c009c` |
| C13 | tree | the suite hung to its bound while its arm 10 expected a stamped `GENERATED_INDEXES` the kit now ships blank; inferred from the timing and the one commit, since the killed suite printed nothing | unattended adopter e2e | GREEN-SINCE `37196051126`, cleared by `ac184eb96` |

## Where the spec's starting facts were wrong

- `spec-tokens self-test` is not a date-relative arm. Its refusals carry the date they should; they
  fail on the separators, C1.
- `process-monitor adopter selftest` is not the temp-root exclusion. The shipped roots do not exist
  on the runner's volume, C3.
- `memory-hygiene self-test`'s check-20 arm is C1, not a tree defect; only its conf-example arm is.
- `unattended driver selftest` carries C1 beside the views loss: its first failing arm is not unit 1's.

## Not observed, and why

- `govkit selftest` spawns a bare `bash` 53 times by `git grep`. Every run stops at its C1 failure
  first, so whether C2 also reds it is unobserved; the C1 unit's own run will see it.
- No log names which of `adopt-process-monitor.sh --check`'s problems fired, because the arm discards
  its output. The not-a-directory line is the one the source, the conf and the green push-bar leg
  leave; the C3 unit's run observes it.
