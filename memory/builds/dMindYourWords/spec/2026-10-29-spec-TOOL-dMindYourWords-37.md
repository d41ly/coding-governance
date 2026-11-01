# TOOL-dMindYourWords-37 — the audit of units 22 to 29: its 31 minors, batched — fixtures that reach their branch, observations that read what they claim, and the readers a move or a merge left behind

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-37-deviation-371.md](../build/2026-10-29-build-TOOL-dMindYourWords-37-deviation-371.md) | deviation | — |
| [2026-10-29-prompt-TOOL-dMindYourWords-34-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-34-promoted-fix-brief.md) | research | TOOL-dMindYourWords-34 |
| [2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-34 TOOL-dMindYourWords-30 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-35 TOOL-dMindYourWords-31 TOOL-dMindYourWords-36 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 29
(`memory/builds/dMindYourWords/reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`)
confirmed 38 findings; its seven highs are units 30 to 36. This unit is BUILD-METHOD M4's batch of its 22
MEDIUM and 9 LOW by raw id, one scope item per id, ids sharing a report item taking that item's
severity. They land on units 13, 14, 15, 17 and 22 to 29 and on units 31 and 36, so the batch repairs no
unit in particular and builds last, at order 21, above every unit of the build.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2, 3, 13, 34 | S1, S2, S3, S4 |
| M2 | MEDIUM | 4, 24 | S5, S6 |
| M3 | MEDIUM | 5 | S7 |
| M4 | MEDIUM | 6 | S8 |
| M5 | MEDIUM | 7 | S9 |
| M6 | MEDIUM | 8 | S10 |
| M7 | MEDIUM | 9, 14 | S11, S12 |
| M8 | MEDIUM | 15, 32 | S13, S14 |
| M9 | MEDIUM | 25 | S15 |
| M10 | MEDIUM | 31 | S16 |
| M11 | MEDIUM | 33 | S17 |
| M12 | MEDIUM | 36 | S18 |
| M13 | MEDIUM | 37 | S19 |
| M14 | MEDIUM | 38 | S20 |
| M15 | MEDIUM | 39 | S21 |
| M16 | MEDIUM | 40 | S22 |
| L1 | LOW | 10, 16, 27 | S23, S24, S25 |
| L2 | LOW | 19 | S26 |
| L3 | LOW | 20 | S27 |
| L4 | LOW | 26, 41 | S28, S29 |
| L5 | LOW | 28 | S30 |
| L6 | LOW | 29 | S31 |

## 2. Scope (IN)

- **S1** — id 2, item M1, landing on unit 28. The shallow arm of unit 28's provenance fixture in
  `tools/lexicon/selftest.py` builds its clone with S3's helper, so `cannot judge provenance — shallow
  history` is reached. Observed by AC1.
- **S2** — id 3, item M1, landing on unit 29. The shallow arms of unit 29 AC24, the moved rate's `dead
  probe:` case, and AC27, the drift blame's `drift not measured — shallow history`, build their clones
  with S3's helper. Observed by AC2.
- **S3** — id 13, item M1, landing on units 28 and 29. One helper, `build_shallow_clone(src, dst)` in
  `tools/lexicon/selftest.py`, runs `git clone -q --depth 1 --no-local "file://<src>" <dst>` with `src`
  absolute and its backslashes turned to forward slashes, the spelling drift-audit's selftest already uses
  (`tools/drift-audit/selftest.py:1318`); a local-path `--depth` clone is not shallow. Observed by AC3.
- **S4** — id 34, item M1, landing on units 28 and 29. The helper asserts `git -C <dst> rev-parse
  --is-shallow-repository` prints `true` before it returns and raises otherwise, so no shallow arm judges
  a full history, and no other `--depth` clone is spelled in the kit's selftest. Observed by AC4.
- **S5** — id 4, item M2, landing on unit 29. Unit 29 S33's guard and `doc_reads` are observed on the
  rendered manifest in its rendered form: the `lexicon drift signals` row of `tools/gate-legs.json`
  carries `memory/builds/` in both, since the render resolves `{memory_root}`. Observed by AC5.
- **S6** — id 24, item M2, landing on unit 29. The source form is observed where it is written: the
  `lexicon drift signals` `[[gate_leg]]` of `tools/lexicon/kit.toml` carries `{memory_root}/builds/` in
  `guard` and in `doc_reads`. Observed by AC6.
- **S7** — id 5, item M3, landing on unit 23. Unit 23 AC1, the drain edit leaving the home unchanged, is
  observed at this pass, after unit 29 S1 routes the tally lines to stderr and unit 29 S11 sets LF, so
  the redirected home holds rows only. Observed by AC7.
- **S8** — id 6, item M4, landing on units 14 and 27. The three accessor rows unit 14 drains are drained
  from the root home unit 27 moved the ledger to, and no file remains at the old path; a row 14's pass
  took out of the old path is taken out of `.lexicon-debt.txt` here. Observed by AC8.
- **S9** — id 7, item M5, landing on units 13, 15 and 27. Every reader unit 27 S2's Readers line left
  out reads the root home: unit 15 AC6's counts are taken over `.lexicon-debt.txt`, the tag rows unit 13
  seeds sit there, and no shipped file or map dossier spells `memory/project/lexicon-debt`. Observed by
  AC9.
- **S10** — id 8, item M6, landing on units 17 and 25. Unit 17's settle-case observation is taken at the
  close, after unit 25 re-points `:10702` and `:10717`, declared on this unit's `New arm:` line so the main
  loop observes it with both units built; no `attended` assertion remains in that case. Observed by
  AC10.
- **S11** — id 9, item M7, landing on units 22 and 26. One helper, `build_compare_base_fixture(tmp)` in
  `tools/lexicon/selftest.py`, builds a bare origin and a clone: the base commit pushed to `origin/main`,
  `refs/remotes/origin/main` and `origin/HEAD` set and fetched, and the branch cut from it, so the
  merge-base is a proper ancestor of `HEAD`. Unit 26's arm and unit 22 AC4's base case build on it.
  Observed by AC11.
- **S12** — id 14, item M7, landing on units 22 and 26. Every child process the helper's arms spawn runs
  with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` cleared from its environment, as
  `tools/codebase-map/selftest.py:1596-1598` does, and each arm asserts the base line names a resolved
  base before it judges. Observed by AC12.
- **S13** — id 15, item M8, landing on unit 22. `registry_rel` is `(resolve_kit_dir("playbook",
  "namespaces.toml", KIT_DIR) / "namespaces.toml").relative_to(root).as_posix()`, so it equals a row's
  forward-slash `path` on every node. Observed by AC13.
- **S14** — id 32, item M8, landing on unit 22. A registry that resolves outside the graded root makes
  `registry_rel` `None`, never a `ValueError`, so every row is `corpus` there. Observed by AC14.
- **S15** — id 25, item M9, landing on units 22 to 29. Wherever a pass of this build left a kit's version
  constant moved, every carrier of that version agrees with it at this pass: the `gov:kit lexicon@`
  markers of `tools/lexicon/lexicon.py`, `tools/lexicon/canon.py`, `tools/lexicon/README.md` and
  `tools/lexicon/LEXICON.md` (`tools/check-kit-versions.sh:383-388`) and the rendered
  `.claude/skills/lexicon/SKILL.md`, re-rendered by the kit's own wiring, and for memory-tree every marker
  the block at `tools/check-kit-versions.sh:248-280` reads. Where no pass moved a constant, nothing moves,
  since a branch owes no bump (`tools/push-main.sh:26-31`). Observed by AC15.
- **S16** — id 31, item M10, landing on unit 22. The corpus walk never extracts a definition from the
  file at `registry_rel`, whatever `LANGS` arms, so no corpus row can carry the registry's path and the
  path alone decides the slice; `--list` names the skipped file. Observed by AC16.
- **S17** — id 33, item M11, landing on unit 26. `read_branch_added_paths(root, base)` lists the paths
  the branch's own first-parent commits add, `git log --first-parent --no-merges -M --diff-filter=A
  --name-status -z --format= <base>..HEAD`, so a default-branch record merged into the branch over a
  stale base is not this branch's addition. Observed by AC17.
- **S18** — id 36, item M12, landing on units 29 and 36. The contract-record walk asks
  `check_shallow_history` (S27) first and reds `cannot judge contract records — shallow history`; a true
  root commit is compared with an empty row set. Observed by AC18.
- **S19** — id 37, item M13, landing on units 22, 23 and 29. When drift is not measured, `check_debt_pin`
  holds the rows whose `rule` is `drift`, counted in unit 22 S3's held count and never compared, and
  `--measure` carries them unchanged with unit 23 S3's stderr count. Observed by AC19.
- **S20** — id 38, item M14, landing on unit 29. The requirements reader follows `-r` through a visited
  set of resolved paths, resolves each target against the including file, and reads it only when the
  normalised path lies inside the repository root and is tracked; a URL, an untracked target or one
  outside the root prints `manifest not read: <path>`, and a literal `..` is not refused by itself.
  Observed by AC20.
- **S21** — id 39, item M15, landing on units 24 and 29. The `lexicon selftest` row of
  `tools/gate-legs.json`, gov's own leg (`tools/govkit/registry.toml:578-580`), guards `{prefix}/policy/`
  and `{prefix}/memory-tree/build_records.py` beside `{prefix}/lexicon/`, the sibling scripts its arms
  run. Observed by AC21.
- **S22** — id 40, item M16, landing on unit 29. `read_vocabulary_record`'s delegate read separates three
  outcomes: the refusal code means no record; a delegate not found, a crash or any other exit reds
  `cannot read vocabulary records — <why>`, naming the interpreter and the three places the locator
  looked. Observed by AC22.
- **S23** — id 10, item L1, landing on unit 29. Unit 29 AC46's second half is observed with `grep -c`,
  which prints `0` on no match. Observed by AC23.
- **S24** — id 16, item L1, landing on units 24 and 29. Unit 24 AC3's and unit 29 AC19's counts are
  observed with `git grep -h -c`, which prints the bare count. Observed by AC24.
- **S25** — id 27, item L1, landing on unit 29. Unit 29 AC42's count is observed with `git grep -h -c`.
  Observed by AC25.
- **S26** — id 19, item L2, landing on unit 26. One `-z` name-status parser, `parse_name_status_z(out)` in
  `tools/lexicon/lexicon.py`, serves unit 9's `read_rename_map` and S17's added set, each reader keeping
  its own git command and tip. Observed by AC26.
- **S27** — id 20, item L3, landing on units 28, 29 and 31. One shallow probe, `check_shallow_history(root)`,
  is the only spelling of `--is-shallow-repository` in `tools/lexicon/lexicon.py`; `read_blame_lines`
  calls it and raises `HistoryRefusal`, which each caller prints in its own words, and unit 28 S1 and unit
  29 S27 drop their own spellings. Observed by AC27.
  **Readers:** by name: READER NOT IN TREE — the per-caller probes are minted by TOOL-dMindYourWords-28
  and -29 in this build, and no tracked file under `tools/lexicon/` spells `is-shallow-repository` at
  base ccd1292e · by value: NO VALUE READERS — the probe's answer is consumed where it is read, and no
  other code compares or stores it.
- **S28** — id 26, item L4, landing on unit 25. The comment opening the settle block of
  `tools/unattended/check-unattended.test.sh` (`:6168-6169` at base) names the `owner` population.
  Observed by AC28.
- **S29** — id 41, item L4, landing on unit 25. In that block, from its opening comment to the
  `missing [units-at-landing]` assertion, the one word `attended` left is the kept legacy record
  `landed-by: attended`. Observed by AC29.
- **S30** — id 28, item L5, landing on unit 29. The generated ask view `memory/backlog/TOOL.md` is
  regenerated with `python tools/memory-tree/gen_build_index.py --write` after unit 29 S20 and S46 write
  their ask rows. Observed by AC30.
- **S31** — id 29, item L6, landing on unit 27. Step 4 of the removal order in `tools/lexicon/README.md`
  (`:738` at base) names `.lexicon-debt.txt` beside `.lexicon.conf` as a file the uninstall takes out.
  Observed by AC31.

## 3. Non-goals (OUT)

- Any high: units 30 to 36, one per id.
- The left-shift lints, idiom bans and checklist entries the report names: each is a gate, its own unit
  (BUILD-METHOD M2), and no clause of this build names one; S3, S4, S11 and S12 are helpers the arms use,
  not gates over other code.
- Re-wording a repaired unit's spec (M4): each item is built and observed at this pass, and a repaired
  unit whose own criterion cannot pass at its pass meets it through M2's AMEND route at build time.

### Edges

- **consumes-from** `TOOL-dMindYourWords-13` — the tag rows its Migration seeds into the root home (id 7)
- **consumes-from** `TOOL-dMindYourWords-14` — the three accessor rows it drains (id 6)
- **consumes-from** `TOOL-dMindYourWords-15` — S7's rows and AC6's counts over the ledger (id 7)
- **consumes-from** `TOOL-dMindYourWords-17` — the settle case and its rename to `owner` (id 8)
- **consumes-from** `TOOL-dMindYourWords-22` — `derive_ledger_slice`, `registry_rel`, the held count and AC4's base case (ids 9, 14, 15, 31, 32, 37)
- **consumes-from** `TOOL-dMindYourWords-23` — the `--measure` carry and AC1's drain edit (ids 5, 37)
- **consumes-from** `TOOL-dMindYourWords-24` — the policy locator its arm exercises and AC3's count (ids 16, 39)
- **consumes-from** `TOOL-dMindYourWords-25` — the re-pointed settle-case lines and the `check-unattended.test.sh` block (ids 8, 26, 41)
- **consumes-from** `TOOL-dMindYourWords-26` — `read_branch_added_paths` and its fixture (ids 9, 14, 19, 33)
- **consumes-from** `TOOL-dMindYourWords-27` — the root home, its Readers line and the kit README's ledger section (ids 6, 7, 29)
- **consumes-from** `TOOL-dMindYourWords-28` — the provenance shallow arm and its fixture (ids 2, 13, 20, 34)
- **consumes-from** `TOOL-dMindYourWords-29` — S1, S11, S18, S19, S20, S24, S27, S29, S33, S42, S46 and their criteria (ids 3, 4, 5, 10, 16, 20, 24, 27, 28, 36, 37, 38, 39, 40)
- **consumes-from** `TOOL-dMindYourWords-31` — `read_blame_lines` under the kit's one pin, inside which S27 moves the shallow probe (id 20)
- **consumes-from** `TOOL-dMindYourWords-35` — the redirect-safe drain edit S7 and S19 run (ids 5, 37)
- **consumes-from** `TOOL-dMindYourWords-36` — the merge-visiting contract walk S18 bounds (id 36)
- **hands-off** `TOOL-dMindYourWords-49` — S17's first-parent form of `read_branch_added_paths`, which that unit moves onto the pinned runner (review id 22)
- **hands-off** `TOOL-dMindYourWords-52` — S9, S15, S17, S20, S21, S27 and AC7, which the round-2 audit's minors batch repairs (review ids 5, 12, 13, 14, 20, 27, 28, 36, 37)

## 4. Design

### Why one unit and not two

M4 admits two batches only when the minors split into two disjoint write sets by M6. S10, S28 and S29
touch only the two unattended suites, and every other item meets `tools/lexicon/selftest.py`,
`tools/lexicon/lexicon.py` or a lexicon carrier. The split is permitted and never required, and the
suite half is three line edits at one order, so a second unit buys one short concurrent pass for a
second spec, its edges and its audit (§8 F1).

### Evidence

- A local-path `git clone --depth 1` printed `warning: --depth is ignored in local clones; use file://
  instead.` and `--is-shallow-repository` read `false`; the `file://` form read `true` (the report's ids
  2, 13 and 34, reproduced in its record). drift-audit's selftest spells the working form at
  `tools/drift-audit/selftest.py:1318`.
