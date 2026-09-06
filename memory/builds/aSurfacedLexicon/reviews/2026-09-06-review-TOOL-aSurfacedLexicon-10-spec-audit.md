**Serves:** spec-audit TOOL-aSurfacedLexicon-10

# Spec audit — the parked unit, re-measured against the tree that landed without it

Tier-2 spec audit · 2026-09-06 · node `a` · build `aSurfacedLexicon` · streams tooling. Five
read-only lenses over the shell wrapper, the scaffolder and the frozen table, the engine's dispatcher
and its conf reader, the selftest harness, and the records a close owes. This is the audit
`TOOL-aSurfacedLexicon-10` never had: the generated roster in the build README named it, alone with
unit 1, as an id no `spec-audit` record has ever covered.

## Verdict: CLEAN WITH FIXES

The design survives intact and the owner's ruling on F1 is buildable exactly as given. What does not
survive is the spec's ARITHMETIC WITH THE TREE. It was written against a base twelve units ago and
then sat parked while every one of them landed, so its citations do not merely drift — some of them
name code that was deleted, and one criterion is factually wrong in both directions at once.

## The finding, which is one finding wearing eleven hats

**A parked spec keeps its reasoning and loses its coordinates.** Every defect below is an instance.
The unit was specced at `6c670b02`, adjudicated, parked for an owner turn, and the other twelve units
built on top of it — including one whose whole job was rewriting the engine this spec cites and one
that deleted the mode this spec offers as its reproducible evidence.

**Struck outright, because the subject is gone:**

- **`--probe` does not exist.** The spec offers `python <engine> --probe` three times as the one
  REPRODUCIBLE command behind its inventory, and names two figures from it. `TOOL-aSurfacedLexicon-3`
  deleted `run_probe` at build order 1, five orders before this unit. Both figures are now
  unreproducible rather than stale, and S3's stated escape hatch — "state its figure in the probe's
  terms" — is not available at all. Replaced by the shipped verb, which prints both counts itself.
- **§8's F1 refutation rests on that same deleted code.** The park recorded that computing candidates
  in the engine would not CREATE the two-readers-of-one-fact class because `run_probe` already made
  it a class with two members. There is now one member. That does not weaken the owner's ruling — it
  strengthens it: the engine route would have re-created a class the order-1 deletion had just
  closed.
- **The dispatcher has four modes, not six.** `--check --list --measure --suggest`.

**Wrong in both directions, in one criterion:**

- **S7** ordered the output to name three pin scalars including `LAYER_OFFENDER_PIN`, at three line
  numbers, and asserted that no `PINS:` block could exist at this build order because unit 12
  introduces it at the next one. The conf carries TWO scalars, `LAYER_OFFENDER_PIN` does not exist
  anywhere (the predicate that owned it was deleted), the line numbers moved, and the `PINS:` block
  exists — unit 12 landed while this unit was parked. A criterion whose subject is that a value
  written beside its source rots, rotted. Re-authored: the output names no pin and points at
  `--measure`.

**Citations that resolve to the wrong thing.** Cited as expressions from rev-5 on:

| Cited | Actual | What sits at the cited line now |
|---|---|---|
| `scaffold_lexicon.py:146` (the closure) | `:184` | `for _p in refused:` |
| `scaffold_lexicon.py:98` (the flag-arity guard) | `:112` | inside the guard's own comment |
| `scaffold_lexicon.py:181` (the descriptive comment) | `:217` | — |
| `adopt-lexicon.sh:247-251` (the overwrite refusal) | `:373-377` | — |
| `adopt-lexicon.sh:184` / `:226` | `:183` / `:225` | — |
| `.lexicon.conf:183` `ratified="2026-08-24 node d"` | `:113`, `"2026-09-05 node a"` | — |
| `selftest.py:95-99` (the `-A` warning) | `:275-279` | the surface-disagreement scan |

rev-1 of this spec congratulated itself on correcting the closure's cite from 143 to 146. It has
moved twice more since.

## What the audit found that the spec could not have known

Four hazards with no counterpart in the document, each of which would have been discovered by
running into it:

- **The engine cannot import the scaffolder at module level.** The sibling reads an engine constant
  in its own module BODY, above which that constant's definition sits, so a top-level import raises
  `AttributeError` out of the sibling and the engine stops importing at all — reddening every leg
  that touches the kit. The import must be function-local, and a landed arm independently requires
  the same thing.
- **Reaching it lazily loads a SECOND copy of the engine.** Run as a script the engine is `__main__`,
  so the sibling's own import finds nothing in `sys.modules` and loads it again under its real name.
  Harmless, and unsurvivable for any identity comparison across the boundary. The suite already
  asserts one such identity elsewhere.
- **The caps substring `CANON` is RATIONED to one occurrence in the scaffolder**, by a landed arm
  asserting exactly that. New code or comment in that file using the word in the register this kit
  writes in reds a different arm than the one the spec's AC8 watches for.
- **`--scaffold` is the fall-through, not a guarded branch.** Adding a mode to the allowlist without
  an exiting handler above it silently runs the scaffold path — which, on an adopted repo, prints a
  plausible-looking refusal that is not the one the operator asked for.

## What the spec got right, and it is the load-bearing half

The measured claims all reproduce. Twenty clusters, twenty live, every representative already
declared, candidate set EMPTY on this corpus — so AC6's population is genuinely empty and AC3's
subset assertion genuinely does need a synthetic fixture, exactly as §4 argued. There is still no
`expanded=` key and no `canon_unfrozen=` key, so S2's guard has no population here and both its arms
are correctly fixture-only. AC5's rev-3 replacement break is right and the original was wrong for the
reason rev-3 gives: the original raises `KeyError` and would red by exception, certifying nothing.
And F2's dirty predicate is the one that can be exercised — every fixture of this kit copies the kit
in untracked, so `git status --porcelain` is non-empty there forever and a refusal built on it could
never fire at all.

## One design change the audit forced

S4's unruled tail is **not** computed by the new function. The engine's own measurement pass already
classifies exactly that population as `unruled`, on every bar, and prints its count. A second
predicate for it in the scaffolder would have been two answers to one question with the copy nobody
grades — the defect this unit's own closure exists to prevent, one level up. The verb reads the
engine's classification instead, and the tail's definition count is therefore the same number
`--check` reports.
