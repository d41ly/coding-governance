# TOOL-aTrimmedWait-8 — a declined staged render leaves the tree as it found it, and the paths the closing review found untested are armed

**Status:** INPROGRESS · rev-2 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 8 · ratified 2026-11-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aTrimmedWait-8-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-8-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-8-promotion.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-8-promotion.md) | research | — |
| [2026-11-14-prompt-TOOL-aTrimmedWait-8-ruling.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-8-ruling.md) | research | TOOL-aTrimmedWait-9 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of units 1 to 7, round 1
(`memory/builds/aTrimmedWait/reviews/2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md`),
left six items in the memory-tree write set. <!-- DERIVED from that record's M1 M3 M4 M5 M6 L1 -->
Two are defects in `--write-staged`: a refusal reached after the render started leaves the worktree
or the index changed, against unit 3's rule that a decline writes nothing. <!-- DERIVED: M1 L1 -->
The other four are verification gaps, where code this build added can regress while every gate
stays green. This unit closes them as the record states each one, and brings the help page's
decline list up to date with the decline M1's fix adds.

## 2. Scope (IN)

- **S1** — Review record, "M1 — `--write-staged` writes and stages the render before it raises the
  view refusal". In staged mode, `cmd_write` declines a Problem from `render_asbuilt_view` before
  anything is written: it prints `build-index: render NOT staged — <the Problem>` and returns 1. A
  `git add` that refuses puts back every path the mode touched, through S2's restore. The
  as-built fixture these arms need is built by `_build_design_fixture`, extracted from
  `test_asbuilt_view`. Observed by AC1, AC2, AC11.
- **S2** — Review record, "L1 — `--write-staged` rewrites the as-built view before `plan()` can
  raise", the skeptic's class-level fix. Every path the staged mode writes or unlinks, from the
  as-built view through the orphaned shards, has its prior bytes recorded first. One `finally`
  puts them all back when the mode leaves before `git add` succeeds, on any exception and on every
  decline return. The guarded branch keeps no restore of its own, so the restore lives once.
  Observed by AC3, AC4.
- **S3** — Review record, "M5 — The guarded decline's view restore and the orphan staging have no
  test". A `test_staged_write` arm plants a guarded backlog view while the armed as-built view's
  bytes move. A second arm stages an orphaned ledger shard's removal. The foreign-index decline
  arm gains the unchanged `git status --porcelain` assertion its siblings carry. Observed by AC4,
  AC5, AC6.
- **S4** — Review record, "M4 — No arm exercises the `.lock` or relative-path arms of the staged
  index rule". Two `test_staged_write` arms run the mode with `GIT_INDEX_FILE` set to a copy of
  the index named `<f>/.git/index.lock`, and to the relative `.git/index`. Observed by AC7.
- **S5** — Review record, "M6 — The scoped hygiene fixture sets no `SPEC_EDGES_CUTOFF`, so the
  scoped edge reading never runs". The scoped12 fixture conf sets `SPEC_EDGES_CUTOFF`, and a third
  build `tThree` plants a one-way edge and a sibling's payload-less edge bullet. The left-shift arm
  asserts the scoped conf arms every cutoff key a `SCOPED` branch of the producer tests, as §8 F1
  rules. Observed by AC8, AC9.
- **S6** — Review record, "M3 — The AC6 arm reads the hygiene producer, but its leg's guard does
  not name that file". `{prefix}/memory-tree/check-memory-hygiene.sh` joins the guard of the
  `branch-guard self-test` leg in `tools/gate-legs.json`. Observed by AC10.
- **S7** — §8 F2's ruling. `help/commit-render.md`, section "When it declines", gains a sixth case:
  the as-built view cannot be rendered. The same section gains one sentence: a refusal while the
  mode renders or stages puts back every file it wrote, and the commit is refused as before.
  Observed by AC12.

## 3. Non-goals (OUT)

- No item of the record outside the six S1 to S6 close. M2, L2 and M7 are TOOL-aTrimmedWait-9's,
  in a disjoint write set.
- No change to plain `--write`. Its view is still written before `plan()`, and a refusal there
  leaves it written, as at base. Only the staged mode gains the restore.
