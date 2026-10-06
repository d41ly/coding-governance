# TOOL-aGraftedHelix-40 — the playbook arm prints its leg's evidence on a miss, and the resume-tick arms grade detachment by a child that outlives the tick

**Status:** SPECCED · rev-1 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 24 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-prompt-TOOL-aGraftedHelix-40-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-40-1-spec-brief.md) | journal | TOOL-aGraftedHelix-41 |

<!-- /gen:spec-records -->

## 1. Goal

The pooled sweep at `b04ab0da` redded two arms of the unattended suites. Neither red is the defect
it reads as. The playbook arm does not reproduce on HEAD, and no reader of `BYPASS_BAN` resolves the
commented spelling differently from the shell (§4). The arm printed none of what its leg said, so
the one red it produced cannot be attributed. The resume-tick arm grades a detached launch by
the tick's whole wall clock, and under induced load it reds while the child is still running (§4).
This unit makes the playbook arm carry its leg's exit and output on a miss. It replaces the two
resume-tick clock arms with an observation the detachment itself produces: the child is alive
after the tick has returned.

## 2. Scope (IN)

- **S1** — The BLOCKER 3 loop in `tools/unattended/check-playbook.test.sh` captures the leg once
  per spelling, as `out=$(run)` with its exit beside it. Its assertion keeps the grep for
  `a tracked EVIDENCE RECORD names the declared bypass flag`. On a miss it prints one FAIL line
  that names the spelling and the leg's exit, and asserts no cause. It then prints every line the
  leg wrote, each prefixed `    leg: `. The miss branch sets `st` and prints its own FAIL line,
  the shape `probe()` already uses for its message check, so a miss counts one assertion and not
  two. A passing spelling prints nothing. Observed by AC1 and AC2.
- **S2** — `tools/unattended/resume-tick.test.sh` declares `STUB_HOLD_S=300` in its prologue,
  beside `STUB_LOG`. It is the hold of every child a stub leaves running, and it bounds only the
  failing path, where a tick that waits on its child returns after it. The figure is PINNED in §4.
  Observed by AC3 and AC4.
- **S3** — The stub's `-p` branch, written by `build_stub`, starts `sleep` for `STUB_HOLD_S` in the
  background. It appends the line `sleeper <pid>` to the stub log, waits on that pid, and then
  appends `done` as today. `remove_stubs` kills every `sleeper` pid the log names as well as every
  stub pid. `read_stub_log` polls for the `sleeper` line, which the stub writes after its `argv`
  line. Observed by AC3 and AC5.
- **S4** — The AC1 block's clock arm is replaced by
  `AC1 the stub's sleeper is alive when the tick has returned, so the launch is detached`. It reads
  the `sleeper` pid off the stub log and derives its Windows pid through `derive_winpid`. It then
  asserts `check_pid_alive` answers `yes`, the probe shape of the U12 and AC13 arms. A derivation
  that yields no pid is a `print_bad` fixture refusal, as U12's is. The existing arms
  `AC1 the stub is still running when the tick has returned` and
  `AC13 the launched pid is alive after the tick returned` are kept unchanged. Observed by AC3.
  **Readers:**
  by name: `tools/unattended/resume-tick.test.sh`, the only file that spells the clock arm's label;
  the brief, the run-state file and the sweep's output quote it as records
  by value: NO VALUE READERS, because an arm label is printed and nothing compares it; the pooled
  runner counts lines opening FAIL and never reads a label
- **S5** — The AC2 orphan stub (`$TMP/stub2/claude`) starts `sleep` for `STUB_HOLD_S` in the
  background and writes that pid to a file beside itself. Today it runs `sleep 60 &`. Its
  logged-out answer is unchanged. The clock arm is replaced by
  `AC2 the CLI's orphan is still running when the tick has returned, so the tick did not wait on it`.
  That arm reads the orphan's pid through `derive_winpid` and `check_pid_alive`, refusing an empty
  derivation the same way. The arm then kills the orphan by its pid, as U12 kills its sleeper.
  Observed by AC4.
  **Readers:**
  by name: `tools/unattended/resume-tick.test.sh`, the only file that spells the orphan stub and
  the clock arm's label
  by value: NO VALUE READERS, because the orphan's 60 s is read by no tool and the arm label is
  printed and never compared
