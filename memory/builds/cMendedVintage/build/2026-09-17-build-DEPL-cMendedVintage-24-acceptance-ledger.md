# cMendedVintage — the acceptance ledger for unit 24

**Serves:** journal DEPL-cMendedVintage-24

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every criterion below was answered by replaying its own arm against a scratch
fixture target under this run's scratchpad, or by running the committed verb directly; the command is
stated per criterion.*

## The one thing worth reading twice

**The destruction was observed, on bytes, before the refusal was believed.** An exit code shows
nothing here and neither does the rollback order: the whole defect is an operator's uncommitted
`.gitattributes` content being staged by gov and then unlinked by the rollback's `checkout-index -f`.
One fixture recipe was built twice and run under two engines. Under the engine at `a2f840b2` the run
wrote the pin block, rolled a kit back, and the operator's uncommitted line was **gone** from the
file afterwards. Under this engine the same fixture **refuses** naming `.gitattributes`, writes no
block, and the same bytes are byte-identical afterwards. Both halves are permanent arms.

**The pre-fix engine is NOT the build's base, and the spec was wrong about that.** rev-1 asked for
the observation at BASE `859daa67`. `git show 859daa67:tools/govkit/govkit.py` carries no pin write
at all — `DEPL-cMendedVintage-10` landed at `8f1f9b51`, inside this same diff — so at BASE
`.gitattributes` never enters `written_paths`, the rollback steps over it, and the arm would have
passed over an absence. The defect's carrier is HEAD. rev-2 moved the sha and the arm pins it as a
literal, never `HEAD`, for the reason `-14` AC8 records: written against `HEAD` it would grade the
fixed engine against itself the moment this unit's own commit landed. A sibling unit landed under
this session mid-build and moved the branch tip past `a2f840b2`; it touched nothing under this kit,
so the engine bytes at that sha are still the bytes this unit changed, and the arm's liveness half
proves that property rather than trusting the sentence.

**The class fix survived contact with the code, and the instance fix was not what shipped.** The
brief asked for that choice to be re-checked rather than inherited. The write loop leaves every row
at `if a["how"] != "table": continue`, and the pin rewrite and the pin withdrawal are the only other
bytes this verb puts at a receipt-claimed path — so the declared set is accurate rather than
cautious, it is derivable from the loop's own shape, and `WRITING_DISPOSITIONS` is what shipped.
`adopter` is deliberately outside it: a kit's `[[regenerate]]` argv writes under its own authority,
keyed on the kit rather than on a row, and its destinations never enter `written_paths` either. That
boundary is written into the constant's own header and into the tally's, because a guard owes the
reader what it does not cover.

## The other half, grepped for before the commit

The brief named `amendment-leaves-its-other-half-standing` as the class that has fired most in this
build, and it fired here too. Three sites were found by grepping this unit's own diff for the
sentence the code stopped implementing, and all three moved in the same commit:

- `UPDATE_ROLE`'s own row for `attributes` still glossed the disposition as
  `recompute, compare, report; never write`. That gloss is the text the dirty-path guard's header
  quoted to argue the row out of its population, so leaving it would have left the argument intact
  one file up from the guard.
- The `[-12] RULING-A` arms asserted the exclusion's legality in as many words —
  *"its role dispatches to `pins`, which never writes"*. Both underlying facts are still true and are
  now the reason the region carve-out has to exist, so the assertions stayed and the conclusion was
  rewritten.
- `[-12] RULING-B`'s negative half chose its subject with the literal `!= "table"`. **MEASURED, not
  reasoned:** on that fixture the only non-`table` row present on disk was `.gitattributes` itself,
  so the arm would have graded the ruling against the one row the ruling no longer covers. Re-scoping
  the list alone would then have left it quantifying over an EMPTY population — a dead probe
  reporting a clean pass — because every `project-owned` and `rendered` row that receipt claims is
  absent from both the index and the worktree. The fixture now CREATES the shadow instead of
  uncaching one, which is the state the refusal is actually about, and it runs over nine rows.

## The comparison carve-out, and what it is not

Carve-out 4 strips gov's marked region from HEAD's blob, the index blob and the worktree bytes and
clears the path when the stripped forms agree. Each side is folded to LF through `derive_lf` first,
and that fold is a correction rather than a convenience: the two blobs come out of the object
database raw while the worktree copy has been through the target's own checkout filter, so on a CRLF
clone the carve-out would never fire for anybody on Windows — while `git diff`, which decided the
path was dirty in the first place, applies those filters and sees nothing. The ceiling is stated in
the helper's own docstring: an operator whose only uncommitted change outside the region is a line
ending is cleared here.

**Evidences:** DEPL-cMendedVintage-24

