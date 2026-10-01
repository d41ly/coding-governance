**Serves:** diff-review TOOL-dMendedRecall-2

# dMendedRecall: Tier-2 closing diff review of the round-1 fold, round 2

*Node `d`, 2026-10-01. This is round 2 of the unattended build's closing review under
`memory/guides/BUILD-METHOD.md`, over the FOLD diff only: the round-1 fold of M1 into
TOOL-dMendedRecall-2, which took that unit's spec to rev-3. Harness: `tools/workflows/tier2-review.js`,
with four primed finder lenses, five skeptic batches prompted to REFUTE each finding, and this
synthesis. Fold text is unreviewed surface, so the lenses were pointed at what the fix introduced as
well as at whether M1 is closed. The round-1 record is
`memory/builds/dMendedRecall/reviews/2026-10-01-review-TOOL-dMendedRecall-1-closing-diff-round1.md`,
and the fold's acceptance readings are the rev-3 section of
`memory/builds/dMendedRecall/build/2026-10-01-build-TOOL-dMendedRecall-2-1-acceptance-ledger.md`.*

**Range reviewed: `0cfb51da3adedf3063b03763e8838bcd54dc6c56...445eec56394803a41f24e712e060ad99ac2a592d`**
(branch `run/dMendedRecall`, 10 files, +470/−60).

**Round: 2.**

## Verdict: CLEAN WITH FIXES

There are no blockers, no highs and no mediums. M1 is closed for the inputs the fold names: under
`LANDER_MODE=primary` an unstaged edit under the memory root, or to `.memory-tree.conf`, now stages no
view, and the close still does not refuse. Two LOW items remain. The first is a third input the
predicate leaves out, which is the generator's own code, and it reaches M1's exact mechanism by that
route. The second is a diagnostic defect in the new `rv_check_commit` test helper. Both are owed a
fold under unit 2's spec.

## Review shape and run integrity

- **Raw 9, confirmed 3, refuted 6, unverified 0, precision 0.33**, which is 3 / (3 + 6).
- **Refuted:** six raw findings did not survive their skeptics. Their text did not reach this
  synthesis, so they are recorded here as a count only.
- **Adjudicated tally by item:** 2 items. That is 0 BLOCKER, 0 HIGH, 0 MEDIUM and 2 LOW (L1, L2).
- **Adjudicated tally by raw confirmed finding:** 0 BLOCKER, 0 HIGH, 0 MEDIUM and 3 LOW (ids 3, 8
  and 9). That totals 3, and every confirmed id is in exactly one item.
- **Merges:** the harness reported 0 duplicates, and it only counts identical findings. Ids 3 and 8
  came from different lenses and describe one defect at one line, so this synthesis merged them into
  L1. Id 8 adds a second half, the comment's claim about untracked paths, which L1 carries.
- **Run integrity:** lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. No
  contradictory verdict was demoted to unverified, no spurious verdict was discarded, and there were
  0 duplicates. Every counter is zero, so **this run is complete**, and the finding set is the
  lenses' whole result, not one missing a dead lens's share.
- **Precision is below 0.5** for the second round running (0.25, then 0.33). §8 says to tighten scope
  or priming before adding agents. The lenses were primed with the security model this time and
  precision rose a little; adding agents is still not the fix.

## What the synthesis checked itself

It re-read every cited site at `445eec56` and re-pinned the line numbers below. It also reproduced
L1 in a scratch clone of this repository at `445eec56`, under the session scratchpad, as described
under L1. On the brief's other questions it found the fold sound:

- **M1 under `primary`.** The dirty-input predicate (`tools/unattended/unattended.sh:6936-6947`)
  runs before the render and returns before `run_bounded` at `:6956`. So a dirty input means no
  render, no `GIT add` of any view, and `return 1`. The caller at `:7107` is
  `write_ask_views "$filed" || :`, so the close is never refused.
