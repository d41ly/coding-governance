# Build brief — DEPL-cMendedVintage-3

**Serves:** journal DEPL-cMendedVintage-3

The pass this brief is handed to builds the unit that makes the coverage tail tell the operator WHY
each open gap is open. Read the spec whole first.

## The false sentence this deletes

The coverage tail ends with "landing them is a verb that does not exist yet". That was true when it
was written and is false now: the unclaimed-source landing block in the same function writes the
blob, `git add`s it and mints the full receipt row — the exact fields the comment claims it has no
evidence for. The stale paragraph above the block says the same thing and goes with it.

So this is a DELETION plus a join, not a new mechanism. Both halves of the contradiction sit inside
one function about ninety lines apart, which is how it survived.

## The join, and the residue that must not be smoothed over

Each open gap joins against the refusals the run already produced, so the operator reads a reason
rather than a bare path. What matters is the RESIDUE: a destination the rename machinery decided
about is in neither the gap set nor the refusal set. For those, print that no reason was recorded
and point at `plan --emit-declines`.

Do NOT print a claim about resolution for an unmatched residue. A gap with no recorded reason is a
gap with no recorded reason; inventing "already handled" for it is the failure this unit is fixing,
one level down.

## Two things to preserve exactly

**The bare `try/except` around the whole coverage block stays.** It is the liveness guard: a probe
that cannot run says UNAVAILABLE rather than printing a reassuring zero, and the comment beside it
records that a coverage probe must never fail the verb after bytes have landed. Do not let the join
raise out of it, and do not narrow the except.

**`gap 0` still prints.** A clean run that printed nothing is indistinguishable from a join that
never ran. Every count prints including its zeros — that rule is load-bearing here and the sibling
tallies in this same function follow it.

## Bounds

Do not re-derive the refusal strings at print time. They already exist and are already the ones the
operator saw on the refusal line; a second copy is the prose-beside-its-source class. Do not suppress
a gap because it has a reason — a declined row prints with its status, it never vanishes.

## Two corrections from the units already landed, so you do not repeat them

`DEPL-cMendedVintage-1` and `-2` both landed in this same function, so any `govkit.py:<line>` number
in your spec has drifted. `-2` deleted every line citation from its own spec for exactly that reason
after re-taking them twice and watching them drift again inside its own commit. Re-derive by
searching for the text, and prefer citing the text over the line.

`-2` also found that a fixture the spec designed was inert — it staged a condition git did not
actually refuse, so the arm would have graded an ordinary run and passed. Whatever your fixture
stages, confirm the RED is the red you meant, not merely a non-zero exit.
