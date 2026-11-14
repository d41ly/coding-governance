# TOOL-aTrimmedWait-3 — a commit refused on build-index drift renders its own index, stages it and is graded again

**Status:** SPECCED · rev-1 · 2026-11-14 · node a · Tier-2 · base 846d51d3 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md](../prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md) | research | TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 |

<!-- /gen:spec-records -->

## 1. Goal

A commit that stages a memory change without re-rendering the build index is refused by hygiene
check 9, and the committer must run `gen_build_index.py --write`, stage what it wrote and commit
again. The measured session lost 71 such refusals, each a round trip and, in a harnessed stage, a
re-dispatched unit. This unit lets the pre-commit hook take that remedy itself, under a
default-off switch, and grade the commit again, so the verdict is the one the manual remedy gets.

## 2. Scope (IN)

- **S1** — A new generator mode, `gen_build_index.py --write-staged`. It renders what `--write`
  renders, and writes only the artifacts whose bytes differ from the worktree. It stages exactly
  those paths, and each orphaned ledger shard it unlinks, into the index the hook was handed, and
  prints one line per staged path. It exits 0 only when it staged at least one path. Observed by
  AC1.
- **S2** — The mode declines before it renders or writes anything when any of the following
  holds. It prints `build-index: render NOT staged — <why>` and exits 1.
  - `STAGED_RENDER` is blank.
  - The hook's index is neither the repository's index nor that index's `.lock`.
  - A render input has an unstaged worktree change.
  - The data-loss guard holds a view.

  It also exits 1, after rendering and writing nothing, when no artifact's bytes moved. A
  `STAGED_RENDER` value other than blank or `1` is refused by name, exit 1. Observed by AC2, AC3,
  AC4.
- **S3** — `build_render_pathspec`, the pathspec `check_staged_render` builds today, extracted so
  that function and the S2 unstaged-input check read one definition of what the render reads.
  Observed by AC4.
- **S4** — `derive_moved_artifacts`, the repo-relative paths whose file is missing or whose BYTES
  differ from the rendered text's UTF-8 encoding. Observed by AC1.
- **S5** — `.githooks/pre-commit` runs the mode only after the hygiene leg fails with a
  `HYGIENE check 9 FAILED` line. When the mode exits 0, the hook prints one line and runs the
  hygiene leg again, and that second run's exit decides. In every other case the hook refuses
  as it does today. Observed by AC5, AC6.
- **S6** — `STAGED_RENDER` is declared blank in `tools/memory-tree/.memory-tree.conf.example`
  with its comment, set to `"1"` in this repository's `.memory-tree.conf`, and described in the
  `gen_build_index.py` row of `tools/memory-tree/README.md`. Observed by AC7.
- **S7** — A help page, `help/commit-render.md`, and its line in `help/README.md`. Observed by
  AC8.
- **S8** — The acceptance ledger records the same commit timed before and after on node a, and
  the same refusal with the switch blank. Observed by AC9, AC10.

## 3. Non-goals (OUT)

- No change to hygiene check 9, to `--check`, to `--check --staged` or to
  `tools/memory-tree/check-memory-hygiene.sh`. The grader stays independent of the writer.
- No render before the first hygiene run. §4 "Alternatives rejected" measures why.
- No staging under a partial commit, `git commit <path>`. The probe in §4 shows the real index
  diverging there.
- No change to plain `--write`, which keeps rewriting every artifact. That is TOOL-aTrimmedWait-4.
- No change to the reference hook blocks in `tools/memory-tree/README.md` and
  `WIRE-INTO-PROJECT.md`. They wire the minimal leg, and the step is off by default.
- No repair of the hygiene leg reading the repository's index rather than the hook's under
  `git commit -a`. That gap predates this unit; §4 "What it does not check" names it.
- No kit version bump. The build's rule moves versions once, after the last code move.
- No speed-up of the render's readers. Their cost is measured in §4 and left to a later build.

### Edges

- **hands-off** `TOOL-aTrimmedWait-4` — plain `--write` still writes every artifact. That unit
  routes it through `derive_moved_artifacts`, which this unit mints.

## 4. Design

### The flow

