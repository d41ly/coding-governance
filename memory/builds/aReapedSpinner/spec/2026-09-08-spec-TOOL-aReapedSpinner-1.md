# TOOL-aReapedSpinner-1 — the census: one bounded read of the process table, or a refusal

**Status:** OPEN · rev-1 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-1-backend-and-kill-measurements.md](../build/2026-09-08-build-TOOL-aReapedSpinner-1-backend-and-kill-measurements.md) | research | — |
| [2026-09-08-prompt-TOOL-aReapedSpinner-1.md](../prompts/2026-09-08-prompt-TOOL-aReapedSpinner-1.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Give every later unit ONE normalized view of the live process table — id, parent, age, CPU,
command — read once, bounded, from a backend selected by platform. Nothing in this repo can list
processes today, so every unit downstream is blocked on this one.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/census.py`, exposing `scan_processes()` returning a list of rows
  with the fixed field set `pid · ppid · age_s · cpu_s · command · backend`. Observed by AC1.
- **S2** — the WINDOWS backend, which is a JOIN and not a single read: MSYS `ps -W` supplies
  `pid`, `ppid` and `winpid`, and `Get-CimInstance Win32_Process` keyed on `winpid` supplies
  `cpu_s` and the precise creation time. The measurements forcing the join are in this build's
  research record. Observed by AC2.
- **S3** — the POSIX backend, one `ps -eo pid,ppid,etimes,times,args` read. Observed by AC3.
- **S4** — backend SELECTION with a refusal: a platform whose backend does not answer raises and
  the CLI exits non-zero naming the backend it tried. It never returns an empty list. Observed by
  AC4.
- **S5** — `python tools/process-monitor/census.py --print` renders the rows as TSV for a human and
  for the units downstream. Observed by AC5.
- **S6** — every subprocess this module runs carries a wall-clock bound, so the observer cannot
  become the thing it observes. Observed by AC6.

## 3. Non-goals (OUT)

- **No classification, no scoping, no killing.** This unit reports what is running and decides
  nothing. Units 2, 3 and 4 own those.
- **No second sample and no sleep.** The build's research record rejects the two-sample progress
  probe; a census that waits is a census that hangs.
- **No caching.** A stale process table is worse than a slow one, and the read is ~1.2 s.
- **No `psutil` or any other new dependency** — M3 veto 2, and every kit here is stdlib-only.

### Edges

- **hands-off** `TOOL-aReapedSpinner-2` — the row shape S1 fixes is what the scope fence filters;
  the fence reads `command` and `pid` and adds no field of its own.
- **hands-off** `TOOL-aReapedSpinner-3` — `age_s` and `cpu_s` are the two fields the classifier
  decides on; without them it has no predicate.
- **hands-off** `TOOL-aReapedSpinner-4` — the `ppid` edges are what the reaper walks. The research
  record measures that the WINDOWS parent graph is a different graph, so the reaper is correct only
  if S2 supplies the MSYS edges rather than CIM's.
- **consumes-from** `TOOL-aReapedSpinner-6` — the kit directory and the descriptor rule that
  CLAIMS this file, without which `govkit selfcheck` reds the moment it becomes tracked.
- **consumes-from** external — a `python3` resolved by `tools/lib/resolve-python.sh`, which RUNS
  each candidate because the MS-Store stub answers `command -v` and exits 9009.

## 4. Design

### Data model

One row per process, a plain dict, field set fixed by S1:

```
pid       int    the id the REAPER can kill, in the backend's own namespace
ppid      int    the parent in THAT SAME namespace — never a mixed graph
age_s     float  now minus creation time
cpu_s     float  kernel + user, seconds
command   str    the fullest command string the backend gives
backend   str    'windows-join' | 'posix-ps' — carried per row so a report can name it
```

`ppid` and `pid` are in ONE namespace per row. Mixing MSYS ids with Windows ids is the defect that
made `taskkill /T` reap one process of four; the field contract is what forbids it.

### Windows: the join

`ps -W` gives `PID PPID PGID WINPID TTY UID STIME COMMAND`. `STIME` is a clock for today and a
`Mon DD` for anything older, so it is NOT used for age — CIM's `CreationDate` is, joined on
`WINPID`. A row whose winpid does not resolve in CIM keeps its MSYS identity and reports
`cpu_s = None`, which the classifier must treat as "unknown", never as zero.

`PGID` is read and DISCARDED. Measured: three descendants of a disposable test tree shared the
Bash-tool shell's own pgid, so a group kill reaps the caller. It is recorded in §4 rather than
dropped silently so the next author does not rediscover it.

### Alternatives rejected

`Get-Process` and `tasklist` (no command line, no usable parent — cannot attribute or walk),
`wmic` (deprecated, absent from recent images), `psutil` (M3 veto 2). Measurements and row counts
are in the research record; they are not restated here.

### Files touched (estimate)

`tools/process-monitor/census.py` new. Nothing else — this unit ships no conf, no gate and no
wiring, which is what makes it independently reviewable.

## 5. Production-readiness checklist

- security — the module RUNS `ps` and `powershell` with a fixed argv and no shell interpolation; a
  command string from the table is DATA and never re-executed.
- perf / scale — measured 1039 ms CIM + 128 ms `ps -W` on node `a`; the 320 ms PowerShell start is
  a floor no backend choice removes, and is why unit 5 throttles rather than reading per tool call.
- error / empty / loading states — an unanswerable backend is a REFUSAL (S4). An empty scoped
  result is a legitimate answer and is unit 2's to report, not this unit's to invent.
- observability — every row carries `backend`, so a report can always name what read it.
- risks — the join is the risk: a winpid that does not resolve leaves `cpu_s` unknown. Handled by
  making unknown a third value rather than folding it to zero.
- testing — a self-test with a captured fixture of each backend's raw output, so parsing is graded
  without a live process table; plus one live arm asserting the reader returns more rows than the
  one process running it.
- migration — none; new module.
- user docs — the kit README, unit 6.

## 6. Acceptance criteria

*Witnesses name kit files by BASENAME, which is this corpus's house style for a kit file and what
keeps `check-spec-tokens.py`'s path join off a file this unit has not built yet. The full paths are
in §2 and §4, which that join does not read.*

- **AC1** — When `scan_processes()` is called on this node, every returned row carries all six
  fields of S1 and no row carries a `None` `pid` or `ppid`. Observed by `selftest.py`, arm
  `test_row_contract_is_complete`.
  Red when: a backend adds or drops a field and the row contract silently changes shape.
- **AC2** — When the Windows backend runs, at least one row has a `cpu_s` derived from CIM AND a
  `ppid` equal to what `ps -ef` reports for the same process. Observed by `selftest.py`, arm
  `test_windows_join_keeps_msys_edges`.
  Red when: the join takes CIM's `ParentProcessId`, which this build's research record measures as
  a different graph, and the reaper then walks edges that do not exist.
  `fixture:` needs a live MSYS `ps` and PowerShell; off Windows the arm SKIPS with a named reason
  and the skip is printed, never silent.
- **AC3** — When the POSIX backend parses a captured `ps -eo` fixture, it produces rows whose
  `age_s` and `cpu_s` equal the fixture's `etimes` and `times` values. Observed by `selftest.py`,
  arm `test_posix_fixture_parses`.
  Red when: the column order the parser assumes differs from the one `-eo` emits.
  `fixture:` a captured text fixture, because MSYS `ps` rejects `-o` entirely — this node can never
  exercise the live POSIX path, and the arm says so rather than implying coverage.
- **AC4** — When the backend is forced to a name that does not exist (`PROCMON_BACKEND=nonesuch`),
  `census.py --print` exits non-zero and its stderr names the backends it tried. It does not print
  an empty table and exit 0. Observed by `selftest.py`, arm `test_no_backend_refuses`.
  Red when: a failed read returns `[]`, and every unit downstream then reports a clean tree.
- **AC5** — When `census.py --print` runs on this node, its stdout carries a header line and at
  least two data rows, one of which is the reading process itself. Observed by `selftest.py`, arm
  `test_live_read_sees_itself`.
  Red when: the renderer emits a column the field contract does not declare, or the live arm passes
  against an empty table.
- **AC6** — When a backend command is made to hang, `scan_processes()` returns within the declared
  bound and reports that backend as unanswered. Observed by `selftest.py`, arm
  `test_hung_backend_is_bounded`, which stages the hang with a shim earlier on `PATH`.
  Red when: the bound is applied through a pipe or a command substitution, which bounds the verdict
  and not the clock — the `bounded-through-a-pipe-is-unbounded` class, selected for these paths.

## 7. Gates

`line length` · `lexicon naming predicates` · `dead-path carriers (deleted files still named)` · `kit version markers`

New arm: `tools/process-monitor/selftest.py` · stages a nonexistent backend, a captured fixture per
platform, and a hanging backend shim · no assertion floor yet, this suite is new.

## 8. Open questions

- **F1 — should `cpu_s` be unknown or zero when the CIM join misses?**
  RESOLVED (agent, 2026-09-08, delegated): UNKNOWN, carried as `None`. Folding it to zero makes an
  unjoined row read as perfectly idle, which is the exact input the classifier uses to label
  `IDLE` — a read failure would manufacture a kill candidate. The vetoes are clear: no acceptance
  criterion or non-goal is broken, no new dependency, and no surface widens.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.

## 10. Reuse audit

No existing seam fits. `python tools/codebase-map/reuse_lookup.py "kill a hung or idle background
process and report it to the session"` returned only name-collisions on the stem `report`
(`tools/drift-audit/selftest.py:report`, `tools/govkit/govkit.py:Report`) and no process-table
reader anywhere in the corpus. The nearest prior art is `tools/run-gates/run-gates.sh:412-414`,
which is a statement of this problem rather than a seam: it records that the runner holds no
process group it can safely kill, and it reads no process table at all. Verified against source at
BASE, not quoted from the recall hit.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
