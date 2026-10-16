# TOOL-dRedressedBar-19 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-19

This is the build pass of the units-16-18 spec audit's minors batch, built from spec 19 rev-6.
`<w19>` is `3275f305a`, the spec-writer pass that corrected specs 12 and 14 to 18. `<p19>` is
`809f794e4`, the product commit. `495ec241a` is the same pass's follow-up, which gave two new arms
the liveness half the bug-class checklist's `fixture-passes-by-finding-nothing` class found
missing. `<p19m>` is `cafbbc460`, the manifest re-stamp. Unit 18 has no acceptance ledger, so
`<p18>` here is its pass commits, `6783992aa` and its follow-up `997fc294f`.

The product commit changes the gate profiler, `held_halves.load_manifest`, the census parser and
its arms, the fixtures, the run-gates descriptor, the registry, the leg's guard, the subject pin,
`WHOLE_RUN`, five `install.sums` writes and two comments in `tools/govkit/govkit.py`, and the
help page. `memory/map/generated/symbols.json` came from `gen_map.py --write`, run alone, and the
build index and `memory/LIVE.md` from `gen_build_index.py --write` over spec 19's dispatched
INPROGRESS header. The kickoff ratchet's staged check requires a re-stamp on a commit that stages
`tools/gate-legs.json`, so `<p19>` holds one at its parent and `<p19m>` re-stamps at `<p19>`.

No merge bar, no gate leg and no self-test suite was run by this pass, with two exceptions named
here. The naming lexicon ran, as this role may run it, and read 1087 offenders against its pin of
1087. And before the role's rule was re-read, one `python -c` called four process-monitor
self-test arms directly (`test_row_contract_is_complete`, `test_cim_memory_fields_are_bytes`, the
separator table and the non-UTF-8 arm), which is a slice of that suite: all four printed `ok`, and
the leg's own run is still owed to the close. `govkit selfcheck --write` was not run: the pin file
was written by hand and a probe compared it with the generator's header and sorted body.

Every other criterion was observed by a direct probe: an in-process python call, the profiler's
CLI over a fixture manifest under the session scratchpad with `TMPDIR` pointed there, or, for
AC40, a fresh `git init` target at `%TEMP%/d19w1`. No arm of `measure_legs.py --selftest` was
run. The section 7 gates are owed to the close, with the RED-first observation of all seven
`New arm:` lines. Where a red half was observed here it is named; every other red half is owed.

**Evidences:** TOOL-dRedressedBar-19
- AC1 — `manifest-audit:` — `git show 809f794e4 -- memory/guides/SESSION-KICKOFF.md` moves
  `last-audit:` from `4a4960958` to `bf05dbdd3`, `<p19>~1`, and `<p19>`'s body carries one
  `manifest-audit:` line. At `cafbbc460` the line names `809f794e4`, `last-body-change` moved there
  after a section B re-read, and the body carries one `manifest-audit:` line. `<p19>`'s
  `tools/gate-legs.json` holds the `measure-legs selftest` row with `{prefix}/run-gates/derive-ceilings.py`.
  Spec 18's section 7 cut carries `kickoff-manifest ratchet`. The pre-commit hook's staged ratchet
  passed both commits. The red half, the staged check refusing `<p19>`'s files with no re-stamp, is
  owed.
- AC10 — `census.OPTIONAL_FIELDS` — reads `("peak_mem_b", "mem_b")` and `census.FIELDS` the nine
  keys. Over a seven-field line whose command holds the separator, a five-field line and a
  seven-field line with both memory fields blank, `parse_cim` and `build_windows_rows` gave
  `(10240, 2048)` with the command rejoined, `(None, None)` with the command `C:/b.exe -y` intact,
  and `(None, None)` with its command, rejected 0. Every row's key set holds `FIELDS` and lies in
  `FIELDS` plus `OPTIONAL_FIELDS`. The module docstring carries `peak_mem_b`, `mem_b` and
  `int|None`, and `test_row_contract_is_complete`'s source carries `OPTIONAL_FIELDS`. Red over
  `<p18>` owed.
