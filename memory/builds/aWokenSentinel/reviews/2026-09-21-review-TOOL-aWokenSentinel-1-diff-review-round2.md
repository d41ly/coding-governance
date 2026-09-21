**Serves:** diff-review TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28

# aWokenSentinel — closing diff-review of the built code, round 2 (the fold review)

*Node `a`, 2026-09-21. The Tier-2 adversarial pass over the FOLD of round 1
(`2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md`, eight confirmed findings), run by
`tools/workflows/tier2-review.js` with round 1's confirmed set as `priorFindings`: a fan of four
primed finder lenses over the two fold commits, a skeptic stage in five batches prompted to REFUTE
each finding, one synthesis. The question this round asks is narrower than round 1's: does each fix
close its finding without opening another, is each new arm honest, and did the fold's new facts
(`host:`, `pid-image:`, `lease-utc:`), the index-blob read, the launched-pid logic, fail 55 and the
`lease-utc` compare drift into two answers anywhere across the driver, the library, the tick, the
two suites, the protocol, the Skill and the README. The lens brief was
`python tools/memory-tree/gotchas.py --for-diff e35dd54f..HEAD`, which selected 24 anchored classes
and the 5 universal ones over 54 changed files; the synthesis re-ran it and used its stdout as the
map from each confirmed finding to a class. Every code claim below was re-read at the cited file
and line at the tip, and the two claims that could be measured in seconds were reproduced on this
node; what the synthesis re-read, reproduced, and could not run is listed at the end.*

**Range:** `e35dd54facb78bdad138fe8bae84b734fa947884...HEAD`, HEAD being `e232cd41` (4 commits: the
round-1 record, the fold brief, the fold `9808fe1d`, and its checklist commit `e232cd41`; 54 files,
1450 insertions and 245 deletions; the code is `tools/unattended/{resume-tick.sh, lib-unattended.sh,
unattended.sh}` and the two suites). **Round: 2.**

## Verdict: CLEAN WITH FIXES

The fold did what round 1 asked, and each of the eight round-1 findings is closed as round 1 wrote
its fix. The round-1 blocker is dead in the form it was filed: the session id the tick hands to
`claude -p --resume … --dangerously-skip-permissions` now comes off the index blob, an untracked
record is announced and skipped, and a file write no longer buys a session of the writer's
choosing. No blocker stands this round, which is why this is not BLOCKED. What the fold left is two
highs of the same shape as round 1's high, both of them the recycled-pid kill it set out to close:
the fix guarded the RECORDED pid's kill with an image and, in the same commit, added a SECOND kill
target — the pid the tick launched — with no image at all, so the class round 1's id 2 named is
open again on the instance the fold created, and it fires in ordinary flow with no adversary
because the launcher is a `bash.exe` that frees its pid the moment every completed resume exits.
The other high is the half of the index read the fold did not do: the verdict the tick acts on and
the pid it kills are still `--liveness`'s reads of the WORKING COPY of a tracked record, so the
tick's own security paragraph, the README and the protocol claim a closure wider than the code —
a file-write actor cannot pick the session any more, but can aim the kill and force the launch.
Both fixes are small and in-mandate, one medium is a bound the fold removed without replacing, and
four lows are a digit sieve, a residual the docs do not state, a sentence three carriers did not
amend, and a duplicate heading. The build closes when the two highs land with their REDs observed
and the three overclaiming carriers say what the code does.

## Review shape

Raw 18, confirmed 17, refuted 1, unverified 0, precision 0.94. That is well above the ~0.5 floor
§8 sets and is the tighter priming round 1 asked for. The figure needs one honest qualification:
the pipeline reported 0 duplicates, and the seventeen confirmed ids are SEVEN defects. Ids 1, 5, 11
and 13 are one defect (the launched pid probed and killed with no image); ids 2, 7, 10 and 16 are
one (the verdict and kill target read the working copy, and three carriers say otherwise); ids 3,
8, 12 and 14 are one (the launch pid is a digit sieve over merged stdout and stderr); ids 6 and 15
are one (the in-flight skip has no bound). Ids 4, 17 and 18 stand alone. Four lenses primed on the
same fold found the same two seams four times each, which is coverage of a narrow surface rather
than four independent confirmations, and the report below is written per DEFECT with its lens ids
listed, as round 1 did for its 7/11 pair. Counted per defect, precision is 7 of 8 raw defects —
still above the floor, and the lever for a round 3, if one is owed, is fewer lenses over a fold
this small rather than tighter priming.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by
the pipeline (the four clusters above are the synthesis's observation, not the pipeline's). The run
is complete: no zero below is a zero by absence.