The hook runs the hygiene leg as it does today, with its output captured and then printed. If
the leg failed and its output holds a line opening `HYGIENE check 9 FAILED`, the hook runs
`gen_build_index.py --write-staged` under the index git handed it. A 0 from the mode means it
staged a rendered artifact, so the hook prints
`pre-commit: the build index was rendered and staged; grading the memory hygiene leg again.` and
runs the leg again. That run's exit is the leg's verdict. Any other outcome sets `rc=1` as today:
the leg failed without a check 9 line, the gate or a launcher did not resolve, or the mode
exited non-zero.

A commit that check 9 does not refuse pays nothing new. A refused one pays one render and one
more hygiene run, in place of the committer's `--write`, `git add` and second commit.

### The mode

`main()` accepts `--write-staged` as a mode word beside `--write`
(`tools/memory-tree/gen_build_index.py@5a0864b8:8839`). It calls
`cmd_write(root, conf, staged=True)`, so the render, the as-built view and the orphan handling are
`cmd_write`'s (`tools/memory-tree/gen_build_index.py@5a0864b8:3214`), never a copy. With
`staged=True`, `cmd_write` makes four changes:

1. It runs `check_staged_write(root, conf)` first, and returns 1 on a decline.
2. It writes the as-built view only when its bytes moved, and writes only the artifacts
   `derive_moved_artifacts` names, instead of every one
   (`tools/memory-tree/gen_build_index.py@5a0864b8:3228`).
3. It declines, writing nothing, when `plan()` reports a guarded view.
4. It runs `git add -A -- <paths>` once over the moved view, the moved artifacts and the
   removed orphans, with `GIT_INDEX_FILE` carried as `check_staged_render` carries it
   (`tools/memory-tree/gen_build_index.py@5a0864b8:1001`). It prints
   `build-index: staged <path>` per path, and returns 0. When nothing moved it prints the decline
   line `render NOT staged — no artifact's bytes moved, so check 9's refusal is not drift a
   render cures` and returns 1.

`--new-build` already stages its own write through `run("git", "add", ...)`
(`tools/memory-tree/gen_build_index.py@5a0864b8:4202`). `run()` drops `GIT_INDEX_FILE`
(`tools/memory-tree/gen_build_index.py@5a0864b8:265`), which is why S1 carries the hook's index
explicitly. Under `git commit -a` git holds the repository index's lock, and only an add through
the hook's index succeeds.

A mode WORD and not `--write --staged`: `main()` today ignores `--staged` beside `--write` and
runs the full unconditional write. A copied hook newer than an adopter's generator would then
rewrite every artifact with no switch read. An old generator answers `--write-staged` with its
usage line and exit 2 (`tools/memory-tree/gen_build_index.py@5a0864b8:8842`), and the hook
refuses as before.

### Declines, cheapest first

`check_staged_write(root, conf) -> (bool, str)`:

1. `STAGED_RENDER` blank declines with `STAGED_RENDER is blank, so the hook does not render`. A
   value other than `1` raises `Problem` naming the value, read the way `LIVE_LANDED_UNCLOSED`
   is (`tools/memory-tree/gen_build_index.py@5a0864b8:1009`).
2. `GIT_INDEX_FILE`, when set, must name the same file as
   `git rev-parse --path-format=absolute --git-path index`, or that path plus `.lock`. Both
   paths are compared after `os.path.abspath` and `os.path.normcase`, and git is run with
   `_build_git_env()`, because an inherited `GIT_INDEX_FILE` moves `--git-path index`. Any other
   index declines and names the index.
3. `git diff --name-only --no-renames -z` over `build_render_pathspec(...)`, against the hook's
   index, must print nothing. A path printed declines and names up to five paths and the count.
   A git failure declines.

`build_render_pathspec(m, kit, carries, llu) -> list` returns `[]` when `llu` is set, meaning
the whole tree, since the Landed-unclosed column reads tracked product source. Otherwise it
returns the list `check_staged_render` builds at
`tools/memory-tree/gen_build_index.py@5a0864b8:995`. `check_staged_render` calls it in place of
that line, and passes it to git only when it is non-empty, as its own `llu` branch does today
(`tools/memory-tree/gen_build_index.py@5a0864b8:1011`).

The unstaged check is what lets the staged set stand for the render's input. The renderer reads
the worktree, so with no unstaged change under the pathspec the worktree is the index, and the
staged artifacts are a pure function of what the commit carries. That is the brief's rule that a
scoped answer which cannot prove its inputs falls back to the full run.

