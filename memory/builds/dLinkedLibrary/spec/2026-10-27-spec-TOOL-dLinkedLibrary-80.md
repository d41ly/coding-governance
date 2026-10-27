# TOOL-dLinkedLibrary-80 — the spec audit of units 65 to 74: its medium and low findings, batched

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 32 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-80-deviation-801.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-80-deviation-801.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-79 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 65 to 74
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`) confirmed
24 MEDIUM and 6 LOW findings. BUILD-METHOD M4 promotes them into one batch unit, and this is it; each
finding is its own scope item below, by report id:

- MEDIUM: 1, 11 and 27 (item M1), 2 (M2), 12 and 41 (M3), 10 and 26 (M4), 28 (M5), 40 (M6), 22 (M7), 21
  (M8), 43 (M9), 42 (M10), 4 (M11), 15 and 37 (M12), 20 (M13), 14 and 38 (M14), 13 (M15), 23 (M16), 24
  (M17), 39 (M18).
- LOW: 6 (L1), 7 and 17 (L2), 8 (L3), 3 (L4), 16 (L5).

Two items are the lower-grade half of a defect the report also binds higher: M3 is H1's, closed by
`TOOL-dLinkedLibrary-75`, and L1 is M15's, both here. Each such item builds only what its higher-grade
half leaves. The findings land on nine units, so this unit repairs none in particular and builds after
every unit of the build (order 32). One unit and not two: S7 re-renders the generated map, which every
item that adds a function moves, so no split by M6's clause 1 leaves two disjoint write sets.

## 2. Scope (IN)

- **S1** — id 1, M1. The site population of `TOOL-dLinkedLibrary-74` S16 is `git grep -l '^# >>>
  region_py' -- tools skills`, a code pathspec, never the whole repository. Observed by AC1.
- **S2** — id 11, M1. A spec or record that quotes the opener at column 0 is not a site: `memory/` is
  outside S1's pathspec, so `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-18.md`,
  which quotes it at :161, is never listed. Observed by AC1.
- **S3** — id 27, M1. Every file S1 lists carries a `splice_region` that raises on a body line `<open>x`,
  as `TOOL-dLinkedLibrary-64` S13 states; a copy that lacks it gains it at this pass, and no population is
  narrowed by hand. Observed by AC1.
- **S4** — id 2, M2. Each version constant 74 S16 names, with the memory-tree, codebase-map and govkit
  constants 64 names, is compared between 74's pass start, the first parent of the earliest commit whose
  subject opens `build(dLinkedLibrary): TOOL-dLinkedLibrary-74 `, and 74's last pass commit, never with the
  build base 5fede642. A kit whose `region_py` copy changed in that range at an unmoved value is moved at
  this pass. Observed by AC2.
- **S5** — id 12, M3. After every unit that writes a reuse tag, units 19, 60, 74 and 75, unit 75's predicate
  re-run at this pass's tip over `tools` and `memory/map` prints nothing; a tag it prints is rewritten as
  75 S2 states. Observed by AC3.
- **S6** — id 41, M3. The predicate's red is shown at this pass too, not assumed from 75's: over a scratch
  plant it prints `unit.reuse.run-gates-2` and not `unit.reuse.run-gates.2`. Observed by AC3.