## The fold, finding by finding

Round 1's eight, each against what `9808fe1d` and `e232cd41` did with it. "Closed" means the code
does what round 1's fix text asked and the arm the fold names would go RED without it, as read;
no suite was run by this synthesis (see the last section).

| Round 1 | Fix in the fold | Closed? | What this round found beside it |
|---------|-----------------|---------|----------------------------------|
| 1 BLOCKER, untracked lease honoured | `scan_worktrees` reads `session:`/`host:` off `git grep --cached` (`resume-tick.sh:320`), announces `ls-files --others` hits (`:313-319`); AC14 | Yes, as written | The verdict and the kill target are still working-copy reads (defect B); the header at `:43` claims more than that |
| 2 HIGH, kill aimed at a pid not a process | `write_lease` records `host`, `pid-image`, `lease-utc` (`unattended.sh:3011-3015`); `check_pid_alive pid image` in the library (`lib-unattended.sh:162-167`); `--liveness` passes the image (`:3342`); the tick stands off a foreign host (`:233`); AC10, AC11, AC15 | Yes, for the recorded pid | The launched pid gets the pid-only reading the fix removed (defect A); a same-image recycle still matches and three carriers say otherwise (defect E) |
| 3 MEDIUM, launched pid never recorded | `launched <pid>` on the attempt line (`:286`), read back by `derive_attempts` (`:197`), IN-FLIGHT skip (`:253`) and hung kill (`:267`); AC13 both halves | Yes | The read-back probes with no image (A); the skip has no bound and writes no line, so the cap the pre-fold tick relied on no longer ends a turnless launch (defect D); the pid is a digit sieve (defect C) |
| 5 MEDIUM, FINISHED-UNSTAMPED never acted on | `STALE:*` or `FINISHED-UNSTAMPED:yes` acts (`:241`); AC16 | Yes | Protocol §5, README and Skill still say `STALE` (defect F) |
| 7/11 MEDIUM, fail 54 misdiagnoses an unbound session | fail 55 before the sidecar read (`unattended.sh:2431-2433`); AC15 in the driver suite; `check-arms` lists 55 ARMED per the fold commit | Yes | An owner landing by hand from a plain shell now meets fail 55 where they used to land; the remedy it names works (a plain-shell `--resume --keepalive-id` records `absent`, which lands `unchecked`), so this is a cost, not a wedge, and is noted, not filed |
| 15 MEDIUM, newest stop line graded whoever wrote it | `_su \< _lu` against `lease-utc` (`:2437`); AC16 in the driver suite; the stamp shapes agree (`renderUtc` strips milliseconds, `run-lease.js:206`; `write_lease` writes second precision) | Yes | Nothing |
| 16 LOW, dead-probe line names a NOTE | `RL_FIRST` prefers the `UNATTENDED check` line, then the first non-NOTE line (`:212-214`); AC12's stub NOTEs first | Yes | Nothing |
| checklist `amendment-leaves-its-other-half-standing` (`e232cd41`) | the Skill's read-back paragraph re-said | Yes, for that carrier | The same class stands in three other carriers on the id-5 amendment (defect F) |

## Findings, severity-ranked

| Sev | Ids | Where | Defect |
|-----|-----|-------|--------|
| HIGH | 1, 5, 11, 13 | `tools/unattended/resume-tick.sh:253`, `:267` | The launched pid is probed and tree-killed with NO image; the recycled-pid class id 2 closed for the recorded pid is open on the pid the same fold introduced, in ordinary flow |
| HIGH | 2, 7, 10, 16 | `tools/unattended/resume-tick.sh:266`, `:43`; `README.md:88-90`; protocol `:520` | The verdict and the kill target are `--liveness`'s reads of the WORKING COPY; only `session:`/`host:` come off the index, and three carriers say the working copy decides nothing |
| MEDIUM | 6, 15 | `tools/unattended/resume-tick.sh:253` | The IN-FLIGHT skip has no age bound and writes no attempt line, so a launched CLI alive before its first turn parks the run forever and `ATTEMPTS EXHAUSTED` can never fire |
| LOW | 3, 8, 12, 14 | `tools/unattended/resume-tick.sh:178` | `RD_PID` is every digit of merged stdout and stderr; a failed `Start-Process` yields `12`, the attempt line records a launch that never happened, and the decision line prints `resumed` |
| LOW | 4 | `tools/unattended/lib-unattended.sh:166`; protocol `:234`; `unattended.sh:2998` | A pid recycled to the SAME image reads `yes`; three carriers say a recycled pid reads dead, unconditionally |
| LOW | 17 | `tools/unattended/PROTOCOL.template.md:392`; `README.md:86`; `SKILL.template.md:66` | Three carriers (and both rendered copies) still say the tick resumes a `STALE` run; it acts on FINISHED-UNSTAMPED with `stale: yes` too |
| LOW | 18 | `memory/gotchas/destructive-step-before-its-precondition.md:52` | A duplicate empty `## Where this repo's killers live` heading above the real one |