### Moved artifacts, by bytes

`derive_moved_artifacts(root, artifacts) -> list` compares each file's bytes with
`text.encode("utf-8")`, the bytes `write_text` writes
(`tools/memory-tree/gen_build_index.py@5a0864b8:296`). It does not use `read_text`, which
normalises CRLF (`tools/memory-tree/tree_lib.py@54a65cd4:418`): a CRLF file equal in text would
read unmoved and be left in place where `--write` rewrites it.

### The hook

The edit sits in the hygiene leg's branch (`.githooks/pre-commit@468b13e4:227`). The generator is
resolved with `resolve_kit_gate memory-tree gen_build_index.py`, and the launcher the way the
red-fix branch resolves one (`.githooks/pre-commit@468b13e4:242`). The mode runs under
`with_hook_index` (`.githooks/pre-commit@468b13e4:11`). The match is a whole-line prefix on
`HYGIENE check 9 FAILED`, the text `fail()` prints
(`tools/memory-tree/check-memory-hygiene.sh@f064ddab:406`). Under `OFFENDERS=1` `fail()` prints
keys instead; the hook never sets that variable.

### The switch

`STAGED_RENDER` is off by default because the hook is copied into adopters, and a hook that adds
paths to a commit nobody staged is new behaviour there (charter `[small]`). This repository sets
it to `"1"` and is the dogfood. The example conf's comment states the two values, what the hook
then does, the three declines and the partial-commit exclusion.

### What it does not check

- Under `git commit -a` the hygiene leg reads the repository's index, not the hook's, so check 9
  may not see the commit's staged set and never refuse. The mode accepts that index, and it is
  reached only when check 9 does refuse.
- A render input that is untracked is not an input: the renderer lists inputs with `git ls-files`.
- The second hygiene run grades the commit as staged. It does not prove the render was needed,
  only that the result is clean.

### The git behaviour this rests on

A fixture repository on node a, git 2.54.0.windows.1, 2026-11-14 (PINNED), with a pre-commit hook
that runs `git add` on a file it writes:

| Commit form | `GIT_INDEX_FILE` in the hook | The hook's add | Index after |
|---|---|---|---|
| `git commit -m` | `.git/index` | in the commit | clean |
| `git commit -a -m` | `<git dir>/index.lock` | in the commit | clean |
| `git commit -m <path>` | `<git dir>/next-index-<pid>.lock` | in the commit | `MM` on the file |

### Measurements (PINNED, node a, 2026-11-14)

- `gen_build_index.py --check` takes 42.5 s wall on this tree, and `plan()` 47.5 s in-process,
  over 3207 artifacts.
- Of `plan()`: `collect()` 11.1 s, `read_carries_coverage` 15.6 s, `read_landed_unclosed` 8.6 s,
  `read_bindings` 1.4 s, the as-built view 1.7 s.
- Rewriting all 3206 rendered artifacts takes 16.8 s in a scratch copy, and comparing them first
  takes 0.8 s, with 0 moved on a clean tree.

### Inventory

| Minted | Kind | Graded by |
|---|---|---|
| `--write-staged` | generator mode word | `main()`'s mode list |
| `STAGED_RENDER` | conf key, blank or `1` | `check_staged_write` |
| `check_staged_write` | function | `lexicon naming predicates`, cell `py.function` |
| `build_render_pathspec` | function | `lexicon naming predicates`, cell `py.function` |
| `derive_moved_artifacts` | function | `lexicon naming predicates`, cell `py.function` |
| `test_staged_write` | selftest function | `lexicon naming predicates`, cell `py.function` |
| `help/commit-render.md` | help page | `docs`, `help page commands` |

