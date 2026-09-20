# TOOL-aWokenSentinel-12 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-12

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite, per the build README's rule three. The pass verified with the direct checks the spec's
section 6 names: the new `U12` arm block of `tools/unattended/resume-tick.test.sh` run ALONE over
the suite's sourced prologue, from a runner assembled under the session scratchpad with `HERE`
pointed at the kit under test and then at a copy carrying the one staged break, the `git init`
fixture under `%TEMP%/rt12`; the three greps of AC2 and AC3 as written; `gotchas.py` in its four
modes for AC4; and `check-install-prefix.sh`, `lexicon.py --check` and `check-spec-tokens.py` each
run ONCE as the checker, never as the bar. Those stand in for the `memory hygiene`, `spec tokens`,
`lexicon naming predicates`, `install-prefix (shipped surface)` and `unattended kit gate` legs,
which run once at the close.

**Evidences:** TOOL-aWokenSentinel-12
- AC1 — the U12 block alone over the fixture with `sleep 300 &` recorded as `pid:` and `STUB_LOGGED_IN=false` printed `pass=6 fail=0`: `rc=0`, the line `resume-tick: tRun · <fixture> · SKIP — the CLI is not logged in on this node; nothing can resume tRun`, `tasklist //FI "PID eq <winpid>"` still listing `sleep.exe`, `argv auth status` logged once and `argv -p` zero times, `resume.tRun.log` absent. RED first against a tick copy with the login call and the kill call swapped (`swap.py` moved the `run_kill_tree` line above the `check_login` block, lines 210/211 in the copy): `pass=5 fail=1`, the one red row `U12 the sleep is still listed by tasklist: expected [1], got [0]` with every message-shaped row still green — the swapped order kills and then announces the skip, which is the class. The refactored AC4 block alone still printed `pass=4 fail=0`. OBSERVED; the suite whole is observed at --close.
- AC2 — `grep -c 'logged-out node kills nothing'` printed `2` over `memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-5.md`, `1` over `tools/unattended/resume-tick.sh` at the tip and `0` over `git show HEAD:tools/unattended/resume-tick.sh` at the base `294534aa` — the base header wrapped the sentence across two comment lines (`a logged-out` / `node kills nothing`), so this unit's edit is the reflow that puts it on one line, and nothing else in the header moved. OBSERVED.
- AC3 — `grep -n 'check_login\|run_kill_tree' tools/unattended/resume-tick.sh` lists the two call sites in the `STALE` branch at `210:  if ! check_login "$sidecar/resume.$slug.$stamp.auth"; then` and `213:  [ "$RL_ALIVE" = yes ] && run_kill_tree "$RL_PID"`; 210 < 213. Unit 5's pass built spec 5's rev-2 order, so this unit's diff to the branch is nothing and the arm of AC1 is the proof. OBSERVED.
- AC4 — `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` (a range touching `resume-tick.sh`) printed `- [ ] destructive-step-before-its-precondition` under `8 class(es) selected by an anchor`; `--for-paths tools/unattended/resume-tick.sh` printed the same; `--report` printed `unanchored : 0` and the record's row `class 4 anchor(s) destructive-step-before-its-precondition`; `--write` wrote `memory/gotchas/INDEX.md (72 record(s))` and `--check` exited 0 afterwards, which is check 17 and check 18 together; the front matter parsed under the folder's grammar on every one of those runs. OBSERVED; the `memory hygiene` leg is observed at --close.
- S3 — `grep -n 'A logged-out node kills nothing'` over spec 5 lists its section 5 risk row at line 391 already reading `A logged-out node kills nothing: the login row precedes the kill row`, written at spec 5's rev-2 by the round-1 disposal; this pass changed nothing there. OBSERVED.
- checkers — `bash tools/check-install-prefix.sh` printed `install-prefix: clean — 276 shipped files, 11 declared waiver(s), 25 marked fixture line(s), no undeclared root-install spelling` and `carried-prefix clean — 139 recorded file(s), 41 hand-justified, none rising`; `python tools/lexicon/lexicon.py --check` printed `lexicon OK — 2157 tracked file(s)` with `derive_winpid` graded and no new offender; `python tools/check-spec-tokens.py` over this spec exited 0. OBSERVED; the legs are observed at --close.
