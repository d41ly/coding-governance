---
name: floor-left-below-the-arms-it-guards
description: a suite's assertion floor not raised when arms land leaves those arms stranded, so deleting them keeps the suite green
kind: class
universal: false
---

# The floor did not move with the arms

## Symptom

A suite compares its executed assertion count against a pinned floor with `-ge`. A unit adds arms
and does not raise the floor, so the new arms can be deleted or short-circuited and the suite stays
green: the floor still clears without them.

## The instance

`tools/run-gates/run-gates.turnstile.test.sh` kept its floor at 101 through arms 29 to 43, and
`tools/run-gates/run-gates.test.sh` kept 326 through section 11s (aPairedSlots closing review, M4).

## The remedy

Raise the floor in the pass that adds the arms, with a dated line counting them off the blocks. A
stronger form reds when the count exceeds the floor, where every arm counts on every branch.

## A row skipped on some hosts

An arm whose sibling row runs only on one platform is still counted on the hosts where it runs
everywhere. TOOL-dPlacedRequest-34's AC28 added two rows to `tools/hooks/scratch-guard.test.sh`, one
on every host and one on a MINGW, MSYS or CYGWIN host alone, and the floor counted neither; on
Windows the second row's slack absorbed the first row's deletion. TOOL-dPlacedRequest-99 S7 raised
the pin by the every-host row and named both rows on the count's comment line, the Windows-only row
left out because its skip elsewhere keeps it from running. A staged break for such a raise deletes
the every-host row with the platform switch forced off, so it reds on any host.

## Gating

No machine gate for the class: a slack-floor red moves every suite's contract, and is its own unit.
