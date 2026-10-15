# TOOL-dRedressedBar-21 — the profiler trusts no path a temp dir supplies: a dead run's logs land in this run's record, no capture is opened, read or deleted through a link, and run-gates' Python temp files take unpredictable names

**Status:** SPECCED · rev-2 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 15 · ratified 2026-10-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-prompt-TOOL-dRedressedBar-21-1-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-1-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-2-revision.md) | research | TOOL-dRedressedBar-13 |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-3-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-3-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-4-revision.md) | research | TOOL-dRedressedBar-23 |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-5-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-5-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-6-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-6-revision.md) | research | TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-7-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-7-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md) | research | TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 |
| [2026-10-15-prompt-TOOL-dRedressedBar-24-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-24-brief.md) | research | TOOL-dRedressedBar-24 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing diff review (`reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md`)
confirmed one high, H1 (report id 1). It is promoted into this unit by the owner's ruling of
2026-10-15 in the README's Build-level rules, and built from this spec under the same recorded
override as round 4's promotions. The dead-run sweep that `TOOL-dRedressedBar-19` S38 added to
`tools/run-gates/measure_legs.py` treats a sibling `gate-profile.*/owner.json` under the shared temp
dir as trusted. It writes into the directory that file's `record` names, reads each `raw/<n>.out`
through links, and `write_atomic` opens a fixed temp name that a planted link redirects. A process
that can write only to the temp dir can therefore make an operator's profile copy any file the
operator can read into a directory of its choosing.

Writing this spec found the same class one step closer. `run_leg` opens each leg's own capture
with `open(capture, "wb")` (`measure_legs.py:777`), and `write_leg_capture` reads it and deletes it
by path (`:1431`, `:1441`). The capture sits in this run's own scratch dir, which `mktemp -d` makes
under the same temp dir (`:318`), so a link planted there is written, read and deleted through. The
owner ruled on 2026-10-15 to fold that into this unit
(`prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-4-revision.md`). The same record widens the temp
fix from `write_atomic` to its class: every Python writer under `tools/run-gates/` that writes a
fixed-name temp and renames it over its destination, which adds `write_held_stamp`
(`tools/run-gates/held_halves.py:320-327`).

This unit makes the profiler trust no path the temp dir supplies, on the one platform it runs on,
gives the kit's Python one temp-then-replace writer, and adds the static gate the record names.

| id | grade | item | sits in | closed by |
|---|---|---|---|---|
| 1 | HIGH | H1 | `derive_abandoned_scratch`, `write_recovered_logs`, `write_atomic`, `run_profile` | S1 to S5 |
| — | owner ruling | the run's own capture | `run_leg`, `run_admission`, `write_leg_capture` | S8 to S10 |
| — | the same record | the temp-name class | `write_held_stamp`, the `measure-legs selftest` guard | S4, S5, S11 |

The skeptic judged the record's fix SOUND. This spec departs from it in two places, each on a
measurement §4 records: the temp file's name, and a pin on the open handle beside the record's
`lstat` checks.

## 2. Scope (IN)

- **S1** — A recovered log never lands where `owner.json` says. `write_recovered_logs` writes every
  recovered log under this run's own `<run_dir>/recovered/<scratch name>/<n>.log.recovered`, the
  branch it already takes when the named record dir is gone (`measure_legs.py:1406-1407`).
  `derive_abandoned_scratch` returns the abandoned scratch dirs alone and no longer reads
  `owner.json`'s `record` (`:1384`). `run_profile` stops writing that key, so `owner.json` holds
  `pid` and `created` alone (`:1529-1530`). Observed by AC1.
  - **Readers:** S1 retires the `record` key of `owner.json`.
    by name: `tools/run-gates/measure_legs.py`, where `run_profile` writes it, `derive_abandoned_scratch`
    reads it and `test_scratch_sweep` plants it.
    by value: `write_recovered_logs` in `tools/run-gates/measure_legs.py`, which takes the value as its
    destination dir at `:1406-1407`. After S1 no code reads the value, and an older run's
    `owner.json` that still carries it is read for `pid` and `created` alone.
