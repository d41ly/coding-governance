# DEPL-cMendedVintage-24 — the dirty-path refusal still excludes the row this diff taught update to write

**Status:** SPECCED · rev-1 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 34

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`demand_claimed_paths_clean` grades only receipt rows whose `UPDATE_ROLE` disposition is `table`, and
the comment above the predicate justifies excluding the `attributes` row by asserting that gov never
writes it. `DEPL-cMendedVintage-10` and `DEPL-cMendedVintage-17` made that assertion false inside this
same diff: `update --write` now writes `.gitattributes` and stages it, and the rollback restores the
pre-run index entry over it. An operator with uncommitted work in that file therefore has it silently
staged on a normal run and destroyed on a green-to-red rollback. Widen the graded population to the
dispositions this verb actually writes, give the guard a comparison it can make for a row that
carries no `oid`, and remove the prose that argues the old case.

## 2. Scope (IN)

- **S1** The population `demand_claimed_paths_clean` grades is every row whose disposition is a
  member of a declared writing set rather than the literal `table`. The set is `{"table", "pins"}`
  today, declared once beside `UPDATE_ROLE` where `selfcheck` already asserts that table covers the
  role enum. Observed by AC1.
- **S2** `dirty_claimed_paths` gains a fourth carve-out for a path gov owns only a MARKED REGION of.
  A path whose index-versus-HEAD and worktree-versus-index differences all vanish once gov's region
  is stripped from each side is not dirty, because nothing outside gov's own block moved. Without
  this, S1 alone re-creates the burden the `-12` carve-out was taken to remove. Observed by AC2.
- **S3** The untracked-shadow refusal inside `_cmd_update` is scoped by the same declared set. Its
  filter is the identical `== "table"` test, and carve-out 2 of `dirty_claimed_paths` explicitly
  hands the untracked case to it, so leaving it narrow leaves the two carve-outs pointing at each
  other across a row neither one covers. Observed by AC3.
- **S4** The comment block above the predicate stops enumerating dispositions. The paragraph
  asserting that a `.gitattributes` row "can never be that write" is deleted; the `-12` measurement
  is kept and its CONCLUSION is replaced, because the missing `oid` it records is the constraint S2
  is designed around rather than a reason to exclude the row; and the closing paragraph's list of
  harmless dispositions loses `pins`. NOT OBSERVED — a string check over a comment grades spelling
  and not truth, which is the round `DEPL-cMendedVintage-20` spent on a retired flag's absence, and
  what keeps this block honest is S5 reddening on the behaviour the block describes.
- **S5** The closing tally asserts that every path in `written_paths` was a member of the population
  the precondition graded, and `r.fail`s naming any that was not. This is the class left-shift: it
  reds the next time a verb learns to write a role it previously only read, whoever forgets the
  guard. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `apply`'s own write population. `apply` writes far more than `update` does and its
  subset assertion is a larger question about a larger loop; S1 and S2 reach `apply` anyway, because
  both verbs route through `demand_writable_target`, and that is the whole of the benefit this unit
  claims for it.
- No change to the target's gate-leg manifest. `write_gate_legs` writes and stages `gr["file"]`,
  which comes from the target's `deploy.toml` and is not a receipt-claimed path, so it sits outside
  this guard's population by construction rather than by omission. A reader will ask; the answer is
  that "a dirty path OUTSIDE the receipt does not block" is the shipped rule and changing it is a
  scope decision, not a blocker fix.
- No new receipt field. `DEPL-cMendedVintage-7` S9 requires an `attributes` row to carry neither
  identity, and stamping an `oid` onto it to make carve-out 3 apply is the move that regressed the
  exactly-one-identity shape once already.
- No widening of the refusal to differences INSIDE gov's block. Gov rewrites that region on every
  run with or without a rollback, so an uncommitted edit there is not work this guard can preserve,
  and the `pins` disposition already reports it as `pins-moved`.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — that unit put the pin write and its `git add` on
  `update --write` and added `.gitattributes` to `written_paths`, which is what turned the exclusion
  from true into false. Without it there is no defect here.
- **consumes-from** `DEPL-cMendedVintage-17` — the withdrawal is the second write of the same path
  and is snapshotted by the same entry, so the population this unit widens has to cover both
  carriers rather than only the rewrite.
- **hands-off** external — the fix lands inside two preconditions and one tally; nothing else in
  this build reads either guard, and the behaviour an adopter sees is a refusal that did not fire
  before.

## 4. Design

The mechanism is two predicates and one missing comparison, and they are separable.

The predicates are the easy half. Both spell `UPDATE_ROLE.get(row.get("role", "engine")) == "table"`
— once at the dirty-path guard and once at the untracked-shadow refusal — and both become a
membership test against a declared set. The set is `{"table", "pins"}` and it is accurate rather than
cautious: the write loop acts only on rows whose `how` is `table` and whose verdict is in the touched
set, and the only other bytes this verb puts at a receipt-claimed path are the pin write and the pin
withdrawal, which is the `pins` disposition and nothing else.

