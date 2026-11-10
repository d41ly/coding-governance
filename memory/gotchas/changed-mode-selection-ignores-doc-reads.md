---
name: changed-mode-selection-ignores-doc-reads
description: a kit-subject leg that declares doc_reads is selected under changed mode by its kit's shipped sources alone, so a change that moves only the records it reads leaves it held
kind: class
universal: false
---

# Changed mode selects by source, not by what the leg reads

## Symptom

A leg is held off the bar as `subject = "kit"`, and `GATE_SELFTESTS=changed` is the mode meant to
run it when its work changes. `tools/run-gates/run-gates.sh` selects a held leg under that mode by
its owning kit's shipped sources plus its suite file. A leg's `doc_reads` are not an input to that
selection. A leg whose verdict turns on records, such as run-state records, guides or archives, is
therefore NOT selected by a change that moves only those records, and the run that should have
caught the drift reads green.

## Where it bit

The aShelvedLeg closing review, round 1 item 5. TOOL-aShelvedLeg-1 held the unattended kit gate,
whose `doc_reads` in `tools/unattended/kit.toml` are the memory tree's `builds/`, `guides/` and
`archive/`. A records-only change leaves it held under changed mode. TOOL-aShelvedLeg-2 stated the
skip beside the leg and in `tools/unattended/README.md`, and named the variable at `1` or the kit's
`--checks` route as the way to run it after such a change. The legs' declarations are rendered into
`tools/gate-legs.json`.

## The fix

Say the skip where the leg is declared and name the route that does run it. Adding `doc_reads` to
changed-mode selection is the mechanism fix; it changes selection for every kit-subject leg and is a
separate unit.

## Gate

There is no machine gate for this. No check over `tools/gate-legs.json` flags a kit-subject leg that
declares `doc_reads`; that arm was deferred as an ask. A reviewer holding a leg whose verdict reads
records checks that its declaration states the changed-mode skip.

## Related

- It coexists-with `held-suite-guard-misses-a-sibling-kit`: both leave a held leg unselected while
  its verdict moves, but there the missed input is a sibling kit's file outside the leg's `guard`,
  and here it is the records the leg's `doc_reads` names, which changed mode never reads.
