# TOOL-dDeclaredLoop-56 — the round-1 spec audit's 47 minors: owed leg rows, one reader each, honest skew and failure paths, and the citations that drifted

**Status:** DEFERRED · rev-4 · 2026-10-25 · node d · Tier-2 · base ed497191 · streams tooling · order 36 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 |
| [2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-561.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-561.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-562.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-562.md) | deviation | — |
| [2026-10-25-build-TOOL-dDeclaredLoop-56-deviation-563.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-56-deviation-563.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
exited CONVERGED with 67 confirmed findings over the build's 34 units. Its 20 highs are units 36 to 55.
This unit is the batch BUILD-METHOD M4 makes of the rest, every MEDIUM and every LOW, each by its report
id and each its own scope item, where the report merged ids into one item too. The minors land on
twenty-eight units, so this unit repairs none in particular and builds after every unit (order 36). An
item whose defect would bite an earlier pass reaches that pass through the hands-off bullet the unit's
own §3 carries to this one; the rest are amended and observed at this pass.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 9, 40, 58 | S1, S2, S3 |
| M2 | MEDIUM | 26, 39 | S4, S5 |
| M3 | MEDIUM | 11, 29 | S6, S7 |
| M4 | MEDIUM | 22, 43, 60 | S8, S9, S10 |
| M5 | MEDIUM | 23, 57 | S11, S12 |
| M6 | MEDIUM | 10 | S13 |
| M7 | MEDIUM | 13 | S14 |
| M8 | MEDIUM | 14 | S15 |
| M9 | MEDIUM | 15 | S16 |
| M10 | MEDIUM | 16 | S17 |
| M11 | MEDIUM | 17 | S18 |
| M12 | MEDIUM | 20 | S19 |
| M13 | MEDIUM | 21 | S20 |
| M14 | MEDIUM | 30 | S21 |
| M15 | MEDIUM | 31 | S22 |
| M16 | MEDIUM | 32 | S23 |
| M17 | MEDIUM | 36 | S24 |
| M18 | MEDIUM | 37 | S25 |
| M19 | MEDIUM | 38 | S26 |
| M20 | MEDIUM | 27 | S27 |
| M21 | MEDIUM | 28 | S28 |
| M22 | MEDIUM | 33 | S29 |
| M23 | MEDIUM | 41 | S30 |
| M24 | MEDIUM | 42 | S31 |
| M25 | MEDIUM | 44 | S32 |
| M26 | MEDIUM | 45 | S33 |
| M27 | MEDIUM | 46 | S34 |
| M28 | MEDIUM | 53 | S35 |
| M29 | MEDIUM | 56 | S36 |
| M30 | MEDIUM | 59 | S37 |
| M31 | MEDIUM | 61 | S38 |
| M32 | MEDIUM | 62 | S39 |
| M33 | MEDIUM | 63 | S40 |
| M34 | MEDIUM | 64 | S41 |
| M35 | MEDIUM | 65 | S42 |
| M36 | MEDIUM | 66 | S43 |
| M37 | MEDIUM | 67 | S44 |
| L1 | LOW | 12 | S45 |
| L2 | LOW | 24 | S46 |
| L3 | LOW | 34 | S47 |

That is 44 MEDIUM and 3 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 9. Each leg added after `TOOL-dDeclaredLoop-4` (order 19) carries its `stage` claim on its
  `tools/gate-legs.json` row, by that unit's seed rule (`step.test` for a fixture leg): `loop command
  conformance` and `loop factories fixtures` (unit 6), `loop splice check` (25), `loop upstream fixtures`
  (29), `loop composition fixtures` (26), `loop scenario fixtures` (27), `loop adapt fixtures` (28),
  `loop review bounds fixtures` (21) and `loop budget fixtures` (30). Observed by AC1.
- **S2** — id 40. Each dossier minted after order 19 carries its top-level `stage` key, and the rule is
  handed once: `python tools/loop/stage_coverage.py` is run as this pass's last probe and every part it
  names unclaimed gets its claim here. Observed by AC2.
- **S3** — id 58. `TOOL-dDeclaredLoop-33` S10's "the stage claim every leg carries" is valued: `loop
  termination` carries `stage = ["step.test"]`. Observed by AC1.
- **S4** — id 26. Every leg this build adds has its `[[gate_leg]]` claim in `tools/loop/kit.toml` with
  `chunk` and `subject`, and a non-empty `enforces` list (§4 "The owed leg rows"). The claims owed are
  the `[[gate_leg]]` part of what PLAY-dOrderedCharter-50's `owed_rows.py --base <the build run's start
  commit>` prints for a leg added, where that parent has landed, else this item's list; an
  `[[exempt_leg]]` row never answers one, since every loop leg ships in the loop kit's descriptor.
  `enforces` is this item's own list, as the probe owes no such row: a leg whose unit wrote it is
  observed; any other gets the tag of the principle whose v2 `[enforcement]` row names the adding
  unit's clause, and the pending list's stale row for that tag is deleted. No tag is invented for a
  clause no row names (§8 F5). Observed by AC3.
  **Readers:** by name: READER NOT IN TREE — the pending list and its reader, the meta-check verb of
  the playbook kit's core.py, are minted by PLAY-dOrderedCharter-7, DEFERRED, so no tracked file spells
  the rows of S4's tags at this spec's base; once that unit lands, the meta-check is the one reader, and it reds
  the row as stale once a leg enforces its tag · by value: NO VALUE READERS — a pending row's value is
  its arming build, which the meta-check prints only in its pending count.
- **S5** — id 39. The same legs, and those of units 21 and 26 to 30, have their
  `tools/govkit/subject-pins.tsv` row (regenerated by `python tools/govkit/govkit.py selfcheck --write`),
  their claim in `memory/map/features/loop.md`'s `gate-legs` list, their
  `tools/run-gates/ceiling-evidence.txt` row, and, for a held leg, its `tools/run-gates/selftest-budgets.txt`
  row. Observed by AC3.
- **S6** — id 11. `refusal` joins `PARK_KINDS` in `tools/runlog/model.py` (:98) and `_RUN_PARK_KINDS` in
  `tools/drift-audit/drift_report.py` (:2427), the two copies the driver's comment holds to its line, as
  `TOOL-dDeclaredLoop-32` does for `fix-pass`. Observed by AC4.
- **S7** — id 29. `TOOL-dDeclaredLoop-14`'s refusal rows are read through runlog's `read_run_state`, which
  already splits ` · step ` (`tools/runlog/model.py:545-547`), reached with `resolve_kit_dir("runlog",
  "model.py", here)`; `read_refusals` is not minted. Observed by AC4.
- **S8** — id 22. The card's claims reader in `skills/session-kickoff/manifest-check.sh` accepts a row of
  five fields or six, reading a five-field row as `key —`, so a newer card over an older driver keeps its
  claims cell. Observed by AC5.
- **S9** — id 43. `tools/unattended/unattended.test.sh`'s five-field assertion (:15019-15021) moves with
  the change and is named in `TOOL-dDeclaredLoop-8`'s readers; the help line `TOOL-dDeclaredLoop-8` S8 adds
  to `skills/session-kickoff/SKILL.md` stays under that file's 18432-byte row
  (`tools/template-size-limits.txt:60`; the file measured 18310 bytes on 2026-10-24), its byte budget
  under 122. Observed by AC6.
- **S10** — id 60. `--claims` prints five fields by default and six only under `--claims --with-key`; the
  new card asks for the key with the flag, falls back to plain `--claims` when the driver refuses the
  flag, and an older card meets the five fields it reads today. Observed by AC5.
- **S11** — id 23. The roles adopter finds the loop kit by asking the loop kit's reader, never by a path
  guess: `adopt-roles.sh` runs `loop_lib.py --workflow-order` through its inline `resolve_python`, the
  directory found by `resolve_kit_dir` carried inline under its parity row. Observed by AC7.
- **S12** — id 57. No awk parses `loop.toml`: the adopter reads the CLI's `name order` lines, so a
  `[[step]]` row after the workflows cannot overwrite a workflow's order. Observed by AC7.
- **S13** — id 10. `TOOL-dDeclaredLoop-16` S4's disposition record keeps `Item` as the disposed item's tag
  and gains `Hold`, the run-state `decision` row a release names; `check_owner_disposition`
  (`TOOL-dDeclaredLoop-31` S6, `TOOL-dDeclaredLoop-19` S6) matches `Hold`, and `TOOL-dDeclaredLoop-28` S5
  matches `Item`. Observed by AC8.
- **S14** — id 13. `TOOL-dDeclaredLoop-24`'s `new item` takes `--inputs`, `--allowance` and `--returns`,
  required for a non-role actor, and its gate runs `python tools/loop/loop_lib.py --check` beside `loop
  item kind`. Observed by AC9.
- **S15** — id 14. The `@<n>` record-version grammar `TOOL-dDeclaredLoop-24` §8 F2 returned to unit 12 is
  applied to the seeded rows: every `record-kind.<name>` in an `inputs` or `returns` field of
  `tools/loop/loop.toml` carries its version. Observed by AC10.
- **S16** — id 15. `--exhausted` refuses unless `budget_state` reads `spent`, so an `unfrozen` budget with
  budget left is refused as an `open` one is. Observed by AC11.
- **S17** — id 16. `tools/loop/kit.toml` gains `requires` `memory-tree` with `TOOL-dDeclaredLoop-5`'s
  check, and `check_actor_list` imports `resolve_compare_base` from the memory-tree kit's shipped
  `coverage_join.py`, never from gov-internal `tools/lib/`. Observed by AC12.
- **S18** — id 17. `read_withdrawn_parents` reads each parent's halt code and asks
  `derive_phase_position` (`TOOL-dDeclaredLoop-52`) for its state, so an ABORTED parent with halt code
  `budget-exhausted` reads `incomplete` and fires no withdrawal route. Observed by AC13.
- **S19** — id 20. `read_commits` gains optional format arms, `body`, `files` (name-status under
  `--no-renames` and `core.quotepath=off`) and `ctime` (`%ct`), and a `counter` hook, so runlog's
  `read_git_range` (`tools/runlog/model.py:592-600`) keeps its one git call, its `GIT_CALLS` count and
  the integer type of `t`. Observed by AC14.
- **S20** — id 21. `check_terminal_proof` asks stderr's console per platform, the stream
  PLAY-dOrderedCharter-15 S5 tests (its §8 F4, the owner's pick): on win32 `sys.stderr.isatty()` and a
  console-mode probe of the stderr handle through `msvcrt`, on POSIX `sys.stderr.isatty()`; where
  `policy_edit.py` keeps a typed confirmation, EOF on that read prints the proposal and writes nothing.
  Observed by AC15.
- **S21** — id 30. `TOOL-dDeclaredLoop-7`'s engine reads the run-state file through runlog's
  `read_run_state` and takes owed membership from `PARK_KINDS_OWED` and `PARK_ACTS_OWED`
  (`tools/runlog/model.py:102`, :105), reached with `resolve_kit_dir("runlog", "model.py", here)`.
  Observed by AC16.
- **S22** — id 31. The guard's `agents-within-mandate` arm reads the effective phase from the driver's
  `--status` verb, which prints `read_derived_phase`'s answer, never the raw `phase:` fact. Observed by
  AC17.
- **S23** — id 32. `TOOL-dDeclaredLoop-20`'s class count reads the appendix through
  `parse_appendix_rows` (`tools/workflows/review_replay.py:151`), reached with `resolve_kit_dir`;
  `measure_class_occurrences` mints no parser, and a record the parser refuses is skipped and printed by
  name. Observed by AC18.
- **S24** — id 36. The run-gates canary keeps a near-miss control pair beside the `stage` key
  `TOOL-dDeclaredLoop-46` admits: a row carrying `stages` reds the canary while `stage` passes.
  Observed by AC19.
- **S25** — id 37. The text units 14 and 19 add to `tools/unattended/PROTOCOL.template.md` fits its
  66860-byte row (`tools/template-size-limits.txt:143`; the render measured 66859 bytes on 2026-10-24):
  this pass trims the render by at least the bytes those units added, and `wc -c` stays at or under the
  row. Observed by AC20.
- **S26** — id 38. `WIRE-INTO-PROJECT.md` gains an anchored `<!-- govkit:entry loop -->` section with a
  body, so the new registry entry adds no runbook-parity problem and `PROBLEM_PIN` stays 18
  (`tools/govkit/check_runbook_parity.py:60`, an equality). Observed by AC21.
- **S27** — id 27. `run_witness_commands` hashes output normalised by `tools/run-gates/lib-attribute.sh`'s
  `write_normaliser` rule (absolute roots, scratch names, durations, CR), the worktree root among the
  stripped roots, carried inline under a `normalise_output` parity row. Observed by AC22.
- **S28** — id 28. The inline `resolve_bash` `TOOL-dDeclaredLoop-42` carries joins a `resolve_bash_py`
  parity row with govkit's copy as canonical, and the re-run's plants run with a PATH whose first `bash`
  is a System32-shaped stand-in. Observed by AC23.
- **S29** — id 33. `upstream.py join --write` writes through `tools/memory-tree/build_records.py new
  upstream`, a registered `upstream` kind with its required fields, never its own file writer.
  Observed by AC24.
- **S30** — id 41. Units 7, 8 and 14 edit `tools/unattended/VERBS.template.md` with its render
  `memory/guides/UNATTENDED-VERBS.md` in the same commit, which unattended check 10 byte-compares.
  Observed by AC25.
- **S31** — id 42. `unattended.sh --status` reads the engine within its fork ceiling: its fork count is
  measured with `fork-count.sh` before and after, and `memory/project/fork-ceilings.txt`'s
  `unattended-status` row (ceiling 57) is either kept or raised with its measured reason. Observed by AC26.
- **S32** — id 44. `TOOL-dDeclaredLoop-21` AC5's grep excludes its own selftest arm by pathspec, and its
  S4 reader list names `tools/unattended/unattended.test.sh`'s `REVIEW_ROUNDS` sites. Observed by AC27.
- **S33** — id 45. `tools/roles/adopt-roles.test.sh`'s fixture copies the loop kit beside the roles kit,
  and one arm runs with no loop kit and expects a refusal naming `loop`. Observed by AC28.
- **S34** — id 46. scratch-guard's policy arm resolves the policy kit as it resolves its siblings, receipt
  then probe, and admits with one note when the kit or `guarded-paths.txt` is absent, never throwing into
  the fail-closed catch. Observed by AC29.
- **S35** — id 53. Every spelled `--review` command carries `--round-highs`: both lines of
  `tools/workflows/unattended-build.template.js` (:1861, :2289) and their render, and
  `tools/unattended/SKILL.template.md` (:120) and its render. Observed by AC30.
- **S36** — id 56. With no remote, or no remote-tracking ref for the default branch, the engine answers on
  local witnesses and prints `interrupt — no remote`; with a tracking ref past its bound it answers
  `stale-remote`, its age read from the ref's reflog. Observed by AC31.
- **S37** — id 59. The factory contract records per path whether it existed: on a red gate or a
  SIGINT or SIGTERM, created paths are deleted and existing ones restored; a gate already red before the
  write is reported as such and does not refuse the instance. Observed by AC32.
- **S38** — id 61. `tools/loop/kit.toml` gains a `requires_if` row naming unattended, and `loop_checklist.py
  check` prints `loop checklist tags: unarmed — no unattended kit` and exits 0 where the driver does not
  resolve. Observed by AC33.
- **S39** — id 62. `read_withdrawn_parents` reads a parent's `RUN.md` at the tip of its `run-branch:`
  remote-tracking ref when one exists, else at the default branch, and prints a parent with no `RUN.md`
  as `not withdrawn (no run record)`. Observed by AC34.
- **S40** — id 63. The review-rounds upgrade step never writes `.governance/policy.toml`: it prints the keys
  for the owner to set through `policy_edit.py`, leaves a key already set untouched and printed as a
  conflict, and keeps the conf line until the owner's value lands. Observed by AC35.
- **S41** — id 64. The left-shift count keys occurrences by distinct review, the unit id and review kind
  from the record name with its rounds collapsed, under `MEMORY_ROOT`. Observed by AC36.
- **S42** — id 65. `read_attribution_tokens` runs once over the whole range and fills `_SUBJ` before
  `build_commit`'s walk, in place of its per-commit call on a cache miss
  (`tools/unattended/lib-unattended.sh:1276`), so no caller spawns an interpreter per commit; both names
  keep their callers. Observed by AC37.
- **S43** — id 66. `TOOL-dDeclaredLoop-23`'s suite arm asserts literal ids per planted commit,
  `TOOL-tFix-1`, `TOOL-tFix-1`, `TOOL-tFix-2` under `union`, and the base-sha compare stays a one-time
  pass probe. Observed by AC38.
- **S44** — id 67. On a refused commit the transition writer resets exactly the paths it staged, removes
  the files it created and exits naming the hook's refusal, so a retry succeeds. Observed by AC39.
- **S45** — id 12. `flow.scenario-default` is a bare name resolved to `scenario.<name>`, then
  `scenario.adopter.<name>`, before lookup; `TOOL-dDeclaredLoop-27` AC1 and AC6 are read as `feature` and
  `nowhere`. Observed by AC40.
- **S46** — id 24. The shared F1 probe's citation `tools/memory-tree/tree_lib.py:27` reads `:28`, the
  `STATUS_TOKENS` tuple, in each live spec carrying it, each as a rev bump with its §9 line.
  Observed by AC41.
- **S47** — id 34. `check_owner_disposition` calls a Python entry point, `python tools/loop/loop_lib.py
  disposition --hold <row>`, through `run_bounded "$_py"`; only the factory's reader parses the record.
  Observed by AC42.

## 3. Non-goals (OUT)

- Any high: units 36 to 55, one per id.
- The spec lints and checklist entries the report names as left-shifts for these minors: each would be a
  new gate no clause of this build names; the classes are recorded at the close.
- Re-reviewing any repaired unit: M4 forbids it; each item here is built and observed at this pass.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — the roles adopter's loop read and the `loop` registry entry (ids 23, 26, 38, 39, 45, 57)
- **consumes-from** `TOOL-dDeclaredLoop-2` — the terminal proof, the mandate arm and scratch-guard's policy arm (ids 21, 26, 31, 39, 46)
- **consumes-from** `TOOL-dDeclaredLoop-3` — the transition writer's commit step (id 67)
- **consumes-from** `TOOL-dDeclaredLoop-4` — the `stage` claim and `loop stage coverage` (ids 9, 26, 36, 40, 58)
- **consumes-from** `TOOL-dDeclaredLoop-5` — `check_actor_list` and its compare base (id 16)
- **consumes-from** `TOOL-dDeclaredLoop-6` — the factory contract and its two legs (ids 9, 26, 39, 59)
- **consumes-from** `TOOL-dDeclaredLoop-7` — the engine's run-state read, its remote answer and `--status` (ids 26, 30, 39, 41, 42, 56)
- **consumes-from** `TOOL-dDeclaredLoop-8` — the keyed `--claims` rows and the card (ids 22, 26, 39, 41, 43, 60)
- **consumes-from** `TOOL-dDeclaredLoop-11` — `loop_checklist.py check` (id 61)
- **consumes-from** `TOOL-dDeclaredLoop-12` — the seeded item rows (id 14)
- **consumes-from** `TOOL-dDeclaredLoop-14` — the `refusal` park kind and its protocol text (ids 11, 26, 29, 37, 39, 41)
- **consumes-from** `TOOL-dDeclaredLoop-15` — `read_withdrawn_parents` (ids 17, 62)
- **consumes-from** `TOOL-dDeclaredLoop-16` — the disposition record's fields (id 10)
- **consumes-from** `TOOL-dDeclaredLoop-17` — `run_witness_commands` (ids 27, 28)
- **consumes-from** `TOOL-dDeclaredLoop-19` — the protocol text and the owner-gate release (ids 10, 37)
- **consumes-from** `TOOL-dDeclaredLoop-20` — the class count (ids 32, 64)
- **consumes-from** `TOOL-dDeclaredLoop-21` — AC5's grep and the review-rounds upgrade step (ids 9, 39, 44, 63)
- **consumes-from** `TOOL-dDeclaredLoop-23` — `read_commits`, `read_attribution_tokens` and the suite arm (ids 20, 65, 66)
- **consumes-from** `TOOL-dDeclaredLoop-24` — the item factory and the record-version grammar (ids 13, 14)
- **consumes-from** `TOOL-dDeclaredLoop-25` — the `loop splice check` leg (ids 9, 26, 39)
- **consumes-from** `TOOL-dDeclaredLoop-26` — the `loop composition fixtures` leg (ids 9, 39)
- **consumes-from** `TOOL-dDeclaredLoop-27` — `flow.scenario-default` and its leg (ids 9, 12, 39)
- **consumes-from** `TOOL-dDeclaredLoop-28` — the disposition match and its leg (ids 9, 10, 39)
- **consumes-from** `TOOL-dDeclaredLoop-29` — `upstream.py join --write` and its leg (ids 9, 33, 39)
- **consumes-from** `TOOL-dDeclaredLoop-30` — `budget_state` and its leg (ids 9, 15, 39)
- **consumes-from** `TOOL-dDeclaredLoop-31` — `--exhausted` and `check_owner_disposition` (ids 10, 15, 34)
- **consumes-from** `TOOL-dDeclaredLoop-32` — the `--round-highs` flag (id 53)
- **consumes-from** `TOOL-dDeclaredLoop-33` — the `loop termination` leg row (ids 26, 39, 58)
- **consumes-from** `TOOL-dDeclaredLoop-42` — the inline `resolve_bash` and the file-backed run (ids 27, 28)
- **consumes-from** `TOOL-dDeclaredLoop-46` — the `stage` key admitted to the canary (id 36)
- **consumes-from** `TOOL-dDeclaredLoop-52` — `derive_phase_position` (id 17)
- **hands-off** `TOOL-dDeclaredLoop-65` — the remote-freshness age source of S36, which that unit reads from what a fetch and a clone write (the round-2 spec audit's id 55)
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 3, 4, 12, 22, 23, 24, 36, 50, 66 and 67, each a scope item of that unit
- **hands-off** `TOOL-dDeclaredLoop-68` — S27's inline normaliser and its `normalise_output` parity row, which that unit replaces with the run-gates program at order 37 (the round-3 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-70` — the shared adopter-phase population, which S18's `read_withdrawn_parents` call takes by passing no explicit `extra` (the round-3 spec audit's id 19)

