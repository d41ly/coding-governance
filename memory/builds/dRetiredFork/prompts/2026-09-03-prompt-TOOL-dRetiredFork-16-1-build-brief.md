# Build brief — TOOL-dRetiredFork-16

**Serves:** journal TOOL-dRetiredFork-16

## The unit's shape depends on an answer nobody has yet

F1 is a FACT-QUESTION: does `govkit apply` really preserve a target-authored gate leg? §5 says so
outright — "the documented contract is only as true as S3's measurement. If `apply` in fact
overwrites a target-authored leg, this unit's premise is false and the unit becomes a defect report
instead."

So the probe runs FIRST, and the record says what it found rather than what the code looked like.

## What reading the code suggests, and why that is not the answer

The guard is at `tools/govkit/govkit.py:4680` with its raise at `:4681-4683`, exactly as rev-2
corrected it. It fires ONLY on a name collision. A non-colliding leg is carried in `existing` and
rewritten at `:4734-4736`, so reading says it survives — silently, with no report.

Reading is not measuring. This build has already had four instrument errors, every one of them
reading in the reassuring direction, and "the code says it works" is the same class one level up.
The probe carries a LIVENESS assertion for that reason: the fixture's leg must be observable BEFORE
the run, so a run that deleted the whole manifest is distinguishable from one that preserved the leg.

## The two behaviours to record, neither of which is "declines and reports"

- non-colliding: preserved, **no report at all**
- colliding: `Refusal` raised, nearest handler is `main`'s at `:7382`, reached AFTER the write and
  stage loop at `:4300-4341` — so the verb exits 2 with the install **partially applied**

AC1b records that as the extension point's LIMIT. Whether it should be a pre-write refusal is filed,
not fixed here.

## What must NOT be built

S5 is a named refusal: no plugin loader inside `check-memory-hygiene.sh`. A kit engine that loads
project code is an engine whose behaviour the kit cannot state, and every gate it runs becomes
ungradeable. The rejected `PROJECT_CHECKS` conf key is the same loader wearing a different name — it
inverts ownership, making the kit responsible for a script it cannot read.

## Scope discipline

gov changes nothing behaviourally. The deliverable is a measured contract plus one worked example.
NicoCares' check 90 travels as EVIDENCE quoted in the record, not as a file: gov does not track that
path and §3 forbids absorbing it, because a check gov cannot fail is a check gov should not carry.

F2 ratified: a project leg gets a declared ceiling like any other, and the worked example says so —
an adopter discovering that rule from a red bar is a worse first experience than reading it.
