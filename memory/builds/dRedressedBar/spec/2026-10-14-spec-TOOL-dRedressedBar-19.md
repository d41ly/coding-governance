# TOOL-dRedressedBar-19 — the units-16-18 spec audit's 19 mediums and 22 lows, batched: the profiler's census, path, launch, turnstile, redaction and leg-declaration gaps closed, the receipt sidecar made atomic, and specs 12 and 14 to 18 corrected

**Status:** SPECCED · rev-6 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md) | research | TOOL-dRedressedBar-10 TOOL-dRedressedBar-13 TOOL-dRedressedBar-17 |
| [2026-10-14-prompt-TOOL-dRedressedBar-19-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-19-2-revision.md) | research | TOOL-dRedressedBar-10 |
| [2026-10-14-prompt-TOOL-dRedressedBar-19-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-19-3-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-18-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-18-4-revision.md) | research | TOOL-dRedressedBar-18 |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md) | research | TOOL-dRedressedBar-12 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-5-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-5-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-6-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-6-revision.md) | research | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-7-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-7-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 16 to 18
(`reviews/2026-10-14-review-TOOL-dRedressedBar-16-18-spec-audit-round1.md`) exited CONVERGED with
41 confirmed findings: no blocker, no high, 19 mediums and 22 lows. BUILD-METHOD M4 batches every
medium and low into ONE unit, and this is that unit. Its minors land on units 16, 17 and 18, so it
repairs no unit in particular. Its order, 14, is one above unit 18's 13, and the README's derived
build-order region says what follows it. Under the owner's ruling of 2026-10-14 in the README's
Build-level rules, this unit is built from its spec as written, with no further audit round.

It closes these findings, by report id, each with the report item it shares:

| id | grade | item | sits in | what is wrong | closed by |
|---|---|---|---|---|---|
| 1 | MEDIUM | M1 | unit 18 §4 Files touched, §7, S13 | edits two kickoff-watched files and never re-stamps the manifest | S1 |
| 26 | MEDIUM | M1 | unit 18 §4 Files touched, §7 | as id 1, from the blast-radius lens | S26 |
| 10 | MEDIUM | M2 | unit 18 S4, §4 census fields, AC3 | widens census rows and the CIM line and names none of the old shape's readers | S10 |
| 33 | MEDIUM | M2 | unit 18 §4 census fields, AC3 | as id 10, from the failure-envelope lens | S33 |
| 11 | MEDIUM | M3 | unit 18 §4 environment and turnstile | an MSYS path reaches native Python unconverted, so the turnstile reads zero | S11 |
| 12 | MEDIUM | M4 | unit 18 §4 selftest, AC15 | the holder runs the regen preflight and its beacon wait has no bound | S12 |
| 19 | MEDIUM | M5 | unit 18 S1, §4 Inventory, §10 | a third leg-manifest reader beside two existing ones | S19 |
| 20 | MEDIUM | M6 | unit 18 S11, §4 Inventory, AC8, AC11 | the Python redactor has no parity arm against the runner's `redact` | S20 |
| 21 | MEDIUM | M7 | unit 18 §4 selftest guard, AC9, AC15 | the leg's guard omits two files its arms read | S21 |
| 25 | MEDIUM | M8 | unit 18 S13, §4, §7 | the new budget row joins foreign-prefix parity with no `WHOLE_RUN` entry | S25 |
| 27 | MEDIUM | M9 | unit 18 §7 | its own new leg is off its leg line, which reds spec tokens once the row lands | S27 |
| 29 | MEDIUM | M10 | unit 18 §4 selftest, §3 Edges | the leg ships to adopters with an undeclared kit and platform dependency | S29 |
| 34 | MEDIUM | M11 | unit 18 §4 launching and sampling, AC8, AC15 | several bash runs bypass `resolve_bash`, and an empty resolve has no refusal | S34 |
| 35 | MEDIUM | M12 | unit 18 §4 launching step 3, §5 | a failed job assign or resume leaves a suspended root that hangs the profile | S35 |
| 36 | MEDIUM | M13 | unit 18 §4 turnstile | normal beacon and ticket churn reads as a refused read | S36 |
| 38 | MEDIUM | M14 | unit 18 S11, §4 record, §5 | raw unredacted captures survive a crash or a kill with no record | S38 |
| 39 | MEDIUM | M15 | unit 18 S11, §4 record | the log redaction states no byte-level contract | S39 |
| 40 | MEDIUM | M16 | unit 17 S23, §4, §5, AC23 | the receipt write is atomic and its `install.sums` sidecar is not | S40 |
| 41 | MEDIUM | M17 | unit 17 AC1 | the `[dRB-14]` span is bounded by its label's first and last line | S41 |
| 2 | LOW | L1 | unit 17 S10, §4 row 15 | the `cross-entry argv:` note keeps a `slash-bearing` label it no longer means | S2 |
| 4 | LOW | L2 | unit 17 §1, §4 "Order, and unit 7" | calls order 12 above every unit of the build | S4 |
| 5 | LOW | L3 | unit 17 AC9 | the cut check requires four of six append sites | S5 |
| 6 | LOW | L4 | unit 18 §3 first non-goal | says no leg changes while S13 adds one | S6 |
| 7 | LOW | L5 | unit 18 S13, AC13, AC14 | the kit README section and the map entry are observed by no criterion | S7 |
| 24 | LOW | L5 | unit 18 S13, AC13, AC14 | as id 7, from the reuse lens | S24 |
| 8 | LOW | L6 | unit 16 S2 against unit 12 AC4 | the rewritten docstring paragraph need not keep unit 12's id | S8 |
| 31 | LOW | L6 | unit 16 S2, S4 against unit 12 S2 | as id 8, and spec 12 S2's stale premise stands | S31 |
| 9 | LOW | L7 | unit 16 §4 "The arm" | cites `build_gov13` from inside `M13_DEPLOY` | S9 |
| 13 | LOW | L8 | unit 18 §7 | the leg line omits `kit epoch` and is not declared a floor | S13 |
| 14 | LOW | L9 | unit 18 AC14 | asks every process-monitor marker to match, and a suite's reads 0.15 | S14 |
| 15 | LOW | L10 | unit 18 S11 Readers | cites the runner's processed `.out` as its raw capture | S15 |
| 16 | LOW | L11 | unit 17 §4, AC10, §10 | "corrects" a correct `:104` citation to `:103` | S16 |
| 17 | LOW | L12 | unit 17 §4 | counts six receipt writes where S23 lists seven | S17 |
| 18 | LOW | L13 | unit 16 §4 step 4, AC1 | cites the update call, not the `except Refusal`, as the catch | S18 |
| 22 | LOW | L14 | unit 18 S13, §4 Files touched | omits the subject-pin row govkit selfcheck requires | S22 |
| 23 | LOW | L15 | unit 17 S23, AC23 | claims AC23 observes two comments it never reads | S23 |
| 30 | LOW | L16 | unit 16 §4 adopter table | omits `derive_parity_lines` | S30 |
| 32 | LOW | L17 | unit 18 AC1, §4 candidates row 1 | AC1 is called the MSYS-fork refutation and spawns no MSYS fork | S32 |
| 37 | LOW | L18 | unit 18 S1, §4 record | the manifest refusals miss most malformed inputs | S37 |
| 42 | LOW | L19 | unit 18 AC6 | the STALLED check matches the whole stdout | S42 |
| 43 | LOW | L20 | unit 16 §4, §3 | says every carried `emitted` row names a claimed kit, and orphans are carried too | S43 |

Ids 2, 32 and 37 were re-graded by the skeptic, and the skeptic's grade binds. Ids 19, 29 and 38
had their fixes judged UNSOUND, and S19, S29 and S38 take the skeptic's corrected fix. Ids 3 and 28
were refuted by the audit and are not findings. Units 12 to 18 build first, as written. Once they
are CLOSED, this unit's spec-writer pass corrects the false prose in specs 12, 14, 15, 16, 17 and 18
and writes their revision lines, because only that role writes spec files. Its build pass then
changes the code sites §4 lists so they hold what the corrected specs say, and observes the
corrected form of each faulted criterion over the tree they leave.

## 2. Scope (IN)

Item S<n> closes report id n. Ids 3 and 28 were refuted, so no S3 or S28 exists. S44 is the
record. Items that share a report item share its observation, and each still names its own id.

- **S1** — id 1, M1. The kickoff manifest `memory/guides/SESSION-KICKOFF.md` is re-stamped twice.
  `<p19>` stages `tools/gate-legs.json` (S21, S29), which the manifest's `watch:` line names
  (`memory/guides/SESSION-KICKOFF.md:6`). The staged ratchet leg (`.githooks/pre-commit:188-195`)
  runs check C5s (`skills/session-kickoff/manifest-check.sh:1582-1593`), which refuses a commit
  staging a watched file unless the staged manifest's audit stamp differs from HEAD's. So `<p19>`
  carries its own re-stamp, naming `<p19>~1`, the sha before it, with a `manifest-audit:` line in
  its body, as unit 18's pass commit `6783992aa` did. A second commit, `<p19m>`, then re-audits the
  manifest against the edits units 18 and 19 make to `tools/gate-legs.json` and
  `tools/run-gates/run-gates.sh`, and re-stamps naming `<p19>`, in the shape of commit `2e187ee8b`
  and unit 17's S18, with a `manifest-audit:` line in the commit body. Only `<p19>`'s manifest
  holds S21's guard paths, so AC1 holds at `<p19m>` alone. Spec 18's §7 leg line names
  `kickoff-manifest ratchet`, and its revision line states that unit 18 owed the re-stamp and names
  AC1. Observed by AC1.
- **S26** — id 26, M1. The blast-radius lens's reading of S1's defect. Closed by S1's re-stamp.
  Observed by AC1.
- **S10** — id 10, M2. Unit 18 built part of this (`tools/process-monitor/census.py` at
  `997fc294f`): the ROW CONTRACT docstring lists `peak_mem_b` and `mem_b` with type `int|None` and
  their unit (`:23-25`), a blank or non-integer memory field reads None and never rejects the row
  (`parse_cim_bytes`, `:93-96`), `build_windows_rows` unpacks the six-tuple `parse_cim` returns
  (`:158`), and the CIM fixtures of `build_cim_fixture` and of
  `test_non_utf8_backend_output_survives` are seven-field lines, one of them with both memory fields
  blank. The build pass does the rest. `census.py` declares
  `OPTIONAL_FIELDS = ("peak_mem_b", "mem_b")`. `parse_cim` reads a line by its field count. A line
  of seven or more fields takes `peak_mem_b` and `mem_b` from fields five and six and its command
  from `parts[6:]` joined by the separator, where the build reads `parts[6]` alone (`:129`). A line
  of four to six fields is the legacy shape: its command is `parts[4]` when present and both memory
  keys read None, where the build reads `parts[4]` as the peak and loses the command. `FIELDS` and
  `render_rows` keep their bytes. In `tools/process-monitor/selftest.py`,
  `test_row_contract_is_complete` (`:104`) compares each row's keys against `FIELDS` plus
  `OPTIONAL_FIELDS`, where the build spells the pair inline and requires the exact set, and still
  requires every key of `FIELDS`. The separator table (`:930`) moves to seven-field lines.
  `test_cim_memory_fields_are_bytes` (`:215`), the arm unit 18 built for its AC3, gains a
  blank-memory line that stays a row and one five-field legacy line whose command reads intact, so
  no second memory arm is minted. Observed by AC10.
- **S33** — id 33, M2. The failure-envelope lens's reading of S10's defect. Closed by S10's change.
  Observed by AC10.
