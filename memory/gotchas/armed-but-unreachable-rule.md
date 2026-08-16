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

## The check

**Prove reachability by CONSTRUCTION, not by observation.** For each declared rule, synthesise the
thing that would violate it — from real corpus members, in the real shape a real author would write —
and require the predicate to flag it. A rule that survives its own synthetic violation will never see
a real one.

```python
# tools/lexicon/lexicon.py — scan_unmatchable_rules()
for t in targets:                       # real tracked files on the TO side
    for synthetic in (stem, dotted, "./" + t):   # the shapes a real importer writes
        if check_layer_violation(probe_src, synthetic, [(frm, to)], index):
            reachable = True
```

And **fixture the production shape**, not a convenient one: if the real declaration names a
hyphenated directory reached by a flat stem import, the fixture must too.

Gated by `tools/lexicon/lexicon.py`, whose `scan_unmatchable_rules()` reds an `UNMATCHABLE LAYERS
RULE`, and armed in `tools/lexicon/selftest.py` by two arms — one where the rule's globs select
nothing, and one reproducing the production shape that shipped the original defect. The GENERAL form
is not gated and cannot be from one repo: no predicate can know what "reachable" means for a rule
type it has never seen. This class is the review question to ask instead.

## Where else this bites

Any gate whose subject is a DECLARATION rather than code: a waiver whose key can never match, a pin
over a population the selector cannot reach, a signal whose glob names a directory that does not
exist, a lint rule scoped to a path pattern nothing satisfies. The symptom is always the same and
always reassuring — a zero, reported confidently, that no change can move. Ask of every new pinned
count: *what edit would make this number go up?* If there is no answer, the number is not a
measurement.
