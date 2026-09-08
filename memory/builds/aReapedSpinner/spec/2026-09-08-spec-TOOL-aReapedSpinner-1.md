# TOOL-aReapedSpinner-1 — the census: one bounded read, keyed on the id every process has

**Status:** CLOSED · rev-4 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 2 · ratified 2026-09-08

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-1-backend-and-kill-measurements.md](../build/2026-09-08-build-TOOL-aReapedSpinner-1-backend-and-kill-measurements.md) | research | — |
| [2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-live-predicate-run.md) | research | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 |
| [2026-09-08-build-TOOL-aReapedSpinner-2-union-graph-measured.md](../build/2026-09-08-build-TOOL-aReapedSpinner-2-union-graph-measured.md) | research | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 |
| [2026-09-08-build-TOOL-aReapedSpinner-4-signal-namespace-measured.md](../build/2026-09-08-build-TOOL-aReapedSpinner-4-signal-namespace-measured.md) | research | TOOL-aReapedSpinner-4 |
| [2026-09-08-prompt-TOOL-aReapedSpinner-1-brief.md](../prompts/2026-09-08-prompt-TOOL-aReapedSpinner-1-brief.md) | journal | — |
| [2026-09-08-prompt-TOOL-aReapedSpinner-1.md](../prompts/2026-09-08-prompt-TOOL-aReapedSpinner-1.md) | research | — |
| [2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round1.md) | diff-review | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md) | spec-audit | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md) | spec-audit | TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Give every later unit ONE normalized view of the live process table — identity, BOTH parent graphs,
age, CPU, command — read once, bounded, with every row proven to be a real process rather than a
fragment of one, and with the namespace question answered in the data rather than left to each
consumer.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/census.py`, exposing `scan_processes()` returning rows with the
  fixed field set `winpid · msys_pid · win_ppid · msys_ppid · kind · age_s · cpu_s · command ·
  backend`. `winpid` is the primary key and is never `None`. Observed by AC1.
- **S2** — the WINDOWS backend, a JOIN: `Get-CimInstance Win32_Process` supplies `winpid`,
  `win_ppid`, `cpu_s`, the creation time and `command` for EVERY process; MSYS `ps -W` supplies
  `msys_pid` and `msys_ppid` for the MSYS subset, joined on `WINPID`. Observed by AC2, AC7.
- **S3** — `kind` is decided by the `0x400000` BIT on the `ps -W` PID column: a PID carrying it is
  a SYNTHETIC id for a non-cygwin process and yields `kind = 'native'` with `msys_pid = None`;
  only a PID without it is a real MSYS id and yields `kind = 'msys'`. Both are first-class and
  neither is dropped. Observed by AC2.
- **S4** — the POSIX backend, one `ps -eo pid,ppid,etimes,times,args` read, where `winpid` and
  `msys_pid` are the same id, `win_ppid` and `msys_ppid` are the same id, and `kind` is `msys`.
  Observed by AC3.
- **S5** — backend SELECTION with a refusal: a platform whose backend does not answer raises and
  the CLI exits non-zero naming what it tried. It never returns an empty list. Observed by AC4.
- **S6** — `census.py --print` renders the rows as TSV. Observed by AC5.
- **S7** — every subprocess carries a wall-clock bound applied to the CHILD, never through a pipe.
  Observed by AC6.
- **S8** — the ROW GUARD: every id field is accepted only as an anchored all-digit token, and a row
  that is a continuation of a previous row's raw argv is REJECTED and COUNTED. Observed by AC8.
- **S9** — backend stdout is read as BYTES and decoded with `errors="replace"`. Observed by AC9.
- **S10** — partial rows — no `command`, or no `ps -W` match — are carried with explicit `None` and
  COUNTED, and `--print` names every count. Observed by AC7, AC10.

## 3. Non-goals (OUT)

- **No classification, no scoping, no killing.** This unit decides nothing.
- **No single-namespace row contract.** rev-2 asserted "`ppid` and `pid` are in ONE namespace per
  row" and called `pid` "the id the REAPER can kill". Measured false for the non-MSYS population,
  which is 300-plus of ~313 rows here: a native `PING.EXE` survived both the bash builtin `kill`
  and `/usr/bin/kill` (`No such process`) and died only to `taskkill //PID <winpid> //F` (D21).
  The row now carries both ids and says which is which.
