# TOOL-dRedressedBar-18 — a gate profiler: every leg run clean and unbounded, serially or under a load cap, each profiled to its processes, stalls reported and never killed

**Status:** CLOSED · rev-9 · 2026-10-16 · node d · Tier-2 · base ebce889c · streams tooling · order 13 · ratified 2026-10-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-build-TOOL-dRedressedBar-18-1-set-aside-work.md](../build/2026-10-15-build-TOOL-dRedressedBar-18-1-set-aside-work.md) | journal | — |
| [2026-10-15-build-TOOL-dRedressedBar-18-2-acceptance-ledger.md](../build/2026-10-15-build-TOOL-dRedressedBar-18-2-acceptance-ledger.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-18-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-18-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-18-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-18-2-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-18-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-18-3-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-18-brief.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-18-brief.md) | research | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-18-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-18-4-revision.md) | research | TOOL-dRedressedBar-19 |
| [2026-10-15-prompt-TOOL-dRedressedBar-18-5-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-18-5-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md) | research | TOOL-dRedressedBar-19 TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-6-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-6-revision.md) | research | TOOL-dRedressedBar-21 TOOL-dRedressedBar-19 |
| [2026-10-15-prompt-TOOL-dRedressedBar-22-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-22-2-revision.md) | research | TOOL-dRedressedBar-22 TOOL-dRedressedBar-19 |
| [2026-10-15-prompt-TOOL-dRedressedBar-25-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-2-revision.md) | research | TOOL-dRedressedBar-25 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 |
| [2026-10-16-prompt-TOOL-dRedressedBar-27-2-revision.md](../prompts/2026-10-16-prompt-TOOL-dRedressedBar-27-2-revision.md) | research | TOOL-dRedressedBar-27 |
| [2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 |
| [2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md) | diff-review | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 |
| [2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md) | diff-review | TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-19 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 |
| [2026-10-15-review-TOOL-dRedressedBar-25-26-diff-review-round3.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-25-26-diff-review-round3.md) | diff-review | TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 TOOL-dRedressedBar-26 |

<!-- /gen:spec-records -->

## 1. Goal

This build's bar profile (`build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md`) was
rebuilt from scratch files the runner erases. It ran with a knob set, saw nothing inside a leg, and
called the bar spawn-bound from a 10 s CPU average. This unit ships `measure_legs.py` in the run-gates
kit. It runs every manifest leg with no knob, no ceiling and no reap, one at a time or under a live
80% CPU and 90% memory cap. It keeps every record and profiles each leg down to its processes, so the
ceilings, the width profiles and the spawn claim rest on measurement. A launcher that is an App
Execution Alias is run as the interpreter it starts, because its children leave any job, and the
record names each such substitution (F3).

## 2. Scope (IN)

- **S1** — `tools/run-gates/measure_legs.py`, a run-gates engine file. Its population is every row of
  the manifest beside the kit dir, read at run time, or of `--legs <path>`. Guarded, kit-subject and
  `selftests`-chunk legs are all in it, and the six `tools/unattended/` suites that are not rows stay
  out by construction. It applies no guard, hold, reuse, docs mode, ceiling, whole-run wall, retry or
  reap. It erases no record. The one file it deletes is each leg's raw capture, once its redacted
  copy is written (S11). An empty manifest, a row with no name
  or no argv list, and a duplicate name each refuse the run with exit 2. Observed by AC1 and AC10.
  `TOOL-dRedressedBar-19` makes this reader `read_profile_legs`, which wraps
  `held_halves.load_manifest`, and adds the malformed-input classes this list misses, each naming
  its row (its S19 and S37, units-16-18 report ids 19 and 37).
  - **Readers:** S1 deletes one named thing, each leg's raw capture `raw/<i>.out` in the scratch
    dir, which this unit also creates. S11 carries the full inventory. It was read at `679afc31`
    with `git grep -n -F 'raw/<i>.out'` and
    `git grep -n -l -e 'measure_legs' -e 'gate-profile/' -e 'raw_kept'` over the tracked tree. The
    first finds only this spec, which is a record. The second finds this spec, four other specs
    and `drift_report.py`'s `measure_legs_retried_after_timeout` with its map entry, which hold the
    words but read nothing of this tool.
    by name: READER NOT IN TREE, because the file is a runtime artifact under the scratch dir's
    TMPDIR, outside the tree, and the only code that will spell its name is this unit's unbuilt
    profiler, which creates and deletes it.
    by value: the capture's bytes are read only by this unit's redaction pass in
    `tools/run-gates/measure_legs.py`, which writes `<i>.log` from them before the delete (S11).
    That file is already in §4's Files touched, so no file is added.
- **S2** — `--serial` runs one leg at a time. `--concurrent` admits the next leg only on a host
  sample taken after the previous admission that reads CPU at or under 80% and memory at or under 90%,
  or when no leg of the run is running. Observed by AC4 and AC5.
- **S3** — Each leg runs in its own Windows Job Object, so the kernel counts its processes, user and
  kernel time, peak memory and I/O, short-lived processes included. On a host whose PYBIN is an
  App Execution Alias this holds only through S14. Observed by AC1 and AC2.
- **S4** — Per-process rows come from `scan_processes` walked with `build_walk` from the leg's root.
  The census row gains two optional fields, `peak_mem_b` and `mem_b`, read by the CIM query it already
  runs. Observed by AC1 and AC3. The old row shape's readers, the pair declared once as
  `OPTIONAL_FIELDS`, and the rule for a legacy line of four to six fields are
  `TOOL-dRedressedBar-19`'s S10 (units-16-18 report ids 10 and 33).
- **S5** — The cost of one spawn is sampled each census tick by the runner's own `measure_spawn_cost`,
  run from its source text. Observed by AC2.
- **S6** — A host-load timeline is sampled every second, and a foreign-load census is taken by the
  runner's rule over each census scan. A selftest arm holds the port to the runner's own predicate.
  Observed by AC4 and AC8.
- **S7** — A leg is STALLED when, over a declared window, its tree's census CPU delta and its job
  CPU delta both stay under a threshold and its log does not grow. The tree is reported and left
  running. Observed by AC6 and AC7.
- **S8** — The knobs are scrubbed from every leg's environment, the two turnstile nesting names
  included, and the scrubbed set is derived and printed. The verdict-relevant environment is recorded
  as digests. The legs get the runner's own exports, its python and its bash. When S14 resolves an
  alias, its python is the interpreter the alias starts. Observed by AC9.
- **S9** — The profile holds no host turnstile (F1, resolved b), so a bar nested in a leg queues on
  the host like any bar. At each census tick the tool reads the host turnstile's queue and slot
  beacons. Per leg it records the foreign holders it saw and its own bars' queue wait, apart from its
  work, and folds both into the `.leg` row's `foreign` field so `derive-ceilings.py` sets the reading
  aside. Observed by AC9 and AC15.
- **S10** — One run directory, `<git-dir>/gate-profile/<run id>/`, holds every record and log, in the
  formats of §4. Each `<i>.leg` row uses the runner's eight-field grammar. Observed by AC10.
- **S11** — Each leg's log is kept as its redacted copy only, redacted as the runner redacts its
  durable copies (F2, resolved b). The raw capture is deleted once that copy is written. A capture a
  process still holds is retried at run end, and otherwise kept and named in `raw_kept` with its
  reason. Observed by AC10 and AC11. The redaction's byte contract and its parity arm against the
  runner's `redact`, and the next run's sweep of the raw captures a crashed or killed run leaves,
  are `TOOL-dRedressedBar-19`'s S39, S20 and S38 (units-16-18 report ids 39, 20 and 38).
  `TOOL-dRedressedBar-22` has an interrupt run the run end's retry too, so a capture an ended leg's
  processes still hold is retried there and, when still held, named in `raw_kept` (its S2; closing
  review round 1, report ids 2 and 14).
  - **Readers:** S11 deletes each leg's raw capture, `raw/<i>.out`, once `<i>.log` is written. The
    inventory was read at `679afc31` with `git grep -n -F 'raw/<i>.out'` and
    `git grep -n -l -e 'measure_legs' -e 'gate-profile/' -e 'raw_kept'` over the tracked tree. The
    first finds only this spec, at §4 "The environment a leg gets" and F2, and a spec is a record.
    The second also finds four other specs, which are records, and `tools/drift-audit/drift_report.py`
    with its map entry, whose `measure_legs_retried_after_timeout` contains the words and reads
    nothing of this tool. The runner's own raw capture, `$WORK/$i$sfx.raw` (`run-gates.sh:3877` at
    the base, `:3876` and `:3880` at `997fc294f`), is a different file, and this unit leaves it
    alone. Its processed copy, `$WORK/$i$sfx.out`, is not the raw capture (`TOOL-dRedressedBar-19`,
    units-16-18 report id 15).
    by name: READER NOT IN TREE, because the capture lives under the scratch dir's TMPDIR,
    outside the tree, and the only code that will spell its name is this unit's unbuilt
    profiler, which creates it, redacts it and deletes it.
    by value: the capture's bytes are read only by this unit's redaction pass in
    `tools/run-gates/measure_legs.py`, at leg end and again at run end, or at an interrupt since
    `TOOL-dRedressedBar-22`, for a leg that left processes running. Each read comes before the
    delete, so no reader loses the value. Once `<i>.log` exists it is the only copy anything reads. That file is already in §4's Files touched, so no file is
    added.
- **S12** — On a non-Windows host the tool refuses with exit 2 and names the platform. Observed by
  AC12.
- **S13** — The `measure-legs selftest` leg runs `--selftest` over committed fixtures under
  `tools/run-gates/fixtures/measure-legs/`. It comes with its descriptor row, its manifest, budget
  and Windows-only rows, both kits' version bumps, the kit README section, a `help/` page and the map
  claim. Observed by AC13 and AC14. Neither reads the kit README section or the map claim, which
  `TOOL-dRedressedBar-19`'s AC7 observes (units-16-18 report ids 7 and 24). That unit also corrects
  the declarations this list gives: the descriptor row gives way to an `[[exempt_leg]]` in the govkit
  registry, with the fixtures withheld as `project-owned` (its S29), the guard gains three files
  (S21), and the subject-pin row and the `WHOLE_RUN` row the leg owes, which this unit left out,
  land there (S22, S25; report ids 21, 22, 25 and 29).
- **S14** — Before the first leg, `resolve_launcher_aliases` probes PYBIN and each distinct first
  word of the legs' argvs after the PYBIN mapping. A launcher whose file is an App Execution Alias
  runs, in every leg, as the interpreter that alias starts, and the legs' `GOV_PYTHON` names that
  interpreter. The interpreter the legs will run must keep its child inside a test job, or the run
  refuses with exit 2. The envelope's `substitutions` names each substitution with its alias path
  and its resolved path (F3, resolved b; §4 "Alias launchers"). Observed by AC1, AC2 and AC16.
- **S15** — The scratch dir, the turnstile key and each probed launcher are converted once with
  `cygpath -m`, in the resolved bash and in the script that produces each. Python opens only the
  converted spelling. The envelope records both spellings of the scratch dir and the key. This
  part of `TOOL-dRedressedBar-19`'s S11 moved here, because native Python cannot open bash's
  scratch spelling and no leg could run without it. That unit keeps the turnstile key's
  failed-conversion rule. Observed by AC17.

## 3. Non-goals (OUT)

- No change to any existing leg's argv, guard or ceiling, and no runner behaviour beyond the version
  line: `run-gates.sh` moves by its version line and its history comment only. The one new leg is
  S13's (`TOOL-dRedressedBar-19`, units-16-18 report id 6). `derive-ceilings.py` is not edited
  (§4 "The record").
- No run of the `tools/unattended/` suites that are not legs (owner rule, 2026-08-23).
- No Event Tracing for Windows and no elevation (§4 "Alternatives rejected").
- No POSIX backend (§4 "Platform").
- No width cap in `--concurrent`. The owner set the caps as load, not width.
- No knob. Every setting is a flag, so the tool reads no new `GATE_` or `GOV_` variable. It sets one
  existing variable in the legs' environment, `GOV_PYTHON`, and only when S14 resolves an alias.
  No flag turns the resolution off: AC1's red half disables it in a probe program.
- No resolution rule for an alias other than PYBIN's. A leg launcher that is an alias and is not
  PYBIN refuses the run (§4 "Alias launchers").
- No report renderer. `legs.tsv` is the table source, and the chunk and slowest-leg tables are a
  `sort` or a five-line script over it.
