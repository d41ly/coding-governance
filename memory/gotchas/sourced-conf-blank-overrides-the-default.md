---
name: sourced-conf-blank-overrides-the-default
description: an engine that presets its keys and then SOURCES the conf over them lets a blank line override a default with blank, and blank is what every measured pin uses to mean skip
kind: class
---

# A sourced conf overrides a preset with BLANK, and blank means skip

## Symptom

`tools/memory-tree/check-memory-hygiene.sh` pre-sets every conf key it reads — `set -u` safety for
an adopter whose `.memory-tree.conf` predates the key — and then sources the conf OVER those
presets. A key written blank in the conf therefore wins over the preset with the empty string.
For a measured pin that is the intended language: blank means "this rule is off". For a key that
SELECTS between two behaviours it is a silent third state — an empty date compares earlier than
every date, so a blank `SPEC10_CUTOFF` would demand the ten-section canon of every grandfathered
spec in the tree, which is the one outcome the cutoff exists to prevent.

## Where it bit

`SPEC10_CUTOFF`, `TOOL-aDeclaredBound-2`. The fix is the seam every later selecting key copies:
capture the shipped value BEFORE the source (`_SPEC10_SHIPPED`), source the conf, then
`: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"` so blank resolves FORWARD to the shipped value and never
to off. Its rule-shaped siblings deliberately do NOT resolve forward, because for them blank IS the
declared off state, and the engine's own comments above the presets say which is which.

## The fix

Decide per key whether blank is a legal value or a missing one, and write it down beside the
preset. A key that must not be skippable is captured before the source and restored after; a key
that may be off is guarded with an explicit `!= ""` test at its use site. Never rely on the preset
surviving the source — it does not, and that is the point of the source.

Gated by `tools/memory-tree/check-memory-hygiene.test.sh` for the `SPEC10_CUTOFF` seam; a new
selecting key that skips the capture has no gate but the engine's comment, which is why this is a
class and not a closed bug.