- **M1 under `in-place`.** Refusal 62 still stops a porcelain-dirty tree before the bar, so the
  predicate is empty there unless the run itself leaves an unstaged path under the memory root. The
  ledger's AC2 reading shows an in-place close that rendered, committed the views, and read
  `build-index: clean` over a clean checkout of its commit.
- **What the predicate treats as input.** `git diff --no-renames --name-only -z` lists tracked paths
  with unstaged changes, deletions included. A path that has a staged change and a further unstaged
  one is listed too, which is correct, because the index does not hold its worktree bytes. Paths are
  NUL-read and the case pattern is quoted, so spaces and tabs are matched correctly. They only make
  the space-joined miss line ambiguous to read. An unstaged `mv` of a tracked path shows as a
  deletion of the old name, so it is caught when the old name is under the memory root. An untracked
  `.memory-tree.conf` is caught by the second loop at `:6941-6942`, unless it is ignored.
- **One spelling of the miss frame.** The earlier two misses set `fix=""`, so `repair: $fix$(...)`
  at `:6950` prints the same bytes as the rev-2 line did. Only the `<why>` and the repair prefix
  differ for the dirty-input miss, which is what spec rev-3's Spellings section states.
- **The skip count, 27 to 39.** The block holds 38 `hit`, `miss` and `same` calls plus one inline
  `n=$((n+1))` arm, which is 39. At `0cfb51da` it held 26 plus that same arm, which is 27. The fold
  removed 5 AC4 assertions, added 3 back, and added 14 in the new arms, so the net is +12.
- **Spec and ledger against the code.** S3's input side, the dirty-input spelling, AC2's
  clean-checkout recipe, AC4's flipped arms and AC7 all match the driver and the suite. The spec's
  evidence citations into `gen_build_index.py` (`:247`, `:293`, `:851`) hold, because the generator
  is unchanged since the build's base. The one place where they disagree with the code is the input
  set itself, which is L1.

## Findings

| # | Sev | Where | What | Raw ids |
|---|---|---|---|---|
| L1 | low | `tools/unattended/unattended.sh:6938` | the dirty-input predicate leaves out the generator's own code, so an unstaged kit edit still feeds a render whose views get staged | 3, 8 |
| L2 | low | `tools/unattended/unattended.test.sh:11279` | `rv_check_commit` inherits ambient `core.autocrlf`, and git's warnings flood the capture a red arm prints | 9 |

### L1 — the generator's own code is an input the predicate does not list

**Where:**

- The predicate is `case "$p" in "$M"/*|.memory-tree.conf)` at `tools/unattended/unattended.sh:6938`.
  The untracked loop at `:6941-6942` adds only the conf.
- The comment at `:6902-6910` states the input set as the tracked paths under the memory root plus
  the conf. It also says at `:6909-6910` that an untracked path under the memory root is no input.
- Spec 2 S3 (`memory/builds/dMendedRecall/spec/2026-10-01-spec-TOOL-dMendedRecall-2.md:52`) says the
  close "never commits a view derived from a change the operator has not staged". The risks bullet
  (`:243-247`) lists "Two residuals", and the generator's code is not one of them.

**Defect.** The generator is part of its own input. `gen_build_index.py:148` puts its own directory
on `sys.path`. It imports `tree_lib` from there at `:149` and `backlog` at `:290`, and it renders
every family view through `backlog.render_family_view` (`gen_build_index.py:1181`,
`backlog.py:1635`). The resolver answers a repo-relative path inside the tree being closed
(`tools/unattended/lib-unattended.sh:128`), and the file test at `unattended.sh:6927` requires it to
be there. So an unstaged edit to `gen_build_index.py`, `backlog.py`, `tree_lib.py` or
`row_grammar.py` feeds `--write` without matching the predicate. The views it moves were clean
before the render, and the delta rule stages them. The pre-commit's worktree `--check` runs the same
edited code and passes. A clean checkout runs the committed generator and reads DRIFT. This is M1's
mechanism through an input the fold did not list.

