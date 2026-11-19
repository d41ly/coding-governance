---
name: kit-argument-dropped-at-an-inner-call
description: a function that takes a resolution root calls a helper that resolves again from its own default root, so the caller's root is honoured at one call and silently replaced at the next
kind: class
universal: false
---

# A root honoured at the outer call and replaced at the inner one

## Symptom

A function takes a kit root, resolves a sibling kit from it, and every case it is run on passes. Run
from a copy whose root differs from the module's own, it still passes: the inner helper resolved the
same modules again from its own default root, the module's `KIT`, and found the source tree's copy,
so the caller's root was read at one call and quietly replaced at the next. Nothing reds until the
default root holds nothing, which on the source tree it never does.

## Where it bit

`memory/builds/dLandedOwners/reviews/2026-11-19-review-TOOL-dLandedOwners-1-3-closing-diff-round1.md`,
item M1: `tools/policy/check_policy.py#derive_landed_builds` loaded `tree_lib` and the run readers
from its `kit`, then called `tools/policy/check_policy.py#derive_run_kind`, which called
`load_tree_lib_or_refuse()` and `load_run_readers()` with no argument. Over gov's tree, 2 of 8
resolutions came from the given root and the rest from the module's absolute `KIT`, and the module
files were resolved and checked again once per candidate base.

## The fix

Thread the root to every call that resolves, or better, hand the callee what the caller already
loaded, so it resolves nothing of its own: `derive_run_kind` now takes `readers`, the four modules
`derive_landed_builds` loaded once from its `kit`. Then run a case where only the caller's root
resolves, so a load from any other root is a refusal rather than a silent success.

Gated by `tools/policy/check_policy.py`, the `policy fixtures` leg's `kit-root-threaded` sub-case of
`reader-coverage-carried`, which swaps the module's resolver for one refusing every root but the
kit copy's. No gate covers the class elsewhere: a helper in another kit that re-resolves from its
default root is unseen until someone writes that kit's case.

The sibling class is `grammar-bound-to-the-wrong-root`, where a module binds its root once at import;
here the root is taken as an argument and dropped one call down.
