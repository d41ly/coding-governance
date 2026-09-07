# TOOL-aReapedSpinner-1 — the census: one bounded read of the process table, or a refusal

**Status:** OPEN · rev-2 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-1-backend-and-kill-measurements.md](../build/2026-09-08-build-TOOL-aReapedSpinner-1-backend-and-kill-measurements.md) | research | — |
| [2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md) | research | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 |
| [2026-09-08-prompt-TOOL-aReapedSpinner-1.md](../prompts/2026-09-08-prompt-TOOL-aReapedSpinner-1.md) | research | — |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Give every later unit ONE normalized view of the live process table — id, parent, age, CPU,
command — read once, bounded, from a backend selected by platform, with every row proven to be a
real process rather than a fragment of one. Nothing in this repo offers that today.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/census.py`, exposing `scan_processes()` returning rows with the
  fixed field set `pid · ppid · age_s · cpu_s · command · backend`. Observed by AC1.
- **S2** — the WINDOWS backend, a JOIN and not a single read: MSYS `ps -W` supplies `pid`, `ppid`
  and `winpid`; `Get-CimInstance Win32_Process` keyed on `winpid` supplies `cpu_s`, the precise
  creation time AND `command`. Observed by AC2, AC7.
- **S3** — the POSIX backend, one `ps -eo pid,ppid,etimes,times,args` read. Observed by AC3.
- **S4** — backend SELECTION with a refusal: a platform whose backend does not answer raises and
  the CLI exits non-zero naming the backend it tried. It never returns an empty list. Observed by
  AC4.
- **S5** — `census.py --print` renders the rows as TSV. Observed by AC5.
- **S6** — every subprocess this module runs carries a wall-clock bound, applied to the CHILD and
  never through a pipe. Observed by AC6.
- **S7** — the ROW GUARD: `pid` and `ppid` are accepted only as anchored all-digit tokens, and a
  row that is a continuation of a previous row's raw argv is REJECTED, not parsed. The count of
  rejected rows is reported. Observed by AC8.
- **S8** — byte-level decoding: backend stdout is read as BYTES and decoded with `errors="replace"`.
  Observed by AC9.
- **S9** — rows the backend could describe only partially — no `command`, or no CIM join — are
  carried with explicit `None` and COUNTED, and `--print` names both counts. Observed by AC10.

## 3. Non-goals (OUT)

- **No classification, no scoping, no killing.** This unit reports what is running and decides
  nothing. Units 2, 3 and 4 own those.
- **No second sample and no sleep.** The research record rejects the two-sample progress probe; a
  census that waits is a census that hangs.
- **No caching.** A stale process table is worse than a slow one, and the read is ~1.2 s.
- **No `psutil` or any other new dependency** — M3 veto 2, and every kit here is stdlib-only.
- **No version marker.** `KIT_PROCESS_MONITOR_VERSION` lives in unit 6's shell adopter. rev-1's
  unit 6 pointed `version_from` at this file, which is the defect D1 records; this unit mints
  nothing the descriptor reads.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-6` — the kit directory and the descriptor rule that CLAIMS
  this file, without which `govkit selfcheck` reds the moment it becomes tracked.
- **hands-off** `TOOL-aReapedSpinner-2` — the row shape S1 fixes is what the scope fence filters.
  S2 is load-bearing for it: the fence reads `command`, and `ps -W`'s own COMMAND column is the
  EXECUTABLE PATH with no arguments, so a fence fed from there matches nothing (measured: zero of
  315 rows).
- **hands-off** `TOOL-aReapedSpinner-3` — `age_s` and `cpu_s` are the fields the classifier decides
  and labels on; `None` is a real value for `cpu_s` and unit 3 handles it as `UNKNOWN`.
- **hands-off** `TOOL-aReapedSpinner-4` — the `ppid` edges are what the reaper walks, and S7 is why
  the reaper can trust that a walked id is a process rather than a word from somebody's argv.
