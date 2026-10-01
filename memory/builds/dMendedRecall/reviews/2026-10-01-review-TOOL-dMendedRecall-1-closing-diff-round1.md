**Serves:** diff-review TOOL-dMendedRecall-1 TOOL-dMendedRecall-2 TOOL-dMendedRecall-3

# dMendedRecall: Tier-2 closing diff review of units 1 to 3, round 1

*Node `d`, 2026-10-01. This is the unattended build's closing review under
`memory/guides/BUILD-METHOD.md`. Harness: `tools/workflows/tier2-review.js`, with four primed finder
lenses, four skeptic batches prompted to REFUTE each finding, and this synthesis. The lens brief was
the recurring-bug-class checklist that `python tools/memory-tree/gotchas.py --for-diff
1f915870..0cfb51da` selected (31 anchored classes plus 6 universal). By the owner's instruction this
build had no spec audit and no pre-code cross-read, so this review is the first one the specs under
`memory/builds/dMendedRecall/spec/` get as well as the first one the code gets. Each unit's
acceptance ledger is under `memory/builds/dMendedRecall/build/`.*

**Range reviewed: `1f9158708e4782dfe2d25a17fdf4153f57d38ae3...0cfb51da3adedf3063b03763e8838bcd54dc6c56`**
(branch `run/dMendedRecall`, 18 files, +1522/−36).

**Round: 1.**

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. One item is MEDIUM, and it sits in unit 2's surface. Under
`LANDER_MODE=primary`, which is the kit default, the new view render reads the operator's unstaged
edits to its own inputs. It then stages the views those edits moved while the edits stay unstaged,
so the records commit passes its pre-commit and is index-stale against its own sources. Units 1 and 3
drew no confirmed finding. This report folds nothing. The item is owed a fix under unit 2's spec
before the build lands, and the fold is owed a round 2, because fold text is unreviewed surface.

## Review shape and run integrity

- **Raw 8, confirmed 2, refuted 6, unverified 0, precision 0.25**, which is 2 / (2 + 6).
- **Refuted:** six raw findings did not survive their skeptics. Their text did not reach this
  synthesis, so they are recorded here as a count only.
- **Adjudicated tally by item:** 1 item. That is 0 BLOCKER, 0 HIGH, 1 MEDIUM (M1) and 0 LOW.
- **Adjudicated tally by raw confirmed finding:** 0 BLOCKER, 0 HIGH, 2 MEDIUM (ids 3 and 7) and 0
  LOW. That totals 2, and every confirmed id is in exactly one item.
- **Merges:** the harness reported 0 duplicates, and it only counts identical findings. Ids 3 and 7
  came from different lenses and describe one defect at adjacent lines of one function, so this
  synthesis merged them into M1. Both were raised as medium, and adjudication kept medium.
- **Run integrity:** lenses 4/4 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. No
  contradictory verdict was demoted to unverified, no spurious verdict was discarded, and there were
  0 duplicates. Every counter is zero, so **this run is complete**, and the finding set is the
  lenses' whole result, not one missing a dead lens's share.
- **Precision is below 0.5.** §8 says to tighten scope or priming before adding agents. Six of eight
  raw findings were refuted, so the next round should prime the lenses with this build's security
  model and its waived suites more explicitly. Adding more agents is not the fix.
- **What the synthesis checked itself.** It re-read every cited site at `0cfb51da` and re-pinned the
  line numbers below. It also reproduced M1 in a scratch clone of this repository at `0cfb51da`,
  under the session scratchpad. The base tree's `--check` read `build-index: clean`. An unstaged
  `SPECCED` to `INPROGRESS` flip on line 3 of aPacedTurnstile's spec 14 was followed by `--write`,
  which moved `memory/LIVE.md`, that build's `README.md` and `memory/ledger/2026-08.md`, and all
  three were clean before the render. With exactly those three staged, the worktree `--check` still
  read `build-index: clean`. After that commit and a `git checkout --` of the input, `--check`
  printed `build-index DRIFT` and named `memory/LIVE.md` as stale.