Blockers 0, highs 2 (eight ids), mediums 1 (two ids), lows 4 (seven ids). Seven defects, seventeen
ids.

### HIGH — defect A, ids 1/5/11/13 · the launched pid is killed by number — `tools/unattended/resume-tick.sh:253`, `:267`

**Defect.** Both reads of the launched pid call `check_pid_alive "$RT_LAUNCHED"` with one
argument (`:253` the IN-FLIGHT probe, `:267` the hung kill). `check_pid_alive`
(`lib-unattended.sh:162-167`) takes `${2:-}` and its `""|absent|"$img"` arm answers `yes` for ANY
process holding the number — the pid-only reading the same function's header names as the
recycled-pid case and that `write_lease` closed for the recorded pid by storing `pid-image`. The
attempt line records `launched <pid>` and nothing else (`:286`), so no later reader could pass an
image even if it wanted to; `read_pid_image "$RD_PID"` is one `tasklist` at launch time and is never
called. The launched pid is `bash.exe` running a three-statement launcher whose last statement is a
foreground `claude -p` (`:280-284`): bash exits and frees the pid the moment the resumed CLI exits,
so EVERY completed resume leaves a freed number on the attempt line.

**Impact.** Two paths, neither needing a reboot or an adversary, both the harm round 1's id 2 was
rated HIGH for. A resume that ran and moved the tree, after which the run stalls again — the
ordinary second-stall case the tick exists for — reads `RT_SINCE=0`, skips the IN-FLIGHT guard, and
`:267` runs `taskkill //PID <freed> //T //F` on whatever now holds the number: an IDE, another
`claude.exe`, `explorer.exe` and every child. Windows reuses freed pids within minutes on a node
that spawns as this fleet does (nine `claude.exe` and a gate bar's worth of bash per hour). A resume
that failed fast, or a reboot with the launch in flight, leaves `RT_SINCE>0`, and `:253` reads the
recycled holder as IN-FLIGHT for that process's lifetime with no attempt line written, so the
consecutive cap never grows and the run is wedged behind a reassuring `skip · IN-FLIGHT` line. Three
carriers claim the guard the path lacks: `README.md:90` ("kills only a pid whose recorded image
still holds it"), the tick header at `:71-73` ("the same function `--liveness` calls" — same
function, half the arguments), and spec 5 §S5 at `:282` ("aimed at the recorded PROCESS, not the
number"). Measured on this node while writing this: `check_pid_alive 4 ''` answers `yes` for
`System`, `check_pid_alive 0 ''` answers `yes` for the idle process.

**Fix.** Record the image at launch, beside the pid: after `run_detached`,
`limg=$(read_pid_image "$RD_PID") || limg=absent` and append ` launched $RD_PID $limg` (the image
LAST, since `System Idle Process` has spaces; the existing `%% launched *` strips and the
`RT_LAUNCHED=${RT_LAUNCHED%% *}` first-token parse already tolerate the extra tokens). In
`derive_attempts` parse `RT_LIMG` as the remainder after the first token, and pass it as the second
argument at both `:253` and `:267`. Say in the header, honestly, that `bash.exe` is a weak image on
a bash-heavy node — that is defect E applied to this pid — and that the class fix is the one that
closes both: `check_pid_alive pid image not-after-utc`, reading the process's start time
(`(Get-Process -Id N).StartTime.ToUniversalTime()` under MSYS, `ps -o lstart=` elsewhere) and
answering `no` for a process that started AFTER the attempt line's own UTC stamp, which the line
already carries at column one. A process that started after the launch was recorded is not the
launch, whatever its image.

**Left-shift.** One RED-first arm in `resume-tick.test.sh` beside AC13's hung half: seed a line
`launched <the suite's own sleep WINPID> claude.exe` older than the run's last move and assert the
sleep is still listed afterwards AND attempt 2 launches; a second seed newer than the last move
under the same wrong image must NOT read IN-FLIGHT. Observe RED against the current tick before
wiring. And gate the CLASS, not the instance: a static arm over the kit asserting every
`check_pid_alive` call site passes a second argument (a grep over `tools/unattended/*.sh` for the
one-argument form, expected 0), because this defect is the second instance of one function called
with half its contract. Class: `destructive-step-before-its-precondition`, the reboot section the
fold itself added to that record, and the charter's "gate the class, not the instance" — the fold
fixed the recorded pid and shipped the launched pid.

### HIGH — defect B, ids 2/7/10/16 · the kill target and the verdict are the working copy's — `tools/unattended/resume-tick.sh:266`

**Defect.** The one index read the fold added is `git grep --cached -E '^(session|host): '`
(`:320`); `session` and `host` are all `run_tick` receives. Everything else it acts on is
`--liveness`'s output (`:211-219`): `RL_VERDICT` decides act-or-skip at `:241`, `RL_PID` and
`RL_ALIVE` aim the kill at `:266`. `print_liveness` (`unattended.sh:3309-3378`) derives `phase`,
`witness`, `session`, `pid` and `pid-image` through `fact()` (`:719-727`), which opens the run-state
file ON DISK. So for a TRACKED record the launch's identity is the index's and the launch's decision
and the kill's target are the working copy's. The tick header at `:43` says "the working copy's
bytes decide nothing"; `README.md:88-90` says "reads the lease from the INDEX, never the working
copy … kills only a pid whose recorded image still holds it"; `PROTOCOL.template.md:520` and the
rendered `memory/guides/UNATTENDED-PROTOCOL.md:520` say "the resume tick reads leases from the index
alone". The lease per `write_lease` is six facts; two are read from the index. AC14's third arm
("a tracked record with a rewritten working copy still resumes") asserts this behaviour as intended
and is green because of it.

**Impact.** The actor is the one round 1's blocker named and the fold's header at `:44` says is
closed — a file write, no stage: an `acceptEdits` session, a sub-agent, an injected edit. On a
tracked, leased record it rewrites `pid: <victim>` and `pid-image: absent` (an empty or absent image
matches anything, `lib-unattended.sh:166`); once the write ages past `RESUME_STALE_BOUND` with
nothing else moving, `--liveness` reads STALE with `pid-alive: yes` and the tick runs
`taskkill //PID <victim> //T //F` on this host under the scheduler's login — any process tree the
actor names, by one file edit. The same actor rewrites `phase: BUILDING` on a LANDED record — the
lease is never cleared on a terminal phase, `write_lease` (`unattended.sh:3009`) being the only
writer of `session:` — and the record flips from TERMINAL to STALE, kills whatever `pid:` names,
and launches the run's authorized session with `--dangerously-skip-permissions` told to "continue
from the phase the run-state file names", the phase the actor wrote. That is a skip-permissions
session obtained by a file write, one notch narrower than round 1's blocker: the session is the
owner's own, resumed with its transcript, not one of the actor's choosing, and the actor needs an
existing leased tracked record rather than any worktree. No tracked `RUN.md` in this repo carries a
real `session:` today (0 of the tracked records; the lease facts are this build's), so the LANDED
path has zero instances here at this tip and will have one per completed unattended run from now
on. Every driver verb stages after `set_fact` (`stage_or_fail`), and the hooks write only
sidecars, so a legitimate record's working copy equals its index blob except inside one verb's
write window — which is what makes the fix below cheap and safe.

**Why HIGH and not BLOCKER.** Round 1 blocked because the security model was false at the launch:
a file write chose the session. The fold bound the session and the host to the owner's staged act,
which is what round 1's fix text asked for, so the model the task states — the tick launches only
on a lease the index holds, on this host — holds at the launch. What is false is the three
sentences that say the index decides EVERYTHING, and what remains reachable is a kill aimed and a
launch forced by a file-write actor on an already-authorized run. That is a real harm on the kit's
most privileged path and it is owed before close; it is not a redesign, and it is not the launch of
an actor-chosen session. The owner can overrule this adjudication with one word.

**Fix.** One spawn, in `scan_worktrees` before `run_tick`: `git -C "$wt" diff --quiet -- "$f"`,
and on a difference `print_decision "$slug" "$wt" "skip · RUN.md differs from the index, and the
tick acts only on the lease the index holds"`. A working copy equal to its index blob makes every
fact `--liveness` then reads equal to the staged one, so the verdict, the pid and the image all
become index-bound without teaching `--liveness` to read blobs. A tick landing inside a verb's
set-then-stage window skips once and says so. Then rewrite `:43`, `README.md:88-90` and protocol
`:520` to say what the code does: the index decides which session, which host, whether a record is
a candidate at all, and (after this fix) refuses to act on a record whose working copy has drifted
from it. Alternative if the skip is unwanted: extend the one grep to `^(session|host|pid|pid-image):`
and refuse the kill when `RL_PID` differs from the index's pid — but that still leaves `phase:` to
the working copy, so the diff-quiet form is the one that closes the class.

**Left-shift.** Retarget AC14's third arm: a tracked record with a rewritten working copy must
produce the announced skip, no launcher, no attempt line; the `--resume $SID` and `99999999-aaaa`
assertions then hold trivially and stay. Add the kill arm: tracked record staged with
`pid: 999999999`, working copy rewritten to the suite's own sleep WINPID with `pid-image: absent`,
tree older than the bound — the sleep must survive and the skip line must print. Observe RED against
the current tick. Class: `two-answers-to-one-question` across the three carriers and the code, and
`fold-text-is-unreviewed-surface` — the sentence at `:43` is fold prose, written after the fix,
claiming the fix's whole intent rather than its extent.

### MEDIUM — defect D, ids 6/15 · the in-flight skip is unbounded — `tools/unattended/resume-tick.sh:253`

**Defect.** `:253-255` returns on IN-FLIGHT whenever the launched pid is alive and `RT_SINCE>0`,
writes no attempt line, and consults no clock. `RESUME_TURNS` bounds turns and `RESUME_ATTEMPTS`
bounds lines; nothing bounds a launched process that stays alive without moving any of
`--liveness`'s four signals. The pre-fold tick (`02648948`) had no in-flight guard: every STALE tick
relaunched and the cap fired after `RESUME_ATTEMPTS`, which is the path the header at `:70-71`
names as the only notification hook ("`ATTEMPTS EXHAUSTED` is the line a notification would key
on"). The fold added the guard and removed that path without a replacement bound; `README.md:90`
states the unbounded rule as design ("in flight until the tree moves"). AC13's in-flight fixture —
a stub that sleeps — IS this state, and the arm asserts the skip and nothing about its end.

**Impact.** A `claude -p --resume` hung before its first transcript write — an auth loop, a network
retry, an MCP init that never returns — keeps `bash.exe` alive with the tree unmoved; every tick
prints `skip · IN-FLIGHT` and returns, `RT_SINCE` never reaches the cap, and the one line a
notification keys on is never printed. Narrow — a hang AFTER the first transcript write moves the
tree, reads `RT_SINCE=0`, and is killed at `:267` — but it is exactly the hung-process class the
tick exists for, and rev 4 bounded it in six ticks. Combined with defect A, a recycled pid produces
the same permanent skip with no hang at all.

**Fix.** Bound the reading by the kit's own staleness bound, derived once: have `--liveness` print
`stale-bound: <seconds>` (the driver already owns `RESUME_STALE_BOUND`; the tick deliberately does
not read it, `:66`), read it in `read_liveness`, and in `run_tick` treat a launched line older than
`now - stale-bound` as hung even when `RT_SINCE>0` — it then takes the existing kill row at `:267`,
appends its line, and counts against the cap. The decision line for that case should say
`IN-FLIGHT past bound`, so a scheduler log shows the stall rather than a skip.

**Left-shift.** Two arms in `resume-tick.test.sh`: a launched line inside the bound with a live
sleep (the existing skip, unchanged); the same line stamped older than the bound with a live sleep —
attempt 2 launches and the sleep is gone. Observe RED against the current tick. Class:
`amendment-leaves-its-other-half-standing` — the header's old sentence "the next tick launches
again, and the cap ends it" was the bound; the amendment removed the sentence and the bound with it.

### LOW — defect C, ids 3/8/12/14 · the launch pid is a digit sieve — `tools/unattended/resume-tick.sh:178`

**Defect.** `:175` sends PowerShell's stdout AND stderr into the pid file (`>"$2" 2>&1`); `:178`
takes `tr -dc '0-9'` over it with no shape check; `:180` returns 0 whatever PowerShell exited; `:286`
appends the result as `launched <n>` and `:287` prints `resumed`. Reproduced on this node while
writing this: `Start-Process` against a missing `-FilePath` exits 1, writes `At line:1 char:2` and
the argv echo truncated with `...`, and the sieve yields `12`; the whole-line form
`tr -d '\r' | grep -m1 -xE '[0-9]+'` yields nothing. The header's own contract at `:167` — `RD_PID`
"empty when the launch reported none" — does not hold for a launch that reported an error.

**Impact.** A failed launch records a fabricated pid on the attempt line and a `resumed` line in
the scheduler log; the fabricated number feeds defect A's unguarded probe. On this node `12` is
free, so the next tick reads `no`, relaunches, fails again, and the cap ends it after six lying
lines — which is why the seam is silent. Where the error text's digits collapse to a held pid (0
and 4 read `yes` here), the run wedges IN-FLIGHT or `:267` kills that process's tree. Four lenses
split three low and one medium; the reason it heads the lows rather than joining the mediums is
that the cap bounds today's harm, and the reason it is not cosmetic is the `resumed` line — a
failed launch reported as success is the reassuring-line class §7 refuses in any probe.

**Fix.** Accept only a whole-line integer: `RD_PID=$(tr -d '\r' < "$2" | grep -m1 -xE '[0-9]+')`,
keep the file's first line for the decision, and print `launch failed: <first line>` instead of
`resumed` when it is empty; a failed launch then writes no `launched` token, which `-z "$RD_PID"` at
`:286` already handles, and the attempt line still counts toward the cap.

**Left-shift.** One arm: stub `cygpath` (or point `command -v bash` at a missing path) so
`Start-Process` fails, and assert the attempt line carries no `launched` token and the decision
line says `launch failed`. Observe RED. Class: none selected by the brief; the shape is a shape-blind
extraction reading an error as a value, a sibling of `line-count-reads-empty-capture-as-one`.

### LOW — defect E, id 4 · a same-image recycle still matches, and three carriers say otherwise — `tools/unattended/lib-unattended.sh:166`

**Defect.** `check_pid_alive` compares image only, so a pid recycled to another `claude.exe` under
a recorded `pid-image: claude.exe` reads `yes`. The library header (`:153-158`) names `absent` as the
one unguarded case and names "the owner's new interactive session" — a `claude.exe` — as what the
guard keeps the kill off; protocol §2 fact 16 (`PROTOCOL.template.md:234`, rendered `:234`) says "a
recycled pid reads dead" unconditionally; `unattended.sh:2998` says "a number a reboot recycled reads
`pid-alive: no`". On a node whose job is running `claude.exe` (nine live here), a same-image
successor after the fleet's recorded reboot is the likely one, and the guard closes the cross-image
case only. Measured: `check_pid_alive 4 "$(read_pid_image 4)"` answers `yes`, as designed and as
the residual.

**Fix.** Either state the residual in all three carriers ("the image closes the cross-image case;
a same-image recycle still matches, and the start-time compare is the upgrade"), or close it with
the mechanism defect A's fix names: record the process start time at lease time beside `pid-image`
and answer `no` for a process that started after `lease-utc`. The second is one more derived fact
in a function that now writes six and is the fix for A's class too, which is the argument for
doing it once.

**Left-shift.** If closed: an arm leasing the suite's sleep with a `lease-utc` older than the
sleep's start asserting `pid-alive: no`. If stated: no arm; the carriers are the fix. Class:
`two-answers-to-one-question` — the code answers "cross-image", three records answer "any".

### LOW — defect F, id 17 · three carriers still say `STALE` alone — `tools/unattended/PROTOCOL.template.md:392`

**Defect.** `resume-tick.sh:241` acts on `STALE:*|FINISHED-UNSTAMPED:yes` and its own header
`:22-23` lists the second arm, yet `PROTOCOL.template.md:392`, `README.md:86` and
`SKILL.template.md:66` still say the tick resumes a `STALE` run, and the rendered
`memory/guides/UNATTENDED-PROTOCOL.md:392` and `.claude/skills/unattended/SKILL.md:66` carry the
same sentence. The fold's own checklist commit (`e232cd41`) fixed this class in the Skill's
read-back paragraph and left these three.

**Impact.** An owner reading `verdict: FINISHED-UNSTAMPED` from `--liveness` concludes from the
contract that the tick will not touch the run; it kills the recorded pid's tree and launches a
skip-permissions resumer on it.

**Fix.** State the acting set once, in the protocol §5 sentence ("resumes a run `--liveness` reads
STALE, or FINISHED-UNSTAMPED with `stale: yes`"), point README `:86` and the Skill `:66` at it, and
re-render both generated copies in the same commit so `--check` stays in sync.

**Left-shift.** None machine-shaped beyond the existing render parity; the class is
`amendment-leaves-its-other-half-standing`, and the fold commit that named it is the precedent.

### LOW — defect G, id 18 · a duplicate empty heading — `memory/gotchas/destructive-step-before-its-precondition.md:52`

**Defect.** The fold's new section put a second `## Where this repo's killers live` at `:52`
directly above the existing one at `:54`, with nothing between them (headings at 10, 22, 30, 38,
52, 54, 66). A heading-keyed reader resolves to the empty one.

**Fix.** Delete `:52` and its blank line.

**Left-shift.** None; cosmetic.

## What the refuted one was

One finding, id 9, did not survive its skeptic and is not listed; it was dropped without
reachability re-established, per §8, and its text did not reach the synthesis. Ids 1 through 8 and
10 through 18 are the seventeen above.

## The bug-class brief over this range

`python tools/memory-tree/gotchas.py --for-diff e35dd54f..HEAD` selected 29 classes. Five are
named above against a confirmed defect: `destructive-step-before-its-precondition` (A — the
reboot section the fold added to that record describes the instance the fold shipped),
`two-answers-to-one-question` (B, E), `fold-text-is-unreviewed-surface` (B — the sentence at `:43`),
`amendment-leaves-its-other-half-standing` (D, F). Two of the fold's own new entries,
`guard-fed-the-value-it-supersedes` and `witness-graded-against-a-fact-written-after-it`, drew no
finding: the guards they describe are the ones the fold built, and this round found them correct.
Defect C fits no selected class. The remaining classes were on the lenses' brief and drew no
confirmed finding; that is the fan's result, not a certificate that the class is absent.

## What the synthesis re-read, reproduced, and could not run

Re-read at the tip, line by line, for every claim above: `tools/unattended/resume-tick.sh` in full;
`tools/unattended/lib-unattended.sh` at 118-167; `tools/unattended/unattended.sh` at 603, 715-727,
2330-2340, 2368-2450, 2985-3018 and 3300-3378; `tools/unattended/run-lease.js` at 205-207; the fold
diffs of both suites in full; `README.md` at 84-92; `PROTOCOL.template.md` at 228-236, 390-394 and
516-540 and its rendered copy at the same lines; `SKILL.template.md` at 64-68 and its rendered copy;
the gotcha's heading list; the fold commit's message. Reproduced on this node: the failed
`Start-Process` sieve (`12` from the sieve, empty from the whole-line grep) and `check_pid_alive`
on pids 0, 4 and 12 with an empty image, a wrong image and the matching image. Grepped: no tracked
`RUN.md` in this repo carries a non-`absent` `session:` (0 of the tracked records).

NOT run: any suite, leg or bar. An attempt to run `resume-tick.test.sh` was refused by the
project's own `gate-guard.js`, because the run on this branch is at BUILDING and the suites run once
at VERIFYING; that refusal is correct and is recorded here so nobody reads the arm claims above as
observed. The fold commit states every arm was observed RED against its break with each block run
ALONE and that no suite ran whole; the AC14 third-arm assertion this round reads as documenting
defect B is taken from the suite's text, not from a run. Every left-shift arm above is a design and
not an observation, and the first thing each fix owes is its RED.

## Disposition

CLEAN WITH FIXES. No blocker stands, and the round-1 blocker is closed in the form it was filed.
The build closes when: defect A lands (the image on the attempt line at minimum, the start-time
compare as the class fix) with its RED observed; defect B lands (the `diff --quiet` skip and the
three carriers re-said) with its RED observed and AC14's third arm retargeted; defect D lands or is
parked by id with a reason in the run-state file; defects C, E, F and G land or are parked the same
way. If a round 3 runs, it reads from this round's recorded tip, carries the seven defects above as
`priorFindings` by defect rather than by lens id, and can afford two lenses rather than four over a
fold this narrow.