- No full profiled bar inside a pass. That run is the main loop's, at the close.
- No hold of the host turnstile (F1), and no write to it. The tool reads the queue and the slot
  beacons, and never takes, drops or reaps a ticket or a beacon.

### Edges

- **consumes-from** external — a Windows host, and the process-monitor kit resolvable as a sibling
  of run-gates. Without either, the tool refuses rather than profiling less.
- **consumes-from** external — the runner's turnstile layout on disk: the host key, the ticket name
  and each slot beacon's `pid` file (`run-gates.sh:1513-1514`, `:1534-1535`, `:1892`, `:1951`).
  It is read as `unattended.sh:6684-6690` already reads the queue, and AC15 runs the real runner
  against the reader, so a layout change reds that arm.
- **hands-off** `TOOL-dRedressedBar-19` — the profiler, its fixtures, its leg's declarations and
  the census fields this unit builds, which that unit corrects: the census readers of the old row
  shape, the refused read for a turnstile key whose conversion fails (the conversion itself is
  S15 here, since rev-4), the holder's preflight and bounded wait, one
  manifest reader, the redaction's byte contract and parity, the leg's guard, parity row, subject
  pin and adopter declaration, one resolved bash, the launch-failure branch, turnstile churn, the
  sweep of a dead run's raw captures, the manifest refusals and the fork fixture. Also the reviewed
  kickoff manifest re-audit in its own second commit, over this unit's edits and that unit's, while
  this unit's pass commit carries only the re-stamp the ratchet's staged check requires (§4 "Files
  touched"). And this spec's prose, §7 leg line and revision line, which it
  corrects in place (units-16-18 report ids 1, 6, 7, 10 to 15, 19 to 22, 24 to 27, 29, 32 to 39
  and 42).
- **hands-off** `TOOL-dRedressedBar-21` — `write_atomic`, whose fixed `.tmp` name that unit
  replaces with a `tempfile.mkstemp` temp (closing review round 1, H1), and the capture's open in
  `run_leg` and its read and delete in `write_leg_capture`, which that unit holds to the file
  `build_capture_file` made (the owner's ruling of 2026-10-15).
- **hands-off** `TOOL-dRedressedBar-22` — the interrupt branch's naming of a capture an ended leg's
  processes still hold and the whole-table `legs.tsv` rewrite at run end and at an interrupt
  (closing review round 1, report ids 2, 9 and 14), the interpreter probe's base-interpreter child
  (id 3), `check_admit` as the loop's one admit decision (id 6), an arm for each of the four alias
  refusals (id 11), and the resolution red half's verdict reads with `memio.py`'s line (id 15).
- **hands-off** `TOOL-dRedressedBar-25` — the `measure-legs selftest` guard, whose run-gates
  entries that unit folds into `{prefix}/run-gates/` beside `{prefix}/gate-legs.json` (round 2, ids
  4, 11, 20 and 23).
- **hands-off** external — a `derive-ceilings.py` that reads `gate-profile/` records directly. It is
  not built here: readings enter through the existing `--observed` route.
- **hands-off** external — the first full profiled run over the fixed tree, and the
  `selftest-pooled-evidence.txt` calibration of the new leg. Both run suites, so both are the main
  loop's.

## 4. Design

### Candidates per measurement, and the test each could lose (M12)

| Measure | Candidate | Loses when | Result |
|---|---|---|---|
| per-leg totals | Job Object per leg | a descendant leaves the job | CHOSEN; AC1 is the refutation for the native-spawn path, and `TOOL-dRedressedBar-19`'s AC32 for the MSYS fork path, which AC1's python children never take (units-16-18 report id 32). An alias's children do leave it (measured below), so S14 resolves the alias first |
| alias launcher | refuse at preflight, remedy `GOV_PYTHON` (F3 a) | the operator must act before any profile runs | REJECTED by the owner, F3 |
| alias launcher | run the interpreter the alias starts (F3 b) | that interpreter's child leaves a test job too | CHOSEN; the run then refuses (S14) |
| alias launcher | census tree against job membership, totals `unknown` (F3 c) | every reading on node d reads `unknown` | REJECTED by the owner, F3 |
| alias detection | the file's reparse tag is `IO_REPARSE_TAG_APPEXECLINK` | the tag cannot be read | CHOSEN, measured below; an unreadable tag refuses |
| alias detection | the path sits under `WindowsApps` | an alias elsewhere, or a plain program in that dir | REJECTED: a convention, where the tag is the file system's own type |
| alias detection | the launcher's child leaves a test job | it needs a child-starting program per launcher kind | REJECTED as the detector; kept as the interpreter's verification |
| real interpreter | the alias's own `sys.executable` | the alias starts no Python | CHOSEN, measured below |
| per-leg totals | sum of census rows | a process lives shorter than one scan | REJECTED, measured below |
| per-leg totals | ETW kernel process trace | the token is not elevated | REJECTED, §4 Alternatives |
| per-process rows | census polling | a process lives shorter than one scan | CHOSEN, with `unseen` counted |
| per-process rows | job completion-port messages plus per-pid handles | the brief bars a second process reader, and Windows documents delivery as not guaranteed | REJECTED |
| host load | `GetSystemTimes` and `GlobalMemoryStatusEx` | a call spawns or blocks | CHOSEN: 12.6 µs and 0.6 µs a call |
| stall CPU | census walk alone | a silent leg works through short-lived children | KEPT, with a job veto (AC7) |
| spawn cost | the runner's `measure_spawn_cost` from its source | its text is not found | CHOSEN; a miss refuses |
| turnstile wait | the host queue's tickets, attributed to a leg by the census | a wait shorter than one census period | CHOSEN, §4 "The turnstile" |
| turnstile wait | the printed `gate queue: waited` line in the leg's log | the suite captures its bar's output | REJECTED, §4 Alternatives |
| foreign holder | each slot beacon's `pid`, attributed by the census | a holder that starts and ends between scans | CHOSEN |

**Measured on node d, 2026-10-14 (PINNED).** Three `scan_processes()` calls took 0.95 to 0.97 s at 327
rows. The clone's spawn floor reads 8.323 ms (`gate-spawn-floor`, 2026-10-11). A trivial process
therefore lives about 1% of one scan, so a census-only count misses nearly all of the churn the
spawn claim is about. `shell32.IsUserAnAdmin()` returned 1 for this session, so ETW would run here.
It is rejected because the tool may not assume an elevated token. `msys-2.0.dll` carries the strings
`CREATE_BREAKAWAY_FROM_JOB`, `NtCreateJobObject` and `NtAssignProcessToJobObject`. UNVERIFIED from
source: Cygwin's spawn adds the breakaway flag only when its own job allows breakaway. So the job is
created with no limit flags at all: no `BREAKAWAY_OK`, no `SILENT_BREAKAWAY_OK`, no
`KILL_ON_JOB_CLOSE`. AC1 fails if a descendant escapes anyway.

**Measured on node d, 2026-10-15 (PINNED).** AC1 failed on the first build
(`build/2026-10-15-build-TOOL-dRedressedBar-18-1-set-aside-work.md`). PYBIN was `python3`, and
`command -v python3` resolved to the App Execution Alias in the user's `WindowsApps` dir, which
starts `pythoncore-3.14-64`. Every leg of `serial.json` read `procs_total` 1, and `memio.py 200`
read `peak_job_mem_b` 6950912 with `write_bytes` 0. The builder's scratch manifest isolated the
cause. A bash leg running only `sleep`s counted 7, so bash-forked processes stay in the job, which
settles the Cygwin question above. A plain `Python312` interpreter running `spawn.py 2 1` counted 4,
and the `python3` and `py` aliases counted 1 each. A direct probe for this revision, with no bash,
created each interpreter suspended, assigned it to a fresh job and resumed it, running a program
that starts one child and waits for it. `TotalProcesses` read 1 for the alias, 2 for the
interpreter the alias starts, and 2 for `Python312`. `os.lstat` gave the reparse tag `0x8000001b`,
`IO_REPARSE_TAG_APPEXECLINK`, for `python3.exe`, `python.exe` and `py.exe` in that dir, and
`os.path.islink` read False for the alias. Run through the alias, `sys.executable` printed the
interpreter it starts, under the user's `AppData\Local\Python\pythoncore-3.14-64`.

### What each cannot see

| Mechanism | On this node (Windows, Git-Bash) | On a POSIX node |
|---|---|---|
| Job Object | Work done for the leg in another process, such as a WMI provider host answering a CIM query or an on-access scanner opening each image. A process that broke away. A process an App Execution Alias starts, unless S14 resolved that alias. Per-process detail. Its peak is commit, not working set. | Does not exist. `getrusage(RUSAGE_CHILDREN)` sums only waited-for descendants, counts no processes and reports the largest single peak RSS. A cgroup v2 scope needs delegation and keeps no spawn total. |
| census polling | Any process that starts and ends between scans. CPU a process burns after its last sighting. MSYS-only parent edges for a process `ps -W` does not list. | `ps -eo` gives no peak memory, so the two new fields read None. |
| ETW | Nothing, with elevation. Without it, the session cannot start. | eBPF, the proc connector and auditd need root. `strace -f` slows fork-heavy work several-fold, which is contamination. |
| turnstile read | A bar on another turnstile key. A wait shorter than one census period. A holder or waiter whose pid no scan saw. | The same files exist, and no backend reads them (§4 "Platform"). |

### Platform

Every registered node in `tools/playbook/fleet.toml` is Windows, and every job in
`.github/workflows/remote-ci.yml` runs `windows-latest`. A POSIX backend would be untested scaffolding
(charter `[yagni]`). The tool refuses on any platform without the job API and names it. The selftest
row joins `tools/run-gates/windows-only-legs.txt`, whose bar admits a suite that exercises its subject
only on Windows.

### Launching a leg

1. The argv is the manifest row's, with `{prefix}` resolved by the inlined canonical
   `resolve_prefix_token` block, against the tool root the runner derives (`run-gates.sh:2727-2736`).
   A first word `python` or `python3` maps to PYBIN, as at `run-gates.sh:3836`. PYBIN comes from the
   runner's own `resolve_python` (`run-gates.sh:137-166`), run once in bash from its source. A first
   word S14 resolved then maps to its resolved interpreter (§4 "Alias launchers").
2. The root is a wrapper, `<bash> -c 'exec "$@"' measure-legs <argv…>`. `<bash>` is
   `profile_bar.resolve_bash` (`profile_bar.py:282-304`), which skips the WSL launcher. The leg thus
   resolves `bash`, `node` and PYBIN through MSYS `PATH`, as the runner's worker does
   (`run_leg_at`, `run-gates.sh:4592-4613`, ends in the same `exec`). Its cwd is the top level
   (`run-gates.sh:103`), its stdin is `DEVNULL`, and stdout and stderr go to one file, the raw
   capture, as at `run-gates.sh:3877`. Every bash the tool starts is this one `<bash>`, resolved
   once at start: the wrapper, `mktemp`, the runner functions of step 1 and of "Sampling", and the
   selftest's runner calls. An empty result refuses with exit 2, naming every candidate tried, and
   an arm holds the rule (`TOOL-dRedressedBar-19`'s S34, units-16-18 report id 34).
3. The root is created with `CREATE_SUSPENDED`. It is assigned to a fresh job through `OpenProcess`
   with `PROCESS_SET_QUOTA | PROCESS_TERMINATE`, which the assign requires and nothing else uses. Its
   one thread is then resumed through `CreateToolhelp32Snapshot` and `ResumeThread`. So no descendant
   exists before the job does. The start stamp is taken at the resume. This step states no outcome
   for a failure of any of those calls, and a suspended root never exits.
   `TOOL-dRedressedBar-19`'s S35 terminates that root, which has executed nothing, records the leg
   as `fail` with its `launch_error`, and lets the run continue (units-16-18 report id 35).
4. The end is the root's `ExitTime` from `GetProcessTimes` on a handle held since launch. Wall time
   is therefore kernel-clocked, and the loop's poll latency does not enter it. Descendants still alive
   are counted as `left_running` and left alone. In `--serial`, the next leg starts at the root's
   exit, as the runner's would.

### Alias launchers (F3, resolved b)

An App Execution Alias is a reparse point that Windows answers by activating a packaged app, and
every process it starts leaves the leg's job (§4 "Measured on node d, 2026-10-15").
`resolve_launcher_aliases` runs once, after PYBIN is known and before the first leg. Steps 1 to 4
are inside it, so a probe program that rebinds it disables the detection and the verification
together, which is how AC1 stages its resolution red half.

1. **Probed set.** PYBIN, and each distinct first word of the legs' argvs after the PYBIN mapping.
   On today's manifest that is `bash`, `node` and PYBIN, DERIVED from the manifest at run time. The
   set-aside `TOOLS_SCRIPT` resolves each with `command -v` in the legs' bash, and S15 adds each
   one's `cygpath -m` spelling beside it. That spelling carries the `.exe` the bash spelling omits
   (measured on node d, 2026-10-15). A launcher `command -v` does not find is recorded unresolved
   and probed no further, and its leg fails as it would under the bar.
2. **Detection.** `check_app_alias(path)` is True when `os.lstat(path).st_reparse_tag` equals
   `stat.IO_REPARSE_TAG_APPEXECLINK`. A found launcher whose file `os.lstat` cannot read refuses the
   run with exit 2, because the tool cannot prove it is no alias.
3. **Resolution.** For PYBIN, `resolve_alias_interpreter` runs
   `"$1" -I -c 'import sys; print(sys.executable)'` once in the legs' bash, with `$1` the launcher
   as PYBIN spells it. The printed path, forward-slashed, is the resolved interpreter when it is a
   file and `check_app_alias` reads False for it. Anything else refuses with exit 2, naming the
   alias and what it printed. A leg launcher that is an alias and is not PYBIN refuses with exit 2,
   naming it, because no rule here resolves one (§3).
4. **Verification.** `measure_job_children` launches the interpreter the legs will run twice, as a
   leg is launched (steps 2 and 3 of "Launching a leg"), with its output sent to `os.devnull`. That
   interpreter is the resolved one, or PYBIN itself when PYBIN is no alias. One run's `-I -c`
   program starts `sys.executable -I -c pass` and waits for it, and its twin runs `-I -c pass`.
   The two jobs' `TotalProcesses` must differ by exactly 1. Any other difference refuses with exit
   2, naming the interpreter, because no job reading of a leg it runs would be true (§5 risks).
   The step runs on every run, alias or not, so any python whose child leaves a job is refused,
   not only an alias. `TOOL-dRedressedBar-22` makes that child the base interpreter,
   `getattr(sys, '_base_executable', None) or sys.executable`, the rule every fixture follows,
   because a venv's `sys.executable` is a redirector whose child is a second process, so a venv
   PYBIN read a difference of 2 and every profile refused (its S3; closing review round 1, report
   id 3).
5. **Application.** Each leg whose mapped first word was resolved runs the resolved interpreter.
   The legs' environment gains `GOV_PYTHON` set to it, so every `resolve_python` a leg's own
   scripts run picks it before `python3` (`tools/lib/resolve-python.sh:30`, inline at
   `run-gates.sh:142`). A `GOV_PYTHON` the operator set to the alias is overridden the same way.
   It is set before the environment digest is taken, so `env_digest` records it.
6. **Record.** The envelope's `substitutions` holds one object per substitution: `launcher` as the
   manifest or PYBIN spelled it, `alias` and `resolved` as converted paths, and `applied`, which
   names `argv0` and `GOV_PYTHON`. It reads `[]` when nothing was substituted. `interpreter_probe`
   holds the interpreter step 4 ran and both counts. Each `<i>.json` already carries the argv the
   leg ran. The start prints one line per substitution,
   `measure-legs: SUBSTITUTED <launcher> <alias> -> <resolved>`, and the summary line repeats the
   count.

**What it cannot see.** A leg's own code that starts a launcher by name outside `resolve_python`,
or through a caller's override such as `resolve_python "${MAP_PY:-}"` set to an alias, still
starts the alias, and that launch's children leave the job unmarked. A `git grep` at `1f45ba9a`
for `python`, `python3` or `py` at command position in tracked `.sh` files under `tools/` found
one, inside a string a suite prints. A search of `tools/` Python and JavaScript for a list opening
with one of those names found only manifest-shaped test data. Code that spells a launcher another
way is UNVERIFIED.

### The environment a leg gets

**Scrubbed, derived at run time.** The set is every variable whose name starts `GATE_`, the names
`git rev-parse --local-env-vars` prints, and the names on `.githooks/pre-push`'s `unset GIT_…` line
(`:100`) when that file exists. No `GATE_` name is exempt. The two the runner exports to its legs
for nesting, `GATE_TURNSTILE_HOLDER` and `GATE_TURNSTILE_HELD` (`run-gates.sh:1875`, `:1885`, `:1961`,
`:2092`), go with the rest. The profile holds no turnstile (F1), so an inherited holder nonce would
nest a leg's bar under some other holder rather than queue it. Every name in
`BAR_SCRUBBED_KNOBS` (`pre-push:1839`) and in the loops at `:1861` and `:1869` starts `GATE_`. The
git list holds every pointer on `:100` except `GIT_NAMESPACE`, which the hook line contributes.
`GIT_EXEC_PATH` stays, for the hook's reason at `:98`. A refused `git` call leaves that half
unarmed, and the tool says so rather than printing an empty set. The tool prints, and records,
each name it scrubbed and the rule that matched it. It never records a value.

**Added, as the runner adds.** A scratch dir is made once by
`mktemp -d "${TMPDIR:-/tmp}/gate-profile.XXXXXXXX"` in the resolved bash. `TMPDIR` is its `tmp/`,
so a leg sees the spelling the runner's `export` at `run-gates.sh:2272` gives it. Each leg's raw
capture is its `raw/<i>.out`, beside it, as the runner's raw sits in its scratch, and it lives only
until its redacted copy is written (§4 "The record"). It is not under the
git dir, because git discovery from inside `.git/` answers differently, which would change a leg's
verdict. This scratch is the one path outside the run directory, and the envelope names it.
`TOOL-dRedressedBar-19`'s S38 writes an `owner.json` into it, naming this run's pid and creation
time, so a later run can prove a dead run's raw captures abandoned and sweep them
(units-16-18 report id 38).
The same bash run prints the dir's `cygpath -m` spelling (S15). Python opens only that spelling,
and a spelling that `os.path.isdir` rejects refuses the run with exit 2. The envelope keeps both,
`scratch` for the converted one and `scratch_posix` for the one the legs see. The legs also get
`GOV_PYTHON` when S14 resolves an alias, and nothing else is added.

**Recorded, never scrubbed.** These are the names the runner's reuse digest calls verdict-relevant:
`GATE_*|GOV_*|*_PY|GIT_*|PYTHON*|LC_*|LANG|TZ` (`run-gates.sh:3404`, read from its `# digest-env-names`
line). `PATH` is recorded too. Each is stored as its name and the first 12 hex of the SHA-256 of its
value. So are each leg launcher's resolved path, `bash --version`'s first line, PYBIN with its
version, `git version`, and `core.autocrlf` and `core.eol`. Every leg of a run gets one environment
by construction, and two runs are comparable by these digests. What this cannot see, as the runner
says of its digest, is a variable outside the class that a leg reads.

### The turnstile (F1, resolved b)

The profile takes no ticket and holds no slot. Its legs get no nesting name (above), so a bar nested
in a leg takes a ticket on the host turnstile as any bar does (`run-gates.sh:1886-1892`), and it
queues behind whatever holds the host. That is another session's bar, or under `--concurrent` a
sibling leg's bar. Another session's bar can also hold the host while a leg runs. Neither is
prevented. Both are recorded per leg, and the record is shaped so that `derive-ceilings.py` sets
such a reading aside by the rule it already applies.

**What is read.** The key is the one the legs' bars resolve. The scrub removes `GATE_TURNSTILE_DIR`,
so that key is the runner's default, `$HOME/.gov/gate-turnstile` (`run-gates.sh:1513-1514`).
`resolve_turnstile_dir` resolves it once at start, by the runner's own expression in the resolved
bash, and the same run prints its `cygpath -m` spelling (S15). Every read below opens that
spelling, and the envelope keeps both, as `turnstile_dir` and `turnstile_dir_posix`. At each
census tick, after the scan returns, `read_turnstile` lists `gate-bar-queue/` and reads
the `pid` file of each slot beacon: `gate-bar-beacon` and every `gate-bar-beacon.<k>`
(`:1534-1535`, `:1951`), by the glob the nesting test uses (`:1834`). A ticket's name is
`<UTC stamp>-<pid>-<random>` (`:1892`), and its pid is taken as `unattended.sh:6687-6688` takes it.
Both kinds of pid are MSYS pids, which census rows carry as `msys_pid`. No read spawns, and nothing
is written. An absent key or queue reads as empty, because the runner creates both on first use. A
key that exists and cannot be read is a refused read. `TOOL-dRedressedBar-19` states two rules
this paragraph leaves out. A key whose conversion fails, or prints no drive-letter spelling,
resolves to no key, so every tick is a refused read and never an empty one (its S11). An entry
gone between the listing and the read, or whose `pid` is absent, empty or not a number, is not
judged at that tick, and only a failure to list the queue or to stat the key is a refused read
(its S36; units-16-18 report ids 11 and 36).

**Attribution**, by `derive_leg_turnstile` against the scan of the same tick. A pid in a running
leg's `build_walk` set belongs to that leg. A pid in another row is foreign. A pid the scan did not
see is not judged at that tick.

- A slot holder that belongs to no running leg is someone else holding the host. Each running leg
  counts it in `ts_holders`, the distinct foreign holder pids seen in its window. A holder in a
  sibling leg is this profile's own neighbour, as a bar's neighbours are its own
  (`run-gates.sh:2912-2913`), and is not counted.
- A ticket that belongs to a leg and is seen at two consecutive census ticks is that leg's bar
  waiting in the queue. An uncontended acquire holds its ticket only for the few processes of one
  attempt (`run-gates.sh:1996-2000`), so one sighting is not a wait. The leg's `ts_queued` counts
  such tickets. Its `ts_wait_s` is the length of the union of their intervals, each from the stamp
  in the ticket's name to its last sighting.

**Wait apart from work.** A `--concurrent` reading of a leg that runs bars includes their queue wait
in `wall_s`. With no hold to nest under, those bars queue behind each other and behind any sibling's
bar. `ts_wait_s` is that wait, and `work_s`, which is `wall_s - ts_wait_s`, is the rest.
`ts_wait_s` under-counts by up to one census period per ticket, and the stamp truncates to the
second.

**Set aside.** The `.leg` row's eighth field is `foreign + ts_holders + ts_queued`. It reads
`unknown` when the census or the turnstile read was refused at any tick of the leg's window. So a
reading taken while foreign gate work ran, while someone else held the host, or while the leg's own
bar waited reads positive, and `read_runs` sets it aside as `contended`
(`derive-ceilings.py:290-306`). AC15 runs that function over the rows. The three counts stay apart
in `<i>.json`.

**What this cannot see.** A bar on another turnstile key: an operator's own `GATE_TURNSTILE_DIR`,
the private key a suite exports for its own bars (`run-gates.evidence.test.sh:154`), or the
common-dir fallback a runner takes when the host dir cannot be made (`run-gates.sh:1518-1519`). A
wait shorter than one census period. A holder or waiter that came and went between scans.

**No hold, so no preflight.** The regen preflight that a hold runs (`run-gates.sh:1416-1452`) does
not run. A stale generated output reds the legs that grade it, and the record carries them as `fail`.

### Sampling, admission and its cost

The main loop ticks every `HOST_EVERY_S = 1` s, a declared constant. Each tick reads `GetSystemTimes`
(busy = 100 x (kernel + user - idle) / (kernel + user) over the interval) and
`GlobalMemoryStatusEx.dwMemoryLoad`, then queries each running job. Neither read spawns. In
`--concurrent`, `check_admit(cpu, mem, running, fresh)` admits one leg when `fresh` holds, meaning
the newest sample was taken after the previous admission, and that sample reads at or under both
caps. It also admits when no leg of the run is running, the `drained` release of the runner's
memory pause (`run-gates.sh:566-569`). So foreign load can delay a profile and never deadlock it.
`TOOL-dRedressedBar-22` makes `check_admit(mode, pending, running, cpu, mem, fresh)` the loop's one
admit decision, called at the host tick and at the drained site, where the loop tested
`pending and not running` itself and the function's drained clause was unreachable; a drained
admission taken at a host tick is then logged on that tick's `host.tsv` row (its S6; closing review
round 1, report id 6).
**One admission costs** at least one tick, plus one suspended bash spawn, a job assign and a thread
resume. A manifest of N legs takes at least N seconds to ramp, DERIVED from N at run time.

Every `--census-every` seconds (default 5, bounded 1 to 3600) one worker thread runs
`scan_processes()`. A scan slower than the period lowers the rate and never stacks. The same tick runs
the runner's `measure_spawn_cost 3` from its source text (`run-gates.sh:3762-3776`), one bash process
timing three `true` spawns. Its `read_spawn_floor` (`:3739-3754`) runs once at start. The same tick
then runs `read_turnstile` (§4 "The turnstile"), a directory listing and one small read per slot.
Each scan's own seconds are recorded, so the observer's cost is visible.

### Stall detection

At each census tick k, for each running leg, let j be the newest earlier tick with
t_j <= t_k - W, where W is `--stall-window` (default 300 s, bounded 2 x the census period to
86400). The test has three inputs:

- **tree delta**: the sum, over the rows `build_walk(rows_k, root)` returns, of cpu_s at k minus
  cpu_s at j, taken as 0 for a process j did not see. A row with `cpu_s` None makes the tick
  unjudgeable.
- **job delta**: the job's user plus kernel time at k minus at j. It is exact and includes every
  short-lived process.
- **log**: the capture file's size at k against at j.

STALLED holds when both deltas are under C, `--stall-cpu` (default 1.0 s, bounded above 0 and to
3600), and the log size is equal. W and C are declared bounds, not measurements. A leg sleeping
deliberately longer than W reads STALLED, and the record says so. So does a leg whose bar waits in
the host queue longer than W, because a waiting runner sleeps between polls (`run-gates.sh:2086`)
and prints only when its position moves (`:2045`). The episode therefore records the leg's waiting
tickets seen in its window, so a queue wait reads as one and not as a hang.

The first STALLED tick opens an episode. It prints
`measure-legs: STALLED  <leg>  (<W>s: job +<x>s, tree +<y>s, log <n> B unchanged)` and records the
tree: winpid, msys_pid, ppid, age, cpu_s, its delta, mem_b and the redacted command. The record also
carries the window's churn, the job's `TotalProcesses` delta, which is context only. The first tick
that fails the test closes the episode with a `RESUMED` line, and the leg's end closes it as `ended`.
Nothing signals any process. `classify.py`'s verdicts are not consulted: they grade age against the
ceiling this tool removes (`classify.py:38-49`).

**Why the job veto.** The brief's census-only test reads near zero for a silent leg that works only
through children shorter than a scan. The job delta sees them. The canary's hang was blocked on a
FIFO while a sampler spawned `sleep 60`, a few spawns per window, so it should stay under C on both
counts. The CPU of one such spawn is UNVERIFIED, and AC6's fixture is where it is observed.

### The foreign census

`measure_foreign(rows, tokens, own)` is the runner's predicate at `run-gates.sh:4220-4245`, applied to
the census population. Its tokens are the two runner paths and every argv word carrying `/` and ending
`.sh`, `.py` or `.js`, as at `:2924-2933`. A word ending `.test.sh` or `selftest.py` also matches. The
profiler's own ancestors (`build_self_chain`) and descendants are excluded, and a tree counts once, at
its topmost match. The census also sees native rows that `ps -ef` cannot, so its population is wider
than the runner's. The predicate is the same, and AC8's arm runs the runner's awk program from its
source beside the port over one snapshot. A leg's `foreign` is the largest count over the ticks in
its window, or `unknown` when one of them was refused.

### The census fields (process-monitor)

`_CIM_QUERY` (`census.py:52-58`) gains `PeakWorkingSetSize` and `WorkingSetSize`, before the command
line, so free text stays last. `parse_cim` and `build_windows_rows` carry them as `peak_mem_b` and
`mem_b`, int or None, and never zero for unreported, as `cpu_s` is (`census.py:12-22`). The builder
measured the CIM units on node d on 2026-10-15 (set-aside record). `PeakWorkingSetSize` is KiB, 78232
beside `Get-Process` `PeakWorkingSet64` 76533760 bytes, so `peak_mem_b` is that value times 1024.
`WorkingSetSize` is already bytes. POSIX rows carry None. `FIELDS` (`:264`) and
`render_rows` keep their bytes, so `census.py --print` and every reap and classify line are
unchanged. process-monitor's version moves, with every marker that `kit version markers` reads.

`test_row_contract_is_complete` (`tools/process-monitor/selftest.py:102-110`) asserts each row's
key set equals `FIELDS` exactly, so it reds the moment rows gain the two keys. It changes in the
same commit, to `FIELDS` plus the two keys, as the set-aside diff has it. `TOOL-dRedressedBar-19`'s
S10 then states the pair once as `OPTIONAL_FIELDS`. This paragraph gives no rule for a line of
four to six fields, which `parse_cim` as built reads with its command lost to the memory fields;
that unit's S10 reads such a line as the legacy shape, its command at `parts[4]`, and keeps one
five-field fixture line (units-16-18 report ids 10 and 33).

### The record

`<git-dir>/gate-profile/<run id>/`, mode 700. The id has the runner's shape
(`run-gates.sh:1456`), and `--out <root>` moves the root. Nothing prunes it. The runner's sweep at
`run-gates.sh:5658` keeps only five entries of `gate-run/`, which is why the record does not live
there.

| File | Written | Holds |
|---|---|---|
| `envelope.json` | at start, rewritten tmp-then-rename at end | the run |
| `host.tsv` | each tick | epoch ns, cpu %, mem %, running count, event (`admit <i>`, `end <i>`) |
| `census.tsv` | each scan | epoch, foreign count or `unknown`, roots as `pid:token`, scan s, spawn us, slot holders as `pid:<i>` or `pid:foreign`, tickets as `<name>:<i>` |
| `<i>.leg` | leg end | the runner's row: name, status, rc, seconds, started ns, ended ns, key `-`, foreign (`run-gates.sh:3936-3939`), the eighth field as §4 "The turnstile" sets it |
| `<i>.log` | leg end, and again at run end or at an interrupt for a leg that left processes running | the capture, redacted, the only copy kept (F2) |
| `<i>.json` | leg end, rewritten at run end, and at an interrupt for a leg whose capture it retried | the full profile below |
| `legs.tsv` | leg end, rewritten whole at run end and at an interrupt | one row per leg, headed, the table source; each row rendered from that leg's final `<i>.json`, in index order (`TOOL-dRedressedBar-22` S9, report id 9) |

**The raw capture is deleted (F2, resolved b).** It holds the same bytes as `<i>.log` unredacted,
which the runner calls "a credential leak the old scratch-dir lifetime was merely hiding"
(`run-gates.sh:3922-3925`). `<i>.log` is written at leg end. When the job's `ActiveProcesses` read 0
at the root's exit, no leg process still writes the capture, and it is deleted then. Otherwise it
stays until run end, where `<i>.log` is rewritten from it and it is deleted. A delete that fails
because a process still holds the file keeps it, and the envelope's `raw_kept` names it with its
reason. An interrupt keeps each running leg's capture the same way, with the reason `interrupted`.
`TOOL-dRedressedBar-22` has an interrupt also run the run end's retry, `write_final_capture`, over
each ended leg, so a capture an ended leg's processes still hold is named with a reason opening
`interrupted; `, and an interrupt names every kept capture (its S2; closing review round 1, report
ids 2 and 14).
These are the only deletes the tool performs. They cover a leg end, a run end and an interrupt
only: an unhandled exception, a kill or a power loss leaves every capture unredacted and unnamed.
`TOOL-dRedressedBar-19`'s S38 has the next run redact and delete those once it proves their owner
dead, naming each in `raw_recovered`. Its S39 states the byte contract `<i>.log` already meets as
built: the capture is read as bytes and written byte for byte but for the masked spans, and
`log_bytes` is the raw size. A leg whose launch failed records its `launch_error` under its S35
(units-16-18 report ids 35, 38 and 39).

**Per leg (`<i>.json`, and `legs.tsv` less `procs` and `stalls`):**

| Field | Source | Why it earns its place |
|---|---|---|
| `wall_s`, `started_ns`, `ended_ns` | resume stamp, root `ExitTime` | the duration, on the kernel's clock |
| `rc`, `verdict` | root exit; `ok` or `fail` | the runner's status vocabulary |
| `user_s`, `kernel_s` | job accounting | process creation and I/O land in kernel time |
| `procs_total`, `active_peak`, `left_running` | job `TotalProcesses`, max sampled `ActiveProcesses`, `ActiveProcesses` at root exit | the spawn count; fan-out against serial churn; leaks the runner reaps only at a ceiling |
| `peak_job_mem_b`, `peak_proc_mem_b` | job extended limit info | peak commit, short-lived processes included |
| `avg_ws_b` | time-weighted mean of the tree's summed `mem_b` | the average, over the processes the census saw |
| `io` | job `IO_COUNTERS` | read, write and other ops and bytes, which nothing measured before |
| `spawn_us` min/median/max, `spawn_s_est`, `spawn_share` | ticks in the window; `procs_total` x median; over `wall_s` | the spawn claim, per leg. It is MSYS-spawn priced, which is high for a native child |
| `procs` | census walk | per process: winpid, msys_pid, ppid, redacted command, first and last tick seen, start (tick - age), last cpu_s, max `peak_mem_b` |
| `unseen` | `procs_total` - `len(procs)` | the census's blind spot, as a count |
| `foreign` | the census, max over the window | foreign gate work beside the leg, one of the three counts the `.leg` row's eighth field sums |
| `ts_holders`, `ts_queued` | the turnstile read, attributed by the census | someone else holding the host; the leg's own bars waiting in the queue |
| `ts_wait_s`, `work_s` | union of the waiting tickets' intervals; `wall_s - ts_wait_s` | the queue wait kept apart from the work, which a concurrent reading of a nesting leg needs |
| `host_cpu`, `host_mem` | mean and max over the window | the load the reading ran under |
| `queued_s`, `concurrency` | admission | why a concurrent reading differs from a serial one. `queued_s` is the profile's own admission wait, not the turnstile's |
| `ceiling`, `share`, `over_ceiling` | manifest; `wall_s / ceiling` | a ceiling argued from a reading no ceiling cut |
| `stalls`, `log_bytes`, `job_final` | episodes; capture size; job re-read at run end | the report; output volume; orphans' work after the root exited |

**The envelope** carries `profile_bar.py`'s keys where they apply (`profile_bar.py:468-492`): `run`,
`at`, `sha`, `host`, `width`, `width_source`, `full` (always true), `wall`, `exit`,
`failed_legs`, `env.quiet` and `env.quiet_detail` (`check_quiet`), and `regime` (`derive_regime`).
Width is 1 under `--serial` and the peak concurrency under `--concurrent`. `queued` does not apply:
the profile takes no ticket, and each leg's turnstile wait is its own `ts_wait_s`. The ledger keys
do not apply either, because this tool writes no ledger. It adds `mode`, the caps, the periods, W and
C, `scrubbed`, `env_digest`, `tools`, `scratch`, `scratch_posix`, `turnstile_dir`,
`turnstile_dir_posix`, `substitutions`, `interpreter_probe`, `raw_kept`, the manifest path and
blob, the leg count, `census_backend`, `spawn_floor_us`, the kit version and `regimes`. `regimes` is `derive_regime` at every power of two
up to the logical core count: the width profile, read off unbounded durations. It is labelled with
the mode.

**derive-ceilings.** Its readings are admissible: a serial `ok` reading whose `.leg` eighth field
reads 0 is the uncut duration that `--observed` exists to carry (`derive-ceilings.py:40-63`). That
field reads 0 only when the census found no foreign gate work, no one else held the host, and none
of the leg's bars waited, which is the reading `read_runs` admits. A positive or `unknown` field is
one `read_runs` sets aside, and AC15 observes that with `read_runs` itself. `--observed` is the one
route `derive-ceilings.py` does not census (`:49`), so only a row whose eighth field reads 0 is
carried there. They enter as `--observed '<leg>=<s>' --how 'measure_legs <run id>'`, so each row
names its provenance. A run whose `substitutions` is not empty measured the resolved interpreter
and not the alias the bar runs, so its readings lack the alias's own process per launch. The help
page says so, and says to write `substituted` into such a row's `--how` text. The tool
does not feed `read_runs` (`:199`, `:267`), because the record sits outside `gate-run/`, and an
automatic second source would let one profile raise ceilings unseen.

**Exit:** 0 when every leg ended and every record was written, whatever the legs' verdicts. 2 on a
refusal before the first leg. 1 when a record write failed, naming it. 130 on an interrupt, which
writes the envelope, with every kept capture in `raw_kept`, a running leg's and one an ended leg's
processes still hold, as `TOOL-dRedressedBar-22` has it (report ids 2 and 14), and leaves the legs
running. A console Ctrl-C still reaches them, as it reaches a bar's legs.

### The selftest and its leg

`--selftest` runs the tool in-process over fixture manifests under
`tools/run-gates/fixtures/measure-legs/`, writing to a temp `--out`. It prints one line per arm and
`PASS (<n> assertions)`. The fixtures are `spawn.py <n> <hold_s>`, which starts n children of
`sys._base_executable -I -c` sleeping hold_s; `memio.py <mb>`; `hog.py <s>`, which runs one busy
child per logical core; `stall.sh <s>`, which blocks opening a FIFO while a loop spawns `sleep 1`,
and a delayed writer frees it; `steady.py <s>`, which is silent and busy; `churn.py <s>`, which is
silent and spawns `-c pass` children back to back; `printenv.py`, which prints variable names,
never values, then one URL carrying a planted credential; and `queued.sh`, which runs the real
runner's hold verb over `true` from the top level, with `GATE_REGEN_CHECK=0` set inside it. There
are four manifests, `serial.json`, `concurrent.json`, `stall.json` and `turnstile.json`, with
`{prefix}`-spelled argvs. The selftest runs at `--census-every 1 --stall-window 8 --stall-cpu 0.5`.
The turnstile arm sets `HOME` to a temp dir, so its key is private, and starts the real runner's hold
verb over `sleep 20` outside any leg before it runs `turnstile.json`. That holder runs in the legs'
scrubbed environment, which holds no `GATE_REGEN_CHECK`, so it runs the regen preflight before it
holds; unit 18 bounds the wait for its beacon at 120 s inline. `TOOL-dRedressedBar-19`'s S12 sets
`GATE_REGEN_CHECK=0` after the scrub, as `queued.sh` does, and moves the bounded wait into
`read_hold_beacon` (units-16-18 report id 12). The pure arms are the scrub
derivation, `check_admit`, the platform refusal and the foreign parity, and that unit adds the
redaction parity against the runner's `redact` (its S20, report id 20) and the fork fixture
`forks.sh` (its S32, report id 32). Every fixture ends by
itself. The alias halves, AC1 and AC2's resolution red half and AC16's alias half, need a host
whose PYBIN is an App Execution Alias. On any other host each prints
`unexercised: no alias on this host` and adds no assertion, so a pass there says nothing about an
alias. The interpreter verification of S14 and the path arm of AC17 run on every host.
`TOOL-dRedressedBar-22` has `memio.py` print `memio: wrote <mb> MiB` once its write is synced,
which the resolution red half reads beside each leg's verdict (its S15; closing review round 1,
report id 15).

The leg row:

```json
{"name": "measure-legs selftest",
 "argv": ["python3", "{prefix}/run-gates/measure_legs.py", "--selftest"],
 "chunk": "selftests", "subject": "kit", "guard": ["..."], "ceiling": "<c>"}
```

The guard lists `measure_legs.py`, `profile_bar.py`, `run-gates.sh` and the
`fixtures/measure-legs/` dir under `{prefix}/run-gates/`, plus `census.py`, `reap.py` and `scope.py`
under `{prefix}/process-monitor/`. Those are the files whose text it reads or imports, less three
the guard omits: `{prefix}/run-gates/derive-ceilings.py`, whose `read_runs` the turnstile arm
loads, `.githooks/pre-push`, whose `unset GIT_…` line the scrub reads, and
`{prefix}/run-gates/held_halves.py`, which `TOOL-dRedressedBar-19`'s S19 makes the tool import.
That unit's S21 adds all three (units-16-18 report id 21). `TOOL-dRedressedBar-25` folds the
run-gates entries into `{prefix}/run-gates/`, and `{prefix}/gate-legs.json` joins the guard (closing
review round 2, report ids 4, 11, 20 and 23). The ceiling
`<c>` is `max(r + 120, 2r)`, rounded up to 10 s, where r is the direct-invocation reading at
build. That clears `ceiling-margin.txt`'s rule. The kit.toml `[[gate_leg]]` row uses `{kit}`, with
the same name, subject and argv, as `govkit.py:2750-2830` requires. The budget row is r x 1.5, floored
at 60, by the file's own rule. Both figures are PINNED with node and date in their rows. The
descriptor row ships the leg to adopters with a process-monitor sibling and a Windows host its
`requires` does not declare; `TOOL-dRedressedBar-19`'s S29 withdraws it for an `[[exempt_leg]]`
row and withholds the fixtures as `project-owned` (units-16-18 report id 29).

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `main`, `cmd_selftest` | functions | `py.function`, `main` and `cmd` are reserved verbs |
| `read_legs`, `read_local_env_vars`, `read_host_load`, `read_job_accounting`, `read_turnstile` | functions | `py.function`, `read`. `read_legs` shares its name with `derive-ceilings.py`'s reader, and `TOOL-dRedressedBar-19` renames it `read_profile_legs` (its S19, units-16-18 report id 19) |
| `derive_scrub_set`, `derive_redacted`, `derive_leg_turnstile` | functions | `py.function`, `derive` |
| `extract_runner_function` | function | `py.function`, `extract` |
| `resolve_leg_python`, `resolve_job_backend`, `resolve_turnstile_dir` | functions | `py.function`, `resolve` |
| `resolve_launcher_aliases`, `resolve_alias_interpreter` | functions | `py.function`, `resolve` |
| `measure_spawn_us`, `measure_foreign`, `measure_job_children` | functions | `py.function`, `measure` |
| `check_admit`, `check_stalled`, `check_app_alias` | functions | `py.function`, `check` |
| `run_leg`, `build_job`, `scan_leg_trees` | functions | `py.function`, `run`, `build`, `scan` |
| `write_leg_record`, `render_leg_row` | functions | `py.function`, `write`, `render` |
| `test_*` | selftest arms | `py.function`, `test` |
| `HOST_EVERY_S` | constant | none declared for constants |
| `peak_mem_b`, `mem_b` | census row keys | none |
| `substitutions`, `interpreter_probe`, `scratch_posix`, `turnstile_dir_posix` | envelope keys | none |
| `measure-legs selftest` | gate leg | none |

Every name above answered OK under `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
on 2026-10-14, and the four rev-4 functions on 2026-10-15. A name the builder adds is asked the
same way.

### Files touched (estimate)

`tools/run-gates/measure_legs.py` · `tools/run-gates/fixtures/measure-legs/` ·
`tools/run-gates/kit.toml` · `tools/run-gates/run-gates.sh` · `tools/run-gates/README.md` ·
`tools/run-gates/selftest-budgets.txt` · `tools/run-gates/windows-only-legs.txt` ·
`tools/gate-legs.json` · `tools/process-monitor/census.py` · `tools/process-monitor/selftest.py` ·
`tools/process-monitor/adopt-process-monitor.sh` · `tools/process-monitor/reap.py` ·
`tools/process-monitor/scope.py` · `tools/process-monitor/classify.py` ·
`tools/process-monitor/procmon-hook.js` · `tools/process-monitor/README.md` ·
`memory/map/features/run-gates.md` · `help/measure-legs.md` · `help/README.md` ·
`memory/guides/SESSION-KICKOFF.md`, plus the outputs `regen.py --write` moves, which the pass
commits.

`run-gates.sh` moves by `KIT_RUN_GATES_VERSION` and its history comment. The process-monitor engine
files move by their markers only, except `census.py`. Both kits move to the next minor over whatever
the tree carries when this unit builds, DERIVED then.

`memory/guides/SESSION-KICKOFF.md` watches `tools/gate-legs.json` and `tools/run-gates/run-gates.sh`
(its `watch:` line, `:6`). The pre-commit hook runs the kickoff ratchet's staged leg
(`.githooks/pre-commit:191`), which refuses a commit staging a watched file without a
`last-audit:` re-stamp. So the pass commit carries that re-stamp with a `manifest-audit:` line in
its body, as unit 17's `6057a55c1` did. This unit makes no second re-stamp commit:
`TOOL-dRedressedBar-19`'s S1 keeps its reviewed one, over both units' edits.

### Restoring the set-aside work

The first build's code is kept verbatim in
`build/2026-10-15-build-TOOL-dRedressedBar-18-1-set-aside-work.md`: `measure_legs.py`, twelve
fixtures and a 255-line process-monitor diff. The redispatch restores it from that record and
changes it only where this revision requires:

- S14: the four functions of "Alias launchers", called before the first leg; `derive_leg_argv`
  mapping a resolved first word; `GOV_PYTHON` in the legs' environment before `env_digest`; the
  envelope's `substitutions` and `interpreter_probe`; the start and summary lines.
- S15: `TOOLS_SCRIPT` prints each launcher's `cygpath -m` spelling beside its bash one. The
  envelope keys the record calls `scratch_bash` and `turnstile_dir_bash` are spelled
  `scratch_posix` and `turnstile_dir_posix`, the names `TOOL-dRedressedBar-19` already uses.
- The selftest: the alias halves and the unexercised line of "The selftest and its leg", the AC16
  and AC17 arms, and AC9's PYBIN compared under the scrubbed environment.
- The declarations the first build never wrote: the manifest row, `kit.toml`, the budget and
  Windows-only rows, the runner's version line, both READMEs, the help page, the map claim and
  the kickoff re-stamp.

The process-monitor diff is applied as kept, its row-contract arm included.

### Alternatives rejected

- **ETW, or WMI start and stop traces.** These see every process, but need an elevated token, which
  is a privilege widening that M3's veto 3 sends to the owner. They also run system-wide.
- **Job completion-port notifications.** These give a row for short-lived processes, but they are a
  second process reader the brief bars, and Windows documents their delivery as not guaranteed. The
  job's exact count plus `unseen` states the gap instead.
- **Capture through a pipe.** It is streamable to redact, but closing the read end at exit sends
  SIGPIPE to an orphan still writing, which kills it. A file is what the runner uses
  (`run-gates.sh:3846-3852`) and kills nothing.
- **Records under `gate-run/`.** That would feed `read_runs` for free, but the runner's sweep erases
  all but five entries there.
- **`derive_scope` attribution.** It needs `PROCMON_ROOTS` declared, and the leg's root pid is
  already known exactly.
- **Holding the turnstile for the profile (F1 a).** The owner chose (b) on 2026-10-14. Contention
  is recorded and set aside, not prevented.
- **The printed queue line.** `gate queue: waited <n>s` (`run-gates.sh:2145`) is what
  `profile_bar.py:415` parses from a bar's own stdout. Inside a leg it goes wherever the suite sends
  its bar's output, and the canary captures that into a variable (`run-gates.test.sh:364`), so the
  leg's log never carries it and the wait would read 0. A bar on a suite's private key prints waits
  that are no host contention. The queue itself is read instead.
- **Keeping the raw capture (F2 a).** The owner chose (b) on 2026-10-14.
- **Refusing an alias at preflight (F3 a), or marking its totals `unknown` (F3 c).** The owner
  chose (b) on 2026-10-15. (a) costs every operator with the Store python a `GOV_PYTHON` before the
  first profile, and (c) leaves every reading on node d without a job total.

## 5. Production-readiness checklist

- security — No elevation, no network, no signal. Command lines and logs are written with the runner's
  URL-credential redaction (`run-gates.sh:301`), mode 700 and 600, under the untracked git dir. Each
  leg's unredacted capture is deleted once its redacted copy is written (F2), and one it cannot
  delete is named in `raw_kept`. The turnstile is read, never written.
  Environment values are stored only as digests. Flags are bounded at parse, so an over-long value
  refuses with exit 2. The process handle asks for `PROCESS_TERMINATE` only because the job assign
  requires it, and the code never calls a terminate. S14 runs no program the bar would not: the
  resolved interpreter is the very process the alias starts, and it is accepted only as a file that
  is no alias and that keeps its child in a test job. `TOOL-dRedressedBar-19` carves out one
  terminate, of a root still suspended after a failed open, assign, snapshot or resume, which has
  executed nothing (its S35). The raw-capture delete covers a leg end, a run end and an interrupt;
  a crash, a kill or a power loss leaves captures that its S38 has the next run redact and delete,
  and its S39 and S20 hold the redaction byte-exact and to the runner's (units-16-18 report ids 20,
  35, 38 and 39).
- perf / scale — A scan took about 1 s at 327 rows on node d. A concurrent run has more rows, and
  the scan's own seconds are in `census.tsv`. Host sampling is about 13 µs a tick. The turnstile
  read adds one directory listing and one small read per slot to each census tick, and no spawn.
- error / empty / loading states — An empty manifest refuses with exit 2. A refused scan is an
  `unknown` tick. A missing process-monitor kit or job API refuses at start. So do an unreadable
  launcher file, an alias that is not PYBIN, an alias whose `sys.executable` is no plain file, an
  interpreter whose child leaves the test job, and a scratch dir whose converted spelling is no
  directory. A leg that never ends keeps the run open, which the owner chose.
  `TOOL-dRedressedBar-19` adds the states this list misses: an empty bash resolve refuses naming
  every candidate (its S34), each malformed manifest class refuses naming its row (S37), a failed
  launch records the leg as `fail` and the run continues (S35), a turnstile key that does not
  convert is a refused read at every tick (S11), and a half-written beacon or a vanished ticket is
  not judged (S36; units-16-18 report ids 11, 34, 35, 36 and 37).
  `TOOL-dRedressedBar-22`'s `test_alias_refusals` drives each of the four alias refusals above, the
  unreadable launcher, the alias that is not PYBIN, the alias whose `sys.executable` is no plain
  file and the interpreter whose child leaves the test job, which no arm reached before (its S11;
  closing review round 1, report id 11).
- observability — The scrubbed set, each substitution, the turnstile key and the record path print
  at start. Each leg
  prints one line as it ends, naming its `ts_wait_s` and `ts_holders` when either is above zero, and
  each STALLED or RESUMED prints one line. A summary line gives the totals, including the
  summed `spawn_s_est` over the summed wall.
- risks — AC1 ran on 2026-10-15 and failed through an App Execution Alias, and this rule parked the
  unit. The rule now holds at run time: an interpreter whose child leaves the test job refuses the
  run rather than shipping a census-only count (S14). The alias's own process per launch, and the
  activation work it does, are in no reading of a substituted run, so those readings are not the
  bar's. That is the owner's accepted cost of F3 (b), and `substitutions` says so on every such
  run. A leg that starts the alias outside `resolve_python` still loses that launch's children
  from its job, unmarked (§4 "Alias launchers"). With no hold (F1b), a leg's bars queue behind any bar on
  the host, and another session's bar can run beside the profile. Both are recorded and set aside,
  not prevented, so a busy host yields readings that argue no ceiling. A profile started inside a
  bar queues each of its legs' bars behind that very bar, for up to the runner's `TS_MAXWAIT` each,
  so the help page says to start one outside any bar. The legs' scratch is never swept, so the
  canary's clones can reach gigabytes, and the end line prints its size.
- testing — AC1 to AC17 run against committed fixtures, the real runner's hold verb and pure probes.
  The alias halves need a host whose PYBIN is an alias, node d at 2026-10-15. The new arms are
  declared in §7.
- migration — Census rows gain two keys that default to None. No conf key and no record format
  moves.
- user docs — `help/measure-legs.md`, linked from `help/README.md`, and a run-gates README section.
  The page names `substitutions` and says a substituted run's readings are not the bar's.

## 6. Acceptance criteria

Commands run from the worktree root on node d. `<ml>` is `python tools/run-gates/measure_legs.py`,
`<fx>` is `tools/run-gates/fixtures/measure-legs`, and `<o>` is a fresh dir under `%TEMP%`. `<r>` is
the run dir the tool prints. Every criterion is a direct run of the tool or a probe of its code, and
`--selftest` re-observes them as §7 declares.

- **AC1** — `<ml> --serial --legs <fx>/serial.json --out <o> --census-every 1` runs
  `spawn.py 6 3` and its zero-child twin `spawn.py 0 3`, under the interpreter the envelope names.
  `tools.pybin` is what the runner's `resolve_python` printed. When that is an alias,
  `substitutions` holds one entry whose `resolved` is the first word of both legs' `argv` in their
  `<i>.json`, and `interpreter_probe` reads a difference of 1. On node d at 2026-10-15 PYBIN is
  `python3`, the alias in the user's `WindowsApps` dir, resolved to the `python.exe` of
  `pythoncore-3.14-64` under the user's local `Python` dir. The difference of the two legs'
  `procs_total` in `<r>/legs.tsv` is 6. The spawn leg's `procs` holds 6 rows whose command
  carries `-I -c`, each with ppid, start, first and last seen, cpu_s and `peak_mem_b`.
  Red when: the job is created with `JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK`. The children then leave
  it, so S14's verification refuses the run with exit 2 naming the interpreter, and a copy that
  also skips the verification reads a difference of 0.
  Red when: the resolution is disabled on node d. A python program rebinds
  `measure_legs.resolve_launcher_aliases` to return no substitution and no probe, and calls
  `measure_legs.main` with the same arguments. Both legs then run the alias, and the difference
  reads 0, as the first build read it on 2026-10-15. `TOOL-dRedressedBar-22` has this half first
  read `spawn six` and `spawn none` at verdict `ok`, so the 0 is work done outside the job and not
  legs that never ran (its AC15; closing review round 1, report id 15).
  figure: 6 is the fixture's argument. The twin cancels the wrapper and the interpreter, so the
  expectation is DERIVED. The interpreter paths are PINNED, node d, 2026-10-15.
  fixture: the resolution red half needs a host whose PYBIN is an App Execution Alias, and node d
  is one at 2026-10-15. Elsewhere the rebinding changes nothing, and that half reads unexercised.
- **AC2** — On the same run, under the same interpreter, the `memio.py 200` leg's
  `peak_job_mem_b` is at least 200 MiB, its `io.write_bytes` is at least 200 MiB, and
  `user_s + kernel_s` is above 0. Every leg's
  `spawn_us.median` is above 0, and its `spawn_s_est` equals `procs_total x median / 1e6`.
  Red when: `extract_runner_function` is pointed at a name the runner lacks. The run then refuses
  with exit 2 before the first leg, rather than recording no spawn cost.
  Red when: the resolution is disabled as AC1 disables it. The memio leg then runs the alias, and
  its `peak_job_mem_b` reads under 200 MiB with `io.write_bytes` 0. `TOOL-dRedressedBar-22` has
  this half first read memio's verdict `ok` and the line `memio: wrote 200 MiB` in its `<i>.log`,
  so the 0 is a write made outside the job (its AC15; closing review round 1, report id 15).
  figure: the first build read 6950912 and 0 on node d, 2026-10-15, PINNED.
  fixture: as AC1's resolution red half.
- **AC3** — `python -c` imports `tools/process-monitor/census.py`, feeds `parse_cim` one
  `\x01`-joined line carrying seven fields, and feeds `build_windows_rows` the result. The row carries
  `peak_mem_b` and `mem_b` as ints, and `command` intact. A `parse_posix` row carries both as None.
  `census.FIELDS` is unchanged.
  Red when: `parse_cim` reads the command from index 4 as before. The command then reads as a number.
- **AC4** — `<ml> --concurrent --legs <fx>/concurrent.json --out <o>` runs `hog.py 10`, then
  `steady.py 2`. In `<r>/host.tsv`, no `admit` event sits on a sample above 80% CPU while another
  leg runs, and at least one sample above 80% falls between the hog's admission and the steady
  leg's.
  Red when: `check_admit` compares with the caps disabled. The steady leg is then admitted on the next
  tick, on a sample above 80%.
  fixture: the liveness half fails, and does not pass, on a host where `hog.py` cannot raise CPU above
  80%.
- **AC5** — `python -c` calls `check_admit` at (cpu, mem, running, fresh) = (81, 50, 1, True),
  (80, 90, 1, True), (50, 91, 1, True), (50, 50, 1, False) and (99, 99, 0, False). It gets hold,
  admit, hold, hold and admit. `TOOL-dRedressedBar-22` widens the call to
  `check_admit(mode, pending, running, cpu, mem, fresh)`, these five rows becoming the first five
  of eight under `concurrent` with `pending` 1, and adds a loop half: over a serial run, each call
  returning True has `running` 0, one per leg, and none returns True while a leg runs (its AC6;
  closing review round 1, report id 6).
  Red when: the drained clause is missing, so (99, 99, 0, False) holds.
- **AC6** — `<ml> --serial --legs <fx>/stall.json --out <o> --census-every 1` with
  `--stall-window 8 --stall-cpu 0.5` runs `stall.sh 20`. Its `stalls` holds one episode whose tree
  names `sleep`, and stdout carries `STALLED`. `steady.py 20` holds none, and the run ends with
  every leg's `rc` 0.
  Red when: the log test is inverted. Then `stall.sh` never reads STALLED.
- **AC7** — On the same run, `churn.py 20` holds no episode. At least one of its windows records a
  tree delta under 0.5 s with a job delta above it.
  Red when: the job veto is dropped from `check_stalled`. `churn.py` then reads STALLED.
  fixture: if no window has a tree delta under 0.5 s, the arm reports the veto unexercised and does
  not pass.
- **AC8** — `--selftest`'s parity arm builds one `ps -ef`-shaped snapshot of six rows. It runs the awk
  program `extract_runner_function` takes from `measure_foreign`, with `ps` shimmed to print the
  snapshot, and runs `measure_foreign` over the same rows. Both give the same count and the same
  roots.
  Red when: the port drops the `selftest.py` word rule, and the counts differ.
- **AC9** — `GATE_JOBS=3 GATE_REUSE=1 GATE_TURNSTILE_HOLDER=probe GIT_NAMESPACE=probe <ml> --serial`
  with `--legs <fx>/serial.json --out <o>` runs `printenv.py`.
  Its `<r>/<i>.log` prints no `GATE_` name, the two nesting names included, and no name from
  `git rev-parse --local-env-vars`. `envelope.json` `scrubbed` lists `GATE_JOBS`, `GATE_REUSE`,
  `GATE_TURNSTILE_HOLDER` and `GIT_NAMESPACE`, each with its rule. The envelope's PYBIN equals what
  the runner's `resolve_python` prints under the scrubbed environment, before S14 sets
  `GOV_PYTHON`.
  Red when: the pre-push half is skipped. `GIT_NAMESPACE` then reaches the leg.
- **AC10** — After AC1's run exits, `<r>` holds `envelope.json`, `host.tsv`, `census.tsv`,
  `legs.tsv`, and one `.leg`, `.log` and `.json` for each leg. Each `.log` is the leg's redacted copy,
  the only log the run keeps. Every `.leg` line splits on tab into 8 fields with a numeric fourth.
  The `scratch` dir the envelope names still exists.
  Red when: an exit handler erases the run dir, as the runner's `cleanup` erases its scratch. The
  listing is then empty.
- **AC11** — On AC9's run, `printenv.py` also prints `https://u:s3cret@example.invalid/x`. Its
  `<i>.log` carries `://***:***@`. With `<s>` the `scratch` dir the envelope names,
  `grep -r s3cret <r> <s>/raw` prints nothing, `<s>/raw/` holds no file, and the envelope's
  `raw_kept` is empty.
  Red when: the log is copied without redaction, or the raw capture is left in place. Either way
  `grep` finds `s3cret`.
  fixture: `printenv.py` leaves no process running, so its capture is deleted at leg end, and a
  `raw_kept` entry for it is a failure, not an allowance.
- **AC12** — `python -c` calls `measure_legs.resolve_job_backend('linux')`. It raises naming `linux`
  and the job API.
  Red when: it returns a backend.
- **AC13** — A `python -c` probe reads `tools/gate-legs.json`, the run-gates `kit.toml` through
  `tomllib`, `selftest-budgets.txt` and `windows-only-legs.txt`. It finds `measure-legs selftest` in
  all four, with equal name, subject and argv once `{kit}` is resolved to `{prefix}/run-gates`.
  Red when: the descriptor row is left out, which `govkit selfcheck` would red at the close.
- **AC14** — `grep -n 'gov:kit run-gates@' tools/run-gates/README.md` and
  `grep -n '^KIT_RUN_GATES_VERSION' tools/run-gates/run-gates.sh` show one equal version above 1.40.
  The process-monitor markers all show one equal version above 0.18. `help/measure-legs.md` names
  `--serial`, `--concurrent`, the record path, `ts_wait_s`, `substitutions` and `scratch_posix`,
  and `help/README.md` links it.
  Red when: one marker lags, as `kit version markers` would find.
- **AC15** — `<ml> --selftest`'s turnstile arm, with `HOME` set to a fresh temp dir, starts the real
  runner's hold verb over `sleep 20` outside any leg, in the legs' scrubbed environment, and waits
  for its slot beacon's `pid` file. It
  then runs `<fx>/turnstile.json` with `--serial --census-every 1`: `steady.py 3`, then `queued.sh`,
  whose own hold queues behind the first. `steady.py`'s `ts_holders` is 1 and its `ts_queued` 0.
  `queued.sh`'s `ts_queued` is 1, its `ts_wait_s` is at least 5, and its `work_s` equals
  `wall_s - ts_wait_s`. Both `.leg` rows carry a positive eighth field. A third row is
  `render_leg_row` over `steady.py`'s record with `foreign`, `ts_holders` and `ts_queued` set to 0.
  `read_runs`, loaded from `tools/run-gates/derive-ceilings.py` and pointed at a temp
  `gate-run/<id>/` holding the three rows, sets the first two aside as `contended` and admits the
  third.
  Red when: `derive_leg_turnstile` ignores tickets. `queued.sh`'s `ts_wait_s` then reads 0, and its
  `work_s` equals its `wall_s`.
  figure: 5 s is the holder's 20 s, less `steady.py`'s 3 s, less a declared 12 s allowance for two
  runner start-ups, one census period and the stamp's truncation. The allowance is declared, not
  measured, and the arm prints the wait it saw.
  fixture: the holder is the profiler's own child, so the census excludes it, and only the turnstile
  read can count it. The temp `HOME` keeps the arm off the host key a surrounding bar holds.
- **AC16** — A python program imports `measure_legs`. `check_app_alias` returns True for the
  `python3.exe` that `command -v python3` resolves on node d, spelled by `cygpath -m`, and False
  for the program's own `sys.executable` and for a path that does not exist. On AC9's run the
  output carries one line opening `measure-legs: SUBSTITUTED python3`. The envelope's
  `substitutions` entry has an `alias` ending in the WindowsApps `python3.exe`, a `resolved` for
  which `os.path.isfile` reads True and `check_app_alias` False, and an `applied` naming `argv0`
  and `GOV_PYTHON`. `interpreter_probe` holds two counts that differ by 1, and `printenv.py`'s
  `<i>.log` lists the name `GOV_PYTHON`.
  Red when: `check_app_alias` tests `os.path.islink`, which reads False for the alias (measured on
  node d, 2026-10-15). No substitution is made, step 4 then verifies the alias itself, and the run
  refuses with exit 2 naming `python3`.
  fixture: the alias half needs node d's alias as of 2026-10-15. Elsewhere `substitutions` reads
  `[]` and that half reads unexercised, while the two False results and the probe's difference
  still hold.
- **AC17** — On AC1's run, the envelope's `scratch` and `turnstile_dir` each match `^[A-Za-z]:/`,
  `scratch` passes `os.path.isdir`, and `scratch_posix` and `turnstile_dir_posix` each open with
  `/`. On AC15's run, whose key exists under the temp `HOME`, `turnstile_dir` passes
  `os.path.isdir`, which AC15's counts rest on.
  Red when: a copy's start-up scripts print the bash spelling where `cygpath -m`'s belongs. Native
  Python resolves an MSYS spelling against the drive root, where no such dir exists (measured on
  node d, 2026-10-15: `/c/Users` reads as no directory), so the run refuses at start naming the
  scratch dir.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `shell hygiene (a fork spent on builtin work)` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)` · `govkit selfcheck` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `python resolver (behaviour + inline parity + idiom ban)` · `every held leg is budgeted, every budget row resolves` · `held-halves selftest` · `process-monitor census selftest` · `process-monitor adopter selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `kickoff-manifest ratchet` · `measure-legs selftest` · `kit epoch (shipped bytes move, the version moves)` · `foreign-prefix parity (every self-test at three prefixes)`