The missing comparison is the real work. Carve-out 3 clears a path whose index blob is the exact
`oid` the receipt recorded landing there, which is how gov's own staging stops reading as somebody's
work in progress. An `attributes` row has no `oid`, so that carve-out cannot reach it, and adding the
row to the population without an analogue would make every target refuse straight after `apply` —
exactly the state the `-12` ruling was taken to remove, arriving through a different door.

The analogue follows from what gov actually owns in that file, which is the MARKED REGION and not the
file. So carve-out 4 strips gov's region from HEAD's blob, from the index blob and from the worktree
bytes, and clears the path when the stripped forms agree. Right after an `apply` the stripped forms
are all the operator's original content, so the path is clean and the burden stays lifted. An
operator's edit to any other line of `.gitattributes` survives the strip on one side only, so the
path is dirty and the run refuses, which is the hazard this unit exists to close.

Three behaviours of that strip are deliberate. `find_block` raises when a file holds two marker
pairs; the guard treats a raise as "not eligible for the carve-out" and lets the path read dirty,
which is the same direction the write path takes for that state. A file whose HEAD copy carries a
block under an older `GA_BLOCK_ID` spelling strips to nothing there, so the old block counts as
operator content and the run refuses rather than guessing. And the markers are recomputed by calling
`lf_pin_block` with an empty pin set, never read off the receipt row, because the pair is derived
from `GA_BLOCK_ID` before that function looks at a single pin — the same construction the withdrawal
already uses.

Cost stays inside the docstring's own discipline. The four population-wide git calls do not move; the
region strip runs for one path, and only for a path the plain test has already flagged.

### Alternatives rejected

Adding `attributes` to the population by name was the review's own proposed fix and is the cheaper
form. It is rejected because it fixes the instance and leaves the class: the defect's mechanism is a
hand-maintained list of dispositions that has to be re-derived every time a verb learns to write a
role it previously only read, and naming one more member re-commits to that maintenance with no
signal when it goes stale. It also mixes levels — `attributes` is a ROLE and the predicate reads
DISPOSITIONS — so a future role mapped to `pins` would fall through the same hole under a different
name. The declared writing set costs one constant more and is the thing S5 can assert against.

A dedicated dirty check on the attributes path immediately before the pin write, the review's second
option, is rejected for two reasons. It is a second answer to a question `dirty_claimed_paths` says
in its own docstring it is the one definition of, and it would fire mid-write, after the lock is
taken and after other rows have landed, which is the opposite of what the precondition order is for.

Putting carve-out 4 in the caller as a post-filter over the returned dirty list is rejected on the
same one-definition ground, and is the fork §8 records.

### Files touched (estimate)

`tools/govkit/govkit.py` — the two predicates, the declared set beside `UPDATE_ROLE`, carve-out 4
inside `dirty_claimed_paths`, the returned graded population, the tally assertion, and the comment
block. `tools/govkit/selftest.py` — four arms. No other file.

## 5. Production-readiness checklist

- security — the whole unit is a write guard over a repository gov does not own. It strictly narrows
  what gov will stage and what a rollback may unlink; nothing is widened, and the region carve-out
  is the only relaxation, scoped to bytes gov itself wrote.
- perf / scale — one membership test per receipt row, replacing one equality test. The region strip
  costs two `git show` calls for one path, and only when that path already read dirty.
- error / empty / loading states — a receipt with no `attributes` row grades exactly as today; a
  target with no `.gitattributes` takes carve-out 1 or 2 before carve-out 4 is consulted; a file
  holding two marker pairs takes the raise path and reads dirty; a repository with no HEAD keeps the
  worktree-versus-index half only, as the existing code already does.
- observability — the refusal message already names each dirty path and the remedy. A path cleared
  by carve-out 4 is silent, deliberately: it is the post-apply steady state and printing a line for
  it every run would train operators to ignore the block.
- risks — the real risk is the behaviour change on arrival. A target carrying an uncommitted
  `.gitattributes` edit now refuses where it used to proceed, and some operators will have been
  living in that state. That is the guard working, and AC1 observes it rather than avoiding it. The
  second risk is that carve-out 4 is too generous if gov's markers ever appear in a file gov does not
  own the region of, which the caller controls by supplying markers only for the `pins` row.
- testing — AC1 to AC5 run the real verbs against scratch fixture targets; AC4 is observed on a
  staged break. The permanent arms are declared in section 7.
- migration — none. No receipt field moves and no on-disk shape changes, so a target written by the
  previous vintage grades correctly under the new predicate.
- user docs — `WIRE-INTO-PROJECT.md` gains one sentence saying that uncommitted edits to
  `.gitattributes` outside gov's block now stop a write, because the shipped text tells an adopter
  which paths must be clean and that list is about to be true of one more file.

## 6. Acceptance criteria

