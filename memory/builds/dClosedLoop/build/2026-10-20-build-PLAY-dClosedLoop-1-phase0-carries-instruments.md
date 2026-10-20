**Serves:** research PLAY-dClosedLoop-1

# Phase 0 carries instruments: P0.1 rows 1 and 2, each plant seen on the old code first

The commands behind P0.1's first two rows (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]`),
built from `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-carries.md` (dispatch 235). Every command run for a
plant is listed in order, with its exit code and the line that proves it, before and after each fix.

**Conventions.**
- `build/` is `memory/builds/dClosedLoop/build/`, and IR is `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-instruments.md`.
- `C` is `build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`, run from a tree root, since it reads v2 and the map
  relative to the working directory.
- `S` is the builder's scratch folder,
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d235`.
  `N` is the new code, `S/repo/` followed by `C`, run by its absolute path from another tree.
- Every `python` is `python -B` under `PYTHONDONTWRITEBYTECODE=1`, Python 3.14.5, in Git Bash on Windows.

**Where they ran.** The old code is `C` at `4bfca2c74`, blob `1f113e30` by `git hash-object`, the same in the
`p0-carries` worktree and in the clone. The baseline ran in `p0-carries`. Everything after it ran in `S/repo`, a
`--shared` clone of `p0-carries` at `4bfca2c74`, on its branch `p0-carries-build`, with `core.hooksPath` set to its own
`.githooks`. This session's edit tools refuse a write into the `p0-carries` worktree, because the session is bound to
another worktree. The real-history probe states ran in `S/probe`, a detached worktree of that clone. The pre-commit
hook's isolation rule refuses a commit on a non-default branch in a primary tree, and the clone is one. So the commit
is made in `S/build`, a worktree of the clone on the branch `p0-carries-commit`, cut from `4bfca2c74` and carrying the
same staged blobs, beside the build README's re-render by `python tools/memory-tree/gen_build_index.py --write`.

## [baseline] The old code, before anything changed

`bash S/runall.sh S/before`, in `p0-carries`. It runs each case as `python C <args>` and writes its output to
`S/before/<case>.out`.

| Case | Arguments | Exit | The line that proves it |
|---|---|---|---|
| tree | none | 2 | `carries: no spec measured, so the join reads nothing and is never green` |
| tree, exit mode | `--exit` | 2 | the same line |
| report | `--report dTrueNorth` | 0 | `Coverage of dTrueNorth's 6 clauses and 1 owned nodes, over 0 specs:` |
| fixture | `--fixture` | 0 | `… specs measured 2 in 1 builds · findings 0 · fixture dTrueNorth` |
| fixture report | `--fixture --report dTrueNorth` | 0 | `- carried whole: 5; carried in parts: 1 (cl-dClosedLoop-0003)` |
| ghost | `--fixture --plant ghost` | 1 | `… carries cl-dClosedLoop-9999, which no clause carries (a ghost id)` |
| unbound | `--fixture --plant unbound` | 1 | `fixture/dTrueNorth/spec/unit-3.md: carries nothing and is derived from nothing (unbound)` |
| stale | `--fixture --plant stale` | 1 | `… pins cl-dClosedLoop-0001@deadbeef, and the clause's text now hashes 83b6b117 (a stale pin)` |
| ambiguous | `--fixture --plant ambiguous` | 1 | `cl-dClosedLoop-0001: carried whole by 2 specs (…)` |
| dropped | `--fixture --plant dropped` | 1 | `fixture/dTrueNorth/spec/unit-1.md: stopped carrying cl-dClosedLoop-0001 since its last revision, with no move, retirement or deferral recorded`, one of 3 findings |
| uncarried | `--fixture --plant uncarried` | 1 | `dTrueNorth: cl-dClosedLoop-0001 is carried by no spec (uncarried)` |
| node | `--fixture --plant node` | 1 | `dTrueNorth: owned node record-kind.deviation is named by no spec` |
| token | `--fixture --plant token` | 1 | ``dTrueNorth: cl-dClosedLoop-0001's token `**Derived:**` appears in none of its carriers`` |
| unmeasured | `--fixture --plant unmeasured` | 2 | `carries: no spec measured, so the join reads nothing and is never green` |