- `tools/gate-legs.json` resolves `{memory_root}` in `doc_reads` (`"doc_reads": ["memory/builds/"]` on
  the lexicon rows) and keeps `{prefix}` in `guard`; the `lexicon selftest` row guards only
  `{prefix}/lexicon/` (`tools/gate-legs.json:1478-1490`), and the leg is gov's own, an `exempt_leg`
  (`tools/govkit/registry.toml:578-580`), so its guard is written in the manifest.
- `resolve_compare_base` returns no base without a resolvable remote and a fetched
  `refs/remotes/<remote>/<branch>` (`tools/lib/compare_base.py:36-44`); `tools/lexicon/selftest.py`
  never clears `GOV_REMOTE`, and `tools/codebase-map/selftest.py:1596-1598` does.
- Measured on git 2.54.0 in a fixture under `%TEMP%`: with a default-branch commit adding `rec.md` merged
  into a feature branch, `git log --first-parent --no-merges --diff-filter=A --name-only <base>..HEAD`
  printed only the feature's own path, while `--no-merges` alone and `--ancestry-path` also printed
  `rec.md` (the report's id 33, skeptic's probe).
- `tools/check-kit-versions.sh:383-388` requires `gov:kit lexicon@<V>` in four files; the Skill render
  carries `lexicon@1.24` (`.claude/skills/lexicon/SKILL.md:6`); `tools/push-main.sh:26-31` mints versions
  at landing.
