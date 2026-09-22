# Build brief — DEPL-cMendedVintage-11

**Serves:** journal DEPL-cMendedVintage-11

Read the spec whole first. It is unusually complete — its §4 already resolved the question that
would otherwise have been your first day's work — so most of what follows is about the tree the spec
was written against and no longer describes.

*Standing note: ten briefs in this build carried a figure or mechanism measurement disproved. The
last three units each amended their own spec mid-build after measuring, and each was right to. Treat
this one as evidence, not authority, and mark anything you did not run.*

## The line numbers in the spec are STALE, and you should assume every one of them is

The spec names `tools/govkit/govkit.py:3164` for the role gate and `:4627` for the row `apply`
synthesizes. It was written at rev-1 on 2026-09-16. Since then `DEPL-cMendedVintage-10`, `-15` and
`-17` have all landed edits in that file, the last of them an hour ago. Locate every site by symbol
and by the surrounding text the spec quotes, never by the number — a line-keyed read that silently
lands one block over is a class this build has already paid for once.

## What landed immediately before you, and why it is your first read

`DEPL-cMendedVintage-17` gave the `pins` arm a withdrawal path: an empty recomputed pin set now
takes a distinct verdict, deletes gov's marked region and DROPS the `attributes` receipt row,
through the existing `withdrawn_rows` channel. It also added two separate flags around the write and
the deletion.

Your spec's own §3 edge says a row that unit withdraws must not then read here as a missing block.
That edge was written as a prediction. It is now a fact you can measure, and nobody has. Measure it:
build a fixture whose pins are withdrawn by `-17`'s path, then run `check` over it under your change
and confirm it reports nothing rather than a REMOVED block. If the two halves disagree, say so — it
is a finding about a landed unit, not a defect in yours.

## The ordering constraint is satisfied, and here is why it mattered

The build README pins that this unit reds every adopter whose pins moved unless
`DEPL-cMendedVintage-10` ships beside it. That unit is CLOSED, so the remedy exists and you are
clear to red. This is deliberate: the verdict and the verb that clears it land in one release.

## The three criteria that fail quietly

**AC1** — if the extractor is handed the file's whole text instead of the marked span, every target
reads as drifted and your arm passes by failing. An arm that goes green because the subject is
broken is the shape this build exists to close.

**AC2** — appending the tamper AFTER the close marker leaves the block byte-identical, so `current`
is the correct verdict and the arm proves nothing. That exact shape has already been measured on a
sibling arm in this same file. Tamper INSIDE the pair.

**AC3** — testing the row's truthiness rather than the key's presence also swallows a legitimately
empty digest, which silently drops a real row from the graded population. Test for the key.

## The string you must not touch

`merged blocks:` is asserted verbatim by two shipped arms in `tools/govkit/selftest.py`. One shared
counter makes it report `2/2` on a fixture holding one merged row and one attributes row, which is a
false sentence and two red arms in the same edit. Count the roles separately, as S2 says.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, **including helpers added to
`selftest.py` or `matrix.py`** — that class has landed twice in this build, both in test-side
helpers, and the offender pin is a two-sided equality where one name reds two unguarded merge-bar
legs. Spell no `tools/<kit>/…` path in shipped prose and check your own new comments against the
carried-prefix predicate, which was widened five units ago.

## Required of every unit

gov does not dogfood govkit and keeps no receipt of its own, so NONE of your criteria is observable
against this repo — every one needs a scratch fixture target under the run's scratch root, built
with `intake` then `apply`. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-11-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line. Re-declare with `--dispatch` if your write set grows; a widening
re-declaration is the shape the driver now handles. Bound every command at 900s or more.