- **No discarding of CIM's parent graph.** rev-2 discarded it as "a different graph". It is a
  different graph, and it is the ONLY parent data the native population has (D22). Both are carried
  and each consumer is told which to use for what.
- **No second sample, no sleep, no caching.**
- **No `psutil` or any other new dependency** — M3 veto 2.
- **No version marker.** `KIT_PROCESS_MONITOR_VERSION` lives in unit 6's shell adopter.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-6` — the kit directory and the descriptor rule that CLAIMS
  this file, without which `govkit selfcheck` reds the moment it becomes tracked.
- **hands-off** `TOOL-aReapedSpinner-2` — `command` and BOTH parent graphs. The fence computes a
  tree closure, so it needs edges over the whole population, not just the MSYS tenth of it.
- **hands-off** `TOOL-aReapedSpinner-3` — `age_s`, `cpu_s` and `win_ppid`. The orphan predicate uses
  the WINDOWS graph because it is the only one defined for every row; `msys_ppid` being `None` is a
  statement about this backend's visibility and never about a parent being dead.
- **hands-off** `TOOL-aReapedSpinner-4` — both graphs for the walk, and `kind` for the signal
  choice. S8 is why a walked id is a process rather than a word from somebody's argv.
- **consumes-from** external — a `python3` resolved by `tools/lib/resolve-python.sh`, which RUNS
  each candidate because the MS-Store stub answers `command -v` and exits 9009.

## 4. Design

### Data model

```
winpid     int         PRIMARY KEY. Every process has one. Never None.
msys_pid   int|None    the MSYS id, present only for kind == 'msys'
win_ppid   int|None    CIM's ParentProcessId. Defined for every row.
msys_ppid  int|None    the MSYS parent. Present only for kind == 'msys'.
kind       str         'msys' | 'native'
age_s      float
cpu_s      float|None  None means UNJOINED, never zero
command    str|None    CIM's CommandLine. None for a process that reports none.
backend    str         'windows-join' | 'posix-ps'
```

**Why the key changed at rev-3.** rev-2 keyed on the MSYS id. Measured on this node: MSYS rows are
10 of 313. `run-gates.sh:1281` dispatches legs with argv[0] rewritten to `$PYBIN`, so a python leg
is a NATIVE row, and its children are native rows. A census keyed on MSYS ids describes 3% of the
population and structurally excludes the processes this kit exists to reap.

**`ps -W`'s PID column is not a Windows pid, and it is not always an MSYS id either.** Measured: a
non-cygwin process gets `winpid | 0x400000` (PID 4223612 against WINPID 29308), which addresses
nothing MSYS can signal. **That bit IS the discriminator S3 uses.** Without it every row would be
labelled `msys` — `ps -W` supplies a PID for all of them — and the whole native population would
be handed to a signal that cannot reach it (D33).

### The two parent graphs, and which is for what

| graph | defined for | used for |
|---|---|---|
| `win_ppid` | every row | the ORPHAN predicate (unit 3), and the descendant walk (unit 4) |
| `msys_ppid` | `kind == 'msys'` only | the descendant walk (unit 4), unioned with the above |

`msys_ppid is None` means "this backend does not see a parent for this row", NOT "the parent is
dead". rev-2 folded that sentinel into the orphan predicate and thereby graded every native process
parentless (D18). The Windows graph has no such sentinel — it names a real parent for every row —
which is exactly why the orphan predicate moves onto it.

### Windows: which side supplies what

