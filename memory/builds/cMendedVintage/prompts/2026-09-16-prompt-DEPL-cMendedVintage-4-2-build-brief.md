# Build brief — DEPL-cMendedVintage-4

**Serves:** journal DEPL-cMendedVintage-4

This unit retires `--allow-ungraded` and repoints the two remedy strings that name a command which
does nothing. Read the spec whole first.

## Why the remedy strings are the point

`update` tells an operator holding `unattributed` rows to run `govkit adopt --re-adopt --write`.
That re-runs the identical `derive_attribution` walk over identical bytes and returns `None` again,
so the operator runs it, nothing changes, and the remedy has closed a loop on them. The form that
works is `--re-adopt --pin <path>=<rev>`, because `--pin` is what sets `evidence = "pinned"`.

`--allow-ungraded` goes with it because its only reader advances the base away from rows nothing
graded. It writes no bytes and buys nothing but a worse receipt.

## THE TRAP IN THIS UNIT'S OWN ACCEPTANCE — read this before you trust AC3

AC3 is `grep -c 'allow_ungraded' tools/govkit/govkit.py` returns 0. **That predicate is known to be
too weak, and the spec audit already confirmed it**: it cannot see six of the fourteen live
occurrences, including the one AC3's own Red-when calls the likeliest miss, because the flag appears
under more than one spelling — the underscore identifier, the hyphenated CLI form, the argv string,
and prose.

That finding was PROMOTED to `DEPL-cMendedVintage-20`, which is sequenced after this unit and owns
making the grading complete under every spelling. It is NOT folded into this spec, so AC3 still
reads as written.

The consequence for you is direct: **AC3 going green does not mean you finished.** Enumerate the
spellings yourself and delete them all — search for the hyphenated form, the underscore form, the
argv literal and the prose independently, and report the count you actually removed. If you leave
six behind, AC3 will still pass and the incompleteness will surface later as somebody else's unit.

Do not "fix" AC3 here. Strengthening the predicate is `DEPL-cMendedVintage-20`'s mechanism and
taking it would leave that unit with nothing to close.

## The docs half is DERIVED, not pinned

The spec deliberately does not name which markdown files mention the flag. Derive it at build time
with a repo-wide grep over `*.md` and act on what you find — a pinned list would be stale and this
one was left derived on purpose.

## Bounds

`USAGE` and the remedy text are operator-facing strings and both must move together; a repointed
remedy with a stale `USAGE` is two answers to one question. Do not touch `--pin`'s own
implementation — it already does what the new remedy names.

## Traps the landed units measured, carried forward

A fixture can stage a condition the tool does not actually refuse, so confirm the RED is the red you
meant rather than a non-zero exit from somewhere else. A first cut can be vacuously green when the
artifact it inspects is absent, so assert the artifact exists before asserting anything about its
contents. And every `govkit.py:<line>` citation in this spec has drifted — four units have landed in
that file since it was written — so search for the text instead.