- **S11** — id 11, M3. Spec 18 rev-4's S15 converts the scratch dir, the turnstile key and each
  probed launcher with `cygpath -m` in the resolved bash and records both spellings, because its
  own legs could not run without it. Its scratch dir refuses the run when the converted spelling
  is no directory. What stays here is the turnstile key's failure rule. The built
  `TURNSTILE_SCRIPT` (`tools/run-gates/measure_legs.py:326-330` at `997fc294f`) falls back to the
  bash spelling when `cygpath` fails, and Python then reads the key as absent and empty, so every
  leg would record no holder and no wait. In this unit a key whose
  conversion exits non-zero, or prints a line that does not open with a drive letter, makes
  `resolve_turnstile_dir` return its unresolved pair `("", "")`. Every tick is then a refused read,
  and never an empty one. Observed by AC11.
- **S12** — id 12, M4. `build_holder_env` returns the legs' scrubbed environment with
  `GATE_REGEN_CHECK=0` set after the scrub, as `queued.sh` sets it, and the selftest's holder runs
  under it. At `997fc294f` the holder runs in the scrubbed environment alone
  (`tools/run-gates/measure_legs.py:1993-1999`), so it runs the regen preflight. The wait for the
  holder's slot beacon is already bounded, inline at `:2000-2007`: 120 s, returning early when the
  holder exits. The build pass moves that loop into `read_hold_beacon`, with the bound declared as
  `HOLD_BEACON_WAIT_S = 120`, the bound `selftest-budgets.txt` prices the arm at. On a timeout or
  an early exit the arm fails and prints the holder's captured output, which the inline failure
  line omits. Observed by AC12.
- **S19** — id 19, M5, by the skeptic's corrected fix. `tools/run-gates/held_halves.py`'s
  `load_manifest` gains a keyword `refuse`, defaulting to its own `print_refusal`, and its row check
  names the first offending row index. The profiler's manifest reader is `read_profile_legs`, which
  calls `held_halves.load_manifest` once with its own refusal function and then adds S37's checks.
  That function raises `ProfileRefused`, which `run_profile` already prints as one stderr line
  opening `measure-legs: REFUSED — ` and turns into exit 2 (`measure_legs.py:1387-1389` at
  `997fc294f`), so every refusal reads that way. The guard S21 sets
  includes `held_halves.py`. Spec 18's §10 names `held_halves.load_manifest` and
  `derive-ceilings.read_legs` as the two existing readers. Observed by AC19.
  - **Readers:** S19 renames the profiler's `read_legs` to `read_profile_legs`, so it no longer
    shares a name with `derive-ceilings.py`'s `read_legs`, which keeps its name.
    by name: `tools/run-gates/measure_legs.py`, which defines the function at its lines 438 to 459
    at the tip of this pass and calls it once, in `run_profile` at line 1354. A grep for its call
    over the tools tree finds no other caller; the three calls in
    `tools/run-gates/derive-ceilings.py` are to that file's own reader. The rename touches the
    definition and the caller in one file.
    by value: `run_profile` is the only reader of the list the function returns, and it reads the
    same list after the rename.
- **S20** — id 20, M6. The port `derive_redacted` stays, and a parity arm holds it to the runner.
  The arm takes `redact` from `run-gates.sh` through `extract_runner_function`, which already
  returns a one-line definition such as `redact`'s (`measure_legs.py:224-244` at `997fc294f`;
  `redact` sits at `run-gates.sh:304` there), and runs it in the
  resolved bash over one LF-only input of eight shapes. `derive_redacted` runs over the same bytes,
  and the two outputs must be byte-equal. Spec 18's §10 lists `redact` among the runner functions
  run from source. Observed by AC20.
- **S21** — id 21, M7. The `measure-legs selftest` leg's guard in `tools/gate-legs.json` gains
  `{prefix}/run-gates/derive-ceilings.py`, `{prefix}/run-gates/held_halves.py` and
  `.githooks/pre-push`, as exact files. Spec 18's sentence naming the files the leg reads or
  imports names all three. Observed by AC21.
- **S25** — id 25, M8. `WHOLE_RUN` in `tools/run-gates/foreign-prefix.gov.test.sh` gains the row
  `measure-legs selftest|a --selftest mode of a shipped engine, so a probe site would be adopter-facing`,
  as `held-halves selftest` carries. Observed by AC25.
- **S27** — id 27, M9. Spec 18's §7 leg line names `measure-legs selftest`, and the paragraph that
  said the leg stays off the line says it is named once the manifest row exists. Observed by AC27.
- **S29** — id 29, M10, by the skeptic's corrected fix. `tools/run-gates/kit.toml` withholds the
  profiler's fixtures in one `[[files]]` rule with `role = "project-owned"`, whose include names
  every file under `fixtures/measure-legs/` literally and kit-relatively. That is the form
  `tools/runlog/kit.toml:37-40` uses, with a comment saying why, as its `:31-35` does. The list
  holds 13 paths once S32 adds `forks.sh`, and it equals what
  `git ls-files tools/run-gates/fixtures/measure-legs` prints. A glob cannot withhold them, because
  a list include claims literal paths only. `rule_sources` (`tools/govkit/govkit.py:318-335`) drops
  every element carrying `*`, `?` or `[`, and only the exact element `**` reads as a wildcard
  (`resolve_rule_pool`, `:6603-6625`). So `scan_claimed_paths` (`:6628-6659`) claims nothing for a
  glob element under the fixture directory, and the `**` engine rule ships every fixture. Observed
  by AC29.
  - **The arm.** The list is typed beside the directory it describes, so a new arm in
    `tools/run-gates/measure_legs.py --selftest`, `test_fixtures_withheld`, reds when the two
    differ, as `test_kit_declarations` does for runlog (`tools/runlog/selftest.py:1010-1026`). It
    reads `kit.toml` beside the module with `tomllib`. It collects every element of a list include
    on a `project-owned` rule and compares those opening `fixtures/measure-legs/` with the files
    under `FIXTURES` (`measure_legs.py:81`), read off the filesystem, both ways. It requires that
    population to be non-empty, so the comparison can fail, and no `project-owned` element to carry
    `*`, `?` or `[`. The arm reads `kit.toml`, so the `measure-legs selftest` guard in
    `tools/gate-legs.json` gains `{prefix}/run-gates/kit.toml` as an exact file, beside S21's three.
  - **The leg.** The descriptor declares no `[[gate_leg]]` named `measure-legs selftest`.
    `tools/govkit/registry.toml` carries an `[[exempt_leg]]` row for that name. Its `why` states
    that the fixtures are withheld, that the tool needs a process-monitor sibling and a Windows
    host, and that the leg stays on gov's bar, held like every self-test.
  - **Readers:** S29 drops the descriptor's `[[gate_leg]]` row that unit 18 added, at
    `tools/run-gates/kit.toml:154-163` at `997fc294f`, its comment block included.
    by name: `tools/gate-legs.json`, `tools/run-gates/selftest-budgets.txt`,
    `tools/run-gates/windows-only-legs.txt`, `tools/run-gates/measure_legs.py` and
    `tools/run-gates/run-gates.sh`, which spell the leg's name at the tip of this pass, and
    `tools/govkit/subject-pins.tsv` once S22 writes its row. Each keeps its row, since the leg stays
    in the manifest; the descriptor row is the only one dropped.
    by value: `tools/govkit/govkit.py` reads a descriptor's `[[gate_leg]]` rows wherever it walks
    `gate_leg`, selfcheck and `write_gate_legs` among them, and with the row gone selfcheck grades
    the leg as an `[[exempt_leg]]`, as it grades `profile-bar selftest`: a manifest leg claimed by
    no descriptor and carried by no `[[exempt_leg]]` reds (`govkit.py:2926-2928` at `997fc294f`).
- **S34** — id 34, M11. The profiler resolves one bash at start, `resolve_bash` against
  `run-gates.sh`, and every bash it starts is that one: the leg wrapper, `mktemp`, `resolve_python`,
  `read_spawn_floor`, `measure_spawn_cost`, `cygpath`, the parity arms' `awk` and `redact` runs, and
  the selftest's runner calls. An empty result refuses with exit 2 and names every candidate tried.
  Unit 18 built both halves: at `997fc294f` every subprocess argv in `measure_legs.py` opens with a
  `bash` it took from `profile_bar.resolve_bash`, and `run_profile` refuses an empty result naming
  the candidates (`:1350-1352`). What remains is the gate: a new arm, `test_no_bare_bash_argv`,
  scans `measure_legs.py` with `ast` and finds no subprocess argv whose first element is the
  literal `'bash'`, which the S20 arm's `redact` run must also meet. Observed by AC34.
- **S35** — id 35, M12. When `OpenProcess`, the job assign, the thread snapshot or `ResumeThread`
  fails, the profiler terminates the still-suspended root through the process handle
  `CreateProcess` returned, with exit code 1. That is the only terminate the tool calls, on a
  process that has executed nothing. The leg records status `fail`, rc 1, and in its `<i>.json`
  a `launch_error` reading `launch: <call> <winerror>`, and the run continues. Spec 18's §5
  security line states the one carve-out. At `997fc294f` `run_leg` raises `OSError` on those
  failures (`measure_legs.py:752-753`, `:772-773`) with no terminate, and `run_admission` lets it
  escape the run. The branch sits in `run_leg`, so the interpreter probe, which launches through
  the same function (`measure_job_children`, `:841-864`), also terminates its root, and its failure
  stays the exit-2 refusal S14 of spec 18 gives it. A leg whose launch failed holds no job and no
  handle, and the run-end loop skips its job re-read and handle close. Observed by AC35.
- **S36** — id 36, M13. In `read_turnstile`, an entry that is gone between the listing and the read,
  or whose `pid` file is absent, empty or not a number, is not judged at that tick, as a pid the
  scan did not see is not judged. A ticket whose name yields no pid is treated the same way. Only a
  failure to list `gate-bar-queue/`, or to stat the key itself, is a refused read. Unit 18 built
  this rule (`measure_legs.py:540-569` at `997fc294f`): a missing `pid` file is skipped, a pid that
  is not a number is not held, a ticket name with no pid field is not listed, and only a listing
  error other than absence raises. What remains is the arm the §7 `New arm:` line declares, over
  AC36's key. Observed by AC36.
- **S38** — id 38, M14, by the skeptic's corrected fix. Right after `mktemp`, the profiler writes
  `owner.json` into its scratch dir: its own Windows pid, that process's creation time from
  `GetProcessTimes`, and its record dir. At start, `derive_abandoned_scratch` lists every
  `gate-profile.*` sibling of its own scratch dir. One is abandoned only when its `owner.json` reads
  and no live process carries that pid with that creation time. A scratch with no readable
  `owner.json`, or one whose owner cannot be opened for a reason other than absence, is left alone.
  For each abandoned scratch, `write_recovered_logs` redacts each `raw/<i>.out` with
  `derive_redacted` into `<record>/<i>.log.recovered`, or into
  `recovered/<scratch name>/<i>.log.recovered` under this run's own record when that record dir is
  gone. It then deletes the raw file. This run's envelope names each in `raw_recovered`. Spec 18's
  §5 security line states the endings the sweep covers. The "What it writes" section of
  `help/measure-legs.md`, a list with no record table at `997fc294f`, names `raw_recovered` and
  S35's `launch_error`, and says a later run sweeps a dead run's raw captures. The scratch dir is
  made by `build_scratch` (`measure_legs.py:309-323`), and `owner.json` is written right after it
  returns. Observed by AC38.
  - **Readers:** S38 deletes an abandoned run's raw captures, `raw/<i>.out`, once each is redacted.
    by name: READER NOT IN TREE, because the captures are runtime files under a scratch dir outside
    the tree, and the only code spelling their name is the profiler unit 18 builds, which writes
    them and redacts them.
    by value: the bytes are read by `derive_redacted` in `tools/run-gates/measure_legs.py` before
    the delete, and the recovered log is the only copy kept, as F2 of spec 18 resolved for a live
    leg.
