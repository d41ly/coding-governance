# DEPL-cMendedVintage-26 — the scoped-index and rename halves of the dirty-path guard

**Status:** CLOSED · rev-2 · 2026-09-18 · node c · Tier-2 · base 859daa67 · streams deployer · order 37

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-18-build-DEPL-cMendedVintage-26-acceptance-ledger.md](../build/2026-09-18-build-DEPL-cMendedVintage-26-acceptance-ledger.md) | journal | — |
| [2026-09-18-prompt-DEPL-cMendedVintage-26-2-build-brief.md](../prompts/2026-09-18-prompt-DEPL-cMendedVintage-26-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-24` widened two guards to the declared writing set and added a closing tally
that reds when a verb writes outside it. Both halves shipped reading a population one step away from
the one they grade. The untracked-shadow refusal iterates the WHOLE receipt while its index read is
`--kits` scoped, so every out-of-scope writing row reads as absent from the index by construction and
every scoped `update` refuses naming files the target has tracked all along. The closing tally
compares a POST-run receipt against a PRE-run path snapshot, so a renamed row reports itself as
having come apart and `update --write` over a renaming vintage exits 1 on a finding it invented about
itself. Both are shipped-behaviour regressions any adopter reaches. Repair the two predicates; keep
what `-24` closed.

## 2. Scope (IN)

- **S1** The untracked-shadow refusal grades the same rows its index read covers. It iterates the
  `--kits`-scoped `rows_all` rather than the whole receipt, through the same
  `derive_graded_rows` membership test, so a scoped run cannot manufacture an absence out of a path
  it never asked git about. Observed by AC1.
- **S2** The role widening `DEPL-cMendedVintage-24` S3 made STAYS. The membership test remains
  `WRITING_DISPOSITIONS` and is not re-narrowed to the literal `table`, so the `attributes` row that
  unit put back into the population is still graded wherever the run can write it — which, measured,
  is every UNSCOPED run and no scoped one, because that row carries the `(govkit)` attribution and
  is therefore in no `--kits` set. Observed by AC2.
- **S3** The closing tally's two sides read ONE vintage of the receipt. `_graded_paths` is derived
  where `_receipt_paths` already is, above the write loop, so neither side can be mutated by the run
  it is grading. Observed by AC4 and AC5.
- **S4** `tools/govkit/selftest.py` gains the arms: a two-kit fixture updated under `--kits` asserted
  to reach its verdict rows, the same recipe with an untracked `.gitattributes` asserted to pass the
  scoped run WITHOUT a pin write and to refuse the unscoped one, an uncommitted `.gitattributes` on a
  scoped run asserted to refuse, and a renaming vintage asserted to finish clean. Every one of those
  runs a PRE-FIX engine pinned at an immutable sha over its own copy of the fixture first, so each
  half of the repair is observed failing before it is observed passing. Observed by AC1, AC2, AC3 and
  AC4; AC5 is observed by the standing `[-24] AC4` arm, which this unit must not break and does not.

## 3. Non-goals (OUT)

- No scoping of `demand_claimed_paths_clean`. That precondition grades the whole receipt today, and
  the symmetry with S1 is tempting and wrong: a dirty path is the operator's uncommitted work, which
  the rollback can destroy whether or not this run's `--kits` set names its row. Section 4 records
  why the two guards legitimately read different populations, and AC3 is written to red if a builder
  makes them agree.
- No change to `index_read`. Its two return values and its out-of-tree filtering are correct for what
  they do; the defect is that one caller read the map and the rows from different lists.
- No revert of `DEPL-cMendedVintage-24`. The staging-and-destroying hazard it closed on an
  operator's uncommitted `.gitattributes` stays closed, and every criterion below is written so that
  a revert fails it rather than passing quietly.
- No second `ls-files` over the unscoped receipt to widen the index read instead. Section 4's
  alternatives record the measurement that rules it against the narrowing, and the follow-up it would
  belong to is a scoping question about the precondition, not about this refusal.
- No recovery verb for an adopter wedged by the shipped predicate. Nothing is written when the
  refusal fires, so the state is not persistent: the adopter drops `--kits` or takes the next vintage.

### Edges

- **consumes-from** `DEPL-cMendedVintage-24` — that unit declared `WRITING_DISPOSITIONS`, moved both
  guards onto `derive_graded_rows`, and added the closing tally. Without it there is no declared set
  to scope and no tally to re-vintage; this unit repairs its two predicates and keeps its result.
- **hands-off** external — an adopter's `--kits` pulls and renaming vintages stop refusing. Nothing
  else in this build reads either predicate.

## 4. Design

### The two populations, and which one the write arm can reach

*Every line number in this section is where the code sat at rev-1, which is BEFORE this unit's own
diff. They are a reading aid for that vintage and are stale by construction the moment the repair
lands; the symbol names beside them are what a later reader should grep for.*

At `tools/govkit/govkit.py:6798` the index read takes its path list from `rows_all`, which the
`--kits` block narrowed at about `:6697` and announced with the `scope:` line. The very next
statement iterates `derive_graded_rows(receipt)`, which reads `receipt["files"]` and knows nothing
about that narrowing. `index_present` therefore holds only scoped paths, and the test
`w["path"] not in index_present` is true for every out-of-scope row whatever git thinks. The second
conjunct, `(target / w["path"]).is_file()`, is true for every such row the target actually carries.
So a scoped run refuses on exactly the rows it deliberately left out, and the message tells the
operator to `git add` a file that has been tracked the whole time. Measured at the commit boundary on
a two-kit target: parent `cd03941a` prints `scope: 3 of 7 receipt row(s)` and exits 0, while
`d2de6795` refuses naming `tools/check-install-prefix.sh` and its sibling test and exits 2.

The repair is to hand the comprehension the scoped list. The membership test is not respelled inline
— `derive_graded_rows` is the one definition `-24` gave three readers, and a fourth spelling is the
defect that unit exists to prevent — so it is applied to the scoped rows rather than to the receipt,
by passing it a receipt view over `rows_all`.

### What the narrowing gives up, measured rather than reasoned

The `attributes` row is written into the receipt carrying the literal `(govkit)` attribution, and
`--kits` keeps a row only when its `kit` is in the requested set, which that value can never be. So
the row is not in `rows_all` on ANY scoped run — rev-1's AC2 asked for a fixture whose "in-scope
`attributes` row" is untracked and no such fixture exists. What follows is the correct behaviour
rather than a hole, and it is the reason this narrowing is safe: the classification loop iterates
`rows_all` too, so on a scoped run that row is never classified, `pins_write` and `pins_drop` both
stay None, the pin block is not rewritten, no snapshot entry is taken for it and the rollback steps
over it. The refusal and the write arm go quiet together. What does NOT go quiet is
`demand_claimed_paths_clean`, which grades the whole receipt and still refuses on uncommitted bytes
at that path under any scope — which is the half of `DEPL-cMendedVintage-24` that matters, and AC3
asserts it on a scoped run.

Restoring the BASE predicate verbatim is not the fix, and the reason is the half of `-24` that was
right. BASE filtered on `UPDATE_ROLE.get(...) == "table"`, which excludes the `pins` disposition.
That exclusion is what `DEPL-cMendedVintage-23` and `-24` between them closed: `update --write` now
rewrites and withdraws the pin block, so an `attributes` row is a row this verb writes, and a
worktree file shadowing it is the hazard the refusal was written for. S2 keeps the widening and S1
fixes only the list it runs over.

### Why the precondition stays unscoped while this refusal does not

The two guards ask different questions and the populations follow from the questions rather than from
a wish for symmetry. This refusal asks whether the WRITE ARM would clobber an untracked file, and the
write arm can only reach a row in `rows_all` — an out-of-scope row is never classified, never
dispatched and never written, so refusing over one is the tax the `-24` comment block already argues
against in the role dimension. `demand_claimed_paths_clean` asks whether the operator has uncommitted
bytes at a path gov claims, and the answer matters beyond this run: the rollback restores a pre-run
index entry through `checkout-index -f`, which unlinks first, and the snapshot it restores from is
taken over paths this run touched. Narrowing that precondition would be a behaviour change nobody
asked for, argued from a coincidence of shape. It is written down here because a later reader looking
at the two predicates side by side will otherwise file the asymmetry as a defect.

### The tally's two vintages

At `:8471` `_graded_paths` is derived from `derive_graded_rows(receipt)` — the receipt as the write
loop left it. `_receipt_paths`, at `:7526`, is a snapshot of `rows_all` taken before that loop ran.
The rename arm at `:7852` rewrites `row["path"]` in place to the new destination and then
`renamed.extend([old_path, new_dest])` at `:7858` puts BOTH spellings into the list that `:8450`
folds into `written_paths`. The old path is therefore in `written_paths`, in the pre-run
`_receipt_paths`, and absent from the post-run `_graded_paths`, which is precisely the conjunction
`_ungraded` reports. The new destination is excluded by the `p in _receipt_paths` clause `-24`'s
rev-2 added, so it was never the half that fired.

The repair is to take `_graded_paths` where `_receipt_paths` is taken, above the write loop. That
makes both sides of the comparison speak the receipt as it stood when the precondition graded it,
which is the only vintage the tally's own question is about: the precondition ran before the loop, so
asking it about paths the loop invented is asking a question with no answer.

The withdrawal arm looks like a second instance and is not one, measured rather than assumed: a
withdrawn row is appended to `withdrawn_rows` at `:7902` but is not removed from `receipt["files"]`
until `:9163`, which is below the tally. It stays in the post-run population today. The pre-run
snapshot keeps it in the population if that removal ever moves up, which is a side effect of fixing
the general defect rather than a claim about current behaviour.

### Files touched (estimate)

| File | What moves |
|---|---|
| `tools/govkit/govkit.py` | the shadow comprehension's row source; the `_graded_paths` derivation's position |
| `tools/govkit/selftest.py` | the four arms S4 declares |
| `WIRE-INTO-PROJECT.md` | one paragraph, per §5's user-docs row |

### Alternatives rejected

Widening the index read to the whole receipt instead of narrowing the rows is the more thorough of
the two shapes for mechanism A, and it is rejected. It costs a second chunked `ls-files` over a path
list measured in the hundreds on a live adopter, on every scoped run, to answer a question about rows
this run will not touch. It would also leave the refusal and the write arm disagreeing in the other
direction: the operator would be stopped over a hazard that cannot occur in this run, which is the
shape `-24`'s own comment calls a tax rather than a guard. The narrowing is specified because it is
both cheaper and the more correct answer, which is the rare case where those agree.

Filtering the rename's old spellings out of `written_paths` before the tally is the cheaper of the
two shapes for mechanism B, and it is rejected. It is a subtraction keyed on `renamed` holding
interleaved pairs, so it reads correctly only for a reader who knows that `renamed[0::2]` is the old
side, and it leaves the two sides of the comparison still reading different vintages — the next
mutation the write loop learns to make reopens the same class at a different verdict. Moving one
derivation is the same size of diff and closes the class.

## 5. Production-readiness checklist

- security — both repairs affect whether gov writes over bytes it does not own. S1 STRICTLY relaxes a
  refusal, so it is stated plainly: on a scoped run, an untracked file shadowing an out-of-scope row
  — including gov's own `.gitattributes`, which is out of scope on every such run — stops being
  refused over. Those rows are never classified and never written on that run, so the relaxation and
  the write arm move together and nothing is exposed; AC2 asserts that pairing rather than the
  relaxation alone. The case that matters stays covered by the precondition, which S1 deliberately
  leaves unscoped.
- perf / scale — S1 removes an unscoped receipt walk on every run. S3 moves one derivation earlier
  and adds no read. Neither adds a git invocation.
- error / empty / loading states — a receipt with no `files` list yields an empty population on both
  sides and both predicates are silent, unchanged. A run with no `--kits` flag leaves `rows_all` as
  the whole receipt, so S1 is a no-op there, which is why the defect was invisible to unscoped arms.
- observability — the refusal message and the `r.fail` text are already written for the comparisons
  these predicates were meant to make, and neither changes. The `scope:` line already printed above
  the refusal is what makes the false one diagnosable at all.
- risks — the real risk is that S1 reads as a revert of `DEPL-cMendedVintage-24` and someone reverts
  the role widening with it. AC2 and AC3 exist to red on exactly that, and both are written so the
  shipped defect cannot satisfy them.
- testing — AC1 to AC5 run the real verb against scratch fixture targets and one staged break. The
  permanent arms are declared in section 7.
- migration — none. The refusal writes nothing, so an adopter who hit it is in no state to leave; a
  renaming vintage that exited 1 has already done its writes and the next run classifies them.
- user docs — `WIRE-INTO-PROJECT.md` gains a short paragraph in the vintage-migration runbook saying
  that a `--kits` pull grades only the rows it names, because the shipped text currently offers no
  account of why a scoped run and a full one would disagree about the same target.

## 6. Acceptance criteria

- **AC1** — When a two-kit fixture target whose out-of-scope rows are tracked and present on disk is
  updated with
  `python tools/govkit/govkit.py update --target <fixture> --kits <one-kit> --write`
  the run reaches its per-row verdicts and does not refuse. Red when: the arm runs an UNSCOPED update
  instead, where the index read and the row population already cover the same paths, so the predicate
  passes for the reason it always did and the scoped defect goes unobserved.
  fixture: two kits in one receipt, at least one out-of-scope row committed and on disk; the tree
  holds no such fixture today and S4 builds it.
- **AC2** — When the fixture's `.gitattributes` is present in the worktree and absent
  from the index,
  `python tools/govkit/govkit.py update --target <fixture> --kits <one-kit> --write`
  neither refuses over that path NOR writes the pin block there, and the same recipe run UNSCOPED
  REFUSES naming it and exits non-zero. Both halves are one criterion because either alone reports on
  half a behaviour: the first says the narrowing does not leave a writable row unguarded, the second
  says the wider role set is intact. Red when: the repair re-narrows the membership test to `table`,
  which drops the pins row from the population and reopens what `DEPL-cMendedVintage-24` S3 closed —
  the unscoped half reds on exactly that, and a fixture using only an engine row could never tell it
  apart from a correct run. rev-1 asked for an "IN-SCOPE `attributes` row" and no such row can exist:
  section 4 records the measurement.
- **AC3** — When the operator has uncommitted bytes in `.gitattributes` at a path the receipt claims
  and the run passes `--kits` naming a kit that row does not belong to,
  `python tools/govkit/govkit.py update --target <fixture> --kits <other-kit> --write`
  still refuses on the dirty path. Red when: the repair scopes `demand_claimed_paths_clean` to
  `rows_all` for symmetry with S1, at which point a scoped run stages and then destroys that file
  exactly as it did before `DEPL-cMendedVintage-24`.
- **AC4** — When gov's new vintage renames a source a fixture receipt claims,
  `python tools/govkit/govkit.py update --target <fixture> --write`
  exits 0 and its closing self-audit reports no ungraded receipt-claimed path. Red when: the rename
  fixture's two blobs fall below the similarity floor, so the verdict is `withdrawn` rather than
  `renamed`, the tally is never handed an old spelling, and the arm passes without reaching the
  defect.
  figure: rev-2 removes the figure rather than deriving it. The fixture renames with NO content edit,
  so its similarity is 100% by construction and clears whatever `RENAME_SIMILARITY_PERCENT` declares
  without reading it — which is strictly stronger than a fraction computed off that constant, and
  pins no literal either. A liveness arm asserts the run really printed a `renamed` verdict, so the
  red-when is closed by observation rather than by arithmetic.
- **AC5** — When a staged break makes a writing arm write a receipt-claimed path whose role is NOT in
  the declared set, `python tools/govkit/govkit.py update --target <fixture> --write` still has its
  closing self-audit `r.fail` naming that path. Red when: the repair widens `_graded_paths` to every
  receipt row instead of re-vintaging it, which makes the tally unfalsifiable while looking exactly
  like a fix for the rename. No new arm: the standing `[-24] AC4` arm stages exactly this break and
  reds on exactly that widening, so a second one would be a copy, and this unit's obligation is that
  it still holds.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a two-kit fixture updated under `--kits` with an out-of-scope
tracked row, the same recipe with an untracked `.gitattributes` run both scoped and unscoped, a dirty
`.gitattributes` outside the scope, and a renaming vintage · every half also run under a PRE-FIX
engine taken from an immutable sha, over its own copy of the fixture · no assertion floor moves,
because nothing here adds or removes a refusal branch and the `BRANCH_PIN` floor in
`tools/govkit/refusal_join.py` is re-derived only when the branch count changes.

Three fixture constructions are load bearing. The scoped fixture's out-of-scope row must be COMMITTED
and present on disk: an untracked one reproduces the refusal for the honest reason, and an absent one
fails the `is_file` conjunct, so either makes AC1 grade nothing. The pre-fix engine is pinned to a
literal sha and never to `HEAD`, for the reason `-14` AC8 records and `-24` paid for: written against
`HEAD` these arms grade the fixed engine against itself the moment this unit's commit lands. And
AC5's break must be staged into the dispatch rather than into the tally — editing `_graded_paths` to
reproduce the symptom tests the guard against itself, which is the shape §7 of the charter names as
no guard at all.

## 8. Open questions

- **Q1 — should the scoped run announce the rows it is NOT grading?** A line naming the out-of-scope
  writing rows would make the narrowing legible and would have made this defect obvious on the first
  scoped run. It is also one more line on every `--kits` run for a fact the `scope:` line above it
  already implies. The recommendation is NO for this unit: the print is a judgment about output
  volume on a verb an owner reads often, the repair does not depend on it, and adding it here couples
  a behaviour change to a regression fix.
  RESOLVED (agent, 2026-09-18, delegated): NO, as recommended and for the reason given. The runbook
  paragraph this unit adds carries the same fact to the reader who needs it at no per-run output
  cost, which is what made the print easy to decline rather than merely deferred.
- **Q2 — does the precondition's unscoped population deserve its own unit?** An adopter with
  uncommitted work in a kit they did not name is refused by a run that would not have touched it.
  That is a real over-refusal, it is not this defect, and section 3 rules it out of scope. The
  recommendation is to file it as a backlog row rather than to grow this unit, because deciding it
  needs the rollback's snapshot population read end to end and that is a separate reading.
  RESOLVED (agent, 2026-09-18, delegated): NOT THIS UNIT, and not filed by this pass either — the
  write set declared for it names no backlog file, and widening a declaration to carry an unrelated
  row is the shape the dispatch gate exists to refuse. The durable record is section 3's non-goal
  plus this question, both of which land in this commit; the build's wrap-up is where a row belongs.

## 9. Revision log

- rev-1 · 2026-09-18 · initial draft, authored from the read-only attribution that reverted
  `DEPL-cMendedVintage-24`'s two predicates in a throwaway clone and measured 68 red falling to 45
  with no unrelated regressions.
- rev-2 · 2026-09-18 · written by the build pass, after measuring. FOUR amendments, all from the
  same reading. (1) AC2 asked for a fixture whose "IN-SCOPE `attributes` row" is untracked, and no
  such fixture can be built: that row carries the `(govkit)` attribution, so it is in no `--kits`
  set. AC2 becomes the PAIRED observation — a scoped run neither refuses over it nor writes the pin
  block, and the unscoped run over the same recipe still refuses — which observes S2 and makes the
  narrowing's give-up honest instead of unstated. Section 4 gains the measurement and section 5's
  security bullet states the relaxation in the terms it actually has. (2) AC4's `figure:` is removed
  rather than derived: the fixture renames with no content edit, so its similarity is 100% by
  construction and clears any floor without reading one. (3) AC5 gets no new arm, because the
  standing `[-24] AC4` arm stages exactly its break and reds on exactly its red-when; the obligation
  is that it still holds, and it does. (4) S4 and section 7 record that every half also runs a
  PRE-FIX engine pinned at `60bd6a4d` over its own copy of the fixture, so both defects are observed
  FAILING before they are observed fixed. (5) Post-commit, from the diff's own bug-class checklist:
  `demand_claimed_paths_clean`'s header claimed the two carve-outs "no longer point at each other
  across a row neither one covers", which S1 makes half true — corrected in place rather than left,
  because that sentence is the one a later reader will trust. Section 4's line numbers are marked as
  a rev-1 reading aid, stale by construction the moment this repair lands.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the declared writing-row population a scoped update grades for untracked shadows and for its closing tally"`
returns no candidate that fits: the ranked list is name-token noise over `write`, `write_text` and
`derive_scope`, none of which is a membership test over receipt rows, and the one relevant symbol it
surfaces is `classify_row` at fan-in 1. THE SEAM THIS UNIT EXTENDS IS ALREADY IN THE TREE and the
probe's failure to rank it is itself the finding: `derive_graded_rows` in `tools/govkit/govkit.py` is
declared as one definition with three readers, and the repair is to apply that definition to the
scoped list rather than to build a fourth membership test beside it. NO NEW SEAM IS ADDED, which is
the whole shape of this unit — two predicates read the wrong list, and both fixes are changes to what
an existing helper is handed.

The measured population confirms it. The same `derive_graded_rows` call appears in
`demand_claimed_paths_clean`, in the untracked-shadow refusal and in the closing tally, and exactly
the two that were handed something other than the receipt-as-graded are the two that regressed.

Recall terms used: govkit update receipt rows_all kits scope index_read index_present derive_graded_rows
WRITING_DISPOSITIONS untracked shadow refusal dirty-path precondition renamed written_paths closing tally.