- `tools/unattended/check-unattended.test.sh:6168-6169` reads "a settled hand-off is counted in the
  `attended` / population"; `:6172` writes `landed-by: attended`, the legacy record kept on purpose.
- The removal order's only deletion is step 4, `Delete .lexicon.conf` (`tools/lexicon/README.md:738`).
- `memory/backlog/TOOL.md:174` lists TOOL-aMendedFleet-96 `OPEN`, and the file is generated by
  `tools/memory-tree/gen_build_index.py --write`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `build_shallow_clone` | function, `tools/lexicon/selftest.py` | `py.function`, asked: OK |
| `build_compare_base_fixture` | function, `tools/lexicon/selftest.py` | `py.function`, asked: OK |
| `check_shallow_history` | function, `tools/lexicon/lexicon.py` | `py.function`, asked: OK, the canon's `check` for a predicate |
| `HistoryRefusal` | exception type, `tools/lexicon/lexicon.py` | `py.type`, asked: OK |
| `parse_name_status_z` | function, `tools/lexicon/lexicon.py` | `py.function`, asked: OK |
| `cannot judge contract records`, `cannot read vocabulary records` | refusal lines | none |

### Migration

None beyond S8's removal of any accessor row left in the root home; every other item edits code, docs,
a fixture or a generated view.

