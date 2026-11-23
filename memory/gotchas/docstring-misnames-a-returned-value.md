---
name: docstring-misnames-a-returned-value
description: a docstring or README names an element of a returned tuple by a value the code does not return, so a caller unpacks it under the wrong name and reads a window as a token count
kind: class
universal: false
---

# A docstring misnames a returned value

## Symptom

A function's docstring, and the README sentence copied from it, state the tuple it returns, and one
element is named for a value the code does not put there. Nothing reds, because a docstring executes
nothing and both callers already unpack the real value. A new caller that trusts the text binds the
element under the documented name and reads it as that, so a context window is read as a token count.

## Where it bit

The closing diff review of the dKeptSession build,
2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1, finding 5, item L1.
`tools/runlog/extract.py#measure_context_fill` opened its docstring with `(share, tokens, source)`
and returned `window` as the second element, and the runlog kit's README repeated the old tuple.
KICK-dKeptSession-79 S7 made both read `(share, window, source)`.

## What to do

Hold the documented tuple against the `return` statement and against each caller's unpacking, the
three side by side, whenever a function's return changes or its docstring is written. Search the
kit's README and every other text for the old spelling before closing. The nearest class is
`doc-names-an-argument-the-code-never-reads`, which is the same drift on an argument rather than on
a returned value.

## The gate

There is no machine gate: a docstring is prose, and no reader of it holds a tuple's names against
the code. A reader holds the documented tuple against the `return` and each caller's unpacking.
