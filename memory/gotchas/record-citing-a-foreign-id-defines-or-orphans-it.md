---
name: record-citing-a-foreign-id-defines-or-orphans-it
description: writing another build's id into a record either DEFINES it or ORPHANS it, and the orphan count sees only one of those, so the obvious check passes on the worse half
kind: class
universal: false
---

# Citing a foreign id changes the corpus, and the count you would check with sees half of it

## Symptom

A record needs to talk about work that belongs to another build — a missing record, an unbuilt unit,
a citation that resolves to nothing. The obvious move is to name the ids. There is no spelling of
that which leaves the corpus as it was:

- **In a row's HEAD** the id is on an ANCHOR. The extractor's dash pattern matches a leading
  `- <ID> ·`, so the id lands in the DEFINITIONS set: the corpus now says that unit exists. Any
  signal whose job was to notice that it does not has just been drained by the record complaining
  about it.
- **In a row's BODY** the id is a bare citation, so it is cited-never-defined. That is an orphan, and
  where the orphan pin sits at its floor with an empty waiver the bar reds. Raising the pin instead
  trips the shrink-only ratchet.

## Where it bit

A build needed to file that three consecutive unit ids of another node's build were minted and never
recorded, two of them cited from tracked source. Both spellings were closed, so the row was written
to name the build and its seq RANGE in prose, which no grammar matches.

The same build then wrote an acceptance criterion to prove that constraint had been honoured, and
chose the orphan count. That criterion was green on the head case — the worse of the two, because a
head-anchored id is silently DEFINED and the orphan count never moves. The check passed on exactly
the violation it existed to catch, and a spec-audit round had to find it.

## The fix

Name the build and the seq range in prose. Do not spell the id, in the head or the body.

To CHECK that, do not reach for the orphan count: it observes the body case only. Enumerate the
foreign build's ids across the memory root before and after and assert the set is byte-identical —
that is what sees the head case. Use both, and say which clause catches which failure, because one
number covering two failure modes covers neither.

`tools/memory-tree/corpus_ids.py` reports the orphan count; the anchor patterns that decide
definition live in `tools/memory-recall/extract.py`.

## Related

[[amendment-leaves-its-other-half-standing]] is the shape the second half took here — the constraint
was repaired and its observation was not. [[id-matched-as-a-substring]] is the neighbouring trap
about matching these ids at all.

## Its gate

Partly gated: `tools/memory-tree/corpus_ids.py` reds on the body case through the orphan pin. The
head case has NO machine gate and is a documented check — a definition arriving is indistinguishable
from a record being written, which is what makes it invisible. This record is the check.
