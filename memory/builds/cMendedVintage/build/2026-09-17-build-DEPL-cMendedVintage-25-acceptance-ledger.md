# cMendedVintage — the acceptance ledger for unit 25

**Serves:** journal DEPL-cMendedVintage-25

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh`
suite ran in this pass. Every criterion below was answered against a scratch fixture target under
this run's scratchpad, or by driving the new arm directly over a staged break; the command is stated
per criterion.*

## The one thing worth reading twice

**The fold was observed on the index blob, under two engines, before any refusal was believed.** One
fixture recipe, built twice and run against the engine at `7f3eb6f6` and against this one. Under the
pre-fix engine both verbs printed a re-stage, exited as a success, and the operator's uncommitted
line was **in the target's index afterwards**. Under this engine both verbs refuse, name the path in
full, and the index blob is byte-identical to what it was before the run. No exit code shows either
half of that: the run that folds exits 0 and reports its re-stage as an achievement.

**The specified class predicate could not fail at either site this unit fixes, and that was measured
rather than noticed.** Section 4 asked for a ban on a bare `.split()` over a git read with no `-z`.
After S1 both renormalize guards split on NUL, so deleting `-z` from either left the arm green —
staged exactly that break and watched it pass. A NUL split over a newline-terminated answer yields
ONE element and every membership test below it goes quietly false, which is this unit's own defect
wearing the repaired code's clothes. The arm that shipped grades both split spellings. rev-2 S2.

**The first draft of the predicate was wrong, in both directions, on the real tree.** Run before
wiring, per §7. It walked the module as a single scope and credited every git call ever assigned to
`out` to every `out.stdout.split()` in the file — the `-23` defect, one unit later, in the check
written to avoid it. Scoped to the nearest enclosing function it was right about the six real sites.
Widened to the NUL spelling it then reddened `dirty_claimed_paths`'s `_names` closure, which is
CORRECT code: its argv is `["git", "-C", str(target), *args, "--", *claimed]` and all four callers
pass `-z` through the splice. A spliced argv is now outside the graded population and the arm PRINTS
which calls it could not read, because a skip that looks like a pass is not coverage.

## The class, over the real tree

Both lists, per the brief, and by SYMBOL rather than by line, because three units landed in this
file while this one was specced and every line number in the review is wrong.

HITS — a record-splitting read of a git call with no `-z`:

- `_cmd_update`'s renormalize cleanliness guard, `git diff --name-only HEAD`. The unit's subject.
- `_cmd_apply`'s renormalize cleanliness guard, the same read. The unit's other subject.
- `selfcheck`'s kit-marker scan, `git ls-files` over gov's OWN root. The identical defect one
  repository over; gov's tree carries no such path today, which is exactly why it would rot.
- `gov_tree_mode`, `git ls-tree`. A fixed leading field, conformed rather than exempted.
- `_cmd_update`'s landing loop, `git ls-files -s -- <dest>`. Same shape, same treatment.
- `derive_attribution`, `git log --format=%H`. The one EXEMPTION, carried as a row with its reason,
  its date and the unit that granted it — the format has one placeholder and it is a commit sha.

NEAR-MISSES — a bare split the walker declined to attribute, both read by hand:

- `index_read`'s record loop, `meta.split()`. The receiver is the metadata half of a record the
  caller already split on NUL from an `ls-files -s -z` read. Correct today, and left alone.
- `_cmd_apply`'s post-renormalize LF verification, `ln.split()[0]` over `git ls-files --eol`. The
  walker declines it because the receiver is a loop variable, and it was **broken anyway** — see
  below. This is why the near-miss list is printed rather than discarded.

UNGRADED and announced on every run, never skipped silently: the calls whose argv carries a
`*splice` — `git`, `index_read`'s chunk read and `dirty_claimed_paths`'s `_names`. The arm names
their lines each run.

## The second spelling, which the predicate does not reach

The brief said the risk was fixing the parsing and leaving a second spelling of the same hazard, and
there was one. `_cmd_apply` verifies, immediately after the renormalize, that every pinned path's
INDEX blob is now LF. It takes each path with a TAB split, which a space never breaks — so it is
outside the arm's population and stays outside it. The QUOTING half still reached it. Measured: git
prints `"caf\303\251.md"` for a non-ASCII name and the set it is tested against holds the raw bytes,
so a pinned non-ASCII path was silently dropped from the offending list and that post-condition went
vacuous for exactly the population the guard above it exists to protect. Conformed with `-z` and a
NUL split; measured that `-z` moves the record terminator and the quoting and leaves the fields
tab-separated, so both field reads still answer. rev-2 S3.

## What was measured about git

Throwaway repo, node `c`, git 2.55.0.windows.1, a dirty `a b.txt` and a dirty `café.txt`.
`git diff --name-only HEAD` printed the first raw on its own line and the second as
`"caf\303\251.txt"`. With `-z` both came back raw and NUL-terminated. So `core.quotePath` is not a
second hazard — it is the same one, and `-z` alone disables it. Section 4's claim REPRODUCED
independently, and `core.quotepath=false` beside `-z` stays specified OUT because a knob that
changes nothing is a knob a later reader will believe is load-bearing. `ls-tree -z`, `ls-files -s -z`
and `ls-files --eol -z` were measured the same way: the terminator and the quoting move, the field
order does not.

**Evidences:** DEPL-cMendedVintage-25

- AC1 — `python tools/govkit/govkit.py update --target <fixture> --write` against a scratch target
  holding the pinned path `memory/a b.md`, committed and then edited in the worktree. The run
  REFUSES naming `memory/a b.md` in full, and the criterion's real assertion is the index blob:
  the operator's line is absent from it after the run. Under the pre-fix engine at `7f3eb6f6` the
  same fixture printed `renormalize: re-staged 5 pinned path(s)`, exited 0 and left that line IN the
  index — so the red-when the criterion names, a dirty path with no space, is closed by the arm
  having been seen to fail on the defect it grades rather than by argument. The fixture moves gov's
  pin block first, because `update`'s guard is reached only on a run that writes the block.
- AC2 — `python tools/govkit/govkit.py apply --target <fixture>` against a scratch target holding a
  committed-then-dirtied `memory/café.md`. The run REFUSES naming that path and the index blob does
  not carry the operator's line. Pre-fix, the same fixture folded it. The criterion's red-when — a
  fixture that creates the path but never dirties it — is closed by a liveness assertion that reads
  the index BEFORE the run and requires the operator's line to be absent from it, so a fixture that
  forgot to dirty anything fails there instead of passing here.
- AC3 — `check_git_split_parses` driven over a scratch copy of the engine with `-z` deleted from
  `_cmd_update`'s renormalize diff. It FAILS naming that line. The criterion's red-when is exercised
  by the same run rather than reasoned about: the comment block above that call SPELLS `-z` and is
  left in place, so a predicate matching source text would have passed. AMENDED rev-2 — as first
  written this criterion could not fail at all, because the site it stages the break at NUL-splits.
- AC4 — `check_git_split_parses` over the shipped module reports zero hits and prints its derived
  populations: git invocations, record-splitting reads of one, exemptions matched, and the calls it
  could not read. The criterion's red-when — a vacuous zero — is closed by a liveness assertion
  requiring both populations non-empty, which is the first thing the arm asserts. Both figures are
  derived at observation time and neither is written down in the spec, in the arm or here.

## What is OWED

- **Every `[-25]` arm's verdict INSIDE the suite is OWED.** The two fixture arms and the class arm
  are committed into `tools/govkit/selftest.py` and were driven OUTSIDE the suite in this pass, from
  the same recipe and against the same engine; the class arm was driven by importing the harness and
  calling it directly.
- The full `python tools/govkit/selftest.py` run is **SKIPPED in this pass** and is not reported as
  a number. The machine is heavily loaded with a sibling unit building beside this one, and a run
  that straddled this unit's commit would grade two engines. It is the main loop's owed bar.
- Section 7's other gates — `govkit selfcheck`, `govkit refusal join`, `govkit acceptance matrix` —
  did not run in this pass. No refusal branch was added or removed, so the `BRANCH_PIN` floor is
  untouched.

## What this unit did NOT fix, deliberately

The same word-split lives in `tools/govkit/selftest.py` itself, at two `git diff --cached
--name-only` reads. The arm reads ONE module and says so in its own header; widening it is specified
OUT and the harness is not what an adopter runs. `matrix.py`, the sibling kits and every shell gate
are equally invisible to it. Nothing here grades whether the guard reading those paths is CORRECT,
only that it can see whole names — a structural check reads as a semantic one to everybody who did
not write it, and that sentence is in the arm's docstring, not only here.