CIM is now the primary read and supplies `winpid`, `win_ppid`, `cpu_s`, `CreationDate` and
`CommandLine`. `ps -W` is the secondary read and supplies only the `msys_pid`/`msys_ppid` overlay,
joined on its `WINPID` column. Two `ps -W` columns are deliberately unused: `STIME` (a clock for
today, a `Mon DD` otherwise) and `COMMAND` (the EXECUTABLE PATH with no arguments — measured,
scoping on it matched zero of 315 rows). `PGID` is read and DISCARDED: three descendants of a
disposable test tree shared the Bash-tool shell's own pgid, so a group kill reaps the caller.

### The row guard (S8), inherited rather than rediscovered

`tools/run-gates/run-gates.sh:432-436` records the hazard and carries the guard: cygwin `ps` prints
argv RAW, so a command line containing a newline splits one process across rows "whose field 2 and
3 are attacker-or-accident-chosen text", and snapshots here "already carry about ten such
continuation rows". Its predicate is `$2 ~ /^[0-9]+$/ && $3 ~ /^[0-9]+$/`. This unit adopts it and
adds the COUNT, because a silent drop is the failure one level up.

### Decoding (S9)

PowerShell writes the CONSOLE codepage. Measured: `subprocess.run(..., text=True)` died with
`UnicodeDecodeError` on `0xe7` at byte 66732, on a reader THREAD, after which `o.stdout` is `None`
and the caller sees an `AttributeError` far from the cause.

### Files touched (estimate)

`tools/process-monitor/census.py`, `tools/process-monitor/selftest.py`, and a frozen census fixture
`tools/process-monitor/fixtures/census-node-a.tsv` captured from this node — both namespaces, an
`export TEMP=` row, and a multi-line `bash -c`. All new.

## 5. Production-readiness checklist

- security — fixed argv, no shell interpolation; a command string is DATA and never re-executed.
  S8 is the security-relevant half: without it untrusted argv text reaches an id field the reaper
  acts on.
- perf / scale — measured 1039 ms CIM + 128 ms `ps -W`, over a 320 ms PowerShell floor.
- error / empty / loading states — an unanswerable backend REFUSES (S5); partial rows are carried
  with `None` and counted (S10), never dropped.
- observability — every row carries `backend` and `kind`; `--print` names the rejected, unjoined
  and no-command counts.
- risks — measured, 199 of 314 CIM rows carry a `CommandLine`, so a third of the table is
  unattributable and that number must be visible.
- testing — captured fixtures per backend, a two-namespace fixture, a continuation-row fixture, and
  live arms.
- migration — none; new module.
- user docs — the kit README, unit 6.

## 6. Acceptance criteria

- **AC1** — When `scan_processes()` runs on this node, every row carries all nine fields of S1, no
  row carries a `None` `winpid`, and every row's `win_ppid` is an integer. Observed by
  `selftest.py`, arm `test_row_contract_is_complete`.
  Red when: a backend adds or drops a field, or `winpid` is ever absent — it is the primary key and
  every consumer joins on it.
- **AC2** — When the Windows backend runs, `native` rows are the MAJORITY and a run grading fewer
  than half the rows native REDS; the msys row's `msys_ppid` equals what `ps -ef`
  reports for it, and the native row's `msys_pid` is `None` while its `win_ppid` is an integer.
  Observed by `selftest.py`, arm `test_both_kinds_are_present_and_distinguished`.
  Red when: the census returns only the MSYS subset (D22), or grades the whole table `msys`
  because no discriminator was applied (D33). "At least one of each" was the rev-3 wording and
  it passes on a table labelled entirely one way — a partition criterion must assert the
  partition's SHAPE against the measurement, which here is 10 msys of 313.
  `fixture:` needs live MSYS `ps` and PowerShell; off Windows the arm SKIPS with a named reason,
  printed, never silent.
- **AC3** — When the POSIX backend parses a captured `ps -eo` fixture, its rows carry `winpid ==
  msys_pid`, `win_ppid == msys_ppid`, `kind == 'msys'`, and `age_s`/`cpu_s` equal to the fixture's
  `etimes`/`times`. Observed by `selftest.py`, arm `test_posix_fixture_collapses_both_namespaces`.
  Red when: the POSIX path leaves a namespace field `None` and every consumer's two-graph logic
  silently degrades off Windows.
  `fixture:` a captured text fixture — MSYS `ps` rejects `-o` entirely, so this node can never
  exercise the live POSIX path, and the arm says so rather than implying coverage.