- **S6** — `run_tick_over` stops computing `SECS`, which no arm reads once S4 and S5 land. Its
  comment drops the clause about the wall clock.
  **Readers:**
  by name: `tools/unattended/resume-tick.test.sh`, its AC1 and AC2 clock arms, both rewritten by S4
  and S5
  by value: the same two arms, which compare it against 20; NO VALUE READERS remain after S4 and S5
  Observed by AC6.
- **S7** — The suite's prose matches what it now does. The header's `WHAT THIS FILE DOES NOT CHECK`
  paragraph gains one sentence: no arm grades the tick's own wall clock, because under a pool that
  clock measures the node, and detachment is graded by a child alive after its parent returned. The
  stub comment's `sleeps 15 s` and `remove_stubs`'s `fifteen seconds later` name the hold. The AC1
  block comment's `the tick back within 5 s` is replaced, and so is the orphan block's `The arm
  MEASURES the wall`. In `tools/unattended/resume-tick.sh`, the `check_login` comment's closing
  `and the suite measures the wall` reads that the suite asserts the CLI's orphan outlives the
  tick. Observed by AC6.
  **Readers:**
  by name: `tools/unattended/resume-tick.test.sh` and `tools/unattended/resume-tick.sh`, the two
  files whose comments carry the phrases
  by value: NO VALUE READERS, because a comment is read by no tool; AC6's grep is this unit's own
  observation
- **S8** — The class record `fixed-sleep-does-not-place-a-signal` gains this instance under "Where
  it applies". It names `tools/unattended/resume-tick.test.sh` and its two arms, so the record's
  derived anchors select it for that suite. Observed by AC7.
- **S9** — The `unattended` kit's version moves once, after the unit's last edit to a shipped file,
  in every carrier `tools/check-kit-versions.sh` pairs, and the installed guides are re-adopted.
  `tools/unattended/check-playbook.test.sh` and `tools/unattended/resume-tick.sh` ship as `engine`.
  `tools/unattended/resume-tick.test.sh` is `project-owned` and moves no version alone. Observed by
  AC8.

## 3. Non-goals (OUT)

- **No change to `tools/unattended/check-playbook.sh`.** Its reader sources the conf, which is the
  fix the two-readers class prescribes, and §4 observed it resolve both spellings to `--no-verify`.
  §8 F2 rejects adding a note that prints the resolved flag on every run.
- **No retry of a missed arm.** A merge-bar leg that misses a flagged record transiently is a
  defect to see, not to absorb.
- **No change to the other arms of the playbook suite.** Most of them grep the leg's output and
  print none of it on a miss. That is the same shape, one instance has redded, and §4's gaps name
  it.
- **No change to the driver suite's wall-clock arms.** `tools/unattended/unattended.test.sh`
  grades bounded observations by elapsed time. The open ask `TOOL-aProvenReuse-6` records that
  class there, and unit 41 re-cuts that suite in this run.
- **No change to the tick's behaviour.** §4 found it detached; only a comment in it moves.
- **No new arm, floor, leg, function or conf key.** S4 and S5 replace one assertion each, so the
  executed count and `FLOOR_ASSERTIONS` of both suites stand.
- **The owed suites are not run here.** The main loop runs them once at VERIFYING.

### Edges

- **consumes-from** external — the pooled sweep's evidence at `b04ab0da`: the two FAIL lines, the
  playbook row's `124 executed` against a baseline of 123, and the per-row output files under the
  frozen clone's git dir. This unit builds none of it.
- **hands-off** external — the re-run of the owed unattended suites, which the main loop makes once
  at VERIFYING. If the playbook arm reds again there, its output now names the leg's exit and lines.
