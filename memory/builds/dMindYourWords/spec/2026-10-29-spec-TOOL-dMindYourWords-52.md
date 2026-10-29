# TOOL-dMindYourWords-52 — the audit of units 30 to 37: its 18 lexicon-side minors, batched — honest git reasons, every reader observed, the drain edit's shells and states, and the carriers a move left behind

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 22 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 |
| [2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md) | research | TOOL-dMindYourWords-38 TOOL-dMindYourWords-40 TOOL-dMindYourWords-48 TOOL-dMindYourWords-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 30 to 37
(`memory/builds/dMindYourWords/reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`)
confirmed 33 findings; its 13 highs are units 38 to 50, one per raw id. Its 15 MEDIUM and 5 LOW split
into two disjoint write sets by BUILD-METHOD M6: item M1's two govkit ids are TOOL-dMindYourWords-51,
and this unit is the other 18, 13 MEDIUM and 5 LOW, one scope item per raw id, ids sharing a report
item taking that item's severity. They land on units 31, 32, 35, 36 and 37 and on units 47 and 50, so
the batch repairs no unit in particular and builds last, at order 22, above every unit of the build.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M2 | MEDIUM | 8, 31 | S1, S2 |
| M3 | MEDIUM | 9, 25, 32 | S3, S4, S5 |
| M4 | MEDIUM | 11 | S6 |
| M5 | MEDIUM | 12 | S7 |
| M6 | MEDIUM | 17 | S8 |
| M7 | MEDIUM | 24 | S9 |
| M8 | MEDIUM | 27 | S10 |
| M9 | MEDIUM | 28 | S11 |
| M10 | MEDIUM | 35 | S12 |
| M11 | MEDIUM | 36 | S13 |
| L1 | LOW | 5, 13 | S14, S15 |
| L2 | LOW | 14 | S16 |
| L3 | LOW | 20 | S17 |
| L4 | LOW | 37 | S18 |

## 2. Scope (IN)

- **S1** — id 8, item M2, landing on units 31 and 47. `run_git` (TOOL-dMindYourWords-47 S1) puts `-c
  advice.graftFileDeprecated=false` after `--no-replace-objects`, so under `GIT_GRAFT_FILE=/dev/null`
  git's first stderr line is the failure and not the graft-deprecation hint. Observed by AC1.
- **S2** — id 31, item M2, landing on units 30, 31 and 32. `read_git_reason(stderr)` in
  `tools/lexicon/lexicon_conf.py` returns the first non-empty stderr line that does not start with
  `hint:`, or `git printed nothing on stderr`; unit 32 S3's raise and every refusal that quotes git,
  `cannot judge provenance — <why>` and `drift not measured — <why>` among them, takes its reason from
  it. Observed by AC2.
