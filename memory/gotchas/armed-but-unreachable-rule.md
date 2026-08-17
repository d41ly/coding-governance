---
name: armed-but-unreachable-rule
description: a declaration can be non-empty, well-formed and still impossible to violate — testing that a rule EXISTS is not testing that it can FIRE
kind: class
universal: false
---

# armed-but-unreachable-rule

**A declaration can be non-empty, well-formed, and still impossible to satisfy or violate. Testing
that a rule EXISTS is not testing that it can FIRE.**

## The instance that produced this class

`tools/lexicon/` gates a forbidden import direction declared as `<glob> -> <glob>`. The engine armed
two vacuity defences from the start: `NOT ARMED` reds when the rule list is EMPTY, and `DEAD PROBE`
reds when an extractor selects no definitions. Both were green. The first real rule this repo
declared was:

```
tools/lexicon/* -> tools/codebase-map/*
```

and it could never match anything, because the matcher compared an import NAMESPACE against a repo
PATH by swapping dots for slashes. No Python module name may contain a hyphen, so no import could
ever produce `tools/codebase-map/...`. The predicate reported `LAYER_OFFENDER_PIN="0"` — a confident,
unfalsifiable zero that no edit could move — and the charter gained a bullet asserting a measurement
over the empty set.

The kit's own module docstring named `vacuous-selector-empty-population` as its dominant failure mode
while shipping an instance of it. Four independent verifiers in the closing review reproduced it.

## Why the existing defences missed it

They test the two ends and not the middle:

| defence | question | blind to |
|---|---|---|
| `NOT ARMED` | is the rule list empty? | a non-empty rule that cannot match |
| `DEAD PROBE` | did the extractor find anything? | a rule the extractor's output can never satisfy |

The fixture missed it for a different reason, and that is the more transferable half: the test used
`core/* -> adapters/*` with `import adapters.db`, where the namespace **happens to spell the path**.
A fixture easier than production certifies coverage production does not have.

## The check that does NOT work, recorded because it was written and shipped

**Proving reachability by CONSTRUCTION is a tautology, and the attempt is instructive.** The first
fix synthesised a violating import from each real target file — its stem, its dotted path, a relative
form — and required the matcher to flag one. It looked rigorous. It certified everything:

```
with the PRE-FIX (known-blind) resolver, unreachable rules reported: NONE
synthetic dotted form: tools.codebase-map..codebase-map.conf   <- a string no import can spell
```

Every synthetic derived from the target's own PATH round-trips through the resolver's own
path-mirroring reading, so the construction proves the resolver agrees with itself. Restoring the
exact resolver whose blindness the arm existed to catch still yielded a clean bill. **A vacuity check
that is itself vacuous is worse than none, because it gets cited as coverage** — in a docstring, a
commit message, a dossier and a charter bullet, all of which claimed proof this arm never delivered.

## What actually works

1. **Check the part that IS decidable, and claim only that.** Both globs must select a real tracked
   file. Narrow, true, and it fires: it caught five of the kit's own fixtures declaring a rule they
   had no files to express.
2. **OBSERVE the failing case** (companion §7). Stage the real violation, watch it red, unstage. That
   is evidence; a synthetic that the matcher's own logic generates is not.
3. **Fixture the PRODUCTION shape.** The original fixture used `import adapters.db` against
   `adapters/*` — a namespace that HAPPENS to spell the path. Production named a hyphenated directory
   reached by a bare stem, which shares no characters with its own directory. A fixture easier than
   production certifies coverage production does not have, and that single substitution is what let
   the blocker through.

Gated by `tools/lexicon/lexicon.py`, whose `scan_unselective_rules()` reds an `UNSELECTIVE LAYERS
RULE` — emptiness only, and its name says so. The GENERAL form is not gated and cannot be from one
repo: no predicate can know what "reachable" means for a rule type it has never seen. This class is
the review question to ask instead, and the question is: **what edit would make this number go up?**

## Where else this bites

Any gate whose subject is a DECLARATION rather than code: a waiver whose key can never match, a pin
over a population the selector cannot reach, a signal whose glob names a directory that does not
exist, a lint rule scoped to a path pattern nothing satisfies. The symptom is always the same and
always reassuring — a zero, reported confidently, that no change can move. Ask of every new pinned
count: *what edit would make this number go up?* If there is no answer, the number is not a
measurement.
