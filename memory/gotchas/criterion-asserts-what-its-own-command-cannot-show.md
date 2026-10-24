---
name: criterion-asserts-what-its-own-command-cannot-show
description: an acceptance criterion names a command and then asserts a figure that command never prints, a field nothing the change moves, a state that holds when the scope item is skipped, an absence its own records break by quoting the pattern, or an input respelled shorter to pass a join so it no longer probes what its scope item names
kind: class
universal: false
---

# The criterion names a command that cannot answer it

## Symptom

An acceptance criterion looks rigorous — it names a real command, gives a real number, reads like an
observation. It cannot fail, or cannot pass. Five ways, and a spec set usually has more than one:

- **The command does not print that.** The criterion asserts on a per-subject set or a breakdown the
  named invocation never emits, so nobody can run it as written and the nearest printed total moves
  for unrelated reasons.
- **The field is the wrong one.** The criterion asserts on a population that nothing the unit does
  can move, where the thing that actually moves is a different field two lines away. Often a sibling
  criterion then demands the first field stay put, so the two contradict on one number.
- **It holds when the scope item is skipped.** Every clause asserts residue — what still exists —
  rather than removal, so never doing the work satisfies it.
- **Its own records answer it.** A "prints nothing" search with no pathspec spans the spec and the
  ledger that quote its pattern, so it never holds for a correct build, and read loosely it also
  misses a real carrier.
- **The input was respelled to pass a join.** A criterion's literal argument — a fixture path, a
  Python literal, a sourced file — was shortened so a join over the spec would pass, and the
  shortened literal no longer probes what its scope item names: the path a bare basename stands for
  is not the path the command reads, so the criterion fails on a correct build or passes on nothing.

## Where it bit

One build's spec set produced this five times across two adversarial rounds, and it was the round's
dominant class both times. A drainability proof named two annotations where five survived the unit's
own scope items, and asserted on the judgeable population, which counts specs, three lines above a
criterion demanding that same population stay non-empty. A deletion criterion asserted only that
each edited record still carried its class name, which is true if the deletion never happens. A
prose-only-citation criterion named an orphan count that structurally cannot see the failure mode it
was written for.

Every one of them was written by someone who had just read the code.

A later build's closing review found two more, review items L5 and L6. `TOOL-aOrientedCast-21` AC2
said a line with its run field cut blocks on the charter shape, and the command does not print
that: a line with the field cut whole names no agent and gets the missing-line message instead, and
the deviation lived only in a commit trailer. `TOOL-aOrientedCast-22` AC6 said a search for the old
version marker prints nothing, and its own spec answered the search, since the spec and its ledger
quote the pattern.

One leg keeps being cited for this: `tools/check-testsuite-counts.sh` asserts a suite's SHAPE and
never a count. It runs nothing, and it only reads that a `PASS ($n assertions)` echo, a non-zero
`FLOOR_ASSERTIONS` pin and a reference to that pin exist. A criterion that names it as the witness
that a floor ROSE therefore cannot go red. Observe the suite itself instead: its printed count at
the bar that runs it, and a static count of its arm calls against the pin. It was recorded against
this leg in TOOL-aLoosenedCeiling-1's review (finding 5), TOOL-aJoinedCanon-1's spec audit round 2
(H7), and TOOL-dDerivedDocket-37's G6 spec audit round 1 (H1).

The respelled input bit dGroundRules twice. Finding 37 of its round-4 spec audit named two criteria
whose candidate paths had lost their prefixes, and the unit promoted to close that corruption,
`TOOL-dGroundRules-34`, was itself committed corrupted: commit `b9f7b5c4e` records in its own
trailer that fourteen criterion paths were respelled as basenames before the first commit, because
the paths join of `tools/check-spec-tokens.py` reds a backticked path `git ls-files` cannot resolve.
Its AC11, AC12, AC15, AC16 and AC32 could then never pass — a sourced library by bare name, a
Python literal that no longer parsed, a candidate list missing the depth it named — which the
round-5 audit of units 33 and 34 confirmed as its H3. The join itself is the open ask
`TOOL-aKeyedAnnotation-9`.

## The fix

Make the criterion DERIVE rather than ASSERT. Name the invocation that enumerates the set and have
the criterion PRINT it, instead of typing a count beside the source that owns it. Assert on the
field the command actually moves — check that by running it and changing the thing, not by reading.
And apply the skip test before the criterion lands: if every clause still holds with the scope item
deleted, it is not an acceptance criterion.

Where one criterion covers two failure modes, split it and say which clause catches which. One
number covering both covers neither.

A "prints nothing" search carries a pathspec that leaves out the records quoting its pattern, and a
liveness twin, the same search for the current value, that must list the carriers: a pathspec that
excluded everything would print nothing for both. And a criterion found wrong at build time is
amended where its spec allows, never only in a commit trailer.

A literal is never shortened to satisfy a join. A criterion's argument the paths join of
`tools/check-spec-tokens.py` cannot resolve — a fixture path, a path that does not exist yet, a
Python literal — is spelled whole in a fenced block of the acceptance section of the spec under
`memory/builds/`, outside every criterion bullet, and the criterion names that block. The house rule
of citing a kit file by its basename covers prose only, never a command's argument.

## Related

[[fixture-passes-by-finding-nothing]] is the same defect one level down, in a test rather than in
the criterion that specifies it. [[two-answers-to-one-question]] is what the wrong-field form
becomes once a sibling criterion contradicts it.

## Its gate

No machine gate, and it is a documented check by construction: deciding whether a criterion can fail
needs the criterion's intent. `tools/check-spec-tokens.py` already walks the spec population and is
where a partial join would go — a backticked leg name or path in a criterion that resolves nowhere
is the mechanical half — but the forms above are not reachable that way.

No lint ships for the respelled input either, and the reason is measured. A missing-prefix
predicate over the live specs — a scope-item path ending in `/` plus a criterion token that path
would end in, with the path itself absent from the criterion — gave 136 hits across 30 specs on
2026-10-23, nearly all the house basename style, so it cannot tell a respelled literal from a kit
file named by basename.