The line is a floor, derived by joining §4 Files touched against the guards in `tools/gate-legs.json`
with `BROAD_LEG_FLOOR` applied, plus the unguarded and broad-guarded legs the change moves: `kit epoch`
grades both kits' version moves, and the new budget row joins the foreign-prefix parity population
(`TOOL-dRedressedBar-19`, units-16-18 report ids 13 and 25).

New arm: tools/run-gates/measure_legs.py --selftest · covers AC1 AC2 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC15 AC16 AC17 · each criterion's Red when, staged on a copy of the tool in the selftest's temp dir; the alias halves only on a host whose PYBIN is an alias, and unexercised, never passed, elsewhere · none

New arm: tools/process-monitor/selftest.py · covers AC3 · a parse_cim reading the command at index 4, and test_row_contract_is_complete over a row lacking one of the two keys · none

`measure-legs selftest` is the leg the first arm line adds. It joins the manifest in this unit, and
it is named on the leg line above once the manifest row exists, which it does since unit 18's pass
commit `6783992aa`; unnamed, its guard trips on `tools/run-gates/measure_legs.py` in §4 Files
touched (`TOOL-dRedressedBar-19`, units-16-18 report id 27). The inlined `resolve_prefix_token` and `resolve_kit_dir` blocks join
the resolver's parity population by their markers. The main loop observes each arm red, then green,
at the close.