- **AC1** — When a fixture target's `.gitattributes` carries an uncommitted edit on a line outside
  gov's marked region and
  `python tools/govkit/govkit.py update --target <fixture> --write`
  runs, the run REFUSES naming that path and no byte is written. Red when: the population is widened
  but carve-out 4 clears the path unconditionally, so the refusal never fires and the test passes for
  the same reason the defect does.
- **AC2** — When a fixture target has just completed `apply`, so gov's block is staged and nothing
  else in the file is uncommitted, then
  `python tools/govkit/govkit.py update --target <fixture> --write`
  proceeds and writes. Red when: the arm is run against a fixture that commits after `apply`, which
  is how the existing fixtures model the flow — it would then pass without ever exercising the
  carve-out, and the `-12` burden would ship re-created.
- **AC3** — When a fixture target holds an untracked `.gitattributes` shadowing the receipt's
  attributes row and
  `python tools/govkit/govkit.py update --target <fixture> --write`
  runs, the run REFUSES before the write loop. Red when: the shadow guard is left scoped to `table`,
  in which case carve-out 2 hands the state to a guard that does not grade the row and the rollback's
  absent-entry arm unlinks a file the operator wrote.
  fixture: the tree holds no untracked-shadow fixture for a non-`table` row today; this arm creates
  one.
- **AC4** — When the declared writing set is edited to drop `pins`, so the guard grades a population
  the pin write is no longer in, and
  `python tools/govkit/govkit.py update --target <fixture> --write`
  runs on a fixture whose block moves, the closing tally `r.fail`s naming `.gitattributes` as a path
  this run wrote and never graded. Red when: the assertion compares the graded population against
  itself, or is only ever exercised on a receipt carrying no attributes row, in which case both sets
  are empty and it cannot fail.
- **AC5** — When the AC1 fixture is run at BASE `859daa67` with a kit forced green-to-red, the
  operator's uncommitted `.gitattributes` bytes are GONE after the rollback, and the same fixture
  after this change never reaches the rollback because the run refuses first. Red when: only the
  post-fix half is written. It passes because the refusal fired and proves nothing about the
  destruction, which is the green-by-absence shape this build has already paid for once.
  cost: the BASE half needs a second checkout of the fixture harness at that sha.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a fixture dirtying `.gitattributes` outside gov's block asserted
to refuse, beside a post-apply fixture asserted to proceed · no floor moves.

New arm: `tools/govkit/selftest.py` · an untracked `.gitattributes` shadowing the attributes row,
asserted to refuse · the `BRANCH_PIN` floor in `tools/govkit/refusal_join.py` is re-derived only if
the branch count moves.

New arm: `tools/govkit/selftest.py` · the declared writing set edited to drop `pins`, asserted to make
the closing tally fail naming the ungraded path · no floor moves.

## 8. Open questions

- **Q1 — does carve-out 4 belong inside `dirty_claimed_paths` or in the caller?** RESOLVED (agent,
  2026-09-17, delegated): inside. That function's docstring calls itself the definition of dirty for
  this whole build and enumerates its carve-outs; a post-filter in `demand_claimed_paths_clean` is a
  second definition living one call up, which is the two-guards-one-question-two-answers shape this
  round is already closing elsewhere. The caller supplies the markers and decides which paths are
  region-owned, so the generic function learns nothing about `.gitattributes`.
- **Q2 — should the refusal message distinguish a region-owned path?** RESOLVED (agent, 2026-09-17,
  delegated): no. A path that reaches the refusal has a difference OUTSIDE gov's block by
  construction, so the existing sentence is already true of it, and a second sentence explaining a
  region the operator did not edit is noise on the one message they must read.

## 9. Revision log

- rev-1 · 2026-09-17 · initial draft, authored mid-build after the closing review adjudicated finding
  B3 a BLOCKER. Every line the finding cites was re-opened at HEAD before designing against it: the
  predicate has moved to `tools/govkit/govkit.py:4799`, the pin writes to `:7213` and `:7252`, and
  the justification paragraph reads as quoted at `:4770-4774`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a claimed path dirty when only a gov-owned marked region differs"`
returns NO EXISTING SEAM FITS for the comparison, and the evidence is that the two halves it needs are
already the one implementation of each: `dirty_claimed_paths` is the tree's only definition of dirty
and ranks in the probe's own symbol hits, and `find_block` is the only region locator, called at nine
sites in this file including the withdrawal three hundred lines below the write this unit guards. The
probe surfaced `marker_pair` and `apply_region` as neighbours; neither is a comparator, and both are
reached through `find_block` or through the memory-tree renderer that has nothing to do with a target.

So this unit composes two existing functions rather than minting a mechanism, and the one new
identifier is the declared writing set beside `UPDATE_ROLE`.

Recall terms used: govkit update receipt row disposition UPDATE_ROLE attributes pins dirty claimed
path carve-out oid marked region gitattributes rollback checkout-index written_paths.
