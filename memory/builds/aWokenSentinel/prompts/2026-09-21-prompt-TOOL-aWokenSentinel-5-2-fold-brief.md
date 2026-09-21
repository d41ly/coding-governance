# Fold brief — the closing diff review's round 1, folded into units 1, 2, 5, 7 and 12

**Serves:** journal TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-12

The pass this brief was handed to FOLDS the eight confirmed findings of
`memory/builds/aWokenSentinel/reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md`
(round 1 over `5f9648d6..e35dd54f`, verdict BLOCKED) into the code and the specs that own it. Read that
record's "Findings, severity-ranked" section whole first: every finding there carries the file and
line at the tip, the defect, the impact, the FIX and the LEFT-SHIFT arm. This brief adds only the
ownership and the order; where it and the record disagree, the record wins.

## What the pass does, in this order

1. **id 1, BLOCKER — the tick honours an untracked lease** (`tools/unattended/resume-tick.sh`).
   Before acting on a record, require it in the index (`git -C "$wt" ls-files --error-unmatch`) and
   read the `session:` fact from the index blob (`git -C "$wt" show ":<path>"`), never from the
   working copy. An untracked hit prints `skip · RUN.md is not tracked` and launches nothing. Arm in
   `tools/unattended/resume-tick.test.sh`: untracked live-session record older than the bound → the
   skip line, no attempt line, no launcher; `git add` it → the same tick launches. RED first with the
   guard removed. Owner: unit 5 (rev bump, §9 line, §4 sentence, §3 names the file-write attacker as
   closed and the staging attacker as section 9's concession).
2. **id 2, HIGH — the tree kill is aimed at a pid, not the leased process** (`tools/unattended/
   unattended.sh` `write_lease`, `check_pid_alive`; `resume-tick.sh` `run_tick`). `write_lease` also
   records `host:` (`COMPUTERNAME`, else `hostname`) and `pid-image:` (the image column of the
   `tasklist` row under MSYS, `ps -o comm=` elsewhere) beside `pid:`; `check_pid_alive` matches pid
   AND image and prints `no` on a mismatch; `run_tick` refuses to kill or launch when `host:` names
   another node and prints why. Arms: `unattended.test.sh` leases the suite's own `sleep` pid under a
   recorded image of `claude.exe` and asserts `pid-alive: no`; `resume-tick.test.sh` with a foreign
   `host:` asserts no kill and the printed refusal. RED first. Owners: unit 1 (the two new facts,
   rev bump, and the protocol section 2 fact list with its render), unit 2 (`check_pid_alive`), unit 12
   (the kill's precondition — its gotcha record gains the reboot case).
3. **id 3, MEDIUM — the launched pid is never recorded** (`resume-tick.sh`). Capture the launched pid
   (`Start-Process -PassThru`, `.Id`; `$!` on the POSIX arm) into the attempt line the tick writes and
   parses as `launched <pid>`; on the next STALE tick, a live launched pid is IN-FLIGHT: print the skip,
   launch nothing. Arm: after a launch the newest attempt line carries `launched <pid>`; a second STALE
   tick with that pid alive prints the in-flight skip and launches nothing. RED first. Owner: unit 5.
   Left-shift the class as `memory/gotchas/guard-fed-the-value-it-supersedes.md` (or the nearest
   spelling `gotchas.py --suggest`-style naming allows): a guard fed only the value the act it guards
   was meant to replace. Kind `class`, `Gated by` the arm, anchors derived.
4. **id 5, MEDIUM — FINISHED-UNSTAMPED outranks STALE** (`resume-tick.sh` `read_liveness`, `run_tick`).
   Capture `stale:`; act when the verdict is STALE, or FINISHED-UNSTAMPED with `stale: yes`. Arm:
   fixture at LANDING with its witness merged into `refs/remotes/origin/main`, `session:` set, HEAD
   older than the bound → an attempt line and a launcher. RED first. Owner: unit 5; unit 8's spec §3
   non-goal gains one sentence pointing here for the dead half.
5. **ids 7 and 11, MEDIUM — fail 54 misdiagnoses an unbound session** (`unattended.sh` `verb_landed`).
   Before the sidecar read, compare `${CLAUDE_CODE_SESSION_ID:-}` with `fact "$rel" session`; on a
   mismatch or an absent fact refuse (a new `fail <n>`, next free above the derived high-water)
   naming the mismatch and `--resume <slug> --keepalive-id <id>` as the step that lets the stop-guard
   record this session; keep the existing fail 54 text for the bound case, and correct the header
   sentence that claims an unbound session is never wedged. Arm: pre-close stop line present,
   `CLAUDE_CODE_SESSION_ID` set to a value the record does not hold → the re-lease remedy printed, END
   THE TURN not printed. RED first. Owner: unit 7.
6. **id 15, MEDIUM — the newest stop line is graded whoever wrote it** (`unattended.sh` `write_lease`,
   `read_stop_listing`/`verb_landed`). `write_lease` records `lease-utc:` (UTC, the driver's own
   spelling) beside the lease; `--landed` treats a newest stop line whose `utc` is older than
   `lease-utc` as pre-close (the fail 54 path), so only a listing the CURRENT incarnation produced can
   pass. Arm: seed a LANDING stop line, replace the lease, assert fail 54 refuses. RED first. Owners:
   unit 1 (the fact) and unit 7 (the compare; its NOT CHECKED list names the class it now checks).
   Left-shift the class as a `memory/gotchas/` record: a witness graded against a fact written after
   it, wherever a sidecar outlives a lease.
7. **id 16, LOW — the dead-probe diagnostic names a NOTE** (`resume-tick.sh` `read_liveness`). Take
   `RL_FIRST` from `grep -m1 '^UNATTENDED check'` over the captured text, falling back to the first
   stdout line; give the AC12 stub a stderr NOTE before its refusal, so the arm is the stub change.
   Owner: unit 5.

Every arm is observed RED against a copy carrying the break BEFORE it is trusted green; every
touched spec takes a `rev-N` bump with its §9 line naming the review record and the finding id;
every touched template re-renders in the same commit (`adopt-unattended.sh`, then `--check`); the
protocol section 2 fact list moves with unit 1's new facts (and its render); new `fail` numbers are
derived from the tree; new facts are read through `fact`, never a second parser. ONE commit, subject
`build(TOOL-aWokenSentinel-5): fold the closing review's round 1 — …` naming every folded id;
the acceptance ledgers of units 1, 2, 5, 7 and 12 each gain one `- AMENDED —` row per criterion the
fold changed. The M6 checklist runs after the commit and is acted on.

## What binds every pass of this build (read before the record)

- **NO merge bar, NO gate leg, NO `*.test.sh` suite, NO spec section-7 gate list runs inside this
  pass.** Those are `--close`'s, once. Observe each arm by running its block ALONE from the suite's
  sourced prologue, the way units 5, 12, 13, 18 and 24 did (their ledgers name the runner shape).
- **Every shell call carries the Bash tool's `timeout` parameter**: 120000 ms by default, at most
  600000 ms for the git commit or a build command the change itself needs. A command unrelated to
  writing code that exceeds its bound is SKIPPED and named in your `summary`. PRIMARY OBJECTIVE:
  code written and committed.
- **Every temporary file goes under the session scratchpad, spelled absolute:**
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-eloquent-pasteur-e7ecb5/2db85696-ae7f-456a-9d88-fffc3fe3482a/scratchpad`.
  Never `$TMPDIR` (EMPTY on this node), never `/tmp`, never `$TEMP`, never a bare `mktemp`. A fixture
  git repo goes under `%TEMP%/<short-name>` because the scratchpad path breaks a clone on Windows.
- **Regrounding (M7):** read `git log --oneline -5`, `memory/builds/aWokenSentinel/RUN.md`,
  `memory/guides/BUILD-METHOD.md` whole, the review record whole, and each owning spec's §4 and §6.
- **Declare, then build.** `bash tools/unattended/unattended.sh --dispatch aWokenSentinel --pass
  TOOL-aWokenSentinel-5 --writes <path>` once per path BEFORE writing. Do NOT declare
  `memory/DECISIONS.md`, `memory/backlog/*`, `memory/project/readme-contract.txt`,
  `memory/builds/aWokenSentinel/RUN.md`, `memory/LIVE.md` or `memory/ledger/*` (the last two are
  refused by check 49 for this build; the index regen does not move them on a fold). Give a many-path
  dispatch 600000 ms. Then record this brief: `bash tools/unattended/unattended.sh --brief
  aWokenSentinel --unit TOOL-aWokenSentinel-5 --path <this file>`.
- **A kit file names nothing outside itself by literal.** The install-prefix gate grades every file
  under `tools/`; a new registry row is a last resort and is justified on its line.
- **New `fail <n>` branches need an ARM** asserting the literal text; `check-arms.py --report` must
  list it ARMED. The driver's high-water is derived, never copied from this brief.
- **No kit version bump** — the closing pass already moved unattended to 1.25; a fold inside the
  same landing does not move it again.
- **Commit** with `gen_build_index.py --write` after staging and `git add -A memory`, let the hook
  run, then `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names.
  Return `committed:false` with a `why` rather than a commit you cannot stand behind.