## 4. Design

### Why one unit and not two

The minors fall on twenty-eight units, and their write sets meet: `tools/loop/loop.toml` and
`tools/loop/kit.toml` are written by S1, S4, S15 and S38; `tools/unattended/unattended.sh` by S10, S16,
S31 and S36; `tools/gate-legs.json` by S1 and S3; and the build's shared records by S46. BUILD-METHOD M6's
clause 1 then fails for any split into two halves that keeps each half's items together, so one unit,
sequenced.

### The owed leg rows (S4, S5)

In the `enforces` column, "own" means the leg's unit writes it in its pass and this item observes it;
a tag means this item writes it. "Base" is `[[gate_leg]]`, pins, dossier and ceiling evidence.

| Leg | Unit | `enforces` | Rows owed here |
|---|---|---|---|
| `loop definition` | 1 | own | base |
| `loop guard fixtures` | 2 | F5: no row names `cl-dClosedLoop-0087` | base |
| `loop transition record` | 3 | own, its §8 F7 | base |
| `loop stage coverage` | 4 | own | base |
| `loop command conformance`, `loop factories fixtures` | 6 | own | base, and `stage` |
| `loop position fixtures` | 7 | `principle.p22` | base |
| `loop claims fixtures` | 8 | `principle.p23` | base |
| `loop frontier fixtures` | 14 | `principle.p24` | base |
| `loop computed witness` | 17 | own | base |
| `loop review bounds fixtures` | 21 | `principle.p38` | pins, dossier, ceiling evidence, `stage` |
| `loop splice check` | 25 | `principle.p20` | base, and `stage` |
| `loop composition fixtures`, `loop adapt fixtures`, `loop upstream fixtures` | 26, 28, 29 | F5: no row names their clauses | pins, dossier, ceiling evidence, `stage` |
| `loop scenario fixtures` | 27 | own | pins, dossier, ceiling evidence, `stage` |
| `loop budget fixtures` | 30 | `principle.p39` | pins, dossier, ceiling evidence, `stage` |
| `loop termination` | 33 | own | base, and `stage` |