## 8. Open questions

- **F1 — Does the profile hold the host turnstile?**
  (a) Yes, through `run-gates.sh --hold`, with the legs keeping the two nesting names (rev-1's §4 "The
  turnstile"). Nested bars inside legs then nest as they do under a bar, and a real bar queues
  instead of overlapping the profile. The cost is that the profile holds the host for as long as it
  runs, which is unbounded by design, and other bars wait out `TS_MAXWAIT` and then run beside it.
  (b) No. Leg-nested bars queue on the host turnstile. Under `--concurrent` they queue behind each
  other, which inflates exactly the readings this tool exists to make truthful, and a real bar can
  overlap the profile, visible only in `foreign`.
  Recommendation: (a). It removes a contention source that (b) can only record.
  RESOLVED (owner, 2026-10-14): (b). The profile holds no turnstile. A leg's bars queue on the host,
  and each leg's record carries foreign holders, its queue wait apart from its work, and an eighth
  `.leg` field that `read_runs` sets aside (§4 "The turnstile", S9, AC15).
- **F2 — What happens to the unredacted capture once its redacted copy exists?**
  The leg writes its raw output into the scratch dir's `raw/<i>.out`, because a file kills nothing
  (§4 Alternatives). The brief says nothing is erased. The runner's own record says a durable
  unredacted copy is "a credential leak the old scratch-dir lifetime was merely hiding"
  (`run-gates.sh:3922-3925`).
  (a) The raw capture is kept in the scratch dir, and the envelope names it.
  (b) The raw capture is unlinked once `<i>.log` is written and no process holds it. A held file is
  retried at run end and otherwise kept, with `raw_kept` and its reason recorded. This is the one
  erase the tool performs.
  Recommendation: (b). Every log is kept as the runner keeps its durable copies, and charter
  `[security]` outranks the letter of "nothing erased" for a file holding the same bytes unredacted.
  RESOLVED (owner, 2026-10-14): (b). Each leg's log is kept redacted only, and the raw capture is
  deleted once its redacted copy is written (§4 "The record", S11, AC11).
- **F3 — How is a launcher that is an App Execution Alias handled?**
  The first build found PYBIN to be the Store `python3` alias on node d, and every process it
  starts leaves the leg's job, so AC1 and AC2 failed (§4 "Measured on node d, 2026-10-15").
  (a) A preflight runs PYBIN and each distinct launcher once in a test job and refuses with exit 2,
  naming the alias. The remedy is `GOV_PYTHON` set to a plain interpreter, which the runner honours
  too, so the bar and the profile still run one python.
  (b) The alias is resolved to the interpreter it starts, for the legs. The alias's own process per
  launch then drops out of every reading, so the readings are no longer exactly the bar's.
  (c) A per-leg escape check compares the census tree with job membership, and marks the job
  totals `unknown` where they disagree.
  Recommendation: the builder's divergence offered the three options without one, and the fork
  went to the owner as returned.
  RESOLVED (owner, 2026-10-15): (b). The profiler resolves an alias launcher to its real interpreter
  for the legs, and the record names every substitution (§4 "Alias launchers", S14, AC1, AC2,
  AC16).

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from the owner's brief. The seams were read at `ebce889c`, the
  census, spawn-floor, admin, job and host-load probes were run on node d, and §4's candidates were
  graded by M12.
- rev-2 · 2026-10-14 · S1 S8 S9 S10 S11 · §3 · §4 · §5 · AC9 AC10 AC11 AC14 AC15 · §7 · §8 ·
  §10 · the owner resolved F1 (b) and F2 (b), marked in place. F1: the hold, `--inside-hold` and `run_held`
  are gone, and so is `derive_held_env`, because the nesting names are now scrubbed (AC9). S9 and
  §4 "The turnstile" add a read of the host queue and slot beacons at each census tick, attributed
  by the census. They give per-leg `ts_holders`, `ts_queued`, `ts_wait_s` and `work_s`, and fold
  them into the `.leg` row's eighth field, which `read_runs` sets aside (AC15, new). A concurrent
  reading of a nesting leg is stated to include its queue wait. The envelope drops `queued` and
  gains `turnstile_dir`. The printed `gate queue: waited` line was weighed and rejected, because
  the canary captures its bars' output (`run-gates.test.sh:364`). F2: the raw capture is deleted
  once `<i>.log` is written, `raw_kept` names any it cannot delete, and AC10 and AC11 read the
  redacted copies and the empty `raw/`. S1 and S11 each gain a **Readers:** clause for that
  delete, read by grep at `679afc31`: no tracked reader spells the capture's name, and its only
  value reader is this unit's own redaction pass.
- rev-3 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-19`, the batch the
  units-16-18 spec audit's minors were promoted into, for that report's ids 1, 6, 7, 10, 11, 12, 13,
  14, 15, 19, 20, 21, 22, 24, 25, 26, 27, 29, 32, 33, 34, 35, 36, 37, 38, 39 and 42. No scope, design
  or criterion moves.
- rev-4 · 2026-10-15 · §1 · S3 S8 S14 S15 · §3 · §4 · §5 · AC1 AC2 AC9 AC14 AC16 AC17 · §7 · §8 · §10
  · the first build's divergence (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-18-4-revision.md`):
  PYBIN was the Store `python3` alias on node d, whose processes leave the job, so AC1 and AC2
  failed. The owner resolved F3 (b) on 2026-10-15. S14 and §4 "Alias launchers" add the probed set,
  detection by reparse tag, resolution by the alias's `sys.executable`, a twin test-job
  verification that refuses an interpreter whose child leaves, the substitution at argv0 and in
  `GOV_PYTHON`, and the envelope's `substitutions`. AC1 and AC2 name their interpreter and gain a
  red half with the resolution disabled, and AC16 is new. The builder's three notes: S15 takes
  the `cygpath -m` conversion from `TOOL-dRedressedBar-19`'s S11 (AC17, new), which keeps the
  turnstile key's failed-conversion rule; Files touched gains `memory/guides/SESSION-KICKOFF.md`
  for the ratchet's staged re-stamp, and §7 names `kickoff-manifest ratchet`; §4 states that
  `test_row_contract_is_complete` changes in the commit that adds the census keys. §4 records the
  measured CIM units and says the redispatch restores the set-aside record. Claims new at rev-4
  were read at `1f45ba9a`, whose `run-gates.sh`, `census.py` and process-monitor `selftest.py` equal
  `ebce889c`'s. §10's turnstile-suite citation moves from `:1499` to `:1500`.