- **AC4** — When the backend is forced to a name that does not exist (`PROCMON_BACKEND=nonesuch`),
  `census.py --print` exits non-zero naming what it tried and prints no table. Observed by
  `selftest.py`, arm `test_no_backend_refuses`.
  Red when: a failed read returns `[]` and every unit downstream reports a clean tree.
- **AC5** — When `census.py --print` runs on this node, its stdout carries a header and at least two
  data rows, one of which is the reading process itself. Observed by `selftest.py`, arm
  `test_live_read_sees_itself`.
  Red when: the renderer emits a column the contract does not declare, or the arm passes against an
  empty table.
- **AC6** — When a backend command is made to hang, `scan_processes()` returns within the declared
  bound and reports that backend unanswered. Observed by `selftest.py`, arm
  `test_hung_backend_is_bounded`, staging the hang with a shim earlier on `PATH`.
  Red when: the bound is applied through a pipe or a command substitution, which bounds the verdict
  and not the clock — the `bounded-through-a-pipe-is-unbounded` class, selected for these paths.
- **AC7** — When a CIM row has no `ps -W` match, it survives as `kind == 'native'` with `msys_pid`
  and `msys_ppid` `None`, and is counted as unoverlaid. When a CIM row reports no `CommandLine`, it
  survives with `command` `None` and is counted separately. Observed by `selftest.py`, arm
  `test_partial_rows_survive_and_are_counted_apart`.
  Red when: either class is dropped, or the two counts are summed — they mean different things and
  one of them is a third of the table.
- **AC8** — When the census parses a fixture containing a multi-line `bash -c` whose argv spans
  several rows, the parsed row count equals the process count, no synthetic row survives, and the
  rejected count is reported non-zero. Observed by `selftest.py`, arm
  `test_continuation_rows_are_rejected_and_counted`.
  Red when: a row whose leading token merely happens to be numeric is admitted. AC1's contract alone
  is satisfied by such a row, which is why this is separate.
  `fixture:` the frozen snapshot from this node, which already carries such rows.
- **AC9** — When a backend emits a byte that is not valid UTF-8, `scan_processes()` returns rows
  rather than raising. Observed by `selftest.py`, arm `test_non_utf8_backend_output_survives`.
  Red when: the reader uses `text=True`, which dies on a reader thread and leaves stdout `None`.
- **AC10** — When `census.py --print` runs, its summary names the total, rejected, unoverlaid and
  no-command counts, each derived from the run. Observed by `selftest.py`, arm
  `test_summary_counts_are_derived`.
  Red when: any count is a literal, or one is omitted so a class goes missing unnoticed.
  `figure:` DERIVED — the arm compares the printed counts against the fixture's own length.
- **AC11** — When every row of a LIVE census read on this node is put to the liveness probe its own
  `kind` implies — `kill -0 <msys_pid>` for `msys`, a CIM presence check on `winpid` for
  `native` — every row answers, and the count of non-answering rows is reported. A row that dies
  between the scan and the probe is re-read once before being counted. Observed by
  `selftest.py`, arm `test_every_live_row_answers_its_own_liveness_probe`; SKIPPED with a named,
  printed reason off Windows.
  Red when: the census claims a row whose namespace nothing can address (D21). rev-3 aimed this
  at the FROZEN fixture, whose rows are all long dead, so it could neither pass nor fail (D40):
  a criterion whose observation is a LIVE property needs a live subject.

## 7. Gates

`line length` · `lexicon naming predicates` · `dead-path carriers (deleted files still named)` · `kit version markers` · `govkit selfcheck`

New arm: `tools/process-monitor/selftest.py` · stages a nonexistent backend, a captured fixture per
platform, a hanging backend shim, a real multi-line `bash -c` snapshot, a non-UTF-8 byte, a
CIM-only row, a no-command row, and the per-kind liveness probe · no assertion floor yet, this
suite is new.