### Evidence

- The park-kind copies: `PARK_KINDS` at `tools/runlog/model.py:98` and `_RUN_PARK_KINDS` at
  `tools/drift-audit/drift_report.py:2427`; `read_run_state` splits ` · step ` at :545-547; the owed sets
  at :102 and :105.
- The card: `NF == 5 && ($5 in rk)` and the first other line recorded as `bad`
  (`skills/session-kickoff/manifest-check.sh:666-676`); the driver cuts its rows to five fields
  (`tools/unattended/unattended.sh:2204`); the suite asserts five (`tools/unattended/unattended.test.sh:15019-15021`).
- The size rows: `skills/session-kickoff/SKILL.md` 18432 (`tools/template-size-limits.txt:60`) and
  `memory/guides/UNATTENDED-PROTOCOL.md` 66860 (:143), measured at 18310 and 66859 bytes.
- `PROBLEM_PIN = 18` and the equality refusal (`tools/govkit/check_runbook_parity.py:44-60`, :118-125).
- `parse_appendix_rows` at `tools/workflows/review_replay.py:151` and `scan_corpus` at :357;
  `write_normaliser`, `add_scratch_worktree` and `remove_scratch_worktree` at
  `tools/run-gates/lib-attribute.sh:40`, :59, :63.
- The two harness lines spelling `--review` at `tools/workflows/unattended-build.template.js:1861` and
  :2289, and the Skill's usage line at `tools/unattended/SKILL.template.md:120`.