The help page shows no fenced `bash` block naming `gen_build_index.py`, because that script has no
docs row and the docs leg would report the block `UNROWED`. It shows the key in a `text` block,
as `help/reference/drive.md` shows `--write`.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`
- `tools/memory-tree/.memory-tree.conf.example`
- `.memory-tree.conf`
- `tools/memory-tree/README.md`
- `help/commit-render.md`
- `help/README.md`

### Alternatives rejected

- **Render first, on every commit that owes one.** Most memory commits owe a render under
  `--check --staged`, an added file alone owes one, and many arrive already rendered. Each would
  pay a full `plan()`, measured at 47.5 s, before a hygiene run that renders again.
- **The write inside check 9.** The grader would then share state with what it guards (charter
  `[class]`).
- **The hook stages `git diff --name-only` after a plain `--write`.** That misses a new ledger
  shard, which is untracked, and puts the list of written paths in a second place.
- **Staging under a partial commit.** The probe above leaves the real index at `MM`.

## 5. Production-readiness checklist

- security — A new write path: the hook adds generated files to a commit. It is off by default.
  It writes only paths `plan()` renders and orphans it removes, and only when no render input is
  unstaged, so no operator edit is ever staged by it.
- perf / scale — A clean commit pays nothing. A refused one pays one render (about 47 s on this
  tree, PINNED above) and one hygiene run, against the manual remedy's render, add and second
  commit.
- error / empty / loading states — Every decline names its reason and exits 1, and the hook then
  refuses as today. Nothing moved is a decline. An unparseable key is refused by name.
- observability — One `build-index: staged <path>` line per path, and one hook line before the
  second grading.
- risks — The hook now captures the hygiene leg's output before printing it, so its lines appear
  at the end of the run rather than as they are printed. A message edit in `fail()` would strand
  the match; the arm of §7 reads the literal from the producer.
- testing — AC1 to AC4 are generator runs in a fixture repository. AC5 and AC6 are the hook
  driven by stand-in gates. AC9 and AC10 are commits in a clone. The arms of §7 repeat AC1 to AC6.
- migration — None. A blank or absent key leaves every commit as it is today.
- user docs — `help/commit-render.md`, S7.

## 6. Acceptance criteria

`<f>` is a fixture repository under `%TEMP%/<short-name>`. It is built by the generator's own
`_fixture` helper, with `STAGED_RENDER="1"` appended to its `.memory-tree.conf`. Its tree is
rendered with `--write` and committed. Then the spec's status token `INPROGRESS` is changed to
`DEFERRED` and staged, and the README is not rendered. `<gbi>` is
`tools/memory-tree/gen_build_index.py` in this worktree, run with `<f>` as the working directory.

- **AC1** — When `python <gbi> --write-staged` runs in `<f>`, it exits 0 and prints
  a `build-index: staged` line naming the build README of `<f>`. Afterwards
  `git diff --name-only` prints nothing, the paths it printed are exactly the ones
  `git diff --cached --name-only` adds beside the spec, and `python <gbi> --check` exits 0.
  Red when: an artifact is written and not staged, so `git diff --name-only` lists it, or an
  unmoved path is printed. At base the mode word is a usage error, exit 2.
- **AC2** — When the same run follows `STAGED_RENDER=""` in `<f>`'s conf, it exits 1 and prints
  `render NOT staged — STAGED_RENDER is blank`, and `git status --porcelain` is unchanged. With
  `STAGED_RENDER="yes"` it exits 1 naming `yes`. Run a second time after AC1's success, it exits
  1 with `no artifact's bytes moved`.
  Red when: a blank key still writes, or an unmoved tree exits 0 and sends the hook to a second
  grading.
- **AC3** — When the run sets `GIT_INDEX_FILE` to a copy of `<f>`'s index under another name, it
  exits 1 naming that index. With `GIT_INDEX_FILE` set to `<f>/.git/index`, it proceeds as in
  AC1.
  Red when: a foreign index is accepted, or the repository's own index under an absolute path is
  declined.
- **AC4** — When the tracked `<f>/memory/notes.md` carries an unstaged edit, the run exits 1
  naming that path. When the only unstaged edit is to a tracked `<f>/src/x.sh`, the run proceeds
  with `LIVE_LANDED_UNCLOSED` blank, and declines naming that path with the key set to `1`. In
  every case `git status --porcelain` is unchanged by a decline.
  Red when: the unstaged check reads a pathspec other than `check_staged_render`'s, so one of the
  two source-file cases flips.
- **AC5** — When the hook commits in a repository whose stand-in hygiene gate prints
  `HYGIENE check 9 FAILED — drift` and exits 1 on its first run and exits 0 on its second, and
  whose stand-in generator stages a file and exits 0, the commit exits 0 and carries that file.
  Red when: the hook does not run the generator, or does not grade again, so the commit is
  refused.
  fixture: stand-in gates planted the way the hook suite's `run_prefix_commit` helper plants one.