- **consumes-from** external — a `python3` resolved by `tools/lib/resolve-python.sh`, which RUNS
  each candidate because the MS-Store stub answers `command -v` and exits 9009.

## 4. Design

### Data model

```
pid       int    the id the REAPER can kill, in the backend's own namespace
ppid      int    the parent in THAT SAME namespace — never a mixed graph
age_s     float  now minus creation time
cpu_s     float|None  kernel + user, seconds. None means UNJOINED, never zero.
command   str|None    the fullest command string the backend gives
backend   str    'windows-join' | 'posix-ps' — carried per row so a report can name it
```

`ppid` and `pid` are in ONE namespace per row. Mixing MSYS ids with Windows ids is the defect that
made `taskkill /T` reap one process of four.

### Windows: the join, and which side supplies what

`ps -W` gives `PID PPID PGID WINPID TTY UID STIME COMMAND`. Three of its columns are used and two
are deliberately not:

- `PID`, `PPID` — the MSYS namespace, which is the only one whose parent edges are real.
- `WINPID` — the join key.
- `STIME` is NOT used for age: it is a clock for today and a `Mon DD` for anything older.
- **`COMMAND` is NOT used for the command.** Measured: it prints `/usr/bin/sleep`, never
  `sleep 900`, so scoping on it matched zero of 315 rows in a tree full of agent processes. CIM's
  `CommandLine` carries the full string and is what `command` is taken from.

`PGID` is read and DISCARDED. Measured: three descendants of a disposable test tree shared the
Bash-tool shell's own pgid, so a group kill reaps the caller.

### The row guard (S7), inherited rather than rediscovered

`tools/run-gates/run-gates.sh:432-436` already records this hazard and already carries the guard:
cygwin `ps -ef` prints argv RAW, so a command line containing a newline splits one process across
rows "whose field 2 and 3 are attacker-or-accident-chosen text", and snapshots on this box "already
carry about ten such continuation rows from other sessions' multi-line `bash -c`". Its predicate is
`$2 ~ /^[0-9]+$/ && $3 ~ /^[0-9]+$/`, and without it "this walk feeds arbitrary text to `kill -9`".

This unit adopts that predicate and adds the COUNT, because a silent drop is the failure mode one
level up. A continuation row is a fragment of a REAL in-scope command line, so without S7 unit 2
admits it, unit 3 grades it, and unit 4 kills whatever integer the fragment spells.

### Decoding (S8)

PowerShell writes the CONSOLE codepage, not UTF-8. Measured: `subprocess.run(..., text=True)` died
with `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 66732` — and the failure
lands on a reader THREAD, after which `o.stdout` is `None` and the caller sees an `AttributeError`
far from the cause. Read bytes; decode with `errors="replace"`.

### Alternatives rejected

`Get-Process` and `tasklist` (no command line, no usable parent), `wmic` (deprecated, absent from
recent images), `psutil` (M3 veto 2). Row counts and timings are in the research record.

### Files touched (estimate)

`tools/process-monitor/census.py` and `tools/process-monitor/selftest.py`, both new.

## 5. Production-readiness checklist

- security — the module RUNS `ps` and `powershell` with a fixed argv and no shell interpolation; a
  command string from the table is DATA and never re-executed. S7 is the security-relevant half:
  without it, untrusted argv text reaches an integer field the reaper acts on.
- perf / scale — measured 1039 ms CIM + 128 ms `ps -W`; the 320 ms PowerShell start is a floor no
  backend choice removes, and is why unit 5 throttles.
- error / empty / loading states — an unanswerable backend REFUSES (S4). Partial rows are carried
  with `None` and counted (S9), never dropped.
- observability — every row carries `backend`; `--print` names the rejected-row and unjoined counts.
- risks — the join is the risk. Measured on this node: 199 of 314 CIM rows carry a `CommandLine` at
  all, so a third of the table is unattributable and that number must be visible, not swallowed.
