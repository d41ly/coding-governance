# TOOL-dDeclaredLoop-67 — the round-2 spec audit's 54 minors, batched

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 38 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 |
| [2026-10-24-build-TOOL-dDeclaredLoop-67-deviation-671.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-67-deviation-671.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-67-deviation-672.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-67-deviation-672.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
exited CONVERGED with 64 confirmed findings over the 21 units the round-1 promotions added. Its ten
highs are units 57 to 66, one per id. This unit is the batch BUILD-METHOD M4 makes of the rest, every
MEDIUM and every LOW, each by its report id and each its own scope item, where the report merged ids
into one item too. The minors land on twenty-two units, so this unit repairs none in particular and
builds after every unit (order 38). An item whose defect would bite an earlier pass reaches that pass
through the hands-off bullet the unit's own §3 carries to this one; the rest are built and observed here.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2 | S1 |
| M2 | MEDIUM | 3, 23 | S2, S3 |
| M3 | MEDIUM | 4, 22 | S4, S5 |
| M4 | MEDIUM | 5, 21, 42 | S6, S7, S8 |
| M5 | MEDIUM | 6 | S9 |
| M6 | MEDIUM | 7, 20 | S10, S11 |
| M7 | MEDIUM | 8 | S12 |
| M8 | MEDIUM | 9, 27 | S13, S14 |
| M9 | MEDIUM | 10 | S15 |
| M10 | MEDIUM | 11 | S16 |
| M11 | MEDIUM | 18 | S17 |
| M12 | MEDIUM | 24 | S18 |
| M13 | MEDIUM | 25, 47 | S19, S20 |
| M14 | MEDIUM | 26 | S21 |
| M15 | MEDIUM | 33 | S22 |
| M16 | MEDIUM | 35 | S23 |
| M17 | MEDIUM | 36 | S24 |
| M18 | MEDIUM | 39 | S25 |
| M19 | MEDIUM | 40 | S26 |
| M20 | MEDIUM | 41 | S27 |
| M21 | MEDIUM | 43 | S28 |
| M22 | MEDIUM | 44 | S29 |
| M23 | MEDIUM | 45 | S30 |
| M24 | MEDIUM | 46 | S31 |
| M25 | MEDIUM | 54 | S32 |
| M26 | MEDIUM | 61 | S33 |
| M27 | MEDIUM | 62 | S34 |
| M28 | MEDIUM | 63 | S35 |
| M29 | MEDIUM | 64 | S36 |
| M30 | MEDIUM | 65 | S37 |
| M31 | MEDIUM | 66 | S38 |
| L1 | LOW | 12 | S39 |
| L2 | LOW | 13, 37 | S40, S41 |
| L3 | LOW | 14, 31 | S42, S43 |
| L4 | LOW | 15, 29 | S44, S45 |
| L5 | LOW | 16, 49 | S46, S47 |
| L6 | LOW | 28 | S48 |
| L7 | LOW | 30 | S49 |
| L8 | LOW | 48 | S50 |
| L9 | LOW | 50 | S51 |
| L10 | LOW | 60 | S52 |
| L11 | LOW | 67 | S53 |
| L12 | LOW | 68 | S54 |

That is 38 MEDIUM and 16 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 2. `TOOL-dDeclaredLoop-33` AC10's "whose guard holds the loop kit's path" clause is
  superseded by `TOOL-dDeclaredLoop-55` S1, as `TOOL-dDeclaredLoop-47` S4 restates a sibling criterion: the
  `loop termination` row carries no guard, its acceptance ledger line cites this item, and S31's arm holds
  the property. Observed by AC1.
- **S2** — id 3. `TOOL-dDeclaredLoop-56` AC41's probe excludes the specs that spell the pattern to
  describe it, `TOOL-dDeclaredLoop-56` and this one: `':!*TOOL-dDeclaredLoop-56.md'
  ':!*TOOL-dDeclaredLoop-67.md'`. Observed by AC2.
- **S3** — id 23. The same probe is anchored, `git grep -nE 'tree_lib\.py:27([^0-9]|$)'`, so the correct
  citation `tree_lib.py:278-297` never matches; its red case on today's tree is 14 files. Observed by AC2.
- **S4** — id 4. `TOOL-dDeclaredLoop-56` AC30 observes each command's whole string expression, read up to
  its statement's `;`, at the sites S35 names, `unattended-build.template.js` :1861 and :2289 and their
  render; the prose at :555 and `*.test.sh` are outside it. Observed by AC3.
- **S5** — id 22. AC30's population also holds `SKILL.template.md` :120 and its render
  `.claude/skills/unattended/SKILL.md`, the render S35 names and the pathspec omitted. Observed by AC3.
- **S6** — id 5. `TOOL-dDeclaredLoop-46` AC2 is observed through TOML: every descriptor parsed with
  `tomllib`, and each `[[gate_leg]]` table carries `stage` as a list of step tags, never an integer.
  Observed by AC4.
- **S7** — id 21. The descriptor family's existing integer `stage` key on `[[regenerate]]`,
  `[[generated]]` and `[[outcome]]` rows, read by `tools/run-gates/regen.py:179-221`, is named in
  `tools/loop/stage_coverage.py`'s header, and the reader scopes `stage` to `[[gate_leg]]` tables, so a
  regen integer is never read as a claim. Observed by AC4.
- **S8** — id 42. regen's reader is shown blind to the list form: `regen.py` reads `stage` only on its
  own row kinds, so a `[[gate_leg]]` list never enters its staging, and a missing gate-leg `stage`
  cannot be masked by a regen integer in the same file. Observed by AC4.
- **S9** — id 6. The stage factory takes `--after` alone: the new step's order is the after-step's plus
  one, and every later step's order moves up by one in the same guarded write, so `read_steps` reads a
  contiguous run; no `--order` option is minted. Observed by AC5.
- **S10** — id 7. `TOOL-dDeclaredLoop-43`'s rollback fixtures fail the record write by patching the
  sibling-temp `os.replace` to raise on its second call, after the policy write landed, never by a
  read-only directory, which does not fail a write on win32. Observed by AC6.
- **S11** — id 20. The record path is never an existing directory in those fixtures: the prior-bytes read
  would raise before any write, so the restore would never run; AC2's "no record exists" holds over the
  patched route. Observed by AC6.
- **S12** — id 8. The literal root is gone from the three specs' code: `TOOL-dDeclaredLoop-60` S1-S2 and
  `TOOL-dDeclaredLoop-64` S1 resolve `MEMORY_ROOT` for 48 and 53, and the 49 instance, gov's own
  `.gitattributes` line, is gov's root by construction, its adopter form being S34's. Observed by AC7.
- **S13** — id 9. A `[[phase]]` row may carry `step = "held-in"` for `HELD` alone, and
  `derive_phase_position` resolves it to the step of the run's `held-from` phase, the fact `--hold`
  writes (`tools/unattended/unattended.sh:7012`), passed as `held_from`. Observed by AC8.
- **S14** — id 27. `TOOL-dDeclaredLoop-52` S3's check admits `held-in` on the `HELD` row and refuses it on
  any other, and the map's `HELD` row is `state paused · step held-in`. Observed by AC8.
- **S15** — id 10. The trailer floor refuses only a requested key of `FLOOR_KEYS` the table lacks:
  `TOOL-dDeclaredLoop-40` §4's unconditional line reads "refuse any requested key in `FLOOR_KEYS` the table
  lacks". Observed by AC9.
- **S16** — id 11. The acceptance half is unarmed exactly when the `acceptance` row's `writer` equals the
  stand-in command, compared through one constant, `ACCEPTANCE_STAND_IN`, that `tools/loop/loop_witness.py`
  defines and `tools/loop/position.py` imports; any other value arms it. Observed by AC10.
- **S17** — id 18. The weighing `TOOL-dDeclaredLoop-62` records in `.gitattributes` is carried where an
  adopter reads it: `tools/loop/README.md`'s budget section names union, the 147-of-151 measurement, the
  row driver's refusal and the draw id. Observed by AC11.
- **S18** — id 24. `check_terminal_proof` on win32 asks
  `ctypes.windll.kernel32.GetConsoleMode(msvcrt.get_osfhandle(0), byref(DWORD()))` for a non-zero answer;
  a mintty session, whose stdin is a pipe, is refused as not a terminal and the refusal names
  `winpty` or a console as the route. Observed by AC12.
- **S19** — id 25. `TOOL-dDeclaredLoop-37`'s S1 probe excludes a parity block by marker range: each
  region from `# >>> commit_trailers_py` to `# <<< commit_trailers_py` is cut from every file before the
  pattern runs, and every other line of a carrier, `tools/runlog/model.py` included, stays graded.
  Observed by AC13.
- **S20** — id 47. No line is excluded for its content: a consumer line that names the reader beside its
  own parse is graded. Observed by AC13.
- **S21** — id 26. The `routed-commits selftest` row in `tools/gate-legs.json` gains the guards
  `{prefix}/unattended/` and `{prefix}/runlog/`, so an edit to `unattended.sh` alone selects the leg that
  hosts the class arm. Observed by AC14.
- **S22** — id 33. `tools/run-gates/regen.py`'s `run_command` and `run_tree_kill` (:249-301) are the named
  shape of the loop runner: it pops an inherited `PWD`, sets `GIT_OPTIONAL_LOCKS=0`, resolves bash as
  govkit does, and writes output to a file; its kill differs by S37, and the module header says so.
  Observed by AC15.
- **S23** — id 35. `check_transition_tables` joins `[[phase]]` rows over the driver's set: `PHASES_CORE`
  read as `TOOL-dDeclaredLoop-52` S3 reads it, and `PHASES_EXTRA` read by sourcing `.unattended.conf` in a
  bash subshell as `tools/unattended/check-unattended.sh:341-343` does; a row naming a phase in neither
  set is refused, and an extra phase needs no row. Observed by AC16.
- **S24** — id 36. The witness normaliser runs the existing program: the run-gates kit resolved by
  `resolve_kit_dir`, `lib-attribute.sh` sourced, `write_normaliser` (:40) written to a file and applied with
  `sed -E -f`; no Python copy and no `normalise_output` parity row is minted. Observed by AC17.
- **S25** — id 39. The `command:` actors `TOOL-dDeclaredLoop-50` and `-51` write into `tools/loop/loop.toml`
  use spec-9's verb form, as `item.plan.recommend` already does: `command:unattended.review`,
  `command:workflows.review-pin`, `command:workflows.tier2-review` and `command:unattended.recommend`.
  Observed by AC18.
- **S26** — id 40. `TOOL-dDeclaredLoop-1`'s pass at order 2 sees `govkit selftest` arms OC8 AC2 and RQ5
  AC1 (`tools/govkit/selftest.py:2723-2725`, :6976-6978) red until `TOOL-dDeclaredLoop-36`'s registry line
  at order 3, and records them owed to that unit; those two arms are the existing coverage
  `TOOL-dDeclaredLoop-36` S3 twins. Observed by AC19.
- **S27** — id 41. The default-plan pins at `tools/govkit/selftest.py:6857-6898` are re-measured with a
  default `plan` into a scratch target after loop joins the default, and either moved with a ladder comment
  naming `TOOL-dDeclaredLoop-36` or recorded unchanged beside the measured counts. Observed by AC19.
- **S28** — id 43. `KIT_RUN_GATES_VERSION` and the `gov:kit run-gates@` marker in
  `tools/run-gates/README.md` move together in one edit, and the README's key list names `stage`.
  Observed by AC20.
- **S29** — id 44. Each pass of units 41 to 52, 54 and 55 keeps green the sibling-minted loop leg that runs
  the file it edits, as the table under §4 lists; the leg is invisible to the base-manifest join, so its
  hands-off bullet to this unit names it. Observed by AC21.
- **S30** — id 45. Two leg rows join `tools/gate-legs.json` and `tools/loop/kit.toml`:
  `loop definition fixtures`, argv `python {prefix}/loop/loop_lib.py --fixture`, and `loop selftest`, argv
  `python {prefix}/loop/selftest.py`, so the arms of units 41, 50 and 54 run; unit 53's arm lives in
  `breakpoints.py --fixture`, matching its AC2. Observed by AC22.
- **S31** — id 46. The no-guard property of `loop termination` gets a lasting arm in
  `tools/run-gates/run-gates.gov.test.sh` modelled on :340-372, liveness first, and the matching descriptor
  assertion in `tools/govkit/selftest.py`. Observed by AC1.
- **S32** — id 54. The stage factory re-targets every build row whose `from` is the after-state and whose
  `to` is the state the exit row reached, refuses when one cannot be re-targeted unambiguously, and
  validates new tags, states and orders before writing. Observed by AC5.
- **S33** — id 61. For an all-zero old sha with no tracking tip, the pre-push policy arm grades the commits
  `git rev-list --full-history <tip> -- .governance/policy.toml` names, merges by
  `TOOL-dDeclaredLoop-59`'s key grade, and exits 0 when none touch the file. Observed by AC23.
- **S34** — id 62. The adopter route is stated, not shipped as a descriptor key, per §8 F2:
  `tools/loop/README.md`'s install section gives the line
  `<MEMORY_ROOT>/builds/*/build/*-transition-*.md merge=union`, and `budget.py` prints one notice per run
  when `git check-attr merge` on a transition record path answers anything else. Observed by AC11.
- **S35** — id 63. A patch draw on an origin is refused while another live run's claim names a patch build
  of the same origin: the driver reads live claims (`read_claims`, `tools/unattended/unattended.sh:2117`)
  and each claimed slug's `parents:`, and the refusal names the other run. Concurrent draws on one origin
  are serialized, the stated cross-worktree limit. Observed by AC24.
- **S36** — id 64. The criterion command's environment is the caller's with every `GIT_ENV_LEAKS` name
  unset (`tools/memory-tree/tree_lib.py:262`), carried inline as `TOOL-dDeclaredLoop-39` S2 carries it.
  Observed by AC15.
- **S37** — id 65. After every command, the runner kills the command's group before reading its output:
  `os.killpg` on POSIX, and on win32 a Job Object created with `KILL_ON_JOB_CLOSE` and closed, because
  `taskkill /T` after bash exits finds no orphan (`tools/process-monitor/reap.py:10-13`). Observed by AC25.
- **S38** — id 66. The factory's signal half has its own plant: a patched write raising
  `KeyboardInterrupt` between two writes restores every path; on win32 a forced kill runs no handler, and
  the next factory run reports any leftover temp or prior-bytes file by path. Observed by AC26.
- **S39** — id 12. The copies `TOOL-dDeclaredLoop-56` S19 and S20 move with their canonicals,
  `tools/loop/policy_edit.py`, `tools/playbook/instructions_edit.py` and the three `commit_trailers.py`
  copies, and its item factory `tools/loop/loop_items.py`, are held byte-identical where a parity row
  names them. Observed by AC27.
- **S40** — id 13. The comment above the S1 probe in `tools/memory-tree/routed_commits.py` says what S19
  does: the block region is cut, never the carrier file. Observed by AC13.
- **S41** — id 37. A carrier is never excluded wholesale: a scratch copy of `tools/runlog/model.py` with a
  banned literal outside its block is reported. Observed by AC13.
- **S42** — id 14. The dead citation `...-spec-audit-round1.md` in the Goal of specs 40 to 56 reads
  `memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`. Observed by AC28.
- **S43** — id 31. The same citation in the §9 lines of specs 4 to 8 is re-spelled the same way.
  Observed by AC28.
- **S44** — id 15. `TOOL-dDeclaredLoop-42` AC2's bound is a derivation, the 2 s timeout plus the 5 s second
  wait plus the worktree and kill overhead, never a pinned 10 s. Observed by AC29.
- **S45** — id 29. That overhead is measured once at this pass, three runs of AC2's command, and the
  bound written into the acceptance ledger as PINNED with its date. Observed by AC29.
- **S46** — id 16. `write_guarded(path, new_text, record)` keeps `TOOL-dDeclaredLoop-2`'s three-argument
  form, the record path and text derived from `record` inside. Observed by AC30.
- **S47** — id 49. Both callers, in `tools/loop/policy_edit.py` and `tools/playbook/instructions_edit.py`,
  call that form, so `TOOL-dDeclaredLoop-2`'s inventory row stays true. Observed by AC30.
- **S48** — id 28. The placement revision is the oldest adding commit:
  `git log --diff-filter=A --format=%H --reverse -- <path>`, its first line. Observed by AC31.
- **S49** — id 30. `TOOL-dDeclaredLoop-36` AC2 runs after that unit's commit, `--to` set to it; this
  pass re-runs it so. Observed by AC19.
- **S50** — id 48. `TOOL-dDeclaredLoop-7` §4's line grammar is amended to `unit — <id> · <step>[ ·
  acceptance unarmed]`, the `--json` row gains `acceptance_armed`, and the driver's `--plan` reader of the
  line in `tools/unattended/unattended.sh` reads the optional field. Observed by AC10.
- **S51** — id 50. `WIRE-INTO-PROJECT.md`'s loop section heading carries `(default)`, says `govkit apply`
  installs it and `update --write` adds it as `default-gained`, and the install tree gains a `(default)`
  line for the loop kit's directory. Observed by AC32.
- **S52** — id 60. A playbook `edges.toml` that does not parse, or a `[[trailer]]` row with no key, is a
  refusal at exit 2 naming the file and the parse error; the floor does not apply, because a broken table
  is not an absent one. Observed by AC9.
- **S53** — id 67. scratch-guard's policy arm admits only when the policy kit does not resolve; with the
  kit resolved and `guarded-paths.txt` missing or unparsable it denies writes to the known policy paths and
  names the list. Observed by AC33.
- **S54** — id 68. The class arm matches `-i -E 'trailers:[^)]*key=pass'` over code lines only, comment
  lines skipped, copies cut by S19's marker range, and is staged with a lowercase, reordered spelling.
  Observed by AC13.

## 3. Non-goals (OUT)

- Any high: units 57 to 66, one per id.
- The spec lints and checklist entries the report names as left-shifts: each would be a new gate no
  clause of this build names; the classes are recorded at the close.
- Re-reviewing any repaired unit: M4 forbids it.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — the roles requires that reds two govkit arms until order 3 (id 40)
- **consumes-from** `TOOL-dDeclaredLoop-33` — the `loop termination` leg row and AC10 (ids 2, 46)
- **consumes-from** `TOOL-dDeclaredLoop-36` — the default join, its AC2 and the pins it moves (ids 30, 40, 41)
- **consumes-from** `TOOL-dDeclaredLoop-37` — the trailer-parse class arm and its probe (ids 13, 25, 26, 37, 47, 68)
- **consumes-from** `TOOL-dDeclaredLoop-40` — the trailer floor and the edges table read (ids 10, 60)
- **consumes-from** `TOOL-dDeclaredLoop-41` — the actor-list arm in `loop_lib.py` (ids 44, 45)
- **consumes-from** `TOOL-dDeclaredLoop-42` — the bounded runner (ids 15, 29, 33, 44, 64, 65)
- **consumes-from** `TOOL-dDeclaredLoop-43` — `write_guarded` and its rollback fixtures (ids 7, 16, 20, 44, 49)
- **consumes-from** `TOOL-dDeclaredLoop-44` — the push-range arm (ids 44, 61)
- **consumes-from** `TOOL-dDeclaredLoop-45` — the acceptance-armed predicate and its line (ids 11, 44, 48)
- **consumes-from** `TOOL-dDeclaredLoop-46` — the `stage` claim and the run-gates version (ids 5, 21, 42, 43, 44)
- **consumes-from** `TOOL-dDeclaredLoop-47` — the stage factory (ids 6, 44, 54)
- **consumes-from** `TOOL-dDeclaredLoop-48` — the budget's homes (ids 8, 44, 63)
- **consumes-from** `TOOL-dDeclaredLoop-49` — the build-wide count and its attribute line (ids 8, 18, 44, 62)
- **consumes-from** `TOOL-dDeclaredLoop-50` — the review item rows (ids 39, 44, 45)
- **consumes-from** `TOOL-dDeclaredLoop-51` — the recommendation rows (ids 39, 44)
- **consumes-from** `TOOL-dDeclaredLoop-52` — the phase map and its check (ids 9, 27, 35, 44)
- **consumes-from** `TOOL-dDeclaredLoop-53` — the placement rule and its arm (ids 8, 28, 45)
- **consumes-from** `TOOL-dDeclaredLoop-54` — the per-level terminal arm (ids 44, 45)
- **consumes-from** `TOOL-dDeclaredLoop-55` — the guard-free termination row (ids 2, 44, 46)
- **consumes-from** `TOOL-dDeclaredLoop-56` — AC30, AC41, the terminal proof, the normaliser, the factory, the write-gate arm and the runbook section (ids 3, 4, 12, 22, 23, 24, 36, 50, 66, 67)
- **consumes-from** `TOOL-dDeclaredLoop-59` — the merge key grade the first-push walk applies (id 61)
- **consumes-from** `TOOL-dDeclaredLoop-60` — the resolved root of the budget reader (ids 8, 63)
- **consumes-from** `TOOL-dDeclaredLoop-62` — the transition-record driver and its weighing (ids 18, 62)
- **consumes-from** `TOOL-dDeclaredLoop-63` — the adopter-phase reading the check's population matches (id 35)
- **consumes-from** `TOOL-dDeclaredLoop-64` — the resolved root of the placement rule (ids 8, 28)
- **consumes-from** `TOOL-dDeclaredLoop-68` — the program-route normaliser and the absent `normalise_output` row, which S24 and AC17 read as landed at order 37 (the round-3 spec audit's id 1)
- **consumes-from** `TOOL-dDeclaredLoop-70` — the shared adopter-phase population, which S13's held-from lookup takes by passing no explicit `extra` (the round-3 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-71` — the `loop breakpoints fixtures` leg that runs AC31's plant, and the arm-home ruling that supersedes S30's sentence on unit 53 (the round-3 spec audit's id 28)
- **hands-off** `TOOL-dDeclaredLoop-75` — the guard, leg, claim, terminal-proof, conf-read, copy and citation items of the round-3 spec audit's minors (ids 6, 7, 10, 16, 20, 21, 26, 27, 30, 32, 38, 46)
- **hands-off** `TOOL-dDeclaredLoop-99` — S30's `loop definition fixtures` leg, which runs that unit's `conf-readers-declared` plant (the round-12 spec audit's id 19)

## 4. Design

### Evidence

Each item's evidence is its finding's row in the review record's appendix, each re-probed by a skeptic;
the code lines this spec cites were read at base `ed497191` on 2026-10-24, among them
`tools/run-gates/regen.py:249` and :270, `tools/memory-tree/tree_lib.py:262`,
`tools/run-gates/lib-attribute.sh:40`, `tools/govkit/selftest.py:6857-6898`,
`tools/process-monitor/reap.py:10-13`, `.githooks/pre-push:610`, :940 and :1166, and
`tools/unattended/unattended.sh:7012`.

### The loop legs S29 names

| Unit | Leg its pass keeps green | Minted by |
|---|---|---|
| 41, 50, 51 | `loop definition` | `TOOL-dDeclaredLoop-1` |
| 42 | `loop computed witness` | `TOOL-dDeclaredLoop-17` |
| 43, 44 | `loop guard fixtures` | `TOOL-dDeclaredLoop-2` |
| 45 | `loop position fixtures` | `TOOL-dDeclaredLoop-7` |
| 46 | `loop stage coverage` | `TOOL-dDeclaredLoop-4` |
| 47 | `loop factories fixtures` | `TOOL-dDeclaredLoop-6` |
| 48, 49 | `loop budget fixtures` | `TOOL-dDeclaredLoop-30` |
| 52, 54 | `loop transition tables` | `TOOL-dDeclaredLoop-13` |
| 54, 55 | `loop termination` | `TOOL-dDeclaredLoop-33` |

### Write set

This pass writes the tools below and, for S42 and S43, the named lines of specs 4 to 8 and 40 to 56 in
this build's folder. S2 to S5, S26, S29 and S49 observe or record and write no code.

### Files touched (estimate)

- `tools/loop/factories.py`
- `tools/loop/loop_table.py`
- `tools/loop/loop.toml`
- `tools/loop/loop_witness.py`
- `tools/loop/position.py`
- `tools/loop/budget.py`
- `tools/loop/guard.py`
- `tools/loop/breakpoints.py`
- `tools/loop/stage_coverage.py`
- `tools/loop/policy_edit.py`
- `tools/loop/kit.toml`
- `tools/loop/README.md`
- `tools/lib/guarded_write.py`
- `tools/lib/commit_trailers.py`
- `tools/playbook/instructions_edit.py`
- `tools/memory-tree/routed_commits.py`
- `tools/unattended/unattended.sh`
- `tools/hooks/scratch-guard.js`
- `tools/gate-legs.json`
- `tools/govkit/selftest.py`
- `tools/run-gates/run-gates.gov.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/README.md`
- `WIRE-INTO-PROJECT.md`
- `memory/builds/dDeclaredLoop/spec/`

### Alternatives rejected

- **One unit per minor.** M4 forbids it.
- **Two batch units.** The minors do not split into two disjoint write sets: `tools/gate-legs.json`,
  `tools/loop/kit.toml` and `tools/loop/README.md` are each written by items of every cluster.

## 5. Production-readiness checklist

- security — S53 closes a fail-open write gate, S18 a terminal-proof gap, S36 a git environment leak.
- perf / scale — S30 adds two fixture legs, seconds each; S37 adds a group kill per command.
- error / empty / loading states — S52 and S53 name the broken-input states; S33 the empty remote.
- observability — S34's notice; S35's refusal names the other run.
- risks — S9 renumbers later steps in one guarded write, restored on a red check by the factory contract.
- testing — AC1 to AC33 as probes and plants; the arms under §7, observed at the close.
- migration — none beyond S42 and S43's citation re-spelling.
- user docs — S51's runbook section and S17 and S34's loop README sections.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe loads `tools/gate-legs.json`, exactly one row is named
  `loop termination` and it has no `guard` key, and the arm §7 declares reds on a staged copy adding one.
  Red when: the row carries a guard, or the arm passes over two rows.
- **AC2** — When the anchored `git grep -nE` of S3 runs with S2's exclusions over the built tree, it prints
  nothing.
  Red when: a stale `tree_lib.py:27` citation remains.
  figure: PINNED, 14 files on today's tree, the red case.
- **AC3** — When a probe reads each statement at the four AC30 sites whole, each command string holds
  `--round-highs`.
  Red when: a site's command lacks the flag on a continuation line.
- **AC4** — When a probe parses every `tools/*/kit.toml` with `tomllib`, every `[[gate_leg]]` table's
  `stage` is a list, `stage_coverage.py` reads no regen row's integer, and the staging `regen.py` reads
  over the same descriptors equals its reading at base.
  Red when: a grep count over `stage =` is the observation, or a gate-leg row lacks the list.
- **AC5** — When `python factories.py new stage audit --after step.build` runs in a scratch copy, `step.test`
  and `step.deploy` read orders 5 and 6, and no build row leads from `building` to `testing`.
  Red when: two steps share order 4, or `item.build.resolve` still reaches `testing`.
- **AC6** — When `python guard.py --fixture --plant write-guarded-rollback` patches the second
  `os.replace` to raise, the policy file is restored byte for byte and no record exists.
  Red when: the fixture relies on directory permissions and the write succeeds on win32.
- **AC7** — When `grep -n "memory/builds" budget.py breakpoints.py` runs in `tools/loop/`, it prints
  nothing.
  Red when: a reader spells the literal root.
- **AC8** — When `python loop_table.py phase HELD --held-from BUILDING` runs, it prints
  `state paused · step step.build`, and a `held-in` step on a non-HELD row is refused by the check.
  Red when: HELD reads `none`.
- **AC9** — When `python commit_trailers.py --fixture --plant table-lacks-policy` serves a `Pass` read, it
  succeeds, and `--plant malformed-edges` exits 2 naming `edges.toml`.
  Red when: a missing floor key refuses every read, or a parse error escapes as a traceback.
- **AC10** — When `python position.py --fixture --plant writer-unexpected` names an unexpected writer, the
  unit reads armed, and `--json` carries `acceptance_armed`.
  Red when: arming compares an unnamed field.
- **AC11** — When `grep -n "147 of 151" README.md` runs in `tools/loop/`, it prints a line, and `python budget.py
  --fixture --plant attr-missing` prints the notice naming the union line once.
  Red when: an adopter has no stated route.
- **AC12** — When `check_terminal_proof` runs on win32 with stdin from `NUL`, it refuses.
  Red when: `os.isatty` alone admits `NUL`.
- **AC13** — When `python routed_commits.py --selftest` runs over scratch copies holding a lowercase
  reordered `trailers:valueonly,key=pass` in code, a banned literal outside the block of `model.py`, and the
  canonical block inlined in `model.py`, the first two are reported and the third is not.
  Red when: the filter works by line content.
- **AC14** — When a probe joins `tools/unattended/unattended.sh` to `tools/gate-legs.json`'s guards, the
  `routed-commits selftest` row is among the rows it trips.
  Red when: the guard misses the scanned files.
- **AC15** — When `python loop_witness.py --fixture --plant leak-env` exports `GIT_DIR` and `GIT_INDEX_FILE`
  at the caller, the criterion's `git rev-parse --show-toplevel` prints the worktree, and its environment
  holds `GIT_OPTIONAL_LOCKS=0` and no inherited `PWD`.
  Red when: the command inherits the caller's git.
- **AC16** — When `python loop_table.py check` runs over a scratch conf with `PHASES_EXTRA="STAGING"`, it
  passes with no `STAGING` row and refuses a row naming `NOPHASE`.
  Red when: the check joins over `PHASES_CORE` alone.
- **AC17** — When `python loop_witness.py --fixture --plant normalise` hashes two runs differing only in a
  scratch root and a duration, the hashes agree, and
  `git grep -c normalise_output -- tools/lib/resolve-python.test.sh` prints nothing.
  Red when: a Python copy of the normaliser ships.
- **AC18** — When `grep -n "command:tools/" loop.toml` runs in `tools/loop/`, it prints nothing, and every
  `command:` actor there reads `command:<kit>.<verb>`.
  Red when: a gov-prefix actor ships.
- **AC19** — When a default `python tools/govkit/govkit.py plan` into a scratch target runs after unit 36's
  commit, its counts equal the pins at `tools/govkit/selftest.py:6857-6898`, and unit 36's AC2 run with
  `--to` that commit prints
  `default-gained loop`.
  Red when: a pin is unmeasured, or AC2 runs against the working tree.
- **AC20** — When `grep -h "gov:kit run-gates@" tools/run-gates/run-gates.sh tools/run-gates/README.md`
  runs, both files print one version.
  Red when: the version moved in one file.
- **AC21** — When a probe reads the `### Edges` block of specs 41 to 52, 54 and 55, each `**hands-off**`
  bullet to this unit names the loop leg §4's table lists for that unit.
  Red when: a pass has no named leg.
- **AC22** — When `python loop_lib.py --fixture` runs in a scratch copy of `tools/loop/` with one plant
  deleted, it exits non-zero, and a `python -c` probe loading `tools/gate-legs.json` finds the rows
  `loop definition fixtures` and `loop selftest`, the first's argv ending in `loop_lib.py --fixture` and the
  second's in the loop kit's self-test file, whose own plant-deleted red is the arm §7 declares.
  Red when: an arm is reachable by no leg row.
- **AC23** — When `python guard.py --fixture --plant push-first-to-empty-remote` runs, it exits 0, and with a
  merge-resolution edit to the policy file it exits 1.
  Red when: a first push of the default branch exits 2.
- **AC24** — When `python budget.py --fixture --plant patch-concurrent` draws for a second patch run of one
  origin under a live claim of the first, the draw is refused naming the first run.
  Red when: both draws land and overdraw the origin.
- **AC25** — When `--plant exit0-grandchild` runs `sleep 600 & exit 0`, no survivor remains on POSIX, and on
  win32 none remains or a named `leaked` path is printed.
  Red when: the group is killed only on timeout.
- **AC26** — When `python factories.py --fixture --plant factory-interrupt` raises `KeyboardInterrupt` between
  two writes, every path is restored.
  Red when: only a red gate triggers the restore.
- **AC27** — When a probe compares each marker block of `guarded_write_py` and `commit_trailers_py` across
  its canonical and copies, every block is byte-identical.
  Red when: a copy is stale.
- **AC28** — When `git grep -c "spec-audit-round1" -- memory/builds/dDeclaredLoop/spec/` runs, it prints
  only `TOOL-dDeclaredLoop-67`'s own file.
  Red when: a spec still cites the dead path.
- **AC29** — When unit 42's AC2, `python loop_witness.py --selftest --plant timeout-grandchild`, runs three
  times in `tools/loop/`, each run's wall time is under the derived bound, and
  `grep -n "PINNED" memory/builds/dDeclaredLoop/build/*-TOOL-dDeclaredLoop-67-*-acceptance-ledger.md` prints
  the bound with its date.
  Red when: the bound is a typed 10 s with no measurement.
- **AC30** — When `python -c` prints `inspect.signature(write_guarded)` from `guarded_write.py`, it shows
  `(path, new_text, record)`, and both callers pass three arguments.
  Red when: the four-argument sketch ships.
- **AC31** — When `python breakpoints.py --fixture --plant readded` re-adds `breakpoints.py` after deleting
  it, the placement is the first add.
  Red when: the newest add is taken.
- **AC32** — When `grep -n "(default)" WIRE-INTO-PROJECT.md` runs, it prints the loop section heading and a
  loop tree line.
  Red when: the runbook never marks loop as a default kit.
- **AC33** — When scratch-guard's policy arm runs with the policy kit present and `guarded-paths.txt`
  missing, an Edit to the policy file is denied naming the list.
  Red when: the missing list admits the write.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `playbook render selftest` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `routed-commits selftest` · `install-prefix (shipped surface)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC1 · a loop termination row that must exist exactly once and carry no guard, staged by adding one · none
New arm: tools/govkit/selftest.py · covers AC1 AC19 · the loop descriptor's termination claim carries no guard, and the default-plan pins re-measured, each staged against a copy · none
New arm: tools/memory-tree/routed_commits.py · covers AC13 · the marker-range strip and the case-insensitive pattern, staged by a lowercase reordered spelling · none
New arm: tools/loop/factories.py · covers AC5 AC26 · the derived order, the class re-target and the interrupt plant, each staged against the base factory · none
New arm: tools/loop/loop_witness.py · covers AC15 AC17 AC25 · the env-leak, normaliser and grandchild plants · none
New arm: tools/loop/selftest.py · covers AC22 · the loop kit's self-test, reachable by the `loop selftest` leg row, staged by deleting one plant in a scratch copy of tools/loop/ · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — How does the transition-record rule reach adopters (id 62)?** Options: (a) a govkit descriptor
  key carrying a merge driver for a pattern, which the skeptic's fix names; (b) the stated adopter route
  with a notice. (a) mints a descriptor key, a public surface no clause of this build names, and veto 2
  discards it; with no delegated resolver for it, (b) survives. RESOLVED (agent, 2026-10-24, delegated):
  (b), S34. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-2 spec audit's 54 minors batched (38 MEDIUM, 16 LOW).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-68 and TOOL-dDeclaredLoop-70 and TOOL-dDeclaredLoop-71 and TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-99, written by the round-12 spec audit's disposal; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, never a parallel copy: regen's runner (S22), the
`GIT_ENV_LEAKS` class (S36), lib-attribute's normaliser run in place (S24), the driver's `held-from` fact
(S13), its claim reader (S35), and the precedent arm at `run-gates.gov.test.sh:340-372` (S31).
`python tools/codebase-map/reuse_lookup.py "read every run-state record including rotated archives"`
and `"adopter phase vocabulary extension PHASES_EXTRA"` ranked the driver's `phases` and the runlog
readers, read above; no new reader is minted where one of these exists.

Recall terms used: spec audit minors batch stage factory phase map trailer floor bounded runner normaliser guard parity
