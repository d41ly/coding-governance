---
name: a-folded-field-leaves-its-row-shape-docs-behind
description: a review fold adds a key to a declared row shape in the code and its gate, and the spec body and the README that describe that shape keep the old key set
kind: class
universal: false
---

# A folded field leaves its row-shape docs behind

## Symptom

A closing-review fold adds a key to a declared table shape, wires its reader and its grading, and
records the change in the spec's revision log. The spec's own scope, design and data-model sections
still describe the old key set, and the README a reader would use to write a row never mentions the
key. The revision log says what changed; nothing a row author reads says what the shape now is.

## Cause

A fold is written against the finding, and the finding names the code. The revision-log line is the
one part of the spec a fold is required to touch, so it is touched and the body is not. No gate reads
a spec body or a README for the keys a reader accepts.

## Where it bit

aWindowedPass, closing review round 1: the `[[generated]]` row in `tools/memory-tree/kit.toml` gained
`when`, read by `tools/unattended/lib-unattended.sh` and graded by `tools/govkit/govkit.py` 6c, while
spec 4's S1, S5 and design section still listed three keys and `tools/unattended/README.md` described
no row at all. Round 2 found it (its M10).

## The fix

When a fold adds, removes or reshapes a key of a declared row, update in the SAME commit the owning
spec's scope and design sections, not only its revision log, and the README section that teaches the
shape. If no README teaches it, write that section: a shape documented only in a reader's comment is
documented for nobody who writes rows.

## Gate

Not gated: no reader compares a spec body or a README to the keys a parser accepts. This is a
documented check of the Tier-2 review checklist, selected by `gotchas.py --for-diff` whenever a diff
touches the files above.