- rev-5 · 2026-10-15 · S1 S4 S11 S13 · §3 · §4 · §5 · §7 · §10 · a records fix for
  TOOL-dRedressedBar-19, closing the units-16-18 spec audit's report ids 1, 6, 7, 10, 11, 12, 13,
  14, 15, 19, 20, 21, 22, 24, 25, 26, 27, 29, 32, 33, 34, 35, 36, 37, 38, 39 and 42, written by
  that unit's spec-writer pass `<w19>`. The status stays CLOSED. Unit 18 built against its
  criteria as written, at `6783992aa` and `997fc294f`; each corrected paragraph names
  TOOL-dRedressedBar-19 and the change, and that spec holds the design. The criteria named below
  are TOOL-dRedressedBar-19's. Ids 1 and 26 were already true since rev-4: §7 names
  `kickoff-manifest ratchet`, Files touched names the kickoff manifest, and the pass commit carried
  the staged re-stamp, so nothing moves for them; unit 18 owed that re-stamp, whose `last-audit:`
  names `4a4960958`, a manifest with no row for the new leg, and AC1 observes the reviewed re-audit
  over both units. Id 6: §3's first non-goal no longer denies the leg S13 adds (AC6). Ids 7 and 24:
  S13 names AC7 for the README section and the map claim no criterion here read; both stand at
  `997fc294f`. Id 13: §7 names `kit epoch` and says the line is a floor (AC13). Id 14: this spec's
  AC14 asked every process-monitor marker for one version, and
  `tools/process-monitor/adopt-process-monitor.test.sh:4` reads `@0.15` beside nine at `@0.19`, so
  its literal reading could not pass; AC14 scopes the grep to the shipped files. Id 15: S11's
  Readers cite the runner's raw capture, `$WORK/$i$sfx.raw`, at its base line and the tip's (AC15).
  Ids 19 and 37: S1, the Inventory and §10 name the profiler's reader, the two readers §10 missed,
  and the refusals S1 lacks (AC19, AC37). Id 20: S11, §4 "The selftest and its leg" and §10 name the
  redaction's parity arm (AC20). Ids 21, 22, 25 and 29: S13 and §4 name the three guard files, the
  subject pin, the `WHOLE_RUN` row and the `[[exempt_leg]]` declaration; at `997fc294f` the pin and
  the row are absent and the descriptor row stands, and this spec's AC13, which reads the
  descriptor, no longer holds once S29 lands (AC21, AC22, AC25, AC29). Id 27: §7 names
  `measure-legs selftest` now that its row exists (AC27). Ids 10 and 33: S4 and "The census fields"
  name the legacy-line rule and `OPTIONAL_FIELDS`; AC3 read a seven-field line only (AC10). Id 11:
  "The turnstile" names the failed-conversion rule (AC11). Id 12: "The selftest and its leg" names
  the holder's preflight and the beacon wait; AC15's holder ran without `GATE_REGEN_CHECK=0` (AC12).
  Id 32: the candidates row says AC1 covers the native-spawn path only (AC32). Ids 34 to 36: "Launching
  a leg", "The turnstile" and §5 name the one bash, the launch-failure branch and turnstile churn
  (AC34, AC35, AC36). Ids 38 and 39: "The environment a leg gets", "The record" and §5 name the
  sweep of a dead run's captures and the byte contract, which `write_leg_capture` already meets
  (AC38, AC39). Id 42: this spec's AC6 matched `STALLED` over the whole stdout of a three-leg run,
  so a STALLED line naming a sibling would have passed it; AC42 reads the line by its leg. Runner
  lines this pass cites are at the base `ebce889c`, the tip's named beside them where they moved.