- **AC6** — When the stand-in hygiene gate fails with `HYGIENE check 12 FAILED — x`, the
  stand-in generator never runs and the commit is refused. When it fails with the check 9 line and
  the stand-in generator exits 1, the hygiene gate runs once and the commit is refused. And
  `grep -c 'echo "HYGIENE check $1 FAILED' tools/memory-tree/check-memory-hygiene.sh` prints 1.
  Red when: any hygiene failure triggers a render, a declined render is followed by a second
  grading, or the producer's text has moved from what the hook matches.
- **AC7** — When `grep -c '^STAGED_RENDER=""' tools/memory-tree/.memory-tree.conf.example` runs it
  prints 1, `grep -c '^STAGED_RENDER="1"' .memory-tree.conf` prints 1, and
  `grep -c 'write-staged' tools/memory-tree/README.md` prints 1 or more.
  Red when: the key ships on, or the kit README is silent. At base each prints 0.
- **AC8** — When `grep -c 'commit-render.md' help/README.md` runs it prints 1, and
  `grep -rl 'STAGED_RENDER' help` names that page, which also names `HYGIENE check 9 FAILED` and
  the partial-commit exclusion.
  Red when: the page or its index line is absent. At base each prints 0.
- **AC9** — When a clone of this repository at the unit's commit has a spec's status token
  changed, staged and not rendered, `git commit -m probe` exits 0 and the commit carries the build
  README. The same staged change in a clone at base `846d51d3` exits 1 on check 9. The ledger
  records both wall times, plus the base remedy's: `--write`, `git add` and the second commit.
  Red when: the unit's clone still refuses, or the two timings are not the same command.
  cost: about three full renders and three hygiene runs, several minutes.
  permission: the main loop's; the commit runs the hygiene gate through the hook.
  fixture: two clones under `%TEMP%/<short-name>`, none in the tree today.
  figure: every time is DERIVED at observation.
- **AC10** — When AC9's unit clone runs again with `STAGED_RENDER=""` committed in its conf, the
  commit exits 1. Its `HYGIENE check` lines equal the base clone's, line for line, and the one
  added line is the hook's decline.
  Red when: a blank switch changes a refusal, a red or a green.
  permission: the main loop's, as AC9.

## 7. Gates

`build-index selftest` · `branch-guard self-test` · `memory hygiene` · `docs` · `help page commands` · `lexicon naming predicates` · `tier2-review self-test` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `transition-audit arms` · `straggler-guard arms`

The first six grade this unit's change. The last six are owed by a guard a path of the estimate
trips. The main loop runs the merge bar once, at the close. No leg is added.

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 AC4 · `test_staged_write` over the fixture of §6, with each decline staged in turn; RED at base, where `--write-staged` is a usage error · none
New arm: .githooks/pre-commit.test.sh · covers AC5 AC6 · stand-in hygiene and generator gates planted as `run_prefix_commit` plants its stand-in, the check 9 literal read from the real `fail()` line; RED at base, where the hook never calls the generator · none

What these arms do not check: the hook against the real hygiene gate, which AC9 observes once,
and `git commit -a`, which §4 names.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-14 · initial draft.

## 10. Reuse audit

The seam is the generator's own write and staged-render path in
`tools/memory-tree/gen_build_index.py`. `cmd_write` takes a `staged` flag rather than gaining a
sibling. `check_staged_render` gives up its pathspec to `build_render_pathspec` and keeps its
index handling, which the new check copies by calling the same `_build_git_env` and
`GIT_INDEX_FILE` carry. `--new-build`'s `run("git", "add", ...)` is the staging precedent. The
hook extends its own hygiene branch, with `resolve_kit_gate`, `with_hook_index` and the red-fix
branch's launcher resolution. `tools/codebase-map/reuse_lookup.py` for "render the build index in
the pre-commit hook and stage what it wrote" ranked name stems only (`render`, `build_index`,
`write_commit`) and named no seam closer than these. Recall returned no record that renders in a
hook. It did return TOOL-aSmoothedDispatch-14 and PLAY-dClosedLoop-31, both refusals of `--write`
itself on an authored `status:` key, which this mode inherits unchanged as a `Problem`, exit 1.

Recall terms used: pre-commit check-9 gen_build_index staged render write artifacts stage index
drift refused unchanged bytes
