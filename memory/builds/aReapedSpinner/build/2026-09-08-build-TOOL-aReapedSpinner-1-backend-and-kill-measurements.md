# Research (build record) — how you enumerate, attribute and kill an agent-launched process tree

**Serves:** research TOOL-aReapedSpinner-1

Node `a`, 2026-09-08, at BASE `e2b82a53`. Every figure below was measured on this node in this
session; nothing here is quoted from documentation.

## M5 — the reuse probes, and what they found

```
python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to the session"
python tools/memory-recall/query.py "why does the gate runner not kill its own child processes when a leg times out or the session stops it" \
  --terms "gate runner wall clock bound timeout kill children orphan process leg pool watchdog GATE_WALL background subprocess reaper"
```

**No existing seam fits, and the probes are what establish it rather than a glance at the tree.**
The map probe returned `report`-stemmed symbols and the `unattended` and `govkit` dossiers — name
collisions, no process-table reader anywhere in the corpus. The recall probe returned 40 hits, all
of them the SAME shape: `run-gates.sh`'s wall watchdog, `run-selftests.sh`'s pool, `unattended.sh`'s
`GATE_BOUND`. Every one bounds a command the checker itself launched and holds the pid for.

**The nearest prior art is `tools/run-gates/run-gates.sh:412-414`, and it is a statement of the
problem rather than a solution to it.** Its own header records that the runner sets no `set -m` and
has no `setsid`, so every leg sits in the RUNNER's process group and a group kill would take the
runner down with it. It therefore kills recorded pids one at a time (`:451`) and reports survivors
(`:468`). What it cannot do is reach a grandchild, and §"the kill test" below measures that gap
rather than inferring it from the comment.

**Stale-hit check.** `TOOL-aPooledSweep-1`'s closing review moved a watchdog kill onto the `timeout`
child. Verified against source: that is real and it is scoped to `run-selftests.sh`'s own suites. It
does not generalize and it does not reach an agent-launched process, which is three of the four
failures the prompt reports.

## Candidate set 1 — the process-table backend

Enumeration must yield, per process: an id that can be killed, a PARENT id in the same namespace,
an age, a CPU total, and a command string long enough to attribute scope. A backend missing any one
of those cannot serve.

| Candidate | Measured | Verdict |
|---|---|---|
| `Get-CimInstance Win32_Process` | 1039 ms, 333 rows | **WINS one half.** The only backend giving CPU time and full command line together. |
| MSYS `ps -W` | 128 ms, 327 rows | **WINS the other half.** The only backend giving MSYS parent edges, and it carries the `WINPID` join key. |
| `Get-Process` | 782 ms, 337 rows | LOST — no command line and no usable parent without a second query, so it can neither attribute scope nor walk a tree. Rejected on capability, not on cost. |
| `tasklist /NH /FO CSV` | 670 ms, 328 rows | LOST — same capability gap, and no parent id at all. |
| `wmic process` | present on this node | LOST on durability: deprecated and absent from recent Windows images, so a kit shipping it would fail silently in an adopter rather than loudly here. |
| `psutil` | not installed | LOST to M3 veto 2 — a new external dependency. Not a close call; every other kit here is stdlib-only. |

**`powershell -NoProfile -Command 1` costs 320 ms**, so the CIM figure is ~700 ms of query over a
fixed 320 ms floor. That floor is why the report path is throttled rather than run per tool call.

**The two winners are BOTH required and the reason is measured, not aesthetic** — see below. The
POSIX backend is `ps -eo pid,ppid,etimes,times,args`, one read giving every field. **It is
UNEXERCISED on this node**: MSYS `ps` rejects `-o` entirely (`ps: unknown option -- o`), so no arm
of this session took that path. The kit must therefore SELECT a backend and REFUSE when none
answers, never fall through to an empty table — a census that reports zero processes because its
reader failed is the exact green-by-absence class this build's README forbids.

## The kill test — three arms, staged against a disposable 3-deep tree

A tree was built in the scratchpad: `tree.sh` → a child `bash -c` → two grandchild `sleep 900`, plus
one direct child sleep. Four sleeps, three levels.

- **Arm A — `kill -9 <top pid>`, which is the `run-gates.sh:451` and `TaskStop` shape.**
  Result: **all four sleeps still alive.** The defect the prompt reports, reproduced in one command.
- **Arm B — `taskkill /PID <winpid> /T /F`, Windows' own tree kill.**
  Result: `SUCCESS`, and **one process died of four.** The survivors still named the just-killed
  process as their MSYS parent. **`/T` walked the WINDOWS tree, which is a different graph**: CIM
  reports the three survivors' parents as 22444, 26264 and 22644 — three unrelated fork-emulation
  stubs — while MSYS reports one shared parent. A success message over a 25%-effective kill is worse
  than a failure, and this is the single most important measurement in this build.
- **Arm C — walk the MSYS parent edges, kill leaves first, verify.**
  Result: **5 killed, 0 survivors.** This is the mechanism.

**One process reparented to `ppid=1` mid-test**, in front of the probe. A tree walk from a root
cannot find a process that has already been orphaned, so the orphan class must be caught by the
classifier over the whole table and never by the reaper's walk. Both mechanisms are needed and
neither substitutes for the other.

**PGID is not the kill unit, and this is a recorded loss.** All three survivors shared
`PGID 2507196` — the Bash-tool shell that launched them, not the job. Killing that group reaps the
caller. This is `run-gates.sh:412-414`'s hazard measured from the other side, and it closes the one
design that would have made the reaper a one-liner.

## Candidate set 2 — the non-progress predicate

- **Two-sample progress probe** (CPU delta and output mtime across a sleep). LOST. It costs a second
  full census plus the sample window on every report, and it discriminates nothing the cheap
  predicate misses: every failure in the prompt was hours past any defensible ceiling. Buying a
  hang-detector for processes still INSIDE their ceiling is speculative, and it would put a timed
  wait inside the observer, which the build rules forbid.
- **Single-sample `cpu_seconds / age_seconds` plus a declared age ceiling.** WINS.
  **Age DECIDES, rate LABELS.** A row past its ceiling is dead weight whatever the rate; the rate
  then says whether it is `SPIN` (burning) or `IDLE` (hung). Against the prompt's own numbers the
  two spin loops read 46221 CPU-s over 41040 s of age, a rate of 1.13 across the pair — unambiguous
  at a single sample, with no second read and no sleep.

## What this settles for the specs

1. The Windows census is a JOIN: `ps -W` for identity and parent edges, CIM keyed on `WINPID` for
   CPU and precise start. POSIX is one `ps -eo` read. An unrecognised platform REFUSES.
2. The reaper walks MSYS parent edges leaves-first and verifies each death. It does not use
   `taskkill /T`, and it does not use process groups.
3. The classifier decides on age against a declared ceiling and labels with the CPU rate.
4. The orphan class is found over the whole table, never by walking down from a root.