- AC11 — `/nonexistent` — `resolve_turnstile_dir` under `PATH=/nonexistent` returned `("", "")`, and
  `read_turnstile` over it raised `OSError`, `the turnstile key did not resolve`. Under this
  process's PATH it returned `('/c/Users/d41ly/.gov/gate-turnstile', 'C:/Users/d41ly/.gov/gate-turnstile')`.
  Red owed.
- AC12 — `GATE_REGEN_CHECK` — `build_holder_env({"GATE_REGEN_CHECK": "1", "GATE_JOBS": "3"})`
  returned `{'GATE_REGEN_CHECK': '0'}`. `read_hold_beacon` over a key no holder writes, with a
  child blocked on its stdin, returned None after 2.0 s with the child still running. With a child
  that printed `holder-said` and exited, it returned None after 0.0 s, and
  `render_holder_failure` over its capture carried `holder-said`. Red owed.
- AC19 — `load_manifest(` — `hasattr(measure_legs, "read_legs")` is False, the source of
  `read_profile_legs` carries `load_manifest(`, and `held_halves.load_manifest` has a `refuse`
  parameter. Spec 18's section 10 cut carries `held_halves.load_manifest` and
  `derive-ceilings.read_legs`. Red over `<p18>` owed.
- AC20 — `extract_runner_function` — took the runner's one-line `redact` and ran it in the resolved
  bash over `REDACT_SHAPES` on stdin: exit 0, the output byte-equal to `derive_redacted` over the
  same bytes, line by line, with 6 masks. Red observed: the port with `\s` dropped from both
  classes differs, on the tab shape.
- AC21 — `tools/run-gates/derive-ceilings.py` — the `measure-legs selftest` guard, `{prefix}` read
  as `tools`, holds it, `tools/run-gates/held_halves.py`, `.githooks/pre-push` and
  `tools/run-gates/kit.toml`, each exact and each carried by one leg against `BROAD_LEG_FLOOR` 5.
  `check_guard_trips` returns True for the derive-ceilings path against the guard. Red owed.
- AC25 — `WHOLE_RUN=(` — `grep -c` of the row prints 1, inside the array, after
  `held-halves selftest`. Red over `<p18>` owed.
- AC27 — `derive_guarded_legs` — spec 18's backticked Files touched paths joined against every
  guarded leg found 7 legs, none unnamed on its section 7, which names `measure-legs selftest`.
  Red over `<p18>`'s spec owed.
- AC29 — `project-owned` — run from `tools/govkit`, the run-gates descriptor through
  `govkit.resolve_descriptor_paths(<desc>, "tools")`: its `project-owned` list elements under
  `fixtures/measure-legs/`, prefixed, equal the 13 paths `git ls-files` prints, no element carries
  a glob, and `govkit.resolve_rule_pool` over the `**` rule holds 0 fixtures of a 16-path pool. No
  `[[gate_leg]]` is named `measure-legs selftest`; the registry's `[[exempt_leg]]` `why` carries
  `process-monitor` and `Windows`; `tools/gate-legs.json`, `selftest-budgets.txt` and
  `windows-only-legs.txt` name the leg; its guard holds `{prefix}/run-gates/kit.toml`. Red
  observed: with the rule respelled `["fixtures/measure-legs/**"]` all 13 fixtures sit in a
  29-path pool. The red over `<p18>` is owed.
- AC34 — `test_no_bare_bash_argv` — its scan over `measure_legs.py` read 8 subprocess calls and no
  argv opening with `'bash'`. With `measure_legs.profile_bar.resolve_bash` rebound to return
  `("", ["cand-a", "cand-b"])`, `main` over `serial.json` returned 2, the out dir stayed empty, and
  stderr read `no bash could open the runner. Tried: cand-a, cand-b`. Red observed: the scan over
  the source with one `subprocess.run(["bash", ...])` appended found it.
