# Build brief — DEPL-cMendedVintage-14

**Serves:** journal DEPL-cMendedVintage-14

Read the spec whole first. This is the only unit in the build that DELETES files in a target's
repository, so the guards matter more than the feature.

*Standing note: fourteen briefs in this build carried a figure or mechanism measurement disproved,
and every one of the last seven units amended its own spec mid-build after measuring. Treat this as
evidence, not authority, and mark anything you did not run.*

## The half that can destroy a record

S3 unlinks. Two things scope it: the glob is `update-conflict-*.md`, and the reap runs only when the
run's `--kits` scope is EMPTY. Both are guards, and a guard you have only seen not-fire is not a
guard — exercise each one directly.

S4 is the guard people get backwards. A run carrying a `--kits` scope reaps NOTHING and says so in
one line. A scoped run classifies a subset of the receipt's rows, so an order belonging to an
out-of-scope row is not stale, it is UNEXAMINED, and deleting it destroys the only record that that
row is still conflicted. Getting this inverted is silent data loss in a repository gov does not own.

S5 is the same distinction one level up, and the spec asks for the reason to be written into the
code beside the glob rather than only into the spec: a withdrawal order records an ACTION whose row
then LEAVES the receipt, so no later run can re-derive it; a conflict order records a STATE every run
re-derives, which is exactly what makes its absence informative. Only the second is reapable.

Exercise every reap against scratch fixture targets under the run's scratch root. Nothing in this
unit should ever point a `--write` run at a real tree.

## Observe the collision as a LOSS, not as an exit code

The basename keying means two conflicts over two files both called `kit.toml` produce ONE order and
the other is silently overwritten. The red you want is the second order's content missing, with both
conflicts genuinely live — not a non-zero exit, which this path will not give you.

## The spec proposes a function name the lexicon gate will red

S1 names `order_slug(path)`. `order` leads no row of `.lexicon.conf`'s verb table. This is the THIRD
consecutive spec in this build to propose a non-conforming name, and the pin is a two-sided equality
where one offender reds two unguarded merge-bar legs. `render` reads right to me — *turn structure
into text*, which is what a filename component is — but `--suggest` is the authority and I have not
run it for your name. The last two units both asked it and both got a different answer than the one
that looked obvious.

## Every line number in the spec is stale

It names `tools/govkit/govkit.py:6891`, `:6975` and `:7021` for the three writers. Seven units have
edited that file since this spec was written, two of them within the hour and one directly in the
write path. Locate all three by symbol and by the text the spec quotes. Note that S2 says the
WITHDRAWAL writer has the same collision and is re-keyed with the other two — three call sites, not
two.

## Out of scope, and the scoping IS the guard

No reaping of `update-rollback-*.md`, `update-preexisting-red-*.md`, or the machine and hole orders
`apply` writes. The last of those are recorded in the receipt's `orders` list, which `check` asserts
against disk, so reaping one would red a target's own install check. A glob scoped to
`update-conflict-*.md` cannot reach any of them, and that scoping is the guard — say in your ledger
that you confirmed it rather than assuming it.

Also out: no counting-threshold refusal, no change to order BODIES, no retro-keying of `apply`'s
filenames, no receipt bookkeeping for conflict orders.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, **including helpers added to
`selftest.py` or `matrix.py`**. Spell no `tools/<kit>/…` path in shipped prose and check your own new
comments against the carried-prefix predicate.

## Required of every unit

gov does not dogfood govkit and keeps no receipt of its own, so no criterion here is observable
against this repo. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-14-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line. Re-declare with `--dispatch` if your write set grows; `--dispatch` refuses a
declaration naming `RUN.md`. Bound every command at 900s or more.
