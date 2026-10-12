---
name: held-suite-guard-misses-a-sibling-kit
description: a held self-test reads another kit's file, but its leg's guard names only its own kit, so an edit to the sibling skips the leg or reuses its stale green
kind: class
universal: false
---

# A held suite whose guard misses a sibling kit it reads

## Symptom

A leg in `tools/gate-legs.json` runs a suite that imports, sources or resolves a file from a SIBLING
kit — a parity arm comparing two implementations, a fixture built from another kit's engine. Its
`guard` names only the suite's own kit. An edit to the sibling alone moves the verdict the suite would
print, yet a scoped bar skips the leg, and the leg's reuse key, which hashes only the guarded paths,
carries the earlier green forward. The parity arm reads green for a check it never ran.

## Where it bit

aHeardState's `format-guard self-test` (`tools/hooks/format-guard.test.sh`) gained an AC6 arm holding
`tools/runlog/prose.py` to `tools/hooks/format-guard.js`, and its guard named only the hook files.
Closing review round 1 ids 2, 10, 14 and 25 found it from three lenses. The same shape stands in
`tools/hooks/scratch-guard.test.sh`, which resolves the run-gates kit through `resolve_kit_dir` while
its guard names none of it.

## The fix

When a suite reads a sibling kit, add the exact files it reads to that leg's guard: the module it
imports, what that module imports, and `{prefix}/lib/` when the suite inlines a resolver. Prefer exact
files to the sibling's directory, which can tip a shared guard past `BROAD_LEG_FLOOR` in
`tools/check-spec-tokens.py` and drop it out of the spec-tokens join.

Not gated: a lint that reads each held suite for the sibling kits it resolves reds scratch-guard's leg
on arrival, so it is a build of its own. Until then this record is the checklist entry, selected by
`gotchas.py --for-paths` for a diff touching `tools/gate-legs.json`.