- **S7** — id 10, M4. The map is re-rendered at this pass's tip with `python
  tools/codebase-map/gen_map.py --write`, and `--check`, the read-only compare the kit's `[[regenerate]]`
  row declares (`tools/codebase-map/kit.toml:155`), exits 0 after it. Observed by AC4.
- **S8** — id 26, M4. The four artifacts `--write` renders (`tools/codebase-map/gen_map.py:143-151`) are in
  this unit's Files touched and are committed together. Observed by AC4.
- **S9** — id 28, M5. For each kit whose constant 74 S16 moves, and govkit (`KIT_GOVKIT_VERSION`,
  `tools/govkit/govkit.py:47`), every `gov:kit <kit>@` marker under `tools` and `help` carries the
  constant's value, the carriers `tools/check-kit-versions.sh` pairs with it (:342-363, :393-396)
  included; a carrier left behind moves at this pass. Observed by AC5.
- **S10** — id 40, M6. `FLOOR_ASSERTIONS` in the micro-format suite and in the run-gates canary rises by
  the assertions 74's arms add to each, the figure derived at this pass from 74's commits. Observed by
  AC6.
- **S11** — id 22, M7. The inline-parity loop (`tools/lib/resolve-python.test.sh:221-241`) gains a free-name
  arm: for every `*.py` file holding a block of a parity row, the canonical included, it reads each block
  with Python's `symtable` and red on any name the block references at global scope that neither the
  block binds, the host binds at module level, nor `builtins` holds, naming the row, file and name. A host
  with a star import is red, named, never passed. The gotchas-only `tree-kill-names-bound` case of 74 S10
  stays as the observed instance. Observed by AC7.
- **S12** — id 21, M8. The `observe-tree-hang` case reads Windows visibility by `read_pid_image`'s measured
  rule (`tools/unattended/lib-unattended.sh:595-614`): `tasklist /FI "PID eq <pid>" /NH` is parsed for a row
  whose pid field equals the pid, its exit code ignored, and the image, every field before the pid, must
  equal the basename of `sys.executable`; on POSIX `os.kill(pid, 0)` decides and the image is the first
  element of `/proc/<pid>/cmdline`. Another image fails `harness: grandchild not visible to the observer`.
  Observed by AC8.
- **S13** — id 43, M9. Identity and the pidfile wait. The grandchild writes `<pid> <nonce>`, the nonce
  minted per case run with `secrets.token_hex(8)` and also on its own argv. Before the bounded `--observe`
  run, the case starts the same planted argv through `resolve_observed_argv` itself, unbounded, polls its
  pidfile every 50 ms up to 1.0 s, failing `harness: grandchild never started` after; it confirms the live
  pid's command line carries the nonce, read on Windows with `powershell -NoProfile -NonInteractive -Command
  "(Get-CimInstance Win32_Process -Filter 'ProcessId=<pid>').CommandLine"` and on POSIX from
  `/proc/<pid>/cmdline`; then it ends that tree with `run_tree_kill` and reads the pid gone by S12's rule.
  The bounded run polls its own pidfile under the same deadline. Observed by AC9.
- **S14** — id 42, M10. `reuse_entries.py propose`'s duplicate refusal (74 S14) matches the part as a whole
  token, `(?<![\w.-])<feature>\.<n>(?![\w])`, so `codebase-map.1` never matches a live
  `codebase-map.12`; the `refile-later-date` plant gains that tip. Observed by AC10.
- **S15** — id 4, M11. S7's render covers `resolve_observed_argv`, the module-level function
  `TOOL-dLinkedLibrary-67` adds to `tools/memory-tree/gotchas.py`, which 74 S23's render does not credit.
  Observed by AC11.
- **S16** — id 15, M12. `resolve_observed_argv` calls `corpus_ids.resolve_bash` only when an argv head is
  `bash`, and catches any exception from the loaded module with `except Exception`, as `append_only_re`
  does (`tools/memory-tree/gotchas.py:155-159`), recording `TOOL-dLinkedLibrary-49`'s cannot-start reading
  with the exception's class and text. Observed by AC12.
- **S17** — id 37, M12. A `--selftest` case `observe-no-bash` sets `GOV_BASH` to a path that does not
  exist, as the boundary case at :1000-1009 does, and asserts the cannot-start reading naming `GOV_BASH`
  and no `Traceback` line. Observed by AC12.
- **S18** — id 20, M13. The docstring of `resolve_observed_argv` names `govkit.resolve_shell_argv`
  (`tools/govkit/govkit.py:1200`) as the contract it mirrors and says why its fallback differs: a run under
  another filesystem observes another tree, so it records cannot-start where govkit returns the argv
  unchanged. It names `resolve_bash_py` (`tools/lib/resolve_bash.py`) and the open ask
  `TOOL-dSettledRoster-6`, whose convergence owns the probe this caller takes. Observed by AC13.
- **S19** — id 14, M14. `read_map_cli` (`TOOL-dLinkedLibrary-69` S1) strips no BOM: the text is decoded as
  `utf-8`, never `utf-8-sig`, and line 1 reaches `parse_conf_assignment` with its BOM, so a BOM-led
  first-line assignment assigns nothing, as bash assigns nothing. Observed by AC14.
- **S20** — id 38, M14. Every input variant of 69 AC1 is compared with bash's output on the same bytes: a
  BOM before a first-line assignment reads `None` where bash leaves `MAP_CLI` unset, and a BOM before a
  comment leaves later lines read. The CRLF parity is recorded as measured on node d's bash 5.3.9
  (x86_64-pc-cygwin), which reads each line without its CR, and claimed for no other bash. Observed by AC14.
- **S21** — id 13, M15. The stripped-block arm of `TOOL-dLinkedLibrary-66` asserts exit 2 together with a
  line holding `region: command not found` or 65's `region_sh block is absent`, accepting either, and
  never the bare substring `region`, which the source line's own `lib/region.sh: No such file or
  directory` line always holds. Observed by AC15.
- **S22** — id 23, M16. 55 S2's inserted-line copy is gone from the micro-format suite: its one non-comment
  line spelling `lib/region.sh` is 66 S1's strip step. Observed by AC16.
- **S23** — id 24, M17. `decision_rubric.py --selftest` gains a case `no-local-row-predicate` that reads the
  module's own source with `ast` and fails naming any `re.compile` argument whose pattern holds `·`,
  `\*\*`, `[-*]` or `DECISIONS`, so a row or archive predicate beside the row grammar's is red. Observed by
  AC17.
- **S24** — id 39, M18. The `log-diff` plant writes a `.memory-tree.conf` whose `FAMILIES` names the
  planted id's family; `derive_log_departures`' call into `row_grammar` catches any exception crossing the
  module boundary, `FileNotFoundError` for an absent conf (`tools/memory-tree/row_grammar.py:111-113`,
  :141-155) and row_grammar's own `Problem` for an empty `FAMILIES` (:176-179) included, and `log-diff`
  exits 2 naming `.memory-tree.conf`; the plant gains a `no-conf` tip. Observed by AC18.
- **S25** — id 6, L1. The arm's comment says what it observes: the exit code together with a line only an
  absent reader prints, the source line's error excluded, so the claim and the check agree. Observed by
  AC19.
- **S26** — id 7, L2. 74 S4's header line sits at column 0 as a comment holding "gov library directory";
  absent, it is written at this pass. Observed by AC20.
- **S27** — id 17, L2. That header is read anchored, `^#`, so 65's guard echo, indented inside the guard,
  never stands in for it. Observed by AC20.
