# TOOL-dRedressedBar-22 — the closing review's profiler findings, batched: an interrupt names every kept capture, the probe spawns the base interpreter, and each faulted arm proves its work

**Status:** INPROGRESS · rev-1 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md) | research | TOOL-dRedressedBar-21 TOOL-dRedressedBar-23 |
| [2026-10-15-prompt-TOOL-dRedressedBar-22-1-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-22-1-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-22-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-22-2-revision.md) | research | TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 |
| [2026-10-15-prompt-TOOL-dRedressedBar-22-3-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-22-3-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing diff review over `ebce889c7..e114f1356`
(`reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md`) read CLEAN WITH FIXES,
and the owner promoted all 13 of its items into this build on 2026-10-15 (the README's Build-level
rules). BUILD-METHOD M4 batches the mediums and lows into one unit per disjoint write set. This is
the profiler's batch: every item lands in `tools/run-gates/measure_legs.py`, its fixtures, its
README section or its help page. Unit 23 is the govkit batch and unit 21 the high, H1. Order 16
follows unit 21's 15, because unit 21 writes the same file first.

It closes these findings, by report id, each with the report item it shares:

| id | grade | item | sits in, at `bf42c511` | what is wrong | closed by |
|---|---|---|---|---|---|
| 2 | MEDIUM | M1 | `tools/run-gates/measure_legs.py:1737-1747` | an interrupt names only a running leg's capture, never one an ended leg's processes still hold | S2 |
| 14 | MEDIUM | M1 | the same branch, from the intent lens | as id 2, against spec 18 §5 and the README | S14 |
| 3 | MEDIUM | M2 | `tools/run-gates/measure_legs.py:859` | the probe's child is `sys.executable`, so a venv PYBIN reads 2 and every profile refuses | S3 |
| 11 | MEDIUM | M5 | `tools/run-gates/measure_legs.py:885`, `:946`, `:952`, `:961` | no arm drives a refusal of `resolve_launcher_aliases` or `resolve_alias_interpreter` | S11 |
| 15 | MEDIUM | M7 | `tools/run-gates/measure_legs.py:2154-2180` | the resolution red half reads no verdict and no sign the legs ran | S15 |
| 6 | LOW | L1 | `tools/run-gates/measure_legs.py:653-659`, `:1698-1699`, `:1706-1708` | `check_admit`'s drained clause is unreachable, and AC5 grades it | S6 |
| 9 | LOW | L2 | `tools/run-gates/measure_legs.py:1665`, `:1757-1762` | the run end updates `<i>.json` and leaves its `legs.tsv` row at the leg-end size | S9 |
| 10 | LOW | L3 | `tools/run-gates/measure_legs.py:2495-2536` | AC35's "the run goes on" arm runs one leg | S10 |
| 16 | LOW | L5 | `tools/run-gates/README.md:768` | the README says nothing is ever signalled | S16 |

Ids 6 and 9 had their fixes judged UNSOUND, and S6 and S9 take the skeptic's corrected fixes. Id 10
was re-graded medium to low by the skeptic, and that grade binds. Ids 7 and 8 were refuted and stay
refuted. Ids 1, 4, 5, 12 and 13 are units 21 and 23's.

Specs 18 and 19 are CLOSED and describe the behaviour S2, S3, S6, S9, S10, S11 and S15 change. Their
corrections are this unit's spec-writer pass, `<w22>`, which runs at this unit's turn and before its
build pass (§4 "What this unit corrects in each spec").

## 2. Scope (IN)

Item S<n> closes report id n, and S17 is the record. S14 shares report item M1 with S2 and is
observed with it. Every line cited is at `bf42c511`. Unit 21 lands first in the same file, so the
builder finds each site by the function this spec names.

- **S2** — id 2, M1. Every exit path that writes the envelope runs one capture-accounting step. A
  new `write_final_capture(lg, raw_kept, prefix)` takes one leg. When the leg's `raw_pending` is
  set, it calls `write_leg_capture(lg, final=True)`, stores the leg's new `log_bytes` in its
  record, and, when the capture is still on disk, appends `{leg, path, reason}` to `raw_kept`, the
  reason being `prefix` followed by what `write_leg_capture` returned. It returns whether it
  retried. The run-end loop (`:1749-1764`) calls it with an empty prefix where its inline retry
  sits today (`:1757-1761`). The `except KeyboardInterrupt` branch (`:1737-1747`) calls it, after
  `ending` is flushed, for every leg holding a record, with the prefix `interrupted; `, and
  rewrites the `<i>.json` of each leg it retried. The branch's stderr line becomes
  `measure-legs: INTERRUPTED — <n> leg(s) left running; <k> raw capture(s) kept, each named in raw_kept; record <dir>`.
  The module docstring's exit sentence (`:57-59`) and the README's record paragraph
  (`tools/run-gates/README.md:758-764`) say an interrupt names every kept capture, a running
  leg's and one an ended leg's processes still hold. A new fixture, `orphan.sh <hold_s>`, prints
  `early` and an LF, starts a background subshell that sleeps hold_s and then prints `late` and an
  LF, and exits 0, so its root ends while a process it started still holds the capture. It joins
  the literal `project-owned` list in `tools/run-gates/kit.toml` (`:108-114`), which
  `test_fixtures_withheld` compares with the fixture directory. A new arm,
  `test_interrupt_capture`, runs it. Observed by AC2.
- **S14** — id 14, M1. The intent lens's reading of S2's defect, against spec 18 §5 and the README.
  Closed by S2. Observed by AC2.
- **S3** — id 3, M2. `JOB_CHILD_PROGRAM` (`:859`) spawns the base interpreter, the rule every
  fixture follows (`tools/run-gates/fixtures/measure-legs/spawn.py:13`, `churn.py:11`,
  `hog.py:11`):
  `import subprocess, sys; exe = getattr(sys, '_base_executable', None) or sys.executable; sys.exit(subprocess.call([exe, '-I', '-c', 'pass']))`.
  `measure_job_children`'s docstring (`:892-896`) names the base interpreter as the child. A new
  arm, `test_venv_interpreter`, makes a scratch venv with `-m venv --without-pip` from this
  process's base interpreter and requires `measure_job_children` over the venv's `python.exe`,
  under its `Scripts` dir, to read a difference of 1. Its liveness half runs the same probe with
  the program spawning `sys.executable` and requires 2, so the venv on the host does carry a
  redirector. Its static half is the record's left-shift: `JOB_CHILD_PROGRAM` and every `.py` file
  under `FIXTURES` carry `_base_executable` on each line that carries `sys.executable`, over a
  population of at least four such lines, three of them in the fixtures. Observed by AC3.
- **S11** — id 11, M5. A new arm, `test_alias_refusals`, drives each of the four refusals. Through
  `main` over `serial.json`, with `measure_job_children` rebound to return `(2, 2)`, the run
  returns 2 with one stderr line opening `measure-legs: REFUSED — ` that carries `keeps no child`
  (`:961`), and `--out` stays empty. Through `main` again, with `check_app_alias` rebound to also
  read True for a path whose file stem is `bash`, the run returns 2 with a line carrying
  `no rule here resolves an alias that is not PYBIN` (`:952`), and `--out` stays empty. Called
  directly, `resolve_launcher_aliases` refuses with `os.lstat cannot` for a PYBIN whose converted
  spelling names no file (`:946`). Over a real non-alias file, with `measure_job_children` rebound
  to `(2, 1)`, the same call returns no substitution. Called directly, `resolve_alias_interpreter`
  refuses with `no plain file` for the launcher `echo` (`:885`), and returns a path
  `os.path.isfile` accepts for this process's base interpreter. The tool's code does not move for
  S11. Observed by AC11.
- **S15** — id 15, M7. `test_resolution_disabled` (`:2154-2180`) requires `spawn six`,
  `spawn none` and `memio` each to read verdict `ok`, and memio's `<i>.log` to carry the line
  `memio: wrote 200 MiB`, before it reads the 0 difference and the 0 `write_bytes` as work done
  outside the job. `tools/run-gates/fixtures/measure-legs/memio.py` prints
  `memio: wrote <mb> MiB` once its write is synced. The record's left-shift for the class
  `ab-arm-never-did-the-work` is a static arm, `test_ab_arms_read_verdicts`. It walks this file
  with `ast` and takes every `test_*` function holding a subtraction whose two operands each read
  `procs_total`. It requires at least three such functions, and requires each to read `verdict`.
  `test_serial_run`'s spawn count and `test_fork_count` (`:2443-2455`) read their two legs'
  verdicts, so they meet it. Observed by AC15.
- **S6** — id 6, L1, by the skeptic's corrected fix. `check_admit` becomes the loop's one admit
  decision, `check_admit(mode, pending, running, cpu, mem, fresh, cpu_cap=CPU_CAP_PCT, mem_cap=MEM_CAP_PCT)`.
  It reads False when nothing is pending, True when no leg of the run is running, which is the
  drained release, and otherwise True only under `--concurrent` on a fresh sample at or under both
  caps. The loop calls it at both admission sites. At the host tick (`:1698-1699`) the call takes
  `len(pending)`, `len(running)`, the tick's sample and its freshness, with no guard around it.
  At the drained site (`:1706`) the call takes the same counts, the last sample and `fresh` False,
  where today the site tests `pending and not running` itself. So the drained clause is the one
  the loop's release passes through, and `test_check_admit` (`:1961-1965`) grades the new
  signature over eight rows. `test_legs_table`'s run (S9) records every call the loop makes, which
  ties the drained half to the loop. Observed by AC6.
- **S9** — id 9, L2, by the skeptic's corrected fix. A new `write_legs_table(run_dir, legs)`
  writes `legs.tsv` whole through `write_atomic`: the `LEGS_COLUMNS` header, then
  `render_legs_row(lg["record"])` for each leg holding a record, in index order. The leg-end
  appends in `write_leg_profile` (`:1665`) stay, so a run killed outright keeps its rows. The run
  end calls it after its loop, and the interrupt branch after S2's step and before the envelope.
  A new arm, `test_legs_table`, runs a two-leg temp manifest, `orphan.sh 2` then `spawn.py 0 5`.
  It requires every `legs.tsv` row to equal `render_legs_row` over that leg's final `<i>.json`,
  which is the record's invariant, and the orphan's `<i>.log` to carry `late`, so its size did
  move after the root's exit. The README's record paragraph says when the table is rewritten.
  Observed by AC9.
- **S10** — id 10, L3. `test_launch_failure`'s temp manifest holds two legs: `launch`, which runs
  `spawn.py 0 1 <marker>`, then `after`, which runs `spawn.py 0 1`. Its `build_closed_job` closes
  only the third job it makes, `len(made) == 3`, which is the first leg's, where today it closes
  every job from the third on (`:2509`). The arm also requires `after` to read verdict `ok` with
  `procs_total` at least 1, and `legs.tsv` to hold two rows. Observed by AC10.
- **S16** — id 16, L5. The README's "What it does not check" paragraph
  (`tools/run-gates/README.md:766-770`) says what the module docstring says (`:42-45`): no process
  that has run is ever signalled, and the one terminate is a leg's root still suspended after a
  failed open, job assign, thread snapshot or resume, which has executed nothing and records
  `fail` with its `launch_error`. The help page's sentence of the same kind,
  `help/measure-legs.md:23`, says no process that has run is ever killed. A new arm,
  `test_signal_docs`, is the record's parity option: the module docstring and the README's
  profiler section each carry `terminate` and `launch_error`, and neither carries
  `nothing is ever signalled`. Observed by AC16.
- **S17** — The record, in two passes. Specs 18 and 19 each take ONE rev bump in this unit's
  spec-writer pass, `<w22>`, which runs once unit 21 is CLOSED and before the build pass. Each
  revision line names `TOOL-dRedressedBar-22` and every report id §4's table assigns that spec,
  and each spec's §3 Edges gains `hands-off` `TOOL-dRedressedBar-22`. The build pass writes no
  spec file but this one's status and date cells. Every reading below goes to this unit's
  acceptance ledger under `memory/builds/dRedressedBar/build/`, carrying
  `**Serves:** journal TOOL-dRedressedBar-22`. Observed by AC17.

## 3. Non-goals (OUT)

- No finding outside the round-1 record. Ids 7 and 8 stay refuted. The H1 sweep fix, the
  `write_atomic` temp open, `derive_abandoned_scratch`, `write_recovered_logs` and
  `test_scratch_sweep` are unit 21's, and the govkit findings are unit 23's.
- No class-level left-shift that is its own mechanism. M5's proposal, a coverage check that every
  `raise ProfileRefused` site is named by an arm, covers 29 sites in the tool body at `bf42c511`,
  most of them outside the two functions this finding names. The checklist entries the record
  offers for M1, L1 and L3 are records in `memory/gotchas/`. Each finding here is left-shifted by
  its own regression arm, observed red first at the close (BUILD-METHOD M8). The in-file gates
  the record names for M1 (one helper), M2 (the static base-interpreter rule), M7 (the A/B verdict
  arm), L2 (the row invariant) and L5 (the parity arm) are in scope.
- No change to the admission rule: the caps, the freshness test and the drained release keep their
  meaning. The one visible move is that a drained admission taken at a host tick is logged on that
  tick's `host.tsv` row rather than on a row of its own.
- No change to how a capture is redacted, kept or retried at leg end (`write_leg_capture`), and no
  new record field.
- No kit version move. The lander mints a version for a move of shipped bytes, so a branch owes none
  (`tools/govkit/govkit.py:13381`, "WHERE THE BUMP IS MADE").
- No re-price of the `measure-legs selftest` budget or ceiling. Both rows are a pinned proxy whose
  own text says to re-price them from the first measured run, which the close's arm observations
  make (`tools/run-gates/selftest-budgets.txt:74`).
- No new help page. `help/measure-legs.md` changes one sentence.

### Edges

- **consumes-from** `TOOL-dRedressedBar-18` — the profiler, its interrupt branch, its admission
  loop, its interpreter probe, its fixtures, its README section and its help page, all of which
  this unit changes, and its spec, whose text `<w22>` corrects. Without them there is nothing to
  fix.
- **consumes-from** `TOOL-dRedressedBar-19` — the launch-failure branch and `test_launch_failure`,
  which S10 extends, `test_fork_count` and the literal fixture list with `test_fixtures_withheld`,
  which S15 and S2 meet, and its spec's AC35, which `<w22>` corrects.
- **hands-off** external — the class-level left-shifts §3 names, for the build's close to dispose.

## 4. Design

### Evidence, read at `bf42c511` on 2026-10-15

`bf42c511`'s `tools/` equals `e114f1356`'s, the reviewed tip
(`git diff --stat e114f1356 bf42c511 -- tools` prints nothing). Every line the record cites was
re-read there and agrees, except that `check_admit` spans `:653-659`, where the record says
`:653-658`.

- The interrupt branch adds a `raw_kept` entry for each leg in `running` only, flushes `ending`
  through `write_leg_profile`, which never reads `raw_pending`, and returns 130 (`:1737-1747`).
  `write_leg_end` sets `raw_pending` from `write_leg_capture(lg, final=False)` (`:1650`), which
  keeps the capture when `left_running` is not 0 (`:1438-1439`). Only the run-end loop retries it
  and names it (`:1757-1761`).
- A capture is opened by `open(capture, "wb")` and handed to the root as its stdout (`:777-780`).
  On Windows that handle shares no delete, so `os.remove` fails while any process the leg started
  still holds it, which is the reason `write_leg_capture` returns at `:1443`.
- `JOB_CHILD_PROGRAM` spawns `sys.executable` (`:859`), and `measure_job_children` subtracts the
  twin's total (`:891-914`). The three spawning fixtures take
  `getattr(sys, "_base_executable", None) or sys.executable`. Measured on node d, 2026-10-15,
  under Python 3.12.10: in a venv made with `--without-pip`, which took 0.05 s, a child spawned
  through `sys.executable` reported a parent other than the interpreter that spawned it, and one
  spawned through `sys._base_executable` reported that interpreter. That is the redirector the
  skeptic of record id 3 reproduced on this host.
- `resolve_launcher_aliases` refuses at `:946`, `:952` and `:961`, and `resolve_alias_interpreter`
  at `:885`. No `test_*` function reaches any of them. `test_resolution_disabled` rebinds the whole
  function and returns early on a host whose PYBIN is no alias (`:2159-2163`).
- `check_admit` is called once, at `:1698-1699`, under `opts.mode == "concurrent" and pending and
  running`, so its `running == 0` clause (`:657-658`) is never reached. The loop's drained release
  is `if pending and not running: run_admission(events)` (`:1706-1708`).
- `legs.tsv` is headed at `:1592` and gains one appended row per leg in `write_leg_profile`
  (`:1665`). The run-end loop sets `rec["log_bytes"]` and rewrites `<i>.json` (`:1759`, `:1762`),
  and nothing rewrites the row. `render_legs_row` reads the record by `LEGS_COLUMNS`
  (`:1100-1108`).
- `test_launch_failure` runs a one-leg manifest and closes every job from the third on
  (`:2501-2511`). `run_admission`'s `LaunchFailed` branch does not touch `pending` (`:1616-1635`).
- `memio.py` prints nothing (`tools/run-gates/fixtures/measure-legs/memio.py:1-24`).
- The README says "nothing is ever signalled" (`tools/run-gates/README.md:768`), the docstring
  carves out the one terminate (`:42-45`), and `run_leg` calls it (`:815-823`). The help page says
  "Nothing is ever killed" (`help/measure-legs.md:23`), while its own `:36-38` say a launch-failed
  process is stopped.
- `check_admit`'s other readers are `test_check_admit` and the generated
  `memory/map/generated/symbols.json`. No file outside `tools/run-gates/` reads `legs.tsv` but the
  help page's `sort` example.

### The profiler, item by item

Each row is a change to `tools/run-gates/measure_legs.py` unless it names another file.

| Id | Change |
|---|---|
| 2, 14 | `write_final_capture`, called by the run end and the interrupt; the INTERRUPTED line; the docstring's exit sentence; `orphan.sh`; one `kit.toml` list element; `test_interrupt_capture` |
| 3 | `JOB_CHILD_PROGRAM`; `measure_job_children`'s docstring; `test_venv_interpreter` |
| 11 | `test_alias_refusals` |
| 15 | `memio.py` prints its line; `test_resolution_disabled` reads three verdicts and that line; `test_serial_run` and `test_fork_count` read verdicts; `test_ab_arms_read_verdicts` |
| 6 | `check_admit`'s signature and its two call sites; `test_check_admit`'s eight rows |
| 9 | `write_legs_table`, called by the run end and the interrupt; `test_legs_table` |
| 10 | `test_launch_failure`'s two-leg manifest and its `len(made) == 3` |
| 16 | `tools/run-gates/README.md`'s signalling sentence; `help/measure-legs.md:23`; `test_signal_docs` |

### The two exit paths

```python
except KeyboardInterrupt:
    for lg in running.values():
        raw_kept.append({"leg": lg["name"], "path": lg["capture"], "reason": "interrupted"})
    for i in sorted(ending):
        write_leg_profile(ending.pop(i))
    for lg in legs:
        if lg.get("record") and write_final_capture(lg, raw_kept, "interrupted; "):
            write_leg_record(run_dir, lg["record"])
    write_legs_table(run_dir, legs)
    ...  # envelope exit 130, write_envelope, the INTERRUPTED line, return 130

# run end
for lg in legs:
    ...  # job_final, as today
    write_final_capture(lg, raw_kept, "")
    write_leg_record(run_dir, lg["record"])
    ...  # handle close, as today
write_legs_table(run_dir, legs)
```

`write_final_capture` is the one step both paths run, so the accounting cannot drift between them.
A capture whose processes have all exited by the interrupt is redacted and unlinked there, and
needs no name. A row a concurrent run appended in end order is written back in index order, which
the help page's `sort` example does not notice.

### The arms

Every arm follows the file's existing shapes: `write_temp_manifest` and `run_fixture` for a run,
a rebinding through `globals()` restored in a `finally` as `test_launch_failure` does, `main` under
`redirect_stderr` as `test_no_bare_bash_argv` does, and `ast` over this file as that arm does.

| Arm | Runs | Liveness, so it cannot pass on nothing | Cost, estimated |
|---|---|---|---|
| `test_interrupt_capture` | `orphan.sh 6` as `orphan`, then `spawn.py 0 6` as `hold`. `write_leg_capture` is wrapped to note a non-final call that kept the capture, and `scan_root_exits` to raise `KeyboardInterrupt` on its first call after that note. It then waits, bounded at 30 s, until both kept captures unlink, so no fixture process outlives it | the note was taken, and `hold`'s `interrupted` entry is present | 20 s |
| `test_venv_interpreter` | a venv under the arm's temp dir; `measure_job_children` twice over its python | the `sys.executable` program reads 2 | 5 s |
| `test_alias_refusals` | two `main` runs over `serial.json` that refuse before any scratch is made; two direct calls of each function | each function answers a real input without refusing | 10 s |
| `test_resolution_disabled` | as today, on an alias host only | three verdicts `ok` and memio's line | as today |
| `test_ab_arms_read_verdicts` | `ast` over this file | at least three A/B functions found | under 1 s |
| `test_check_admit` | eight pure rows | rows of both answers | under 1 s |
| `test_legs_table` | `orphan.sh 2` as `orphan`, then `spawn.py 0 5` as `hold`, with `check_admit` wrapped to record each call and to raise `KeyboardInterrupt` once 60 s have passed | `orphan`'s log carries `late`, and two admissions were recorded | 15 s |
| `test_launch_failure` | as today, two legs | `after` reads `ok` | 2 s more |
| `test_signal_docs` | the module docstring and the README's profiler section | the section is found and carries `measure_legs.py` | under 1 s |

`test_legs_table`'s 60 s deadline bounds the staged break of S6. With the drained clause taken out of
`check_admit`, a serial run admits nothing, and the deadline turns that into a red `130` instead of a
selftest that hangs until the leg's ceiling.

The eight `test_check_admit` rows are (mode, pending, running, cpu, mem, fresh):
(`concurrent`, 1, 1, 81, 50, True) holds, (`concurrent`, 1, 1, 80, 90, True) admits,
(`concurrent`, 1, 1, 50, 91, True) holds, (`concurrent`, 1, 1, 50, 50, False) holds,
(`concurrent`, 1, 0, 99, 99, False) admits, (`serial`, 1, 0, None, None, False) admits,
(`serial`, 1, 1, 10, 10, True) holds, and (`concurrent`, 0, 0, 10, 10, True) holds.

`test_alias_refusals`' first half feeds `resolve_launcher_aliases` a count pair, `(2, 2)`, rather
than a real interpreter whose child leaves its job. The real 2 is `test_venv_interpreter`'s liveness
half, so the comparison is shown to meet the value it guards against, and the refusal path is shown
to reach exit 2 with nothing written.

### What this unit corrects in each spec

A corrected paragraph carries `TOOL-dRedressedBar-22` and one sentence naming the change, and this
spec's §2 and §4 hold the design. Under `.claude/roles.json` only `gov-spec-writer` writes spec
files and only `gov-builder` writes product files, and scratch-guard admits a builder's spec edit
only where it moves the status and date cells of a spec its card routes
(`tools/hooks/scratch-guard.js:91-99`). So these rows are this unit's spec-writer pass, `<w22>`, M6's
"a review's fixes folded in", dispatched once unit 21 is CLOSED, because unit 21's own pass edits
the same two specs, and before the build pass. Each target takes its correction as a records fix
with its status unchanged. A build pass that finds no `<w22>` returns that to the main loop before
any write.

| Spec | Ids | What moves |
|---|---|---|
| 18 | 2, 3, 6, 9, 11, 14, 15 | S11 and §4 "The record": an interrupt retries and names a capture an ended leg's processes still hold, and the Exit paragraph says every kept capture; the record table's `legs.tsv` row reads "leg end, rewritten whole at run end and at an interrupt"; §4 "Alias launchers" step 4: the child is the base interpreter; §4 "Sampling, admission and its cost": the loop's one admit decision; §4 "The selftest and its leg": `memio.py` prints its line; §5 error states: the four alias refusals are each driven by an arm; AC5's call shape and its loop half, AC1 and AC2's resolution red halves reading verdicts and memio's line; §3 Edges gains the hands-off; revision line naming AC1, AC2 and AC5 |
| 19 | 10 | AC35 runs a two-leg manifest, `launch` then `after`, closing only the third job, and requires `after` to read `ok`; §3 Edges gains the hands-off; revision line naming AC35 |

Until `<w22>` lands, an unstaged `memory hygiene` run reds check 12's reciprocity join on §3's two
`consumes-from` edges, because specs 18 and 19 name no `hands-off` back. The staged run holds the
joins (`memory/TEMPLATE-SPEC.md`, "§3 Edges").

### Order, and the symbol index

Order 16 is one above unit 21's. Unit 21 writes `tools/run-gates/measure_legs.py` first, so M6
sequences this unit after it, and unit 23 after this one, because both regenerate
`memory/map/generated/symbols.json`. The new functions are minted in `measure_legs.py`, so the build
pass runs `python tools/codebase-map/gen_map.py --write` alone before its product commit, as unit
19's did. No file the kickoff manifest watches moves, so no re-stamp is owed.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `write_final_capture`, `write_legs_table` | functions | `py.function`, `write` |
| `test_interrupt_capture`, `test_venv_interpreter`, `test_alias_refusals`, `test_ab_arms_read_verdicts`, `test_legs_table`, `test_signal_docs` | selftest arms | `py.function`, `test` |
| `orphan.sh` | fixture | none |

Each name answered OK under `python tools/lexicon/lexicon.py --suggest <name> --as py.function` on
2026-10-15. `check_admit` keeps its name and answered OK the same day.

### Files touched (estimate)

- `tools/run-gates/measure_legs.py`
- `tools/run-gates/fixtures/measure-legs/`
- `tools/run-gates/kit.toml`
- `tools/run-gates/README.md`
- `help/measure-legs.md`
- `memory/map/generated/`
- `memory/builds/dRedressedBar/build/`

The fixture directory gains `orphan.sh` and changes `memio.py`. Specs 18 and 19 are `<w22>`'s write
set, not the build pass's.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| L1 by the finder's fix, re-stating AC5 over the unreachable clause | the skeptic: AC5 then still grades a clause no production call reaches | Rejected |
| L1 by taking the clause out of `check_admit` and keeping the loop's inline `pending and not running` | the drained half is then tested only through a whole run, and the function and the loop hold two answers to one question | Rejected; S6 makes `check_admit` the loop's one decision, the record's "for example" |
| L2 by writing `legs.tsv` once, after the run-end loop | spec 18's record table writes it at leg end, and an interrupt or a kill would leave no rows (the skeptic) | Rejected; S9 keeps the appends and rewrites the whole table on both exit paths |
| L2 by rewriting the one affected row | `write_record_line` only appends, so one row cannot be replaced without rewriting the file (the skeptic) | Rejected |
| M1 by a second inline retry in the interrupt branch | two copies of one accounting step drift, which is how id 2 arose | Rejected; S2's one helper |
| S2's orphan as an inline `bash -c` argv in a temp manifest | the script crosses Windows command-line quoting into MSYS, where parentheses, quotes and `&` must survive both, the class `bash-c-multiline-flattens-under-msys` | Rejected; a fixture file, as `stall.sh` is |
| M7's evidence as a nonzero `user_s` | an alias launch that failed still spends CPU in its launcher | Rejected; memio prints a line only after its write |
| The corrections to specs 18 and 19 in the build pass's commit | scratch-guard refuses a builder's edit to another spec, and the spec writer writes no product file (unit 10's divergence) | Refused by the hook |

## 5. Production-readiness checklist

- security — S2 closes the one exit path that left an unredacted capture on disk with no name: an
  interrupt now redacts what it can and names every capture it keeps in `raw_kept`, as the README
  and spec 18 §5 already promised. `legs.tsv` is rewritten through `write_atomic`, owner-only, in
  the run dir the tool already owns. No new write path, process kill or network call.
- perf / scale — `legs.tsv` is written once more per exit, one row per leg. The arms add about 50 s
  to the selftest, an ESTIMATE summed from §4's arm table and not measured. The leg's budget, 380 s,
  and its ceiling, 500 s, are PINNED proxies on an r of 250 s, and the close's first measured run
  re-prices both, as their row says.
- error / empty / loading states — An interrupt names every kept capture with a reason opening
  `interrupted`. Each alias refusal exits 2 with one named line and writes nothing. A venv PYBIN
  profiles where it refused.
- observability — The INTERRUPTED line counts the kept captures beside the running legs.
- risks — `test_venv_interpreter`'s liveness half fails, never passes, on a host whose venv carries
  no redirector, as AC4's hog half does on a host the hog cannot load. AC15's alias half reads
  `unexercised` on a host whose PYBIN is no alias, so a pass there says nothing about an alias, as
  today. `test_interrupt_capture` rests on Windows refusing to unlink a file another process holds,
  the rule `write_leg_capture` already rests on. A serial run's drained admission may now be logged
  on a tick's `host.tsv` row (§3).
- testing — AC2 to AC17 are direct runs of the tool over fixtures and temp manifests, in-process
  probes, `ast` and grep probes over source and specs. The new and moved arms are declared in §7.
- migration — No record field, flag or conf key moves. A concurrent run's `legs.tsv` rows are in
  index order rather than end order. A run dir from before this unit reads as it did.
- user docs — `help/measure-legs.md:23` stops saying nothing is ever killed. The README's profiler
  section states the interrupt's naming, the table rewrite and the one terminate.

## 6. Acceptance criteria

The numbering follows report ids, so it skips the ids other units close, and the criterion that
observes S2 also observes S14. `<p22>` is this unit's product commit and `<w22>` its spec-writer
commit, each named in its ledger. A break said to be "as at `<p22>~1`" is the code the build pass
starts from, which unit 21 leaves. `<ml>` is `python tools/run-gates/measure_legs.py`, `<fx>` is
`tools/run-gates/fixtures/measure-legs`, `<o>` is a fresh dir under `%TEMP%`, `<sf>` is the
selftest's flags `--census-every 1 --stall-window 8 --stall-cpu 0.5`, and `<sN>` is spec N's file
under `memory/builds/dRedressedBar/spec/`. "Joined" means piped through `tr '\n' ' ' | tr -s ' '`.
Every command runs from the worktree root on node d.

- **AC2** — A python program imports `measure_legs`, wraps `write_leg_capture` to note a
  non-final call that kept the capture, and wraps `scan_root_exits` to raise `KeyboardInterrupt`
  on its first call after that note. It runs `main` with `--serial --legs <m> --out <o>` and
  `<sf>`, where `<m>` is a temp manifest of `bash <fx>/orphan.sh 6` named `orphan` and
  `spawn.py 0 6` named `hold`. `main` returns 130. The envelope's `exit` is 130. Its `raw_kept`
  holds an entry for `hold` with the reason `interrupted`, and one for `orphan` whose `path` still
  exists and whose reason opens `interrupted; `. `orphan`'s `<i>.json` exists, and the stderr line
  opening `measure-legs: INTERRUPTED` carries `2 raw capture(s) kept`.
  `inspect.getsource(measure_legs.run_profile)` carries `write_final_capture(` twice. Spec 18's
  "The record" section, cut and joined, carries `TOOL-dRedressedBar-22`.
  Red when: the interrupt branch's pending step is taken out, as at `<p22>~1`. `raw_kept` then
  names `hold` alone, and `orphan`'s unredacted capture stays on disk with no name.
  cost: about 20 s, the fixture's 6 s hold included.
  fixture: when the note is never taken, the orphan having left the job or exited first, the
  program reports the interrupt unstaged and fails.
- **AC3** — A python program makes a venv under `<o>` with `-m venv --without-pip` from its own
  `sys._base_executable`. `measure_legs.measure_job_children` over the venv's `python.exe`, under
  its `Scripts` dir, with `api` from `resolve_job_backend()` and `bash` from
  `profile_bar.resolve_bash`, returns two counts that differ by 1. With
  `measure_legs.JOB_CHILD_PROGRAM` rebound to the program spawning `sys.executable`, they differ
  by 2. With `GOV_PYTHON` set to the venv python, `main` over a temp
  manifest of `spawn.py 0 0` returns 0, and the envelope's `pybin` names the venv python and its
  `interpreter_probe` differs by 1. `JOB_CHILD_PROGRAM` carries `_base_executable`, and every line
  of a `.py` file under `<fx>` carrying `sys.executable` also carries `_base_executable`, over at
  least three such lines. Spec 18's "Alias launchers" section, cut and joined, carries
  `_base_executable`.
  Red when: the program spawns `sys.executable`, as at `<p22>~1`. The probe over the venv reads 2,
  and the `GOV_PYTHON` run returns 2 with a REFUSED line carrying `keeps no child`.
  figure: 1 is DERIVED, the twin cancelling the wrapper and the interpreter. 2 is the redirector,
  measured on node d on 2026-10-15 under Python 3.12.10 (§4 Evidence), so it is PINNED to a host
  whose venv carries one.
- **AC11** — A python program imports `measure_legs`, rebinds `measure_job_children` to return
  `(2, 2)`, and runs `main` with `--serial --legs <fx>/serial.json --out <o>` under
  `redirect_stderr`. It returns 2, exactly one stderr line opens `measure-legs: REFUSED — ` and
  carries `keeps no child`, no `Traceback` is printed, and `<o>` stays empty. With that rebinding
  restored and `check_app_alias` rebound to also read True for a path whose stem is `bash`, a fresh
  run returns 2 with one such line carrying `no rule here resolves an alias that is not PYBIN`, and
  its `<o>` stays empty. `resolve_launcher_aliases` called directly with a PYBIN whose `path` names
  no file raises `ProfileRefused` carrying `os.lstat cannot`. With `path` set to this process's
  base interpreter and `measure_job_children` rebound to `(2, 1)`, the same call returns an empty
  substitution list. `resolve_alias_interpreter` with the launcher `echo` raises `ProfileRefused`
  carrying `no plain file`, and with this process's base interpreter returns a path
  `os.path.isfile` accepts. Spec 18's §5, cut and joined, carries `TOOL-dRedressedBar-22`.
  Red when: the raise at `:961` is deleted. The first run then profiles every leg and returns 0
  with a run dir in `<o>`. And with the raise at `:952` deleted, the second run refuses later, in
  `resolve_alias_interpreter`, with a line that does not carry the not-PYBIN phrase.
  cost: about 10 s.
- **AC15** — A python program reads `test_resolution_disabled`'s source with `inspect` and finds
  `verdict` and `memio: wrote`. `<ml> --serial --legs <m> --out <o>` over a temp manifest of
  `memio.py 1` writes a `<i>.log` carrying `memio: wrote 1 MiB`. On a host whose PYBIN is an App
  Execution Alias, the program rebinds `resolve_launcher_aliases` to return `([], None)` and runs
  `main` over `<fx>/serial.json`. `spawn six`, `spawn none` and `memio` then read verdict `ok`,
  memio's `<i>.log` carries `memio: wrote 200 MiB`, and the spawn difference reads 0. An `ast`
  walk of `tools/run-gates/measure_legs.py` finds at least three `test_*` functions holding a
  subtraction whose operands each read `procs_total`, and each of them reads `verdict`. Spec 18's
  AC1, cut from `- **AC1**` to `- **AC2**` and joined, carries `verdict`.
  Red when: on an alias host, a `serial.json` copy whose memio row names a script that does not
  exist is run with the resolution disabled. The gate as at `<p22>~1` passes it, memio reading
  under 200 MiB with 0 bytes written, and the new half reds on memio's verdict `fail` and its
  absent line. And the `ast` walk over the file as at `<p22>~1` finds three functions reading no
  `verdict`.
  fixture: the alias half needs a host whose PYBIN is an App Execution Alias, which node d is at
  2026-10-15 (spec 18 AC1). Elsewhere it reads `unexercised`, while memio's line and the `ast`
  half hold on every host.
- **AC6** — A python program calls `measure_legs.check_admit` at §4's eight rows and gets hold,
  admit, hold, hold, admit, admit, hold and hold. It wraps `check_admit` to record each call and
  runs `main` over AC9's manifest. Exactly two calls return True, one per leg, each with
  `running` 0 and `pending` at least 1, and no call returns True while a leg runs.
  `inspect.getsource(measure_legs.run_profile)` carries no `if pending and not running`. Spec 18's
  AC5, cut from `- **AC5**` to `- **AC6**` and joined, carries `TOOL-dRedressedBar-22`.
  Red when: the drained clause is taken out of `check_admit`, so the fifth and sixth rows read
  hold, and the run admits nothing until the recorder's 60 s deadline ends it with 130. And when
  the drained site calls `run_admission` past `check_admit`, as at `<p22>~1`, the recorder sees no
  call return True for a serial run.
- **AC9** — A python program runs `main` with `--serial --legs <m> --out <o>` and `<sf>`, where
  `<m>` is a temp manifest of `bash <fx>/orphan.sh 2` named `orphan` and `spawn.py 0 5` named
  `hold`. `legs.tsv` holds the header and two rows, and each row equals
  `measure_legs.render_legs_row` over that leg's `<i>.json`, column for column. `orphan`'s
  `<i>.log` carries `late`, its `<i>.json` `log_bytes` is 11, and `raw_kept` is empty.
  `tools/run-gates/README.md`'s profiler section, cut and joined, carries `rewritten whole`. Spec
  18's record table, cut from `| File | Written | Holds |` to its last row, carries `run end` on
  its `legs.tsv` row.
  Red when: the run end calls no `write_legs_table`, as at `<p22>~1`. `orphan`'s row then reads
  `log_bytes` 6, the size of `early` alone, where its `<i>.json` reads 11.
  figure: 6 and 11 are the fixture's bytes, `early` and `late` each with an LF, DERIVED.
  cost: about 15 s.
- **AC10** — A python program rebinds `measure_legs.build_job` to a wrapper that closes only the
  third job it makes, and runs `main` over a temp manifest of `launch`, `spawn.py 0 1 <marker>`,
  then `after`, `spawn.py 0 1`. `main` returns 0 within 60 s. `launch` reads verdict `fail`, rc 1,
  and a `launch_error` opening `launch: AssignProcessToJobObject`. `after` reads verdict `ok` with
  `procs_total` at least 1, and `legs.tsv` holds two rows under its header.
  `inspect.getsource(measure_legs.test_launch_failure)` carries `len(made) == 3`. Spec 19's AC35,
  cut from `- **AC35**` to `- **AC36**` and joined, carries `after`.
  Red when: `run_admission`'s `LaunchFailed` branch also clears `pending`. `after` is then absent
  and `legs.tsv` holds one row, while the one-leg arm as at `<p22>~1` still passes.
  cost: under a minute.
- **AC16** — `grep -c 'nothing is ever signalled' tools/run-gates/README.md` prints 0, and the
  README's profiler section, cut from `## The gate profiler` to the next `## ` and joined, carries
  `terminate`, `suspended` and `launch_error`.
  `grep -c 'Nothing is ever killed' help/measure-legs.md` prints 0, and the page carries
  `has run is ever killed`. A python program applies
  `test_signal_docs`' rule to `measure_legs.__doc__` and that section: each carries `terminate`
  and `launch_error`, and neither carries `nothing is ever signalled`.
  Red when: over the README as at `<p22>~1`, the grep prints 1 and the section carries no
  `terminate`.
- **AC17** — `git diff <w22>~1 <w22> -- memory/builds/dRedressedBar/spec/` shows `<s18>` and
  `<s19>` each with one header rev change and one new revision line, and each line names
  `TOOL-dRedressedBar-22` and every report id §4's table assigns that spec. Each carries a CLOSED
  header at `<w22>~1` and a §3 bullet `hands-off` `TOOL-dRedressedBar-22` at `<w22>`.
  `git diff --name-only <p22>~1 <p22> -- memory/builds/dRedressedBar/spec/` names no file but this
  spec. The ledger S17 names exists and carries `**Serves:** journal TOOL-dRedressedBar-22`.
  Red when: a target takes no bump or two, a revision line misses one of its ids, or a build-pass
  commit writes another spec.

## 7. Gates

`measure-legs selftest` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates canary` · `run-gates gov canary` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

The line is a floor. Joined against the guards in `tools/gate-legs.json` with `BROAD_LEG_FLOOR`
applied, §4 Files touched owes `measure-legs selftest`, `recall floor` and `recall floor arms`; the
rest are legs the change moves: the kit's shipped bytes, its descriptor, the symbol index, new text
IO and this spec.

New arm: tools/run-gates/measure_legs.py --selftest · covers AC2 · test_interrupt_capture with the interrupt branch's pending-capture step taken out · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC3 · test_venv_interpreter with JOB_CHILD_PROGRAM spawning sys.executable · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC11 · test_alias_refusals with the keeps-no-child raise deleted, then with the not-PYBIN raise deleted · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC15 · test_resolution_disabled over a serial.json copy whose memio row names a missing script, on an alias host; test_ab_arms_read_verdicts with test_fork_count's verdict read taken out · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC6 AC9 · test_check_admit with the drained clause taken out of check_admit; test_legs_table with the run end's write_legs_table call taken out, and again with the drained site calling run_admission past check_admit · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC10 · test_launch_failure with pending.clear() added to run_admission's LaunchFailed branch · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC16 · test_signal_docs over the README with its "nothing is ever signalled" sentence restored · none

The main loop observes each new or moved arm red on its staged break, then green, at the close, and
runs the bar once after the last unit is terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-15 · initial draft, promoted from the round-1 closing diff review's profiler
  findings by the owner's ruling of 2026-10-15. Report ids 2, 3, 6, 9, 10, 11, 14, 15 and 16 are
  batched by M4. Every citation was re-read at `bf42c511`, whose `tools/` equals the reviewed tip's,
  and the venv redirector was measured on node d. Ids 6 and 9 take the skeptic's corrected fixes. S16
  also corrects `help/measure-legs.md:23`, the same absolute claim in the page that points at the
  README, which the record's left-shift grep over the kit's docs finds.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "on interrupt, finalize every pending raw capture and name
the kept ones in the envelope"` ranked name-stem matches only (`raw`, `read_host_name`,
`raw_write_cells`) and no capture-accounting seam. `python tools/codebase-map/reuse_lookup.py
"rewrite a tsv summary table whole from final per-row records through a temp file and rename"`
ranked `rows`, `row` and `records` by stem, and none writes a table from records. Both are recorded
as misses, and no existing seam outside the file fits. The seams extended are the profiler's own:
`write_leg_capture` (`tools/run-gates/measure_legs.py:1427-1444`), which S2's `write_final_capture`
calls unchanged; `render_legs_row` (`:1100-1108`) and `write_atomic` (`:1022-1035`), which S9's
`write_legs_table` composes; `check_admit` (`:653-659`), which S6 widens into the loop's decision
rather than minting a second one; and the fixtures' base-interpreter idiom
(`tools/run-gates/fixtures/measure-legs/spawn.py:13`), which S3 adopts. The arms reuse
`write_temp_manifest`, `run_fixture`, the `globals()` rebinding of `test_launch_failure`, the
`redirect_stderr` refusal read of `test_no_bare_bash_argv`, and that arm's `ast` walk. `orphan.sh`
follows `stall.sh`'s background-subshell shape, and its list element follows
`tools/run-gates/kit.toml:108-114`.

The gotchas checklist for `tools/run-gates/measure_legs.py`, `tools/run-gates/README.md`, the
fixtures and `help/measure-legs.md` selected these classes, each answered here:
- `guard-above-a-fold-makes-its-fallback-dead`, the class of id 6, which S6 closes by making the
  loop's guard the function's own.
- `fixture-passes-by-finding-nothing`, which is why every arm in §4's table states its liveness
  half, and why `test_interrupt_capture` fails when no capture was kept pending.
- `staged-break-substitutes-a-synthetic-value`, which `test_alias_refusals`' `(2, 2)` meets: §4
  says where the real 2 is observed.
- `two-answers-to-one-question`, the class of id 16, which `test_signal_docs` gates, and of S6's
  rejected two-site alternative.
- `a-folded-field-leaves-its-row-shape-docs-behind`, which is why `<w22>` corrects spec 18's record
  table and the README states when `legs.tsv` is rewritten.

The recall probe returned the review record and spec 18, the reading of id 2 in unit 1's agent
returns, and TOOL-aReapedSpinner-7, the runner's own interrupt path, which kills nothing, as this
tool's interrupt does not. The precedent aSweptBar-7, a closing review's minors batched into one
unit, corrected a CLOSED spec in a spec pass and left the class-level left-shifts to the close, and
this unit takes that shape. The record and the code agree on every citation re-read, with the one
`check_admit` span §4's Evidence names.

Recall terms used: `python tools/memory-recall/query.py "how does the gate profiler account for kept
raw captures on interrupt and refuse an interpreter whose child leaves the job" --terms "measure_legs
raw_kept raw_pending interrupt KeyboardInterrupt legs.tsv check_admit drained JOB_CHILD_PROGRAM
_base_executable venv redirector ProfileRefused"`