- **S39** — id 39, M15. `derive_redacted` takes and returns bytes. It replaces every match of
  `rb'://[^/@\s]+:[^/@\s]+@'` with `b'://***:***@'`, the runner's ERE at `run-gates.sh:301` in
  bytes, and writes every other byte as it came, NULs and CRs included. The capture is read as bytes
  and never decoded. `log_bytes` is the raw capture's size. Unit 18 built this half at
  `997fc294f`: `REDACT_BYTES` spells `\s` as its six ASCII bytes (`measure_legs.py:486`),
  `derive_redacted` returns bytes for bytes (`:490-494`), and `write_leg_capture` reads the
  capture as bytes, sets `log_bytes` to its length and writes the redacted bytes
  (`:1279-1296`). Its `str` branch masks census command lines (`:1183`, `:1268`) and stays. What
  remains: `printenv.py` also prints byte `0xe7` and, after a CRLF, a second planted credential,
  written to its binary stdout. Observed by AC39.
- **S40** — id 40, M16. At each of the five sidecar sites in `tools/govkit/govkit.py`, the
  `install.sums` text is written through `write_atomic` first and the receipt last.
  `ADOPTER_BAR_PATHS` gains the spelling `'"install.sums"'` beside the `receipt_path` unit 17 adds,
  so the routing arm refuses a direct write to either. Spec 17's S23 and §5 state the order and
  that an interrupt between the two writes leaves a new sidecar beside the old receipt, which
  `check` reports until the next apply rewrites both. Spec 14's "When CONFIGURE fails" table gains
  that row. Observed by AC40.
- **S41** — id 41, M17. Unit 17's AC1 is observed by label: a python program reads every `check(`
  call in `tools/govkit/selftest.py` whose first argument is a string opening `[dRB-14]`, or opening
  `[dRB-15]`, wherever it sits. Unit 17's S2 sidecar check carries a label opening `[dRB-14]`
  (`tools/govkit/selftest.py:3641` at `997fc294f`), so the build pass writes nothing for S41. Spec
  17's AC1 says it reads by label. Observed by AC41.
- **S2** — id 2, L1. The `cross-entry argv:` selfcheck note in `tools/govkit/govkit.py` reads
  `<o> argv element(s) offered by [adopt], [check], [[gate_leg]] and [[regenerate]] ...` with no
  `slash-bearing`. Spec 17's S10 restates the note in that form, and its §4 row 15 names spec 15's
  OFFERED and GRADED sentences and the note template. Spec 15's §4 "The ownership join" states the
  offered population S10 of unit 17 set and the new template. Observed by AC2.
- **S4** — id 4, L2. Spec 17's §1 and its §4 "Order, and unit 7" say unit 17 is ordered after units
  9 to 16, whose specs and tree it corrects, and point at the README's derived build-order region
  for what follows. Observed by AC4.
- **S5** — id 5, L3. Spec 17's AC9 requires the cut to carry `:7424`, `:7502`, `:7540`, `:7593`,
  `:7616` and `:7621`, and its awk half reads "prints exactly 7424 7502 7540 7593 7616 7621 at
  46eb75ed". Observed by AC5.
- **S6** — id 6, L4. Spec 18's first non-goal reads: no change to any existing leg's argv, guard or
  ceiling, and no runner behaviour beyond the version line; the one new leg is S13's. Observed by
  AC6.
- **S7** — id 7, L5. `tools/run-gates/README.md` carries a section, under its own `## ` heading,
  naming `measure_legs.py` and `--concurrent`. `memory/map/features/run-gates.md` lists
  `tools/run-gates/measure_legs.py` among its files and `measure-legs selftest` among its gate legs.
  Unit 19 writes whichever of the three unit 18 left out. At `997fc294f` unit 18 left none out: the
  README's section headed "The gate profiler" names both (`:722-732`), and the map
  feature lists the file and the leg (`memory/map/features/run-gates.md:17`, `:65`). So the build
  pass writes nothing for S7 and AC7 observes the tree. Spec 18's S13 names AC7 as the
  observation. Observed by AC7.
- **S24** — id 24, L5. The reuse lens's reading of S7's defect. Closed by S7. Observed by AC7.
- **S8** — id 8, L6. The `carry_out_of_scope` paragraph of `write_gate_legs`' docstring carries
  `TOOL-dRedressedBar-12` beside `TOOL-dRedressedBar-16`. Spec 16's S2 and AC3 require both tokens.
  Unit 16 kept both when it rewrote the paragraph (`tools/govkit/govkit.py:4248-4253` at
  `997fc294f`), so the build pass writes nothing for S8 and AC8 observes the tree.
  Observed by AC8.
- **S31** — id 31, L6. Spec 12's S2 carries an inline note that its rationale, the same-argv
  re-claim, is superseded by `TOOL-dRedressedBar-16`. Spec 16's S4 names that note. Observed by
  AC31.
- **S9** — id 9, L7. Spec 16's §4 "The arm" cites `tools/govkit/selftest.py:15428-15459` for
  `build_gov13`. Observed by AC9.
- **S13** — id 13, L8. Spec 18's §7 leg line names `kit epoch (shipped bytes move, the version moves)`,
  and a sentence below it says the line is a floor, derived by joining §4 Files touched against the
  guards in `tools/gate-legs.json` with `BROAD_LEG_FLOOR` applied, plus the unguarded legs the
  change moves. Observed by AC13.
- **S14** — id 14, L9. The process-monitor marker check is scoped to the files the kit ships:
  `git grep` over `tools/process-monitor` with `':!*.test.sh'`. Spec 18's revision line states that
  its AC14 read `adopt-process-monitor.test.sh`'s `@0.15` and names AC14. At `997fc294f` the scoped
  grep prints one version, `0.19`, so the build pass writes nothing for S14. Observed by AC14.
- **S15** — id 15, L10. Spec 18's S11 Readers cite `$WORK/$i$sfx.raw` (`run-gates.sh:3877`) as the
  runner's raw capture. Observed by AC15.
- **S16** — id 16, L11. Spec 17 cites `tools/codebase-map/kit.toml:104` in §4, AC10 and §10, and its
  §10 says the report's citation was right. Observed by AC16.
- **S17** — id 17, L12. Spec 17's §4 says "every receipt write" with no number. Observed by AC17.
- **S18** — id 18, L13. Spec 16 cites the update call at `:11888-11890` and the `except Refusal` at
  `:11898-11903` separately, in §4 step 4 and in AC1's fixture line. Observed by AC18.
- **S22** — id 22, L14. `tools/govkit/subject-pins.tsv` carries the row
  `measure-legs selftest<TAB>kit<TAB>selftests`, regenerated by
  `python tools/govkit/govkit.py selfcheck --write` when unit 18 left it out. Spec 18's revision line
  names the file. Observed by AC22.
- **S23** — id 23, L15. `write_atomic`'s docstring and the comment block between the ADOPTER-BAR
  banner and `ADOPTER_BAR_PATHS =` each name the receipt and `install.sums`. Spec 17's AC23 says
  so. Observed by AC23.
- **S30** — id 30, L16. Spec 16's "What an adopter sees change" table gains a row: after a narrower
  apply, a failing contract clause whose installed consumer sits on a carried kit's leg reds `check`
  and `update` again, as after a full apply, through `derive_parity_lines`. Observed by AC30.
- **S32** — id 32, L17. A fixture `forks.sh <n>` runs n `( /usr/bin/true )` subshells and n
  `$(true)` substitutions, and `serial.json` runs it with n = 5 beside its zero-count twin, as two
  rows whose first word is `bash`, as `stall.json` runs `stall.sh`. `serial.json` holds four legs
  at `997fc294f`, and `test_serial_run` reads that count (`measure_legs.py:1839`, `:1871-1876`),
  so its record count and its AC10 listing move to six. A new
  arm, `test_fork_count`, requires a `procs_total` difference of at least 10. Spec 18's §4
  candidates row 1 says AC1 covers the native-spawn path and this unit's AC32 the fork path.
  Observed by AC32.
- **S37** — id 37, L18. `read_profile_legs` adds, after `load_manifest`'s checks: an empty list, a
  duplicate name, an argv that is not a non-empty list of strings, a name holding a tab, CR or LF,
  and an argv token still carrying `{` after `resolve_prefix_token`. Each refuses with exit 2 and
  names the row index. Unit 18's `read_legs` already refuses unparseable JSON, a non-list, an empty
  list, a non-object row, a bad argv and a duplicate name (`measure_legs.py:438-459` at
  `997fc294f`), naming the row for a missing name only. The new refusals are the tab, CR or LF in a
  name and the unresolved token, and every row refusal names its index. A new arm,
  `test_manifest_refusals`, feeds one temp manifest per class. Observed by AC37.
- **S42** — id 42, L19. Unit 18's AC6 is observed line by line: exactly one stdout line opens
  `measure-legs: STALLED  ` and names `stall.sh`'s leg, and none names `steady.py`'s or
  `churn.py`'s. The line names a leg by its manifest name (`measure_legs.py:1271`), and
  `stall.json` names those three legs `stall`, `steady` and `churn`. The selftest's stall arm reads
  the same way: at `997fc294f` it requires a line opening `measure-legs: STALLED  stall  `
  (`:1972-1974`) and reads neither how many there are nor whether one names a sibling. Spec 18's
  revision line names AC42. Observed by AC42.
- **S43** — id 43, L20. Spec 16's §4 "Why the carry is consistent after unit 12" states what it
  proves: a carried row whose kit the receipt claims names a claimed kit. Its §3 gains the orphan
  case as an accepted gap: a row whose kit the receipt no longer claims is carried too, because the
  carry is keyed on the selection, which that non-goal keeps. Observed by AC43.
- **S44** — The record, in two passes. Specs 12, 14, 15, 16, 17 and 18 each take ONE rev bump in
  this unit's spec-writer pass, `<w19>`, which runs once units 12 to 18 are CLOSED and before the
  build pass. Each revision line names `TOOL-dRedressedBar-19` and every report id §4's table
  assigns that spec. The build pass and `<p19m>` write no spec file but this one's status and date
  cells. Every reading below goes to this unit's acceptance ledger under `memory/builds/dRedressedBar/build/`, carrying
  `**Serves:** journal TOOL-dRedressedBar-19`. Observed by AC44.

## 3. Non-goals (OUT)

- Rewriting a faulted criterion of specs 16 to 18. Each was built against its §6 as written. Its
  revision line states which half did not hold and names the criterion here that observes the
  corrected form. Prose stating a false fact is corrected in place, as units 10, 13 and 17 did, and
  a design paragraph this unit changes points here rather than restating the change.
- The report's left-shift proposals that are their own mechanism: the spec-tokens checks, the
  selftest-lint and guard-coverage rules, the repo-wide `ast` lint, the govkit selfcheck rule on
  `requires`, the `.governance/` write lint and the new checklist entries. S34's arm and S40's
  routing member are the gates the report names for their findings, so they are in scope.
- No change to the merge bar's runner, to any existing leg's argv, or to `read_runs` and
  `derive-ceilings.py`. S21 and S29 widen one guard, S29 moves one leg's declaration, and S25 adds
  one row.
- No staged stale output in the turnstile arm. The report's case for S12 writes into the tree the
  selftest runs over, which a leg run on every bar must not do (§4 "Alternatives rejected").
- No kit version moved by this unit. Unit 18 moved both kits' versions on this branch, and the
  lander's mint dates a later move of shipped bytes (`tools/govkit/govkit.py:13034-13063`, "WHERE
  THE BUMP IS MADE").
- No change to `write_gate_legs`' carry keying (S43), to `check`'s sidecar compare, or to
  `derive_parity_lines` (S30).
