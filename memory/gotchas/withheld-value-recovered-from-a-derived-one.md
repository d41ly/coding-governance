---
name: withheld-value-recovered-from-a-derived-one
description: a schema withholds a value by name and still publishes one derived from it, so a reader recovers the withheld value from the rendered one by arithmetic
kind: class
universal: false
---

# The withheld value comes back through a value derived from it

## Symptom

A closed schema keeps a value out: an owner turn's clock time, say, reduced to a count per position.
The renderer drops every row of that kind, and the schema leg refuses any record carrying one. Both
checks look at the value itself. Neither looks at what was computed FROM it.

A derived value that took the withheld one as an input can give it back: a gap's start, a duration,
the end a start plus a duration implies, a window edge, the time an anomaly fired. When the withheld
event is an endpoint of that computation, the rendered number IS the withheld number, or is it plus a
figure the record also prints. When the withheld event only CAUSED the endpoint, as an owner's turn
causes the reply that follows it seconds later, the rendered number places it to within that latency.

The tell to hand a reviewer is one question: **which rendered values took a withheld value as an
input, and does any of them, alone or summed with another rendered value, land on it?**

## Where it bit

The closing diff review of build `dLoggedFlight`, round 1, confirmed it as that build's one BLOCKER.
The run model computed idle gaps over a timeline that still held the run's in-window owner turns, and
the committed record rendered each gap's start and its duration. An owner turn opening a gap was the
idle row's UTC to the second, and one closing a gap was that UTC plus the duration. The renderer
dropped every owner row, so the only rendered gap endpoint with no row beside it was an owner turn.
The kit README accepted the closing case as residue, a narrowing of the spec's explicit decision
that no owner turn carries a clock time, written during the build and read by no audit round.

Dropping the owner turns from the gap sequence was not the whole fix. The owner's reply lands
seconds after the turn, so a gap then ended on the reply and placed the turn to within the reply's
latency: the causal form of the same class.

The same build's closing review, round 2, reproduced the blocker through a third door, R2-B1: **a
cache preferred over its source, with its freshness key never read.** A session's store extract is
derived from its transcript, and `tools/runlog/model.py` read the extract first. An extract cut
before the run's last owner turn withheld that turn from the owner count, and the idle guard,
reading the same stale turns, let a gap end beside a turn it could not see. The guard shared its
input with the defect it guarded. `TOOL-dLoggedFlight-14` reads a local transcript before its
extract, and `TOOL-dLoggedFlight-16` grades an extract by its `extracted_at` where no transcript
is local.

## The fix

Three parts, and the first is the one that holds.

- **Keep the derivation away from the withheld value.** `tools/runlog/model.py` builds the gap
  sequence from no owner turn, and keeps out, and counts, any gap with an owner turn inside it or
  within one idle threshold of either end.
- **Grade the rendered TEXT, not the inputs.** `tools/runlog/record.py` refuses the whole record
  when any UTC it would write, or any idle row's start plus its duration, or the second after that
  sum, falls in an owner turn's second. It reads the text the render produced, not the model's gaps,
  so a model that regressed is still caught. The second-after comparison matters: a start and a
  duration each truncated to the second can put their sum a second BEFORE the true end, which an
  equality test misses.
- **Strike the residue.** A README line accepting half the leak is not a disclosure. It is an
  unratified amendment to the spec.

Gated by the runlog kit's self-test, whose idle arms build their session from a transcript through
the real extractor, so an owner turn is followed by its reply the way the harness writes one. Each
part above was seen RED with its own break staged.

## What this does NOT say

It does not say every derived value must be withheld. Commit times are public through git whatever
the record says, and a coincidence between one and an owner turn's second is refused only because
the text check cannot tell a coincidence from a derivation. The class is about values the withheld
one FLOWS INTO. Enumerate those, not every number that happens to be close.