### Rollout

Live at landing, the last unit of the build, so the merge bar at the close grades the repaired tree once.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S13, S14, S16, S17, S18, S19, S22, S26, S27
- `tools/lexicon/lexicon_conf.py`: S22
- `tools/lexicon/pack.py` and `tools/lexicon/stack_census.py`: S20
- `tools/lexicon/selftest.py`: S1 to S4, S11, S12 and the arms of §7
- `tools/lexicon/kit.toml` and `tools/gate-legs.json`: S5, S6, S21
- `tools/lexicon/canon.py`, `tools/lexicon/LEXICON.md` and `.claude/skills/lexicon/SKILL.md`: S15
- `tools/lexicon/README.md`: S15, S31
- `.lexicon-debt.txt`: S8, S9
- `tools/unattended/check-unattended.test.sh`: S28, S29
- `tools/unattended/unattended.test.sh`: S10
- `memory/backlog/TOOL.md`: S30

### Alternatives rejected

- **One unit per minor**: M4 forbids it.
- **Folding each fix into the repaired unit's spec**: the audit's exit folds none (M4).
- **Reverting every branch version move to the base value** (S15): it contradicts unit 29 AC35, which
  observes units 4 and 6 moving the lexicon version; agreeing the carriers with whatever the branch
  holds satisfies both that criterion and the markers leg.