- AC35 — `measure_legs.build_job` — rebound to close its third job, under a scratch-dir probe over a
  `spawn.py 0 1` manifest: `main` returned 0 in 2.7 s, the `.leg` row read `launch fail 1`, the
  record's `launch_error` read `launch: AssignProcessToJobObject 6`, and a fresh census held no row
  with the root's winpid, captured from the `CREATE_SUSPENDED` launch. Red observed with
  `Popen.terminate` a no-op: the root's winpid stayed in the census, and the run returned after
  32.7 s, its bounded 30 s wait, rather than staying open at the spec's 60 s bound. The suspended
  root was then removed by hand.
- AC36 — `gate-bar-beacon/` — with no `pid`, `gate-bar-beacon.1/` reading `x` and a ticket
  `20261015T000000-nopid-x`, `read_turnstile` returned no refusal, no holder and no ticket. A key
  whose `gate-bar-queue` is a file raised `NotADirectoryError`. The liveness key, one whole beacon
  at pid 4242 and one ticket at pid 4243, read both. Red owed.
- AC37 — `{nope}/x` — each of `MANIFEST_CLASSES`' eight manifests, run by the CLI, exited 2 with one
  `measure-legs: REFUSED — ` stderr line and no `Traceback`, the out dir empty, and the five row
  classes' lines carry `row `: row 0 for the non-object row, the number argv, the tab name and the
  unresolved token, row 1 for the duplicate. Red over `<p18>` owed.
- AC38 — `owner.json` — a probe planted, under a `TMPDIR` of its own, a dead scratch owned by an
  exited child with its creation time and a record dir that exists, holding
  `https://u:s3cret@example.invalid/`, and a live scratch owned by the probe holding `live-bytes`.
  One CLI run over `serial.json` exited 0. The dead raw file is gone, the record dir's
  `0.log.recovered` reads `https://***:***@example.invalid/`, `s3cret` occurs nowhere under the out
  dir or the dead scratch, the live raw file still reads `live-bytes`, and the envelope's
  `raw_recovered` names the dead capture alone. `help/measure-legs.md` carries `raw_recovered` and
  `launch_error`. Red owed.
- AC39 — `0xe7` — `derive_redacted(b"a\xe7\r\nhttps://u:s3cret@h\x00z")` returned the masked bytes
  with the `0xe7`, the CR and the NUL kept. A CLI run of `serial.json`'s six legs exited 0, and the
  printenv leg's log holds the byte, a CR, `://***:***@` twice and no `s3cret`. Red owed.
- AC40 — `install.sums.govkit-new` — `govkit.ADOPTER_BAR_PATHS` holds `'"install.sums"'` and
  `receipt_path`, and the direct-write grep prints 0. Over `%TEMP%/d19w1`, after a first
  `apply --target <t> --kits check-wiring`, a second with `pathlib.Path.write_text` writing half and
  raising on `install.sums.govkit-new` raised that `OSError`; the sidecar and the receipt each equal
  their earlier bytes and no sibling is left. `check --target` printed no sidecar mismatch line and
  `sidecar: 3 line(s) compared against 3 hashed row(s)`. Spec 14's "When CONFIGURE fails" cut
  carries `install.sums`. The `[-21] AC2` routing walk, copied into a probe, found 0 direct writes
  and 13 routed, five of them the sidecar. Red observed for the member: the same walk over HEAD's
  engine with `'"install.sums"'` declared found the five plain sidecar writes. The fault red over
  `<p18>` is owed.
- AC41 — `[dRB-14]` — an `ast` read of govkit's self-test found 6 `check` calls labelled
  `[dRB-14]`, none carrying `kit 'agent-cap'`, and a `[dRB-15]` check asserting no line opens
  `govkit: kit '`. Spec 17's AC1 carries `label` and no `first to the last line carrying`. Red owed.
- AC2 — `note template` — `slash-bearing` counts 0 in `govkit.py` and specs 15 and 17,
  `argv element(s) offered by` counts 1 in `govkit.py`, and spec 17 carries `note template`. Red
  owed.
