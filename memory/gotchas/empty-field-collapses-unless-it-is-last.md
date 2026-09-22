---
name: empty-field-collapses-unless-it-is-last
description: `IFS=$'\t' read -r a b c d` collapses a run of tabs because tab is IFS whitespace, so a field that can be empty silently shifts every field after it and the branch reading them is dead
kind: class
universal: false
---

# An empty field is not a field, unless it is the last one

## Symptom

A shell reads a tab-separated record emitted by a helper:

```sh
while IFS=$'\t' read -r name budget argv state; do
  if [ "$state" = UNRESOLVED ]; then ... ; fi
```

and the `UNRESOLVED` branch never runs. Not rarely — **never**, on the only rows that can reach it.
Every other row is fine, the gate is green, and the branch has been dead since the day it was
written.

**Tab is an IFS *whitespace* character.** POSIX word splitting collapses a run of IFS whitespace into
one delimiter, so `a<TAB>b<TAB><TAB>d` yields THREE fields, not four: the empty third is gone and `d`
lands in `argv`. The one row that carries an empty field is exactly the row the branch exists for, so
the branch is unreachable on its own population and reachable on none.

It is invisible from every direction a reader looks. The emitter is correct. The record on disk is
correct. `read` returns 0. The variable that should hold the sentinel holds an empty string, which
`[ "$state" = UNRESOLVED ]` compares false without complaint under `set -u`, because it *is* set.

## The rule

**Put the field that can be empty LAST.** A trailing empty field and a missing one are the same thing
to `read` — the variable ends up empty either way — so the collapse becomes harmless instead of
shifting everything after it. If more than one field can be empty, the record needs a real
separator, not a whitespace one.

Never "fix" this by choosing a sentinel for the empty value. A sentinel is a second vocabulary every
consumer must learn, and the first consumer that forgets it reads the sentinel as data.

## What it hides, and what hides it

This class is a *masker*. While the empty field sat in the middle, a **second** defect underneath it
was undetectable: the python emitter was writing CRLF, because `print` translates newlines on
Windows. That CR landed on the LAST field, which was the state — so `state` was `ok<CR>`, which
nothing compared successfully anyway, and nothing looked wrong. Moving the state to the front to fix
the collapse moved the CR onto the argv, whose final path token then carried it into `git ls-files`,
and all 56 rows read as untracked at once.

So: **when a field-order fix turns one silent row into a loud failure of every row, suspect a second
defect that the old order was absorbing**, rather than assuming the fix was wrong. Two defects hiding
each other is the normal case in a record format nobody has ever seen fail.

## The gate

There is **no machine gate** for this class, and a general one would need to know which fields a
given format allows to be empty. What replaces it is a documented check, applied when reviewing any
diff that emits or parses a delimited record: **name the fields that can be empty, and confirm every
one of them is last.** If two can, the format is wrong.

The cheap mechanical half is testable, though, and it is what caught this one: **the branch that reads
the sentinel needs an arm.** A refusal nothing has ever seen fire is the shape this whole tree is
built to remove — see [[../../AGENTS.md]] §7 and [[suite-invalidated-by-a-commit-under-it]] for the
sibling class where the arm exists but grades the wrong tree.

## The anchors

The taken set is the three directories that hold this repo's tab-separated declarations and the shell
that parses them: `tools/run-gates/`, where it was found; `tools/govkit/`, whose `subject-pins.tsv`
is read the same way; and `tools/memory-tree/`, whose row-keyed merge driver and its replay both
split records on tabs. It is deliberately NOT `tools/`, which would select on every checker in the
tree including the many that parse nothing, and not the one file that produced it, which would make
this a citation rather than a class.