The gap was inherited, not invented by the fold. Round 1's own recommended fix (a) spelled the
input set as `GIT ls-files -- "$M/"` plus `.memory-tree.conf`, and the fold implemented that
faithfully.

**The second half (id 8).** The comment's claim that an untracked memory-root path is no input
contradicts the generator. `read_stale_header_waiver` (`gen_build_index.py:815-818`) reads
`memory/project/stale-header-waiver.txt` off the disk whether or not it is tracked. The spec names
that file as a residual and the comment denies it exists. That is two answers to one question.

**Reproduction.** In a scratch clone at `445eec56` the tree's `--check` read
`build-index: clean (973 artifact(s))`. The synthesis then made an unstaged edit to the text of
`GEN_HEADER` in `tools/memory-tree/gen_build_index.py`. It ran the driver's predicate with `M=memory`
over that tree, and the predicate came back empty. `--write` exited 0, and the delta rule would have
staged 9 paths that were clean before it: `memory/LIVE.md`, the four family views under
`memory/backlog/`, and four ledger shards. With those staged, the worktree `--check` read
`build-index: clean` with rc 0. With the generator edit set aside and the staged views kept,
`--check` read `build-index DRIFT` with rc 1.

**Reach.** It needs `LANDER_MODE=primary`, which is the kit default and never calls `check_clean`
on `--close`. It also needs uncommitted edits to the memory-tree kit in the closing tree, from a
copy-in upgrade or a local edit, at a close that files an ask. This repo declares `in-place`, where
refusal 62 stops a dirty tree first.

**Adjudication: LOW.** The damage is M1's: a silent stale records commit that the pre-commit passes,
caught only at pre-push or in a clean checkout. The reach is much narrower than M1's, because it
needs a dirty kit rather than a dirty record. Nothing is lost, and a re-render repairs it.

**Fix.**

- Add the generator's kit directory to the input arm, derived from `gen` rather than spelled, so
  that the line becomes `case "$p" in "$M"/*|.memory-tree.conf|"$kd"/*)`. Mind the resolver's `.`
  case at `lib-unattended.sh:134`, where the kit is the repo root and `${gen%/*}` has no slash.
- Reword the comment at `:6902-6910` and S3 so that the stated input set matches what the predicate
  covers.
- Name the untracked registries the generator reads off the disk as a residual in one place, the
  spec's risks bullet, and stop the comment from denying them.
- If the kit directory is left out on purpose, record it as a third residual in the risks bullet and
  take S3's "never" out. Either choice is a rev-4 line in the spec's section 9.

**Left-shift gate.**

- **An AC7-style arm.** In the TOOL-dMendedRecall-2 block, build the `primary` fixture and append a
  byte to a rendered string in the fixture's own copy of `backlog.py` or `gen_build_index.py`, for
  example `GEN_HEADER`. Run the filing close, then assert that the miss line names the kit path and
  that `memory/backlog/ARCH.md` is absent from `git diff --cached --name-only`. Stage the break on
  the rev-3 driver first and confirm RED (§7). The block's skip count moves with it.
- **Grade the class with the harness the fold already built.** `rv_check_commit` runs the committed
  generator over a checkout of the commit, so it reds on this defect whichever input moved the view.
  A dirty-kit arm graded by `rv_check_commit` is the class gate, not just the instance.
- **Derive the input set instead of listing it.** The predicate is a hand-kept list of a population
  the generator owns. A generator mode that prints the paths it reads would let the driver ask
  instead of guess, and the next input the generator gains would be covered without a review.

### L2 — `rv_check_commit` inherits ambient `core.autocrlf`

**Where:** `tools/unattended/unattended.test.sh:11276-11283`, introduced by the fold. The
`git init -q -b main . && git add -A` is at `:11279`, and `) 2>&1` merges git's stderr into the
capture the arms at `:11306` and `:11326` grade.