- No change to `check_staged_write`, to the hook, to `.githooks/pre-commit.test.sh` or to
  `tools/memory-tree/check-memory-hygiene.sh`. M4's alternative, a hook arm running the real
  generator under `git commit -a`, is rejected in §4.
- No meta-check over every shell suite's reads. That is M3's class gate, handed off below.
- No factory for `test_coverage_region`'s design fixture. Its recipe differs: two builds' chains, a
  nodes module and its own `git init`.
- No help page edit beyond S7's case and sentence, and no other page.
- No kit version bump. The build moves versions once, after its last code move.

### Edges

- **hands-off** external — a gate that reds a shell suite reading a file outside its leg's guard,
  M3's left-shift class. `tools/run-gates/py_reads.py` walks Python suites only, and
  `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md` records a shell walker as a build of
  its own. That record stays the checklist entry for a diff touching `tools/gate-legs.json`.
- **consumes-from** external — the kickoff manifest's `last-audit` re-stamp. The pre-commit
  manifest leg demands it of any commit staging a watched file, and `tools/gate-legs.json` is
  watched (`memory/guides/SESSION-KICKOFF.md@7626f651:7`). It is commit-time collateral, as
  unit 3's build commit carried it, and not part of this design.

## 4. Design

### The staged window, today

`cmd_write` (`tools/memory-tree/gen_build_index.py@fb93e554:3284`) catches a Problem from
`render_asbuilt_view` into `refused` (`tools/memory-tree/gen_build_index.py@fb93e554:3301`). In
staged mode it then writes the moved view (`tools/memory-tree/gen_build_index.py@fb93e554:3312`),
calls `plan()` (`tools/memory-tree/gen_build_index.py@fb93e554:3313`), writes the moved artifacts
and removes the orphans (`tools/memory-tree/gen_build_index.py@fb93e554:3332`,
`tools/memory-tree/gen_build_index.py@fb93e554:3335`), and runs `git add`
(`tools/memory-tree/gen_build_index.py@fb93e554:3346`). Only then does it raise `refused`
(`tools/memory-tree/gen_build_index.py@fb93e554:3365`). A refused `git add` raises with the files
written (`tools/memory-tree/gen_build_index.py@fb93e554:3349`). A `plan()` Problem, such as a
`parents:` entry naming no build folder (`tools/memory-tree/gen_build_index.py@fb93e554:2790`),
leaves the view rewritten. Only the guarded decline restores the view
(`tools/memory-tree/gen_build_index.py@fb93e554:3314`).

### The staged window, after

1. `check_staged_write`, `check_archives_tracked` and the view render run as today.
2. **S1.** `if staged and refused:` prints `build-index: render NOT staged — {refused}` and
   returns 1. Nothing has been written. The late `raise refused` stays for plain `--write`.
3. **S2.** In staged mode, `undo` is a dict from a repo-relative path to its prior bytes, or
   `None` when the file was absent. A path enters it once, before its first write or removal.
   `landed` starts false.
4. `try:` the view write, `plan()`, the guarded decline, the moved-artifact derivation, the
   no-bytes-moved decline, the artifact writes, the orphan removals and `git add`. `landed`
   turns true on the line after `git add` returns.
5. `finally:` when `staged and not landed`, each path in `undo` gets its bytes back, or is
   removed when its value is `None`.
6. The prints after `git add` sit outside the window, as today.

The guarded branch keeps its print and its `return 1` and loses its inline restore. The
no-bytes-moved decline is reached only with the view unmoved, so `undo` is empty there.

The restore puts back file bytes only. A refused `git add` writes no index, and a Problem before it
has touched no index, so the index needs no restore. The original exception propagates unchanged,
so `main()` still prints it and exits 1.

M1's fix offered two ways to handle a refused `git add`: restore what was written, or probe that
`git add` works before writing. This design takes the restore, because L1's class fix already puts
one `finally` over the same window. A probe would be a second mechanism for the same window.

### The arms

`test_staged_write` (`tools/memory-tree/gen_build_index.py@fb93e554:4710`) keeps its tree `<f>`
and gains a second tree `<d>` under the same base directory, so the unit 3 arms read the bytes they
read today. Each new arm restores `<f>` or `<d>` with `git reset -q --hard` before it stages its
case, as `write_staged_change` does.

- The `.lock` arm copies `<f>/.git/index` to `<f>/.git/index.lock` and removes that file before
  any later git command, because a file of that name refuses every index write.