- rev-6 · 2026-10-15 · §3 · a records fix for TOOL-dRedressedBar-21, which closes the round-1
  closing diff review's H1 (report id 1) and, by the owner's ruling of 2026-10-15, the same class at
  a leg's own capture, written by that unit's spec-writer pass `<w21>`. The status stays CLOSED.
  §3's Edges gain the hands-off to TOOL-dRedressedBar-21: `write_atomic`'s fixed `.tmp` name, and
  the capture's open in `run_leg` and its read and delete in `write_leg_capture`, which that spec
  holds. No sentence here is false after that unit. Each was re-read at `9bf1eb443`, where it sits
  on the line that spec cites, and this revision's §3 bullet moves each down four: `:351`, `:520`,
  `:537` and `:752-755` still hold, and so does `:528-536`, because a capture kept for any reason is
  named in `raw_kept` and the deletes it lists stay the only ones. No scope item, design or
  criterion moves.
- rev-7 · 2026-10-15 · S11 · §3 · §4 · §5 · AC1 AC2 AC5 · a records fix for TOOL-dRedressedBar-22,
  which closes the round-1 closing diff review's report ids 2, 3, 6, 9, 11, 14 and 15 in the
  profiler, written by that unit's spec-writer pass `<w22>`. The status stays CLOSED. Unit 18 built
  against its criteria as written; each corrected paragraph names TOOL-dRedressedBar-22 and the
  change, and that spec holds the design. Code lines below are at `64e887ae6`. Ids 2 and 14: S11,
  its by-value Readers, "The record"'s raw-capture paragraph, its `<i>.log` and `<i>.json` rows and
  the Exit paragraph say an interrupt retries and names a capture an ended leg's processes still
  hold, so every kept capture is named; the interrupt branch names only `running`'s
  (`measure_legs.py:1903-1913`) and only the run end retries (`:1923-1927`). Id 9: the record
  table's `legs.tsv` row reads "leg end, rewritten whole at run end and at an interrupt"; the row is
  appended once at leg end (`:1831`) while the run end rewrites `<i>.json` (`:1928`). Id 3: "Alias
  launchers" step 4's child is the base interpreter, where `JOB_CHILD_PROGRAM` spawns
  `sys.executable` (`:872`). Id 6: "Sampling, admission and its cost" makes `check_admit` the loop's
  one admit decision, where its drained clause (`:667-668`) sits under a call guarded by `running`
  (`:1864-1866`) and the drained site tests `pending and not running` itself (`:1872`); AC5 names
  the widened call shape and its loop half. Id 11: §5's error states say an arm drives each of the
  four alias refusals (`:898`, `:959`, `:965`, `:974`). Id 15: "The selftest and its leg" names
  `memio.py`'s line, and AC1 and AC2's resolution red halves read verdicts and that line, which
  `test_resolution_disabled` reads neither of (`:2360-2385`). §3's Edges gain the hands-off to
  TOOL-dRedressedBar-22. The spec lines rev-6 cites are as of `9bf1eb443`, and this revision's
  insertions move them lower still. No other scope item, design or criterion moves.
