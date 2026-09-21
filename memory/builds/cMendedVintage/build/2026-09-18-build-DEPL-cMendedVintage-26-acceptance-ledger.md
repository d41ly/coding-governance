# cMendedVintage — the acceptance ledger for unit 26

**Serves:** journal DEPL-cMendedVintage-26

*Node `c`, 2026-09-18, written by the pass that built the unit. No merge bar, no `*.test.sh` suite
and no run of the deployer's own selftest program ran in this pass — the pass's own directive holds
that over the brief, which asked for the suite. Every criterion below was answered by replaying its
own arm OUTSIDE the suite against scratch fixture targets under this run's scratchpad, in the shape
the permanent arms use; the command is stated per criterion.*

## The one thing worth reading twice

**Both defects were observed FAILING before either was observed fixed, under one pre-fix engine.**
The two repairs sit in one shipped blob, so the arms take `govkit.py` at `60bd6a4d` — this unit's
immutable parent, never `HEAD` — and run it over its own copy of each fixture. Under that engine the
scoped update refuses naming a path the target has tracked all along, and the renaming vintage exits
non-zero on the closing self-audit's own `never graded` finding. Under the engine that shipped here
the first reaches its verdict rows and the second exits 0 saying nothing. A liveness arm proves the
old blob carries both defects and the new one carries neither, and the tally half of that liveness is
a POSITION rather than a string: the defect is where the derivation sits relative to the write loop,
so the assertion is an ordering over two anchors and not the presence of a line both engines have.

**The spec asked for a fixture that cannot exist, and finding that out is the unit's real finding.**
rev-1's AC2 wanted an untracked file at an "IN-SCOPE `attributes` row". The row is written into every
receipt carrying the literal `(govkit)` attribution and `--kits` keeps a row only when its `kit` is
in the requested set, so that row is in NO scope, ever. Which means the narrowing this unit ships
does remove the shadow refusal from gov's own `.gitattributes` on a scoped run — and that is correct
rather than a hole, because the classification loop reads the same narrowed list: the row is never
classified, `pins_write` and `pins_drop` stay None, no block is written, no snapshot entry is taken
and the rollback steps over it. AC2 was rewritten to assert that PAIRING — not refused AND not
written — instead of the relaxation alone, because half of it reported on half a behaviour.

**What must not reopen was replayed, and it does not.** `DEPL-cMendedVintage-24` exists because an
operator's uncommitted `.gitattributes` was staged by gov and then unlinked by a rollback's
`checkout-index -f`. That refusal is `demand_claimed_paths_clean`, it grades the whole receipt, and
S1 deliberately leaves it unscoped. It was replayed twice in this pass: once scoped to a kit that row
does not belong to (AC3) and once unscoped, and both refuse, write no block, and leave the operator's
bytes byte-identical afterwards.

## What was NOT done, and why it is not tidiness

No scoping of `demand_claimed_paths_clean` for symmetry with S1. The two guards ask different
questions: this refusal asks whether the WRITE ARM would clobber an untracked file and the write arm
cannot reach a row outside `rows_all`, while the precondition asks whether the operator has
uncommitted bytes where gov claims a path and the rollback can destroy those whichever kits the run
named. AC3 is written to red if a later builder makes them agree.

No second `ls-files` over the unscoped receipt to widen the index read instead. It would pay a
chunked read on every scoped run to refuse over a hazard that run cannot create, and it would leave
the refusal and the write arm disagreeing in the other direction.

No new arm for AC5. The standing `[-24] AC4` arm stages exactly its break — `pins` removed from the
declared set in a copy of the gov — and reds on exactly its red-when, a `_graded_paths` widened to
every receipt row. A second copy would be a copy. This unit's obligation there is that the arm still
holds after the derivation moved, and it does.

**Evidences:** DEPL-cMendedVintage-26

- AC1 — `python tools/govkit/govkit.py update --target <fixture> --kits <one-kit> --write` against a
  two-kit scratch target whose out-of-scope rows are committed and present on disk, asserted by their
  own liveness arm reading both `ls-files` and the filesystem. Under the pre-fix engine the run exits
  non-zero with the `present in the target's WORKTREE` refusal naming one of those tracked paths.
  Under this engine it exits 0, reaches its per-row verdicts and raises no refusal. The criterion's
  red-when — an arm that runs unscoped, where the index read and the row population already cover the
  same paths — is closed by a liveness arm asserting the run printed its own `scope: --kits` line.
