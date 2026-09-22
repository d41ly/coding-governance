**Serves:** diff-review TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28

# aWokenSentinel — closing diff-review of the built code, round 1

*Node `a`, 2026-09-21. The Tier-2 adversarial pass over what the build SHIPPED, run by
`tools/workflows/tier2-review.js` as the build method's M8 prescribes: a fan of four primed finder
lenses over the cumulative diff, a skeptic stage in four batches prompted to REFUTE each finding, one
synthesis. The lens brief was the recurring-bug-class checklist for this range,
`python tools/memory-tree/gotchas.py --for-diff 5f9648d6..HEAD`, which selected 42 anchored classes
and the 5 universal ones over 151 changed files; the synthesis re-ran it and used its stdout as the
map from each confirmed finding to a class. Every code claim below was re-read at the cited file and
line at the tip; what the synthesis re-read, and what it did not run, is listed at the end. The two
records that decide ids 29 and 30 in this range are a decision and a backlog row with no spec H1, so
the binding line names the twenty-eight units and not them.*

**Range:** `5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b...HEAD`, HEAD being `e35dd54facb78bdad138fe8bae84b734fa947884`
(51 commits; 32 files under `tools/unattended/`, `tools/workflows/` and `tools/memory-tree/check-arms.py`,
3738 insertions and 235 deletions; 151 files in all with the records). **Round: 1.**

## Verdict: BLOCKED

One blocker stands, and it is the security model rather than a mechanism. The build's stated model is
that the tick launches a skip-permissions session only "on a run the owner authorized by committing
its build folder", and the tick checks nothing of the kind: it globs `RUN.md` off the worktree,
tracked or not, and hands whatever `session:` it finds to `claude -p --resume … --dangerously-skip-permissions`.
That turns a file write — the one capability a permission-gated session, a sub-agent or an injected
edit already has — into an unprompted session under the owner's login, ninety minutes later and again
every stale cycle. The fix is small and in-mandate, and the build does not close with its own security
model false at the one place that grants the widest privilege. One high follows: the pre-launch kill
is aimed at a pid, not at the process the lease named, and this fleet has a recorded reboot that
recycles pids. Four mediums are gaps in the resumer's coverage and in `--landed`'s read-back, each of
them a state the build set out to close and did not; one low is a diagnostic that names the wrong
line. Two of the eight confirmed ids are one defect reported twice, said below where it matters.

## Review shape