- **S28** — id 8, L3. 74 S21's pointer is read on a comment line of `tools/run-gates/kit.toml`, not the
  `include` row at :40, and 74 S24's bounded kill is re-observed with a staged red, a scratch copy of
  `tools/run-gates/regen.py` that calls `proc.kill()` where the `run_tree_kill` call stood. Observed by AC21 and
  AC22.
- **S29** — id 3, L4. `TOOL-dLinkedLibrary-64` S6 re-observes 67's resolver and lands none of its own: at
  this pass `tools/memory-tree/gotchas.py` holds exactly one call of `resolve_bash`, inside
  `resolve_observed_argv`. Observed by AC23.
- **S30** — id 16, L5. `help/adopt.md` names each key `TOOL-dLinkedLibrary-71` refuses (`!reference`, the
  merge key `<<`, an alias, a top-level `include:`) and each template level `TOOL-dLinkedLibrary-72`
  refuses (a stage template, a job template, a top-level `extends:` template); a missing one is written at
  this pass. Observed by AC24.

## 3. Non-goals (OUT)

- The HIGH findings of the same audit: units 75 to 79, one per id.
- Re-opening any unit's design: each item corrects the built code or a criterion's observation, or records
  where the finding lands.
- A gate per left-shift the report proposes: every item lands on an existing arm, plant, docstring or
  record, the free-name arm of S11 excepted, which is M7's own fix.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-74` — S16's copies and constants, S7 and S8's pidfile checks, S14's duplicate refusal, S4's header, S21's pointer, S23's render and S24's re-observation, which S1 to S4, S7 to S10, S12 to S15 and S26 to S28 complete (ids 1, 11, 27, 2, 10, 26, 28, 40, 21, 43, 42, 4, 7, 17, 8)
