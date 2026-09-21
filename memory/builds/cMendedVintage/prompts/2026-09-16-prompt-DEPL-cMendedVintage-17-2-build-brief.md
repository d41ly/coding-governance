# Build brief — DEPL-cMendedVintage-17

**Serves:** journal DEPL-cMendedVintage-17

The second repair to `DEPL-cMendedVintage-10`'s write, and unlike the first one this defect is LIVE
in the tree right now. Read the spec whole first.

*Standing note: nine briefs in this build carried a figure or mechanism measurement disproved — the
most recent found its whole blocker already fixed in another spelling and correctly wrote no code.
Anything below I have not run is marked UNVERIFIED. Measure before you build.*

## Why this one is urgent rather than tidy

The `pins` arm sets `_om, _cm, _text = ("", "", "")` when the recomputed pin set is empty, leaves
`_span` at `None`, and still evaluates to `pins-moved`. It does not skip.

Before `DEPL-cMendedVintage-10` that verdict only printed a line. Two units ago it gained a WRITE. So
a target that HAD pins, and whose claimed kits now declare none, calls
`write_block(cur, "", "", "", "append")` on every run — and `find_block`'s marker test with an empty
marker matches every blank line in the file.

That is not a raise-and-stop. It is a splice at an arbitrary position in a file the target owns,
every run, silently. `DEPL-cMendedVintage-15` proved that the pin block survives a rollback; nothing
protects a file spliced at a blank line.

## What the fix has to separate

A withdrawal is a real state with a real answer — the block should go, not be rewritten empty. Give
it its own verdict rather than folding it into `pins-moved`, so the summary line tells an operator
which of the two happened. Gate the write on a non-empty pin set; that is the guard, and the verdict
is what makes the guard legible.

## The fixture you need probably exists now

`DEPL-cMendedVintage-15` built a scratch gov whose kit carries an `[[lf_pin]]` and whose target has a
tampered block, and used it to stage a green-to-red check across a run. A target that HAD pins and
now declares none is one descriptor edit away from that. Reuse it rather than building a third
scratch gov — and if it does not reach your case, say so rather than forcing it.

Observe the RED first, and be specific about what the red IS: not merely a non-zero exit, but the
empty-marker splice landing bytes at a blank line in a file the run did not mean to touch.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, **including helpers added to
`selftest.py` or `matrix.py`** — that class has landed twice in this build, both in test-side
helpers. Spell no `tools/<kit>/…` path in shipped prose, and check your own new comments against the
carried-prefix predicate, which was widened three units ago.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-17-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED; if you discharge an owed
criterion belonging to another unit, say so explicitly and add its own `**Evidences:**` block, as
`DEPL-cMendedVintage-15` did for `-10`'s AC4. Keep every backticked span whole on its own line.
Re-declare with `--dispatch` if your write set grows. Bound every command at 900s or more.
