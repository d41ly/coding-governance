---
name: containment-tested-one-way
description: a guard asking only "is this path under the protected one" refuses the narrow declarations and admits the one that claims everything
kind: class
universal: false
---

# The widest possible input passes every "is it under" test

## Symptom

A path guard refuses the obvious violations and is green on the input that violates it most. Declaring
`memory/DECISIONS.md` is refused. Declaring `memory` — which contains it, and everything else — is
accepted, because `memory` is not *under* `memory/DECISIONS.md`.

The guard looks correct in review and its fixtures pass, because fixtures are written from the same
mental model as the code: somebody trying to sneak a write past it declares the file, and that is the
case everybody tests.

## Where it bit

`tools/unattended/unattended.sh`, `verb_dispatch`'s condition 3, found by this build's closing review:

```sh
for q in ${SHARED_RECORDS:-}; do
  case "$p" in "$q"|"$q"/*) fail 49 "…" ;; esac
done
```

`--writes memory` sailed through every refusal in the verb and licensed a pass to write every shared
record in the tree. The same file had the relation spelled by hand at four sites — one used string
equality outright, which certifies `tools/beta` and `tools/beta/one.sh` disjoint.

## The fix

Collision between paths is SYMMETRIC, and the relation gets a name:

```sh
covers()   { case "$2" in "$1"|"$1"/*) return 0 ;; esac; return 1; }
overlaps() { covers "$1" "$2" || covers "$2" "$1"; }
```

`covers` is directional and is what a "may this pass write here" question wants. `overlaps` is what
every disjointness question wants, and disjointness is what condition 3 and the sibling intersection
are both actually asking.

## How to catch it in review

For any path guard, ask what the ROOT does. If declaring `.` or the repository root passes, the
relation is backwards. The test is cheap, it takes one line in a fixture, and it is the one input
that separates a containment check from a string comparison wearing its clothes.

## Gate

Gated by construction: every path relation in `tools/unattended/unattended.sh` now calls `covers` or
`overlaps`, so the direction is decided once. The arms in `tools/unattended/unattended.test.sh` pin
both halves — `--writes memory` refused, and a genuinely disjoint sibling path still accepted, because
a refusal that fires on every input is the same nothing as one that fires on none.

The review question at the top of this record is the ungated part: for any NEW path guard, ask what
the repository root does. No predicate can ask that for you.
