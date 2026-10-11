---
name: name-search-resolves-a-namesake
description: a resolver that SEARCHES for a file by name where the file's location is declared admits every file sharing the name, and its finding then blames the subject for a collision it did not cause
kind: class
universal: false
---

# A name search where the location is declared resolves a namesake

## Symptom

A checker needs the one file a subject belongs to: the index an archive was cut from, the config a
module reads, the spec a record serves. The location is DECLARED somewhere, by a layout rule or a
conf key, but the checker searches for the file by NAME instead, because a search also reaches the
places a fixed path once missed.

The search is right on the day it is written and wrong the day any other file takes the name. The
result grows from one to several, and the checker reports the subject as unresolvable. The finding
names the subject, never the namesake, so the owner of the subject gets the red for a file they did
not write, often in a folder they never look at.

The tell to hand a reviewer is one question: **is this lookup a SEARCH where the location is
declared, and what stops an unrelated file from taking the name tomorrow?**

## Where it bit

Hygiene check 10 in `tools/memory-tree/check-memory-hygiene.sh` resolved a rotated archive's live
index by basename anywhere under the memory root. That search was itself the fix for an earlier
defect: the fixed path `<memory>/<stem>.md` had missed every backlog shard. On 2026-10-09 inCMS core
rotated its decision index, and two build-folder ledgers named `DECISIONS.md` made the stem resolve
to three live indexes. Check 10 refused the rotation, and core renamed both ledgers to land. The
same search sat in `check_rotation` in `tools/memory-tree/row_grammar.py`, where a namesake left
check 24's exclusivity half ungraded.

## The fix

Resolve at the DECLARED location, then ask the tree whether that one path exists, and make "it does
not" a named finding. The declared home here is `DECISIONS.md` at the memory root or
`backlog/<FAMILY>.md`, through one function per language, and a cross-reader arm compares the two
for every declared stem (`TOOL-dHomedResolver-1`). "Several" stops being a case at all.

This instance is gated by the `homed` fixture in `tools/memory-tree/check-memory-hygiene.test.sh`
and the cross-reader and namesake arms of `row_grammar.py --selftest`. The CLASS has no machine
gate: whether a new lookup searches where a location is declared is a reviewer's question.

## What this does NOT say

- It does not say every search is wrong. Where NO location is declared, a search is the only honest
  reader, and its several-result branch is then a real finding, not a namesake.
- It does not say a fixed path is enough. A fixed path that is not the declared one is the earlier
  defect, and it misses the real file instead of finding an extra one. Resolve at the DECLARED
  location, whatever it is.
- It does not cover a declared location that is itself wrong. That is a layout defect, and the
  missing-home finding is what surfaces it.