## 5. Production-readiness checklist

- security — S20 bounds a read surface to tracked files inside the root; S22 turns a dead delegate from a
  misdiagnosis into a named refusal; no new write path beyond the generated view S30 regenerates.
- perf / scale — S17's walk is linear in the branch's own commits; every other item is linear in what it
  reads.
- error / empty / loading states — S4, S14, S18, S19, S20 and S22 each name a state a repaired unit left
  undefined.
- observability — every new refusal names its cause and its file.
- risks — the fixtures of S1 to S4 and S11 to S12 change what earlier arms stage; each arm asserts its
  precondition (shallow, base resolved) before judging, so a fixture that misses its branch reds.
- testing — AC1 to AC31 and the arms of §7.
- migration — S8.
- user docs — `tools/lexicon/README.md` (S31).

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in `build_shallow_clone`'s clone of unit 28's provenance
  fixture, it exits 1 printing `cannot judge provenance — shallow history`.
  Red when: the clone is a full history and the row is judged.
  fixture: the fixture and its clone under `%TEMP%/<short>`.
- **AC2** — When `python lexicon_signals.py` and `python <kit>/lexicon.py` run in `build_shallow_clone`'s
  clones of unit 16's signals fixture and unit 10's drift fixture, they print the rate's `dead probe:`
  line and `drift not measured — shallow history`.
  Red when: either clone is a full history and its shallow arm is never entered.