- The refused-add arm plants an empty `<f>/.git/index.lock` with `GIT_INDEX_FILE` unset. A read
  probe on node a, 2026-11-14 (PINNED), showed `git add` exiting 128 with the lock planted while
  `git diff --name-only` exits 0, so `check_staged_write` passes and the add refuses. The arm
  removes the lock and then reads `git status --porcelain`.
- The foreign-index arm (`tools/memory-tree/gen_build_index.py@fb93e554:4774`) reads
  `git status --porcelain` before and after the run.
- The no-bytes-moved arm (`tools/memory-tree/gen_build_index.py@fb93e554:4763`) gains no
  porcelain assertion. A write of unmoved bytes changes no status, so no break could red one. The
  record's left-shift names it, and this is the one place the design narrows it.

### The as-built fixture factory

`test_asbuilt_view` builds an armed design inline
(`tools/memory-tree/gen_build_index.py@fb93e554:5231` to
`tools/memory-tree/gen_build_index.py@fb93e554:5238`), and `<d>` needs the same one. The charter's
`[reuse]` rule therefore extracts it as `_build_design_fixture(tmp) -> tuple`. The helper runs
`_fixture(tmp)`, writes the record, writes the view's `merge=ours` line into `.gitattributes`,
commits `design`, and appends the `Baseline:` line naming that commit. It returns
`(texts, record_rel, view_rel, sha)`. `test_asbuilt_view` calls it in place of those lines and keeps
its own `write_conf`, so its arm lines are unchanged.

`<d>` is `_build_design_fixture` plus `STAGED_RENDER="1"` and the four `DESIGN_*` keys in its conf,
rendered with `--write` and committed. A read probe on node a, 2026-11-14 (PINNED), confirmed that
a `DESIGN_BASELINE` of forty zeros makes `render_asbuilt_view` raise its Problem on a `_fixture`
tree. The same probe showed that `BACKLOG_MODE="builds"` with `ASK_CUTOFF="2099-01-01"` renders
the ARCH family's backlog view, and that an authored row appended to it makes `plan()` report it
guarded. A third probe showed `parents: nope` in tOne's front matter makes `plan()` raise.

### The scoped edge fixture

The scoped12 conf (`tools/memory-tree/check-memory-hygiene.test.sh@2b3fa466:1303`) gains
`SPEC_EDGES_CUTOFF="2026-09-08"`, the value this repository sets
(`.memory-tree.conf@b6aad21f:383`). Every existing plant is dated 2026-08-26 or earlier, and the
edge arm registers only specs dated on or after the cutoff
(`tools/memory-tree/check-memory-hygiene.sh@e3771865:2232`). So no tOne or tTwo verdict moves.

A third build `tThree` is committed in the tree's first commit. Its three specs are `good10`
(`tools/memory-tree/check-memory-hygiene.test.sh@2b3fa466:328`) renamed and redated to 2026-09-08,
with a `### Edges` block inside §3. `good10` carries the ten-section canon the engine's default
`SPEC10_CUTOFF` demands at that date (`tools/memory-tree/check-memory-hygiene.sh@e3771865:111`).

| Spec | Edges body |
|---|---|
| `ARCH-tThree-1` | `- **hands-off** ` then `ARCH-tThree-2` in backticks, then ` — the second half.` |
| `ARCH-tThree-2` | `none` |
| `ARCH-tThree-3` | `- **hands-off** — something, somewhere.` |

The record's fix plants the pair in tOne. tThree carries it instead for two reasons. tOne's specs
predate any cutoff that would leave tOne-1 clean. And the `--build tOne` arm counts four specs,
per `tools/memory-tree/check-memory-hygiene.test.sh@2b3fa466:1337`.

`--spec` on tThree-1 grades it as `P` and reads tThree-2 and tThree-3 as `J` siblings
(`tools/memory-tree/check-memory-hygiene.sh@e3771865:2136`). The reciprocity finding is tThree-1's
own, so it is printed. tThree-3's payload finding belongs to a `J` sibling, and `stg` keeps it out
(`tools/memory-tree/check-memory-hygiene.sh@e3771865:3030`). The tThree plants also carry a base
`0123abcd`, which the base-resolve arm reports; no assertion reads that line.

