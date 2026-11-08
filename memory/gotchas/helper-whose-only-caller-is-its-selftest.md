---
name: helper-whose-only-caller-is-its-selftest
description: a function lands with its selftest arms and the flag or leg that would call it never lands, so its docstring describes a live path that nothing runs and the next change assumes it is wired
kind: class
universal: false
---

# A helper whose only caller is its selftest

## Symptom

A function is green in its selftest, and its docstring speaks of what it does as if a live path
called it. Grepping for callers finds the definition, the docstrings and the selftest arms. The
selftest proves the function works and says nothing about whether anything uses it, so the next
change assumes the reader is wired when nothing calls it.

## Where it bit

The closing diff review of the dFairHearing build,
2026-11-04-review-TOOL-dFairHearing-1-40-diff-review, id 5. `tools/memory-tree/gotchas.py` gained
check_ungated and extract_gated_scope across five units, and the flag that would call them never
landed. A docstring there said the function counts a class as ungated and announces it as a note.

## The fix

Say so where the function is defined: state in each docstring that it has no caller until its flag
lands, or delete it until that unit. The docstrings here are unit TOOL-dFairHearing-44.

## Its gate

There is no machine gate: no leg reads a function's callers.
