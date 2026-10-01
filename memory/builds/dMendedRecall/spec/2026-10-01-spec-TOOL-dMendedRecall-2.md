# TOOL-dMendedRecall-2 — the inherited-red auto-file re-renders the generated views it makes stale, and stages them with its rows

**Status:** CLOSED · rev-4 · 2026-10-01 · node d · Tier-2 · base 1f915870 · streams tooling · order 1 · closes TOOL-dAlignedCarrier-9 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-dMendedRecall-2-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-dMendedRecall-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-dMendedRecall-1-build-brief.md](../prompts/2026-10-01-prompt-TOOL-dMendedRecall-1-build-brief.md) | journal | TOOL-dMendedRecall-1 TOOL-dMendedRecall-3 |
| [2026-10-01-prompt-TOOL-dMendedRecall-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-dMendedRecall-1-spec-brief.md) | journal | TOOL-dMendedRecall-1 TOOL-dMendedRecall-3 |
| [2026-10-01-prompt-TOOL-dMendedRecall-2-fold-brief.md](../prompts/2026-10-01-prompt-TOOL-dMendedRecall-2-fold-brief.md) | journal | — |
| [2026-10-01-review-TOOL-dMendedRecall-1-closing-diff-round1.md](../reviews/2026-10-01-review-TOOL-dMendedRecall-1-closing-diff-round1.md) | diff-review | TOOL-dMendedRecall-1 TOOL-dMendedRecall-3 |
| [2026-10-01-review-TOOL-dMendedRecall-2-closing-diff-round2.md](../reviews/2026-10-01-review-TOOL-dMendedRecall-2-closing-diff-round2.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

When `gates-green` reads a red whose every leg is INHERITED, `write_inherited_asks` files an ask per
leg in the build's `BACKLOG.md` and stages the rows. It renders nothing, so the generated views the
index generator derives from that file go stale in the same index, and the in-place close's own
records commit is then refused by the pre-commit's hygiene check 9 after the whole flagged bar was
paid. This unit makes the writer of the rows also render and stage the views they move, so the
close commits `records(<slug>): close — LANDING` with the views current.

## 2. Scope (IN)

- **S1** — `write_inherited_asks` in `tools/unattended/unattended.sh` counts the asks one call
  FILES: written, staged and read back as one OPEN HIGH ask. A reused ask, the dark path under a
  blank `ASKS_CMD`, a leg it could not file, and rows it rolled back count nothing. After its loop,
  a count above zero calls `write_ask_views` once with that count; a count of zero calls nothing,
  so every path that files nothing prints the bytes it printed at BASE. Observed by AC1, AC3, AC5.
- **S2** — `write_ask_views` is minted in `tools/unattended/unattended.sh`, beside
  `write_backlog_rows`. It resolves the generator with the library's `resolve_index_generator` and
  the interpreter with `resolve_python`, and requires that path to be a file at the repository top,
  where the driver already runs. It records the paths carrying unstaged or untracked changes, runs
  `<python> -B <generator> --write` under `run_bounded`, records them again, and stages with
  `GIT add -A --` exactly the paths in the second set and not in the first. `-B` keeps the render's
  own imports from leaving bytecode caches beside the kit, which in a tree that does not ignore them
  are new untracked paths the delta rule would stage (rev-2). It prints one line, §4's success
  spelling. Observed by AC1, AC2.
- **S3** — A path that carried unstaged or untracked changes BEFORE the render is never staged by
  it. Its hash is taken before and after, and one the render changed too is named on the success
  line as left unstaged, because staging it would commit work the run did not do. Observed by AC4.
  THE INPUT SIDE, rev-3: when any INPUT of the views carries a change the index does not hold before
  the render, `write_ask_views` runs no render and stages no view. The inputs are every tracked path
  under the memory root with an unstaged change, deletions included, and `.memory-tree.conf` with an
  unstaged change or untracked, because the generator reads the conf off the disk either way. An
  untracked path under the memory root is no input: the generator lists its inputs with
  `git ls-files`. It prints §4's miss spelling with the dirty-input `<why>`, naming the inputs, and
  the repair to stage or discard them and run the generator's `--write`, and returns 1 as S4 does.
  It never commits a view derived from a change the operator has not staged. Observed by AC4, AC7.
  rev-4: the GENERATOR'S OWN CODE is an input too. `--write` imports its siblings from the directory
  the resolved generator lives in, so a tracked path there with an unstaged change is a dirty input,
  asked of git with that directory as the pathspec; a generator at the root names only its own
  top-level modules. Observed by AC8.
- **S4** — A miss is named and does not refuse. When no generator resolves, the resolved path is
  not a file at the top, or the render exits non-zero or is killed by its bound, `write_ask_views`
  prints §4's miss spelling, which carries `derive_index_repair`'s text, stages whatever paths the
  render did change under S3's rule, and returns 1. The caller continues: the item's verdict, its
  other lines and the close's exit are what they would have been, and no `fail` branch is added.
  A stage that git refuses after a render, a held index lock say, is named on §4's stage-refused
  line and returns 1 the same way, because the success line would claim paths the index does not
  hold (rev-2). Observed by AC3.
- **S5** — The comment block opening "STAGED BY THIS ITEM" (`tools/unattended/unattended.sh:6808`)
  says the views are rendered and staged with the rows, by `write_ask_views`, so whichever step
  commits the rows commits the views. Observed by AC5.
- **S6** — Two arm sets are written in `tools/unattended/unattended.test.sh` and not run. In the
  inherited-red block, the AC9 MET arm gains a `hit` on the miss spelling: that fixture holds no
  generator at the path the resolver names. After that block, a new self-contained block builds the
  AC1 fixture and asserts AC1's commit subject, AC2's committed paths and clean `--check`, and AC4's
  untouched paths and its left-unstaged naming. The inherited-red block's F4 slice, which runs the filer
  with its neighbours doubled, gains a double for the helper, so the sliced filer calls no function
  the slice lacks; its arms read whether the double was called and with what count (rev-2).
  At rev-3 the new block grades the commit rather than the worktree: AC2's and AC4's `--check`
  arms run over a clean checkout of the commit, and it gains AC4's split arms and AC7's two.
  Observed by AC6.

## 3. Non-goals (OUT)

- `write_close_commit`. It already commits everything staged; with the views staged it needs no
  change, and its refusal 69 keeps its text.
- The stop contract's §13 sentence on the owner-on-record ask (`tools/unattended/STOPS.template.md`
  and its render). It stays true, since the rows are still staged and read back; saying that the
  views ride with them is a change to a carrier no accept clause of this build names, which M3's
  veto 2 leaves to the owner.