### The derived-key arm (§8 F1)

The suite derives a key set from `$SCRIPT`. It takes every `[A-Z0-9_]+_CUTOFF` on a line that tests
`"$SCOPED" = 1` or reads `| SCOPED`. Run over the producer on 2026-11-14, that set is
`SPEC_EDGES_CUTOFF` alone (DERIVED: the arm re-derives it each run). The arm reds on an empty set.
For each key, the scoped conf must set a non-blank date on or before the filename date of a
committed scope-tree spec. Every read is `$HERE`-relative, as the suite's are today
(`tools/memory-tree/check-memory-hygiene.test.sh@2b3fa466:15`).

### The leg guard

`branch-guard self-test` (`tools/gate-legs.json@c487c5fe:619`) guards `.githooks/` and
`{prefix}/lib/`. Its suite reads the `fail()` literal out of the hygiene producer
(`.githooks/pre-commit.test.sh@6afa5a00:294`). `changed()` skips a guarded leg when no guard path
moved (`tools/run-gates/run-gates.sh@bfc3ad49:539`). The guard gains the exact file
`{prefix}/memory-tree/check-memory-hygiene.sh`, spelled as the `memory hygiene` leg spells it.
That path then sits in two guards. <!-- DERIVED from tools/gate-legs.json@c487c5fe and this edit -->
Two is under `BROAD_LEG_FLOOR` (`tools/check-spec-tokens.py@42905ba5:421`). The generator is not
added, because the suite uses a stand-in for it.

### The help page (§8 F2)

`help/commit-render.md` lists the decline cases under "When it declines"
(`help/commit-render.md@ceac7113:38`). S7 adds one bullet after the guard case, "the as-built view
cannot be rendered, so the render has nothing to stage", in the list's own lowercase, semicolon
style. After the list it adds one sentence: a refusal while the mode renders or stages puts back
every file it wrote, and the hook refuses the commit as before. The page carries no fenced command
for this, so no command row moves.

### What it does not check

- `--legs-for` reads a guard the way `tools/check-spec-tokens.py` reads it. `changed()` diffs the
  same pathspec through git. The two agree for an exact file, and nothing proves they agree in
  general.
- A restore that itself fails replaces the original exception, and no arm plants that case.
- A decline added to `cmd_write` later without an arm is caught by nothing.
- No arm runs the real generator under a real `git commit -a`. AC7 hands the mode the lock-named
  index directly.
- The guard edit covers the one file M3 names. Any other file `.githooks/pre-commit.test.sh` reads
  from outside its guard is the handed-off class.
- The derived-key arm sees a cutoff only on the line that tests `SCOPED`. A condition split across
  two lines is invisible to it.

### Inventory

