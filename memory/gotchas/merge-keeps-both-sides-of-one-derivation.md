---
name: merge-keeps-both-sides-of-one-derivation
description: a conflict-free merge leaves two derivations of one value, disagreeing, and the first is a dead store
kind: class
universal: false
---

# Two answers to one question, delivered by a merge nobody had to resolve

## Symptom

A file derives one value twice, a few lines apart, with different conventions — one appends a
trailing separator, the other does not. Nothing is wrong today because the single live consumer
happens to read the second one and supplies its own separator. The comment sitting above the dead
derivation condemns exactly the state the file is now in.

## Why

Two branches fix the same defect in the same file in different places. Git finds no textual
conflict, because the hunks do not overlap, so the merge is CLEAN and both survive. A conflict you
must resolve is visible; a conflict-free merge that keeps both sides is not.

This is the "auto-took" class the charter's landing rule names, and it is why that rule says to diff
a merge against BOTH parents rather than reading the result on its own. Reading the merged file
looks fine: each derivation is individually correct.

## Where it bit

`tools/process-monitor/adopt-process-monitor.sh`, cMendedVintage closing review round 3, L1. One
side derived `TOOL_ROOT` and appended a trailing slash; the other derived it without one. Both
landed. `grep -c '^TOOL_ROOT='` returned 1 at each parent and 2 at the merge — which is the whole
detection method. Nothing between them read the value, so the first was a pure dead store, and any
line later inserted between the two would have read a different value from anything after. With
`TOOL_ROOT="tools"` the slash-less form renders `toolssettings-merge.py`.

## The rule

**After a merge, count the assignments of every name either side touched.** A name assigned twice
at column 0 with no read between is the shape. Diff the merge against both parents, never against
one.

```bash
git diff --name-only <parentA> <merge> | while read -r f; do
  a=$(git show "<parentA>:$f" 2>/dev/null | grep -cE '^[A-Za-z_]+=')
  m=$(grep -cE '^[A-Za-z_]+=' "$f")
  [ "$m" -gt "$a" ] && echo "$f grew $((m - a)) top-level assignment(s)"
done
```

## Gate

**There is no machine gate for this class, and that is a decision rather than an omission.** A
static dead-store rule for shell is more machinery than the class earns,
and the narrow derivable version — an awk pass flagging one name assigned twice at column 0 with no
read between — should be run over the whole tree to see what it reds before anyone wires it. Until
then this record is the check: it prints into the bug-class checklist of every reconcile through
`python tools/memory-tree/gotchas.py --for-diff <base>..<head>`.