**Defect.** The helper's fresh repository takes `core.autocrlf` from the machine. Every other
committing fixture in the file pins `core.autocrlf false` (`:150`, `:8495`, `:9608`, `:10265`,
`:10701`, `:10992`, `:11186`, `:11393`, `:11709`). The two unpinned inits (`:125`, `:2532`) discard
their output, so this is the only site where git's noise reaches an assertion. This is the class
`memory/gotchas/fixture-inherits-ambient-machine-state.md` names, and that gotcha names
`core.autocrlf` explicitly.

**Impact.** On node `d`, `core.autocrlf=true` is set in both the system and the global config
(git 2.54.0.windows.1, confirmed by `git config --show-origin`). `git add -A` there prints one
`LF will be replaced by CRLF` warning per file. The skeptic's probe over a comparable tree produced
55 warnings and 7235 bytes. `hit` (`:93`) prints only the first 400 characters of what it got. So
when the AC2 or AC4 clean-checkout arm reds, which is the arm that exists to left-shift M1, the reader
sees warnings and never the `build-index DRIFT` line that names the stale view. The pass/fail verdict
does not change under default config, because the extracted files stay LF. A global
`core.safecrlf=true` would make the add fail and red the arm for an unrelated reason; this node has
no such setting, so that half is hypothetical.

**Adjudication: LOW.** It degrades the diagnostic of a red arm and does not change a verdict on this
node.

**Fix.** Pin the checkout the way the fixture is pinned, with `git -c core.autocrlf=false init`, or
with `git config core.autocrlf false` right after the init. Send the init, add and commit output to
`/dev/null`, so that the capture is the generator's `--check` output alone. For example:
`... commit -q -m checkout --no-verify >/dev/null 2>&1 && "$rv_py" -B "$rv_gen" --check 2>&1`.

**Left-shift gate.** Route every fixture `git init` in the suite through one helper that pins
`core.autocrlf`, so that a new fixture cannot forget it. Add a grep leg that reds on a bare
`git init` in the suite outside that helper. The two existing unpinned inits either adopt the helper
or carry a named exemption.

## Synthesis notes, not findings

These were seen while checking the fold and were NOT put to a skeptic. They are recorded so the L1
fold can weigh them, and they carry no severity.

- **The memory root is an authored pair.** The predicate's `$M` is the driver's `MEMORY_ROOT`, read
  from `.unattended.conf` (`:10`, commented "matching .memory-tree.conf"). The generator reads its own
  `MEMORY_ROOT` from `.memory-tree.conf`. No check comparing the two was found in the driver. If they
  disagree, the predicate matches none of the generator's real inputs and M1 returns silently. The
  pair predates this build, but rev-3 makes the close's safety depend on it. Deriving the input set
  from the generator, as L1's third gate suggests, would remove the dependency.
- **Round 1's third left-shift was not carried.** Round 1 recommended a gotcha recording that a
  freshness check run over the worktree certifies the worktree and not the commit. The fold brief did
  not list it as owed, and no such entry exists under `memory/gotchas/`. That is record-keeping, not
  a defect in the fold.
- **The predicate is deliberately broad.** Any unstaged path under the memory root now blocks the
  render, including notes that feed no view, such as AC4's `BUILD-METHOD.md` arm. That is the cost
  F3 accepted for a one-command repair, not a defect.

## State

- Reviewed at `445eec56`. The two LOW items are unfolded.
- Under `memory/guides/BUILD-METHOD.md` a LOW is FOLDED into its spec as a rev-N bump with a
  section 9 line. Round 1 recorded CONVERGED, which the method makes terminal for its subject, and
  this round's confirmed count (3) is not strictly smaller than round 1's (2). So the method does not
  re-arm a round 3 over the L1 and L2 fold.
- The waived kit suites are still unobserved. The rev-3 arms (39 assertions in the block) are written
  and not run, and the memory-recall self-test at the close's flagged bar is still owed. Neither is
  cleared by this review.