The `dropped` plant re-adds `cl-dClosedLoop-0002` whole, not the clause it dropped, so it also reds as ambiguous and
uncarried. That is its verdict today, and it is kept.

## [real-old] IR's plants on real commits, on the old code

The helpers are d218's (IR:754-838), adapted, in `S`. `mkspecs.py` writes the same two dTrueNorth specs, named
`2026-10-21-spec-probe-unit-1.md` and `-2.md` with the H1 `# probe unit N`, so no file name holds a unit id or a colon.
NTFS takes no colon in a file name. `plant.py` keeps the `crossbuild`, `drop` and `typo` steps. Its `typo` step edits
that H1, and it adds a control step, `moved`, which appends `**Moved:** cl-dClosedLoop-0007 to dTrueNorth by
XX-dProbe-1`. That decision id is of no family, so no generator joins it. `run.sh <label> [<carries.py>]` runs
`--build dTrueNorth` and `--build dTrueNorth --exit` in the working directory, then prints both exits and every
finding line. With no path, it runs the clone's own `C`, the old code. Each step is committed in the clone, so
`real_specs` reads it as a revision.

| # | Step, and its commit in the clone | Command | Exits, plain and `--exit` | The line that proves it |
|---|---|---|---|---|
| 1 | `python S/mkspecs.py` (`318f911ef`) | `bash S/run.sh clean` | 0, 0 | `## clean: carries=0 carries--exit=0` |
| 2 | `python S/plant.py crossbuild` (`313834806`) | `bash S/run.sh crossbuild` | 0, 0 | `## crossbuild: carries=0 carries--exit=0`, and no finding line: row 1's escape |
| 3 | `python S/plant.py moved` (`2de33e1bd`) | `bash S/run.sh moved` | 0, 0 | `## moved: carries=0 carries--exit=0` |
| 4 | from `318f911ef`, `python S/plant.py drop` (`cfe29736f`) | `bash S/run.sh drop` | 1, 1 | `…/2026-10-21-spec-probe-unit-1.md: stopped carrying cl-dClosedLoop-0003 since its last revision, with no move, retirement or deferral recorded` |
| 5 | `python S/plant.py typo` (`1635f8cca`) | `bash S/run.sh typo` | 0, 1 | `## typo: carries=0 carries--exit=1`. Its one line is `dTrueNorth: cl-dClosedLoop-0003 is carried by no spec (uncarried)`, from `--exit` only: row 2's escape |

## [stage-a] The plants ported, the join untouched

`C` gains `crossbuild` and `typo` in `PLANTS` and in `fixture`.
- `crossbuild` carries the first clause of the next build in v2's chain whole, with its current pin, in the second
  spec. For dTrueNorth that is `cl-dClosedLoop-0007@b0458b78`, d218's own.
- `typo` drops the first clause's Carries line from the first spec in one revision. A later revision then appends a
  line. The second spec carries the clause whole with its body, so only the drop arm can see it. d218's `drop`
  removes `cl-dClosedLoop-0003` outright. Since `--fixture` always runs in exit mode, the uncarried arm would red that
  both before and after the fix. So the port keeps the clause carried, as the `dropped` plant means to.

At this stage the fixture still gave each spec its previous text as one string. So `typo`'s previous text was the
dropped revision, which is what the old `real_specs` read from git.

| Command | Exit | The line that proves it |
|---|---|---|
| `bash S/runall.sh S/stageA crossbuild typo`, case `--fixture --plant crossbuild` | 0 | `… findings 0 · fixture dTrueNorth · plant crossbuild` |
| the same run, case `--fixture --plant typo` | 0 | `… findings 0 · fixture dTrueNorth · plant typo` |
| the same run, the 14 baseline cases | as in [baseline] | `cmp` of each output against `S/before` prints nothing |

## [fix-1] Row 1: a carried id's build must be the spec's own

`join` collects every `**Moved:** <clause> to <build>` line of every measured spec. A Carries line whose clause
belongs to a build other than the spec's own folder's, with no such line naming it to that folder's build, is a
finding. It joins no carrier set, so it counts as carried for no build, its owner included.

