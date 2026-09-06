---
name: naming-leg-grades-what-python-named
description: the naming gate grades nested helpers and dunder methods, and its armed set follows symbols.json, so a new file reds on a later unrelated commit and only at the lander
kind: class
---

# The naming leg grades more surface than it looks like it does

## Symptom

`lexicon naming predicates` reds one offender over its pin, on a name you did not think was a
declaration — or on a commit that touched nothing in the offending file.

## Three separate ways it happens, all measured in one build

**A NESTED helper counts.** `def got(target, importer=...)` inside a test function is a definition
like any other. `got` leads with no declared verb and took the count 467 → 468.

**A DUNDER counts.** A small proxy class written for a test arm carried `__getattr__`, and the leg
graded it: the table has no row for a name Python chose, and there is no reason it should. The
cheaper repair is to stop needing the proxy — swap the ONE attribute under test on the real module
and restore it in `finally` — rather than to argue with the table.

**ARMING FOLLOWS `symbols.json`.** A new `.py` under an armed kit directory is NOT graded until
`gen_map.py --write` puts its symbols in the map. So the leg is green on the commit that ADDS the
file and reds on a later, unrelated commit that regenerates the map — which reads as a regression in
whatever that commit touched.

## And it only reds at the lander

A branch bar skips the leg as unchanged-vs-main, so none of the above surfaces until the push
boundary, where the full bar runs. Two of the three instances above were found that way.

## What to do

`python3 tools/lexicon/lexicon.py --suggest <name>` BEFORE writing the name; it prints the declared
verb table and answers for one identifier. Run `python tools/lexicon/lexicon.py` directly after
adding any `.py` and again after the next `gen_map.py --write`, rather than trusting a green branch
bar. Never raise the pin to admit a name you control: a conforming name exists, and the table's
value is the scoping question it forces, not the spelling.

## The gate

GATED BY `lexicon naming predicates` (`python tools/lexicon/lexicon.py`); every instance here is it
doing its job. What has NO gate is the arrival TIMING — a branch bar skips the leg as
unchanged-vs-main, and arming follows `symbols.json`, so nothing surfaces either fact before the
lander. There is NO MACHINE GATE for the timing: making the leg run on a branch that adds a `.py` would
close it, and that is a unit nobody has specced.
