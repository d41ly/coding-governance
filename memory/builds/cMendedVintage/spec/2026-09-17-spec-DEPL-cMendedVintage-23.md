# DEPL-cMendedVintage-23 — the lf-pin write is contained before the receipt path reaches the root

**Status:** CLOSED · rev-2 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 33

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-23-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-23-acceptance-ledger.md) | journal | — |
| [2026-09-17-prompt-DEPL-cMendedVintage-23-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-23-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`cmd_update` joins the `attributes` row's `path` onto the target root three times for one row and
guards none of the three. The value comes off `install.json`, which is committed, hand-editable and
text-merged in a repository gov does not own. With `../../evil` in that field, `find_block` finds no
marker pair, the verdict reads `pins-moved`, and `write_block` creates a file outside the operator's
repository at exit 0 — while the rollback for that same row calls `demand_contained_dest` at
`tools/govkit/govkit.py:8227`. Grade the row once, before classification decides anything, and leave
one join in the engine instead of three.

## 2. Scope (IN)

- **S1** The `pins` arm of `cmd_update`'s classification loop grades `row["path"]` with
  `demand_contained_dest` as its first statement, above the empty-pin exit and above every line that
  joins or reads. A row whose path escapes the target refuses the run before any byte moves, on the
  read-only preview as well as on `--write`. Observed by AC1, AC2 and AC3.
- **S2** The two write-phase joins at `tools/govkit/govkit.py:7209` and `tools/govkit/govkit.py:7245`
  are DELETED. Both write sites take the path the classification arm already joined and contained,
  carried forward in one function-scoped name beside the existing `pins_write` and `pins_drop`.
  Observed by AC1 and AC3.
- **S3** `selfcheck` gains a structural arm over its own source: a join of the target root onto a
  mapping subscript, whose bound name reaches a mutating call, must carry a containment check on that
  same expression or name. Both spellings of the check count, the helper and the inline
  resolve-and-compare. Observed by AC4.
- **S4** `tools/govkit/selftest.py` gains the fixture arms: a receipt whose `attributes` row path
  escapes the target, exercised through the rewrite branch and through the withdrawal branch, each
  asserted to refuse and to leave nothing on disk outside the fixture. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- No blanket containment grading of every receipt row. Section 4 records the measurement that rules
  it out: a machine-scoped rule with a non-landable role legitimately takes a receipt row whose
  destination sits outside the target, and a blanket grading would refuse that adopter.
- No change to `demand_contained_dest` itself. Four callers pass it a string and get the right
  answer; the defect is the calls that were never made, not the function.
- No fix to the dirty-path carve-out on this same `attributes` row. That is a different guard
  answering a different question — whether the operator has uncommitted bytes there — and it is
  specced by its own unit from the closing review's third blocker.
- No change to the rollback's containment call at `tools/govkit/govkit.py:8227`, nor to `index_read`'s
  deliberate filtering of out-of-tree paths. Both are correct for what they do and neither is a gate
  on this path.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — that unit moved the lf-pin write out of the
  classification loop and into `update`'s write phase, which is what created the unguarded write join
  at `:7209`. Without it this row was read-only on this verb and the escape had no write to reach.
- **consumes-from** `DEPL-cMendedVintage-17` — that unit added the withdrawal, which created the
  second join at `:7245` and, more consequentially for this unit, put an early exit ABOVE the
  classification join. That exit is why the guard cannot sit where the join sits.
- **hands-off** external — the dirty-path carve-out on the same row, and the `never write` paragraph
  in `demand_claimed_paths_clean`'s header that justifies it, are left standing for the unit that owns
  the closing review's third blocker. Nothing else in this build reads the containment change.

## 4. Design

### The three joins, and why two of them exist

One receipt row is joined onto the target root three times inside `cmd_update`. The classification
read at `:6765` binds `_ga` and decides the verdict that sets `pins_write` or `pins_drop`. The
rewrite at `:7209` binds `_pw_path` and writes it at `:7213`. The withdrawal at `:7245` binds
`_pd_path` and splices it at `:7250`. All three operands resolve to the same string, and the row is
synthesized by `apply` with a literal `.gitattributes` at `tools/govkit/govkit.py:5113`, so the only
way the string becomes something else is an edit or a text merge of the committed receipt — which is
precisely the supply channel `demand_contained_dest`'s own docstring was written for.

The write loop's containment check at `:7276` never sees this row. Both arms of the `pins` branch
`continue` before `acted.append` at `:6841`, so the row is not in `acted`.

### Which form of the fix, and why

The review offers two. **This unit specifies the preamble form** — grade the row ONCE, before
classification reads anything — and not the minimum of two calls at the write sites. The minimum
closes the write and leaves `:6765` computing a verdict from a file outside the repository, which is
the read that DECIDES whether a write happens at all; a guard that lets the decision be made on
foreign bytes and only stops the consequence is a guard placed one step too late.

**It is placed at the top of the `pins` arm, not inside the S9 `rows_all` preamble at `:6401`**, and
the reason is measured rather than stylistic. Receipt rows are not all repo-relative by construction.
A rule whose role is not landable goes into `unlanded` at `:5051` and takes a receipt row at `:5205`,
while `demand_contained_rows` deliberately exempts machine-scoped and link rules at `:2394`. So a
blanket grading in the S9 loop would refuse an adopter whose receipt legitimately records a
`{user_skills}`-rooted destination — a false red on correct configuration. Scoping the grading to the
`pins` disposition removes that surface entirely, and once it is scoped that narrowly the `pins` arm
is the same place one function later, with the row already in hand and no second lookup.

**Above the empty-pin exit, not at the join.** The arm's withdrawal branch sets `pins_drop` and
`continue`s at `:6762`, which is ABOVE the join at `:6765`. A guard written at the join — the obvious
placement, and the one the phrase "the classification read" suggests — covers the rewrite and misses
the withdrawal completely. The call goes above `_pins = lf_pins(...)`, the arm's first statement, so
both branches sit behind it.

**The joins are deleted rather than guarded.** Joining one row's path onto the root three times in one
verb is what let two of the three go unguarded; the duplication is the defect's carrier, not an
incidental detail. The classification arm already binds the joined path, so carrying it to the write
phase in one function-scoped name leaves exactly one join for this row in the engine, and that join's
operand IS the containment call. That is smaller than two added guards, it is the charter's own "one
fact in one place", and it makes the structural arm in S3 pass by being right rather than by having a
check nearby.

### The candidate predicate, run over the real tree

Measured on node `c`, 2026-09-17, against `4c4d42fe` in this worktree. Every figure below is PINNED
at that point and is re-derived on each run by the arm S3 adds; none of it is authored anywhere else.

Three widths were run over `tools/govkit/govkit.py`, because the review's phrasing admits all three
and they do not behave alike.

| Width | Population | Hits | False reds |
|-------|-----------|------|------------|
| 1 — any `target /` join with a non-literal operand | 33 | 33 | 31 |
| 2 — operand is a mapping subscript | 10 | 9 | 7 |
| 3 — subscript operand whose bound name reaches a write | 4 | 2 | 0 |

*rev-2 corrects two figures in this table against a RE-MEASUREMENT on the tree this unit actually
landed in. Width 1's population is 33, not 34 — rev-1 counted a wrapped join twice, because a walk
of the syntax tree meets `(target / X).resolve()` as both a call and a join. Width 3's population is
four, not three, and that correction is section 9's second line.*

Width 1 is not a predicate, it is a rewrite. Its population holds `target / prefix`,
`target / dest` and `target / p`, whose operands are locals a reader cannot resolve to a
receipt value without following the binding, and 26 further joins with literal operands sit just
outside it. A gate at this width reds correct code on its first run and is waived within a week.

Width 2 is where the near-misses live, and they are the reason the review's wording needs narrowing
before it becomes an arm. Three of the seven matter. `tools/govkit/govkit.py:7276` carries a
containment check and is spelled INLINE — `.resolve()`, then `.relative_to(target.resolve())` under
`except ValueError` — so a predicate written literally against the helper's NAME reds the one join in
the engine that already does the right thing. `gr["file"]` at `:2636` is graded, at `:3964`, in a
different function and against the string rather than the joined path. `u["dest"]` at `:5238` is
graded upstream by `demand_contained_rows` at `:5046`. The remaining four are read-only existence and
digest probes in `cmd_check` and `cmd_apply`, where nothing is written and a refusal buys nothing.

Width 3 is what S3 adopts. **rev-2: its population is FOUR, not three, and rev-1 named the wrong
reason for the fourth.** `:2636`, whose `rf` reaches `write_atomic` and which passes because
`gr["file"]` is graded in the pre-write pass; `:7209` and `:7245`, which fail; and the write loop's
own `dp`, which rev-1 claimed leaves the population because "the loop's writes travel under other
names". They do not. That binding reaches `dp.unlink()` some 250 lines further down the same loop
with nothing rebinding it in between, so it STAYS in the population and PASSES on its inline
resolve-and-compare. Two hits, both of them this finding, no false red. It would have reddened this
diff.

The correction is favourable and is the reason both spellings of the check had to count: the arm
covers that loop's unlink rather than being silent about it, and a predicate keyed on the helper's
NAME would have reported the one join in this verb that already does the right thing.

**rev-2 also records where the evidence is searched, because that is the arm's real limit.** It is
searched MODULE-WIDE, not within the enclosing function. `:2636`'s join and the call that grades its
operand sit in different functions, so a function-scoped rule reds correct code on the arm's first
run — which is how a structural arm gets waived rather than obeyed. The price is that the arm proves
the expression is graded SOMEWHERE in the engine, not that the grading dominates the write. That is
written into the predicate's own docstring rather than left for a reader to discover.

What width 3 does NOT see, stated plainly because a structural arm that oversells itself is worse
than no arm: it is silent about every write whose destination is not a root-join on a mapping
subscript — a join on a local, a join built in pieces, a path handed in as an argument. The arm
asserts one shape. It does not assert that the engine contains every write, and its own header says
so.

**The first draft of this predicate was wrong in the way `DEPL-cMendedVintage-21`'s was**, and the
run-it-over-the-real-tree rule is what caught it. Crediting every mutating call in a function to
every binding of that name reported three read-only probes as unguarded writes, because one function
binds `dp` five times across as many loops. The window has to end at the next rebinding. Both lists
— the hits and the near-misses at every width — are in this unit's acceptance ledger.

### Alternatives rejected

The review's stated minimum, two calls before `:7209` and `:7245`, is rejected above: it leaves the
deciding read ungraded and leaves three joins where one will do.

Adding the contained path as a field on the receipt row is rejected — the row is the operator's
committed data and gov writing a derived field into it to pass its own guard is a worse shape than
the one being fixed.

Widening `demand_safe_token` to refuse `..` is rejected. Its comment at `:790` already records why
the two guards are separate: one grades characters, the other grades escape, and every legitimate
path fragment here contains `.` and `/`.

### Files touched (estimate)

`tools/govkit/govkit.py` — one call added, one local added, two joins deleted, two write sites
retargeted. `tools/govkit/selftest.py` — two fixture arms. No other file.

## 5. Production-readiness checklist

- security — this unit IS the security change. It closes a path traversal that writes outside the
  repository the operator named, on a verb that runs unattended, with the value supplied by a file
  a text merge can rewrite.
- perf / scale — one string normalisation per run, on one row. The helper takes no filesystem call
  and no target root.
- error / empty / loading states — three branches share the one guard. A receipt with no `attributes`
  row never enters the arm. A withdrawal whose file is already gone still refuses on the path before
  it discovers there is nothing to remove. A row whose path is legal behaves exactly as today.
- observability — the refusal text is `demand_contained_dest`'s own and ends by blaming a `prefix` in
  the target's `deploy.toml`, which is FALSE for this caller. The `where` argument is the only part
  this unit controls and it must name the receipt's `attributes` row, so the operator is sent to the
  file that actually carries the value rather than to one that does not.
- risks — the real risk is placement, not blast radius. A guard at the join instead of at the top of
  the arm passes AC1 and misses the withdrawal entirely, which is why AC3 exists as a separate
  criterion rather than as a second assertion inside AC1. Behaviour change on arrival is nil for a
  healthy target: gov synthesizes this row with a literal path.
- testing — AC1 to AC4 run the real verb against scratch fixture targets and the real `selfcheck`
  against this repo's own source. The permanent arms are declared in section 7.
- migration — none. No receipt field moves, no schema changes, and a target whose row is already
  legal sees no difference.
- user docs — N/A — the operator-facing surface is the refusal message, which section 5's
  observability row already binds; `WIRE-INTO-PROJECT.md` describes adoption and says nothing about
  receipt path containment, so there is nothing there to correct.

## 6. Acceptance criteria

- **AC1** — When a fixture target's receipt carries an `attributes` row with an escaping path and
  `python tools/govkit/govkit.py update --target <fixture> --write`
  runs, the run REFUSES, exits non-zero, and the escaped path does not exist on disk afterwards.
  Red when: the arm asserts the exit code alone, so a guard placed at the write site instead of ahead
  of the classification read passes it while the verdict has already been computed from a file
  outside the fixture.
- **AC2** — When the same fixture is run WITHOUT `--write`, so that only the read-only preview
  executes,
  `python tools/govkit/govkit.py update --target <fixture>`
  REFUSES rather than printing a `pins-moved` verdict. Red when: the containment sits in the write
  phase only, so the preview an operator approves is still derived from foreign bytes and reports a
  confident verdict about a file in another tree.
- **AC3** — When the fixture's receipt carries the escaping path AND no selected kit declares an
  `lf_pin`, so the arm takes its withdrawal branch,
  `python tools/govkit/govkit.py update --target <fixture> --write`
  REFUSES. Red when: the guard is written at the join rather than above the empty-pin exit, in which
  case this branch never reaches it and the withdrawal splices a file outside the fixture whenever
  one happens to carry gov's markers.
- **AC4** — When
  `python tools/govkit/govkit.py selfcheck`
  runs over this repository, the structural arm reports zero unguarded write-reaching root-joins, and
  it reports two when the two bare write joins this unit deleted are staged back in. Red when: the arm
  is written at width 2, where it reds `tools/govkit/govkit.py:7276` for spelling its containment
  inline — a red on correct code, which is the outcome that gets a structural arm waived rather than
  fixed.
  figure: the counts are DERIVED by the arm at every run; section 4's table is the PINNED measurement
  that chose the width.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/govkit.py` · the `selfcheck` structural join over its own source, staged red by
re-introducing a bare write join on a mapping subscript · no floor to move.

New arm: `tools/govkit/selftest.py` · a fixture receipt whose `attributes` row path escapes the
target, driven through the rewrite branch and the withdrawal branch · the `BRANCH_PIN` floor in
`tools/govkit/refusal_join.py` does not move, because the guard raises through the helper's existing
branch and mints no new refusal site.

## 8. Open questions

- **Q1 — should the containment failure abort the run or be recorded as a finding?**
  RESOLVED (agent, 2026-09-17, delegated): abort, which is what calling `demand_contained_dest`
  chooses. A finding would let the loop classify the remaining rows against a receipt already known
  to be corrupt, and every other containment site in this engine aborts — a second answer to the same
  question is the class this build has already paid for twice.

## 9. Revision log

- rev-1 · 2026-09-17 · initial draft, authored mid-build after the closing review adjudicated finding
  B2 a BLOCKER. Adopted under the protocol's discovery rule as a blocker between this run and its own
  landing.
- rev-2 · 2026-09-17 · four corrections, every one from a measurement taken during the build rather
  than from re-reading rev-1. (a) Section 4's width-1 population is 33, not 34: rev-1 double-counted
  a join it met twice while walking the syntax tree. (b) Width 3's population is FOUR, not three, and
  rev-1's stated reason for excluding the fourth — the write loop's own `dp`, said to be "bound only
  to be containment-tested" — is false: that binding reaches an `unlink` 250 lines later and passes
  on its inline check. (c) Section 4 now records that the containment evidence is searched
  module-wide, with the reason and the price, because a function-scoped search reds a correct site.
  (d) AC4's staged-red names the two joins this unit deleted rather than a `row["path"]` operand that
  is not what either of them spells. None of the four changes the design: the guard, its placement,
  the deleted joins and the arm's width are all as rev-1 specified, and the fix was measured to
  behave exactly as section 5's risk row predicted.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a receipt-supplied path for containment before joining it onto the target root and writing"`
returns a ranking of name-token neighbours and does NOT name the seam, which is a property of the
tool rather than a finding: it ranks how often a name stem appears and resolves no symbols, and its
own header says a high rank never means "this is the seam you want". THE SEAM NEVERTHELESS EXISTS and
this unit extends it — `demand_contained_dest` at `tools/govkit/govkit.py:807`, already called from
`:2398`, `:2462`, `:3964` and `:8227`, one of which is the rollback for this exact row. Nothing new is
built here. What the probe did surface usefully is `check_paths_never_lost`, `dirty_claimed_paths` and
`raw_write_cells`, all in the same file and all structural assertions about the engine's own
behaviour, which is the shape S3's `selfcheck` arm takes rather than a new mechanism.

Recall terms used: govkit update attributes row lf-pin block receipt-supplied path containment
demand_contained_dest target root join traversal escape write_block find_block pins-moved
pins-withdrawn install.json.
