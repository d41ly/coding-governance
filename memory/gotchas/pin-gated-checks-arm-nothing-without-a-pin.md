---
name: pin-gated-checks-arm-nothing-without-a-pin
description: hygiene checks 13-15 alone are behind a declared pin, so a fixture conf without one arms nothing there and the checks report clean by never loading
kind: class
---

# Checks 13-15 alone are pin-gated; a fixture without a pin arms nothing there

## Symptom

A self-test fixture writes a minimal `.memory-tree.conf` — root, disciplines, families — and runs
the hygiene engine expecting the orphan-id or dead-path arm to fire. It does not. Nothing failed
and nothing skipped visibly: the classifier's `armed()` read no `DEAD_PATH_PIN` and no
`ORPHAN_ID_PIN`, so checks 13-15 stayed off and the id grammar was never loaded.

## Where it bit

The kickoff manifest carried this trap for a while as "checks 13-19 are pin-gated", which was
FALSE above 15: 16 is structural and behind no pin, and 17-19 are `tools/memory-tree/gotchas.py`'s
and pinned by nothing either. `tools/memory-tree/corpus_ids.py`'s own selftest carries the arm
that `armed()` is False on a conf with no pin and that 13-15 stay off — the range the manifest
misstated was already measured there.

## The fix

Set a pin in the fixture — `ORPHAN_ID_PIN="0"` and `DEAD_PATH_PIN="0"` are legal when every id and
path resolves — and read `tools/memory-tree/check-memory-hygiene.sh`'s own comment above the
delegation for which checks are behind which key. Which is: 13-15 behind the two pins, 16 behind
none, 17-19 behind none.

Gated by `tools/memory-tree/check-memory-hygiene.test.sh`, whose fixtures set both pins for the
reason above, and by the classifier selftest's `armed()`-is-False arm; the wrong-range claim was a
documentation defect and is fixed by this record replacing it.