| Command | Exit | The line that proves it |
|---|---|---|
| `bash S/runall.sh S/stageB crossbuild typo`, case `--fixture --plant crossbuild` | 1 | `fixture/dTrueNorth/spec/unit-2.md: carries cl-dClosedLoop-0007, a clause of dGroundRules, and no Moved line names it to dTrueNorth (another build's clause)` |
| the same run, every other case | as in [stage-a] | `cmp` against `S/stageA` names only `plant-crossbuild.out` |
| in `S/probe` at `313834806`: `bash S/run.sh "313834806 new" N` | 1, 1 | `…/2026-10-21-spec-probe-unit-2.md: carries cl-dClosedLoop-0007, a clause of dGroundRules, and no Moved line names it to dTrueNorth (another build's clause)` |
| at `2de33e1bd`, the Moved control: `bash S/run.sh "2de33e1bd new" N` | 0, 0 | `## 2de33e1bd new: carries=0 carries--exit=0` |
| in `S/repo`: `python S/probe_moved.py N`, the crossbuild fixture with a Moved line appended | 0 | `no Moved line: findings 1`, `Moved to dTrueNorth: findings 0`, `Moved to dSafePassage: findings 1`, `Moved with no build: findings 1` |
| in `S/probe` at `313834806`, the old code: `python C --report dGroundRules` | 0 | `- carried whole: 1; carried in parts: 0 (none)`, the foreign carry counted for its owner |
| the same, the new code: `python N --report dGroundRules` | 0 | `- carried whole: 0; carried in parts: 0 (none)`, and `cl-dClosedLoop-0007` now leads the uncarried list |

## [fix-2] Row 2: the drop arm reads every revision

`real_specs` reads the spec's text at every commit `git log --format=%H -- <spec>` lists, where it read only the
second of the last two. Each spec is now `(path, text, [revisions])`, and `fixture` passes the same shape. `typo`'s
revisions are the original and the dropped text. The drop arm takes every clause any revision carried. Its line now
reads "which an earlier revision carried" where it read "since its last revision".

| Command | Exit | The line that proves it |
|---|---|---|
| `bash S/runall.sh S/stageC crossbuild typo`, case `--fixture --plant typo` | 1 | `fixture/dTrueNorth/spec/unit-1.md: stopped carrying cl-dClosedLoop-0001, which an earlier revision carried, with no move, retirement or deferral recorded` |
| the same run, case `--fixture --plant dropped` | 1 | the same three findings, the first in the new wording: the only other change against `S/stageB` |
| the same run, every other case | as in [fix-1] | `cmp` against `S/stageB` names only `plant-typo.out` and `plant-dropped.out` |
| in `S/probe` at `318f911ef`: `bash S/run.sh "318f911ef new" N` | 0, 0 | `## 318f911ef new: carries=0 carries--exit=0` |
| at `cfe29736f`: `bash S/run.sh "cfe29736f new" N` | 1, 1 | `…/2026-10-21-spec-probe-unit-1.md: stopped carrying cl-dClosedLoop-0003, which an earlier revision carried, …` |
| at `1635f8cca`, the typo: `bash S/run.sh "1635f8cca new" N` | 1, 1 | the same line, now beside the uncarried one: the escape closed |
| at `313834806`: `bash S/run.sh "313834806 new" N` | 1, 1 | row 1's line, as in [fix-1] |
| at `2de33e1bd`: `bash S/run.sh "2de33e1bd new" N` | 0, 0 | `## 2de33e1bd new: carries=0 carries--exit=0` |
| in `S/repo`: `python S/probe_typo.py N`, the typo fixture with a release line appended to the dropping spec | 0 | `no release line: findings 1`, `Retired line: findings 0`, `Retired line for another clause: findings 1` |
| `python S/probe_moved.py N` again | 0 | `findings 1`, `0`, `1` and `1`, as in [fix-1] |
| `python N --fixture --plant crossbuild --build dGroundRules` | 1 | `fixture/dGroundRules/spec/unit-2.md: carries cl-dClosedLoop-0001, a clause of dTrueNorth, and no Moved line names it to dGroundRules (another build's clause)` |
| `python N --fixture --plant typo --build dGroundRules` | 1 | `fixture/dGroundRules/spec/unit-1.md: stopped carrying cl-dClosedLoop-0007, which an earlier revision carried, …` |
| `python N --fixture --build dGroundRules` | 0 | `… findings 0 · fixture dGroundRules` |