## 8. Open questions

- **F1 — should `cpu_s` be unknown or zero when CIM reports nothing?**
  RESOLVED (agent, 2026-09-08, delegated): UNKNOWN, carried as `None`. Zero makes the row read as
  perfectly idle, which is the exact input unit 3 uses to label — a read failure would manufacture
  a kill candidate. Vetoes clean.
- **F2 — should a row with no `command` be dropped?**
  RESOLVED (agent, 2026-09-08, delegated): CARRIED AND COUNTED. Measured, 115 of 314 rows, so
  dropping them removes a third of the table with no reader told. Unit 2 refuses to attribute them,
  which is the right place for that decision. Vetoes clean.
- **F3 — should the census key on `winpid` or keep the MSYS id?**
  RESOLVED (agent, 2026-09-08, delegated): `winpid`. It is the only id defined for every row;
  measured, the MSYS id exists for 10 of 313. The whole native population — every `python.exe` a
  gate leg is, every `node.exe`, every `pwsh.exe` — is unaddressable without it, and `run-gates.sh`
  dispatches legs as native processes. Keeping the MSYS key would have made the kit's promise
  structurally unmeetable for its own primary target. Vetoes clean: no dependency, no new surface,
  and the change narrows rather than widens what may be killed.

## 9. Revision log

- rev-4 · 2026-09-08 · S3 · §4 · AC2 · AC11 · folded spec-audit round 3 at its NON-CONVERGENT
  exit. D33: `kind` gains its discriminator — the `0x400000` bit — which rev-3 never stated, so
  every row would have graded `msys`. AC2 now asserts the partition's SHAPE against the
  measured 10-of-313, because "at least one of each" passes on a table labelled entirely one
  way. D40: AC11 moves off the frozen fixture, whose rows are dead, onto a live read.
- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · S2 · S7 · S8 · S9 · AC2 · AC7-AC10 · §10 · folded spec-audit round 1
  (D13, D14) and the live-predicate probe.
- rev-3 · 2026-09-08 · S1 · S2 · S3 · S4 · §3 · §4 · AC1 · AC2 · AC3 · AC7 · AC11 · §8 F3 · folded
  spec-audit round 2. D21: the single-namespace row contract is measured false — a native
  `PING.EXE` survived both MSYS `kill`s and died only to `taskkill //PID` — so the row now carries
  `winpid`, `msys_pid` and `kind`, and AC11 asserts every row answers its own liveness probe.
  D22: CIM's parent graph is no longer discarded; it is `win_ppid`, defined for every row, and it
  is what makes a native descendant walkable at all. The primary key moves to `winpid` (§8 F3).

## 10. Reuse audit

**The corpus DOES hold a process-table reader, and rev-1 was wrong to deny it.**
`tools/run-gates/run-gates.sh:445-468` (`remove_descendants`) snapshots `ps -ef` at `:447` and
`scan_descendants` at `:428-443` walks its ppid edges to depth 8.

What this unit ADOPTS from it, by citation: the numeric field guard at `:432-436`, which S8 now
requires and AC8 stages, with the recorded reason. What it DIFFERS on, and why extending in place
was rejected: that reader is scoped to one root's descendants, depth-capped at 8, and works purely
in MSYS ids — which rev-3 measures to be 10 of 313 rows. This unit enumerates the WHOLE table with
no root and no cap, carries two parent graphs and a CPU field that reader does not collect, and is
keyed on `winpid`. Widening a depth-capped MSYS descendant walk into that would change every
existing caller's cost and semantics for a benefit only this kit wants; unit 7 inverts the
dependency instead.

`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to
the session"` returned no process-table reader — its `SEAM`-marked hits were the `report` name stem.
That probe MISSED the live reader above, and the reason is recorded because it is the reason rev-1's
§10 was wrong: the reader is a shell function and the probe's own coverage line says
`unscanned layers: .sh`. A `no seam fits` finding from that probe alone is weaker than it looks.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
