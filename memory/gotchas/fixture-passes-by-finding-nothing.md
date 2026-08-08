---
name: fixture-passes-by-finding-nothing
description: a test arm whose fixture never triggers the rule passes, and proves nothing
kind: class
universal: true
---

# An arm satisfied by a fixture that does not exercise it

## Symptom

A red arm is green. Not because the rule fires, but because the fixture never produced the condition
the rule looks for, and the assertion was phrased so that absence satisfies it.

## Where it bit

The orphan-id arm in `tools/memory-tree/corpus_ids.py`. Its fixture put the orphan id in a backlog
row — but a dash-led id row IS an anchor, so the row DEFINED the id and the corpus had no orphan at
all. The arm asserted a message that never appeared, for a reason unrelated to the rule. Upstream
counted six probes across one session that reported success while exercising nothing.

## The fix

Every arm asserts the SPECIFIC message its branch emits, never a process exit code, and the fixture
is checked against the classifier before the arm is trusted — a report mode exists partly for this.

No machine gate: this is a review discipline, not a source-level pattern. The nearest mechanical
protection is that every arm names a branch message, so an arm whose fixture stops working fails
instead of passing.