- rev-8 · 2026-10-15 · §3 · §4 · a records fix for TOOL-dRedressedBar-25, which closes the round-2
  closing diff review's report ids 4, 11, 20 and 23 at the `measure-legs selftest` guard, written by
  that unit's spec-writer pass `<w25>`. The status stays CLOSED. Unit 18 built against its criteria
  as written; the corrected paragraph names TOOL-dRedressedBar-25 and the change, and that spec
  holds the design. Ids 4, 11, 20 and 23: §4 "The selftest and its leg" says the run-gates entries
  fold into `{prefix}/run-gates/` and `{prefix}/gate-legs.json` joins the guard. At `b5472169f` the
  row names nine run-gates files and dirs one by one (`tools/gate-legs.json:1277-1285`), so
  `tools/run-gates/README.md`, which `test_signal_docs` reads, and a `*.py` added later under the
  kit dir trip no entry. §3's Edges gain the hands-off to TOOL-dRedressedBar-25. The spec lines
  earlier revisions cite move lower by this revision's insertions. No other scope item, design or
  criterion moves.
- rev-9 · 2026-10-16 · AC15 · records, TOOL-dRedressedBar-27: the turnstile arm runs the real
  runner's hold verb inside `--selftest`, which no pass ran, and no record observes it. The
  criterion does not move, and the status stays CLOSED.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "profile every gate leg's process tree, CPU, memory and
