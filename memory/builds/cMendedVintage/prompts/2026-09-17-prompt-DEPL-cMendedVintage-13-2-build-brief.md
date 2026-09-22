# Build brief — DEPL-cMendedVintage-13

**Serves:** journal DEPL-cMendedVintage-13

Read the spec whole first. This is the largest unit left in the roster and the only remaining one
that is an EXTRACTION rather than a repair — most of the risk is in the half nobody asked you to
change.

*Standing note: twelve briefs in this build carried a figure or mechanism measurement disproved, and
every one of the last five units amended its own spec mid-build after measuring. Treat this as
evidence, not authority, and mark anything you did not run.*

## The risk is `apply`, not `update`

You are lifting `_cmd_apply`'s manifest-emission core into a shared function and giving `update` a
second call site. `update` gaining the behaviour is the point; `apply` CHANGING behaviour is a
regression in a verb nobody asked you to touch, and it is the failure this unit is most likely to
ship.

Measure it rather than reasoning about it: run `apply --write` over a scratch fixture against the
PRE-change engine, capture stdout and the resulting runner file, then run the same fixture against
your engine and diff both. `apply` keeps its own `step` prints, its before/after verdict maps and
its kit-subject advice, so the diff you want is empty.

## The floor the spec buries in §7

`tools/govkit/refusal_join.py`'s `BRANCH_PIN` is raised to the live count **in the same commit**.
Forgetting it reds the bar, and the number is DERIVED by that engine rather than typed — read it
from the engine's own output, never carry it from anywhere.

## Two shapes that lose data quietly

**S4 — ownership is MERGED, never replaced.** A scoped run that rewrote the whole
`gate_runner.emitted` list revokes gov's claim on an out-of-scope leg, and after that every later run
refuses the leg gov itself wrote. The union is with the PREVIOUS receipt's rows for kits outside the
scope.

**S5 — in `update` a bad runner file is `r.fail`, never `Refusal`.** `apply` raises and is right to,
because nothing is written yet. In `update` the bytes are already on disk, so an abort leaves the
target updated with an un-restamped receipt and no emission. That wedge has been recorded against
this step twice.

## The ordering that is easy to get backwards

S2 puts the emission after the write loop AND after the verify/rollback pass. A kit whose writes were
reverted must not have its legs emitted by the same run. S3 is the other half and points the opposite
way: a leg is a DECLARATION, not a file, so a claimed kit whose bytes did not move this run IS still
in the population — that case is the whole reason this unit exists. Population is the receipt's
claimed kits, narrowed by `--kits`, minus what this run rolled back.

## The function name will trip the lexicon gate if you let it

The obvious name for what you are extracting starts with `emit`, and `emit` is in no row of
`.lexicon.conf`'s verb table. A non-conforming definition raises `VERB_OFFENDER_PIN`, a two-sided
equality where one name reds two unguarded merge-bar legs. `DEPL-cMendedVintage-12` hit this exact
trap one unit ago — its spec proposed `inert_kits` and `--suggest` resolved it to `read_inert_kits`.
Ask `--suggest` rather than guessing; it is the authority and I have not run it for your name.

## Every line number in the spec is stale

Five units have edited `tools/govkit/govkit.py` since this spec was written on 2026-09-16, two of
them within the hour. Locate every site by symbol and by the text the spec quotes.

## Out of scope, explicitly

Do not fix `TOOL-dRetiredFork-27`, the duplicate row a manifest whose `dedupe_key` is `name` keeps.
This unit gives that behaviour a second caller and must not widen it; the row is open and stays open.
Say so in your ledger if you see it fire.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, **including helpers added to
`selftest.py` or `matrix.py`**. Spell no `tools/<kit>/…` path in shipped prose and check your own new
comments against the carried-prefix predicate.

## Required of every unit

gov does not dogfood govkit and keeps no receipt of its own, so no criterion here is observable
against this repo — each needs a scratch fixture target under the run's scratch root. AC6's atomic
write is named by your spec but closed by `DEPL-cMendedVintage-21`, which is later in the roster:
record it OWED rather than claiming it. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-13-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line. Re-declare with `--dispatch` if your write set grows, and note that
`--dispatch` refuses a declaration naming `RUN.md`, which the last unit tried. Bound every command
at 900s or more.
