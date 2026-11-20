# TOOL-dSkippedRecord-1 — the close's run-record commit is made only when staging left a diff

**Status:** CLOSED · rev-1 · 2026-11-20 · node d · Tier-2 · base 81657e77 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dSkippedRecord-1-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dSkippedRecord-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-1.md](../build/2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-1.md) | red-fix | — |
| [2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-2.md](../build/2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-2.md) | red-fix | — |
| [2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-3.md](../build/2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-3.md) | red-fix | — |
| [2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-4.md](../build/2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-4.md) | red-fix | — |
| [2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-5.md](../build/2026-11-20-build-TOOL-dSkippedRecord-1-red-fix-5.md) | red-fix | — |
| [2026-11-20-prompt-TOOL-dSkippedRecord-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dSkippedRecord-1-brief.md) | research | — |
| [2026-11-20-review-TOOL-dSkippedRecord-1-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dSkippedRecord-1-closing-diff-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

`write_run_record` commits the re-rendered run record under `in-place` after `--close` with nothing
testing that the stage holds a diff. A record re-rendered byte-identical stages nothing, so the
commit fails and the close prints "its commit failed" over git's own output. This unit tests the
stage before that commit and answers it the way `tools/push-main.sh#write_staged_change` answers its
own. A diff commits, an empty stage skips with one line, and a failed test refuses with one line.
The registry row the stage-commit leg carries for this site is drained in the same commit.

## 2. Scope (IN)

- **S1** — Inside `write_run_record`'s `in-place` `--close` branch, before the commit line, the
  driver runs `GIT diff --cached --quiet` over the whole index. It reads that exit as the stage
  answer: git's 1 is answer 0 and the commit runs, git's 0 is answer 1 and the skip line prints,
  and any exit above 1 is answer 2 and the refusal line prints. Answers 1 and 2 return 0 before the
  commit. Observed by AC1, AC2 and AC4.
- **S2** — The two existing stage-failure lines of `write_run_record` are the failed-stage half of
  answer 2. Each keeps its text and its `return 0`, so a failed `GIT add` never reaches the test or
  the commit. Observed by AC3 and AC6.
- **S3** — The commit line, its "run record committed at" line, its "its commit failed" line and
  the closing "commit them with the run-state file" line stay byte-identical. Every path through
  `write_run_record` still returns 0, so no verb's exit moves. Observed by AC2 and AC6.
- **S4** — The comment paragraph above `write_run_record`, and the `S5` comment above its commit,
  each carry a sentence saying the commit is made only when the stage holds a diff, with those
  three words. Observed by AC6.
- **S5** — `tools/unattended/unattended.test.sh` extends `run_render_helper` with an optional third
  argument, a mode. Its four existing calls pass none and behave as today. Four new calls in the
  same block pass `same`, `moved`, `addfail` and `difffail`. Observed by AC1, AC2, AC3 and AC4.
- **S6** — The `tools/unattended/unattended.sh` row of `memory/project/stage-commit-sites.txt` is
  deleted in the commit that lands S1. Observed by AC5.
  **Readers:** by name: `tools/gate-legs.json`, whose stage-commit leg passes the registry path to
  `tools/gate-lint/sh_hygiene.py`. No tracked file outside the memory tree spells the row itself. A
  git grep for the registry's file name, outside the build records, names only that leg, the conf's
  registry list and the gate-lint dossier. by value:
  `tools/gate-lint/sh_hygiene.py`, whose `check_registry` compares each row's count with the scan's,
  in both directions, so the row must go in the same commit that brings the count to 0.

## 3. Non-goals (OUT)

- No other commit site. The close-record commit in `write_close_commit`, the `commit-tree` in
  `write_claim`, any commit in `lib-unattended.sh` and the merge conclusion in
  `tools/unattended/pass-tree.sh` stay as they are. The `pass-tree.sh` and kickoff-fixture rows of
  the registry stay too.
- No change to `tools/push-main.sh` or `tools/gate-lint/sh_hygiene.py`.
- No change to any verb's exit code. The run record's own rule is that every miss is one line and a
  return 0.
- No staged-diff test on the non-committing paths. Under `--abort`, or a lander mode other than
  `in-place`, the closing "staged" line prints as today, because the operator commits that stage.
- No change to `tools/unattended/README.md`. Its sentence "under `in-place` the close commits them.
  A miss is one line, and no exit moves." stays true when a skip is one line.
- No shared stage-answer helper. Section 4's alternatives table gives the scanner evidence.
- No `--allow-empty` and no `--no-verify` on the run-record commit.

### Edges

none

## 4. Design

### The site today

All citations are read at the base `81657e77`. `tools/` is unchanged between that base and this
branch's HEAD, per `git diff --stat 81657e77c HEAD -- tools/`, which prints nothing.

`write_run_record` (`tools/unattended/unattended.sh#write_run_record`) stages the record first
(`tools/unattended/unattended.sh@5ac156849363:16559`). It then renders the index and stages only the
paths the render newly dirtied (`tools/unattended/unattended.sh@5ac156849363:16586`). Its `S5` branch
commits when `$VERB` is `--close` and `$LANDER_MODE` is `in-place`
(`tools/unattended/unattended.sh@5ac156849363:16590`). Nothing between the last stage and that
commit tests the index.

A close whose re-rendered record is byte-identical to the committed one, and whose render moved no
index path, stages nothing. The commit then exits 1, and the branch prints its "its commit failed"
line followed by git's output.

The stage-commit scan reads this as the one `unchecked` site in the file. A probe of
`scan_stage_file` over the base file, run on 2026-11-20, classified line 16592 `unchecked`, and lines
2789 and 11434 `unpaired`. The registry row says the same
(`memory/project/stage-commit-sites.txt@c21cd09191cf`, its last row).

### The precedent in this file

`write_close_commit` (`tools/unattended/unattended.sh#write_close_commit`) already guards the
close-record commit. It runs `GIT diff --cached --quiet -- "$2"` and, on exit 0, prints that nothing
was committed and names the commit that last changed the record. This unit's skip line takes that
shape. The run-record test carries no pathspec, because `git commit` commits the whole index, and
the test must answer about what the commit would commit.

### The answer

The answer uses `write_staged_change`'s vocabulary
(`tools/push-main.sh@790d21474c0e:989`): 0 the stage holds a diff, 1 nothing is staged, 2 a stage or
the test failed. The table is the whole contract.

| Answer | How it arises | What `write_run_record` does |
|---|---|---|
| 2 | `GIT add -- "$rec"` fails | prints its existing line and returns 0; no index render, no commit |
| 2 | `GIT add -A -- "${stage[@]}"` fails | prints its existing line and returns 0; no commit |
| 2 | `GIT diff --cached --quiet` exits above 1 | prints the new refusal line and returns 0; no commit |
| 1 | `GIT diff --cached --quiet` exits 0 | prints the new skip line and returns 0; HEAD stays put |
| 0 | `GIT diff --cached --quiet` exits 1 | runs the unchanged commit line |

**An error from the test is a refusal, never a commit.** `write_staged_change` reads an error from
`git diff` as 0, so its caller's commit runs and refuses with its own line. The brief chose the
other reading here, item 1: "a failing `git diff --cached --quiet` (exit above 1) is a 2, never read
as 'staged'". A commit over an index git cannot read is not attempted.

The branch takes this shape. `dq` joins the function's `local` line.

```bash
  # S5 - THE COMMIT, only where the close already commits: `in-place`, after `--close`, and only
  # when the stage holds a diff: git's 1 is answer 0, its 0 is answer 1, anything above is answer 2.
  if [ "$VERB" = --close ] && [ "$LANDER_MODE" = in-place ]; then
    GIT diff --cached --quiet 2>/dev/null; dq=$?
    case "$dq" in
      0) echo "unattended: run record unchanged — re-rendering it staged no change, so no commit was made; the record was last committed at $(GIT log -1 --format=%h -- "$rec" 2>/dev/null)"
         return 0 ;;
      1) ;;
      *) echo "unattended: run record staged, but git could not test whether the stage holds a change (git diff --cached exited $dq), so no commit was attempted"
         return 0 ;;
    esac
    if run_bounded git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" commit -q -m "records($slug): the run record"; then
      # ... unchanged from here to the end of the function
```

The test is written inline, in `write_run_record`'s own scope. The scan pairs a stage, a test and a
commit inside one function (`tools/gate-lint/sh_hygiene.py#scan_stage_file`). It reads a call to a
same-file function as a stage only when that function's body stages
(`tools/gate-lint/sh_hygiene.py#read_stage_helpers`). So a test moved into a helper of its own leaves
the commit `unchecked`. That is the bug class `memory/gotchas/a-helper-extraction-blinds-a-per-function-rule.md`
names.

The pass verifies the scan's reading with this probe, which calls the scanner's function over one
file and runs no leg:

```bash
python -c "import sys; sys.path.insert(0, 'tools/gate-lint'); import sh_hygiene as s; f = s.scan_stage_file(open('tools/unattended/unattended.sh', encoding='utf-8').read()); print('unchecked', len(f['unchecked'])); print([c for _n, c in f['admitted'] if 'the run record' in c])"
```

### The suite arms

`run_render_helper` (`tools/unattended/unattended.test.sh@fa35bdfb9aba:17170`) already slices
`write_run_record` out of the shipped driver and calls it in a subshell. Its stubs stand in for the
resolvers and for `run_bounded`, and it prints the staged paths. It sits in region 8, and its block
ends with `reset_tree; unset -f run_render_helper`
(`tools/unattended/unattended.test.sh@fa35bdfb9aba:17202`). The new calls go before that line.

The helper gains an optional third argument, a mode. With no mode it runs exactly as today, with
`VERB=--abort` and `LANDER_MODE=primary`. Any mode sets `VERB=--close` and `LANDER_MODE=in-place`
and adds four things inside the subshell.

1. `GIT_CONFIG_COUNT=1`, `GIT_CONFIG_KEY_0=core.hooksPath` and `GIT_CONFIG_VALUE_0` set to an empty
   directory under the fixture's git dir, exported. The commit then runs no hook the machine
   declares globally (`memory/gotchas/fixture-inherits-ambient-machine-state.md`).
2. A `run_bounded` branch for an argv whose first word is `git`. It runs that argv, puts its output
   in `RB_OUT`, and returns its exit. It sits ahead of the catch-all branch. The generator's argv
   starts with the python stub and its path holds `.git`, so the match is anchored on the first word.
3. The fixture's HEAD read before the call, and after it the lines `HEAD: same` or `HEAD: moved`,
   then `SUBJECT: ` and HEAD's subject.
4. The mode's own fixture, from this table.

| Mode | Fixture | Expected |
|---|---|---|
| `same` | `memory/builds/tRun/build/lu-record.md` holding `rec` is committed by `fixture`; the render stub writes nothing | the skip line; no "its commit failed"; `HEAD: same` |
| `moved` | as today: the record is new and the render stub appends to `memory/LIVE.md` | "run record committed at"; `HEAD: moved`; `SUBJECT: records(tRun): the run record` |
| `addfail` | as `moved`, and a `GIT` override that returns 1 for an argv starting `add -A` | "git could not stage what the index render moved: memory/LIVE.md"; `HEAD: same` |
| `difffail` | as `moved`, and a `GIT` override that returns 128 for exactly `diff --cached --quiet` | the refusal line naming `exited 128`; `HEAD: same` |

The `GIT` overrides pass every other argv to `git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV"`, as
the library's own `GIT` does (`tools/unattended/lib-unattended.sh#GIT`). `scan_dirty_paths` runs
`GIT diff --cached --name-only`, so the `difffail` override matches the whole argument list and
never a prefix.

**`moved` is the control.** Without it, `same` passes on a driver that never reaches its commit
branch at all, since `HEAD: same` holds there too
(`memory/gotchas/fixture-passes-by-finding-nothing.md`). `moved` shows that the branch is reached,
that a real diff commits, and that the answer is not inverted.

**Each failure mode has a break that turns it red.** `addfail` stages the record first, so a driver
that fell through past a failed second stage would reach the test with a diff and commit. HEAD
would move. `difffail` stages a new record and a moved `memory/LIVE.md`, so a driver that read
git's 128 as a diff would commit. HEAD would move there too.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `dq` | shell local in `write_run_record` | none, a local | nothing |
| the four modes of `run_render_helper` | suite helper arguments | none | the suite's own `hit`, `miss` and `same` lines |

No function, verb, flag, conf key or refusal number is minted.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `memory/project/stage-commit-sites.txt`

`memory/guides/SESSION-KICKOFF.md`'s `watch:` line names none of the three, so no manifest re-stamp
is owed.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| The answer in `lib-unattended.sh`, as a helper `write_run_record` calls | The scan does not follow a sourced library: its boundary row "a stager in a sourced library" reads the commit `unpaired` (`tools/gate-lint/sh_hygiene.py#STAGE_BOUNDARY`). With the adds left in `write_run_record` the commit stays `unchecked` and the row cannot drain. With the adds moved too, the commit reads `unpaired`, which is counted and never gated, so the row would drain over a site the leg no longer sees. |
| One helper shared with `write_close_commit` | That function tests a pathspec after another function's stage, while this one tests the whole index after its own two stages. A test-only helper is not a stager to the scan, so the commit would stay `unchecked`, as section 4 shows. A stage-and-test helper would have one caller. |
| Sourcing `write_staged_change` from `tools/push-main.sh` | It belongs to another copy-installed kit, which `unattended.sh` cannot source. It also stages the whole tree with `git add -A`, where this function stages only the paths its render moved. |
| `--allow-empty` on the commit | It lands an empty `records(<slug>): the run record` commit on every re-run close. |
| A new helper beside `run_render_helper` for the arms | It would copy the slice and its stubs. The charter's `[reuse]` rule extends the seam at a kind's second instance. |

## 5. Production-readiness checklist

- security: no new write path, surface or input. The commit line is unchanged and gains no bypass.
- perf / scale: one `git diff --cached --quiet` per `in-place` close, well under a second.
- error / empty / loading states: the empty stage is the skip line, and a failed test is the
  refusal line. A failed stage keeps its existing line. Each one returns 0.
- observability: the skip line names the commit that last changed the record, as
  `write_close_commit`'s does. The refusal line names git's exit.
- risks: the new guard sits above the commit's own failure branch
  (`memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md`). That branch stays live, because a
  stage holding a diff can still fail to commit on a hook, an `index.lock` or a missing identity.
  The new lines are `echo` lines, not `fail` calls. So neither the `ARMS_FLOORS` pair for the driver
  nor its `REFUSAL_CEILINGS` census moves (`.memory-tree.conf@cce444e49721:637`, `:664`). The suite
  asserts the driver spells `git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV"` at least twice
  (`tools/unattended/unattended.test.sh@fa35bdfb9aba:4480`). The commit line keeps that spelling.
- testing: the probes of section 6, and the two arms section 7 declares.
- migration: N/A — no stored data and no conf key; the kit is copied whole and its version is minted
  at landing.
- user docs: N/A — no page under `help/` spells the close's run-record lines. `git grep -n "run
  record committed" -- help/` printed nothing on 2026-11-20.

## 6. Acceptance criteria

- **AC1** — When `run_render_helper "" write_run_record same` runs, the output carries
  `unattended: run record unchanged` and `HEAD: same`, and does not carry `its commit failed`.
  Red when: `write_run_record` at base `81657e77` is restored, so the commit runs on the empty stage
  and the output carries "its commit failed" and no skip line.
  fixture: the suite's region 8. A pass observes it with a `bash` probe built from the same slice
  and stubs in a repository under `%TEMP%/<short-name>`.
- **AC2** — When `run_render_helper "" write_run_record moved` runs, the output carries
  `run record committed at`, `HEAD: moved` and `SUBJECT: records(tRun): the run record`.
  Red when: the answer is inverted so git's 1 reads as nothing staged, or the branch is never
  reached, and HEAD does not move.
  fixture: as AC1.
- **AC3** — When `run_render_helper "" write_run_record addfail` runs, the output carries
  `git could not stage what the index render moved: memory/LIVE.md` and `HEAD: same`, and does not
  carry `run record committed at`.
  Red when: the `return 0` after that line is deleted, so the staged record falls through to the
  test and is committed, and the output carries `HEAD: moved`.
  fixture: as AC1.
- **AC4** — When `run_render_helper "" write_run_record difffail` runs, the output carries
  `git could not test whether the stage holds a change (git diff --cached exited 128)` and
  `HEAD: same`.
  Red when: the `case`'s catch-all arm is removed, so git's 128 reaches the commit as
  `write_staged_change` would read it, and the output carries `HEAD: moved`.
  fixture: as AC1.
- **AC5** — When the `scan_stage_file` probe of section 4 runs over `tools/unattended/unattended.sh`,
  it prints `unchecked 0` and a one-item list holding the `records($slug): the run record` commit
  line. When `grep -c 'tools/unattended/unattended.sh' memory/project/stage-commit-sites.txt` runs,
  it prints 0.
  Red when: the test sits after the commit or in a helper of its own, so the probe prints
  `unchecked 1`, or the registry row is left standing.
- **AC6** — When `git grep -h -e 'unattended: run record' 81657e77 -- tools/unattended/unattended.sh`
  and `grep -h -e 'unattended: run record' tools/unattended/unattended.sh` run, the second prints
  every line of the first unchanged and in order, plus the skip and refusal lines. When
  `sed -n '/^write_run_record()/,/^}/p' tools/unattended/unattended.sh | grep -cE 'return [1-9]'`
  runs, it prints 0. When
  `sed -n '/^# TOOL-aMendedFleet-63 - THE RUN RECORD/,/^}/p' tools/unattended/unattended.sh | grep -c 'holds a diff'`
  runs, it prints 2 or more.
  Red when: an existing line is reworded or dropped, a path returns non-zero, or the comments still
  say the close commits unconditionally.

## 7. Gates

`shell hygiene (a stage committed with no staged-diff test)` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `harness arms (fail branches armed or pinned)` · `unattended kit gate` · `lexicon naming predicates` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · region 8, the empty-stage call of run_render_helper in mode same, with mode moved as its control; its failing case is staged by restoring write_run_record from base 81657e77, which commits the empty stage and prints its commit-failed line · none
New arm: tools/unattended/unattended.test.sh · covers AC3 AC4 · region 8, the failed-stage calls of run_render_helper in modes addfail and difffail; their failing cases are staged by deleting the return after the second stage's refusal line, and by letting the case's catch-all arm fall through to the commit · none

Neither arm moves a floor. `tools/unattended/unattended.test.sh` pins no `SELFTEST_FLOOR`, and the
driver's `ARMS_FLOORS` pair counts `fail` branches, which this unit neither adds nor removes. The
stage-commit leg reads the registry both ways, so the row deleted by S6 is what turns it green over
the fixed site. AC5 and AC6 are observed by their own commands at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.

## 10. Reuse audit

The seam extended is `write_run_record`'s own `S5` branch
(`tools/unattended/unattended.sh#write_run_record`). Its test takes the shape of the in-file
precedent `tools/unattended/unattended.sh#write_close_commit` and the answer vocabulary of
`tools/push-main.sh#write_staged_change`. The suite seam is `run_render_helper` in region 8 of
`tools/unattended/unattended.test.sh`, extended with a mode rather than copied.

`python tools/codebase-map/reuse_lookup.py "skip a commit when staging left nothing staged"` ranked
`skip`, `write_commit`, `build_commit`, `stage_or_fail` and `write_staged_change`. `stage_or_fail`
(`tools/unattended/unattended.sh#stage_or_fail`) stages the run-state file and refuses through
`fail 9`; it tests no staged diff. `write_staged_change` is another kit's, which this one cannot
source. No existing seam fits beyond the function's own branch and its in-file precedent. Section
4's alternatives table records why the library and a shared helper lose, by the scan's own rules.

Recall returned the brief, the build README and TOOL-dSettledStage-2's registry table naming this
site. It returned TOOL-dDerivedDocket-3's spec, which describes `write_close_commit`'s empty-stage
skip. It also returned TOOL-dAlignedCarrier-9 and TOOL-dMendedRecall-2, an earlier repair of the
in-place close's record commit. The brief adds TOOL-aMendedFleet-63, where the run record's commit and its
one-line-and-return-0 rule began. The probes and the source agreed; no hit was stale.

Recall terms used: write_run_record run record close commit in-place stage empty write_staged_change unchecked-stage stage-commit-sites drained