- **S3** — id 9, item M3, landing on unit 31. Every git spawn this batch adds (S12's unmerged probe, S13's
  stage read, S18's merge reads) goes through `run_git` or is a `NON_HISTORY_GIT` read, and
  `check_history_pins` (TOOL-dMindYourWords-50) over the kit at this pass, after every reader of the
  build exists, returns no problem. Observed by AC3.
- **S4** — id 25, item M3, landing on unit 31. `check_history_pins` prints one population line naming
  each module with its count, `history pins: judged <n> — <file> <n>, … · carried blocks: <names|none>`,
  so an empty capture can never read as a pass and a file's spawns are named, not summed away.
  Observed by AC4.
- **S5** — id 32, item M3, landing on units 31, 47, 48 and 49. One graft sweep in
  `tools/lexicon/selftest.py`: a fixture holding a suppression row with its record, drift-measured lines,
  a two-parent merge and a `CONTRACTS:` row with its record is run by `python <kit>/lexicon.py`,
  `--offenders` and `--merge-losses <range>`, ungrafted and then with a mid-history commit grafted onto
  no parent by `build_graft_fixture`, and each mode's exit code and verdict lines agree. Observed by
  AC5.
- **S6** — id 11, item M4, landing on unit 35. The drain edit is a bash command: unit 35 S2's emptied-home
  refusal adds `— a PowerShell redirect truncates the home before Python starts and hands it a pipe; run
  the drain edit under bash (Git Bash on Windows)`, and the README's debt-ledger section (unit 35 S4)
  says the edit runs under bash. Observed by AC6.
- **S7** — id 12, item M5, landing on units 29 and 37. `--measure` writes LF bytes on every platform,
  its stdout reconfigured with `newline="\n"` wherever unit 29 S11 has not, and the observation reads
  the home's bytes rather than an eol-normalising `git diff`. Observed by AC7.
- **S8** — id 17, item M6, landing on unit 31. `build_git_env()` returns the process environment less
  `GIT_ENV_LEAKS`, with `GIT_GRAFT_FILE=/dev/null`, as `tools/memory-tree/tree_lib.py:278-297`'s
  `read_git_output` runs, the tuple carried inline in `tools/lexicon/lexicon_conf.py` as the
  `git_env_leaks_py` block, byte-identical with `tools/lib/git_env_leaks.py` and graded by the existing
  row of `tools/lib/resolve-python.test.sh`. Observed by AC8.
- **S9** — id 24, item M7, landing on units 30, 33 and 36. The provenance join is a declared reader of
  the merge semantics unit 36 S3 gives the `rev` mode: a suppression row written in a merge resolution
  with a `unit.lexicon.suppressions` record that resolution adds is admitted, and one whose record was
  added on one branch only is refused. Unit 33 §3's sentence calling the contract walk "the one reader
  that asks it of a merge" is superseded by this item and TOOL-dMindYourWords-45 S1. Observed by AC9.
- **S10** — id 27, item M8, landing on unit 37. Wherever a pass of this build moved
  `KIT_MEMORY_TREE_VERSION`, the four dogfood renders, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`,
  `memory/guides/BUILD-METHOD.md` and `memory/guides/ANNOTATION-STYLE.md`, are re-rendered with `bash
  tools/memory-tree/adopt-memory-tree.sh --render`, and `kit/dogfood doc parity` is on §7. Observed by
  AC10.
- **S11** — id 28, item M9, landing on unit 37. No reader names the ledger's old home by its literal,
  tokenized or basename spelling in any tree a hook, skill or kit reads; any reader the widened grep
  of AC11 finds is re-pointed to `.lexicon-debt.txt`. Observed by AC11.
- **S12** — id 35, item M10, landing on unit 35. `read_ledger_source` first asks `git ls-files -u --
  <home>`; when it is non-empty the run exits 2 with `lexicon: the ledger home <home> is unmerged —
  resolve it with git checkout --merge -- <home>, or read a side with git show :2:<home> or :3:<home>`,
  never the `no committed copy survives` line. Observed by AC12.
- **S13** — id 36, item M11, landing on unit 37. The requirements reader of unit 37 S20 tests containment
  on `Path(target).resolve()` against `root.resolve()`, refuses a tracked symlink (mode `120000` in `git
  ls-files -s`) with `manifest not read: <path>`, and follows the include class `-r`, `--requirement`,
  `-c` and `--constraint`, each spelled with a space or `=`. Observed by AC13.
- **S14** — id 5, item L1, landing on unit 37. One observation reads the whole memory-tree marker
  population, the templates `tools/check-kit-versions.sh:248-280` derives, their four dogfood renders
  and the engine line, and finds one version, the constant's. Observed by AC14.
- **S15** — id 13, item L1, landing on unit 37. Every tracked `tools/memory-tree/*.template.md`, four at
  base, carries `gov:kit memory-tree@` equal to `KIT_MEMORY_TREE_VERSION` wherever a pass moved it.
  Observed by AC15.
- **S16** — id 14, item L2, landing on unit 37. The `lexicon selftest` row of `tools/gate-legs.json`
  guards `.lexicon.conf` beside the paths unit 37 S21 adds, since the suite reads the root conf
  (`tools/lexicon/selftest.py:2386`, `:3371-3372`). Observed by AC16.
- **S17** — id 20, item L3, landing on unit 37. The kit's shallow predicate is named `check_shallow`, the
  name `tools/policy/policy.py:626` gives the same probe; unit 37 S27's `check_shallow_history` is
  renamed. Observed by AC17.
  **Readers:** by name: READER NOT IN TREE — `check_shallow_history` is minted by TOOL-dMindYourWords-37
  at order 21 and no tracked file spells it at base ccd1292e · by value: NO VALUE READERS — the
  predicate's answer is consumed where it is read.
- **S18** — id 37, item L4, landing on units 36 and 37. `read_branch_added_paths` also counts, for each
  merge on the branch's first-parent chain in `<base>..HEAD`, the paths unit 36 S3's per-parent
  intersection says the merge itself adds, through `build_added_set_argv` (TOOL-dMindYourWords-44), so a
  record born in the branch's own merge resolution is the branch's, and a record merged in from the
  default branch still is not. Observed by AC18.

## 3. Non-goals (OUT)

- Any high: units 38 to 50, one per id.
- Item M1's govkit ids 4 and 18: TOOL-dMindYourWords-51.
- The left-shift lints, spec-lint rules and checklist entries the report names: each is a gate or a
  checklist, its own unit (BUILD-METHOD M2), and no clause of this build names one.
- Re-wording a repaired unit's spec (M4): each item is built and observed at this pass.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`); S10, S14 and S15 make the
  carriers agree with whatever the branch holds, as unit 37 §8 F2 resolved.

### Edges

- **consumes-from** `TOOL-dMindYourWords-31` — `build_git_env()`, which S8 strips of the leak variables (id 17)
- **consumes-from** `TOOL-dMindYourWords-32` — S3's raise, whose reason S2 takes from `read_git_reason` (id 31)
- **consumes-from** `TOOL-dMindYourWords-35` — `read_ledger_source` and its emptied-home refusal, which S6 and S12 extend (ids 11, 35)
- **consumes-from** `TOOL-dMindYourWords-36` — S3's merge semantics of the `rev` mode, which S9 observes on the provenance join and S18 applies to the branch walk (ids 24, 37)
- **consumes-from** `TOOL-dMindYourWords-37` — S9, S15, S17, S20, S21, S27 and AC7, the items S7, S10, S11, S13 to S18 repair (ids 5, 12, 13, 14, 20, 27, 28, 36, 37)
- **consumes-from** `TOOL-dMindYourWords-41` — `build_graft_fixture`, through which S5's sweep stages its grafts (id 32)
- **consumes-from** `TOOL-dMindYourWords-47` — `run_git`, to which S1 adds the hint switch and through which S8's environment reaches every read (ids 8, 17)
- **consumes-from** `TOOL-dMindYourWords-50` — `check_history_pins`, whose population line S4 names per file and which S3 runs over the finished kit (ids 9, 25)

## 4. Design

### Why this half of two

M4 admits two batches only for disjoint write sets by M6's clauses; TOOL-dMindYourWords-51 §4 states
the split. Every item here meets the lexicon kit, its suite, `tools/gate-legs.json` or a memory-tree
carrier, and none meets `tools/govkit/`.

### Evidence

- On git 2.54.0.windows.1, `GIT_GRAFT_FILE=/dev/null` makes a command print `hint: Support for
  <GIT_DIR>/info/grafts is deprecated` first, and `-c advice.graftFileDeprecated=false` makes the first
  line `fatal: …` (review ids 8 and 31, reproduced in the record).
- `tools/memory-tree/tree_lib.py:278-297` runs `read_git_output` under `build_git_env()` less
  `GIT_ENV_LEAKS`; `tools/lib/git_env_leaks.py` is the canonical block, `tools/policy/policy.py:68-86`
  carries it inline, and `tools/lib/resolve-python.test.sh` finds every carrier with `git grep -l "^#
  >>> git_env_leaks_py"` and holds it byte-identical (`:185`, `:221-241`).
- Under PowerShell 5.1, `python lexicon.py --measure > .lexicon-debt.txt` hands Python a pipe, truncates
  the home and writes UTF-16LE (review id 11, reproduced in the record).
- `git show :led.txt` exits 128 on an unmerged path, `git checkout -- led.txt` refuses it, and `git
  show :2:led.txt` prints a side (review id 35, reproduced in the record).
- `git diff --exit-code` exits 0 over a CRLF working copy of a `text eol=lf` path (review id 12).
- `git grep -l 'gov:kit memory-tree@'` lists the four `tools/memory-tree/*.template.md`, their four
  renders under `memory/` and the engine `tools/memory-tree/check-memory-hygiene.sh:69`, among others;
  `tools/check-kit-versions.sh:248-280` derives its population from `git ls-files` of the templates.
- `tools/policy/policy.py:626` defines `check_shallow(repo)`.
- `tools/gate-legs.json:1484-1486` guards the `lexicon selftest` leg with `{prefix}/lexicon/` alone.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_git_reason` | function, `tools/lexicon/lexicon_conf.py` | `py.function`; `lexicon.py --suggest read_git_reason --as py.function` answered `OK` at writing |
| `check_shallow` | function, `tools/lexicon/lexicon.py`, the rename of S17 | `py.function`, the canon's `check` for a predicate |
| the unmerged-home refusal | refusal line | none |

### Migration

None beyond S10's and S15's marker moves; every other item edits code, docs, a fixture or a manifest
row.

### Rollout

Live at landing, the last unit of the build, so `check_history_pins` (S3) and the graft sweep (S5) run
over every reader the build adds.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1, S2, S8
- `tools/lexicon/lexicon.py`: S2, S4, S6, S7, S9, S12, S17, S18
- `tools/lexicon/pack.py` and `tools/lexicon/stack_census.py`: S13
- `tools/lexicon/selftest.py`: S5 and the arms of §7
- `tools/lexicon/README.md`: S6, S9
- `tools/gate-legs.json`: S16
- `tools/memory-tree/ANNOTATION-STYLE.template.md`, `tools/memory-tree/BUILD-METHOD.template.md`,
  `tools/memory-tree/HYGIENE.template.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`: S15
- `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` and
  `memory/guides/ANNOTATION-STYLE.md`: S10, never edited; each is the rendered copy of its template
  above, rewritten by `adopt-memory-tree.sh --render`, and the render's diff trips `recall floor` and
  `recall floor arms` through their `memory/` guard
- `.lexicon-debt.txt`: S7
- any reader AC11's grep names: S11; none at base

### Alternatives rejected

- **One unit per minor**: M4 forbids it.
- **Folding each fix into the repaired unit's spec**: the audit's exit folds none (M4).
- **Leaving the old-home grep at unit 37 AC9's population** (S11): the report measured the widened
  grep empty at base, so it is a valid predicate with no false hit.
- **Stating the branch walk's merge exclusion as a non-goal** (S18): it keeps two answers to "what does
  a merge add" in one kit.

## 5. Production-readiness checklist

- security — S8 keeps a hook's `GIT_DIR` and a caller's pathspec mode out of every pinned read; S13
  bounds the requirements read by resolved path and refuses a tracked symlink; S3 and S5 observe the
  pin over every reader.
- perf / scale — S5's sweep is one fixture run twice per mode; S18 adds one per-parent read per branch
  merge; every other item is linear in what it reads.
- error / empty / loading states — S2, S6 and S12 each replace a misleading reason with the true one.
- observability — S4 names each file's spawns; every new refusal names its cause and its file.
- risks — S8 changes the environment of every pinned read; a caller depending on an inherited
  `GIT_DIR` would change answer, and none in the kit does, since each spawn names `cwd`.
- testing — AC1 to AC18 and the arms of §7.
- migration — S10 and S15.
- user docs — `tools/lexicon/README.md` (S6, S9).

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/lexicon'); import lexicon_conf as c;
  print(c.run_git('.', 'cat-file', '-t', '0' * 40, text=True).stderr.splitlines()[0])"` runs in the
  repository, it prints a line starting `fatal:`.
  Red when: the deprecation hint is git's first stderr line.
- **AC2** — When unit 32 AC4's call runs after the pass, the raised text holds `fatal:` and no `hint:`.
  Red when: a refusal names the hint instead of the missing object.
  fixture: unit 32 AC4's repository under `%TEMP%/<short>`.
- **AC3** — When `python -c "import sys, pathlib; sys.path.insert(0, 'tools/lexicon'); import lexicon;
  print(lexicon.check_history_pins(pathlib.Path('tools/lexicon'))[0])"` runs after the pass, it prints
  `[]`.
  Red when: a spawn this batch or any unit of the build added bypasses the runner.
- **AC4** — When `python tools/lexicon/lexicon.py` runs after the pass, its output carries one line
  starting `history pins: judged`, naming `lexicon.py` and `lexicon_conf.py` each with a count.
  Red when: the line prints a total alone, or prints nothing.
- **AC5** — When the sweep's fixture is run by `python <kit>/lexicon.py`, `--offenders` and
  `--merge-losses <range>` before and after `build_graft_fixture` grafts its middle commit onto no
  parent, each mode's exit code and its lines naming `SUPPRESSION`, `CONTRACTS`, `drift`, `LOSS` or
  `SKIPPED` are equal across the two runs, for a replace ref and for a graft file.
  Red when: any reader of the kit follows the graft.
  fixture: one scratch repository under `%TEMP%/<short>`.
- **AC6** — When `powershell -NoProfile -Command 'python <kit>/lexicon.py --measure > .lexicon-debt.txt
  2> err.txt; exit $LASTEXITCODE'` runs in unit 35 AC1's fixture on a Windows node, it exits 2 and
  `err.txt` names `PowerShell`.
  Red when: the refusal names only `git checkout`, or the run writes a ledger.
  permission: a Windows node with `powershell` on `PATH`, which this node is.
- **AC7** — When `python tools/lexicon/lexicon.py --measure > .lexicon-debt.txt` runs at the pass, `python
  -c "import sys; sys.exit(b'\r' in open('.lexicon-debt.txt', 'rb').read())"` exits 0.
  Red when: a carriage return reaches the home, which `git diff` would normalise away.
- **AC8** — When `GIT_DIR=/nonexistent python -c "import sys; sys.path.insert(0, 'tools/lexicon'); import
  lexicon_conf as c; print(c.run_git('.', 'rev-parse', 'HEAD', text=True).returncode)"` runs, it prints
  `0`; and `diff <(sed -n '/^# >>> git_env_leaks_py/,/^# <<< git_env_leaks_py/p' tools/lib/git_env_leaks.py
  | tr -d '\r') <(sed -n '/^# >>> git_env_leaks_py/,/^# <<< git_env_leaks_py/p'
  tools/lexicon/lexicon_conf.py | tr -d '\r')` exits 0.
  Red when: an inherited `GIT_DIR` reaches a pinned read, or the carried block drifts.
- **AC9** — When `python <kit>/lexicon.py` runs in a fixture whose merge resolution writes a suppression
  row beside a `unit.lexicon.suppressions` record that resolution adds, it exits 0; when the record was
  added on one branch only, it exits 1 naming `SUPPRESSION WITHOUT PROVENANCE` and the merge's sha8.
  Red when: the provenance join reads a merge by anything but its per-parent intersection.
  fixture: a scratch repository under `%TEMP%/<short>`, no `core.hooksPath`.
- **AC10** — When `git grep -h -o 'gov:kit memory-tree@[0-9.]*' -- memory/HYGIENE.md memory/TEMPLATE-SPEC.md
  memory/guides/BUILD-METHOD.md memory/guides/ANNOTATION-STYLE.md | sort -u` runs after the pass, it
  prints one line whose version equals `KIT_MEMORY_TREE_VERSION` in
  `tools/memory-tree/check-memory-hygiene.sh`.
  Red when: a render still carries the old marker after the constant moved.
- **AC11** — When `git grep -n -e 'project/lexicon-debt' -e 'F:lexicon-debt' -- tools .githooks .claude
  skills .gitattributes .memory-tree.conf .lexicon.conf WIRE-INTO-PROJECT.md help memory/map
  memory/HYGIENE.md` runs after the pass, it prints nothing.
  Red when: a reader still names the old home by a tokenized or basename spelling.
- **AC12** — When `python <kit>/lexicon.py --measure > other.txt` runs in a fixture whose ledger home is
  left conflicted by a `git merge`, it exits 2 and stderr names `git checkout --merge` and `:2:`.
  Red when: the run reports `no committed copy survives` or suggests `git checkout -- <home>`.
  fixture: a scratch repository under `%TEMP%/<short>` with a conflicting merge on the home.
- **AC13** — When `python <kit>/lexicon.py --list` runs in a fixture whose tracked
  `<fixture>/requirements/x.txt` is a symlink to a file outside the root and whose `requirements.txt`
  holds `--requirement=base.txt`, it prints `manifest not read:` naming that link by its repo-relative
  path and lists the pack `base.txt` declares.
  Red when: the link is followed, or the long-form include is skipped.
  fixture: a scratch repository under `%TEMP%/<short>` with `core.symlinks` true.
- **AC14** — When `git grep -h -o 'gov:kit memory-tree@[0-9.]*' -- 'tools/memory-tree/*.template.md'
  memory/TEMPLATE-SPEC.md memory/HYGIENE.md memory/guides/BUILD-METHOD.md
  memory/guides/ANNOTATION-STYLE.md tools/memory-tree/check-memory-hygiene.sh | sort -u` runs after the
  pass, it prints exactly one line, equal to `KIT_MEMORY_TREE_VERSION`.
  Red when: any carrier of the population disagrees with the constant.
- **AC15** — When `git ls-files 'tools/memory-tree/*.template.md' | wc -l` runs it prints `4`, and `git
  grep -L "gov:kit memory-tree@<V>" -- 'tools/memory-tree/*.template.md'`, `<V>` the constant, prints
  nothing.
  Red when: a template carries another version, or the population is empty.
  figure: 4 PINNED at base 2026-10-29.
- **AC16** — When `python -c "import json; print('.lexicon.conf' in [x for x in
  json.load(open('tools/gate-legs.json')) if x['name'] == 'lexicon selftest'][0]['guard'])"` runs, it
  prints `True`.
  Red when: a conf-only commit skips the suite on a scoped bar.
- **AC17** — When `git grep -n 'check_shallow_history' -- tools` runs after the pass it prints nothing,
  and `git grep -n 'def check_shallow(' -- tools/lexicon/lexicon.py` prints one line.
  Red when: the kit keeps a second name for the predicate `policy.py` already names.
- **AC18** — When unit 37 AC17's fixture branch instead adds a vocabulary record in the resolution of a
  merge of its own and cites it in a `widened:<record>` row, `python <kit>/lexicon.py` exits 0; unit
  37 AC17's own case still exits 1 naming `record not added by this branch`.
  Red when: the branch's own merge-born record is refused, or the default branch's is admitted.
  fixture: `build_compare_base_fixture`'s origin and clone under `%TEMP%/<short>`.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `codebase-map kit selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `kit version markers` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/lexicon/selftest.py · covers AC2 AC5 AC9 AC12 AC13 AC18 · one fixture per criterion, AC5's the all-readers graft sweep, its failing case each item's change cut out in turn, AC5's the runner's `--no-replace-objects` cut · none

## 8. Open questions

- **F1 — What does the branch walk do with a merge the branch makes?** Options: (a) count the merge's
  own additions by unit 36 S3's per-parent intersection; (b) state the exclusion as a non-goal with its
  refusal text. (b) keeps two rules for one question in the kit. RESOLVED (agent, 2026-10-29,
  delegated): (a), rung 3, the most capable option and the rule unit 36 already states. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from the round-1 audit of units 30 to 37's 13 MEDIUM and
  5 LOW lexicon-side findings, one scope item per raw id.

## 10. Reuse audit

Each item extends the seam of the unit it repairs, named in its scope item. Four reuse findings are
items themselves: S8 carries `tools/lib/git_env_leaks.py`'s block as `tools/policy/policy.py:68-86`
does and mirrors `read_git_output` (`tools/memory-tree/tree_lib.py:278-297`), the shape
TOOL-dDeclaredLoop-39 gives `run_pinned_git`; S2's reason rule is the one `read_git_output` states for
a first stderr line; S17 takes the name `check_shallow` from `tools/policy/policy.py:626`, which a kit
that imports no sibling cannot call; and S18 reads a merge's additions through
TOOL-dMindYourWords-44's `build_added_set_argv`. `python tools/codebase-map/reuse_lookup.py "route every
git history read through one pinned spawn helper"` ranked `run_git`, `read_git_output` and
`build_git_env`, the seams named; `git grep -n 'def check_shallow' -- tools` prints
`tools/policy/policy.py:626`, the predicate unit 37 §10 said did not exist.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon debt ledger keep its rows when tag findings and corpus findings share one population" --terms "lexicon-debt ledger drain measure unmerged powershell redirect graft hint leaks shallow"`