- testing — captured fixtures per backend so parsing is graded without a live table, plus a
  multi-line `bash -c` fixture for S7, plus live arms.
- migration — none; new module.
- user docs — the kit README, unit 6.

## 6. Acceptance criteria

- **AC1** — When `scan_processes()` runs on this node, every row carries all six fields of S1 and
  no row carries a `None` `pid` or `ppid`. Observed by `selftest.py`, arm
  `test_row_contract_is_complete`.
  Red when: a backend adds or drops a field and the row contract silently changes shape.
- **AC2** — When the Windows backend runs, at least one row has a `cpu_s` AND a `command` taken
  from CIM AND a `ppid` equal to what `ps -ef` reports for the same process. Observed by
  `selftest.py`, arm `test_windows_join_keeps_msys_edges_and_cim_command`.
  Red when: the join takes CIM's `ParentProcessId` (a different graph), or takes `command` from
  `ps -W` (the executable path, which scoped zero of 315 rows).
  `fixture:` needs a live MSYS `ps` and PowerShell; off Windows the arm SKIPS with a named reason
  and the skip is printed, never silent.
- **AC3** — When the POSIX backend parses a captured `ps -eo` fixture, its rows' `age_s` and
  `cpu_s` equal the fixture's `etimes` and `times`. Observed by `selftest.py`, arm
  `test_posix_fixture_parses`.
  Red when: the column order the parser assumes differs from the one `-eo` emits.
  `fixture:` a captured text fixture, because MSYS `ps` rejects `-o` entirely — this node can never
  exercise the live POSIX path, and the arm says so rather than implying coverage.
- **AC4** — When the backend is forced to a name that does not exist (`PROCMON_BACKEND=nonesuch`),
  `census.py --print` exits non-zero naming the backends it tried, and prints no table. Observed by
  `selftest.py`, arm `test_no_backend_refuses`.
  Red when: a failed read returns `[]`, and every unit downstream reports a clean tree.
- **AC5** — When `census.py --print` runs on this node, its stdout carries a header and at least two
  data rows, one of which is the reading process itself. Observed by `selftest.py`, arm
  `test_live_read_sees_itself`.
  Red when: the renderer emits a column the contract does not declare, or the live arm passes
  against an empty table.
- **AC6** — When a backend command is made to hang, `scan_processes()` returns within the declared
  bound and reports that backend unanswered. Observed by `selftest.py`, arm
  `test_hung_backend_is_bounded`, staging the hang with a shim earlier on `PATH`.
  Red when: the bound is applied through a pipe or a command substitution, which bounds the verdict
  and not the clock — the `bounded-through-a-pipe-is-unbounded` class, selected for these paths.
- **AC7** — When a `ps -W` row's `winpid` resolves to no CIM row, the row survives with `cpu_s` and
  `command` as `None` and is counted as unjoined. Observed by `selftest.py`, arm
  `test_unjoined_row_survives_as_none`.
  Red when: the row is dropped, which shrinks the population silently, or `cpu_s` is set to 0.0,
  which makes a read failure look like a perfectly idle process.
- **AC8** — When the census parses a fixture containing a multi-line `bash -c` whose argv spans
  several rows, the parsed row count equals the process count, no synthetic row survives, and the
  rejected-row count is reported as non-zero. Observed by `selftest.py`, arm
  `test_continuation_rows_are_rejected_and_counted`.
  Red when: a row whose leading token merely happens to be numeric is admitted — AC1's contract
  alone is satisfied by such a row, which is why this criterion exists separately.
  `fixture:` a real snapshot from this node, which already carries such rows; a synthetic fixture
  would not reproduce the shape.
- **AC9** — When a backend emits a byte that is not valid UTF-8, `scan_processes()` returns rows
  rather than raising. Observed by `selftest.py`, arm `test_non_utf8_backend_output_survives`.
  Red when: the reader uses `text=True`, which dies on a reader thread and leaves stdout `None` —
  observed on this node at byte 66732 of a real CIM read.