- **AC3** — When `git grep -n -e "'--depth'" -e '--depth 1' -- tools/lexicon/selftest.py` runs, every hit
  sits inside `build_shallow_clone`, and that body spells `--no-local` and `file://`.
  Red when: a shallow arm spells its own local-path clone.
- **AC4** — When `build_shallow_clone` is called on a fixture with `file://` cut from its argv, it raises
  naming `is-shallow-repository`.
  Red when: the helper returns a full clone to an arm that judges it as shallow.
- **AC5** — When `python -c "import json; l = [x for x in json.load(open('tools/gate-legs.json')) if
  x['name'] == 'lexicon drift signals'][0]; print('memory/builds/' in l['guard'], 'memory/builds/' in
  l.get('doc_reads', []))"` runs, it prints `True True`.
  Red when: a records-only push skips the leg.
- **AC6** — When `python -c` loads `tools/lexicon/kit.toml` with `tomllib` and prints whether
  `{memory_root}/builds/` is in the `lexicon drift signals` row's `guard` and `doc_reads`, it prints
  `True True`.
  Red when: the source row and its render disagree.
- **AC7** — When `python tools/lexicon/lexicon.py --measure > .lexicon-debt.txt` runs at the pass, `git
  diff --exit-code -- .lexicon-debt.txt` exits 0 and `grep -c '^lexicon:' .lexicon-debt.txt` prints 0.
  Red when: a tally line or a carriage return reaches the home the drain edit writes.
- **AC8** — When `git ls-files -- 'memory/*/lexicon-debt.txt'` runs, it prints nothing, and `python
  tools/lexicon/lexicon.py 2>&1 | grep -c 'drained'` prints 0.
  Red when: an accessor row survives in the root home, so the corpus run prints it drained.
- **AC9** — When `git grep -n 'memory/project/lexicon-debt' -- tools .gitattributes WIRE-INTO-PROJECT.md
  help memory/map` runs, it prints nothing; `grep -cE 'py\.(file|constant)\.conv' .lexicon-debt.txt`
  prints the count `python tools/lexicon/lexicon.py` prints for those two rows; and `grep -c
  'namespaces.toml' .lexicon-debt.txt` prints a nonzero count.
  Red when: a reader still names the old home, or a unit's rows sit outside the root home.
- **AC10** — When `grep -cE 'phase LANDED \(attended\)|"attended LANDED 1"'
  tools/unattended/unattended.test.sh` runs, it prints 0.
  Red when: the settle case still asserts the old population while unit 17's writer prints `owner`.
