---
name: usage-exit-list-lags-its-function
description: a verb's usage line lists its exit codes by hand, the function behind it gains a return, and the usage line keeps the old list, so a caller reading the usage misses an exit the verb takes
kind: class
universal: false
---

# A usage line's exit list lags its function

## Symptom

A driver's usage block lists each verb's exit codes beside its form. The function behind the verb
documents its returns in its own header. A unit adds a return to the function and updates the
header, and the usage line, a separate line far above, keeps the earlier list. A caller that
branches on the usage line's codes treats the new exit as unexpected, or never tests for it.

## The instance

The `--entry-claim` usage line of `tools/unattended/unattended.sh` listed `0 claimed, 1 refused, 4
waiting, 5 a fresh slug owed`, while `run_entry_claim`'s header and body also returned 2, not
written, and 3, spent (dPlacedRequest closing review, round 2, L3). Its four returns of a variable
passed `claim.py`'s exit through with no word on which codes it could carry.

TOOL-dPlacedRequest-99 S8 wrote the header's words into the usage line, pinned each pass-through
return with a `# passes ... through: <codes>` comment, and added an arm to the unattended kit's suite:
the usage line's list equals the header's, every literal `return <n>` and every pinned code is on
it, and every `return "$<var>"` in the body carries a pinning comment.

## The fix

Write a verb's exit list once in the function's header and copy it into the usage line in the same
words, and give each return of a variable a comment naming the codes it can pass through. An arm
holds the instance; review holds the rest.

## Gating

The instance is gated for `--entry-claim` alone. The class rule across every verb belongs to the
unattended kit gate, another write set, so this record is the checklist entry, claimed by the
unattended kit's codebase-map dossier.