- **AC10** — When `census.py --print` runs, its summary names the total row count, the rejected-row
  count and the unjoined count, each derived from the run. Observed by `selftest.py`, arm
  `test_summary_counts_are_derived`.
  Red when: any count is a literal, or a count is omitted so a third of the table goes missing
  without a reader noticing.
  `figure:` DERIVED — the arm compares the printed counts against the fixture's own length.

## 7. Gates

`line length` · `lexicon naming predicates` · `dead-path carriers (deleted files still named)` · `kit version markers` · `govkit selfcheck`

New arm: `tools/process-monitor/selftest.py` · stages a nonexistent backend, a captured fixture per
platform, a hanging backend shim, a real multi-line `bash -c` snapshot, a non-UTF-8 byte, and an
unjoined winpid · no assertion floor yet, this suite is new.

## 8. Open questions

- **F1 — should `cpu_s` be unknown or zero when the CIM join misses?**
  RESOLVED (agent, 2026-09-08, delegated): UNKNOWN, carried as `None`. Folding it to zero makes an
  unjoined row read as perfectly idle, which is the exact input unit 3 uses to label `IDLE` — a
  read failure would manufacture a kill candidate. Vetoes clean.
- **F2 — should an unjoined row be dropped from the census entirely?**
  RESOLVED (agent, 2026-09-08, delegated): CARRIED AND COUNTED. Measured, 115 of 314 CIM rows on
  this node carry no `CommandLine` at all, so dropping them would remove a third of the table with
  no reader told. Unit 2 refuses to attribute them, which is the right place for that decision;
  removing them here would hide it. Vetoes clean.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · S2 · S7 · S8 · S9 · §3 Edges · §4 · AC2 · AC7 · AC8 · AC9 · AC10 · §7 ·
  §8 F2 · §10 · folded spec-audit round 1 and the live-predicate probe. D13: S7 adds the anchored
  numeric guard and continuation-row rejection, inherited by citation from `run-gates.sh:432-436`
  rather than rediscovered, with AC8 staged from a real snapshot. D14: §10 corrected — the corpus
  DOES hold a process-table reader and rev-1 denied it. Probe: `command` moves from `ps -W` to CIM
  (S2, AC2), decoding goes byte-level (S8, AC9), and partial rows are carried and counted (S9,
  AC7, AC10).

## 10. Reuse audit

**The corpus DOES hold a process-table reader, and rev-1 was wrong to say it does not.**
`tools/run-gates/run-gates.sh:445-468` (`remove_descendants`) snapshots `ps -ef` at `:447` and
`scan_descendants` at `:428-443` walks its ppid edges to depth 8. rev-1's §10 asserted it "reads no
process table at all" under an explicit verified-against-source claim; that sentence was
contradicted eleven lines inside the range it cited, and correcting it is D14.

What this unit ADOPTS from that reader, by citation: the numeric field guard at `:432-436`, which
S7 now requires and AC8 stages, together with the recorded reason. What it deliberately DIFFERS on:
that reader is scoped to one root's descendants and is depth-capped at 8, while this unit
enumerates the WHOLE table with no root and no cap, because the orphan population it must see has
no root to walk from. It also needs `cpu_s`, which that reader does not collect, and a
Windows-namespace join, which that reader does not perform because it works purely in MSYS ids.
Extending `scan_descendants` in place was considered and rejected: widening a depth-capped
descendant walk into a whole-table census with a CIM join would change every existing caller's
cost and semantics for a benefit only this kit wants.

`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to
the session"` returned no process-table reader — its `SEAM`-marked hits were the `report` name stem
(`tools/drift-audit/selftest.py`, `tools/govkit/govkit.py`). That probe MISSED the live reader
above, which is recorded here because the miss is the reason rev-1's §10 was wrong: the reader is a
shell function and the map's scan coverage line says `unscanned layers: .sh`.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
