# Build brief — DEPL-cMendedVintage-12

**Serves:** journal DEPL-cMendedVintage-12

Read the spec whole first. This is the most self-contained unit left in the roster — its §3 says in
so many words that it takes nothing from and leaves nothing for any other unit — so unlike the last
four you owe no cross-unit measurement.

*Standing note: eleven briefs in this build carried a figure or mechanism measurement disproved, and
each of the last four units amended its own spec mid-build after measuring. Treat this as evidence,
not authority, and mark anything you did not run.*

## The spec proposes a function name the lexicon gate will red

S1 names `inert_kits(deploy)`. The declared verb table in `.lexicon.conf` requires every function
definition to LEAD with one of its verbs, and `inert` is not one of them — so that name lands as a
verb offender and raises `VERB_OFFENDER_PIN`, which is a two-sided equality where one new name reds
two unguarded merge-bar legs. That class has landed twice in this build already, both times in a
test-side helper nobody thought to check; this is the first time the SPEC itself proposes it.

Ask the declaration rather than taking my word or the spec's: `--suggest` answers one identifier
from the table and the canon. `read` looks right to me — it pulls records from a named source, which
is what this does to a parsed `deploy` — but the tool is the authority and I have not run it.

## Every line number in the spec is stale

It names `tools/govkit/govkit.py:7389` for the set comprehension, `:4889` for the argv resolution,
`:4935` for OBSERVE and `:7387` for the re-render decline. The spec is from 2026-09-16, and four
units have edited that file since — the most recent two touched the `pins` arm and `cmd_check`
within the hour. Locate every site by symbol and by the surrounding text the spec quotes. A
line-keyed read that lands one block over is a class this build has already paid for.

## What the unit is actually about, and the trap inside it

The `inert` list is a posture the target WROTE DOWN, and `apply` — the verb every runbook
recommends as the fallback — currently ignores it and runs the adopter anyway. So the remedy flips
the operator's own declaration.

S1's real content is not the reader, it is that there will be exactly ONE reader. Two consumers
answering the same question from two spellings is the defect class this build was opened to close;
rewire the existing comprehension to call your function rather than leaving it standing beside it.

S3 is the half most easily got wrong. A `rendered` destination absent because its adopter was
DECLINED must be REPORTED with that reason, never failed — the OBSERVE phase already has a branch
that does exactly this for a kit that stopped at an accepted outcome, and a declined adopter is the
second legitimate reason a render can be absent. Reuse that branch; do not write a second one.

S4 says the decline prints on every run that has an inert kit in its selection, including a run
where nothing else happens. A posture that silently changes what a verb does is the same defect in a
quieter coat.

## Do not touch the re-render decline

`update`'s decline is correct, and `DEPL-cMendedVintage-1` depends on it staying OUT of the
render-staleness set. This unit makes it share a reader; it does not move it.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, **including helpers added to
`selftest.py` or `matrix.py`**. Spell no `tools/<kit>/…` path in shipped prose and check your own new
comments against the carried-prefix predicate, which was widened five units ago.

## Required of every unit

gov does not dogfood govkit and keeps no receipt of its own, so no criterion here is observable
against this repo — each needs a scratch fixture target under the run's scratch root. Write the
acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-12-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line. Re-declare with `--dispatch` if your write set grows. Bound every command at
900s or more.