- AC4 — `build-order` — `above every unit` counts 0 in spec 17, and its section 1 cut carries it.
- AC5 — `:7424` — spec 17's AC9 cut carries each of the six sites and the awk line's six numbers.
- AC6 — `existing leg's argv, guard or ceiling` — spec 18's section 3 carries it, and the old
  non-goal counts 0.
- AC7 — `--concurrent` — one `## ` section of `tools/run-gates/README.md` carries it and
  `measure_legs.py`; the map feature carries the file and the leg; spec 18's S13 carries
  `TOOL-dRedressedBar-19`.
- AC8 — `TOOL-dRedressedBar-12` — `write_gate_legs`' docstring carries it and
  `TOOL-dRedressedBar-16`, and so do spec 16's S2 and AC3.
- AC31 — `superseded by TOOL-dRedressedBar-16` — spec 12's section 2 cut carries it, and spec 16's
  S4 carries `inline note`.
- AC9 — `grep -c 'selftest.py:15412' <s16>` — prints 0, and the `15428-15459` count prints 1.
- AC13 — `floor` — spec 18's section 7 cut carries it and the kit epoch leg's full name.
- AC14 — `@0.15` — the shipped-file grep over `tools/process-monitor` without suites prints one
  marker, `process-monitor@0.19`, and spec 18's revision log names report id 14 and AC14.
- AC15 — `run-gates.sh:3877` — spec 18's S11 carries it and `$WORK/$i$sfx.raw`, and no
  `run-gates.sh:3916`.
- AC16 — `grep -c 'kit.toml:104' <s17>` — prints 3, and the `kit.toml:103` count prints 0.
- AC17 — `grep -c 'six writes' <s17>` — prints 0.
- AC18 — `:11898-11903` — spec 16 carries it and `:11888-11890`, and `:11880-11891` counts 0.
- AC22 — `grep -c -P '^measure-legs selftest\tkit\tselftests$' tools/govkit/subject-pins.tsv` —
  prints 1. A probe found the file equal to the generator's header plus every manifest leg sorted,
  which also moved `branch-reconcile selftest` and `cleanup skill wiring` into sorted order. The
  selfcheck run is owed.
- AC23 — `THE DECLARED ADOPTER-BAR DESTINATION SET` — the lines from it to `ADOPTER_BAR_PATHS =`
  carry `receipt` and `install.sums`, `write_atomic`'s docstring carries both, and spec 17's AC23
  carries `docstring`. Red over `<p18>` owed.
- AC30 — `derive_parity_lines` — spec 16's "What an adopter sees change" cut carries it.
- AC32 — `procs_total` — a CLI run over `serial.json` at `--census-every 1` ran `forks five` at 17
  processes and `forks none` at 2, read from `legs.tsv`, a difference of 15. Red owed.
- AC42 — `stall.json` — a CLI run at `--stall-window 8 --stall-cpu 0.5` printed one STALLED line,
  opening with the leg `stall`, and none for `steady` or `churn`. Red owed.
- AC43 — `orphan` — spec 16's section 3 carries it, and its section 4 no longer carries
  `so the carried row names a claimed kit`.
- AC44 — `TOOL-dRedressedBar-19` — `<w19>` gives specs 12, 14, 15, 16, 17 and 18 one header rev
  change each, 7 to 8, 6 to 7, 5 to 6, 3 to 4, 4 to 5 and 4 to 5, and one new revision line each
  naming the unit and every report id the table assigns it; all six were CLOSED at `<w19>~1`.
  Under the spec folder `<p19>` changed this spec alone, its dispatched status cell, and
  `495ec241a` and `<p19m>` none. This record carries the binding line above.

## Owed to the close

Every section 7 gate, and the RED-first observation of each `New arm:` line, after the last unit
is terminal. Two readings the main loop should hold beside them. AC35's red half reads the root
alive in the census, and the run returns after its bounded wait rather than staying open at 60 s.
And the run-gates kit README's profiler section, which unit 18 wrote, still says nothing is ever
signalled, which S35's one terminate now narrows. That file is outside this unit's write set, so
it is named here and not changed.