spawned processes, and detect a stalled leg"` ranked `scan_processes`
(`tools/process-monitor/census.py`, SEAM, fan-in 4) and `run_leg_at` and `run_leg_reap`
(`tools/run-gates/run-gates.sh`). It found no profiler. The seams extended are these. `scan_processes`
gains two fields, and `build_walk` (`reap.py:136-164`) and `build_self_chain` (`scope.py:254`) are
used unchanged. From `profile_bar.py` come `resolve_bash`, `run_git`, `check_quiet` and
`derive_regime`, imported as siblings. `resolve_python`, `measure_spawn_cost`, `read_spawn_floor` and
the `measure_foreign` awk are run from the runner's source text, by the extraction seam
`run-gates.turnstile.test.sh:1500` uses. `redact` is run the same way, in
`TOOL-dRedressedBar-19`'s parity arm against the port `derive_redacted` (its S20, units-16-18
report id 20). The `resolve_prefix_token` and `resolve_kit_dir` canonical
blocks are inlined. `run_leg_at` gives the launch shape but is bound to the runner's globals, so it is
mirrored, not called. The turnstile read (rev-2) follows the one reader of the runner's queue that
already exists outside the runner, `unattended.sh:6684-6690`, which parses a ticket's pid the same
way. The set-aside reuses `read_runs` unchanged by shaping the `.leg` row it reads. The brief named
the evidence suite's nested bar as one that queues on the host. It does not: that suite exports a
private `GATE_TURNSTILE_DIR` for its bars (`run-gates.evidence.test.sh:154`). The canary's bars do
take the host key (`run-gates.test.sh:364`).

The probe disagreed with the brief once. The brief names "the `gate-legs.json` reader the runner and
`run-selftests.sh` already share", and none is shared: the runner parses inline
(`run-gates.sh:2697-2845`), and `run-selftests.sh` twice (`:523-585`, `:827-834`). What they share is
`resolve_prefix_token`, which this unit inlines over one `json.load`. That probe missed two Python
readers of the manifest in this kit: `held_halves.load_manifest` (`held_halves.py:80-88`) and
`derive-ceilings.read_legs` (`derive-ceilings.py:139-142`), which honours `GATE_LEGS`.
`TOOL-dRedressedBar-19`'s S19 makes the profiler wrap the first (units-16-18 report id 19). `derive_scope` and `classify.py`
were weighed and left out (§4). The gotchas checklist for the touched paths selected
`a-new-leg-trips-a-growing-set-of-meta-gates`, which is why §7 names every meta-gate a new leg trips.
It selected `fixture-passes-by-finding-nothing`, which is why AC4 and AC7 carry liveness halves.
And it selected `a-runner-knob-owes-a-push-class`, which is why the tool adds flags and no knob.

The recall probe returned TOOL-aGraftedHelix-5's foreign census, which is the predicate ported here.
It returned the aMeteredSweep runner research, which measured spawn cost at 19-39 ms on node d
against 78-251 ms on node a, the reason the spawn figure is sampled live rather than typed. It
returned TOOL-aFrugalTurnstile-5's `--hold`, and the brief itself.

Rev-4, for S14 and S15. `python tools/codebase-map/reuse_lookup.py "detect a Microsoft Store app
execution alias python launcher and resolve it to its real interpreter"` ranked `resolve_python`
(`tools/lib/resolve-python.sh`, SEAM, 70 installs) and `resolve_bash`, and no alias detector. The
seam S14 extends is `resolve_python`'s `GOV_PYTHON` candidate (`tools/lib/resolve-python.sh:30`):
setting it reaches every leg script that resolves its python, with no edit to any of them. For
the alias itself no existing seam fits. A grep of `tools/` for `reparse`, `APPEXECLINK` and
`WindowsApps` found no reader of a reparse TAG: `branch_reconcile.py:969` reads the reparse
attribute to avoid descending a link. It found eight inline `/windowsapps/` substring skips in bash
resolvers, such as `tools/govkit/govkit.py:1187` and `tools/roles/handoff.py:236`. Those skip a bash
that runs on another file system, which is a different question, and no shared function exists to
extend. S14 asks whether a file is an alias, which the tag answers exactly (§4
candidates). S15 reuses the conversion the set-aside
code already makes in its start-up scripts, which `TOOL-dRedressedBar-19`'s §10 found has no Python
converter to reuse. The first build's code is the record
`build/2026-10-15-build-TOOL-dRedressedBar-18-1-set-aside-work.md`, restored as §4 "Restoring the
set-aside work" says. The precedent build `aSweptBar` carries no alias or job precedent. The recall
probe returned TOOL-aDrainedSluice-6, the one resolver that runs its candidate because of the same
Store stub, and TOOL-aBatchedTribunal-6p's launcher-idiom ban, which S14 does not touch because it
writes no shell assignment.

Recall terms used: `python tools/memory-recall/query.py "how is a gate leg profiled, its spawn cost
measured, and a hung leg detected without a ceiling" --terms "profile_bar census scan_processes
build_walk spawn floor measure_spawn_cost foreign census ceiling evidence stall hung canary turnstile
hold job object"`

Recall terms used at rev-4: `python tools/memory-recall/query.py "how is the Microsoft Store python3
alias detected and resolved to a real interpreter" --terms "WindowsApps alias python3 stub 9009
resolve_python GOV_PYTHON reparse APPEXECLINK sys.executable job breakaway"`