| Minted | Kind | Graded by |
|---|---|---|
| `_build_design_fixture` | selftest helper function | `lexicon naming predicates`, cell `py.function` |
| `undo`, `landed` | locals of `cmd_write` | none |
| `tThree` | fixture build in the scoped12 tree | the suite's own arms |

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/gate-legs.json`
- `help/commit-render.md`

### Alternatives rejected

- **A `try` around `plan()` alone.** The record judges it instance-only: it misses the guarded
  return and a refused `git add`.
- **Probing `git add` before any write.** A second mechanism over the window the `finally` already
  covers.
- **A hook-suite arm running the real generator under `git commit -a`.** It lives in
  `.githooks/pre-commit.test.sh`, outside this write set. The two generator arms observe the same
  index rule directly.
- **Planting the edge pair in tOne.** It moves tOne-1's clean verdict and the `--build tOne` count.

## 5. Production-readiness checklist

- security — No new write path. The staged write path now writes nothing on any refusal, which
  closes a case where a refused commit left paths staged that the user never staged.
- perf / scale — A clean staged render pays one extra read of each moved path's bytes before its
  write. `test_staged_write` gains eight generator runs and three `--write` setups. <!-- DERIVED from §6 -->
  It runs ten generator runs today. <!-- DERIVED from tools/memory-tree/gen_build_index.py@fb93e554:4710 -->
  A re-declared row in
  `tools/run-gates/selftest-budgets.txt`, if the leg's wall time crosses it, is the main loop's at
  the close.
- error / empty / loading states — Every refusal inside the window restores, and its message is the
  one it prints today. The view refusal prints under the decline prefix.
- observability — One new decline line, `build-index: render NOT staged — as-built view — ...`.
- risks — A guard edit moves the leg manifest, so the pre-push hook forces a full run at the next
  push. The `undo` read happens after `derive_moved_artifacts` has already read the same bytes.
- testing — AC1 to AC7 and AC11 are generator runs in fixture repositories. AC8 is a hygiene run in
  the scoped tree. AC9 and AC10 are probes of the producer and the manifest. The arms of §7 repeat
  AC1 to AC9.
- migration — None. Plain `--write` and every non-staged verb are unchanged.
- user docs — `help/commit-render.md` gains the view refusal as a decline case and the restore
  sentence, S7, as §8 F2 rules.

## 6. Acceptance criteria

`<f>` is the fixture of `TOOL-aTrimmedWait-3` §6: a `_fixture` tree with `STAGED_RENDER="1"`,
rendered with `--write` and committed, then the spec's status changed from `INPROGRESS` to
`DEFERRED` and staged. `<d>` is `<f>` built through `_build_design_fixture`, with the four
`DESIGN_*` keys in its conf, rendered and committed before the same staged status change. `<gbi>`
is `tools/memory-tree/gen_build_index.py` in this worktree, run with the fixture as its working
directory. "Unchanged" means `git status --porcelain` and `git diff --cached --name-only` print the
same bytes before and after the run.

- **AC1** — When `<d>`'s conf sets `DESIGN_BASELINE` to forty zeros and is staged,
  `python <gbi> --write-staged` exits 1 and prints
  `build-index: render NOT staged — as-built view — DESIGN_BASELINE`, and the tree is unchanged.
  Red when: the refusal is raised after the writes, so the build README is staged. That is base
  behaviour.
- **AC2** — When an empty `<f>/.git/index.lock` is planted with `GIT_INDEX_FILE` unset, the run
  exits 1 and prints `git add refused the rendered artifacts`. After the lock is removed, the tree
  is unchanged and the build README holds its committed bytes.
  Red when: the files written before the refused add stay in the worktree. That is base behaviour.
- **AC3** — When `<d>`'s view carries a staged hand edit and tOne's README a staged `parents: nope`,
  the run exits 1 naming `parents: names 'nope'`, and the tree is unchanged, the view at its staged
  bytes. When the view's removal is staged instead of an edit, the same run leaves no view file.
  Red when: the view is left rewritten, or a view the run created is left behind. Base leaves it
  rewritten.
- **AC4** — When `<d>`'s conf adds `BACKLOG_MODE="builds"` and `ASK_CUTOFF="2099-01-01"`, the tree
  is rendered and committed, an authored row is appended to the ARCH family's backlog view and
  staged, and the as-built view carries a staged hand edit, the run exits 1. It prints
  `render NOT staged — the data-loss guard holds` naming the ARCH view, and the tree is unchanged.
  Red when: the guarded return skips the restore, so the view is left rewritten.
- **AC5** — When `<f>` carries a committed ledger shard for the month `2020-01`, which no record
  renders into, the run exits 0 and prints a `build-index: staged` line naming that shard. The file
  is gone, and `git diff --cached --name-only --diff-filter=D` lists it.
  Red when: the orphans drop out of the staged set, so the removal is left unstaged.
- **AC6** — When `<f>` runs with `GIT_INDEX_FILE` set to a copy of its index named `other-index`,
  the run exits 1 naming that index, and the tree is unchanged.
  Red when: the index decline is reached after a write.
- **AC7** — When `<f>` runs with `GIT_INDEX_FILE` set to a copy of its index at
  `<f>/.git/index.lock`, the run exits 0 and prints `build-index: staged` naming the build README.
  When it runs with `GIT_INDEX_FILE=.git/index`, a relative path, it exits 0 the same way.
  Red when: `own + ".lock"` leaves the allowed set, or the compare stops resolving a relative path,
  so `git commit -a` or a plain commit is declined.
- **AC8** — When `check-memory-hygiene.sh --only 12 --spec` names tThree-1's path in the scoped
  tree, it exits 1. It prints a line holding `declares no matching **consumes-from**` for
  tThree-1, equal to the unscoped `--only 12` run's line for it, and no line naming
  `2026-09-08-spec-tThree-3.md`.
  `--build tOne` still prints `over 4 spec(s) of tOne`. <!-- PINNED: check-memory-hygiene.test.sh@2b3fa466:1337 -->
  The arm reads it unchanged from base.
  Red when: `|| SCOPED` leaves the sibling tagging, so the line is missing, or `| SCOPED` leaves
  the edge awk's `stg`, so tThree-3's payload finding leaks into the run.
  fixture: the suite's scoped tree, built in its temp directory. Its conf arms
  `SPEC_FORMAT_CUTOFF`, `BASE_RESOLVE_CUTOFF` and `SPEC_EDGES_CUTOFF`, and `SPEC10_CUTOFF` takes
  the engine's default.
- **AC9** — When
  `grep -E '"\$SCOPED" = 1|\| SCOPED' tools/memory-tree/check-memory-hygiene.sh | grep -oE '[A-Z0-9_]+_CUTOFF' | sort -u`
  runs, it prints exactly `SPEC_EDGES_CUTOFF`. And
  `grep -c 'SPEC_EDGES_CUTOFF="2026-09-08"' tools/memory-tree/check-memory-hygiene.test.sh` prints
  2: the scoped12 conf now sets the key at the tThree plants' date, beside the PR4 conf.
  At base the grep prints 1. <!-- PINNED 2026-11-14, check-memory-hygiene.test.sh@2b3fa466:4601 -->
  Red when: the derivation prints nothing, so the arm would grade an empty set, or the grep prints
  1, so the scoped conf lacks the key.
  figure: the key set is DERIVED by the command, never pinned.
- **AC10** — When `python tools/check-spec-tokens.py --legs-for tools/memory-tree/check-memory-hygiene.sh`
  runs, it prints the row
  `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh [selftests/repo]`.
  The unit's commit adds one line to `tools/gate-legs.json` and removes none.
  Red when: the guard lacks the file, as at base, or names `tools/memory-tree/`, which prints the
  row as broad.
- **AC11** — When `grep -c '_build_design_fixture(' tools/memory-tree/gen_build_index.py` runs, it
  prints 3: the definition and two callers. `grep -cF 'merge=ours\n"'` over the same file prints 1,
  the factory's `.gitattributes` write.
  At base the first prints 0 and the second 1. <!-- PINNED 2026-11-14, gen_build_index.py@fb93e554 -->
  Red when: `<d>` copies the design recipe a second time instead of calling the factory, so the
  second count reads 2.
- **AC12** — When `grep -c 'as-built view cannot be rendered' help/commit-render.md` runs, it
  prints 1, and `grep -c 'puts back every file it wrote' help/commit-render.md` prints 1.
  At base each prints 0. <!-- PINNED 2026-11-14, help/commit-render.md@ceac7113 -->
  Red when: the page still lists only the base decline cases, so a reader meeting the view refusal
  finds no line for it.

## 7. Gates

`build-index selftest` · `memory-hygiene self-test` · `branch-guard self-test` · `lexicon naming predicates` · `memory hygiene` · `docs` · `tier2-review self-test` · `policy fixtures` · `run-gates gov canary` · `run-gates canary` · `measure-legs selftest`

The first six grade this unit's change, `docs` for S7's page, which trips no guarded leg. The last
five are owed by a guard a path of the estimate trips. The main loop runs the merge bar once, at
the close. No leg is added.

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 · `test_staged_write` over `<d>` and `<f>` with each refusal staged in turn; RED at base, where the refused view, the refused add and the `plan()` raise each leave the tree changed · none
New arm: tools/memory-tree/gen_build_index.py · covers AC4 AC5 AC6 AC7 · `test_staged_write`; GREEN at base, observed RED on staged breaks: the guarded return moved past the restore, the orphans dropped from the staged set, `check_staged_write` moved after the writes, and `own + ".lock"` dropped or the compare made a plain string compare · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC8 · the tThree plants; RED with `|| SCOPED` dropped from the sibling tagging, and again with `| SCOPED` dropped from `stg` · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC9 · the derived-key arm; RED with `SPEC_EDGES_CUTOFF` dropped from the scoped conf, and on a producer copy carrying a planted `SCOPED` line testing a key the conf does not set · none

AC10 has no arm: it is manifest data, and its class gate is handed off in §3. AC11 and AC12 have
no arm.

## 8. Open questions

- **F1 — Which cutoff keys must M6's left-shift arm require the scoped fixture conf to set?** The
  record's left-shift reads "every cutoff key this repo's `.memory-tree.conf` sets".
  - (a) The record's literal: every `*_CUTOFF` key the host repository's conf sets.
    That conf sets 28 such keys. <!-- PINNED 2026-11-14, .memory-tree.conf@b6aad21f -->
    The suite would read a file outside its kit, where every read
    today is `$HERE`-relative, so the arm moves with the host's conf and an adopter's is a
    different population. Several of those keys, `ROUTED_COMMIT_CUTOFF`, `ASK_CUTOFF` and
    `LEDGER_TOKEN_CUTOFF` among them, reach no check-12 path: check 12's awk takes none of them
    (`tools/memory-tree/check-memory-hygiene.sh@e3771865:2171`). The arm grades presence, so a
    far-future value passes while arming nothing
    (`memory/gotchas/pin-gated-checks-arm-nothing-without-a-pin.md`).
  - (b) Derived from the producer, as §4 "The derived-key arm" states: every `*_CUTOFF` on a line
    testing `SCOPED`, today `SPEC_EDGES_CUTOFF`, set to a date that arms a committed plant, red on
    an empty set. It is self-contained and grades arming, not presence. It is blind to a condition
    split across lines.
  Recommendation: (b). It gates the class the finding names, scoped paths a fixture leaves
  unarmed, and cannot pass vacuously. AC9 and its arm are written for (b). Under (a), AC9 becomes
  a comparison of the scoped conf's keys with the host conf's, and the arm's staged break becomes
  a host key the scoped conf omits.
  RESOLVED (owner, 2026-11-14): (b), the derived set.
- **F2 — Does `help/commit-render.md` gain the view refusal as a decline?** The page's section
  "When it declines" lists its decline cases under "The mode writes nothing".
  It lists five today. <!-- PINNED 2026-11-14, help/commit-render.md@ceac7113:38 -->
  S1 adds another that prints the same prefix. The brief limited this unit to three files.
  - (a) Add one bullet, "the as-built view cannot be rendered", and one sentence that a refusal
    while rendering or staging puts back every file the mode wrote. The rev recording the ruling
    adds the page to the estimate and the legs `--legs-for` names for it to §7. The write set stays
    disjoint from TOOL-aTrimmedWait-9's.
  - (b) Leave the page. It already says a decline writes nothing and that any other failure refuses
    as before, and the new line names its own reason.
  Recommendation: (a). The charter's `[docs]` rule outranks the brief's scope, and under (b) the
  page's list omits a case the mode prints under the decline prefix.
  RESOLVED (owner, 2026-11-14): (a), update the page. S7, AC12 and the `docs` leg fold it in.

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.
- rev-2 · 2026-11-14 · §1 §2 §3 §4 §5 §6 §7 §8 · S7 AC12 · the owner resolved F1 to (b), the derived
  key set, and F2 to (a), the page update, each through its own question relayed by the main loop.
  F2 folds in as S7, AC12, `help/commit-render.md` under Files touched, §4 "The help page" and the
  `docs` leg in §7. Every figure now carries its pin on its own line. The status tail gains
  `ratified 2026-11-14`.

## 10. Reuse audit

The seam is `cmd_write`'s own staged branch in `tools/memory-tree/gen_build_index.py`. Its
`view_prev` restore becomes the one `finally` over the whole window, and the guarded branch's
inline copy is deleted. The arms extend `test_staged_write`, and the design fixture is extracted
from `test_asbuilt_view` rather than copied. The scoped arms extend the scoped12 block and its
`good10` helper. The guard joins the existing manifest row. `tools/codebase-map/reuse_lookup.py`
for "restore files a staged render wrote when the render is declined or git add fails" ranked
name stems only (`git`, `render`, `write_file`), and no seam closer than these. Recall returned
the review record's L1 text and unit 3's §4, and an unrelated rollback in the deployer kit; no
record holds a staged-write rollback in this generator.

Recall terms used: write-staged decline restore view_prev finally rollback undo git-add refused
guarded as-built scoped fixture SPEC_EDGES_CUTOFF guard