- **consumes-from** `TOOL-dLinkedLibrary-75` — the hyphen-admitting predicate and its scratch plant, which S5 and S6 re-run at this tip (ids 12, 41)
- **consumes-from** `TOOL-dLinkedLibrary-66` — the stripped-block arm, its assertion and its comment, which S21, S22 and S25 correct (ids 13, 23, 6)
- **consumes-from** `TOOL-dLinkedLibrary-67` — `resolve_observed_argv` and the `observe-tree-hang` plant, which S13, S16 to S18 and S29 complete (ids 43, 15, 37, 20, 3)
- **consumes-from** `TOOL-dLinkedLibrary-68` — the row-grammar read of `derive_log_departures` and the `log-diff` plant, which S23 and S24 complete (ids 24, 39)
- **consumes-from** `TOOL-dLinkedLibrary-69` — `read_map_cli` and AC1's variants, which S19 and S20 correct (ids 14, 38)
- **consumes-from** `TOOL-dLinkedLibrary-71` — S5's page paragraph, which S30 completes (id 16)
- **consumes-from** `TOOL-dLinkedLibrary-72` — S5's page paragraph, which S30 completes (id 16)
- **consumes-from** `TOOL-dLinkedLibrary-64` — S6's `--observe` resolution, which S29 holds to 67's one resolver (id 3)
- **hands-off** `TOOL-dLinkedLibrary-86` — S1, S4, S9 to S12, S23, S28 and S30 with their criteria, and §10's recall line, which unit 86 corrects (ids 2, 16, 22, 40, 3, 4, 18, 6, 12, 14, 15, 39, 26, 27, 10, 28, 41, 23, 11 of the spec audit of units 75 to 80)

## 4. Design

### Evidence

- S1 to S3: at base `git grep -n '^# >>> region_py'` lists only the spec record of unit 18, at :161
  inside a code fence; `git grep -n '^# >>> region_py' -- tools skills` lists nothing, because unit 18
  inserts the copies.
- S4: unit 18 S9 (order 2), unit 52 (order 27) and unit 64 (order 29) move the same constants, so by order
  30 every one differs from 5fede642 whatever 74 does.
- S7, S8: `gen_map.py:213` makes the mode group required, so a bare `gen_map.py` exits 2 and renders
  nothing; `--write` renders `inventories.json`, `MAP.md`, `CARDS.md` and `symbols.json` (:143-151).
- S9: `git grep -l` of the roles, drift-audit, runlog, playbook-render and govkit markers over `tools help`
  lists 25 files at base (PINNED, 2026-10-27), Files touched below.
- S10: the micro-format suite counts one assertion per `say_ok` or `say_fail` call and holds
  `FLOOR_ASSERTIONS=20` (:142); the canary counts `n=$((n+1))` lines and holds `FLOOR_ASSERTIONS=405`
  (:146), both at base.
- S11: the parity rows at `tools/lib/resolve-python.test.sh:168-186` hold `resolve_bash_py`,
  `health_log_py`, `compare_base_py`, `remote_ladder_py` and `git_env_leaks_py` among their Python rows,
  and the loop at :221-241 compares bytes only.
- S12: `read_pid_image` records that `tasklist` exits 0 for a live pid and a dead one alike; a probe on
  2026-10-27 printed `INFO: No tasks are running` for pid 999999 at exit 0.
- S13: the command-line query took 0.89 to 1.35 s per call on node d (PINNED, three runs, 2026-10-27),
  most of 61's 2 s bound, which is why it runs on an unbounded twin and not inside the bounded run.
- S16, S17: `corpus_ids.py:142` and `gotchas.py:101` each define `Problem`; `resolve_bash` raises the
  former (:416, :433), and `gotchas.py:140-141` records that `except Problem` cannot catch it.