- **hands-off** external — a second reader of the same key, outside this kit. govkit's
  `read_conf_key_gaps` strips one quote layer only when a value both opens and closes with it. A
  quoted value followed by a comment therefore keeps its quotes and the comment. Observed on
  2026-10-06: over `A=""   # x`, `B="<flag>"   # y` and `C=""` it reports only C. Sourcing gives A
  empty and B a placeholder. The kit's own check 1 still refuses an empty `BYPASS_BAN`, so nothing
  lands on it, but govkit's report disagrees with the kit. It is a different kit and mechanism, for
  the main loop to adopt as a unit of its own.

## 4. Design

### What the playbook red is not

The brief's hypothesis was a reader of `BYPASS_BAN` that resolves
`BYPASS_BAN="--no-verify"   # the flag the lander bans` to something other than `--no-verify`. Four
observations refute it. Each was made on node `a`, 2026-10-06, with the kit at HEAD `1b4f7720`,
whose `tools/unattended/` is byte-identical to the swept `b04ab0da`. Every figure here is PINNED to
that day.

| Probe | What ran | Result |
|---|---|---|
| P1, slice alone | the suite's prologue, the BLOCKER 2 arm and the BLOCKER 3 loop | green, 3 assertions, 28 s |
| P2, under load | the loop's two spellings five times, beside 24 loops of `git --version` | 10 of 10 red the leg with the EVIDENCE RECORD refusal at rc 1, 8 min 11 s |
| P3, in order | suite lines 1 to 558, every arm before the loop (93 assertions), then the loop | green, 5 min 36 s |
| census | every tracked non-record file naming `BYPASS_BAN` | every value reader sources the conf |

`git diff eb96ea8b2..HEAD -- tools/unattended/` names neither `tools/unattended/check-playbook.sh`
nor `tools/unattended/check-playbook.test.sh`. Only the version markers of the fixture playbook
and its records moved, and nothing in a marker carries the flag.

The probe can answer the other way, which is its liveness. The same probe ran over a scratch copy of
the kit whose check 10 read the key by the old `sed | tr -d '"' | head -1` pipeline. Both spellings
missed, each with a different signature:

| Spelling | Leg exit | What the leg printed |
|---|---|---|
| `BYPASS_BAN='--no-verify'` | 0 | `bypass scan - …/fixture-records: 3 tracked evidence record(s) read`, no refusal |
| `BYPASS_BAN="--no-verify"   # …` | 1 | `PLAYBOOK check 10 FAILED — the declared bypass flag resolves to a value carrying whitespace …` |

That table is the case for S1. The first row is the fail-open shape the arm exists to catch, and
the second is a fail-closed refusal under another check. The sweep's red printed neither, so which
one it was, or whether it was a third thing, is not recoverable. The sweep's output for the row is
four lines: the FAIL line, two lines of a fixture's `git status`, and the trailer.

`124 executed` against 123 is not an extra arm. The loop counts `n=$((n+1))` before its grep, and
`bad` counts once more on a miss. S1's miss branch counts once.

### Reader census

| Reader | Where | How it reads the key | The commented spelling |
|---|---|---|---|
| check 10 | `_conf_key` in `tools/unattended/check-playbook.sh` | sources in a subshell, with a sentinel and a cross-check | `--no-verify` (P1) |
| the gate leg | `tools/unattended/check-unattended.sh` | sources in a process substitution and imports an allow-list | `--no-verify`, by reading |
| the driver | `tools/unattended/unattended.sh` | `. "$CONF"` | `--no-verify`, by reading |
| govkit | `read_conf_key_gaps` in `tools/govkit/govkit.py` | a regex, presence and placeholder only | assigned, which agrees here; §3 Edges names where it does not |

The tick, the adopter, `tools/unattended/check-brief-recorded.sh` and
`tools/unattended/check-pass-order.sh` source the conf too, and none of them reads this key.

### What the resume-tick red is

The tick is detached, and the arm measured the node. Slices of the suite's prologue and its AC1
block, and separately its AC2 orphan block, ran on node `a`, 2026-10-06. The tick's wall was read
by the slice wrapper:

| Block | Condition | Tick wall | Clock arm (`≤ 20 s`) | Detachment signals |
|---|---|---|---|---|
| AC1 | alone, three runs | 19 s, 10 s, 9 s | pass | stub still running, launched pid alive |
| AC1 | beside 8 loops | 19 s | pass | both hold |
| AC1 | beside 24 loops | 68 s | FAIL `no: 68s` | both hold |
| AC2 orphan | alone | 7 s | pass | — |
| AC2 orphan | beside 24 loops | 49 s | FAIL `no: 49s` | the orphan sleeps 60 s, so a tick back at 49 s did not wait on it |

The sweep's own reading was 21 s under an eight-wide pool. Most of a tick's wall comes before the
launch: the liveness read, the login probe and a PowerShell `Start-Process`. None of that is
detachment. The detachment is an ORDERING: the tick returns while its child runs. A clock can only
approximate that ordering, and a pool moves the approximation. This is `TOOL-cSteadyMetronome-1`'s
rule, a gate asserts what the subject does and never what the node does. It is also
`TOOL-aPooledSweep-1`'s reason, that a contended clock cannot grade, applied inside one suite.

### The hold, and the sleeper today's suite leaks

A child that outlives the tick is the signal, and the child must not end on its own before the
read. `STUB_HOLD_S` sets that. It is PINNED at 300 s, which is over four times the worst whole-tick
wall measured above, 68 s. A child starts no earlier than the tick, so the read comes less than one
tick wall after the child starts. The hold costs nothing on the passing path, because the stubs are
killed. On the failing path, a tick that waits on its child returns after the hold, so a staged
break costs 300 s once.

A longer hold makes an existing leak longer, so S3 closes the leak. `remove_stubs` kills the stub
shell by the pid it logged, and that shell's `sleep 60` child survives it. Observed 2026-10-06: after
an AC1 slice exited through the suite's own trap, `ps` listed `sleep 60` with parent 1. S3 logs the
sleeper's pid and kills it too.

### Inventory

No function, file, leg, conf key or gotcha record is minted. The identifiers the unit adds:

| Identifier | Where | Kind |
|---|---|---|
| `STUB_HOLD_S` | the resume-tick suite's prologue | a suite constant; no naming cell grades a shell variable |
| `sleeper <pid>` | the stub log | a line shape read by `remove_stubs`, `read_stub_log` and the S4 arm |
| `    leg: ` | the playbook suite's output on a miss | an output prefix |
| the S4 and S5 arm messages | the resume-tick suite | assertion labels |

No map key moves, because the map does not scan `.sh`.

### Files touched (estimate)

- `tools/unattended/check-playbook.test.sh`
- `tools/unattended/resume-tick.test.sh`
- `tools/unattended/resume-tick.sh`, one comment
- `memory/gotchas/fixed-sleep-does-not-place-a-signal.md`
- `memory/gotchas/INDEX.md`, only if the generator moves it
- `.claude/skills/unattended/SKILL.md`, its version marker through the re-adopt
- every other version carrier `tools/check-kit-versions.sh` pairs for the `unattended` kit, with
  the guides `tools/unattended/adopt-unattended.sh` re-adopts from them

### Rollout

One pass, in this order, each step verified by its own criteria before the next:

1. S1, then AC1 and AC2.
2. S2 to S6, then AC3 to AC6, the staged breaks last because each waits out the hold.
3. S7 and S8, then AC6 and AC7.
4. S9, the version, last, then AC8.

The two halves share no file, so their order is the builder's.

### Gaps it leaves, stated

- **The playbook red stays unexplained.** S1 makes the next one explain itself. It cannot recover
  the one at `b04ab0da`.
- **The other playbook arms still print nothing on a miss.** One loop redded, and one instance is
  not yet a class with an extension pattern. A second unexplained red in this suite is the moment
  to move the evidence print into `run` for every arm.
- **The hold is still a bound.** A detached tick whose read comes more than 300 s after its child
  started would red falsely. The measured worst whole-tick wall is 68 s.