- Rendering at commit time in `write_close_commit`, or in the Skill's close sequence. §8 F1 says
  why the writer renders instead.
- `GENERATED_INDEXES` in `.unattended.conf`. It declares the index outputs and their generators for
  the history legs, and a build README's generated regions are outside it; it is not the staging
  set here.
- Any other auto-written records surface. TOOL-dDerivedDocket-42 owns the question of one
  declaration for every path a run's machinery writes.
- The unattended kit version. The orchestrator moves it once, at VERIFYING.

### Edges

- **hands-off** external — the stop contract's §13 sentence, to the owner under veto 2, if the
  views are to be named there.
- **hands-off** external — the clean reading of the S6 arms, owed with TOOL-dDerivedDocket-76 under
  the build README's waiver of this kit's own suites.

## 4. Design

### Evidence

Read at `1f915870` on 2026-10-01, PINNED to that date.

- `write_inherited_asks` (`tools/unattended/unattended.sh:6900`) stages each ask with
  `GIT add -- "$bl"` and reads it back through `ASKS_CMD`; nothing in it or in its caller, the
  `gates-green` item of `dod_met` (`:7605`), runs a renderer.
- `write_close_commit` (`:7187`) commits the whole index under `records(<slug>): close — LANDING`
  with hooks on, and reports refusal 69 when the commit fails.
- The pre-commit's memory-tree leg runs `check-memory-hygiene.sh --staged`, whose check 9 runs
  `gen_build_index.py --check` whenever a `.md` file is staged
  (`tools/memory-tree/check-memory-hygiene.sh:1039-1041`). `--check` renders from the working tree
  and compares; `--write` writes every artifact, prints verdicts without refusing on them, and exits
  1 only when its data-loss guard kept one view unwritten (`tools/memory-tree/gen_build_index.py:2306-2322`).
