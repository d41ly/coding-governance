---
name: liveness-negative-from-another-population
description: a probe is shown able to read negative on inputs it will never act on, while over its real population a positive is structural, so the liveness assertion passes and certifies nothing
kind: class
universal: false
---

# The liveness negative came from another population

## Symptom

A probe gets a liveness assertion, and the assertion passes: fed a known negative, the probe reads
OFF. The probe then reads ON for every member of the population it was built for, and that is taken
as a finding. But the known negative was not a member of that population. Over the real population
the positive is STRUCTURAL: the way the members are produced makes the probe read ON whatever the
truth is. The assertion proves that the probe can say no. It does not prove that it can say no to
anything it will ever be asked.

## Where it bit

`dUnstuckLanding`'s census asked whether each ABORTED run record's `witness` is an ancestor of the
remote default tip, and read ON for all 30. Liveness was shown on two LANDING stamps known to be
unmerged, and both read OFF.

- **Why the positive was structural.** `verb_abort` in `tools/unattended/unattended.sh` writes the
  witness as HEAD of the tree that runs it, and the record's own commit sits on top. So every
  ABORTED record that reached the tip has its witness on the tip, whether or not the run's work ever
  landed.
- **The worse shapes it hid.** A witness equal to the run's base is on every later tip. A witness
  from another tree is foreign work.
- **Who caught it.** The closing diff review, round 1, finding H1. That was after the census had
  stated the probe "separates landed from not-landed", and after a design and two asks had been
  built on it. One of those asks would have shipped a drift signal, in
  `tools/drift-audit/drift_report.py`, whose liveness assertion could not fail over its real input.

## The fix

- **Draw the negative from the population.** Construct a member of the population the probe acts
  on that should read OFF, and confirm that it does. For the witness, those members are a record
  whose witness equals its base, a record whose witness is foreign, and work that merged and was
  then reverted.
- **When none can be built, say so.** If no member can be constructed that should read OFF, the
  probe is structural over that population and measures something else. Name what it measures.
  Here, that was "the record reached the default branch".
- **Ask how the members are produced.** Before trusting a universal positive, ask what produces the
  members and whether that process FORCES the property. A 30-of-30 result is a reason to look for
  the mechanism, not a finding.

No machine gate: whether an input belongs to the probe's population is a judgement about meaning.
The nearest class is `fixture-passes-by-finding-nothing`, which is the opposite fault: there the
fixture never triggers the rule, and here the rule can fire but was never aimed at the right thing.

## What this does NOT say

It does not say liveness assertions are worthless. Feeding a probe a known negative is still the
cheapest guard against a dead probe. The claim is narrower: the negative proves liveness only for
the population it was drawn from.