- **A stub that starts after the suite's exit trap** lives for the hold, not for 60 s. A detached
  launch whose child had not started when the trap read the log is the only such case. Every arm
  that launches waits for the `sleeper` line through `read_stub_log` before it moves on.
- **`derive_winpid` reads the MSYS process table.** The stub runs in the process tree PowerShell
  started, not the suite's. That `remove_stubs` kills it by its MSYS pid today shows the table is
  shared, and AC3 observes the read directly.

### Alternatives rejected

- **Print the resolved flag from the leg on every run** (§8 F2, option b).
- **Retry the playbook arm on a miss** (§8 F2, option c).
- **A release-file rendezvous for the stub** (§8 F4, option b).
- **Raise the 20 s threshold** (§8 F4, option c).
- **Delete the clock arms and keep only `done` absent** (§8 F4, option d).

## 5. Production-readiness checklist

- security — No write path and no new surface. The evidence print shows lines the leg already
  writes to the same output, the flag literal included, and only on a miss.
- perf / scale — The playbook loop runs the leg once per spelling, as today, and spawns one `sed`
  only on a miss. Each resume-tick stub adds one background `sleep` and one log line. Each
  replaced arm costs one `ps` poll and one `tasklist` read, where a clock compare cost nothing.
  That is seconds per suite run.
- error / empty / loading states — A pid that `derive_winpid` cannot produce is a `print_bad`
  fixture refusal naming the empty value, never a pass. A playbook miss with empty leg output
  prints its FAIL line and no `leg:` line, which is itself the evidence.
- observability — The playbook miss names the spelling, the leg's exit and every leg line. The
  runner's display selector `^(FAIL|nope|.*FAILED)` will show a `leg:` line carrying the leg's own
  `FAILED` under the row. Its FAIL count reads `^FAIL` only, so the count does not move.
- risks — `tools/unattended/check-playbook.test.sh` ships, so the `harness arms` leg reads it for
  positive assertions of check 10. The grep string stays whole, as the arms leg requires. No
  install-prefix waiver is keyed to either suite's lines. Both suites' executed counts stand, so the
  pooled baselines do not move for this unit.
- testing — Every replaced arm is observed red on a staged break in the suite's own kit copy, and
  the playbook arm's evidence on the old reader, as §6 names.
- migration — None.
- user docs — None. The suites are kit-internal, and the class record is the documented check.

## 6. Acceptance criteria

A slice is a suite's prologue plus the block a criterion names, run from the session scratchpad
under a name that is not a suite name. `HERE` is pinned to the kit dir under test. For the
playbook suite `TMPDIR` is a short directory in %TEMP%. For the resume-tick suite
`RESUME_TICK_TEST_TMP` is the scratchpad and `RESUME_TICK_TEST_GITTMP` a short directory in
%TEMP%. "Under load" means 24 background loops of `git --version` for the slice's duration, killed
by pid after it. A staged break edits the scratch kit copy the suite makes in `$TMP/kit`, or a
scratch copy of the kit dir for the playbook suite, and never a tracked file.

- **AC1** — When a slice of the playbook suite runs the BLOCKER 3 loop over a scratch kit copy whose
  `tools/unattended/check-playbook.sh` reads `BYPASS_BAN` by `sed -n 's/^BYPASS_BAN=//p'` piped
  through `tr -d '"'` and `head -1`, it prints two FAIL lines, and `st` is 1. Each FAIL line names
  its spelling and the leg's exit, 0 for the single-quoted spelling and 1 for the commented one. Each
  is followed by lines opening `    leg: `. The first group carries `bypass scan - `, and the second
  carries `the declared bypass flag resolves to a value carrying whitespace`. No line the loop
  prints carries `resolves to something no record can contain`, and no `leg:` line opens `FAIL`.
  Red when: a miss prints no leg output, as the parent's loop does over the same scratch kit.