- The `unattended-status` fork ceiling row: `5.3 47 57` (`memory/project/fork-ceilings.txt:15`).
- The per-commit fallback: `tools/unattended/lib-unattended.sh:1276`.

### Inventory

| Minted | Kind | Where |
|---|---|---|
| `--with-key` | flag of `--claims` | `tools/unattended/unattended.sh` |
| `Hold` | disposition record field | `tools/memory-tree/build_records.py` |
| `body`, `files`, `ctime`, `counter` | keyword arguments of `read_commits` | `tools/lib/commit_trailers.py` |
| `normalise_output`, `resolve_bash_py` | parity rows and block markers | `tools/lib/resolve-python.test.sh` |
| `upstream` | record kind | `tools/memory-tree/build_records.py` |
| `disposition` | CLI verb | `tools/loop/loop_lib.py` |

### Files touched (estimate)

- `tools/gate-legs.json`
- `tools/playbook/core-pending.txt`: the stale `principle` rows of S4's tags, deleted where held
- `tools/loop/kit.toml`
- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`
- `tools/loop/position.py`
- `tools/loop/guard.py`
- `tools/loop/factories.py`
- `tools/loop/loop_witness.py`
- `tools/loop/loop_parents.py`
- `tools/loop/loop_checklist.py`
- `tools/loop/review_dispose.py`
- `tools/loop/upstream.py`
- `tools/loop/loop_transition.py`
- `tools/loop/scenario.py`
- `tools/lib/commit_trailers.py`
- `tools/lib/guarded_write.py`
- `tools/lib/resolve-python.test.sh`
- `tools/runlog/model.py`
- `tools/drift-audit/drift_report.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/SKILL.md`
- `tools/roles/adopt-roles.sh`
- `tools/roles/adopt-roles.test.sh`
- `tools/hooks/scratch-guard.js`
- `tools/memory-tree/build_records.py`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/run-gates/selftest-budgets.txt`
- `tools/govkit/subject-pins.tsv`
- `tools/govkit/selftest.py`
- `memory/map/features/loop.md`
- `memory/project/fork-ceilings.txt`
- `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- **One unit per minor.** M4 forbids it: the batch is the one unit the one-mechanism rule admits.
- **Folding the minors into the repaired specs.** M4 forbids folding at the exit; each item is built here.

## 5. Production-readiness checklist

- security — S20 closes a terminal-proof gap on win32, S22 a mandate check read from the raw phase, and
  S34 a throw into a fail-closed write gate; S40 keeps the owner's policy file owner-written.
- perf / scale — S42 removes an interpreter start per commit; S31 keeps `--status` inside its fork ceiling.
- error / empty / loading states — S36, S38 and S39 each turn an absent input into a named reading, never a
  red and never a silent green.
- observability — each item's refusal or skip names its subject.
- risks — S10 adds a flag to a verb two kits read; the fallback keeps both skews working.
- testing — AC1 to AC42 as probes and plants; the arms under §7, observed at the close.
- migration — S40 replaces a write with a printed proposal; no other item migrates data.
- user docs — S26's runbook section; `help/loop.md` names S2's claim rule.

## 6. Acceptance criteria

- **AC1** — When a probe reads `tools/gate-legs.json` on the built tree, each of the ten legs S1 and S3 name
  carries a non-empty `stage` list of declared step tags.
  Red when: a leg added after order 19 carries no `stage`, so `loop stage coverage` reds it.
- **AC2** — When `python stage_coverage.py` runs on the built tree, it prints `0 unclaimed` for
  every join and kind and exits 0.
  Red when: a dossier minted after order 19 lacks its `stage` key.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, 7h finds a descriptor
  claim for every leg of §4's table and `tools/govkit/subject-pins.tsv` a row for each; `grep -c` over
  the loop dossier, `loop.md`, finds each leg name; no `[[exempt_leg]]` row of
  `tools/govkit/registry.toml` names one; each leg's row of `tools/gate-legs.json` carries a non-empty
  `enforces`, the tag §4 names where it names one; and `python tools/playbook/core.py meta-check`
  names none of them.
  Red when: a leg this build added has no `[[gate_leg]]` claim, no subject-pins row or no `enforces`,
  or an `[[exempt_leg]]` row stands in for its claim.
- **AC4** — When `grep -c 'refusal'` runs over the tuples at `tools/runlog/model.py:98` and
  `tools/drift-audit/drift_report.py:2427`, each prints 1, and `git grep -n 'def read_refusals' -- tools`
  prints nothing.
  Red when: a copy lacks `refusal`, so `read_run_state` files every refusal row under `unknown_kinds`.
- **AC5** — When a probe pairs the new card with a driver that refuses `--with-key`, and the old card with
  the new driver, each card prints its claims cell and neither prints `cannot read`.
  Red when: a skewed pair replaces the cell with the skip line.
- **AC6** — When `wc -c skills/session-kickoff/SKILL.md` runs on the built tree it prints at most 18432,
  and the suite's five-field assertion reads the default `--claims`.
  Red when: the help line breaches the cap, or the suite still asserts five fields over `--with-key`.
- **AC7** — When the roles adopter's `--check` runs over a fixture whose `loop.toml` holds `[[step]]` rows
  after its `[[workflow]]` rows and whose loop kit is homed at a non-default path by its install receipt,
  `install.json`, it exits 0, and `grep -c 'loop.toml' tools/roles/adopt-roles.sh` finds no
  awk over that file.
  Red when: the awk reads the last workflow's order from a step row, or the lookup guesses a path.
- **AC8** — When `check_owner_disposition` reads a fixture record whose `Hold` names the `decision` row and
  whose `Item` names an item tag, it releases the hold; a record with only `Item` does not.
  Red when: one field is matched against three populations.
- **AC9** — When `python core.py new item` writes a command-actor row with `--inputs`,
  `--allowance` and `--returns`, `python loop_lib.py --check` exits 0 after it, and the same
  call without them refuses naming the missing field.
  Red when: the factory reports success on a row the definition check refuses.
- **AC10** — When `grep -cE 'record-kind\.[a-z-]+@[0-9]+' loop.toml` runs in `tools/loop/`, it prints at least 1,
  and no `record-kind.` reference in an `inputs` or `returns` field lacks its version.
  Red when: the grammar lives only in fixture plants.
- **AC11** — When `unattended.sh --exhausted` runs over a fixture whose `budget_state` reads `unfrozen 2/4`,
  it refuses.
  Red when: an unfrozen budget with budget left ends the build.
- **AC12** — When `grep -n 'requires' kit.toml` runs in `tools/loop/`, it lists `memory-tree`, and
  `grep -n 'tools/lib' loop_lib.py` there finds no import.
  Red when: a copy-installed loop kit imports gov-internal `tools/lib/`.
- **AC13** — When `python loop_parents.py --fixture --plant incomplete-parent` runs, a
  parent ABORTED with `budget-exhausted` answers `route none`.
  Red when: every ABORTED parent fires the withdrawal route.
- **AC14** — When `read_git_range` reads a scratch range through `read_commits` with the format arms, its
  `GIT_CALLS` count and the type of each `t` equal base `ed497191`'s on the same range.
  Red when: the re-point adds a git call or turns `t` into a string.
- **AC15** — When `check_terminal_proof` runs with stderr redirected to a pipe, `NUL` and a regular file on
  win32, each is refused by name, and where `policy_edit.py` keeps its typed confirmation, EOF on that
  read prints the proposal and writes nothing.
  Red when: `NUL` passes the terminal test, the check reads stdin, or EOF raises a traceback.
- **AC16** — When `git grep -n 'read_run_state\|PARK_KINDS_OWED' -- tools/loop` runs, both
  appear in `position.py`, and `git grep -n 'PARK_KINDS_OWED *=' -- tools/loop` prints nothing.
  Red when: the engine carries a third owed-set copy.
- **AC17** — When `python guard.py --fixture --plant mandate-landed` runs a run whose recorded
  phase is LANDING with its landing observed, `agents-within-mandate` refuses.
  Red when: the raw `phase:` fact reports a landed run live.
- **AC18** — When the class count runs over a fixture record whose appendix the parser refuses, it skips
  that record and prints its name, and `git grep -n 'def measure_class_occurrences' -- tools/loop` finds a
  function that calls `parse_appendix_rows`.
  Red when: a second parser counts the refused record.
- **AC19** — When the canary runs over a scratch manifest with one row carrying `stages`, it fails; with
  `stage` it passes.
  Red when: the key set admits any key spelled near `stage`.
- **AC20** — When `wc -c memory/guides/UNATTENDED-PROTOCOL.md` runs on the built tree, it prints at most
  66860.
  Red when: units 14 and 19's text breaches the row.
- **AC21** — When `python tools/govkit/check_runbook_parity.py` runs, it prints `18 problem(s) · pin 18`.
  Red when: the `loop` entry adds a nineteenth problem.
- **AC22** — When `python loop_witness.py rerun` re-runs one fixture command that prints its
  tree path twice at one sha, the two hashes are equal.
  Red when: the raw output's worktree path differs per run, so a holding probe reads `refuted`.
- **AC23** — When the re-run's plants `bash -c 'exit 0'` and `true | grep -c x; exit 0` run with a PATH
  whose first `bash` is a System32-shaped stand-in, each records exit 0, and the `resolve_bash_py` parity
  extract matches govkit's copy.
  Red when: the stand-in is resolved, or the inline copy drifts.
- **AC24** — When `upstream.py join --write` runs in a fixture, the record is readable through
  `build_records.py`'s `read_record`, and `git grep -n "open(.*'w'" -- tools/loop` prints no
  `upstream.py` line.
  Red when: the join writes the file itself.
- **AC25** — When `grep -c` runs over `tools/unattended/VERBS.template.md` and
  `memory/guides/UNATTENDED-VERBS.md` for each verb units 7, 8 and 14 add, the two counts agree.
  Red when: the template is edited and the render is not.
- **AC26** — When `fork-count.sh` measures `unattended-status` on the built tree, the count is at or under
  that row's ceiling in `memory/project/fork-ceilings.txt`.
  Red when: the engine call breaches the ceiling unrecorded.
- **AC27** — When `TOOL-dDeclaredLoop-21` AC5's grep runs with its new pathspec, it prints only the upgrade
  program and its `kit.toml` row.
  Red when: the unit's own selftest arm reds its criterion.
- **AC28** — When the roles adopter suite's fixture is built, `ls` finds the loop kit beside the roles kit,
  and the no-loop arm's adopter run exits non-zero naming `loop`.
  Red when: every arm fails stage binding for a missing kit.
- **AC29** — When scratch-guard's policy arm runs in a fixture with no policy kit, an Edit is admitted with
  one note, and `grep -n 'tools/policy/guarded-paths.txt' tools/hooks/scratch-guard.js` finds no literal.
  Red when: the absent kit throws into the fail-closed catch and every write is denied.
- **AC30** — When `git grep -n -e "--review '" -e ' --review ' -- tools/workflows tools/unattended/*.template.md`
  runs, every line it prints carries `--round-highs`.
  Red when: the degraded hand-record line omits the flag.
- **AC31** — When `python position.py --fixture --plant no-remote` runs, the answer is `act` and
  the line `interrupt — no remote` is printed; `--plant offline-stale` answers `stale-remote`.
  Red when: a fresh scratch tree with no remote answers `stale-remote`.
- **AC32** — When `--plant factory-restores-create` runs the hook factory against a red gate, its new files
  are absent afterwards, and `--plant factory-restores-append` restores the appended file's bytes.
  Red when: a created file survives a red gate.
- **AC33** — When `python loop_checklist.py --fixture --plant no-driver` runs, it prints
  `unarmed — no unattended kit` and exits 0.
  Red when: the leg exits 2 in every tree without the driver.
- **AC34** — When `python loop_parents.py --fixture --plant aborted-on-run-branch` and
  `--plant no-run-record` run, the first reads the
  parent withdrawn from its run branch's tip and the second prints `not withdrawn (no run record)`.
  Red when: the parent's phase is read from the child's tree.
- **AC35** — When the upgrade step runs in a fixture whose policy file, `policy.toml`, already sets
  `review.design.rounds`, the file's bytes are unchanged, the conflict is printed, and the conf line stays.
  Red when: the step writes the policy file, which the guard refuses for an agent commit.
- **AC36** — When the class count runs over two rounds of one review disposing `class:stale-pin` and no
  other record, no gate is earned.
  Red when: a review's own earlier round counts as a prior occurrence.
- **AC37** — When a probe counts interpreter starts while `build_commit` walks a fixture range of twenty
  commits with an empty cache, it counts one.
  Red when: the fallback starts one interpreter per commit.
- **AC38** — When `grep -n 'git show'` runs over the routed-commits arm `TOOL-dDeclaredLoop-23` declares,
  it prints nothing, and the arm names `TOOL-tFix-1` and `TOOL-tFix-2` literally.
  Red when: the arm's oracle is read from a historical sha.
- **AC39** — When `python loop_transition.py --fixture --plant commit-refused` runs with a hook
  exiting 1, `git diff --cached --name-only` prints nothing afterwards and a retry succeeds.
  Red when: the staged records stay and every later `record` exits 2.
- **AC40** — When the scenario fixture sets `flow.scenario-default = "feature"`, the composition places
  `scenario.feature`, and `nowhere` is refused naming it.
  Red when: the bare value is looked up as a tag and never found.
- **AC41** — When `git grep -c 'tree_lib.py:27' -- memory/builds/dDeclaredLoop/spec/` runs on the built tree,
  it prints nothing.
  Red when: a live spec still cites the comment line.
- **AC42** — When `grep -n 'loop_lib.py.* disposition' tools/unattended/unattended.sh` runs, it finds
  `check_owner_disposition`'s call, and a fixture record with two `Disposition` lines is refused.
  Red when: a shell parse admits the record the factory refuses.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `check-wiring self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `lexicon naming predicates` · `review-join self-test` · `routed-commits selftest` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended protocol size` · `unattended skill size` · `kickoff engine size <=18KiB` · `manifest-check self-test` · `roles adopter self-test` · `scratch-guard self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `spawn budget (forks per hot entrypoint)` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `codebase-map coverage + freshness` · `python resolver (behaviour + inline parity + idiom ban)` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `drift-audit selftest` · `unattended-build self-test` · `workflow script syntax` · `recall floor` · `recall floor arms` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC19 · the `stages` control row, staged against a canary that admits any key near `stage` · none
New arm: tools/lib/resolve-python.test.sh · covers AC22 AC23 · the `normalise_output` and `resolve_bash_py` parity rows, each staged by a one-byte edit to the loop copy · none
New arm: tools/roles/adopt-roles.test.sh · covers AC28 · the fixture with the loop kit and the no-loop arm, staged against the base fixture · the suite's assertion floor raised by the arm added
New arm: tools/loop/position.py · covers AC31 · the `no-remote` and `offline-stale` plants, staged against the engine's single stale-remote rule · none

The unattended kit's own suites are waived for this build's landing (README rule 8): AC6, AC11, AC37 and
AC42 are observed by probes, never by those suites.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — One batch unit or two?** Options: (a) one; (b) two halves by write set. §4 shows the halves meet on
  `tools/loop/loop.toml`, `tools/loop/kit.toml`, `tools/unattended/unattended.sh` and the shared records,
  failing M6's clause 1. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — How does `--claims` survive kit skew (S10)?** Options: (a) six fields by default with a tolerant
  card; (b) five by default, six under `--with-key`. (a) still breaks an old card over a new driver, the
  skeptic's reason for judging the finder's fix unsound. RESOLVED (agent, 2026-10-24, delegated): (b), rung
  3; the flag serves the clause's keyed claims, the surface `PLAY-dClosedLoop-3` grants for this build's
  clauses. grants: PLAY-dClosedLoop-3 the --claims --with-key flag · widens: none · relaxes: none
- **F4 — Where does the review-rounds upgrade write (S40)?** Options: (a) a proposal the owner lands; (b) a
  new admitted shape in the guard. (b) widens the guard's write surface, veto 3, and the skeptic judged it
  unsound. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — Who writes `enforces` for a leg whose own unit names none?** PLAY-dOrderedCharter-7 S3 reds
  such a leg from the pass that adds it, and its pending list only shrinks after that unit's pass, so
  no row excuses it. The re-ground gives the key to units 1, 3, 4, 6, 17, 27 and 33; units 2, 7, 8, 14,
  21, 25, 26 and 28 to 30 add legs before order 36 with none, as do units 11 (P11), 13 (P20) and 15,
  which §4's table omits. No `[enforcement]` row names the clauses of units 2, 15, 26, 28 and 29.
  Options: (a) re-ground each such unit so its own pass writes the key, its tag settled where no row
  names its clause, and S4 only observes; (b) S4 writes the keys at order 36, the bar's `core
  meta-check` leg red from each such pass until then; (c) a pending-list row, which the shrink-only
  list refuses. (b) lands red across many passes and (c) breaks unit 7's rule. Recommendation: (a).
  Open for the owner, since (a) revises specs outside this re-ground.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the batch of the round-1 spec audit's 44 MEDIUM and 3 LOW findings.
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-65 and TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-68 and TOOL-dDeclaredLoop-70, written by the round-3 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-25 · §2 S4, S20 · §4 The owed leg rows, Files touched · §6 AC3, AC15 · §8 F5 ·
  re-grounded on dOrderedCharter at `462d20f35` by the cross-check record
  `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`, rows 126 and 127 and
  the `enforces` rows 7, 18, 23, 36 and 47: S4 takes only the `[[gate_leg]]` part from `owed_rows.py`,
  keeps its own `enforces` list with no pending-list fallback and refuses an `[[exempt_leg]]` answer;
  the table gains units 3, 17 and 27; S20 tests stderr, per PLAY-dOrderedCharter-15 F4.

## 10. Reuse audit

Every item reuses a seam the report names and this spec's §4 cites: runlog's `read_run_state` and owed sets
(S7, S21), `parse_appendix_rows` (S23), lib-attribute's normaliser (S27), govkit's `resolve_bash` (S28),
the record factory (S29, S47), `resolve_kit_dir` (S11, S34), `derive_phase_position` from
`TOOL-dDeclaredLoop-52` (S18), and the driver's `read_derived_phase` through `--status` (S22); no item
mints a second reader of a grammar one already reads. `python tools/codebase-map/reuse_lookup.py "read the
run-state file's parked rows and the owed kinds"` ranked generic name-stem hits (`rows`, `row`, `read`,
`read_journal`) and missed `read_run_state` (`tools/runlog/model.py`), which the report's reuse lens found
and which was read at source for S7 and S21: a stale or blind map, recorded here as M5 asks.

Recall terms used: owed rows gate_leg subject-pins stage claim park kinds read_run_state claims skew runbook anchor normaliser