- No new `help/` page. `help/measure-legs.md` is unit 18's, and no flag or record a user reads
  moves except `raw_recovered` and `launch_error`, which S38 adds to that page's "What it writes"
  section.

### Edges

- **consumes-from** `TOOL-dRedressedBar-12` — the `carry_out_of_scope` paragraph of
  `write_gate_legs`' docstring that its S2 writes with its id, which S8 keeps beside unit 16's, and
  its spec's S2, which S31 annotates. Without that paragraph there is no unit-12 token to keep.
- **consumes-from** `TOOL-dRedressedBar-14` — the RECEIPT write and its sidecar write, which S40
  reorders through `write_atomic`, and its spec's "When CONFIGURE fails" table, which S40 extends.
- **consumes-from** `TOOL-dRedressedBar-15` — the `cross-entry argv:` note its S5 mints, whose label
  S2 corrects, and its spec's ownership-join paragraph and note template.
- **consumes-from** `TOOL-dRedressedBar-16` — the rewritten docstring paragraph S8 extends, and its
  spec's S2, S4, §3, §4 and AC3, which S8, S9, S18, S30, S31 and S43 correct. AC8's red half reads
  its pass commit.
- **consumes-from** `TOOL-dRedressedBar-17` — `scan_entry_argv` and the note counts its S10 sets,
  the `receipt_path` member and receipt routing of its S23, its `[dRB-14]` and `[dRB-15]` checks,
  and its manifest re-stamp. Its spec is what S2, S4, S5, S16, S17, S23, S40 and S41 correct.
- **consumes-from** `TOOL-dRedressedBar-18` — the profiler, its fixtures, its leg's rows and the
  census fields, which every profiler item here changes. Its spec is what S1, S6, S7, S11 to S15,
  S19 to S22, S25, S27, S29, S32 and S34 to S42 correct. Most red halves read its pass commit
  `<p18>`.

## 4. Design

### Evidence, read at `17908e7d` on 2026-10-14

`17908e7d`'s `tools/`, `skills/`, `help/` and `.githooks/` equal `ebce889c`'s
(`git diff --stat ebce889c7 HEAD -- tools skills help .githooks` prints nothing). Specs 16 to 18
were read at the blobs the report pins. Units 12 to 18 are unbuilt there, so every reading of a
code site they add is derived from their specs.

- `parse_cim` rejects a line of fewer than four fields and takes the command from `parts[4]` when
  present (`tools/process-monitor/census.py:83-120`). `build_windows_rows` unpacks a four-tuple
  (`:136`). `FIELDS` holds nine keys (`:264`), which `render_rows` writes (`:268-280`), and the ROW
  CONTRACT docstring lists the same nine (`:12-22`). `test_row_contract_is_complete` asserts
  `sorted(r) == sorted(census.FIELDS)` (`tools/process-monitor/selftest.py:102-110`). Five-field
  CIM lines sit at `:69-72`, `:206-209` and `:911-915`. No other file reads `FIELDS`.
- The turnstile key is `${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}` resolved by `cd ... && pwd`
  (`tools/run-gates/run-gates.sh:1513-1514`), an MSYS spelling. `cygpath -m /c/Users` printed
  `C:/Users` on node d. A beacon's `pid` is written after its directory exists (`:1950-1951`), and
  the runner itself treats a beacon with no pid as one being written (`:1554-1558`).
- The regen preflight's only skip is `GATE_REGEN_CHECK=0` (`run-gates.sh:1433`).
- `held_halves.load_manifest` refuses unreadable JSON, a non-list and a row with no name through
  `print_refusal`, which prints `held-halves: REFUSED — ` and raises `SystemExit(2)`
  (`tools/run-gates/held_halves.py:69-88`). Its callers are `:336`, `:418` and `:528`, and no file
  reads its message text. `derive-ceilings.py` has its own `read_legs` (`:139-142`), which honours
  `GATE_LEGS`.
- `redact` is one `sed -E` (`run-gates.sh:301`). Under MSYS its pipe drops the CR of a CRLF
  (`:305-307`), and the runner's capture drops NULs (`:3878-3880`). The raw capture is
  `$WORK/$i$sfx.raw` (`:3877`), and `$WORK/$i$sfx.out` is the processed copy (`:3916`).
- `resolve_bash` returns `("", tried)` when no candidate can stat the script
  (`tools/run-gates/profile_bar.py:282-304`).
- `foreign-prefix.gov.test.sh` reds both directions on `WHOLE_RUN` (`:48-50`), and the array
  carries `held-halves selftest` with the shipped-engine reason (`:124-139`).
- `tools/run-gates/kit.toml` declares `requires = []` (`:15`), one engine rule over `**` (`:17-19`),
  and an LF pin on `{kit}/*.sh` (`:194-196`). `tools/govkit/registry.toml` holds `[[exempt_leg]]`
  `profile-bar selftest` (`:610-612`), and `{prefix}/govkit` is exempt from every entry
  (`:295-297`), so a registry edit moves no kit version.
- govkit selfcheck fails a manifest leg with no `subject-pins.tsv` row (`tools/govkit/govkit.py:2904-2960`),
  and `held-halves selftest` and `profile-bar selftest` carry `kit` and `selftests` there.
- `tools/check-spec-tokens.py` adds a `guards` hit for every guarded leg a Files-touched path trips
  that §7 does not name (`:1198-1207`, `check_guard_trips` at `:494`), and a `leg` hit for a §7 name
  the manifest lacks (`:1133-1134`). `BROAD_LEG_FLOOR` is 5 (`:262`), and today
  `{prefix}/run-gates/` is carried by 6 legs, so it is broad.
- Every receipt write is followed by a plain `install.sums` write: `:8019` and `:8027`, `:12017`
  and `:12018`, `:12055` and `:12056`, `:12062` and `:12063`, `:12692` and `:12694`. `check`
  compares the two both ways (`:5318-5333`). `write_atomic` writes UTF-8 with `newline="\n"`, as
  every sidecar write does (`:3967-4000`). The routing arm matches a declared member as a
  substring of a write's destination segment (`tools/govkit/selftest.py:15848-15917`).
- `derive_parity_lines` is at `tools/govkit/govkit.py:6075`, its `r.fail` at `:6119-6121`, and its
  callers at `:5416` and `:9658`. The carry keys on the selection alone (`:4303-4305`).
- `build_gov13` starts at `tools/govkit/selftest.py:15428`, and `M13_DEPLOY` ends at `:15412`. In
  `update`, the `write_gate_legs` call is `:11888-11890` and the `except Refusal` with its `r.fail`
  is `:11898-11903`. `tools/codebase-map/kit.toml:104` is the argv line.
- `git show 46eb75ed:tools/govkit/govkit.py | awk 'NR>=7233 && NR<=8031 && /rows\.append/ {print NR}'`
  prints 7424 7502 7540 7593 7616 7621.
- The only `gov:kit process-monitor@` marker not at 0.18 is
  `tools/process-monitor/adopt-process-monitor.test.sh:4`, at 0.15.

### Evidence, read at `997fc294f` on 2026-10-15

Units 12 to 18 are CLOSED here, and unit 18 built against spec 18 rev-4 in `6783992aa` and
`997fc294f`. This unit's spec was audited against spec 18 rev-3, so each item that reads the
profiler, its fixtures, its declarations or the census was re-read over the built tree, and §2
states, per item, what unit 18 already built and what the build pass still does. The base
readings above stand as evidence of the defects. At the tip:

- Already built, so the build pass writes nothing for them: S7's README section and map claim,
  S8's two docstring ids, S14's single shipped marker version, and S41's `[dRB-14]` sidecar label.
- Built in part: S10's docstring, blank-memory rule, six-tuple unpack and seven-field fixtures;
  S12's bounded beacon wait, 120 s inline; S34's one bash and its empty-result refusal; S36's
  per-entry turnstile rule; S37's refusals other than the tab-bearing name and the unresolved
  token; S39's bytes redaction. §2 names what each still owes.
- Still owed whole: S11's no-fallback key rule (`TURNSTILE_SCRIPT` keeps `|| printf` at
  `measure_legs.py:329`), S19's wrapped reader, S20's parity arm (`RUNNER_FUNCTIONS` at `:144`
  holds no `redact`), S21's three guard paths (the guard at `tools/gate-legs.json:1261-1269`
  holds none), S22's subject pin (`tools/govkit/subject-pins.tsv` holds no `measure-legs` row,
  and selfcheck's pin compare sits at `tools/govkit/govkit.py:2946-3000`), S25's `WHOLE_RUN` row
  (`tools/run-gates/foreign-prefix.gov.test.sh` names the leg nowhere), S29's declarations
  (`tools/run-gates/kit.toml:159-163` holds the `[[gate_leg]]` row, and `registry.toml` holds no
  such `[[exempt_leg]]`), S32's fork fixture, S35's launch-failure branch, S38's sweep, S2's note
  label (`govkit.py:3348`), S23's two comments, which name the receipt and not `install.sums`
  (`:4154-4171`, `:4174-4195`), and S40's five sidecar writes, each a plain `write_text` after its
  receipt write (`:8339`, `:12341`, `:12379`, `:12386`, `:13016`).
- The kickoff manifest's `last-audit:` names `4a4960958`, whose `tools/gate-legs.json` holds no
  `measure-legs selftest` row, so S1's `<p19m>` still re-stamps. Unit 18's `6783992aa` moved that
  line from `6057a55c` to `4a4960958`, its parent, and its body carries `manifest-audit:`.

### Evidence, read at `3275f305a` on 2026-10-15

Unit 19's builder returned a divergence before writing any file: rev-5's S29 named a
`fixtures/measure-legs/**` include, which govkit cannot honour. Re-read here:

- `tools/run-gates/kit.toml` holds one `**` engine rule (`:17-19`) and six `project-owned` rules,
  each a literal list (`:39-97`); no `project-owned` element carries a glob.
- A python probe loaded the descriptor through `govkit.resolve_descriptor_paths(<desc>, "tools")`,
  took `govkit.canonical_ctx("run-gates")`, and called `govkit.resolve_rule_pool` over the `**`
  rule. As built, 12 of the 12 tracked fixtures sit in the engine pool. With a `project-owned`
  rule `include = ["fixtures/measure-legs/**"]` appended, 12 of 12 still do. With a rule naming
  the 12 literally, none does.
- `tools/runlog/kit.toml:31-35` records the same trap ("`fixtures/**` here claimed nothing"), and
  its self-test compares its literal list with the directory both ways
  (`tools/runlog/selftest.py:1010-1026`).
- No run-gates suite compares a `[[files]]` list with a directory. The `measure-legs selftest`
  guard already holds `{prefix}/run-gates/fixtures/measure-legs/` (`tools/gate-legs.json:1265`), so
  a new fixture runs that leg on a scoped bar, which makes its suite the arm's home. No guard in
  `tools/gate-legs.json` names `{prefix}/run-gates/kit.toml` exactly, and no other live spec lists
  that file under Files touched.

### The profiler, item by item

Each row is a change to `tools/run-gates/measure_legs.py` as unit 18 builds it, unless the row
names another file.

