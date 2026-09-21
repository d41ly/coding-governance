# Fold brief — the closing diff review's round 2, folded into units 2, 5, 6 and 12

**Serves:** journal TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-12

The pass this brief was handed to FOLDS the seven defects of
`memory/builds/aWokenSentinel/reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md`
(round 2 over `e35dd54f..e232cd41`, CLEAN WITH FIXES, 0 blockers, CONVERGED — the loop is done; every
defect at this exit is a FOLD, recorded as such by `--review`). Read that record's "Findings" section
whole first: each defect carries file and line at the tip, the defect, the FIX and the LEFT-SHIFT arm.
This brief adds ownership and order; where it and the record disagree, the record wins. This is the
LAST fold: CONVERGED is terminal for the subject and no further review round runs, so the arms here
are the only reader of what you write — observe each RED first, or it proves nothing.

## What the pass does, in this order

1. **Defect B, HIGH — the kill target and the verdict are the working copy's** (`resume-tick.sh`
   `scan_worktrees`). One spawn before `run_tick`: `git -C "$wt" diff --quiet -- "$f"`; on a
   difference print `skip · RUN.md differs from the index, and the tick acts only on the lease the
   index holds`, no launcher, no attempt line. Retarget AC14's third arm to a tracked record with a
   rewritten working copy → the skip; add the kill arm the record describes (staged `pid: 999999999`,
   working copy rewritten to the suite's own sleep WINPID with `pid-image: absent` → the sleep
   survives and the skip prints). RED first. Owner: unit 5; the tick header, `README.md` and the
   protocol sentence that claim the working copy decides nothing now become TRUE — leave them.
2. **Defect A, HIGH — the launched pid is killed by number** (`resume-tick.sh` `run_detached` /
   `run_tick`). Record the image at launch beside the pid (`read_pid_image "$RD_PID"`, `absent` when
   underivable; image LAST on the attempt line since an image may carry spaces), and pass it to both
   `check_pid_alive` calls (the IN-FLIGHT probe and the hung kill). Arm beside AC13's hung half: a
   seeded `launched <sleep WINPID> claude.exe` line older than the last move → the sleep survives AND
   attempt 2 launches; the same seed newer than the last move must NOT read IN-FLIGHT. RED first.
   Owner: unit 5.
3. **Defect D, MEDIUM — the in-flight skip is unbounded** (`resume-tick.sh`, `unattended.sh`
   `print_liveness`). `--liveness` prints `stale-bound: <seconds>` (the driver owns
   `RESUME_STALE_BOUND`); `read_liveness` captures it; a launched line older than `now - stale-bound`
   is HUNG even with `RT_SINCE>0` and takes the existing kill row. Two arms: inside the bound with a
   live sleep → the skip; older than the bound → attempt 2 launches and the sleep is gone. RED first.
   Owners: unit 5 and unit 2 (the new line, its VERBS entry sentence, its arm in `unattended.test.sh`
   asserting the fourteenth line prints the declared value).
4. **Defect C, LOW — the launch pid is a digit sieve** (`resume-tick.sh` `run_detached`). Accept only
   a whole-line integer (`grep -m1 -xE '[0-9]+'` over the CR-stripped pid file); on an empty result
   print `launch failed: <first line>` instead of `resumed`; the attempt line carries no `launched`
   token and still counts toward the cap. Arm: make `Start-Process` fail (stub `cygpath`, or point
   the bash path at nothing) → no `launched` token, `launch failed` printed. RED first. Owner: unit 5.
5. **Defect E, LOW — a same-image recycle still matches** (`lib-unattended.sh` `check_pid_alive`,
   protocol §2 fact, unit 12's gotcha). Take the record's SECOND option: close it — `write_lease`
   records `pid-start:` (the process start time, `tasklist`/`wmic`/PowerShell `Get-Process`
   `StartTime` under MSYS, `ps -o lstart=` elsewhere, `absent` when underivable), and
   `check_pid_alive` answers `no` for a process whose start time is later than `lease-utc`. If the
   start time cannot be read on this node in under an hour of trying, take the FIRST option instead:
   state the residual identically in the lib header, protocol §2 and the gotcha, and say in `summary`
   which you took. If closed: an arm leasing the suite's sleep under a `lease-utc` older than the
   sleep's start → `pid-alive: no`. RED first. Owners: unit 12 (the mechanism and the gotcha), unit 2
   (`check_pid_alive`), unit 6 (the protocol fact and its render).
6. **Defect F, LOW — three carriers still say STALE alone** (`PROTOCOL.template.md` §5,
   `README.md`, `SKILL.template.md`). State the acting set once in the protocol §5 sentence
   (`STALE`, or `FINISHED-UNSTAMPED` with `stale: yes`), point the README and the Skill at it,
   re-render both. Owner: unit 6.
7. **Defect G, LOW — a duplicate empty heading** in
   `memory/gotchas/destructive-step-before-its-precondition.md`. Delete it. Owner: unit 12.

Every touched spec (2, 5, 6, 12) takes a `rev-N` bump with its §9 line naming the round-2 record and
the defect letter; every touched template re-renders in the same commit; the protocol render stays
under the 61440 B guide cap (trade bytes inside §5 if it does not fit, never a curation-debt row);
the acceptance ledgers of units 2, 5, 6 and 12 each gain one `- AMENDED —` row per criterion the fold
changed. ONE commit, subject `build(TOOL-aWokenSentinel-5): fold the closing review's round 2 — …`
naming every folded defect letter and unit. The M6 checklist runs after the commit and is acted on.

## What binds every pass of this build (read before the record)

- **NO merge bar, NO gate leg, NO `*.test.sh` suite, NO spec section-7 gate list runs inside this
  pass.** Observe each arm by running its block ALONE from the suite's sourced prologue, the way the
  round-1 fold did (its ledger rows name the runner shape).
- **Every shell call carries the Bash tool's `timeout` parameter**: 120000 ms by default, at most
  600000 ms for the git commit or a build command the change itself needs. PRIMARY OBJECTIVE: code
  written and committed.
- **Every temporary file goes under the session scratchpad, spelled absolute:**
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-eloquent-pasteur-e7ecb5/2db85696-ae7f-456a-9d88-fffc3fe3482a/scratchpad`.
  Never `$TMPDIR`, `/tmp`, `$TEMP` or a bare `mktemp`. A fixture git repo goes under
  `%TEMP%/<short-name>`.
- **Regrounding (M7):** `git log --oneline -5`, `memory/builds/aWokenSentinel/RUN.md`,
  `memory/guides/BUILD-METHOD.md` whole, the round-2 record whole, and each owning spec's §4 and §6.
- **Declare, then build.** `bash tools/unattended/unattended.sh --dispatch aWokenSentinel --pass
  TOOL-aWokenSentinel-5 --writes <path>` once per path BEFORE writing; never `memory/DECISIONS.md`,
  `memory/backlog/*`, `memory/project/readme-contract.txt`, `memory/builds/aWokenSentinel/RUN.md`,
  `memory/LIVE.md` or `memory/ledger/*`. Then `--brief aWokenSentinel --unit TOOL-aWokenSentinel-5
  --path <this file>`.
- **A kit file names nothing outside itself by literal.** New `fail <n>` branches need an ARM and
  `check-arms.py --report` lists it ARMED. No kit version bump. Commit with
  `gen_build_index.py --write` after `git add -A memory`, let the hook run, then
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on it. Return
  `committed:false` with a `why` rather than a commit you cannot stand behind.