- **S2** — Nothing in a scratch dir is read through a link. Three new functions hold the rule, and
  none takes the job backend, because `write_leg_capture`, whose `(lg, final)` signature
  `TOOL-dRedressedBar-22` S2 calls, holds none.
  `read_plain_stat(root, parts, want)` `os.lstat`s each component of `<root>/<parts...>` in turn.
  Every component but the last must be a directory, and the last must be a directory or a regular
  file as `want` says. No component may carry an `st_reparse_tag`, and a regular file must have
  `st_nlink == 1`. It returns the last component's stat, or raises `OSError` naming the first
  component that fails.
  `check_pinned_handle(fd, root, parts)` reads `os.fstat(fd)`, which must be a regular file with
  `st_nlink == 1`, and the handle's final path, which must equal
  `os.path.join(os.path.realpath(root), *parts)` under `os.path.normcase`. It returns the `fstat`,
  or raises `OSError` naming the final path. `GetFinalPathNameByHandleW` gives the final path, with
  its `\\?\` prefix dropped and `\\?\UNC\` read as `\\`. The prototype joins
  `resolve_job_backend`'s table (`:687-704`), and `check_pinned_handle` calls
  `resolve_job_backend()` for it, so kernel32 is bound in one place. `msvcrt` is imported inside
  `check_pinned_handle`, since the module imports nothing Windows-only at top level.
  `read_scratch_file(root, parts)` runs `read_plain_stat`, opens the file with
  `os.O_RDONLY | os.O_BINARY`, and runs `check_pinned_handle`. It reads only when the `fstat` names
  the same `(st_dev, st_ino)` as the stat, and returns `(data, (st_dev, st_ino))` or raises
  `OSError`.
  `derive_abandoned_scratch` reads `owner.json` only through `read_scratch_file`, so a scratch dir
  or `owner.json` that is a link, a junction or a second name is left alone and unlisted.
  `write_recovered_logs(abandoned, run_dir)` lists `raw/` only once `read_plain_stat` passes it as a
  directory. Otherwise it records one entry naming `raw/`, with `log` null and `kept` opening
  `not read: `. It reads each capture only through `read_scratch_file`. A capture that fails is left
  in place, and its entry carries `log` null and `kept` opening `not read: `. Observed by AC2 and AC3.
  - **Readers:** S2 retires the plain path reads of a sibling scratch: the `open` of its
    `owner.json` and the `open(raw, "rb")` of each capture.
    by name: `derive_abandoned_scratch` in `tools/run-gates/measure_legs.py`, which opens
    `owner.json` (`:1375`), and `write_recovered_logs`, which opens each capture (`:1409`). A grep of
    the tree outside `memory/` finds no other site that reads either. `test_scratch_sweep` writes its
    plants with its own `open` (`:2560`) and reads none of them through these two.
    by value: `read_process_created`, which takes the `pid` and `created` read from `owner.json`, and
    `derive_redacted`, which takes each capture's bytes. After S2 both take the same values from
    `read_scratch_file`.
- **S3** — A sibling's capture is deleted only if it is still the file that was read. Before
  `os.remove`, `write_recovered_logs` calls `read_plain_stat` again. It deletes only when that passes
  and names the `(st_dev, st_ino)` that `read_scratch_file` returned. Otherwise the capture stays,
  and its entry's `kept` opens `not deleted: `. Observed by AC4.
  - **Readers:** S3 retires the unconditional `os.remove(raw)` that follows a recovery.
    by name: `write_recovered_logs` in `tools/run-gates/measure_legs.py` (`:1421`), the one site
    that spells it. `help/measure-legs.md`'s "What it writes" and the module docstring's sweep
    paragraph state the delete in prose, without a condition, and S6 rewrites both passages.
    by value: `test_scratch_sweep`, which reads the dead capture's absence after the run. It still
    observes that absence, because its dead plant is a plain file that S3 deletes. The new
    `not deleted: ` reason is read by `run_profile`'s start-of-run line (`:1587-1589`) and lands
    in the envelope's `raw_recovered`.
- **S4** — One temp-then-replace writer for the kit's Python. `tools/run-gates/held_halves.py`, the
  sibling `measure_legs.py` already imports (`:90`), gains `write_replace(path, data)`. It writes
  `data` (bytes) through
  `tempfile.mkstemp(dir=<the destination's dir>, prefix=<its name> + ".", suffix=".tmp")`, an
  unpredictable name opened `O_CREAT | O_EXCL` and owner-only, so no link can be planted at it in
  advance. It writes through `os.fdopen(fd, "wb")` and renames with `os.replace`. Any exception after
  the temp exists removes the temp and is raised again. `write_atomic` (`measure_legs.py:1022-1035`)
  calls `held_halves.write_replace` inside its existing `try`, and keeps its signature, its return
  value and its `WRITE_FAILURES` handling. `write_held_stamp` (`held_halves.py:320-327`) encodes its
  `<key>\t<value>\n` lines as UTF-8, calls `write_replace`, and keeps its signature and return value.
  Its failure still raises out of `run_combine`, as now. Observed by AC5.
  - **Readers:** S4 retires the fixed temp name `path + ".tmp"` in both writers, `write_atomic`'s
    `O_TRUNC` open and `write_held_stamp`'s text-mode `open(tmp, "w")`.
    by name: `write_atomic` in `tools/run-gates/measure_legs.py` and `write_held_stamp` in
    `tools/run-gates/held_halves.py`, the two sites a grep of the tree outside `memory/` finds
    spelling a fixed `.tmp` beside a replace or a rename in a Python file.
    by value: NO VALUE READERS — no code opens either temp by its name. A temp lives only from its
    open to the `os.replace` beside it, and S4 removes it on failure. `run-gates.test.sh:3237` plants
    a directory at a fixed `.tmp` name, but for the spawn floor's bash writer at `run-gates.sh:3792`,
    which F1 leaves out. The profiler's directory readers, `measure_scratch_bytes` (`:1111`), the
    fixture reader at `:1852` and `test_serial_run`'s record listing at `:2105`, read final names
    or sum bytes, and the held-halves selftest reads `held-green` by its final name
    (`held_halves.py:605`, `:610`).
- **S5** — The left-shift gate the record names, as a static arm over the class.
  `test_write_atomic_temp` parses every `*.py` file under `KITDIR`, the run-gates kit dir, found by
  `os.walk` at run time with `__pycache__` skipped. A file that does not parse reds the arm. Its
  population is every call of `os.replace` or `os.rename`. For each, the innermost enclosing function
  must call `tempfile.mkstemp` with a `dir` keyword and must call neither `os.open` nor `open`, and a
  call outside any function reds. The arm asserts that the population is non-empty and holds a call
  inside `write_replace`. The selftest's own staging functions are in the population, with no
  exemption, so AC4's swap is written to meet the predicate. Observed by AC6.
- **S6** — The docs say where a recovered log lands, what the sweep refuses, and what a planted
  capture does. In `help/measure-legs.md`, "What it writes" says a recovered log lands under
  `recovered/<scratch name>/` in the new run's own record. It says a capture reached through a link,
  a junction or a second name is not read, is left in place, and is named in `raw_recovered`. Its
  launch-failure sentence says a leg whose capture could not be made as a new file in this run's
  scratch reads `fail` with rc 1 and a `launch_error` opening `capture: `, having started nothing.
  The module docstring's "A DEAD RUN'S RAW CAPTURES ARE SWEPT" paragraph says the same with
  `TOOL-dRedressedBar-21`. The docstrings of `LaunchFailed`, `derive_abandoned_scratch`,
  `write_recovered_logs`, `write_leg_capture`, `write_atomic` and `write_held_stamp` state the new
  contract. Observed by AC7.
- **S7** — The record, in two passes. This unit's spec-writer pass, `<w21>`, runs before the build
  pass and gives specs 18 and 19 one revision each, as §4 "What this unit corrects in each spec"
  lists. The build pass writes no spec but this one's status and date cells. Every reading below
  goes to this unit's acceptance ledger under `memory/builds/dRedressedBar/build/`, carrying
  `**Serves:** journal TOOL-dRedressedBar-21`. Observed by AC8.
- **S8** — A leg's capture is a new file this run made. `run_profile` splits `scratch` once into
  its parent and its name, the `os.path.split(os.path.normpath(scratch))` that
  `derive_abandoned_scratch` makes (`:1364`). Each leg row (`:1594-1600`) gains `capture_at`,
  `(parent, (name, "raw", "<i>.out"))`, beside `capture`. A new `build_capture_file(root, parts)`
  runs `read_plain_stat(root, parts[:-1], want="dir")`, and requires `os.lstat` of the capture path
  to raise `FileNotFoundError`, so an entry already there, a dangling link included, is refused
  before any open. It then opens the path with
  `os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_BINARY`, mode `0o600`, and runs
  `check_pinned_handle`. On a failure after the open it closes the descriptor and raises `OSError`.
  It returns `(fd, (st_dev, st_ino))`. `run_admission` (`:1609-1635`) calls it before `run_leg`. A
  refusal makes the leg a failed launch in the shape S35 of `TOOL-dRedressedBar-19` gives one: no
  process, no job, no handle, rc 1, and `launch_error` reading `capture: <reason>`, and the run goes
  on. Like S35's branch, the refusal leaves `pending` as it is. On success the row takes `capture_id`, and `run_leg` gets the descriptor as a binary file
  object. `run_leg`'s last parameter becomes `stdout`, which it hands to `subprocess.Popen` as is,
  and `measure_job_children` passes `subprocess.DEVNULL` there (`:900`). `LaunchFailed`'s docstring
  (`:179-181`) names both `launch_error` forms. Observed by AC9.
  - **Readers:** S8 retires `run_leg`'s `open(capture, "wb")` and its `capture` parameter.
    by name: `run_leg` in `tools/run-gates/measure_legs.py`, which opens it, and its two callers,
    `run_admission`, which passes the leg's capture path, and `measure_job_children`, which passes
    the null device's path.
    by value: `subprocess.Popen` inside `run_leg`, which takes the file object as `stdout` and
    `stderr`, unchanged. The census's size read in `derive_stall_window` (`:1282`) and
    `write_leg_capture` read the capture by its path, which `capture` still holds. The record's
    `launch_error` is read by `write_leg_end` and the leg's printed line as an opaque string, and
    `test_launch_failure` reads its `launch: ` form, which a capture refusal does not take.
- **S9** — A leg's capture is read only if it is the file this run made. `write_leg_capture` keeps
  its `(lg, final)` signature. With no `capture_id` on the row it opens nothing and returns
  `unreadable: this run made no capture at <path>`. Otherwise it reads through
  `read_scratch_file(*lg["capture_at"])`, and reads the bytes only when the returned
  `(st_dev, st_ino)` equals `capture_id`. A failure or a mismatch returns a reason opening
  `unreadable: ` and writes no log. The reason reaches `raw_kept` through the run-end retry, as a
  read failure does now. Observed by AC10.
  - **Readers:** S9 retires `write_leg_capture`'s plain `open(lg["capture"], "rb")`.
    by name: `write_leg_capture` in `tools/run-gates/measure_legs.py`, the one site that spells it.
    by value: `derive_redacted`, which takes the bytes, and `write_leg_end` and the run-end loop,
    which read the returned reason into `raw_pending` and `raw_kept`. `test_serial_run` reads the
    log and the empty `raw/` after a plain run (`:2113-2124`), which S9 leaves as they are.
- **S10** — A leg's capture is deleted only if it is still the file that was read. Before
  `os.remove`, `write_leg_capture` calls `read_plain_stat(*lg["capture_at"], want="file")`. It
  deletes only when that passes and names `capture_id`. Otherwise the capture stays, and the
  function returns a reason opening `not deleted: `. A delete that fails keeps its existing reason.
  Observed by AC11.
  - **Readers:** S10 retires the unconditional `os.remove(lg["capture"])` that follows a log write.
    by name: `write_leg_capture` in `tools/run-gates/measure_legs.py`, the one site that spells it.
    by value: `write_leg_end`, which sets `raw_pending` from the reason, the run-end loop, which
    names a kept capture in `raw_kept`, and `test_serial_run`, which reads `raw/` empty after a
    plain run (`:2122-2124`). A plain capture this run made passes S10, so that arm still sees it
    deleted.
- **S11** — The static arm's leg is guarded by every file it parses. The `measure-legs selftest`
  row's `guard` in `tools/gate-legs.json` (`:1261-1273`) gains `{prefix}/run-gates/check-receipt.py`
  and `{prefix}/run-gates/regen.py` as exact files, after `{prefix}/run-gates/held_halves.py`. With
  them every `*.py` S5 parses at `bf42c5113` trips the leg. The product commit carries the
  kickoff-manifest re-stamp at its parent that the ratchet's staged check requires, as `809f794e4`
  did. A second commit, `<p21m>`, re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md` at
  the product commit after a section B re-read, with a `manifest-audit:` line in its body, as
  `cafbbc460` did. Observed by AC12.

## 3. Non-goals (OUT)

- The bash writers under `tools/run-gates/` that write a fixed-name temp and `mv` it into place, and
  the Python heredoc in `run-gates.sh` whose temp is `<key>.tmp.<pid>` (`:5472-5475`). They are F1's,
  and this spec is written to its recommendation: they stay as they are here.
- A bug-class checklist entry under `memory/gotchas/`. The record names it beside the static arm,
  and the brief admits either. S5 is the gate, and the entry is a separate document by M2.
- Any change to `owner.json`'s owner proof (`read_process_created`, `:1337-1356`), to which siblings
  count as abandoned, or to the `raw_recovered` entry's keys. An entry still carries `raw`, `log`
  and, where the capture stays, `kept`.
- `write_record_line` (`:1038-1048`), `write_envelope` and every write under the run's record dir.
  The record dir is under the operator's git dir or `--out`, not the shared temp dir.
- The census's size read of a running capture, `os.path.getsize(lg["capture"])` (`:1282`). It
  follows a link, and it reads a size and no bytes.
- A race in either delete. S3 and S10 narrow it to the moment between the second `read_plain_stat`
  and `os.remove`. A directory swapped in at that moment can still remove another file named
  `<n>.out`. `os.remove` on Windows takes a path, and Python's `os.open` does not share delete
  access, so the file cannot be removed through the read handle.
- No kit version moved. Run-gates already moved from 1.40 to 1.41 on this branch, and the lander
  mints a later move (`tools/govkit/govkit.py:13380-13386`, "WHERE THE BUMP IS MADE").
- No change to `tools/run-gates/README.md`, whose gate-profiler section does not describe the
  sweep, and no change to `tools/gate-legs.json` beyond S11's two guard paths.

### Edges

- **consumes-from** `TOOL-dRedressedBar-18` — `write_atomic`, `run_profile`, `run_leg` and
  `write_leg_capture`, which S1, S4, S8, S9 and S10 change. Without them there is no writer to fix.
- **consumes-from** `TOOL-dRedressedBar-19` — S38's sweep: `derive_abandoned_scratch`,
  `write_recovered_logs`, the `owner.json` write and AC38's arm `test_scratch_sweep`, which S1 to
  S3 change and AC1 and AC2 extend; and S35's failed-launch shape, which S8 reuses.
- **hands-off** `TOOL-dRedressedBar-24` — the bash fixed-name temp writers under `tools/run-gates/`, in
  `run-gates.sh`, `post-merge.sh` and `run-selftests.sh`, and the Python writer in the `run-gates.sh`
  heredoc, which F1 resolved as (a) to that unit, with its bash-side static check.

## 4. Design

### Evidence, read at `bf42c5113` on 2026-10-15

`bf42c5113`'s `tools/`, `help/`, `skills/` and `.githooks/` equal `e114f1356`'s, the reviewed range's
tip (`git diff --stat e114f1356 HEAD -- tools help .githooks skills` prints nothing). So every line
the record cites reads the same here, and red halves run over `e114f1356`. The record's citations
hold: `derive_abandoned_scratch` is `:1359-1385` and returns `owner.get("record")` at `:1384`;
`write_recovered_logs` picks `dest_dir` at `:1406-1407` after `os.path.isdir(record)` alone, opens
the capture with `open(raw, "rb")` at `:1409` and removes it at `:1421`; `write_atomic` opens
`path + ".tmp"` with `O_WRONLY | O_CREAT | O_TRUNC` at `:1025-1027`; and `run_profile` calls the
sweep at `:1545`.

The leg's own capture: `SCRATCH_SCRIPT` makes the scratch with `mktemp -d` under `TMPDIR` and its
`raw/` with `mkdir` (`:318-319`). Each leg row's `capture` is `<scratch>/raw/<i>.out` (`:1597`).
`run_leg` opens it with `open(capture, "wb")` (`:777`), and `run_admission` calls `run_leg` with it
(`:1615`), catching `LaunchFailed` alone (`:1616-1620`). `measure_job_children` calls `run_leg` with
`os.devnull` (`:900`). `write_leg_capture` opens the capture with `open(lg["capture"], "rb")`
(`:1431`) and calls `os.remove(lg["capture"])` (`:1441`). It is called with `(lg, final)` at
`:1650` and `:1758`, and `TOOL-dRedressedBar-22` S2 spells the same call.

The temp-name class: `grep -nE 'os\.(replace|rename)|\.tmp'` over every `*.py` under
`tools/run-gates/` finds `measure_legs.py:1025`, `:1030` and `held_halves.py:322`, `:326`, and
nothing else. The tree holds 12 such files, PINNED at `bf42c5113`. `write_held_stamp` writes
`<common dir>/held-green` (`held_halves.py:339`, `:381`). The `measure-legs selftest` guard
(`tools/gate-legs.json:1261-1273`) names `measure_legs.py`, `profile_bar.py`,
`derive-ceilings.py`, `held_halves.py` and `fixtures/measure-legs/`, and not `check-receipt.py` or
`regen.py`.

Probes, PINNED, run on node d on 2026-10-15 under Python 3.12.10, each in a scratch dir:

| Probe | Reading |
|---|---|
| `os.open` with `O_CREAT \| O_EXCL` over a dangling file symlink | opened, and created the link's target |
| the same with `O_TRUNC` and no `O_EXCL` | wrote the link's target |
| `os.remove` of a file symlink | removed the link and left the target |
| `os.lstat` of a junction made by `_winapi.CreateJunction` | `S_ISDIR` true, `S_ISLNK` false, `st_reparse_tag` `0xa0000003` |
| `os.lstat` of a file reached through that junction | a regular file, `st_reparse_tag` 0 |
| `os.lstat` of a file symlink | `S_ISLNK` true, `st_reparse_tag` `0xa000000c`; this host makes one |
| `os.lstat` of a dangling file symlink | succeeds |
| `os.link` to a file, unprivileged | succeeds; `os.lstat` and `os.fstat` both read `st_nlink` 2, and equal `st_ino` |
| `open(<a hard link to secret.txt>, "wb")`, then a write | `secret.txt` reads the written bytes |
| `os.open` with `O_CREAT \| O_EXCL` over an existing hard link | `FileExistsError` |
| `os.remove("<s>/raw/0.out")` where `raw` is a junction to `victim/` | `victim/0.out` is gone |
| `tempfile.mkstemp(dir=d, prefix="held-green.", suffix=".tmp")` | a name such as `held-green.0hy7v7ux.tmp` |
| `hasattr(os, "O_NOFOLLOW")` | False |
| `GetFinalPathNameByHandleW` of a plain file's descriptor | its path with a `\\?\` prefix, equal under `normcase` to `realpath` of the parent joined to the name |
| the same, opened through a junctioned `raw/` | the junction target's path, which differs |

The first row is why S4 departs from the record's part (3). Removing the stale entry and then
opening the fixed name with `O_EXCL` leaves a window. In that window a link re-planted at the name
is followed, and its target is created. The fixed name is what makes planting possible, so S4
removes the name rather than racing for it.

The capture cannot take an unpredictable name, because the sweep, the census and every reader of
`raw_kept` find it as `raw/<i>.out`. So S8 refuses any entry at the name, `O_EXCL` closes every
case but the dangling link re-planted after that check, and the pin catches that one: the handle's
final path is the link target's. The empty file `O_EXCL` made there is left, and §5 says so.

The last two rows are why S2 pins the handle. The record's `lstat` checks are a check followed by a
use of the same path. A capture swapped for a link, or `raw/` swapped for a junction, between the
two reads through. A hard link is a regular file to `lstat`, so `st_nlink` is the only sign of it.

### A capture's life after this unit

```
run_profile
  owner.json  <- write_atomic {"pid", "created"}                        S1, S4
  derive_abandoned_scratch(api, scratch) -> [d, ...]
    for each gate-profile.* sibling: read_scratch_file(parent, (name, "owner.json"))
      fails -> left alone, unlisted                                      S2
  write_recovered_logs(abandoned, run_dir)
    read_plain_stat(parent, (name, "raw"), want="dir") fails -> one entry, not read   S2
    for each <n>.out: read_scratch_file(parent, (name, "raw", f))
      fails -> entry kept "not read: ...", capture left in place         S2
      ok    -> write_atomic(<run_dir>/recovered/<name>/<n>.log.recovered)   S1, S4
               read_plain_stat again, same (st_dev, st_ino) -> os.remove
               otherwise -> entry kept "not deleted: ..."                S3
  run_admission(i)
    build_capture_file(parent, (own, "raw", "<i>.out")) -> (fd, capture_id)   S8
      fails -> leg fail, rc 1, launch_error "capture: ...", nothing started
      ok    -> run_leg(..., stdout=<fd as a binary file>)
  write_leg_capture(lg, final)
    no capture_id -> "unreadable: this run made no capture at ..."       S9
    read_scratch_file(*capture_at), same (st_dev, st_ino) as capture_id
      fails -> "unreadable: ...", no log                                 S9
      ok    -> write_atomic(<run_dir>/<i>.log)                           S4
               read_plain_stat again, names capture_id -> os.remove
               otherwise -> "not deleted: ..."                           S10
```

`parent` is the directory holding this run's own scratch dir, which the operator's `TMPDIR`
names, and `name` is a `gate-profile.*` entry of `os.listdir(parent)`. `own` is this run's own
scratch name, which `mktemp -d` returned. None of them comes from a file another process wrote. The
envelope's `raw_recovered` keeps its shape, and the start-of-run line at `:1587-1589` already prints
`not recovered; KEPT: <reason>` for an entry with no log.

### The writer S4 extracts

`write_atomic` and `write_held_stamp` are the kit's two Python instances of one kind, a temp file
renamed over its destination, so the charter's `[reuse]` rule extracts one writer at this second
instance rather than spelling `tempfile.mkstemp` twice. It lives in `held_halves.py` because
`measure_legs.py` already imports that sibling for `load_manifest` (`:90`), and the reverse import
would be circular. `write_replace` raises, as `write_held_stamp` does today, and `write_atomic` keeps
turning that into a named, remembered failure. `tempfile` opens its temp in binary mode and
owner-only, which matches `write_atomic`'s `0o600`. `held-green` becomes owner-only too, and every
reader of it is the operator's own process.

### The arms

`test_scratch_sweep`, AC38's arm since unit 19, gains the hostile plants in the same run, so one
profile observes AC38, AC1 and AC2. Its dead plant's `record` moves from `<out>/dead-record` to a
directory outside the out root, which is the record's plant. The masked-log read moves to
`<run>/recovered/gate-profile.dead0000/0.log.recovered`. Every plant's owner is the arm's real
exited child, never a synthetic pid.

`test_scratch_read_pin` is in-process. The `lstat` checks settle every static plant before the open,
so no static plant reaches the final-path compare or the delete-time compare
(`guard-above-a-fold-makes-its-fallback-dead`). The arm reaches each of them by staging the state
an attacker leaves after a check has passed. For AC3 it rebinds `os.lstat` to `os.stat`, which is
what a check sees once a junction is swapped in after it ran. For AC4 it rebinds `derive_redacted`
to a wrapper that swaps the capture before passing the bytes on. Both rebindings are restored in a
`finally`.

`test_capture_pin` covers the leg's own capture. For AC9 it rebinds `build_scratch` to a wrapper that
calls the real one and then plants a hard link at `raw/0.out`, which is the window an attacker has
between the scratch's `mktemp -d` and the capture's open. The rest of AC9, and AC10 and AC11, call
`build_capture_file` and `write_leg_capture` in-process over plants the arm makes, and stage the
post-check state as `test_scratch_read_pin` does.

`test_write_atomic_temp` holds S5's static predicate and the behaviour S4 promises, through both
callers of `write_replace`. A hard link reproduces the write-through without privilege. The file
symlink adds the dangling-target case on a host that can make one.

### What this unit corrects in each spec

Only `gov-spec-writer` writes spec files, and scratch-guard admits a builder's spec edit only to the
status and date cells of the spec its card routes (`tools/hooks/scratch-guard.js:94-99`). So these
rows are `<w21>`, this unit's spec-writer pass. The main loop dispatches it with this table as its
brief, after this spec is committed and before the build pass. Its subject names
`TOOL-dRedressedBar-21`. Each target takes one rev bump, one revision line naming
`TOOL-dRedressedBar-21` and H1, and keeps its CLOSED status. A build pass that finds no `<w21>`
returns that to the main loop before any write.

| Spec | What moves |
|---|---|
| 18 | §3 Edges gain the mirror below; revision line, which also names the owner's ruling on the capture. No sentence of spec 18 is false after this unit: `:351`, `:537`, `:520` and `:752-755` still hold, and so does `:528-536`, because a capture kept for any reason is named in `raw_kept` and the deletes it lists stay the only ones. |
| 19 | S38's `owner.json` contents lose "its record dir", and its destination sentence names `recovered/<scratch name>/<i>.log.recovered` under this run's own record alone, with a pointer to `TOOL-dRedressedBar-21`. §4's `owner.json holds` line (`:549`) loses `record`. §3 Edges gain the mirror below. The revision line also states that AC38's arm now plants its record outside `<o>` and reads its log under `<r>/recovered/`, observed by this spec's AC1. S35 holds as written: it states the four call failures, and a refused capture is a fifth cause this unit states. |

The two mirror bullets, worded so each backticked token occurs in this spec:

- spec 18: `- **hands-off** \`TOOL-dRedressedBar-21\` — \`write_atomic\`, whose fixed \`.tmp\` name that unit replaces with a \`tempfile.mkstemp\` temp (closing review round 1, H1), and the capture's open in \`run_leg\` and its read and delete in \`write_leg_capture\`, which that unit holds to the file \`build_capture_file\` made (the owner's ruling of 2026-10-15).`
- spec 19: `- **hands-off** \`TOOL-dRedressedBar-21\` — the S38 sweep: \`derive_abandoned_scratch\`, \`write_recovered_logs\`, the \`owner.json\` write whose \`record\` key that unit retires, and AC38's arm \`test_scratch_sweep\` (closing review round 1, H1).`

### Order, and the symbol index

Order 15 is one above unit 19's 14. Units 18 and 19 built every function this unit changes in
`measure_legs.py`. `TOOL-dRedressedBar-22` changes the same file and orders after this unit, and
calls `write_leg_capture` with the signature S9 keeps. `TOOL-dRedressedBar-23` edits the
`govkit selftest` row of `tools/gate-legs.json`, below S11's row, and re-stamps the manifest after
this unit's re-stamp. This unit mints functions in `measure_legs.py` and `held_halves.py`, so the
build pass runs `python tools/codebase-map/gen_map.py --write` before its product commit, as unit 19
did. `tools/gate-legs.json` is on the kickoff manifest's `watch:` line
(`memory/guides/SESSION-KICKOFF.md:6`), so S11's re-stamps are owed.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `read_plain_stat`, `read_scratch_file` | functions in `measure_legs.py` | `py.function`, `read` |
| `check_pinned_handle` | a function in `measure_legs.py` | `py.function`, `check` |
| `build_capture_file` | a function in `measure_legs.py` | `py.function`, `build` |
| `write_replace` | a function in `held_halves.py` | `py.function`, `write` |
| `test_scratch_read_pin`, `test_capture_pin`, `test_write_atomic_temp` | selftest arms | `py.function`, `test` |
| `capture_at`, `capture_id` | leg-row keys | none |
| `stdout` | `run_leg`'s last parameter, renamed from `capture` | none |
| `GetFinalPathNameByHandleW` | a kernel32 prototype in `resolve_job_backend`'s table | none; the Win32 name |
| `not read: `, `not deleted: ` | `kept` and kept-reason prefixes | none |
| `capture: ` | a `launch_error` prefix | none |

Each function name answered OK under `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
on 2026-10-15. A grep of `tools/` and `skills/` for each new identifier found none of them at
`bf42c5113`.

### Files touched (estimate)

- `tools/run-gates/measure_legs.py`
- `tools/run-gates/held_halves.py`
- `tools/gate-legs.json`
- `help/measure-legs.md`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/`
- `memory/builds/dRedressedBar/build/`

Specs 18 and 19 are `<w21>`'s write set, not the build pass's.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| Accept `record` when its realpath is a direct child of the same out root and no reparse point, the record's second option | a planted file still chooses which of the operator's records takes a log, and can overwrite a log recovered there; the log lands beside its own run only when both runs used one `--out`; and the roster's mechanism for this unit is that the sweep "trusts no path a shared temp dir supplies" | Rejected; S1 never follows it |
| The record's part (3) as written: remove the stale entry, then `O_EXCL` at the fixed name | the probe in §4: on this platform `O_EXCL` over a dangling link creates the target, so a link re-planted after the remove is written through | Rejected; S4 removes the fixed name |
| `lstat` and skip alone, the record's part (2) as written | a check-then-use by path: a swap after the check reads through, and a hard link reads as a regular file to `lstat` | Kept as the first step; S2 adds `st_nlink` and the handle pin |
| `O_NOFOLLOW` on each open | absent here (`hasattr(os, "O_NOFOLLOW")` is False), and the tool runs only on Windows | Rejected |
| A bug-class checklist entry as the left-shift gate | a checklist entry asks and a static arm reds, and the entry is its own document (M2) | Rejected for S5 |
| An unpredictable name for each leg's capture, as S4 gives a temp | the sweep keys on `raw/<i>.out`, and so do the census and `raw_kept`; refusing any entry, `O_EXCL` and the pin close the same cases at the fixed name | Rejected; S8 |
| The job backend passed to each scratch helper | `write_leg_capture`'s `(lg, final)` signature carries none, and unit 22 calls it so; `check_pinned_handle` calls `resolve_job_backend()`, which keeps one kernel32 table | Rejected |
| A second `tempfile.mkstemp` writer in `held_halves.py` beside `write_atomic` | two spellings of one kind, the copy the charter's `[reuse]` rule forbids at the second instance | Rejected; S4 extracts `write_replace` |
| The static arm over the files its leg's guard names, rather than every `*.py` | a writer added to an unguarded file would escape both the arm and the guard | Rejected; S5 walks the dir and S11 guards what it finds |

## 5. Production-readiness checklist

- security — Closes H1, and the same class at the run's own capture. A planted `owner.json` chooses
  no destination, and a link, junction or second name planted in a dead scratch is neither read nor
  deleted. A link planted at this run's capture path fails that leg before anything runs, and the
  capture is read and deleted only while it is the file this run made. That holds against a swap made
  after a check, because each open is pinned to its final path. No temp file under
  `tools/run-gates/`'s Python is opened at a name a planted link can occupy. What it does not check:
  a plain file planted in a dead scratch is still redacted into this run's own `recovered/`, so a
  temp-dir writer can place `<n>.log.recovered` files of its own bytes there, one per planted
  capture. A dangling link re-planted at a capture path between S8's `lstat` and its open leaves an
  empty file at the link's target, though the pin refuses the capture. The census's size read
  follows a link (§3). The deletes keep the race §3 states. The bash writers and the heredoc writer
  F1 names keep their fixed names. The static arm sees `os.replace` and `os.rename` called as
  attributes of `os`, so a `from os import replace` writer escapes it, and a `*.py` added later under
  `tools/run-gates/` outside the guard is parsed but does not trip the leg.
- perf / scale — N/A — at most five `lstat`s, one `fstat` and one final-path call per capture or
  `owner.json`, on paths taken once per leg and once per run.
- error / empty / loading states — A refused `owner.json` or scratch dir is skipped as an unreadable
  one already is. A refused `raw/` or sibling capture is named in `raw_recovered` with `log` null and
  its reason, and the run goes on. A refused own capture is a failed leg with its reason, and the run
  goes on. A `write_atomic` failure removes its temp and is named as before, and a
  `write_held_stamp` failure removes its temp and raises as before.
- observability — Each refused or kept sibling capture prints the existing start-of-run line with
  its reason. A refused own capture prints the leg's `launch_error` and lands in `raw_kept` with its
  path, so a hostile plant is visible to the operator.
- risks — A plant that is refused is left in place, so every later run names it again until someone
  removes it. That is the intended signal. The temp name moves from `<dest>.tmp` to a random
  `<dest>.<random>.tmp`, and no reader depends on the old name (S4's readers). The final-path
  compare relies on `os.path.realpath(root)` and the handle agreeing on long names and drive
  spelling, which §4's probe showed for `%TEMP%` on node d. A scratch under a mapped or subst drive
  is resolved by both. Editing `tools/gate-legs.json` trips the run-gates canaries and the
  kickoff-manifest ratchet, which S11 re-stamps.
- testing — AC1 to AC12 are direct python probes over the profiler, in-process calls of the new
  functions, an `ast` read, a JSON read, a grep of the help page and `git` reads of `<w21>` and
  `<p21m>`. The arms are declared in §7.
- migration — An older run's `owner.json` that names a `record` is read for its owner alone. Logs
  that earlier runs recovered into their own record dirs stay there. `raw_recovered` and `raw_kept`
  keep their shapes, and `launch_error` gains a second form beside the first.
- user docs — `help/measure-legs.md` "What it writes", S6.

## 6. Acceptance criteria

Some placeholders recur below. `<p21>` is this unit's product commit, `<p21m>` its manifest
re-stamp commit and `<w21>` the commit of its spec-writer pass, each named in this unit's ledger.
`<ml>` is `python tools/run-gates/measure_legs.py` and `<pre>` is `e114f1356`. `<t>` is a fresh dir
under `%TEMP%`, and `<o>` an out root inside it. `<r>` is the run dir the tool prints. A red half
"over `<pre>`" runs the file from a local `git clone` of gov under `%TEMP%`, checked out at `<pre>`.
Every command runs from the worktree root on node d. A dead owner is a child process the probe
started and let exit, named by its own pid and creation time, as AC38's. `TMPDIR` is `<t>/sweep` as
the resolved bash spells it, as `test_scratch_sweep` sets it. `<secret>` is `<t>/secret.txt`,
holding `SECRET-TOKEN=abc123`.

- **AC1** — A python probe plants `<t>/sweep/gate-profile.dead0000`, owned by a dead owner whose
  `owner.json` names `record` as `<t>/elsewhere`, an existing dir outside `<o>`. Its `raw/0.out`
  holds `https://u:s3cret@example.invalid/`. The probe then runs
  `<ml> --serial --legs <a one-leg spawn.py manifest> --out <o>`. Afterwards `<t>/elsewhere` holds
  no file, and `<r>/recovered/gate-profile.dead0000/0.log.recovered` carries `://***:***@`. The
  envelope's `raw_recovered` entry for that capture names that log. The run's own `owner.json`,
  read from the envelope's `scratch` before the probe removes it, has exactly the keys `pid` and
  `created`.
  Red when: over `<pre>`, `<t>/elsewhere/0.log.recovered` exists and the run's `owner.json` carries
  `record`.
- **AC2** — In the same run, the probe also plants, each owned by the dead owner with `record`
  naming `<t>/elsewhere`, these scratch dirs beside `<secret>`. `gate-profile.hln0000` has a
  `raw/0.out` hard-linked to `<secret>`. `gate-profile.sym0000` has a `raw/0.out` that is a file
  symlink to it. `gate-profile.jnr0000` has a `raw/` that is a junction to `<t>/outside-raw/`, which
  holds a `0.out` of the same bytes. `gate-profile.jnd0000` is itself a junction to
  `<t>/outside-scratch/`, which holds a dead `owner.json` and a `raw/0.out` of the same bytes.
  Afterwards `SECRET-TOKEN` occurs in no file under `<o>` or `<t>/elsewhere`. `<secret>`,
  `outside-raw/0.out` and `outside-scratch/raw/0.out` each still hold their bytes, and the hard link
  and the symlink still exist. `raw_recovered` holds an entry for each of the two links' captures
  and for `gate-profile.jnr0000`'s `raw/`. Each has `log` null and a `kept` opening `not read: `. No
  entry names `gate-profile.jnd0000`. The plain dead capture of AC1 is still recovered in the same
  run, so the refusals are not a sweep that read nothing.
  Red when: over `<pre>`, `SECRET-TOKEN` lands in `<t>/elsewhere` and `outside-raw/0.out` is deleted.
  fixture: the file symlink needs Developer Mode or the symlink privilege. Node d made one on
  2026-10-15. On a host that cannot, the arm prints `UNEXERCISED` for that plant alone and counts no
  assertion for it. The hard link and both junctions need no privilege and are always graded.
  cost: one profile of one leg, seconds.
- **AC3** — A python probe makes `<t>/gate-profile.pin0000/raw` a junction to a dir holding
  `0.out` = `SECRET`. With `os.lstat` rebound to `os.stat` for the call, it calls
  `measure_legs.read_scratch_file("<t>", ("gate-profile.pin0000", "raw", "0.out"))`.
  The call raises `OSError`, and its message names the junction target's final path.
  Red when: a copy with the final-path compare taken out of `check_pinned_handle` returns
  `b"SECRET"`.
- **AC4** — A python probe makes a dead scratch `<t>/gate-profile.swp0000` with a plain
  `raw/0.out` = `https://u:s3cret@example.invalid/`. It rebinds `measure_legs.derive_redacted` to a
  wrapper that first writes `swapped` through `tempfile.mkstemp(dir=<the capture's dir>)` and
  `os.fdopen`, and `os.replace`s that file over the capture. It then calls
  `measure_legs.write_recovered_logs(["<t>/gate-profile.swp0000"], "<t>/run")`. Afterwards
  `raw/0.out` still exists and reads `swapped`. The returned entry carries a non-null `log` and a
  `kept` opening `not deleted: `.
  Red when: a copy with S3's identity compare taken out deletes the swapped-in file.
- **AC5** — A python probe makes `<t>/a` and `<t>/b`, and hard-links `<t>/a/x.json.tmp` to
  `<t>/b/outside.txt`, which holds `outside-bytes`. `measure_legs.write_atomic("<t>/a/x.json", b"new")`
  returns True. Right after that call, `outside.txt` and the planted `x.json.tmp` read
  `outside-bytes`, `x.json` reads `new`, and `os.listdir("<t>/a")` is exactly `x.json` and
  `x.json.tmp`. Where `os.symlink` succeeds, `<t>/a/y.json.tmp` is a dangling link to
  `<t>/b/made-by-link`, and `write_atomic("<t>/a/y.json", b"y")` leaves `made-by-link` absent.
  `write_atomic` onto `<t>/a/sub`, an existing directory, returns False and leaves no `sub.*.tmp` in
  `<t>/a`. Then, in `<t>/gd`, `held-green.tmp` is hard-linked to `outside.txt`, and
  `held_halves.write_held_stamp("<t>/gd", (("sha", "x"),))` returns `<t>/gd/held-green`, which reads
  `sha\tx\n`, while `outside.txt` still reads `outside-bytes` and `os.listdir("<t>/gd")` is exactly
  `held-green` and `held-green.tmp`. Over `<t>/gd2`, where `held-green` is a directory, the call
  raises `OSError` and leaves no `held-green.*.tmp`.
  Red when: over `<pre>`, `outside.txt` reads `new` after `write_atomic`, or `sha\tx\n` after
  `write_held_stamp`, and `made-by-link` exists.
- **AC6** — `python -c` walks `tools/run-gates/` for every `*.py` outside `__pycache__` and parses
  each with `ast`. The calls of `os.replace` or `os.rename` are a non-empty set. Each one's innermost
  enclosing function calls `tempfile.mkstemp` with a `dir` keyword and calls neither `os.open` nor
  `open`, and one of them sits inside `write_replace`.
  Red when: over `bf42c5113`, the set is the two calls inside `write_atomic` and `write_held_stamp`,
  and each fails: `write_atomic` calls `os.open`, `write_held_stamp` calls `open`, and neither calls
  `tempfile.mkstemp`.
  figure: the population is DERIVED at observation. At `bf42c5113` it was 2, PINNED on 2026-10-15.
- **AC7** — `grep -c "in that run's record dir" help/measure-legs.md` prints 0. The page's "What it
  writes" section carries `recovered/<scratch name>/`, `left in place` and `capture: `.
  `ast.get_docstring` of `measure_legs.py` carries `TOOL-dRedressedBar-21`, and `LaunchFailed`'s
  docstring carries `capture: <reason>`.
  Red when: the page still sends a recovered log to the dead run's record dir, as at `<pre>`, or
  names one `launch_error` form alone.
- **AC8** — `git diff <w21>~1 <w21> -- memory/builds/dRedressedBar/spec/` shows specs 18 and 19,
  each with one header rev change and one new revision line naming `TOOL-dRedressedBar-21` and H1.
  Both carry a CLOSED header on each side. Each spec's §3 carries
  `` **hands-off** `TOOL-dRedressedBar-21` ``, and spec 18's names `build_capture_file`. Spec 19's
  S38 at `<w21>` carries no `<record>/<i>.log.recovered`. `git diff --name-only <p21>~1 <p21> -- memory/builds/dRedressedBar/spec/`
  and the same over `<p21m>` name no file but this spec. The ledger S7 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-21`.
  Red when: a target takes no bump or two, a mirror is missing, S38 still names the owner's record,
  or a build-pass commit writes another spec.
- **AC9** — A python probe runs `measure_legs.main` in-process with
  `--serial --legs <a one-leg spawn.py manifest> --out <o>`, with `measure_legs.build_scratch`
  rebound to a wrapper that calls the real one and then hard-links `<scratch>/raw/0.out` to
  `<secret>`. `main` returns 0. The leg's `<i>.json` reads verdict `fail`, rc 1 and a `launch_error`
  opening `capture: `. `<secret>` still reads `SECRET-TOKEN=abc123`, the hard link still exists, and
  the envelope's `raw_kept` names that path with a reason opening `unreadable: `. In-process, with
  `<t>/gate-profile.cap0000/raw/` made as plain dirs,
  `build_capture_file("<t>", ("gate-profile.cap0000", "raw", "1.out"))` over a dangling file symlink
  to `<t>/made-by-capture` raises `OSError` and leaves `made-by-capture` absent. The call for `3.out`
  in the same `raw/` returns a descriptor whose `fstat` names the `(st_dev, st_ino)` it returns.
  With `<t>/gate-profile.cjn0000/raw` a junction to `<t>/cap-target/` and `os.lstat` rebound to
  `os.stat`, the call for `("gate-profile.cjn0000", "raw", "2.out")` raises `OSError` naming the
  junction target's final path.
  Red when: over `<pre>`, the same rebinding of `build_scratch` leaves `<secret>` holding the leg's
  output. A copy of `build_capture_file` without the `lstat` refusal creates `made-by-capture`, and
  one without the pin returns a descriptor for `2.out`.
  fixture: the dangling symlink needs the symlink privilege, as AC2's; without it that one case
  prints `UNEXERCISED` and counts no assertion.
- **AC10** — A python probe makes `<t>/gate-profile.rd0000/raw/` as plain dirs, calls
  `build_capture_file` for `<t>/gate-profile.rd0000/raw/0.out`,
  writes `https://u:s3cret@example.invalid/` through the descriptor and closes it, and builds the
  row `{"capture", "capture_at", "capture_id", "log": "<t>/0.log", "left_running": 0}`. It then
  removes the capture and hard-links `raw/0.out` to `<secret>`. `measure_legs.write_leg_capture(lg, True)`
  returns a string opening `unreadable: `, `<t>/0.log` does not exist, `<secret>` still reads its
  bytes, and the hard link still exists. The same call with `raw/0.out` replaced by a plain file
  holding `planted` returns `unreadable: ` and writes no log. With the row's `capture_id` absent, the
  call returns `unreadable: this run made no capture at` and the path.
  Red when: over `<pre>`, `write_leg_capture(lg, True)` over the hard-link plant writes a `<t>/0.log`
  carrying `SECRET-TOKEN` and removes the link.
- **AC11** — A python probe makes the row of AC10 over a plain capture holding
  `https://u:s3cret@example.invalid/`, and `<t>/victim/0.out` holding `victim`. It rebinds
  `measure_legs.derive_redacted` to a wrapper that removes `raw/` with `shutil.rmtree`, makes `raw`
  a junction to `<t>/victim` with `_winapi.CreateJunction`, and then passes the bytes on.
  `measure_legs.write_leg_capture(lg, True)` returns a string opening `not deleted: `, `<t>/0.log`
  carries `://***:***@`, and `<t>/victim/0.out` still reads `victim`.
  Red when: over `<pre>`, the same staging deletes `<t>/victim/0.out` through the junction, and a
  copy with S10's identity compare taken out does the same.
- **AC12** — A python program loads `tools/gate-legs.json`. With `{prefix}` read as `tools`, every
  `*.py` under `tools/run-gates/` outside `__pycache__` is the exact path or under a directory entry
  of the `measure-legs selftest` row's `guard`, which names `{prefix}/run-gates/check-receipt.py`
  and `{prefix}/run-gates/regen.py`. The `last-audit:` line of `memory/guides/SESSION-KICKOFF.md`
  names a commit at which `git show <sha>:tools/gate-legs.json` holds both paths, and
  `git log -1 --format=%B <p21m>` carries `manifest-audit:`.
  Red when: over `bf42c5113`, `check-receipt.py` and `regen.py` are outside that guard.

## 7. Gates

`measure-legs selftest` · `held-halves selftest` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `testsuite counts (every bar self-test prints one)`

The line is a floor. It joins §4 Files touched against the guards in `tools/gate-legs.json`, with
`BROAD_LEG_FLOOR` applied, which owes `measure-legs selftest`, `recall floor`, `recall floor arms`,
`run-gates canary` and `run-gates gov canary`. It adds the unguarded legs the change moves: the
held-halves selftest over `write_held_stamp`, the manifest ratchet, the spec and ledger, the new
names, the regenerated symbol index, the shipped kit's bytes and the selftest's assertion count.

New arm: tools/run-gates/measure_legs.py --selftest · covers AC1 AC2 · `test_scratch_sweep` with `write_recovered_logs`' destination set back to the owner's `record` and with `read_scratch_file` replaced by a plain `open`, each on a copy in the selftest's temp dir · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC3 AC4 · `test_scratch_read_pin` with the final-path compare taken out, and with the identity compare before `os.remove` taken out · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC5 AC6 · `test_write_atomic_temp` with `write_atomic` restored to `os.open(path + ".tmp", O_WRONLY | O_CREAT | O_TRUNC)`, and again with `write_held_stamp` restored to `open(path + ".tmp", "w")` · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC9 AC10 AC11 · `test_capture_pin` with `run_leg` restored to `open(capture, "wb")`, with `write_leg_capture`'s read restored to a plain `open`, and with its identity compare before `os.remove` taken out · none

AC12 is a one-time read of the manifest at the close, held by no arm. The main loop observes each
arm red, then green, at the close, and runs the bar once after the last unit is terminal.

## 8. Open questions

- **F1 — Does this unit also take the bash fixed-name temp writers under `tools/run-gates/`?** The
  brief asks for every fixed-name temp-then-replace writer under that dir. A grep finds two kinds.
  The Python kind is S4's two writers. The bash kind is 19 `mv` sites over a `.tmp` name, in
  `run-gates.sh` (16), `post-merge.sh` (2) and `run-selftests.sh` (1), counted per non-test `.sh` by
  `grep -cE 'mv -f? ?"[^"]*\.tmp'`, PINNED at `bf42c5113` on 2026-10-15. Beside them is one Python
  writer inside a `run-gates.sh` heredoc, whose temp is `<key>.tmp.<pid>` (`:5472-5475`). Some bash
  sites write under `$WORK`, which `mktemp -d` makes under the ambient temp dir (`run-gates.sh:2212`),
  so H1's planter reaches them. Others write under the git dir. `run-gates.test.sh:3237` plants a
  directory at the spawn floor's fixed `.tmp` to stage a write failure, so that suite reads the
  fixed name by value. `ast` reads none of them.
  - (a) This unit takes the Python files alone, as written. The bash sites and the heredoc go to a
    unit of their own, with a static check that reads bash, because they are a separate language, a
    separate gate and the bar runner itself (M2).
  - (b) This unit takes them all: each bash site moves to a `mktemp` temp beside its destination, the
    heredoc to `tempfile.mkstemp`, and S5 gains a grep arm over the `.sh` files. It moves the bar
    runner, its version line and its canaries, and rewrites the `run-gates.test.sh:3237` staging.
  - (c) A record alone: a gotcha entry names the class, and no unit builds it now.
  Recommendation: (a). The bash class is real and reaches `$WORK`, so it deserves its own unit and
  its own gate rather than a rider on this one.
  RESOLVED (owner, 2026-10-15): (a). `TOOL-dRedressedBar-24` takes the bash writers and the heredoc
  writer under a bash-side static check, and §3's edge hands them off to it.

## 9. Revision log

- rev-1 · 2026-10-15 · initial draft, promoted from the round-1 closing diff review's H1 (report
  id 1) by the owner's ruling of 2026-10-15. Each citation was re-read at `bf42c5113`, whose
  `tools/` equals `e114f1356`'s. Parts (1) and (2) of the record's fix are taken. Part (1) takes its
  first option, never following `record`. Part (2) gains `st_nlink` and a final-path pin on the open
  handle. Part (3) replaces the fixed temp name with `tempfile.mkstemp`, on §4's probe that
  `O_EXCL` follows a dangling link here. The left-shift gate is the static arm. Drafting note,
  within rev-1 and before any commit: the owner ruled on 2026-10-15 to fold in the run's own capture,
  which the first draft had handed off, and the revision record
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-4-revision.md` widened S4 and S5 to the class. So
  S8 to S10 take the capture's open, read and delete, S4 extracts `write_replace` for
  `write_atomic` and `write_held_stamp`, S5 walks every `*.py` under the kit, S11 guards what it
  walks, the scratch helpers drop the job backend so `write_leg_capture` keeps the signature unit 22
  calls, F1 asks about the bash writers, and the H1 names the wider unit.
- rev-2 · 2026-10-15 · §3 · §8 · F1 resolved by the owner as (a), marked in place. `TOOL-dRedressedBar-24`
  takes the bash fixed-name temp writers and the heredoc writer, so §3's external hand-off becomes a
  hands-off edge to that unit, which its consumes-from mirrors, and the header gains
  `ratified 2026-10-15`. Written by unit 24's spec-writer pass. No scope item, design or criterion
  of this unit moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a file under a shared temp directory without
following a symlink or junction"` and `python tools/codebase-map/reuse_lookup.py "write a file
atomically through a temp file and rename"` ranked name-stem SEAMs only (`read`, `read_text`,
`write`, `write_text`), with no no-follow reader and no atomic writer. `python
tools/codebase-map/reuse_lookup.py "create a new file exclusively and refuse an existing entry or
link at its path"` ranked `CensusRefused`, `ScopeRefused` and other name-stem neighbours, and
`python tools/codebase-map/reuse_lookup.py "write a stamp file through an unpredictable temp file and
rename it into place"` ranked `write`, `write_text` and `stamp`, none of them an exclusive creator or
a temp writer. Each miss is recorded as a miss. A grep of `tools/` for `st_reparse_tag`,
`GetFinalPathNameByHandle`, `mkstemp`, `O_EXCL` and `st_nlink` found the seams extended here.
`check_app_alias` (`measure_legs.py:863-873`) already reads `st_reparse_tag` off an `os.lstat`, so
`read_plain_stat` takes the same read. The prototype table in `resolve_job_backend` (`:687-704`)
takes one more row. `write_atomic` (`:1022-1035`) is the writer S4 reroutes, and `held_halves.py`,
which `measure_legs.py` imports for `load_manifest` (`:90`), is where its shared core lands.
`write_recovered_logs`' existing `recovered/<scratch name>/` branch (`:1406-1407`) is the
destination S1 keeps. S35's failed-launch row in `run_admission` (`:1616-1620`) is the shape S8's
refusal takes. The fixture pattern `memio.py` already uses `tempfile.mkstemp`
(`tools/run-gates/fixtures/measure-legs/memio.py:14`). govkit's lock
(`tools/govkit/govkit.py:7373-7383`) is the repo's `O_EXCL` precedent, and its `write_atomic`
(`:4180`) is another kit's and is not touched. The symlink-or-junction fallback in AC2 follows
`tools/runlog/selftest.py:1682-1695`, which tries a symlink, falls back to a junction and says so
when it can make neither. S11 follows `809f794e4` and `cafbbc460`, which widened the same guard
with exact files and re-stamped the manifest.

The gotchas checklist for `tools/run-gates/measure_legs.py`, `tools/run-gates/held_halves.py`,
`tools/gate-legs.json` and `help/measure-legs.md` selected these classes, each answered here:
- `guard-above-a-fold-makes-its-fallback-dead`: the `lstat` checks settle every static plant before
  the final-path pin and the delete-time compare, so AC3, AC4, AC9 and AC11 stage the post-check
  state to reach each one.
- `fixture-passes-by-finding-nothing`: AC2 recovers a plain dead capture in the same run as its
  refusals, AC6 asserts its population is non-empty and holds `write_replace`'s call, and AC9 builds
  a plain capture beside its refusals.
- `staged-break-substitutes-a-synthetic-value`: every dead owner is a real exited process, and every
  link, junction and hard link is real on NTFS. The rebound `os.lstat` of AC3 and AC9 is the one
  substitution, and it stands for a swap made after a check, which no static plant can produce.
- `two-answers-to-one-question`: the destination and the capture refusal are stated in the help
  page and the module docstring, and AC7 reads both.
- `held-suite-guard-misses-a-sibling-kit`: the static arm reads files its leg did not guard, so S11
  adds the exact files, as that record's fix says.
- `a-new-leg-trips-a-growing-set-of-meta-gates`: a guard edit trips the canaries and the manifest
  ratchet, which §7 names and S11 re-stamps.

The recall probe returned the round-1 record's H1, `TOOL-aTetheredScratch-1` and
`TOOL-aTetheredScratch-2` on this repo's temp dir sitting under `$HOME`, and aRoutedQuill's closing
review M5, where a path reached through a junction was graded by its real path. M5 is the precedent
for S2 comparing the handle's final path rather than the path as spelled. The second probe returned
this unit's revision record and `TOOL-aProbedUnit-5` on the scratch guard's temp rules. The record
and the code agree on every citation re-read.

Recall terms used: `python tools/memory-recall/query.py "how does a tool sweeping a shared temp
directory avoid trusting a path or link another process planted there" --terms "owner.json scratch
sweep symlink junction reparse O_EXCL write_atomic temp TMPDIR planted untrusted"`, and `python
tools/memory-recall/query.py "how does a tool open, read and delete its own capture file without
following a link planted in its scratch dir, and write a temp file at an unpredictable name" --terms
"capture raw scratch hard link symlink junction O_EXCL mkstemp tmp os.replace guard held_halves"`