- S19, S20: on node d, bash 5.3.9 sourcing `\xef\xbb\xbfMAP_CLI="tools/x.py"` left `MAP_CLI` unset; with a
  BOM before a comment line it assigned the second line; with CRLF it assigned without the CR.
- S21, S25: 66 S3 credits the substring to bash's command-not-found line and 65's refusal and misses the
  source line's own error, which the audit reproduced at rc 2.
- S22: `grep -c 'lib/region.sh'` over the micro-format suite prints 0 at base.
- S28: `tools/run-gates/kit.toml:40` is the non-comment `include` row naming the canary; the comment above
  it (:35-38) is where 74 S21 writes the pointer.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`, `tools/playbook/render_playbook.py`, `tools/roles/check_roles.py`,
  `tools/roles/roles_lib.py`, `tools/runlog/prose.py`, `tools/runlog/runlog_lib.py`,
  `tools/drift-audit/drift_report.py`, `tools/codebase-map/map_lib.py`, `tools/govkit/selftest.py`,
  `tools/govkit/govkit.py`: S3, S4, S9
- `tools/roles/README.md`, `tools/roles/SKILL.template.md`, `tools/runlog/README.md`,
  `tools/runlog/adopt-runlog.sh`, `tools/runlog/extract.py`, `tools/runlog/model.py`,
  `tools/runlog/record.py`, `tools/runlog/runlog.py`, `tools/runlog/selftest.py`,
  `tools/drift-audit/README.md`, `tools/drift-audit/adopt-drift-audit.sh`,
  `tools/drift-audit/drift_signals.py`, `tools/drift-audit/drift_signals.template.py`,
  `tools/drift-audit/selftest.py`, `tools/drift-audit/kit.toml`, `tools/workflows/drift-audit-code.js`,
  `tools/workflows/drift-audit-code.template.js`, `tools/workflows/drift-audit-state.js`,
  `tools/workflows/drift-audit-state.template.js`: S9
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: S7, S8, S15
- `memory/map/features/`: S5, a tag the predicate prints
- `tools/check-microformats.test.sh`: S10, S21, S22, S25
- `tools/run-gates/run-gates.test.sh`: S10
- `tools/lib/resolve-python.test.sh`: S11
- `tools/memory-tree/gotchas.py`: S12, S13, S16, S17, S18
- `tools/memory-tree/reuse_entries.py`: S14
- `tools/govkit/steps/retire_reuse_lookup.py`: S19, S20
- `tools/memory-tree/decision_rubric.py`: S23, S24
- `tools/check-microformats.sh`: S26
- `help/adopt.md`: S30

### Alternatives rejected

- **One unit per finding.** M4 forbids it.
- **Folding each item into its unit's spec.** The owner's 2026-10-05 ruling promotes every minor and folds
  none.
- **S13's identity check inside the bounded run.** The query costs most of the bound, so a slow start
  reads a killed grandchild as invisible; the twin removes the race and the bounded run keeps 61's 2 s.
- **S19 by refusing a BOM-led conf with exit 1.** 69 exists to read `MAP_CLI` the way bash reads it; a
  refusal is a third reading neither bash nor the kit gives.
- **S11 by a gotchas-only case.** It guards one block in one host; the class is every Python copy of every
  row.

## 5. Production-readiness checklist

- security — S12 and S13 stop a foreign process certifying a kill; S14 stops a false refusal of a
  legitimate proposal; S30 documents the census's refusals.
- perf / scale — S13 adds one unbounded twin run of about a second to the gotchas selftest; S11 adds one
  `symtable` read per Python copy.
- error / empty / loading states — S13, S16, S17 and S24 each fail naming the cause, never with a
  traceback.
- observability — each refusal names its file, row, key, pid or variable.
- risks — S11 can red a host that binds a name dynamically; such a host is named, and the fix is an
  explicit binding.
- testing — AC1 to AC24 by fixture, selftest case, plant, scratch copy and probe.
- migration — S4 and S9's version moves and S5's tag rewrite, each in its own commit.
- user docs — `help/adopt.md`, S30.

## 6. Acceptance criteria

- **AC1** — When `git grep -l '^# >>> region_py' -- tools skills` runs at this pass's tip, it lists no file
  under `memory/`, and each file's `region_py` block, sliced between its markers and run alone under
  `python -I`, defines a `splice_region` that raises on a body line `<open>x`.
  Red when: a record joins the site population, or a listed copy keeps the old body.
- **AC2** — When `git show` reads each constant S4 names at 74's pass start and at 74's last pass commit,
  every kit whose `region_py` copy changed between them has a moved value at this pass's tip.
  Red when: a kit ships a changed copy at the version it had when 74 began.
  figure: DERIVED at the pass from 74's commits.
- **AC3** — When unit 75's predicate `git grep -nE 'unit\.reuse\.[A-Za-z0-9_-]+-[0-9]+([^0-9A-Za-z_]|$)'
  -- tools memory/map` runs at this pass's tip it prints nothing, and in a scratch repository under
  `%TEMP%/rt80` holding `unit.reuse.run-gates-2` and `unit.reuse.run-gates.2` it prints the first line
  only.
  Red when: a hyphenated tag survives a later unit, or the predicate is green on its planted case.
- **AC4** — When `python tools/codebase-map/gen_map.py --check` runs at this pass's tip it exits 0; in a
  scratch clone under `%TEMP%/gm80` with one module-level function added to `gotchas.py` it exits 1.
  Red when: the committed render is stale, or the command cannot fail.
- **AC5** — When `git grep -h -o -E 'gov:kit <kit>@[0-9][0-9.]*[0-9]' -- tools help` runs for each of
  `roles`, `playbook-render`, `runlog`, `drift-audit` and `govkit`, each prints one distinct marker,
  equal to that kit's constant.
  Red when: a carrier keeps the old marker beside a moved constant.
- **AC6** — When `grep -n '^FLOOR_ASSERTIONS='` runs over the micro-format suite and the run-gates canary
  (their paths in Files touched), each prints its value at 74's pass start plus the assertions 74's arms
  add to it.
  Red when: a suite's floor stays below the arms it runs, so deleting one leaves it green.
  figure: DERIVED at the pass, the canary's from the `n=$((n+1))` lines 74's commits add, the micro-format
  suite's from the `say_ok` or `say_fail` assertions 74's arms add.
- **AC7** — When the free-name read S11 adds is run by hand with `python -I` over every `*.py` file holding
  a parity row's block, it names no unbound name; over a scratch copy of `gotchas.py` with its `import
  signal` deleted, it names `signal` and the `tree_kill_py` row.
  Red when: a block's free name is unbound in any Python host.
- **AC8** — When `python tools/memory-tree/gotchas.py --selftest` runs `observe-tree-hang` with its pidfile
  rewritten to hold the pid of a live process of another image the case starts, `ping` on Windows and
  `sleep` on POSIX, it fails as `grandchild not visible`; with a pid no process holds it fails the same
  way.
  Red when: `tasklist`'s exit code, or a pid number alone, reads a process as the grandchild.
- **AC9** — When the same selftest runs the case with the twin's pidfile rewritten to hold the observer's
  own pid and the run's nonce, it fails as `grandchild not visible`; with the plant writing no pidfile it
  fails as `grandchild never started` within 1.5 s; unmodified it prints `ok`.
  Red when: a live process lacking the nonce, or a late pidfile, decides the kill's verdict.
  cost: about a second for the twin's command-line query.
- **AC10** — When `python reuse_entries.py --fixture --plant refile-later-date` runs, the tip proposing
  `alpha.1` while `alpha.12` is live writes its proposal and exits 0, and re-filing `alpha.1` while it is
  live exits 2 naming the record.
  Red when: a part whose name prefixes a live part's is refused.
- **AC11** — When `python -I -c` loads `memory/map/generated/symbols.json` at this pass's tip, it finds an
  entry for `resolve_observed_argv` in `tools/memory-tree/gotchas.py`.
  Red when: the render predates the function unit 67 adds.
- **AC12** — When `python tools/memory-tree/gotchas.py --selftest` runs `observe-no-bash`, it prints `ok`,
  having read the cannot-start reading naming `GOV_BASH` and no `Traceback` line; with the catch narrowed
  to `except Problem` in a scratch copy, the case fails on the traceback.
  Red when: the sibling module's exception escapes the observer.
- **AC13** — When `grep -n "resolve_shell_argv\|resolve_bash_py\|TOOL-dSettledRoster-6"` runs over
  `tools/memory-tree/gotchas.py` at this pass's tip, it prints the docstring lines of
  `resolve_observed_argv` naming all three.
  Red when: the third resolver ships with no record of the two it mirrors or the ask that owns them.
- **AC14** — When `python -I -c` loads `retire_reuse_lookup.py` by its path and calls `read_map_cli` on a
  BOM before `MAP_CLI="x.py"`, on a BOM before a comment line and that assignment, and on the
  assignment with CRLF, it returns `None`, `x.py` and `x.py`, and `bash -c '. <file>; printf
  %s "${MAP_CLI-UNSET}"'` prints `UNSET`, `x.py` and `x.py` for the same bytes under
  `%TEMP%/rl80`.
  Red when: a BOM-led first-line assignment reads as assigned, or any result differs from bash's.