- What the views are, measured on the one real occurrence: `10663361`, dAlignedCarrier's close made
  by hand, carries the record, the `BACKLOG.md` rows, and three rendered files beside them,
  `memory/backlog/TOOL.md`, the build's `README.md` and `memory/ledger/2026-09.md`. The README's
  generated regions are outside `GENERATED_INDEXES`, which is why S2 stages by observed change
  rather than by that declaration.
- `resolve_index_generator` (`tools/unattended/lib-unattended.sh:128`) answers the generator's path
  relative to the top of the repository holding the kit, and `derive_index_repair` (`:142`) spells
  the repair from it. The driver `cd`s to the repository top at start (`unattended.sh:458`), so the
  relative path resolves there. When the driver runs from a kit outside the repository it acts on,
  as the suite does, the path names nothing there, and S2's file test is what keeps the render from
  running anywhere but the tree being closed.
- `--close` does not call `check_clean`, so a tree carrying other changes can reach this item;
  S3 is not hypothetical. CORRECTED at rev-2: that holds under `primary` only. Under `in-place`,
  `check_inplace_preconditions` refuses a tree that is not porcelain-clean with refusal 62 before
  the bar runs, measured over this unit's fixture, so there a dirty path can reach the item only
  through something the bar itself writes. AC4 therefore reads the `primary` close.
- ADDED at rev-3, from the closing review's M1 and a fixture read on 2026-10-01: the rev-2 S3
  guarded the render's output side only. `gen_build_index.py` lists its inputs with `git ls-files`
  and reads their bytes off the disk (`read_text` at `:247`, the memory-root listing at `:851`), and
  reads `.memory-tree.conf` with `load_conf` (`:293`) whether it is tracked or not. Under `primary`,
  an unstaged `SPECCED` to `INPROGRESS` flip on a spec's status header was followed by the rev-2
  close staging `memory/LIVE.md`, the family view, the build README and the ledger shard; the
  operator's records commit passed the worktree `--check` pre-commit, and `--check` over a clean
  checkout of that commit read `build-index DRIFT`.

### Spellings

```
gates-green: re-rendered the generated views for <n> filed ask(s) and staged <k> path(s): <paths>
gates-green: re-rendered the generated views for <n> filed ask(s); the render changed no path
gates-green: the <n> filed ask(s) are staged, but the generated views were not re-rendered: <why>; until they are, a records commit meets a stale index — repair: <derive_index_repair>
```

The success spellings take the suffix `; left unstaged, dirty before the render: <paths>` when S3
names a path; a render that moved only such paths reads `and staged 0 path(s): none` before it.
A stage git refuses after the render is its own line, added at rev-2:

```
gates-green: the generated views for <n> filed ask(s) were re-rendered, but git could not stage the <k> path(s) the render moved: <paths>; until it does, a records commit meets a stale index — stage them by hand
```

`<why>` is one of: `no memory-tree generator resolves beside this kit`, `the
generator the resolver names is not a file here: <path>`, or `the generator exited <rc> after
<s>s`, the last followed by `run_bounded`'s captured output indented four spaces, the shape every
other bounded call site of this driver prints. None of them begins `UNATTENDED check`, because none
is a refusal. rev-3 adds a fourth, for S3's input side, whose repair is prefixed:

```
<why>    the views' inputs carry changes the index does not hold, and a render would stage views derived from them: <paths>
<repair> stage or discard those changes, then run <derive_index_repair>
```

The miss line is spelled once in the driver for every `<why>` decided before a render runs, so the
dirty-input line differs from the other two only in those two fields.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `write_ask_views` | shell function, verb `write` | `sh.function` |

Asked of `python tools/lexicon/lexicon.py --suggest write_ask_views --as sh.function`, which read OK
on 2026-10-01. `write`, persist to a store, is the row for a function that puts rendered bytes into
the tree and the index; `render` would name only the generator's half, and `stage` is not a
declared verb.

### Fixture

