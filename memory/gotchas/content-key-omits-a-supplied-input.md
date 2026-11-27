---
name: content-key-omits-a-supplied-input
description: a write door's content key hashes only part of what the caller supplies, so a call differing in an input the key leaves out answers `exists` and its record is dropped with exit 0
kind: class
universal: false
---

# The key leaves out an input, so a different record reads as the same write

## Symptom

A door makes a replay a no-op by a content key. The key is derived from some of the call's inputs, and a
second call that differs in one of the others derives the same key. The door answers `exists`, exit 0,
before the refusal that guards a different value under an existing id. The caller is told its record is
written, and nothing of it was.

## Where it bit

The dTotalRecall closing review of 2026-11-25
(`memory/builds/dTotalRecall/reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md`, H3).
The record door's key held the kind, the stem and the bullet fields. The unit, the title, an untyped record's
cause, the edge lines and the build were outside it, so a kind whose row names no field was keyed by its name
alone. The table of the spec `TOOL-dTotalRecall-2` promises exit 2 for a different value under an existing id.
One of the omissions was disclosed under the door's `WHAT IT DOES NOT CHECK`, which no reader of `exists` sees.

## The fix

- Derive the key from everything a caller supplies, and name what stays out: who minted the record, the date
  and the minted number.
- Read both sides through one reader of the record's bytes, `read_key_fields` of
  `tools/memory-tree/build_records.py`, so the compare cannot be two derivations. A record the reader refuses
  has no key and is never the same write.
- Write one refusal arm per input, each the replayed call with that one input changed.

## Gated by

`tools/memory-tree/check-memory-hygiene.test.sh`, which runs the `door-header` plant of
`tools/memory-tree/build_records.py` and asserts its case count: the replay answers `exists`, and one case each
for the unit, the title, the cause, the edge, no edge, the build and a typed pair never does. A new flag of the
door owes a case; nothing reds a flag without one.

## What this does NOT say

- It coexists-with `append-without-an-idempotence-key`: there a row has no key, or one shared by two events that
  repeat; here the key is declared and too narrow for what the call says.