- AC2 — `python tools/govkit/govkit.py update --target <fixture> --kits <one-kit> --write` against
  two targets of one recipe whose `.gitattributes` was untracked with `git rm --cached` and
  committed, so the file is present in the worktree and absent from the index, asserted per fixture.
  The scoped run neither refuses over that path nor writes the pin block — both halves in one
  assertion, because the relaxation is only safe as a pair. The unscoped run over the same recipe
  refuses naming it and writes no block, which is the half that reds if the membership test is
  re-narrowed to `table` and reopens what `DEPL-cMendedVintage-24` S3 closed. rev-2 records why the
  criterion could not be written as rev-1 wrote it.
- AC3 — `python tools/govkit/govkit.py update --target <fixture> --kits <other-kit> --write` against
  a target whose tracked `.gitattributes` carries an uncommitted line after gov's close marker,
  asserted dirty by its own liveness arm. The run exits non-zero, exactly one dirty-path line is
  emitted and it NAMES that path, no block is written, and the operator's bytes compare equal
  afterwards. The path is read off the refusal's own line rather than searched for anywhere in the
  output. Red-when closed by construction: the run is scoped to a kit that row does not belong to, so
  an implementation that narrowed the precondition to `rows_all` would pass it straight through.
- AC4 — `python tools/govkit/govkit.py update --target <fixture> --write` against two targets of one
  recipe whose gov renames a claimed source between vintages. Under the pre-fix engine the run exits
  non-zero on the closing self-audit's `never graded` finding, which is the run reporting a defect
  about itself. Under this engine it exits 0 and the finding does not appear. The criterion's
  red-when was about a similarity floor: rev-2 removes the figure rather than deriving it, because
  the fixture renames with NO content edit and so clears any floor by construction, and a liveness
  arm asserts the run really printed a `renamed` verdict — so the tally was handed an old spelling
  rather than the arm passing over an absence.
- AC5 — `python tools/govkit/govkit.py update --target <fixture> --write` from a copy of the scratch
  gov with `pins` removed from the declared writing set, over a fixture whose pin block was tampered
  inside gov's own marker pair so the row reads `pins-moved` and there is a write to grade. The
  closing self-audit fails naming `.gitattributes` as a path this run wrote and never graded, and a
  liveness arm confirms the broken run really did write the block. The break is staged into the
  DISPATCH and not into the tally, so the guard is not being tested against itself. No new permanent
  arm was added: this replays the standing `[-24] AC4` arm's construction, and the criterion here is
  that it survives the derivation moving above the write loop.

## What is OWED

- **Every `[-26]` arm's verdict INSIDE the suite is OWED**, and so is the suite's verdict on the
  `[-24]`, `[-11]`, `[-13]`, `[-14R]`, `[-23]`, `[-RS1]` and `[-PV]` arms this repair is expected to
  return to green. They were replayed OUTSIDE the suite in this pass, in their committed order,
  against fixtures built by the recipe the permanent arms use, and all held.
- **The full selftest program is NOT run in this pass and no red count is reported from it.** The
  pass's directive forbids running a self-test suite inside a unit and overrides the brief, which
  asked for it; the program also takes about 33 minutes, which is past this pass's command bound, and
  a run straddling this unit's own commit would grade two engines. It is the main loop's owed bar.
  The number to beat there is 68 red, and a correct fix is expected at or near 43.
- Nothing else. No criterion here needed a gate, a merge bar or a `*.test.sh` to observe.

## What this unit did NOT fix, deliberately

The precondition's unscoped population still over-refuses: an operator with uncommitted work in a kit
they did not name is stopped by a run that would not have touched it. That is real, it is not this
defect, and section 8's Q2 files it as a backlog question rather than growing this unit — deciding it
needs the rollback's snapshot population read end to end. A kit's declared re-render argv can still
overwrite uncommitted work at a destination gov does not track in `written_paths`, unchanged from
`-24`. And a scoped run still says nothing about the writing rows it is NOT grading; section 8's Q1
recommends against adding that line here, because it is an output-volume judgment coupled to a
regression fix.