| Id | Change |
|---|---|
| 11 | `TURNSTILE_SCRIPT` keeps no fallback after `cygpath -m`, and `resolve_turnstile_dir` returns `("", "")` unless the converted line matches `^[A-Za-z]:/`. The conversion itself is spec 18's S15 |
| 12 | `build_holder_env(env)` scrubs as the legs are scrubbed, then sets `GATE_REGEN_CHECK=0`. `read_hold_beacon(key, holder, bound_s)` polls for any slot beacon's `pid` file and returns it, or None on a timeout or on the holder's exit; it replaces the inline loop at `:2000-2007` |
| 19, 37 | `read_profile_legs(path)` replaces the profiler's `read_legs`. `held_halves.load_manifest(path, refuse=...)`, with a `refuse` that raises `ProfileRefused` |
| 20 | a parity arm over eight LF-only shapes: plain `https://u:p@h`, two on one line, `git+ssh://`, a password holding `:`, no colon, a `/` in the userinfo, a tab in the userinfo, and a non-ASCII byte beside a match |
| 32 | `fixtures/measure-legs/forks.sh`, `serial.json` rows `forks.sh 5` and `forks.sh 0`, and `test_fork_count` |
| 34 | `test_no_bare_bash_argv`; the one `<bash>` and its refusal are built |
| 35 | `run_leg`'s failure branch, with `TerminateProcess(hProcess, 1)` |
| 36 | an arm over AC36's key; `read_turnstile`'s per-entry rule is built |
| 38 | `owner.json`, `derive_abandoned_scratch`, `write_recovered_logs`, `raw_recovered` |
| 39 | `printenv.py` gains its two lines; `derive_redacted`'s bytes path is built |
| 42 | the stall arm's line rule: exactly one STALLED line, naming `stall`, and none naming `steady` or `churn` |

`owner.json` holds `{"pid": <int>, "created": <FILETIME as int>, "record": "<converted path>"}`.
A process is live when `OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION)` opens it,
`GetExitCodeProcess` reads `STILL_ACTIVE`, and `GetProcessTimes` gives the recorded creation time.
`ERROR_INVALID_PARAMETER` from `OpenProcess` means no such pid, so the scratch is abandoned. Any
other failure, access denied included, cannot prove the owner dead, and the scratch is left alone.
The selftest runs the tool with `TMPDIR` set to its own temp dir, so the sweep it exercises never
reaches the operator's real scratch dirs.

`read_hold_beacon` exists because the beacon is the holder's only proof of holding, and a holder
that never takes the slot must end the arm, not stall it. `HOLD_BEACON_WAIT_S` is a declared
bound, not a measurement: the holder's start-up on node d plus the turnstile's acquire take well
under it.

### The census fields

| Line | Fields | `peak_mem_b`, `mem_b` | Command |
|---|---|---|---|
| fewer than 4 fields, or a non-numeric id | — | — | rejected, as today |
| 4 to 6 fields | legacy | None | `parts[4]` when present |
| 7 or more fields | current | `int(parts[4])`, `int(parts[5])`, each None when blank or not an integer | `parts[6:]` joined by the separator |

The unit of `PeakWorkingSetSize` is the one unit 18 confirmed against `Get-Process` and wrote into
spec 18's §4. The docstring states that unit, and the probe re-reads it from spec 18.

### The leg's declarations

| File | Row |
|---|---|
| `tools/gate-legs.json` | the `measure-legs selftest` guard gains three exact paths (S21) and `{prefix}/run-gates/kit.toml` (S29) |
| `tools/run-gates/kit.toml` | a `[[files]]` rule with `role = "project-owned"` whose include names each fixture under `fixtures/measure-legs/` literally, one element per file, as `tools/runlog/kit.toml:37-40` does; no `[[gate_leg]]` for the leg (S29) |
| `tools/run-gates/measure_legs.py` | `test_fixtures_withheld`, run by `cmd_selftest` (S29) |
| `tools/govkit/registry.toml` | one `[[exempt_leg]]` row (S29) |
| `tools/govkit/subject-pins.tsv` | one row, by `selfcheck --write` (S22) |
| `tools/run-gates/foreign-prefix.gov.test.sh` | one `WHOLE_RUN` row (S25) |
| `memory/guides/SESSION-KICKOFF.md` | a re-stamp naming `<p19>~1` in `<p19>`, and one naming `<p19>` in `<p19m>` (S1) |

The four guard paths are exact files, so none joins a broad guard, and each is carried by at most
five legs. With the fixtures withheld, the LF pin on `{kit}/*.sh` has nothing to miss in an adopter,
and gov's own `.gitattributes` pins `*.sh` LF (`git check-attr eol` reads `lf` for a fixture path).
The fixture list is typed beside the directory it describes, and `test_fixtures_withheld` is the
check in both directions that keeps it one fact. Its population is read off the filesystem, never
off the list it is compared against. The arm reads paths relative to `measure_legs.py`'s own
directory, so it passes at every prefix the foreign-prefix leg moves the tree to.

### The govkit sites

| Id | Site | Change |
|---|---|---|
| 40 | `_cmd_apply` RECEIPT, `update`'s three, `adopt`'s one | each `install.sums` write becomes `write_atomic(target / ".governance" / "install.sums", <text>)`, moved above its receipt write |
| 40 | `ADOPTER_BAR_PATHS` | gains `'"install.sums"'`; the routing arm's substring match then refuses a direct sidecar write |
| 23 | the comment block above `ADOPTER_BAR_PATHS`, and `write_atomic`'s docstring | each names the receipt and `install.sums` |
| 2 | the `cross-entry argv:` note | `argv element(s) offered` |
| 8 | the `carry_out_of_scope` paragraph of `write_gate_legs`' docstring | carries `TOOL-dRedressedBar-12` beside `TOOL-dRedressedBar-16` |

The sidecar write takes no new local, so no name in `_cmd_apply`'s long body can shadow it. The
member is a spelling, as `ADOPTER_BAR_PATHS`' comment says its members are. `"install.sums"`
appears at `:12153` in a tuple of strings, which the arm's derivation rule does not follow, and at
`:5322` in a read, which it does not grade.

### What this unit corrects in each spec

A corrected design paragraph carries `TOOL-dRedressedBar-19` and one sentence naming the change,
and this spec's §2 and §4 hold the design.

No one role can write these corrections and the product files in one commit. Under
`.claude/roles.json`, only `gov-spec-writer` writes spec files and only `gov-builder` writes
product files, and scratch-guard admits a builder's spec edit only where it moves the status and
date cells of a spec its card routes (`tools/hooks/scratch-guard.js:91-99`). So the rows below are
this unit's spec-writer pass, `<w19>`, M6's "a review's fixes folded in". The main loop dispatches
it once units 12 to 18 are CLOSED, with this table as its brief, and before the build pass. Each
target then takes its correction as a records fix with its status unchanged. It does not run
earlier: specs 12 and 14 to 18 are unbuilt until then, and folding into them before they build is
the first rejected alternative below. A build pass that finds no `<w19>` returns that to the main
loop before any write.

| Spec | Ids | What moves |
|---|---|---|
| 12 | 31 | S2 gains the inline note; revision line |
| 14 | 40 | "When CONFIGURE fails" gains the between-writes row; revision line |
| 15 | 2 | §4 "The ownership join": the OFFERED sentence and the note template; revision line |
| 16 | 8, 9, 18, 30, 31, 43 | S2 and AC3 require both tokens; S4 names spec 12's note; §3 gains the orphan gap; §4 step 4, "Why the carry is consistent", "What an adopter sees change" and "The arm"; AC1's fixture line; revision line naming AC8 |
| 17 | 2, 4, 5, 16, 17, 23, 40, 41 | §1; S10, S23; §4 Evidence, "Three choices", row 15, "Order, and unit 7"; §5; AC1, AC9, AC10 and AC23's wording; §10; revision line naming AC41 |
| 18 | 1, 6, 7, 10, 11, 12, 13, 14, 15, 19, 20, 21, 22, 24, 25, 26, 27, 29, 32, 33, 34, 35, 36, 37, 38, 39, 42 | S1, S4, S11, S13; §3 first non-goal; §4 candidates row 1, "Launching a leg", "The environment a leg gets", "The turnstile", "The census fields", "The record", "The selftest and its leg", Inventory; §5 security and error states; §7 leg line and its floor sentence; §10; revision line naming AC1, AC14 and AC42 |

### Order, and unit 7

Order 14 is one above unit 18's. Units 16, 17 and 18 write the files this unit corrects, so M6
sequences it after them. Units 12, 14 and 15 are edges because criteria here read what they built.
Unit 7's measurement need not cover this unit, because no kit version moves here (§3). The new
functions are minted in `measure_legs.py`, a file unit 18 adds to the symbol index, so this pass
runs `python tools/codebase-map/gen_map.py --write` alone before the product commit.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `read_profile_legs`, `read_hold_beacon` | functions | `py.function`, `read` |
| `build_holder_env` | function | `py.function`, `build` |
| `derive_abandoned_scratch` | function | `py.function`, `derive` |
| `write_recovered_logs` | function | `py.function`, `write` |
| `test_no_bare_bash_argv`, `test_fork_count`, `test_manifest_refusals`, `test_fixtures_withheld` | selftest arms | `py.function`, `test` |
| `OPTIONAL_FIELDS`, `HOLD_BEACON_WAIT_S` | constants | none declared for constants |
| `owner.json`, `raw_recovered`, `launch_error` | record names | none |

