---
name: criterion-asserts-what-its-own-command-cannot-show
description: an acceptance criterion names a command and then asserts a figure that command never prints, a field nothing the change moves, or a state that holds when the scope item is skipped
kind: class
universal: false
---

# The criterion names a command that cannot answer it

## Symptom

An acceptance criterion looks rigorous — it names a real command, gives a real number, reads like an
observation. It cannot fail. Three ways, and a spec set usually has more than one:

- **The command does not print that.** The criterion asserts on a per-subject set or a breakdown the
  named invocation never emits, so nobody can run it as written and the nearest printed total moves
  for unrelated reasons.
- **The field is the wrong one.** The criterion asserts on a population that nothing the unit does
  can move, where the thing that actually moves is a different field two lines away. Often a sibling
  criterion then demands the first field stay put, so the two contradict on one number.
- **It holds when the scope item is skipped.** Every clause asserts residue — what still exists —
  rather than removal, so never doing the work satisfies it.

## Where it bit

One build's spec set produced this five times across two adversarial rounds, and it was the round's
dominant class both times. A drainability proof named two annotations where five survived the unit's
own scope items, and asserted on the judgeable population, which counts specs, three lines above a
criterion demanding that same population stay non-empty. A deletion criterion asserted only that
each edited record still carried its class name, which is true if the deletion never happens. A
prose-only-citation criterion named an orphan count that structurally cannot see the failure mode it
was written for.

Every one of them was written by someone who had just read the code.

## The fix

Make the criterion DERIVE rather than ASSERT. Name the invocation that enumerates the set and have
the criterion PRINT it, instead of typing a count beside the source that owns it. Assert on the
field the command actually moves — check that by running it and changing the thing, not by reading.
And apply the skip test before the criterion lands: if every clause still holds with the scope item
deleted, it is not an acceptance criterion.

Where one criterion covers two failure modes, split it and say which clause catches which. One
number covering both covers neither.

## Related

[[fixture-passes-by-finding-nothing]] is the same defect one level down, in a test rather than in
the criterion that specifies it. [[two-answers-to-one-question]] is what the wrong-field form
becomes once a sibling criterion contradicts it.

## Its gate

No machine gate, and it is a documented check by construction: deciding whether a criterion can fail
needs the criterion's intent. `tools/check-spec-tokens.py` already walks the spec population and is
where a partial join would go — a backticked leg name or path in a criterion that resolves nowhere
is the mechanical half — but the three forms above are not reachable that way.