- AC1 — `python tools/govkit/govkit.py update --target <fixture> --write` against a scratch target
  whose `.gitattributes` carries an uncommitted line after gov's close marker. The run exits
  non-zero, its dirty-path line NAMES that path, and `wrote the lf-pin block` never appears — the
  refusal fired before the write. The path is read off the refusal's own line rather than searched
  for anywhere in the output, because the fixture settles everything else and a bare substring would
  also pass on a refusal that named something else. The criterion's red-when is closed by the AC2
  fixture: there the same widened population is flagged by both halves of git's own dirty test and
  the run proceeds, so the carve-out is not clearing unconditionally.
- AC2 — `python tools/govkit/govkit.py update --target <fixture> --write` against a target built by
  `make_target` plus the real apply and **deliberately not committed**, which is the post-apply state
  the criterion's red-when warns about every other fixture in this file settling away. An unstaged
  edit inside gov's region is added so both halves of the dirty test flag the path, asserted by its
  own liveness arm. The run proceeds past the precondition and writes the block. The assertion is on
  the precondition's own refusal text and on the write, never on the exit code: measured, a target
  straight out of apply also carries every engine row staged, so the renormalize guard refuses over
  `tools/demo/conf.txt` and the run exits 1 with a finding that has nothing to do with this unit.
  Reading rc there would make the arm hostage to every other guard in the verb. The same behaviour
  was confirmed on a REAL `memory-tree` install outside the fixture govs — intake, apply, no commit,
  then `update --write` — which exits 0 with no dirty refusal, which is ruling A's own burden case.
- AC3 — `python tools/govkit/govkit.py update --target <fixture> --write` against a target whose
  `.gitattributes` was untracked with `git rm --cached` and committed, so the file is present in the
  worktree and absent from the index. The run exits non-zero with the
  `present in the target's WORKTREE` refusal naming that path, and no block is written. Red-when
  closed structurally: the shadow guard and the dirty-path precondition now read one derivation, so
  the two carve-outs can no longer point at each other across a row neither covers.
- AC4 — `python tools/govkit/govkit.py update --target <fixture> --write` twice over one fixture
  recipe. With the real engine the same path is written and the tally stays silent, which is the
  arm that proves the assertion does not red on correct code. With `pins` removed from the declared
  set in a COPY of the scratch gov, the closing tally fails naming `.gitattributes` as a path this
  run wrote and never graded, and a liveness arm confirms that broken run really did write the
  block. A further liveness arm confirms the fixture's receipt carries an `attributes` row, which is
  the criterion's own red-when: over a receipt without one both sets are empty and the assertion
  cannot fail.
- AC5 — `python tools/govkit/govkit.py update --target <fixture> --write` run from two govs that
  differ in exactly one file, the engine, over two targets of one recipe. Under `a2f840b2` the run
  reaches the write and rolls a kit back — both asserted — and the operator's uncommitted bytes are
  GONE from the file afterwards. Under this engine the run refuses and the same bytes compare equal.
  Red-when closed by construction: the pre-fix half is an arm, not a claim, and it reads the file
  rather than the exit code.
- AC6 — `python tools/govkit/govkit.py selfcheck` over this repository exits 0. The failing case was
  observed directly: with the declared set edited to name `pinz` the run prints
  `the declared writing set names disposition 'pinz', which update's dispatch maps no role to` and
  exits 1. The criterion's red-when — an arm that only asserts the set is non-empty — is not what
  shipped: the assertion is membership in the dispatch's own values, so a renamed member reds.

## What is OWED

- **Every `[-24]` arm's verdict INSIDE the suite is OWED**, and so is the suite's verdict on the two
  `[-12]` arms this unit rewrote. They were replayed OUTSIDE the suite in this pass, in their
  committed order, against fixtures built by the same recipe, and all held; the ruling-A and
  ruling-B replays ran against a real `memory-tree` install rather than a fixture gov.
- The full `python tools/govkit/selftest.py` run is **SKIPPED in this pass** and is not reported as a
  number: it exceeded its bound on a heavily loaded machine and was stopped rather than left to
  straddle this unit's commit, which is the `suite-invalidated-by-a-commit-under-it` class the brief
  named. It is the main loop's owed bar.
- Nothing else. No criterion here needed a gate, a merge bar or a `*.test.sh` to observe.

## What this unit did NOT fix, deliberately

The renormalize guard refuses on a post-apply target because every engine row is staged relative to
HEAD; that is a pre-existing behaviour on a different guard over a different population and no
criterion here grades it. A kit's `[[regenerate]]` argv can still overwrite an operator's
uncommitted work at a `rendered` destination: gov does not know that argv's write set, those paths
are outside `written_paths`, and closing it is a unit about a different population. `merged` rows
keep reading dirty-then-clean through carve-out 3's absence exactly as round 4 left them.