- **AC11** — When `build_compare_base_fixture` builds its fixture, `git -C <clone> rev-parse
  refs/remotes/origin/main` prints the base commit and `git -C <clone> merge-base HEAD origin/main`
  prints it too, a proper ancestor of `HEAD`; unit 26 AC1's case then exits 1 naming `record not added
  by this branch`.
  Red when: the fixture has no remote and the admission is never asked.
  fixture: the bare origin and its clone under `%TEMP%/<short>`.
- **AC12** — When AC11's case runs with `GOV_REMOTE=nosuch` exported in the calling shell, the run names a
  resolved base and exits 1 as before.
  Red when: the ambient variable reaches the child and the base half drops out.
- **AC13** — When unit 22 AC1's fixture runs `python <kit>/lexicon.py` on a Windows node, it prints
  `1 row(s) held for the other slice`.
  Red when: `registry_rel` carries backslashes and the tag row reads as `corpus`.
- **AC14** — When a fixture places the lexicon kit so the registry probe resolves outside the repository
  root, the corpus run prints `0 row(s) held` and no `ValueError`.
  Red when: `relative_to` raises out of the slice predicate.
- **AC15** — When `git grep -h -o 'gov:kit lexicon@[0-9.]*' -- tools/lexicon/lexicon.py
  tools/lexicon/canon.py tools/lexicon/README.md tools/lexicon/LEXICON.md .claude/skills/lexicon/SKILL.md
  | sort -u` runs, it prints one line whose version equals `KIT_LEXICON_VERSION` in `lexicon.py`; and
  `git grep -h -o 'gov:kit memory-tree@[0-9.]*' -- memory/TEMPLATE-SPEC.md
  tools/memory-tree/check-memory-hygiene.sh | sort -u` prints one line equal to
  `KIT_MEMORY_TREE_VERSION`.
  Red when: a constant moved without its carriers.
- **AC16** — When a fixture arms `toml` in its `LANGS` and plants a corpus `verb` offender inside its
  `namespaces.toml`, `python <kit>/lexicon.py --offenders` prints no key with that path, and `--list`
  names the file as skipped.
  Red when: a corpus row carries the registry path and reads as `tags`.
- **AC17** — When a fixture branch from `build_compare_base_fixture` merges a default-branch commit that
  adds a vocabulary record, while `origin/main` stays at the pre-merge tip, and cites that record in a
  `widened:<record>` row, `python <kit>/lexicon.py` exits 1 naming `record not added by this branch`.
  Red when: a record another branch added reads as this branch's.
- **AC18** — When `python <kit>/lexicon.py` runs in `build_shallow_clone`'s clone of a fixture holding
  `CONTRACTS:` rows, it exits 1 printing `cannot judge contract records — shallow history`; in a full
  fixture whose root commit adds a row and its record, it exits 0.
  Red when: a shallow boundary reds every row or passes unexamined.
- **AC19** — When `python <kit>/lexicon.py` runs in `build_shallow_clone`'s clone of a fixture whose
  ledger holds a `drift` row, it prints no `drained` line naming that row, and `--measure` prints the row.
  Red when: a row the run did not measure is advised for deletion or dropped by the drain edit.
- **AC20** — When `python <kit>/lexicon.py --list` runs in a fixture whose
  `<fixture>/requirements/dev.txt` holds an `-r` include of `<fixture>/requirements.txt` spelled relative
  to its own directory, whose `a.txt` and `b.txt` include each other, and whose `c.txt` holds an `-r`
  include of `<fixture>/../../x.txt`, two directories above the fixture root, it reads the first
  include, prints `manifest not read:` for the escaping target, and prints no `RecursionError`.
  Red when: the cycle recurses, the escape is read, or the legal include is refused.
- **AC21** — When `python -c "import json; print([x['guard'] for x in json.load(open('tools/gate-legs.json'))
  if x['name'] == 'lexicon selftest'][0])"` runs, it prints a list holding `{prefix}/policy/` and the
  memory-tree kit's `build_records.py` under the same prefix.
  Red when: an edit to a sibling the arms run skips the leg on a scoped bar.
- **AC22** — When a fixture's planted `build_records.py` exits 1, `python <kit>/lexicon.py` exits 1
  printing `cannot read vocabulary records`; with no memory-tree kit in the fixture, it prints the same
  line naming the three places looked.
  Red when: a dead delegate reads as no record and every row asks for a record that exists.
- **AC23** — When `grep -c '_read_defs_at_sha' tools/drift-audit/drift_report.py` runs after the pass, it
  prints 0.
  Red when: drift-audit keeps a reader of its own after unit 16's move.
- **AC24** — When `git grep -h -c '^# >>> resolve_kit_dir' -- tools/lexicon/lexicon.py` runs, it prints
  `1`, and `git grep -h -c 'check_noun_subtokens(' -- tools/lexicon/lexicon.py` prints at least 3.
  Red when: a second locator copy lands, or a noun check bypasses the shared one.
- **AC25** — When `git grep -h -c -e "'--porcelain'" -e '"--porcelain"' -- tools/lexicon/lexicon.py` runs,
  it prints `1`.
  Red when: a second porcelain blame parser lives in the engine.