- **AC2** — When the same slice runs over the pass's own kit, it prints no FAIL line and no line
  opening `    leg: `, and its assertion count is 2 for the loop. Run with a scratch copy of the
  loop that forces a miss, `n` rises by exactly 1 per miss.
  Red when: a miss counts twice through `bad`, which the parent's loop does.
- **AC3** — When a slice of the resume-tick suite runs its AC1 and AC13 block under load, no line
  opens `FAIL`. The wrapper's own reading of the first tick's wall is printed and exceeds 20 s,
  which shows the load reached the clock that the replaced arm graded. The S4 arm prints `ok`.
  Red when: the scratch tick's `run_detached` runs the launcher in the foreground. Then the S4 arm
  and `AC1 the stub is still running when the tick has returned` both print FAIL once the hold
  ends.
  cost: the loaded slice ran 2 min 44 s on node `a`, and the staged break waits `STUB_HOLD_S`.
  figure: the 20 s is PINNED from the replaced arm, and the loaded wall is DERIVED at observation.
- **AC4** — When a slice of the resume-tick suite runs its AC2 orphan block under load, no line
  opens `FAIL`, and the S5 arm prints `ok`. After the arm, `ps -p` on the orphan's pid lists
  nothing.
  Red when: the scratch tick's `check_login` reads `claude auth status` through a command
  substitution and writes it to the file afterwards. The orphan holds that pipe, the tick returns
  after the hold, and the S5 arm prints FAIL.
  cost: the staged break waits `STUB_HOLD_S`.
- **AC5** — When an AC1 slice copies the stub log to the scratchpad before it exits, the `sleeper`
  pid that copy names is not listed by `ps -p` once the slice's trap has run. Over the parent the
  same slice leaves `sleep 60` listed with parent 1.
  Red when: `remove_stubs` kills only the stub shell, which a scratch copy of the suite with the
  parent's `remove_stubs` pattern shows.
- **AC6** — When `grep -cE '\bSECS\b' tools/unattended/resume-tick.test.sh` runs it prints 0.
  `grep -cE 'sleeps 15 s|fifteen seconds|back within 5 s|MEASURES the wall'` over the same file
  prints 0, and `grep -c 'the suite measures the wall' tools/unattended/resume-tick.sh` prints 0.
  `bash -n` passes on both files.
  Red when: the dead variable stays assigned or a comment still describes the clock arms.
- **AC7** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/resume-tick.test.sh`
  runs, its checklist lists `fixed-sleep-does-not-place-a-signal`, and
  `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: the instance is added without a backticked suite path, so no derived anchor reaches it.
  At the parent the checklist does not list the record (observed 2026-10-06).
- **AC8** — When `python tools/govkit/govkit.py epoch --base <the parent>` runs at the pass's
  commit, its `unattended` line reads `clean` at the bumped version. `bash tools/check-kit-versions.sh`
  exits 0, and `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: a shipped file moved and the version did not.
  figure: the version is DERIVED from the parent at observation.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `playbook validity gate` · `check-wiring self-test` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `gotchas selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `line length` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/check-playbook.test.sh · the BLOCKER 3 loop over a scratch kit whose check 10 reads the key by the old pipeline, as AC1 names · none, one assertion per spelling as before
New arm: tools/unattended/resume-tick.test.sh · the S4 and S5 arms, staged by a foreground launch and a substitution-read login probe in the suite's kit copy, as AC3 and AC4 name · none, each replaces one clock arm

Neither suite is on the bar. A pass runs every criterion above directly, through slices, and the
main loop runs the owed suites once at VERIFYING.

## 8. Open questions

- **FACT-QUESTION · F1 — Does the playbook red reproduce, and does any reader resolve the
  commented spelling differently from sourcing?** Probe: P1, P2 and P3 of §4, and the census.
  Observation: 13 of 13 runs red the leg as the arm expects, and every value reader sources the
  conf. Liveness: the same probe over a kit reading the key by the old pipeline misses both
  spellings, so it can answer yes.
  RESOLVED (agent, 2026-10-06, delegated): it does not reproduce, and no reader re-derives the
  value, so the brief's "fix it at that reader" has no reader to fix.
