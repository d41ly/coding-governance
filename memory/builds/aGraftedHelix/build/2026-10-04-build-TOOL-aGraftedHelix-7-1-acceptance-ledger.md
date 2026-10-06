# Acceptance ledger — TOOL-aGraftedHelix-7

**Serves:** journal TOOL-aGraftedHelix-7

Node `a`, 2026-10-05. The build commit is `1e372d653`, over the spec's rev-4 commit `b506bd335`;
`e6891f058` follows it with one more arm, for S5's third verdict writer, the suites' bars run with
the pause off, and the prose pointed at the figures' owners, and `8a89d2841` moves run-gates to 1.27
because govkit epoch read that follow-up as a move after the 1.26 bump. Two spec revisions preceded
the code: rev-3 (the runner as unit 5 left it at 1.25) and rev-4 (AC14 reaches the forced-progress
branch by construction, AC6's pressure lands as B ends). No merge bar and no self-test suite ran in
this pass. Every criterion below was observed through fixture repositories under a short `%TEMP%`
root, driving the working-tree runner, and then through slices of the suites assembled under
`tools/run-gates/` and `tools/lib/` under a name that is not `*.test.sh` (the gate-guard refused one
that was), deleted after each run. Each new arm was observed red against a staged break in the
working tree, restored from a scratchpad copy and compared with `cmp` after every run. The suites
whole are the main loop's at VERIFYING: the canary's floor rose 278 -> 309, the evidence suite's
110 -> 112, the run-log suite's 210 -> 211, and the self-test runner suite's 139 -> 141.

**Evidences:** TOOL-aGraftedHelix-7
- AC1 — `GATE_MEMPAUSE=x` — over a row `width=2,timeout=0,wall=0,mempause=80`, --print-profile printed `mempause 80` and a line carrying `mempause 80%;`; with `GATE_MEMPAUSE=0` the line read `mempause off;`; a row at 101 exited 2 naming `knob 'mempause'`; `x` printed one NOTE and `mempause off`. Canary section 11a, seven assertions, green in the slice.
- AC2 — `mempause=90` — `grep -c` over the shipped table printed 3, the table's row count, and `PINNED_KNOBS` reads `mempause timeout wall width` at line 1225 of the canary at `1e372d653`.
- AC3 — `PARITY_ROWS` — `git grep -l` named run-gates.sh and run-selftests.sh, both blocks cksum `2786339598 6429`, and the row `mempause_sh|$ROOT/$RUNGATES_DIR/run-gates.sh|…` sits in the table; a slice of resolve-python.test.sh through its parity loop ran 227 green and, with `MEMPAUSE_HOLD=301` staged in the copy, named run-selftests.sh as drifted.
- AC4 — `read_mem_used` — sourced from the AC3 extraction: 85, 85, 85, nothing with rc 1 for no MemTotal, 95 beside a cgroup at 950/1000, 85 with memory.max reading max, and nothing for an absent file. Cost re-timed: 1000 calls over the fixture in 3661 ms and over /proc/meminfo in 2934 ms, about 3 ms a decision against the 0.69 ms the spec pinned for one bare read; the gap is the cgroup probes and MSYS's full meminfo walk, and it is still no spawn.
- AC5 — `memory: 1 pause(s)` — one `pauses` row ending fell, held 3 to 4 s, B's and C's `.leg` starts at or after A's end, verdict `paused 1`, one summary line; the pause-off control started B before A ended. Red with the hold call deleted, all six assertions.
- AC6 — `GATE_MEMPAUSE_HOLD=2` — the episodes read `bound drained`, five `GATE ok` lines, inside 60 s, exit 0 equal to the pause-off run's. Red with rule 4 deleted (`bound bound`) and with the bound compare reversed (`drained bound`). Before rev-4 the start-of-leg write read `drained drained drained` and `bound bound drained` in two runs of five.
- AC7 — `mempause INERT` — one NOTE naming the pause INERT, the profile line `mempause INERT;`, no `pauses` row, `memory: no reading on this host…`, header `mempause inert`. Red with the INERT branch reading 0.
- AC8 — `git grep -n "memory: " -- tools/run-gates/run-gates.test.sh tools/run-gates/run-gates.runlog.test.sh` — names arm 3a's filter beside its exactly-one presence check and the run-log AC5 filter beside its `1|1` check. A slice of arm 3a ran 4 green and redded with the summary line deleted; the run-log AC5 slice ran 15 green and redded `expected [1|1], got [0|0]` under the same break.
- AC9 — `--pooled --calibrate` — at 95 % the second suite started no earlier than the first ended and the sweep printed `memory: 1 pause(s)`, drained 1; at 10 % both started together under `memory: no pause`. The suite's two arms ran green in a slice and the 95 % arm redded with the sweep's call replaced by `while false`.
- AC10 — `1 paused` — `L 30.0 2 300 270 30 ok 1` and `# set aside: 0 contended, 1 paused, 0 uncensused`; with the overlap made non-strict L read 20.0 from 1 and 2 paused. Evidence suite slice, two assertions.
- AC11 — `bash tools/check-kit-versions.sh` — clean, 16 carriers, at `1e372d653` and at `8a89d2841`; `govkit.py epoch` reads `run-gates · clean · 1.27` at `8a89d2841`; manifest-check exits 0 with no check 5 line; the catalog's wall line, line 183 of the manifest, names mempause. Its kickoff-manifest row reads FAILED against a move at `5db6e3894`, an ancestor of this unit's base.
- AC12 — `unread` — one row ending unread, B and C dispatched at A's end. Red with rule 2 deleted (two rows, `drained drained`).
- AC13 — `paused_s` — a wall of 3 s over a 10 s leg: exit 1, one row ending wall, the verdict carrying paused and paused_s, one `memory:` line. Red with the wall close deleted (no row).
- AC14 — `check_dispatch_pause 0` — the block alone held with 2 running and then dispatched, writing one row ending drained; the FIFO fixture closed C's episode drained with exit 0, and with the forced branch's call deleted closed it wall. The rev-2 form, twenty runs at width 2, stayed green under that same break, which is why rev-4 replaced it.