None in the tree, and AC1 to AC4 read one the pass builds under `%TEMP%` with a short name. It
composes two existing suite blocks of `tools/unattended/unattended.test.sh`, read for their shapes
and not run: the in-place block opening `TOOL-dDerivedDocket-3 — LANDER_MODE`, for its stub lander
and its overrides of the items a fixture cannot meet, and the inherited-red block opening
`TOOL-dDerivedDocket-24 — THE INHERITED-RED POLICY`, for its stub bar writing one INHERITED leg and
its `INHERITED_RED=land` policy. To those it adds this repository's `tools/unattended/`,
`tools/lib/` and the memory-tree kit's python modules under the same relative paths, a
`.memory-tree.conf` declaring `BACKLOG_MODE="builds"` and the fixture's family, `ASKS_CMD` naming
that generator's `--asks` exactly as this repository's conf does, and `core.hooksPath` naming a
`pre-commit` that runs that generator's `--check`, which is the predicate check 9 delegates to. The
fixture is rendered once with `--write` and committed, so `--check` is clean at its base. The BASE
reading swaps in the kit extracted by `git archive 1f915870`. Measured at rev-2, the generator
refuses a tree with no stale-header waiver registry, so the fixture carries an empty one under its
memory root's project folder; it ignores `__pycache__/` as any tree carrying Python does; and the
kit is copied without its own suites, whose literal ids would otherwise feed the id the auto-file
mints. The `tools/lib/` copy turned out unneeded: the driver is copy-installed standalone.
At rev-3 AC7 reads the same fixture under `primary`, its rev-2 reading swaps in the kit the rev-2
pass built, and every `--check` that grades a commit runs over a clean checkout of it, as AC2
states.

### Rollout

No render: nothing this unit edits is a template. The pass edits the driver and the suite, observes
AC1 to AC5 over the fixture, and commits. The rev-3 fold observes AC2, AC4 and AC7 the same way.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Render inside `write_close_commit`, before it commits.** It covers the in-place close only.
  Under `primary` the operator commits the staged records, and on a `hold ·` path the Skill's close
  sequence does; both would still carry stale views. The writer that makes the views stale is the
  one step all three paths share.
- **Stage everything under the memory root after the render.** S3's case is real because `--close`
  does not refuse a dirty tree, and this would commit an operator's unrelated work under the
  close's subject.
- **Stage the `GENERATED_INDEXES` paths.** The 2026-09-30 recovery shows the build README's
  regions moving too, and they are outside that declaration.
- **Roll the rows back when the render misses.** The stop contract gives every inherited leg an
  owner on the record; discarding the ask to keep a commit clean trades the record for the commit.
  S4 keeps the ask and names the repair.

## 5. Production-readiness checklist

- security — N/A: the generator is the repository's own, resolved by the library resolver the
  driver already uses for its repair text, and it writes only under the memory root; no new input
  crosses a trust boundary.
- perf / scale — one generator run per close that files an ask, a few seconds on node `d`, bounded
  by the driver's existing bound; a close that files nothing pays nothing.
- error / empty / loading states — S4's miss line for each failure; a render that changes nothing
  says so; a pre-dirty path is named rather than swept in; a dirty input is named and not rendered
  over.
- observability — one line per render naming what it staged, or why it did not.
- risks — `--write` renders every artifact, so a tree whose index was already stale before the
  close would have that drift staged into the records commit. The pre-commit keeps the default
  branch's index clean. Under `primary` the operator's unstaged edits to the views' inputs can move
  it too, and rev-3's input rule (S3) renders nothing over them rather than stage views derived from
  them. A generator verdict that `--check` refuses and `--write` only prints still meets refusal 69,
  now with the render line above it naming the state. Two residuals stay outside the input rule.
  An untracked registry the generator reads off the disk, such as its stale-header waiver file, is
  not an input here, because the rule follows `git ls-files`. An untracked VIEW the render rewrites
  is named as left unstaged and is not staged, so a tree that stopped tracking one keeps that drift
  in its records commit, as it had before the close.
- testing — the scratch fixture of AC1 to AC4, RED on the BASE kit, and of AC7, RED on the rev-2
  kit; the S6 arms written and not run.