- **F2 — With no reader to fix, what does the unit do with the playbook arm?** (a) On a miss, print
  the leg's exit and every line it wrote, and stop asserting a cause. (b) Do (a), and have the leg
  print the resolved flag in a note on every run. (c) Retry the arm on a miss. (d) Change nothing
  and re-run at VERIFYING. Option (b) puts the declared bypass flag into every green bar's output.
  That widens where the literal appears, and nobody has inventoried which readers copy leg output
  into records, which is veto 3. Its fact is also one (a) already separates by exit and census
  line, as §4's liveness table shows. Option (c) absorbs a transient in a merge-bar leg. Option (d)
  leaves the next red as unattributable as this one.
  RESOLVED (agent, 2026-10-06, delegated): (a).
- **FACT-QUESTION · F3 — Is the tick still detached?** Probe: the slices of §4, alone and under 8
  and 24 loops. Observation: in every run the stub was still running and the launched pid alive
  when the tick returned. Liveness: the clock arm redded in the same runs at 68 s and 49 s, so the
  load was real, and S4's staged break shows the signals red when the launch is not detached.
  RESOLVED (agent, 2026-10-06, delegated): detached, so the arm measures the node, and the brief's
  first branch governs.
- **F4 — What replaces the clock?** (a) The child alive after the tick returned, held by
  `STUB_HOLD_S`, with its pid logged and killed. (b) A release-file rendezvous: the stub polls for a
  file the arm writes after its read. (c) Raise the threshold. (d) Delete the clock arms and keep
  `done` absent as the only signal. Option (b) gives every stub a polling child and every arm a
  release step. It removes no failure that (a)'s hold leaves on the passing path. Option (c) is the
  shape `TOOL-cSteadyMetronome-1` retired. Option (d) decides AC1 by a signal reading zero, which
  the counter-rule refuses, and it leaves the orphan arm no signal at all, because that arm's
  message is right whether or not the tick waited.
  RESOLVED (agent, 2026-10-06, delegated): (a).
- **F5 — Is the AC2 orphan arm this unit's?** The brief names only AC1. (a) Include it. (b) Leave
  it. It is the same class in the same file, graded under the same pool, and it redded at 49 s under
  the load of §4 while the tick did not wait. Leaving it fixes the instance and not the class.
  RESOLVED (agent, 2026-10-06, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from the unit 40 spec brief, grounded on the run branch at
  `1b4f7720`, with the playbook probes, the reader census and the resume-tick slices run on node `a`.

## 10. Reuse audit

The map probe was `python tools/codebase-map/reuse_lookup.py "a self-test arm that grades
detachment of a launched child by elapsed wall time"`. It ranked name-stem neighbours only, `armed`
and `build_self_chain` first. It printed `unscanned layers: .sh`, so its miss says nothing about the
shell suites this unit edits, which were read by hand. The seams this unit extends are in the
resume-tick suite: `derive_winpid` with the library's `check_pid_alive`, the probe pair the U12 and
AC13 arms already use, and the stub's pid line that `remove_stubs` already reads. The playbook loop
takes `probe()`'s miss shape from the same suite. No existing seam prints a leg's output on a miss.

Recall surfaced `TOOL-cSteadyMetronome-1`, that a gate asserts what the subject does and not what the
node does, and `TOOL-aPooledSweep-1`, that a contended clock cannot grade. It also surfaced the open
ask `TOOL-aProvenReuse-6` on the driver suite's wall-clock arms, and `TOOL-aWokenSentinel-5`'s
measurement of the PowerShell detach. None of them records a ruling that keeps a clock arm here.

Recall terms used: `python tools/memory-recall/query.py "why must a self-test arm not grade a launched child's detachment or a conf reader's resolution by elapsed time or by a message it cannot attribute" --terms "elapsed wall clock contended pooled sweep rendezvous detached launch stub sleeper BYPASS_BAN sourced conf reader two-readers fixed-sleep"`