- **AC15** — When the stripped-block arm's assertion is reproduced by hand in a scratch repository under
  `%TEMP%/mf80`, the stripped copy at a lib-less prefix satisfies it; a copy with `region() { exit 2; }`
  written after its source line exits 2 and fails it.
  Red when: the assertion holds on an exit 2 no absent reader caused.
- **AC16** — When `grep -v '^[[:space:]]*#'` over the micro-format suite (its path in Files touched) is
  piped to `grep -c 'lib/region.sh'`, it prints 1.
  Red when: 55 S2's inserted-line copy survives beside the strip step.
- **AC17** — When `python decision_rubric.py --selftest` runs, `no-local-row-predicate` prints `ok`; over
  a scratch copy holding `re.compile(r"^- (\S+) · ")` it names that pattern.
  Red when: the module keeps a row or archive predicate of its own.
- **AC18** — When `python decision_rubric.py --fixture --plant log-diff` runs, the `no-conf` tip exits 2
  naming `.memory-tree.conf` with no `Traceback` line, and the conf-carrying tips read as 59 and 68 state.
  Red when: an absent conf or an empty `FAMILIES` prints a traceback or reads a row as a departure.
- **AC19** — When the AC15 reproduction is re-run with the source line's error discarded, `2>/dev/null` on
  the `.` line, the stripped copy still satisfies the assertion, and the arm's comment, read with `grep -n
  'No such file'` over the suite, names the line it excludes.
  Red when: the assertion leans on the source line's own error.
- **AC20** — When `grep -n '^#.*gov library directory' tools/check-microformats.sh` runs, it prints
  exactly one line, the header, while the unanchored `grep -c 'gov library directory'` prints 2.
  Red when: the header is missing and 65's echo stands in for it.
- **AC21** — When `grep -n '^#.*run-gates[.]test[.]sh' tools/run-gates/kit.toml` runs at this pass's tip,
  it prints one comment line, 74 S21's pointer.
  Red when: only the `include` row names the canary.
- **AC22** — When `python -I -c` loads a scratch copy of `tools/run-gates/regen.py` and calls
  `run_command(["bash", "-c", "sleep 5 & wait"], root, 1)`, it returns `TIMEOUT` within 3 seconds; with the
  copy's `run_tree_kill` call replaced by `proc.kill()`, the same call takes 4 seconds or more.
  Red when: the kill no longer reaches the grandchild holding the pipe.
  cost: about 8 seconds for the two runs.
- **AC23** — When `python -I -c` parses `tools/memory-tree/gotchas.py` with `ast` and counts calls whose
  callee is named `resolve_bash`, it prints 1, and the call sits inside `resolve_observed_argv`.
  Red when: unit 64's pass lands a second resolution beside 67's.
- **AC24** — When `grep -c` runs over the help page `adopt.md` (its path in Files touched) for each of
  `!reference`, `merge key`, `top-level .include:.`, `stage template`, `job template` and `extends:.
  template`, each prints at least 1 at this pass's tip, and 0 over the page as unit 63's pass leaves it,
  read with `git show`.
  Red when: a token 63's page already holds stands in for 71's or 72's paragraph.

## 7. Gates

`micro-format gate selftest` · `gotchas selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary` · `policy fixtures` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `roles catalogue` · `roles render selftest` · `runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `drift-audit selftest` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `kit version markers` · `build-index selftest` · `row-grammar selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC7 · the free-name read over every Python copy of every parity row, the failing case staged by deleting `import signal` from a copy of gotchas.py · none
New arm: tools/memory-tree/gotchas.py · covers AC8 AC9 AC12 · the image, identity-twin, pidfile-deadline and `observe-no-bash` cases, the failing case staged by a foreign pid in the pidfile and an `except Problem` around the corpus_ids call · none
New arm: tools/memory-tree/reuse_entries.py · covers AC10 · the `refile-later-date` plant's prefix tip, the failing case staged by a substring match · none
New arm: tools/check-microformats.test.sh · covers AC6 AC15 AC16 AC19 · the stripped-block assertion and the floor 74's arms owe, the failing case staged by `region() { exit 2; }` after the source line and by deleting one of 74's arms · FLOOR_ASSERTIONS raised by the count S10 derives
New arm: tools/run-gates/run-gates.test.sh · covers AC6 · the floor 74's lib-less and absent-block slice arms owe, the failing case staged by deleting one of those arms · FLOOR_ASSERTIONS raised by the count S10 derives
New arm: tools/memory-tree/decision_rubric.py · covers AC17 AC18 · the `no-local-row-predicate` case and the `no-conf` tip, the failing case staged by a local middot pattern and an uncaught row_grammar exception · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How does S18 close the third-resolver record (id 20)?** Options: (a) `gotchas.py` carries the
  canonical `resolve_bash_py` block inline, graded by its parity row, in place of `corpus_ids.resolve_bash`;
  (b) the resolver keeps 67's `corpus_ids.resolve_bash` and its docstring names the two resolvers it
  mirrors and `TOOL-dSettledRoster-6`, so the ask's convergence finds this caller by `git grep`. (a)
  reverses 67 §4's rejection of a second resolution rule in the memory-tree kit, which §3 above keeps out
  (veto 1), and its fall-through on an unusable `GOV_BASH` drops S17's named failure. RESOLVED (agent,
  2026-10-27, delegated): (b), rung 3, the most feature-rich survivor; the probe's strength stays
  `TOOL-dSettledRoster-6`'s to converge for every caller at once. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 65 to 74, 24 MEDIUM and 6 LOW
  findings batched in one unit.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-86, promoted from the spec
  audit of units 75 to 80; nothing else moved.

## 10. Reuse audit

Every item extends the seam its finding names: 74 S16's copies and constants, unit 75's predicate,
`gen_map.py --check`, `check-kit-versions.sh`'s pairings, each suite's `FLOOR_ASSERTIONS`, the parity loop
of `tools/lib/resolve-python.test.sh`, `read_pid_image`'s reading rule, the `observe-tree-hang` case, unit
1's `propose`, `append_only_re`'s boundary catch, `govkit.resolve_shell_argv` as the mirrored contract,
`read_map_cli`, 66's arm, `row_grammar`'s `--selftest` self-count and `load_conf`, and the help page; no
item mints a second implementation of any. `python tools/codebase-map/reuse_lookup.py "check the process
holding a pid is the one we started"` ranked `check`, `checks`, `check_line` and `check_convention`, and
`"check every free name of an inline block is bound in its host module"` ranked `check` and `checks`,
none a pid-identity or free-name reader, so no existing seam fits beyond those the items name.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse a ci job whose text or credentials come from a block it does not read" --terms "census ci-job refused opaque step credentials default variables block scalar fold header promoted"`