## What the zero counts for units 1 and 3 mean

The run is complete, so a zero here is evidence from four lenses and four skeptic batches. It is
still not an observation. Unit 1's whole leg, the memory-recall kit self-test, is observed only at
the close's flagged bar, and that bar has not yet run. The unattended kit's suites are waived for
this landing by the build README's rule, so the S6 arms of unit 2 and any arm added by the fold are
written and not run here. A clean review cannot stand in for either reading.

## Findings

| # | Sev | Where | What | Raw ids |
|---|---|---|---|---|
| M1 | medium | `tools/unattended/unattended.sh:6934` | under `primary`, the render feeds on the operator's dirty view inputs, and its delta rule stages the views they moved | 3, 7 |

### M1 — under `primary`, the render stages views derived from the operator's unstaged inputs

**Where:**

- The render is at `tools/unattended/unattended.sh:6934` (`run_bounded "$py" -B "$gen" --write`).
- The delta rule is at `:6937-6945`. It stages every path at `:6942` that was clean before the
  render and dirty after it, and runs `GIT add -A` on that set at `:6945`.
- The spec sentence it falsifies is the risks bullet of spec 2 §5, at
  `memory/builds/dMendedRecall/spec/2026-10-01-spec-TOOL-dMendedRecall-2.md:206-210`, which says
  "only the run's own writes can move it".
- The AC4 arms that cannot reach it are at `tools/unattended/unattended.test.sh:11298-11317`.

**Defect.** S3 protects only the OUTPUT side of the render. It snapshots the paths that were dirty
before the render, and it never stages one of those. It never asks whether a generator INPUT was
dirty. `gen_build_index.py` lists tracked paths with `git ls-files` and reads their bytes off disk.
It does this through `read_text` at `:247`, through the memory-root listing at `:851` and through
`read_bindings` at `:610`, and it reads `.memory-tree.conf` from the top at `:295`. So an unstaged
edit feeds `--write`. That edit could be a spec status header, another build's `BACKLOG.md` row or
README front matter, or the conf. Every view derived from it that was clean before the render then
lands in `stage`. That set includes `memory/LIVE.md`, a family view under `memory/backlog/`, a
ledger shard, and another build's README region. The source edit itself stays unstaged.

**Reach.**

- Under `primary`, `verb_close` (`:7303`) never calls `check_clean`. Refusal 62 in
  `check_inplace_preconditions` (`:7166`) runs only under `in-place` (`:7614`).
- `write_inherited_asks` runs on the `land`, `hold` and `other` states (`:7698-7700`). So a dirty
  tree reaches the auto-file with a filed count above zero, and a hygiene red of its own does not
  stop the filing.
- Spec 2's own Evidence section (`:114-118`) says that S3's case "is not hypothetical" under
  `primary`.
- This repo declares `LANDER_MODE="in-place"` (`.unattended.conf:23`), so it is not affected. The
  kit default is `primary` (`unattended.sh:528`).

**Impact.** The records commit carries views that encode uncommitted edits. The pre-commit cannot
see it. Hygiene check 9 (`tools/memory-tree/check-memory-hygiene.sh:1039-1041`) runs
`gen_build_index.py --check`, which renders from the WORKING TREE, so the commit passes. AC4's own
commit arm (`unattended.test.sh:11313-11314`) uses the same predicate, and so does the fixture's
pre-commit. Check 9 then reds on a clean tree, in two cases:

- at the pre-push or CI bar, once the operator discards the edit. The pre-push's dirty-tree
  refusal forces a commit or a discard before any push.
- in any checkout of that commit, for example under bisect.

That red is the stale-index red this unit exists to remove, back again by a second path, and the
repair is a hand re-render. In derived form it also commits work the run did not do, which is S3's
own stated reason for not staging. The failure was loud at BASE: the operator's commit met check 9
and refused. Unit 2 made it silent.

