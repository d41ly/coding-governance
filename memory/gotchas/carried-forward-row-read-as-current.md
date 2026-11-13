---
name: carried-forward-row-read-as-current
description: a reader of a store whose writer carries old rows forward takes every row as present state, so a months-old row decides today's answer
kind: class
universal: false
---

# A carried-forward row read as current state

## Symptom

A store is rewritten on every run, and its writer copies forward each row the run did not re-measure.
A reader then asks "is any row in state X" and tests the state field alone. A row written long ago,
for a subject no later run touched, still answers yes. The reader reports a present condition that
is a stale one, and nothing in its output says how old the deciding row is.

## Where it bit

aNimbleMend's red-fix lane, `tools/hooks/scratch-guard.js`, read every `fail` or `timeout` row of the
gate ledger as an open red. `tools/run-gates/run-gates.sh` carries forward each row a run did not
re-record, so a red of a held or guard-skipped leg is never cleared. The primary checkout's ledger
held nine such rows from two months earlier (PINNED, 2026-11-12), all in the legacy five-field form,
so with the lane's key at its default the write gate would have admitted a spec-less product write
that answered no current red. The closing review's round 1 found it from three lenses, as its ids 1,
7 and 22 (`memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`).

## The fix

Bound a row by its OWN run or head field before reading its state, never by the store's age or by
"the newest run". `TOOL-aNimbleMend-14` counts a ledger row as open only when it carries the current
row form, names a leg of the manifest, and its head is HEAD or an ancestor of HEAD the landed
revision does not already hold. A newest-run bound is the wrong fix: a later run that does not
measure the subject would then clear a red that still stands.

Gated by the leg `scratch-guard self-test` for the lane: its arm class "a carried-forward ledger
row never opens the lane" sits in `tools/hooks/scratch-guard.test.sh`. For any other reader of the gate ledger, or of another store
with a carry-forward writer, this record is the checklist entry: ask which field of the row says
when and where it was measured, and whether the reader tests it.