`--report` keeps its arguments and its output. The report and fixture-report cases are byte-identical in every
stage, so the departures report can still call it as a subprocess.

## [staged] On the staged bytes

`C` was staged with `git add` by name, `git diff --quiet` on it exited 0, and its index entry reads `i/lf`. Then:

| Command | Exit | The line that proves it |
|---|---|---|
| `bash S/runall.sh S/staged crossbuild typo` | per case, as in [fix-2] | `cmp` of every output against `S/stageC` prints nothing |

## [limits] What the two arms do not check

- Row 1 accepts a Moved line in any measured spec, so a Moved line anywhere excuses the carry. It does not resolve
  the line's decision id, and it does not read which build's spec holds the line. Under `--fixture` only the one
  build's specs are measured.
- Next to row 1, and unchanged here: the token arm reads only the owner build's own specs. So a clause moved by a
  Moved line reds its token when its owner build is measured too. `python S/probe_owner.py N` exits 0 and prints
  `owner measured: findings 1` with ``dGroundRules: cl-dClosedLoop-0007's token `.governance/policy.toml` appears in
  none of its carriers``, though the dTrueNorth spec that carries the clause holds the token. Neither row 1 nor row 2
  names it.
- Row 2's revisions are the commits `git log -- <spec>` lists without `--follow`, so it does not read a renamed
  spec's revisions from before the rename. Git's default history simplification can omit a side-branch revision
  whose content a merge discarded. An uncommitted edit is read as the spec's text, never as a revision.
- The real-history plants ran only in the scratch clone. The fixture holds its revisions in memory and never calls
  git.