**Why AC4 cannot catch it.** AC4's dirt is an untracked `memory/notes.md` and a tracked
`memory/guides/BUILD-METHOD.md` edit (`:11299-11300`). `ls-files` never feeds the first to the
render. The second is not a build, spec or backlog input, so no view moves. The README arm
(`:11321-11326`) edits an authored body line, which no other view derives from. Every one of these
arms passes whether or not the render reads dirty inputs. That is the fixture-passes-by-finding-
nothing class, and `memory/gotchas/inputs-inside-the-subjects-reach.md` names the method that would
have found it: list who SUPPLIES each input to the render.

**Adjudication: MEDIUM.** It is reachable on the kit's default mode, it makes a refusal that used to
be loud into a silent stale commit, and the shipped spec states the opposite. The damage is bounded.
Nothing is lost, the operator's input is never committed, and a re-render repairs the tree. That is
why it is not HIGH.

**Fix, and the fork it carries.** Both confirmed findings propose the same direction: do not stage
the render's output when a generator input was dirty before it. The fold must record which predicate
it takes, because the choice changes AC4.

- **(a) Recommended.** Before the render, intersect the tracked half of `h0` with the generator's
  input set. That set is `GIT ls-files -- "$M/"` plus `.memory-tree.conf`. A bare "under the memory
  root" predicate, which both findings spelled, misses the conf. If the intersection is non-empty,
  skip the render and stage nothing. Print the miss line naming those dirty inputs, with
  `derive_index_repair`, and return 1. The rows stay staged, as S4 already does on a miss. The
  operator's commit then meets check 9 loudly, which is BASE's behaviour, and the line has already
  said why. Untracked dirt never feeds the render, so the `notes.md` arm keeps its verdict. The two
  tracked arms do not keep theirs. `BUILD-METHOD.md` and the README are both under the memory root,
  so each one now expects the miss line naming it, and spec 2's AC4 must be amended to say so.
- **(b) Render against the index instead.** Commit the index to a temporary tree, render in a
  scratch checkout of it, and stage only the outputs whose bytes differ from the index blob and
  whose worktree path was clean. That is precise and keeps AC4's arms as written. It costs a
  checkout of the whole tree for each filing close, against spec 2's stated "a few seconds", and it
  adds a second write path into the operator's tree.

Either way, the fold amends spec 2. S3 gains the input-side rule. The §5 risks bullet loses "only
the run's own writes can move it". AC4 gains the arm below. The fold records the decision as a
revision-log line.

**Left-shift gate.**

- **Unit-2 arm.** In the TOOL-dMendedRecall-2 block, add a `primary` fixture that leaves an
  unstaged edit on a tracked spec's status header, flipping `SPECCED` to `INPROGRESS`, and then
  runs the filing close. Assert that `memory/LIVE.md` is absent from `git diff --cached --name-only`
  and that the output names the dirty spec. Before wiring it, stage the break on today's driver and
  confirm RED (§7), since today's driver stages `LIVE.md` here. Under the build's waiver this arm is
  written and not run here, and its first reading is owed with the waived suites.
- **The class: grade the commit, not the worktree.** AC2's and AC4's freshness arms run `--check`
  over the fixture's working tree, which can only certify the worktree. Re-run each one over a
  clean checkout of the commit, for example `git archive HEAD` into a fresh directory with a
  `git init` over it, and expect `build-index: clean` there too. That arm reds on this defect
  whichever input was dirty, and it would catch any later path that stages a view its source does
  not carry.
- **A gotcha entry.** Record that a freshness check run over the working tree certifies the
  working tree and not the commit, and point it at check 9 and this item. Then the next diff that
  stages derived output is handed the class by `gotchas.py --for-diff`.

## State

- Reviewed at `0cfb51da`. The report is unfolded, so a round 2 over the fold is owed.
- The waived kit suites and the memory-recall self-test at the close's flagged bar are still
  unobserved. Neither is cleared by this review.