- migration — none: no fact, file or format is added.
- user docs — N/A here: the driver comment is S5, and the stop contract's sentence is a hands-off.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --close <slug>` runs from the fixture's own
  kit over the §4 fixture, whose stub bar leaves one INHERITED red under `INHERITED_RED=land`, the
  output carries `gates-green: filed ask`, then `re-rendered the generated views`, then
  `committed at`, and `git log -1 --format=%s` in the fixture reads
  `records(<slug>): close — LANDING`. With the kit extracted by `git archive 1f915870` over a fresh
  copy of the same fixture, the output carries `UNATTENDED check 69 FAILED` and
  `could not commit its own record`.
  Red when: the built close fails 69, or the BASE close commits, which would mean the fixture
  does not reproduce the defect.
  fixture: none in the tree; §4 "Fixture" is the recipe, and the pass builds it under `%TEMP%`.
  cost: composing the fixture by hand from two suite blocks is the expensive half, tens of
  minutes; each close over it runs in seconds against the stub bar.
- **AC2** — When AC1's close has committed, `git show --name-only --format= HEAD` in the fixture
  lists the build's `BACKLOG.md` and the family view under `memory/backlog/`,
  `python tools/memory-tree/gen_build_index.py --check` run over a CLEAN CHECKOUT of that commit,
  never over the fixture's worktree, prints `build-index: clean`, and `git status --porcelain` in
  the fixture is empty. The checkout is `git archive HEAD` extracted into a fresh directory with a
  repository initialised and committed over it.
  Red when: the commit carries the rows without the views, a rendered view is left unstaged, or a
  committed view is derived from bytes the commit does not carry.
  rev-3: `--check` reads the commit, because the worktree `--check` the pre-commit runs passed a
  commit whose views were derived from an unstaged edit (§4 Evidence, the closing review's M1).
- **AC3** — When the fixture is rebuilt with the inherited-red block's stub `ASKS_CMD`, which reads
  every id back as one OPEN HIGH ask, no memory-tree kit and no pre-commit hook, the close's output
  carries `gates-green: filed ask` and `were not re-rendered`, that line carries `--write`, and
  `git diff --name-only HEAD~1 HEAD` there still lists the build's `BACKLOG.md`. The close exits 0
  and prints no `UNATTENDED check` line, as the BASE kit does over the same variant.
  Red when: the miss is silent, unstages the rows, or turns the close into a refusal.
- **AC4** — When AC1's fixture is built with `LANDER_MODE="primary"` and carries, before the close,
  an untracked `notes.md` under the memory root, the close prints `re-rendered the generated views`
  with no `left unstaged` clause, `notes.md` is absent from `git diff --cached --name-only` and
  still `??` in `git status --porcelain`; the operator's records commit of what the close staged
  passes the `--check` pre-commit, `notes.md` is absent from `git show --name-only --format= HEAD`,
  and `--check` over a clean checkout of that commit, as AC2 builds one, prints
  `build-index: clean`. When the same `primary` fixture instead carries an unstaged edit to its
  tracked `BUILD-METHOD.md` guide, the close prints `were not re-rendered` with the dirty-input
  `<why>` naming `memory/guides/BUILD-METHOD.md` and the `stage or discard` repair, the build's
  `BACKLOG.md` is in `git diff --cached --name-only` and the family view under `memory/backlog/`
  and the guide are not, the guide is still ` M`, and no `UNATTENDED check` line prints. When it
  instead carries an unstaged edit to an authored line of the build's `README.md`, the miss line
  names that README, no `re-rendered the generated views` line prints, and the README is absent
  from the cached names
  with the edit intact in `git diff`. When the fixture instead stops tracking the family view in a
  commit before the close, leaving it untracked on the disk, the render line names
  `memory/backlog/ARCH.md` after `left unstaged` and it is absent from the cached names.
  Red when: the render stages a dirty path, which is the sweep S3 forbids; renders over a dirty
  tracked input; names a path it changed that was dirty before it nowhere; or the commit's own
  checkout is not clean.
  rev-2: read under `primary`, because under `in-place` refusal 62 stops a porcelain-dirty close
  before the bar runs and the criterion as first written held vacuously (§4 Evidence).
  rev-3: the guide and README arms flip from a render that leaves them unstaged to no render at all,
  because both are inputs under the memory root; the untracked-view arm takes over the
  `left unstaged` naming the README arm used to observe.
- **AC5** — When `grep -c 'write_ask_views' tools/unattended/unattended.sh` runs it prints at least
  3, where BASE prints 0, for the definition, the one call after the loop and the S5 comment;
  `grep -c 'fail 69 ' tools/unattended/unattended.sh` prints 1, its BASE count; and
  `python tools/lexicon/lexicon.py --suggest write_ask_views --as sh.function` prints a line
  opening `OK`.
  Red when: the helper is called from anywhere but the auto-file, the comment does not name it, or
  refusal 69 moved.
- **AC6** — When `grep -c -F 'were not re-rendered' tools/unattended/unattended.test.sh` and
  `grep -c -F 're-rendered the generated views' tools/unattended/unattended.test.sh` run, each prints
  at least 1, where BASE prints 0 for both.
  Red when: either path has no arm.
  permission: running this kit's own suites is waived for this landing by the build README's rule;
  the arms are written and their run is not observed here.
- **AC7** — When AC1's fixture is built with `LANDER_MODE="primary"` and carries, before the close,
  an unstaged flip of its spec's status header from `SPECCED` to `INPROGRESS`, the close prints
  `were not re-rendered` with the dirty-input `<why>` naming that spec's path, and `memory/LIVE.md`
  is absent from `git diff --cached --name-only`; the operator's records commit then meets the
  `--check` pre-commit and is refused, which is BASE's loud behaviour. With the rev-2 kit over a
  fresh copy of the same fixture, the close stages `memory/LIVE.md`, the operator's commit passes
  the pre-commit, and `--check` over a clean checkout of it prints `build-index DRIFT`. When the
  fixture instead carries an unstaged edit to `.memory-tree.conf`, the miss line names
  `.memory-tree.conf` and `memory/LIVE.md` is absent from the cached names.
  Red when: the built close stages a view over the dirty spec or conf, or the rev-2 kit's commit
  reads clean in its checkout, which would mean the fixture does not reproduce M1.
  fixture: AC1's, under `primary`, in `%TEMP%`.
- **AC8** — When `write_ask_views`, extracted verbatim from the driver, runs over a scratch repository
  whose tracked memory-tree generator carries an unstaged edit, it prints `were not re-rendered` with
  the dirty-input `<why>` naming that generator's path, renders nothing, stages nothing and returns 1;
  over the same repository with the edit absent, it renders and returns 0. The driver at `445eec56`
  over the edited repository renders and returns 0.
  Red when: an unstaged edit to the generator's own code still feeds a render whose views are staged.
  fixture: a scratch repository in `%TEMP%` with `resolve_index_generator` and `run_bounded` stubbed.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `memory hygiene` · `install-prefix (shipped surface)`

New arm: `tools/unattended/unattended.test.sh` · the inherited-red block's MET arm with no generator, and a new block composing the in-place and inherited-red fixtures with the real generator and a `--check` pre-commit · none

## 8. Open questions

- **F1 — Which step renders the views?** (a) `write_close_commit`, before it commits. (b) The
  Skill's close sequence, by instruction. (c) `write_inherited_asks`, the writer that makes them
  stale, after it files. (a) fixes the in-place close and leaves the `primary` and `hold ·` paths
  committing stale views by hand; (b) is a governance carrier no accept clause names, which veto 2
  refuses, and an instruction is the shape the 2026-09-30 close already had and missed. (c) covers
  all three paths with one call and satisfies the accept clause. Recommendation (c). RESOLVED
  (agent, 2026-10-01, delegated): (c), the most feature-rich survivor after M3's vetoes.
- **F2 — What does a render that misses do?** (a) Refuse the item with a new numbered branch.
  (b) Roll the filed rows back. (c) Keep the rows staged, name the miss and its repair, and let the
  close proceed. (a) adds a refusal after the bar was paid, for a state a hand render repairs in
  seconds, and an arm the waived suite cannot run; (b) drops the inherited leg's owner from the
  record, against the stop contract's §13. (c) keeps both and loses nothing the BASE close had.
  Recommendation (c). RESOLVED (agent, 2026-10-01, delegated): (c), the most feature-rich survivor
  under M3's rule: it meets every criterion the other two meet, and keeps the ask on the record.
- **F3 — What does the render do when an input of the views is dirty?** Raised by the closing
  review's M1, round 1. (a) Before the render, intersect the dirty paths with the views' inputs,
  the tracked paths under the memory root and `.memory-tree.conf`; when any is dirty, render nothing,
  stage no view, name the inputs and the repair, and return 1 without refusing the close. (b) Render
  against the index instead, in a scratch checkout of it, and stage only the outputs whose bytes
  differ from the index blob and whose worktree path was clean. (b) keeps AC4's arms as first
  written, but it adds a write surface outside the tree, a checkout per filing close, which veto 3
  prices, to rescue a case the operator repairs in one command. (a) never commits a view derived
  from a change the operator has not staged, and the operator's commit meets the freshness check
  loudly, as at BASE.
  RESOLVED (agent, 2026-10-01, delegated): (a), handed down by the fold brief. (b) falls to veto 3,
  and (a) is the survivor that meets every criterion.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the ask's accept clause, the build's spec brief, the
  hand-made close commit `10663361`, and the driver read at BASE.
- rev-2 · 2026-10-01 · the unit pass, from the fixture it built. AC4 is read under `primary`: under
  `in-place` refusal 62 refuses its dirty tree before the bar runs, so the §4 Evidence line on
  `check_clean` was half true and AC4 held vacuously; it gains the left-unstaged half S3 names.
  S2's render takes `-B`: without it the fixture's first close staged two bytecode caches into its
  records commit. S4 and §4 gain the stage-refused line, and §4 the `staged 0 path(s): none` form.
  S6 gains the F4 slice's double. §4 Fixture records the waiver registry, the ignore line and the
  suite-less kit copy the fixture needed.
- rev-3 · 2026-10-01 · the fold of the closing diff review's round 1, M1 (MEDIUM), as the fold brief
  disposes it. §8 F3 resolved to (a). S3 gains the input side: a dirty input of the views stages no
  view and prints the miss line naming it. §4 gains the M1 evidence and the dirty-input spelling;
  §5's risks bullet loses "only the run's own writes can move it" and names the two residuals.
  AC2 and AC4 read `--check` over a clean checkout of the commit, never the worktree. AC4's guide
  and README arms flip to the miss line, and an untracked-view arm takes the `left unstaged`
  naming. AC7 is new: the spec status-header flip of M1 itself, and the conf. S6 names the arms;
  §4 Fixture and Rollout and §5's testing line name AC7, and the driver's S5 comment names the miss.
- rev-4 · 2026-10-01 · §2 §6 · S3 AC8 · the fold of the closing diff review's round 2. L1 (LOW): the
  dirty-input predicate left out the generator's own code, so an unstaged edit to its modules still
  fed a staged render, M1's mechanism again. S3 adds the generator's directory, and AC8 observes it.
  L2 (LOW): the suite's `rv_check_commit` pins `core.autocrlf=false`, so git's CRLF warnings no longer
  crowd a red arm's output. The new suite arm is written and not run; the block's skip count is 41.

## 10. Reuse audit

The probe, run on 2026-10-01:

```
python tools/codebase-map/reuse_lookup.py "re-render the generated index views after a records write and stage what changed"
```

It ranked `write`, `write_text` and `records` as name-stem seams, the generator's own writer among
them, and reported `.sh` as an unscanned layer, which is where this driver lives. The seams reused
were found by reading the driver and its library: `resolve_index_generator` and
`derive_index_repair` in `tools/unattended/lib-unattended.sh`, which already locate this install's
generator and spell its `--write` repair; `resolve_python` and `run_bounded`, which every bounded
call site of the driver uses; and the generator's own `--write`, which is the one renderer of these
views. No existing seam fits the staging rule: nothing in the driver stages a renderer's output, and
`GENERATED_INDEXES` was read and rejected as the staging set for the reason §4 gives.

Recall terms used: write_close_commit write_inherited_asks gates-green inherited-red auto-file BACKLOG.md generated views check 9 check 69 in-place LANDER_MODE gen_build_index --write

The question passed with them: "how does an in-place close commit its own record and why did an
auto-filed ask leave the generated views stale".