- No leg runs this instrument. Only a hand runs it (the plan's `[constraints]`).

## Finding 14

The revision record's finding 14 (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-revision.md`), built from
`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-carries-2.md` (dispatch 242), its recommended option 1: the
token arm reads every carrier's text, from whichever measured build's folder holds it. The second item in
[limits] above is the escape it closes.

**What changed in `C`.**
- `join` reads a carrier's text from every measured build's specs, where it read only the owner build's. The
  uncarried arm's release check still reads the owner build's specs, as before.
- `fixture` gains two plants. `moved` is crossbuild's carry, with the owner build measured too. The owner's first
  spec moves the clause to this build by `**Moved:** <clause> to <build> by XX-dProbe-1` where it carried the clause,
  and its earlier revision still carries it. `moved-token` is the same, with one of the clause's tokens dropped from
  the carrier: the first token that this build's own text lacks. `XX-dProbe-1` is d235's decision id, of no family.
- Under `--fixture` the findings filter is every build the fixture measures. Before, `only` was the fixture's build,
  so a moved clause's owner was never read. Every older plant measures one build, so its output is unchanged.

**Where they ran.** Here `S` is this dispatch's scratch folder, the `d242` sibling of d235's. `S/repo` is a
`--shared` clone of the session's worktree at `bcc416ced`, with `core.hooksPath` set to its own `.githooks`. It holds
the old code: `C` at blob `9657a5e8`, d235's committed fix. `S/build` is that clone's linked worktree on the branch
`p0-carries-2`, and `N` is `S/build/` followed by `C`. `S/runall.sh` is d235's runall, with W's default moved to
`S/repo` and `crossbuild` and `typo` added to its plant list. `S/probe_owner.py` is d235's probe, copied unchanged.
Every run is in `S/repo` unless it names `W=S/build`.

| # | Command | Exit | The line that proves it |
|---|---|---|---|
| 1 | `git hash-object C` in `S/repo` | 0 | `9657a5e8679de272e7385a2615cbacece8703ed4` |
| 2 | `bash S/runall.sh S/c-before`, the old code | per case | tree and tree-exit 2, the report and fixture cases 0, unmeasured 2, every other plant 1, as in [baseline] and [fix-2] |
| 3 | `python S/probe_owner.py C`, the old code | 0 | `owner measured: findings 1` and ``dGroundRules: cl-dClosedLoop-0007's token `.governance/policy.toml` appears in none of its carriers`` |
| 4 | a `python -c` over the old code: for dTrueNorth and dGroundRules, the clause crossbuild carries, its tokens, and whether the first is in that build's second fixture spec, run once more at the end to print its exit | 0 | dTrueNorth carries `cl-dClosedLoop-0007` with one token, absent from its text. dGroundRules carries `cl-dClosedLoop-0001`, whose first token `**Carries:**` its text holds, so `moved-token` drops the first token the text lacks |
| 5 | Stage A, the plants and the filter added, `join` untouched: `W=S/build bash S/runall.sh S/c-stageA moved moved-token` | per case | the 16 older cases exit as in row 2, and `cmp` of each against `S/c-before` prints nothing |
| 6 | the same run, case `--fixture --plant moved` | 1 | ``dGroundRules: cl-dClosedLoop-0007's token `.governance/policy.toml` appears in none of its carriers``, its one finding, with `specs measured 4 in 2 builds`: red before the fix |
| 7 | the same run, case `--fixture --plant moved-token` | 1 | the same line, its one finding |
| 8 | Stage B, the token arm fixed: `W=S/build bash S/runall.sh S/c-stageB moved moved-token` | per case | `cmp` against `S/c-stageA` names only `plant-moved.out` |
| 9 | the same run, case `--fixture --plant moved` | 0 | `… specs measured 4 in 2 builds · findings 0 · fixture dTrueNorth · plant moved`: green after |
| 10 | the same run, case `--fixture --plant moved-token` | 1 | ``dGroundRules: cl-dClosedLoop-0007's token `.governance/policy.toml` appears in none of its carriers``: the same carrier without the token, red |
| 11 | `python S/probe_owner.py N` | 0 | `owner measured: findings 0`, where row 3 printed 1 |
| 12 | `python N --fixture --plant moved --build dGroundRules` | 0 | `… findings 0 · fixture dGroundRules · plant moved` |
| 13 | `python N --fixture --plant moved-token --build dGroundRules` | 1 | ``dTrueNorth: cl-dClosedLoop-0001's token `**Derived:**` appears in none of its carriers``, its one finding |
| 14 | line-length scans of `N` and the schedule script, an authoring aid | 0 | two new lines over 120 characters, a docstring line and the `every` comment, shortened at rows 16 and 18 |
| 15 | `S/stageA-carries.py`, written by a `python -c` as `N` with the one `joined` line put back: `--fixture --plant moved --build dGroundRules`, then `--plant moved-token --build dGroundRules`, then `--plant moved` | 1, 1, 1 | six findings each for the first two, one per token of `cl-dClosedLoop-0001`, the first ``dTrueNorth: cl-dClosedLoop-0001's token `**Carries:**` appears in none of its carriers``. The third prints row 6's line. Red before the fix under `--build dGroundRules` too |
| 16 | a docstring rewrap; then `git add` of `C` by name, `git diff --quiet` on it, and `git ls-files --eol` | 0 | `i/lf    w/lf    attr/text eol=lf`, no CR byte |
| 17 | `W=S/build bash S/runall.sh S/c-staged moved moved-token` | per case | `cmp` of all 18 outputs against `S/c-stageB` prints nothing |
| 18 | the comment row 14 found, shortened; `git add` again, `git diff --quiet` | 0 | the index entry `0b5fab9cc06d`, `i/lf` |
| 19 | `W=S/build bash S/runall.sh S/c-staged moved moved-token` again, then rows 11 to 13 again | per case | `cmp` against `S/c-stageB` prints nothing; `owner measured: findings 0`. Rows 12 and 13 were first piped through `tail`, whose exit is not counted, then re-run unpiped: exits 0 and 1, rows 12 and 13's lines |

Today's tree still exits 2 with `carries: no spec measured, so the join reads nothing and is never green`, and the
report and fixture-report cases are byte-identical in every stage. No function was added or removed, so no name went
to the lexicon.

**What this does not check.**
- The plant places the Moved line in the owner's spec. Row 1's arm accepts it in any measured spec, so where the line
  sits is not varied. d235's probe, rows 3 and 11, places it in both builds' specs.
- `real_specs` is unchanged, and no real-history plant ran for this finding. The fixture never calls git.
- A clause moved in with no carrier anywhere still reds as uncarried under `--exit` unless the owner's own specs hold
  the release line, as before this fix.
- `moved-token` cannot plant a clause whose every token is in the carrying build's own text. It exits with a message
  naming the clause.