- **AC26** — When `git grep -h -c 'parse_name_status_z(' -- tools/lexicon/lexicon.py` runs, it prints at
  least 3, its definition and the two readers that call it.
  Red when: the rename map and the added set each parse `-z` output their own way.
- **AC27** — When `git grep -h -c 'is-shallow-repository' -- tools/lexicon/lexicon.py` runs, it prints
  `1`.
  Red when: a caller of `read_blame_lines` keeps its own shallow probe, or a third caller has none.
- **AC28** — When `grep -c 'counted in the `attended`' tools/unattended/check-unattended.test.sh` runs,
  it prints 0.
  Red when: the comment describes a population the leg no longer prints.
- **AC29** — When `awk '/TOOL-dUnstuckLanding-14 AC1, the leg/,/missing \[units-at-landing\]/'
  tools/unattended/check-unattended.test.sh | grep -cP '(?<!un)attended\b'` runs, it prints 1.
  Red when: an `attended` survives beyond the kept legacy record, or that record was reworded.
- **AC30** — When `grep -n 'TOOL-aMendedFleet-96' memory/backlog/TOOL.md` runs after the pass, its row
  does not read `OPEN`.
  Red when: the generated view lags the ask row unit 29 closed.
- **AC31** — When `grep -n 'Delete `.lexicon.conf`' tools/lexicon/README.md` runs, its line names
  `.lexicon-debt.txt`.
  Red when: the uninstall leaves the root ledger behind.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `codebase-map kit selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `unattended kit gate` · `memory hygiene` · `kit version markers`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC4 AC11 AC12 AC14 AC16 AC17 AC18 AC19 AC20 AC22 · one fixture per criterion, the shallow and compare-base ones built by the two helpers, its failing case each item's change cut out in turn, AC4's the `file://` form cut from the helper · none
New arm: tools/unattended/unattended.test.sh · covers AC10 · unit 17's settle case observed after unit 25's re-pointing, its failing case `:10717` restored to `attended LANDED 1` while the writer prints `owner` · none

## 8. Open questions

- **F1 — One batch or two?** Options: (a) one unit; (b) two, the unattended-suite items S10, S28 and S29
  apart. The rule permits (b) and requires neither, and (b) buys a short concurrent pass for a second
  spec, its edges and its audit. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, fewer units for the
  same coverage. widens: none · relaxes: none
- **F2 — What does S15 do with a version a pass moved on the branch?** Options: (a) every carrier agrees
  with the constant the branch holds; (b) every constant reverts to its base value for the lander's mint.
  (b) fails unit 29 AC35, a written criterion. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the
  one option that keeps every written criterion. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from the round-1 audit of units 22 to 29's 22 MEDIUM and 9
  LOW findings, one scope item per raw id.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 30 to 37
  declare toward this unit (TOOL-dMindYourWords-49, TOOL-dMindYourWords-52); no scope, design or criterion moved.

## 10. Reuse audit

Each item extends the seam of the unit it repairs, named in its scope item. Four reuse findings are
items themselves: S3 carries drift-audit's shallow-clone spelling (`tools/drift-audit/selftest.py:1318`),
S12 carries codebase-map's cleared environment (`tools/codebase-map/selftest.py:1596-1598`), S26 shares
one `-z` parser between unit 9's rename map and unit 26's added set, and S27 puts the shallow probe in the
shared reader the way `read_commit_paths` does (`tools/codebase-map/map_diff.py:128-150`). `python
tools/codebase-map/reuse_lookup.py "list the paths a branch adds over its compare base, renames
excluded"` ranked `resolve_compare_base`, which S11's fixture feeds, and name-stem helpers, and no
added-set reader to import, so S17 changes unit 26's own reader; `python tools/codebase-map/reuse_lookup.py "detect a shallow git history before trusting blame"`
ranked generic git wrappers and no shallow predicate, so S27 mints one inside the kit, which imports no
sibling.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon debt ledger keep its rows when tag findings and corpus findings share one population" --terms "lexicon-debt ledger drain measure rebaseline tags slice check_debt_pin widened shallow provenance"`