Raw 16, confirmed 8, refuted 8, unverified 0, precision 0.50. That sits ON the ~0.5 floor §8 sets,
not above it. Ids 7 and 11 are the same defect (fail 54's remedy for an unbound session) found by two
lenses and passed by two skeptic batches, and the pipeline's dedup did not collapse them; counted as
one defect the confirmed set is 7 and precision 7/15, below the floor. The refuted half was spread
across every lens rather than concentrated in one, so the lever for round 2 is tighter priming on the
sidecar and lease seams, where every confirmed finding sits, rather than fewer lenses.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 4/4 returned, 0 died. 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by
the pipeline (the 7/11 pair above is the synthesis's observation, not the pipeline's). The run is
complete: no zero below is a zero by absence.

## Findings, severity-ranked

| Sev | Id | Where | Defect |
|-----|----|-------|--------|
| BLOCKER | 1 | `tools/unattended/resume-tick.sh:253` | The tick grants skip-permissions on a lease read from any worktree file, tracked or not; the committed-mandate property is never checked where it matters |
| HIGH | 2 | `tools/unattended/resume-tick.sh:213`, `tools/unattended/unattended.sh:3251` | `pid-alive: yes` proves some process holds the pid; the tree kill then runs on a recycled pid after a reboot or on another node |
| MEDIUM | 3 | `tools/unattended/resume-tick.sh:219` | The tick never records the pid it launched, so the pre-launch kill is inert against a hung resumed session and a second resumer joins the first |
| MEDIUM | 5 | `tools/unattended/resume-tick.sh:194`, `tools/unattended/unattended.sh:3356` | FINISHED-UNSTAMPED outranks STALE, so a dead session at LANDING with its witness on main is skipped by every tick forever |
| MEDIUM | 7, 11 | `tools/unattended/unattended.sh:2425` | fail 54's remedy assumes the current session is the leased one; an unbound takeover session loops on it with a false "hook is unwired" diagnosis |
| MEDIUM | 15 | `tools/unattended/unattended.sh:2335` | `read_stop_listing` takes the newest line whoever wrote it, so a LANDING line from a dead incarnation passes check 53 against the id the new lease replaced |
| LOW | 16 | `tools/unattended/resume-tick.sh:177` | The dead-probe diagnostic is the driver's first merged stderr/stdout line, which is a source-time NOTE for any adopter on a kit default |

Blockers 1, highs 1, mediums 4 (five ids), lows 1.

### BLOCKER — id 1 · the tick honours an untracked lease — `tools/unattended/resume-tick.sh:253`

**Defect.** `scan_worktrees` globs `"$wt/$mr"/builds/*/RUN.md` off the filesystem and takes the
first `session:` line of each hit; `print_liveness` (`unattended.sh:3296`) tests only `[ -f "$rel" ]`.
Neither consults `git ls-files`, the build README, nor `check_authorization` (`unattended.sh:1429`),
which only `--preflight` calls (`:2783`). `run_tick` then goes from `verdict: STALE` straight to the
launcher at `:228`, `claude -p --resume <sid> --dangerously-skip-permissions --max-turns <n>`. The
untracked file itself is the newest write by `scan_dirty_paths`, so the staleness clock starts at the
drop and reads STALE `RESUME_STALE_BOUND` later with no further action by anyone.

**Impact.** Any actor that can write one file under a worktree — an `acceptEdits` session, a
sub-agent, a prompt-injected edit — drops `memory/builds/<slug>/RUN.md` with `phase: BUILDING` and
`session: <its own id>` and, once the tick is registered, obtains a skip-permissions session under
the owner's login for `RESUME_TURNS` turns, repeated each stale cycle because a transcript write resets
the consecutive cap. Protocol section 9 (`memory/guides/UNATTENDED-PROTOCOL.md:534`) concedes that a
run with shell access defeats local checks; it does not concede a file-write-only actor, which is a
strictly weaker attacker, and every leg check it describes iterates over the TRACKED records. The tick
is the one reader that does not, and it is the reader that grants the most.

**Fix.** Before `run_tick`, require the record to be in the index and read the lease from there:
`git -C "$wt" ls-files --error-unmatch -- "$mr/builds/$slug/RUN.md"` and
`git -C "$wt" show ":$mr/builds/$slug/RUN.md"` for the `session:` fact. The index is what
`stage_or_fail` (`unattended.sh:1648`) writes, so `--resume --keepalive-id` still counts. An untracked
hit prints `skip · RUN.md is not tracked` and launches nothing. This closes the file-write attacker
only; an actor who can stage is the shell-access case section 9 already concedes, and the remote-BASE
check stays `--preflight`'s.

**Left-shift.** One arm in `tools/unattended/resume-tick.test.sh`: an untracked `RUN.md` carrying a
live session id in a tree older than the bound must produce the skip line, no attempt line and no
launcher file; then `git add` it and the same tick must launch. Observe RED with the guard removed
before wiring. Class: `inputs-inside-the-subjects-reach` — the tick's authority input is a file the
subject it grades can write.

### HIGH — id 2 · the tree kill is aimed at a pid, not at the leased process — `tools/unattended/resume-tick.sh:213`

**Defect.** `check_pid_alive` (`unattended.sh:3251-3261`) runs `tasklist //FI "PID eq N" //NH` and
matches the pid token alone; the image name on the same row is discarded, and `write_lease`
(`unattended.sh:2979-2989`) records session, pid and keepalive and nothing about the host, image or
start time. `run_kill_tree` (`resume-tick.sh:129-136`) then runs `taskkill //PID N //T //F` on
whatever holds N.

**Impact.** Two paths hand the pid to a stranger. A reboot mid-run, a recorded event on this fleet and the
research record's own stall class C (`build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md:28`),
recycles the pid to whatever the owner starts next; every liveness signal predates the reboot, so the first tick past the bound reads STALE,
`pid-alive: yes`, and force-kills the owner's new interactive `claude.exe`, an IDE, or `explorer.exe`
and every child, then launches a resume, and does it again the next cycle. `RUN.md` is tracked, so a
run branch checked out on another node carries node `a`'s pid into node `b`'s process table — the
weaker path, since it needs a human checkout, but the reboot path alone makes the collateral kill
real. This is `destructive-step-before-its-precondition`: the kill's useful precondition, that N IS the
run's process, is never probed.

**Fix.** Record what the lease names: `write_lease` adds `host:` (`COMPUTERNAME`, else `hostname`)
and `pid-image:` (the image column of the same `tasklist` row, `comm=` on the POSIX arm) beside
`pid:`; `check_pid_alive` matches pid AND image, printing `no` on a mismatch; `run_tick` refuses to
kill or launch when `host:` is not this node and prints why. Three facts in a function that already
writes three.

**Left-shift.** An arm in `tools/unattended/unattended.test.sh` that leases the suite's own `sleep`
pid under a recorded image of `claude.exe` and asserts `pid-alive: no`; an arm in
`resume-tick.test.sh` with a foreign `host:` asserting no kill and a printed refusal. Stage each
break and observe RED first.

### MEDIUM — id 3 · the launched pid is never recorded — `tools/unattended/resume-tick.sh:219`

**Defect.** The attempt line at `:219` carries the OLD pid; the launcher at `:225-229` captures
none; `run_kill_tree` is only ever fed `RL_PID`, which `--liveness` reads from `RUN.md`, and `RUN.md`'s
pid changes only when the resumed session itself runs `--resume --keepalive-id` (`verb_resume`,
`unattended.sh:3387-3396`). The CONTINUE payload (`:217`) asks for that and nothing enforces it;
`--resume <sid>` keeps the same session id so no reader notices a stale pid.

**Impact.** A resumed session that hangs (class B, the case the research record names the kill for)
or ignores the payload's first instruction (recorded fleet behaviour) leaves the lease naming the dead
pid; the next STALE tick reads `pid-alive: no`, kills nothing, and launches a second
`claude -p --resume` of the same session into the same worktree — two skip-permissions agents editing
one tree and racing `set_fact`'s last-writer-wins on one `RUN.md`, a third and fourth following every
`RESUME_STALE_BOUND`. The `NO IN-FLIGHT GUARD` header (`:38-42`) reasons only about a launch that
produced no turn; a launch that produced a turn and then hung is the unguarded case. Closed by a
compliant resumed session, open otherwise.

**Fix.** Capture the launched pid (`Start-Process -PassThru`, printing `.Id`; `$!` on the POSIX
arm) into the attempt line the tick already writes and parses, and on the next STALE tick kill that
pid's tree too, or treat it alive as in-flight and skip.

**Left-shift.** An arm in `resume-tick.test.sh`: after a launch, the newest attempt line carries a
`launched <pid>` field; a second STALE tick with that pid alive either kills it (observed absent
afterwards) or prints the in-flight skip. No selected class names this shape; it is a guard fed only
the value the launch it guards was meant to supersede, and the class is worth a
`memory/gotchas/` entry if the fix is not gated.

### MEDIUM — id 5 · FINISHED-UNSTAMPED outranks STALE, and the tick acts on STALE alone — `tools/unattended/resume-tick.sh:194`

**Defect.** `print_liveness` (`unattended.sh:3355-3359`) ranks `finished-unstamped` before the stale
test, so a LANDING record whose witness is an ancestor of `refs/remotes/origin/<default>` prints
`stale: yes` with `verdict: FINISHED-UNSTAMPED`; `run_tick:194` skips every verdict but STALE.

**Impact.** A session that dies between the lander's push and `--landed` — process death, a reboot,
or the tick's own resumed session hitting `--max-turns` — leaves the record at LANDING with its work
on main, and no actor stamps it: the stop-guard's landing-unstamped row (`stop-guard.js:141`) needs a
live bound session, the stall-recorder only records, the keepalive is reaped before `--close`, and
`check_single_live` (`unattended.sh:1372-1385`) only excludes the record from the next run's live
count. The terminal stamp, the units-at-landing freeze and the keepalive read-back never land — the
B1 wedge, reopened for the dead-session case unit 8 did not cover. Spec 5's table, spec 8's non-goal
and `resume-tick.test.sh` (no FINISHED-UNSTAMPED arm; the grep count is 0) show the composition was
never recorded as accepted. Class: `amendment-leaves-its-other-half-standing` — unit 8 handled the
live half of this state and the dead half stands.

**Fix.** `read_liveness` also captures `stale:`; the guard at `:194` acts when the verdict is STALE
or when it is FINISHED-UNSTAMPED with `stale: yes`. The payload's "continue from the phase the
run-state file names" is `--landed` at LANDING and needs no change. Re-ranking in `print_liveness`
would also work but moves the stop-guard's message selection, so the tick-side read is the smaller
diff.

**Left-shift.** An arm in `resume-tick.test.sh`: fixture at LANDING with a witness merged into
`refs/remotes/origin/main`, `session:` set, HEAD older than the bound — must produce an attempt line
and a launcher. Observe RED at the tip before the fix.

### MEDIUM — ids 7 and 11 · fail 54 misdiagnoses an unbound session — `tools/unattended/unattended.sh:2425`

One defect, two ids; the pipeline reported both and both survived their skeptic, so both are listed
and adjudicated together.

**Defect.** `read_stop_listing` (`:2330-2340`) returns 1 only when `stop.<slug>.log` is absent or
empty, so the `unchecked` branch at `:2421` never applies once a sidecar from an earlier bound session
exists; the newest line then carries that session's pre-close phase and fail 54 fires. Its remedy says
END THE TURN, but `stop-guard.js` binds by `resolveLease` (`run-lease.js:172-174`), which filters
`RUN.md`'s `session:` against the payload's `session_id`; a session other than the leased one appends
nothing, re-runs `--landed` into the same refusal, and the only alternate diagnosis the text offers —
the hook is unwired — is false while `adopt-unattended.sh --check` reports it wired. No verb compares
`CLAUDE_CODE_SESSION_ID` with the lease, so a fresh owner session can `--close` and reach this
unbound. The header's "a session never bound … is never wedged" (`:2412`) is false for this state,
and the actual remedy, `--resume <slug> --keepalive-id <id>`, is named nowhere on the path.

**Impact.** The dominant recorded resume pattern — a human taking over a dead run in a fresh session,
and the only route for a run whose pid the tick cannot reach — loops on a false diagnosis. Recoverable,
but the operator is sent to the wrong tool. Class: `two-answers-to-one-question` — the comment
answers "never wedged" and the code answers "wedged".

**Fix.** Before the sidecar read, compare `${CLAUDE_CODE_SESSION_ID:-}` with `fact "$rel" session`;
on a mismatch or an absent fact refuse naming the mismatch and `--resume $slug --keepalive-id <id>`
as the step that lets the stop-guard record this session, keeping the existing text for the bound
case.

**Left-shift.** An arm in `unattended.test.sh`: pre-close stop line present, `CLAUDE_CODE_SESSION_ID`
set to a value the record does not hold, assert the re-lease remedy is printed and END THE TURN is not.

### MEDIUM — id 15 · the newest stop line is graded whoever wrote it — `tools/unattended/unattended.sh:2335`

**Defect.** `read_stop_listing` returns `tail -n 1` with no session or freshness filter;
`verb_landed` (`:2416-2432`) accepts any line whose phase is LANDING (check 54) and greps the CURRENT
`keepalive` fact against that line's `session_crons` (check 53). The stop-guard writes a LANDING line
on EVERY stop of a bound session at LANDING, allowed or blocked (`stop-guard.js:215-222`), including
the pre-push class-E park the hook was built for; `verb_resume --keepalive-id` replaces `keepalive`
and writes nothing to the stop log.

**Impact.** After a stall and a resume — the tick's, or the Skill's Resume section, which reaps the
old id, schedules a new one and runs `--resume --keepalive-id` — the resumed incarnation's one-turn
lander then `--landed` reads the dead incarnation's LANDING line, whose listing predates the new id by
construction, prints `keepalive-reaped: checked` and stamps LANDED while the new idle-wake fires on:
the false pass the read-back (unit 7) exists to refuse. The verb's own NOT CHECKED list (`:2413-2415`)
does not name a line older than the lease, so it is an unrecorded gap. The stop line does carry a
`session` key (`stop-guard.js:216`), but a tick resume keeps the session id, so filtering by session
would close only the fresh-session half. The driver-suite fixtures write stop lines with no `session`
key and never replace the lease, so no arm can see this. No selected class names it; it is an
observation older than the fact it grades.

**Fix.** `write_lease` records a `lease-utc` fact beside `session:` and `pid:`; `--landed` treats a
newest line whose `utc` is older than that fact as pre-close, the existing fail 54 path, so only a
listing the CURRENT lease's incarnation produced can pass.

**Left-shift.** An arm in `unattended.test.sh` that seeds a LANDING stop line, replaces the lease,
and asserts check 54 refuses; and a `memory/gotchas/` entry for the class, since the shape — a
witness graded against a fact written after it — recurs wherever a sidecar outlives a lease.

### LOW — id 16 · the dead-probe diagnostic names a NOTE — `tools/unattended/resume-tick.sh:177`

**Defect.** `read_liveness` captures the driver with `2>&1` and takes `head -n 1` as `RL_FIRST`;
`run_tick:192` prints it as the whole diagnostic on a failed probe. The driver's source-time code
(`unattended.sh:349-360`) calls `read_bound_key` for three bounds before any verb dispatches, and
`lib-unattended.sh:99` echoes a NOTE to stderr for any undeclared key; `:360` adds one more when
`RESUME_STALE_BOUND` is below the sum. The check-52 sentence (`fail`, `:380`) reaches stdout only
when `print_liveness` runs later.

**Impact.** For any adopter on a kit default — the supported path — the one line a scheduler log
keeps for a dead probe reads `liveness probe failed: unattended: NOTE - this project declares no …`.
This repo declares every key, which is why no arm saw it; AC12's stub driver emits a single stdout
line, the `staged-break-substitutes-a-synthetic-value` class.

**Fix.** Take `RL_FIRST` from `grep -m1 '^UNATTENDED check'` over the captured text, falling back to
the first stdout line; give AC12's stub a stderr NOTE before its refusal.

**Left-shift.** That stub change is the arm: with the NOTE present the tick's line must name check 52.

## What the refuted half was

Eight findings did not survive their skeptic and are not listed; each was dropped without
reachability re-established, per §8. They clustered on the same seams as the confirmed set — the
sidecar grammar, the lease, the tick's decision table — which is consistent with a fan primed well on
where the risk sits and less well on what the code there already handles. Round 2 should feed the
confirmed set above as `priorFindings` and prime on the fold.

## The bug-class brief over this range

`python tools/memory-tree/gotchas.py --for-diff 5f9648d6..HEAD` selected 47 classes. Five are named
above against a confirmed finding: `inputs-inside-the-subjects-reach` (1),
`destructive-step-before-its-precondition` (2), `amendment-leaves-its-other-half-standing` (5),
`two-answers-to-one-question` (7/11) and `staged-break-substitutes-a-synthetic-value` (16). Two
confirmed findings (3, 15) fit no selected class and are proposed as new entries above. The remaining
classes were on the lenses' brief and drew no confirmed finding; that is the fan's result and not a
certificate that the class is absent from the diff.

## What the synthesis re-read, and what it did not run

Re-read at the tip, line by line, for every claim above: `tools/unattended/resume-tick.sh` in full;
`tools/unattended/unattended.sh` at 345-380, 1429, 1648, 2322-2340, 2395-2440, 2971-2989 and
3244-3399; `tools/unattended/lib-unattended.sh` at 88-104; `tools/unattended/stop-guard.js` at
130-143 and 205-230; `tools/unattended/run-lease.js` at 159-174; `memory/guides/UNATTENDED-PROTOCOL.md`
at 530-536; the grep for `FINISHED-UNSTAMPED` over `resume-tick.test.sh` (0 hits). Run: the gotchas
brief only. NOT run: any suite, leg or bar; no break was staged and no RED was observed, so every
left-shift arm above is a design and not an observation, and the first thing each fix owes is its
RED.

## Disposition

BLOCKED on id 1. The build closes when: id 1's guard lands with its RED observed; id 2's lease facts
and image match land with theirs; ids 3, 5, 7/11 and 15 land or are parked by id with a reason in the
run-state file; id 16 lands or is parked. Round 2 reads the fold from this round's recorded tip and
carries the seven confirmed defects as `priorFindings`.