Each function name answered OK under `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
on 2026-10-14, and `test_fixtures_withheld` on 2026-10-15.

### Files touched (estimate)

- `tools/run-gates/measure_legs.py`
- `tools/run-gates/held_halves.py`
- `tools/run-gates/fixtures/measure-legs/`
- `tools/run-gates/kit.toml`
- `tools/run-gates/foreign-prefix.gov.test.sh`
- `tools/gate-legs.json`
- `tools/govkit/govkit.py`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/process-monitor/census.py`
- `tools/process-monitor/selftest.py`
- `help/measure-legs.md`
- `memory/map/generated/`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dRedressedBar/build/`

`<p19>` touches `memory/guides/SESSION-KICKOFF.md` for the staged ratchet's re-stamp, and `<p19m>`
touches it again for the re-audit (S1). Specs 12 and 14 to 18 are `<w19>`'s write set, not the
build pass's.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| Fold each fix into specs 16 to 18 now, before they build | M4 forbids folding at a CONVERGED exit (owner, SPEC 2026-10-05) | Refused by the method |
| Two batch units, the profiler and the govkit corrections | the profiler half writes `tools/govkit/registry.toml` and `subject-pins.tsv`, which the govkit half's `govkit.py` reads in selfcheck and generates, so M6 clauses 2 and 3 both fail | Rejected |
| Id 20 by running the runner's `sed` per leg log | MSYS `sed` drops the CR of a CRLF (`run-gates.sh:305-307`), so id 39's byte contract cannot hold | Rejected; S20 keeps the port under a parity arm |
| Id 19 by catching `SystemExit` from `load_manifest` | its line has already printed `held-halves: REFUSED`, which misnames the tool | Rejected; S19 passes a refusal function |
| Id 12 with a stale output staged in the turnstile arm | the arm runs on every bar, and staging writes into the tree it runs over | Rejected; AC12 exercises the bound on a key no holder writes |
| Id 38 by the finding's own fix, "a scratch still holding raw files" | a profile running at the same moment matches too, and its live captures would be deleted (the skeptic's refutation) | Rejected; S38 proves the owner dead |
| Id 11 by refusing the whole run on an unconvertible turnstile key | the job readings stay true without the turnstile, and a refused read already sets every reading aside | Rejected; S11 makes it a refused read, and only the scratch dir refuses the run, under spec 18's S15 |
| Id 41 by begin and end markers | they bind a layout the `[dRB-15]` checks may interleave with, where a label filter reads each check wherever it sits | Rejected; S41 reads by label |
| The spec corrections in the build pass's own commit, as rev-2 wrote it | scratch-guard refuses a builder's edit to another spec, and the spec writer writes no product file, so no role can make that commit (unit 10's divergence, `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`) | Refused by the hook |

## 5. Production-readiness checklist

- security — S38 closes the leak F2 of spec 18 left on a crash, a kill or a power loss: the next
  run redacts and deletes a dead run's raw captures, and proves the owner dead by pid and creation
  time before touching anything. S39 keeps the redaction byte-exact and S20 holds it to the
  runner's. S35 adds the tool's only terminate, on a suspended process that has run nothing. S29
  stops shipping a leg whose dependencies an adopter cannot see. S40 leaves no truncated sidecar.
- perf / scale — N/A — one directory listing of scratch siblings per run, and two atomic renames
  per receipt write.
- error / empty / loading states — An empty `resolve_bash` result and each malformed manifest class
  refuse with exit 2 and one named line. A turnstile key that does not convert is a refused read at
  every tick. A launch failure records the leg as `fail` and the run continues. A half-written
  beacon or a vanished ticket is not judged.
- observability — The envelope records every recovered capture and every launch failure.
- risks — `held_halves.load_manifest` gains a keyword and a longer refusal message, and its three
  callers pass nothing new, so `held-halves selftest` grades it unchanged. The census's legacy
  rule keeps a five-field line readable, so a census taken by an older query still parses. The
  `measure-legs selftest` guard widens by four files, so a scoped bar runs it on an edit to any.
  Editing `tools/gate-legs.json` trips both run-gates canaries and the kickoff-manifest ratchet,
  which `<p19>` and `<p19m>` each re-stamp (S1). A fixture added without its name in the
  descriptor's list would ship to adopters; `test_fixtures_withheld` reds on it instead.
- testing — AC1 to AC44 are direct runs of the profiler over committed fixtures, in-process python
  probes, `ast` and grep probes over source and specs, and a fault-injected apply under `%TEMP%`.
  The new arms are declared in §7.
- migration — `owner.json` is new and optional on read: a scratch without one, which every
  pre-unit-19 run leaves, is left alone. Census rows keep their two optional keys. No receipt
  field, conf key or deploy shape moves.
- user docs — `help/measure-legs.md` gains `raw_recovered` and `launch_error` in its "What it
  writes" section, and a line saying a later run sweeps a dead run's raw captures.

## 6. Acceptance criteria

AC<n> observes S<n>, so the numbering skips 3 and 28, and S26, S33, S24 and S31 are observed
by AC1, AC10, AC7 and AC31. `<pN>` is the commit of unit N's build pass, as unit N's
acceptance ledger names it. `<p19>` is this unit's product commit and `<p19m>` its manifest
re-stamp commit. `<w19>` is the commit of this unit's spec-writer pass, which §4 "What this unit
corrects in each spec" describes; its subject names `TOOL-dRedressedBar-19`, and this unit's
ledger names it. `<ml>` is `python tools/run-gates/measure_legs.py`, `<fx>` is
`tools/run-gates/fixtures/measure-legs`, `<o>` is a fresh dir under `%TEMP%`, and `<r>` is the
run dir the tool prints. `<sN>` is
`memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-N.md`. "Joined" means
piped through `tr '\n' ' ' | tr -s ' '`. A red half "over `<p18>`" runs the file from a local
`git clone` of gov under `%TEMP%`, checked out at `<p18>`. Every command runs from the
worktree root on node d.

- **AC1** — `git show <p19> -- memory/guides/SESSION-KICKOFF.md` moves the `last-audit:` line to
  name `<p19>~1`, and `git log -1 --format=%B <p19>` carries `manifest-audit:`. At `<p19m>`, the
  `last-audit:` line of `memory/guides/SESSION-KICKOFF.md` names `<p19>`, and
  `git show <p19>:tools/gate-legs.json` holds a row named `measure-legs selftest` whose guard holds
  the derive-ceilings path S21 adds. `git log -1 --format=%B <p19m>` carries `manifest-audit:`.
  Spec 18's §7 leg line carries `` `kickoff-manifest ratchet` ``.
  Red when: over `<p18>`, the line names a sha whose manifest holds no `measure-legs selftest` row;
  and with `<p19>`'s product files staged and no re-stamp, `bash skills/session-kickoff/manifest-check.sh --staged`
  exits non-zero, printing `staged changes touch watched files`.
- **AC10** — A python program imports `tools/process-monitor/census.py`. `census.OPTIONAL_FIELDS`
  equals `("peak_mem_b", "mem_b")` and `census.FIELDS` is the nine-key tuple. Fed to `parse_cim`
  and `build_windows_rows`, a seven-field line gives a row with both keys as ints and its command
  intact; a five-field line gives both as None and its command intact; a seven-field line with both
  memory fields blank gives a row with both None, and the rejected count is 0. Every row's key set
  contains `FIELDS` and lies within `FIELDS` plus `OPTIONAL_FIELDS`. `ast.get_docstring` of the
  module carries `peak_mem_b`, `mem_b` and `int|None`. `inspect.getsource` of
  `test_row_contract_is_complete` carries `OPTIONAL_FIELDS`.
  Red when: over `<p18>`, the five-field line's row reads `command` None, its command taken as a
  memory field, and the module has no `OPTIONAL_FIELDS`. The blank-memory line already stays a row
  there, so that half is the liveness case and not the red one.
- **AC11** — A python program imports `measure_legs` and calls
  `resolve_turnstile_dir(<bash>, <env>)`, where `<env>` is its own environment with `PATH` set to
  `/nonexistent`, so the script finds no `cygpath`. It returns `("", "")`, and
  `measure_legs.read_turnstile` over that key raises `OSError`, the refused read. Under its own
  `PATH` the same call returns a pair whose second member matches `^[A-Za-z]:/`.
  Red when: a copy keeping the set-aside fallback returns the bash spelling as the key it opens.
  `read_turnstile` over it raises nothing and lists no holder, and a leg's eighth field would read 0.
- **AC12** — A python program imports `measure_legs`. `build_holder_env({"GATE_REGEN_CHECK": "1", "GATE_JOBS": "3"})`
  returns a dict whose `GATE_REGEN_CHECK` is `0` and which holds no `GATE_JOBS`.
  `read_hold_beacon(<temp key>, <a child running sleep 30>, 2)` returns None within 4 s, and the
  child is still running. With a child that exits at once after printing `holder-said`, it returns
  None within 1 s, and the arm's failure line carries `holder-said`.
  Red when: `build_holder_env` sets nothing after the scrub, so `GATE_REGEN_CHECK` is absent.
- **AC19** — A python program imports `measure_legs`. `hasattr(measure_legs, "read_legs")` is
  False, and `inspect.getsource(measure_legs.read_profile_legs)` carries `load_manifest(`.
  `inspect.signature(held_halves.load_manifest)` has a `refuse` parameter. Spec 18's §10, cut with
  `sed -n '/^## 10. Reuse/,$p'` and joined, carries `held_halves.load_manifest` and
  `derive-ceilings.read_legs`.
  Red when: over `<p18>`, `measure_legs.read_legs` exists and its source calls no `load_manifest`.
- **AC20** — A python program imports `measure_legs`, takes `redact` with
  `extract_runner_function`, and runs it in the resolved bash over S20's eight shapes on stdin. The
  output equals `measure_legs.derive_redacted` over the same bytes, byte for byte.
  Red when: a copy whose port drops `\s` from both classes differs on the tab shape.
- **AC21** — A python program loads `tools/gate-legs.json` and reads each guard path with `{prefix}`
  read as `tools`. The `measure-legs selftest` guard then holds `tools/run-gates/derive-ceilings.py`,
  `tools/run-gates/held_halves.py` and `.githooks/pre-push`, each as an exact file. `check_guard_trips`,
  loaded from `tools/check-spec-tokens.py`, returns True for `tools/run-gates/derive-ceilings.py`
  against that guard.
  Red when: over `<p18>`, the guard holds none of the three, and the predicate returns False for
  every guard path.
- **AC25** — `grep -c '"measure-legs selftest|a --selftest mode of a shipped engine' tools/run-gates/foreign-prefix.gov.test.sh`
  prints 1, and the line sits inside the `WHOLE_RUN=(` array.
  Red when: over `<p18>`, it prints 0.
- **AC27** — Spec 18's §7, cut with `sed -n '/^## 7. Gates/,/^## 8/p'`, carries
  `` `measure-legs selftest` `` on its leg line. A python program loads `tools/check-spec-tokens.py`,
  reads spec 18's backticked §4 Files touched paths and §7 leg line, and joins each path against
  every guarded leg from `derive_guarded_legs` over `tools/gate-legs.json`. Every joined leg it
  finds is named on the line.
  Red when: the same program over `git show <p18>:<s18>` finds `measure-legs selftest` unnamed.
- **AC29** — A python program run from `tools/govkit` imports `govkit`, reads
  `tools/run-gates/kit.toml` with `tomllib`, and loads it through
  `govkit.resolve_descriptor_paths(<desc>, "tools")`. The elements of every list include on a
  `project-owned` rule that open `fixtures/measure-legs/`, each prefixed `tools/run-gates/`, equal
  the set `git ls-files tools/run-gates/fixtures/measure-legs` prints, and no `project-owned`
  element carries `*`, `?` or `[`. `govkit.resolve_rule_pool` over the rule whose include is `**`,
  with `govkit.canonical_ctx("run-gates")` and the loaded descriptor's `home`, holds no path under
  `tools/run-gates/fixtures/measure-legs/`. No `[[gate_leg]]` is named `measure-legs selftest`.
  `tools/govkit/registry.toml` holds an `[[exempt_leg]]` with that name whose `why` carries
  `process-monitor` and `Windows`. `tools/gate-legs.json`, `tools/run-gates/selftest-budgets.txt`
  and `tools/run-gates/windows-only-legs.txt` each carry the name, and the leg's guard in
  `tools/gate-legs.json` holds `{prefix}/run-gates/kit.toml`.
  Red when: the same program, with that rule's include respelled `["fixtures/measure-legs/**"]`,
  finds every fixture in the `**` rule's pool, the vacuous pass rev-5's string check allowed; and
  over `<p18>`, the descriptor holds the `[[gate_leg]]`, the registry holds no such
  `[[exempt_leg]]`, and the pool holds every fixture.
  figure: the fixture set is DERIVED from `git ls-files` at observation time, 13 once S32 lands.
  The glob spelling's 12 of 12 in the pool is PINNED, measured on 2026-10-15 at `3275f305a`.
- **AC34** — `test_no_bare_bash_argv`'s scan, run by a python program over
  `tools/run-gates/measure_legs.py` with `ast`, finds no call to a `subprocess` function whose first
  argument is a list or tuple opening with the constant `'bash'`. A program that rebinds
  `measure_legs.profile_bar.resolve_bash`, the function `run_profile` calls, to return
  `("", ["cand-a", "cand-b"])` and calls `measure_legs.main` with
  `--serial --legs <fx>/serial.json --out <o>` gets the return value 2 before any leg, `<o>` stays
  empty, and its stderr carries `cand-a` and `cand-b`.
  Red when: a copy with one `subprocess.run(["bash", ...])` makes the scan find it.
- **AC35** — A python program rebinds `measure_legs.build_job` to a wrapper that returns a real job
  for its first two calls, the twin launches of the interpreter probe, which runs before the first
  leg, and from its third call on a job handle it has already closed. It runs `main` over a temp
  manifest holding `spawn.py 0 1`. `main` returns 0
  within 60 s. The leg's `.leg` row reads `fail` with rc 1, its `<i>.json` `launch_error` opens
  `launch: AssignProcessToJobObject`, and a fresh `scan_processes()` holds no row with the root's
  winpid.
  Red when: a copy with the terminate taken out leaves the run open at the 60 s bound, with the
  suspended root alive.
  cost: up to a minute.
- **AC36** — A python program builds a temp key holding `gate-bar-beacon/` with no `pid` file, a
  `gate-bar-beacon.1/` whose `pid` reads `x`, and a ticket in `gate-bar-queue/` whose name has no
  pid field. `measure_legs.read_turnstile(<key>)` reports no refusal and lists no holder and no
  ticket pid. A key whose `gate-bar-queue` is a file reports a refusal.
  Red when: a copy that treats a missing `pid` file as a refused read reports one for the first
  key, and the leg's eighth field would read `unknown`.
- **AC38** — A python program makes a temp `TMPDIR` holding two scratch dirs. The dead one's
  `owner.json` names a child process that has since exited, with that child's creation time, and a
  record dir under `<o>`, and its raw capture for leg 0 holds `https://u:s3cret@example.invalid/`.
  The live one's `owner.json` names the program's own pid and creation time, and its raw capture
  for leg 0 holds `live-bytes`. It then runs `<ml> --serial --legs <fx>/serial.json --out <o>` with that `TMPDIR`.
  The dead raw file is gone. `<o>`'s recovered log carries `://***:***@`, and `grep -r s3cret <o>`
  and the same over the dead scratch print nothing. The live raw file still reads `live-bytes`. The
  new run's envelope names the dead capture in `raw_recovered`. `help/measure-legs.md` carries
  `raw_recovered` and `launch_error`.
  Red when: a copy whose test reads the pid alone, with the live owner's creation time altered,
  deletes the live raw file; and with the sweep taken out, the dead raw file still carries
  `s3cret`.
- **AC39** — `measure_legs.derive_redacted(b"a\xe7\r\nhttps://u:s3cret@h\x00z")` returns
  `b"a\xe7\r\nhttps://***:***@h\x00z"`. On a run of `printenv.py` through `<fx>/serial.json`, its
  `<i>.log` holds the byte `0xe7`, a CR, and `://***:***@` twice, and no `s3cret`.
  Red when: a copy that decodes the capture with `errors="replace"` loses the `0xe7` byte from the
  log.
- **AC40** — `govkit.ADOPTER_BAR_PATHS` holds `'"install.sums"'` and `receipt_path`.
  `grep -c '"install.sums").write_text' tools/govkit/govkit.py` prints 0. A python program wraps
  `pathlib.Path.write_text` so a call on `install.sums.govkit-new` writes half its text and raises
  `OSError`, and runs `govkit.main` with `apply --target <t> --kits check-wiring` over a target
  holding an earlier receipt. The call fails, and the target's sidecar and receipt each equal their
  earlier bytes. `python tools/govkit/govkit.py check --target <t>`
  then prints no line carrying `install.sums carries` or `which install.sums does not`. Spec 14's
  "When CONFIGURE fails" section, cut and joined, carries `install.sums`.
  Red when: over `<p18>`, the same fault on a plain `install.sums` write truncates it, and `check`
  prints a sidecar mismatch line.
  cost: two applies and a `check`, about two minutes.
- **AC41** — A python program run from `tools/govkit` reads govkit's self-test module as text,
  parses it with `ast`, and collects every call to `check` whose first argument is a string
  constant. Those whose label opens `[dRB-14]` number at
  least one, and none of their sources carries `kit 'agent-cap'`. One whose label opens `[dRB-15]`
  asserts that no line opens `govkit: kit '`. Spec 17's AC1, cut and joined, carries `label` and no
  `first to the last line carrying`.
  Red when: a copy whose `[dRB-14]`-labelled check carries `kit 'agent-cap'` makes the program find
  it, wherever that check sits.
- **AC2** — `grep -c 'slash-bearing' tools/govkit/govkit.py <s15> <s17>` prints 0 for each file, and
  `grep -c 'argv element(s) offered by' tools/govkit/govkit.py` prints 1. Spec 17's §4 row 15 carries
  `note template`.
  Red when: over `<p18>`, the engine's count is 1.
- **AC4** — `grep -c 'above every unit' <s17>` prints 0. Spec 17's §1, cut with
  `sed -n '/^## 1. Goal/,/^## 2/p'` and joined, carries `build-order`.
  Red when: the count prints 2, as over the audited blob `8910bf9c`.
- **AC5** — Spec 17's AC9, cut from `- **AC9**` to `- **AC10**`, carries each of `:7424`, `:7502`,
  `:7540`, `:7593`, `:7616` and `:7621`, and `7424 7502 7540 7593 7616 7621`.
  Red when: the cut carries `:7616` nowhere, as over `8910bf9c`.
- **AC6** — `grep -c "No change to the merge bar's behaviour, ceilings or legs" <s18>` prints 0,
  and spec 18's §3, cut and joined, carries `existing leg's argv, guard or ceiling`.
  Red when: it prints 1, as over `b3f92c49`.
- **AC7** — A python program splits `tools/run-gates/README.md` at its `## ` headings, and one
  section carries both `measure_legs.py` and `--concurrent`. `memory/map/features/run-gates.md`
  carries `tools/run-gates/measure_legs.py` and `measure-legs selftest`. Spec 18's S13, cut and
  joined, carries `TOOL-dRedressedBar-19`.
  Red when: either file lacks its strings; the program then names the one missing.
- **AC8** — `ast.get_docstring` of `write_gate_legs` in `tools/govkit/govkit.py` carries both
  `TOOL-dRedressedBar-12` and `TOOL-dRedressedBar-16`. Spec 16's §2 and its AC3, each cut and
  joined, carry both.
  Red when: a docstring carrying only `TOOL-dRedressedBar-16`, as spec 16's S2 allows, fails the
  first half, and spec 12's AC4 reds on its re-observation.
- **AC31** — Spec 12's §2, cut with `sed -n '/^## 2. Scope/,/^## 3/p'` and joined, carries
  `superseded by TOOL-dRedressedBar-16`. Spec 16's S4, cut and joined, carries `inline note`.
  Red when: the cut lacks it, as over the blob spec 12 holds at `17908e7d`.
- **AC9** — `grep -c 'selftest.py:15412' <s16>` prints 0, and `grep -c 'selftest.py:15428-15459' <s16>`
  prints at least 1.
  Red when: the first prints 1, as over `87f10494`.
- **AC13** — Spec 18's §7 cut carries `` `kit epoch (shipped bytes move, the version moves)` `` on
  its leg line and carries `floor`.
  Red when: the cut carries neither, as over `b3f92c49`.
- **AC14** — `git grep -h -o 'gov:kit process-monitor@[0-9.]*' -- tools/process-monitor ':!*.test.sh'`,
  piped through `sort -u`, prints one line, and its version is above 0.18. Spec 18's revision log
  holds a line naming report id 14 and this AC14.
  Red when: the same grep without the exclusion prints two lines, `@0.15` among them, which is the
  literal reading spec 18's AC14 cannot pass.
- **AC15** — Spec 18's S11, cut and joined, carries `$WORK/$i$sfx.raw` and `run-gates.sh:3877`, and
  no `run-gates.sh:3916`.
  Red when: it carries `run-gates.sh:3916`, as over `b3f92c49`.
- **AC16** — `grep -c 'kit.toml:103' <s17>` prints 0, and `grep -c 'kit.toml:104' <s17>` prints at
  least 3.
  Red when: the first prints 3, as over `8910bf9c`.
- **AC17** — `grep -c 'six writes' <s17>` prints 0.
  Red when: it prints 2, as over `8910bf9c`.
- **AC18** — `grep -c ':11880-11891' <s16>` prints 0, and `<s16>` carries both `:11888-11890` and
  `:11898-11903`.
  Red when: the first prints 2, as over `87f10494`.
- **AC22** — `grep -c -P '^measure-legs selftest\tkit\tselftests$' tools/govkit/subject-pins.tsv`
  prints 1.
  Red when: the row is absent; govkit selfcheck then fails at `tools/govkit/govkit.py:2960`.
- **AC23** — `ast.get_docstring` of `write_atomic` carries `receipt` and `install.sums`. The source
  lines between the line carrying `THE DECLARED ADOPTER-BAR DESTINATION SET` and the line opening
  `ADOPTER_BAR_PATHS =` carry `receipt` and `install.sums`. Spec 17's AC23, cut and joined, carries
  `docstring`.
  Red when: over `<p18>`, the docstring and the comment block name the receipt, which unit 17 added,
  and neither carries `install.sums`.
- **AC30** — Spec 16's "What an adopter sees change" table, cut with
  `sed -n '/^### What an adopter sees change/,/^### The arm/p'`, carries `derive_parity_lines`.
  Red when: it does not, as over `87f10494`.
- **AC32** — `<ml> --serial --legs <fx>/serial.json --out <o> --census-every 1` runs `forks.sh 5` and
  `forks.sh 0`. The difference of their `procs_total` in `<r>/legs.tsv` is at least 10.
  Red when: the job is created with `JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK`, and the difference
  reads 0.
  figure: 10 is twice the fixture's argument, DERIVED; each subshell and each substitution is at
  least one process.
- **AC37** — For each of eight temp manifests, unparseable JSON, a top-level object, a non-object
  row, an empty list, a duplicate name, an argv holding a number, a name holding a tab, and an argv
  token `{nope}/x`, `<ml> --serial --legs <manifest> --out <o>` exits 2. Neither its stdout nor its
  stderr carries `Traceback`, one stderr line opens `measure-legs: REFUSED — `, and for the five
  row classes that line carries `row `.
  Red when: over `<p18>`, the tab-name manifest runs its leg and exits 0, and the refusals of the
  number-argv and duplicate-name manifests name the leg and carry no `row `.
- **AC42** — `<ml> --serial --legs <fx>/stall.json --out <o> --census-every 1 --stall-window 8 --stall-cpu 0.5`
  prints exactly one line opening `measure-legs: STALLED  `, and it opens
  `measure-legs: STALLED  stall  `, the leg `stall.json` runs `stall.sh` under. No such line opens
  with the leg `steady` or `churn`.
  Red when: a copy that prints the STALLED line with a sibling leg's name passes the whole-output
  match and fails this one.
- **AC43** — Spec 16's §4 cut, joined, carries no `so the carried row names a claimed kit`, and its
  §3 cut carries `orphan`.
  Red when: the sentence stands, as over `87f10494`.
- **AC44** — `git diff <w19>~1 <w19> -- memory/builds/dRedressedBar/spec/` shows specs 12, 14, 15,
  16, 17 and 18 each with one header rev change and one new revision line, and each line names
  `TOOL-dRedressedBar-19` and every report id §4's table assigns that spec. Each of the six specs
  carries a CLOSED header at `<w19>~1`. `git diff --name-only <p19>~1 <p19> -- memory/builds/dRedressedBar/spec/`
  and the same over `<p19m>` name no file but this spec. The ledger S44 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-19`.
  Red when: a spec takes no bump, two bumps, or a revision line missing one of its ids, a target was
  folded before it closed, or a build-pass commit writes another spec.

## 7. Gates

`measure-legs selftest` · `held-halves selftest` · `process-monitor census selftest` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `every held leg is budgeted, every budget row resolves` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

The line is a floor, derived by joining §4 Files touched against the guards in `tools/gate-legs.json`
with `BROAD_LEG_FLOOR` applied, plus the unguarded legs the change moves. `measure-legs selftest`
resolves: unit 18 landed its row in `6783992aa`.

New arm: tools/run-gates/measure_legs.py --selftest · covers AC11 AC12 AC34 AC36 · the turnstile key's `cygpath` fallback kept, `build_holder_env` setting nothing, a bare `'bash'` argv, and a pid-less beacon read as refused, each on a copy in the selftest's temp dir · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC20 AC39 · a port dropping `\s` from its classes, and a port decoding with replacement · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC32 AC35 AC37 AC38 AC42 · breakaway allowed, the launch terminate taken out, a refusal class let through, a pid-only liveness test, and a STALLED line naming a sibling · none
New arm: tools/run-gates/measure_legs.py --selftest · covers AC29 · `test_fixtures_withheld` over `tools/run-gates/kit.toml` with one fixture name taken out of the list, and again with the list respelled as one `fixtures/measure-legs/**` element · none
New arm: tools/process-monitor/selftest.py · covers AC10 · `test_row_contract_is_complete` over a row carrying an undeclared extra key, and `test_cim_memory_fields_are_bytes`' blank-memory and legacy cases over a parser that rejects a blank memory field or reads a five-field line's command as memory · none
New arm: tools/run-gates/foreign-prefix.gov.test.sh · covers AC25 · the `WHOLE_RUN` row taken out, where the leg reds as an undeclared whole run · none
New arm: tools/govkit/selftest.py · covers AC40 · the `[-21] AC2` routing assertion with one sidecar write respelled as a direct `write_text`, where its no-direct-write check reds · none

The refusal join's floor does not move: S40 adds no `r.fail` site. The main loop observes each new
or moved arm red, then green, at the close, and runs the bar once after the last unit is terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, promoted at the CONVERGED exit of the units-16-18 spec audit.
  All 41 confirmed medium and low findings, by report id, are batched into this unit by M4. Each
  claim was re-read at `17908e7d`, whose `tools/` equals `ebce889c`'s, and at the blobs the report
  pins. Ids 19, 29 and 38 take the skeptic's corrected fixes. Id 12's staged-stale case and id 41's
  markers depart from the report's sketch (§4 "Alternatives rejected").
- rev-2 · 2026-10-14 · H1 · §6 · the commit holding this unit's promotion was refused by HYGIENE
  checks 7 and 12. Check 7's `README.md:134` counts body lines after the front matter, so it is
  file line 143, this unit's index row at 370 chars, not spec 10's at 308: the H1 now ends "the
  receipt sidecar made atomic, and specs 12 and 14 to 18 corrected". Check 12's `AC10` was not
  the criterion, which carries its `Red when:` line, but the §6 preamble, whose second line opened
  with `AC10,` at column 0 and so was read as a bullet with no clause: the preamble is rewrapped
  so no line opens with a label. No scope, design, criterion or order moves.
- rev-3 · 2026-10-14 · §1 · S44 · §4 · AC44 · unit 10's builder divergence, applied here
  (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`): no role can make a build-pass
  commit that also edits another spec, because scratch-guard admits a builder's spec edit only to
  its own status and date cells (`tools/hooks/scratch-guard.js:91-99`). The moved items: S44's six
  rev bumps, and the spec halves of S1, S2, S4 to S9, S13 to S23, S27, S30 to S32, S35, S38 and S40
  to S43, are now this unit's spec-writer pass `<w19>`, dispatched once units 12 to 18 are CLOSED
  and before the build pass. They are not folded now, because those six specs are unbuilt and the
  first rejected alternative still holds. §4 Files touched lists product files, the manifest and the
  ledger only. AC44 reads `<w19>` in place of `<p19>` and observes that neither build-pass commit
  writes another spec. Alternatives rejected gains one row. No product design or other criterion
  moves.
- rev-4 · 2026-10-15 · S1 S11 S38 · §3 · §4 · §5 · AC11 AC38 · §7 · unit 18's builder divergence
  (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-18-4-revision.md`): native Python cannot open the
  profiler's bash scratch spelling, so unit 18 needs the `cygpath -m` conversion already. Spec 18
  rev-4's S15 takes the conversion of the scratch dir, the turnstile key and the probed launchers,
  with both spellings in the envelope and the help page. S11 keeps the turnstile key's
  failed-conversion rule, and AC11 observes that alone; `resolve_win_path` leaves the inventory.
  S38, AC38, §3 and §5 no longer claim the two `_posix` keys. S1 states that unit 18's pass commit
  carries the ratchet's staged re-stamp and keeps `<p19m>` as the reviewed re-audit. The `<w19>`
  pass and its table do not move.
- rev-5 · 2026-10-15 · S7 S8 S10 S11 S12 S14 S19 S20 S29 S32 S34 S35 S36 S37 S38 S39 S41 S42 · §3 ·
  §4 · §5 · AC10 AC23 AC34 AC35 AC37 AC42 · §7 · this unit's spec-writer pass `<w19>`, run at
  `997fc294f` once units 12 to 18 were CLOSED, which also took the corrections §4's table assigns
  specs 12 and 14 to 18. This spec was audited against spec 18 rev-3, and unit 18 built rev-4, so
  every item reading the profiler, its fixtures, its declarations or the census was re-read over the
  built tree; §4 gains "Evidence, read at `997fc294f`". Already built, so the build pass writes
  nothing for them: S7, S8, S14 and S41. Built in part, each item now stating what remains: S10
  (`OPTIONAL_FIELDS`, the legacy and `parts[6:]` rules, the contract arm, the separator table; the
  blank-memory and legacy cases join unit 18's `test_cim_memory_fields_are_bytes`, so
  `test_cim_memory_fields` leaves the Inventory and the AC10 `New arm:` line), S12 (the 120 s
  inline wait becomes `read_hold_beacon`, `HOLD_BEACON_WAIT_S` is 120, the bound the budget row
  prices, in place of 60), S34 (only `test_no_bare_bash_argv`), S36 (only its arm), S37 (the
  tab-bearing name, the unresolved token and the row index) and S39 (only `printenv.py`'s two
  lines). Restated over the built code: S11 cites the built `TURNSTILE_SCRIPT`; S19's Readers name
  the built reader and its one caller, and its refusal raises `ProfileRefused`; S20 cites the
  extraction seam and `redact`'s tip line; S29's Readers name the built descriptor row and the
  files spelling the leg; S32 moves `test_serial_run`'s count from four legs to six; S35 states
  that the branch in `run_leg` also covers the interpreter probe; S38, §3 and §5 name the help
  page's "What it writes" list, since the page holds no record table; S42 reads the STALLED line by the
  manifest names `stall`, `steady` and `churn`, since the line prints a leg's name and not its
  script. Criteria whose halves could not hold over the built tree: AC10's red half read a
  blank-memory rejection the build never made, and now reads the five-field line's lost command;
  AC23's red half read a docstring unit 17 already changed; AC34 rebound a name the module does not
  bind, expected `SystemExit` from a `main` that returns, and read stdout for a stderr line; AC35's
  closed job would have refused the interpreter probe before any leg; AC37's red half expected a
  traceback the built reader already refuses; AC42 matched script names the line never prints.
  Files touched drops `tools/run-gates/README.md` and `memory/map/features/run-gates.md`, which
  S7 no longer writes. Both reds unit 18's builder handed here still hold: `subject-pins.tsv` has
  no `measure-legs selftest` row (S22) and `WHOLE_RUN` names it nowhere (S25). No other scope
  item, criterion or the `<w19>` table moves.
- rev-6 · 2026-10-15 · S1 S29 · §3 · §4 · §5 · AC1 AC29 · §7 · unit 19's builder divergence
  (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-6-revision.md`), re-read at `3275f305a` in §4's
  new evidence. S29, §4's `kit.toml` row and AC29 named a `fixtures/measure-legs/**` include, and
  govkit's `rule_sources` drops every glob-bearing element of a list include, so that rule claimed
  nothing and the `**` engine rule kept all 12 fixtures. AC29's string check would have passed over
  that. S29 now names each fixture literally, 13 once S32 lands, as `tools/runlog/kit.toml:37-40`
  does. AC29 reads that the list equals `git ls-files` of the fixture directory and that
  `govkit.resolve_rule_pool` over the `**` rule holds no fixture, and its red half is the glob
  spelling. A new arm, `test_fixtures_withheld` in `measure_legs.py --selftest`, reds when the list
  and the directory differ, and the leg's guard gains `{prefix}/run-gates/kit.toml`, the file the
  arm reads (§3, §4 Inventory and table, §5, §7 `New arm:`). The builder's second finding: `<p19>`
  stages `tools/gate-legs.json`, which the kickoff manifest watches, so the staged ratchet refuses
  it without a re-stamp. S1 and §4's table now give `<p19>` its own re-stamp naming `<p19>~1`, as
  unit 18's pass commit did, and `<p19m>` re-stamps naming `<p19>`. AC1 observes both, and Files
  touched says both commits touch the manifest. No other scope item, criterion or the `<w19>` table
  moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read and validate the gate leg manifest json and refuse
a malformed row"` ranked name-stem SEAMs (`rows`, `read`, `legs`, `manifest`) and not
`held_halves.load_manifest`. `python tools/codebase-map/reuse_lookup.py "convert an MSYS bash path
to a Windows path before python opens it"` ranked `resolve_python` and `resolve_bash`, and no
converter: no Python file under `tools/` calls `cygpath`, and two suites call it from bash
(`tools/memory-recall/recall-opened.test.sh:25`). Both misses are recorded as misses. The seams
extended were found by reading the report's citations. `held_halves.load_manifest`
(`tools/run-gates/held_halves.py:80-88`) is the reader S19 wraps, extended by one keyword.
`profile_bar.resolve_bash` (`tools/run-gates/profile_bar.py:282-304`) is the one bash S34 routes
through. `extract_runner_function`, unit 18's seam, gives S20 the runner's `redact`.
`write_atomic` and its declared population `ADOPTER_BAR_PATHS` (`tools/govkit/govkit.py:3964-4000`)
are the writer and the gate S40 extends, and the `[-21] AC2` routing arm
(`tools/govkit/selftest.py:15838-15917`) grades the new member with no new code. The
`[[exempt_leg]]` shape follows `profile-bar selftest` (`tools/govkit/registry.toml:610-612`), and
the `WHOLE_RUN` row follows `held-halves selftest`. The manifest re-stamp follows commit
`2e187ee8b` and unit 17's S18, and `<p19>`'s bundled re-stamp follows unit 18's `6783992aa`. S29's
literal fixture list follows `tools/runlog/kit.toml:31-40`, and `test_fixtures_withheld` follows
that kit's `test_kit_declarations` (`tools/runlog/selftest.py:1010-1026`), its population read off
the filesystem and never off the list.

The gotchas checklist for `tools/run-gates/measure_legs.py`, `tools/process-monitor/census.py`,
`tools/govkit/govkit.py` and `tools/gate-legs.json` selected these classes, each answered here:
- `a-folded-field-leaves-its-row-shape-docs-behind`, the class of ids 10 and 33, which is why S10
  names the docstring and every fixture of the old shape. The process-monitor README describes no
  row shape.
- `a-new-leg-trips-a-growing-set-of-meta-gates`, the class of ids 22 and 25, which is why §4 lists
  every file the leg owes and §7 names the meta-gates.
- `a-new-local-collides-in-a-long-function`, which is why S40 adds no local to `_cmd_apply`.
- `staged-break-substitutes-a-synthetic-value`, which is why AC38's dead owner is a real exited
  process and AC32's fork fixture forks rather than spawning natively.
- `fixture-passes-by-finding-nothing`, which is why AC12 and AC38 each assert the case that must
  stay untouched beside the one that must change.
- `two-answers-to-one-question`, which is why S19 wraps one reader and S20 holds the port to the
  runner.

The recall probe returned `TOOL-aEvidencedLens-20`, `TOOL-aDistilledCharter-7`,
`TOOL-dRedressedBar-13` and `TOOL-dRedressedBar-17`, the precedent minors batches. Each observed
built units' criteria in a corrected form and corrected prose with one rev bump per spec, and this
unit takes their shape. The report and the code agree on every citation re-read, with one
exception: `derive_parity_lines` starts at `tools/govkit/govkit.py:6075`, not `:6092`.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit's batch of minor
findings over a profiler and a deployer closed after the faulted units are built" --terms
"spec-audit minors batch promoted unit corrected observation rev bump ledger measure_legs census
cygpath write_atomic"`
