---
name: off-switch-leaves-new-output-standing
description: a mechanism ships behind a key, and with the key off some of its parts still print new lines and still grade, while the page that documents the switch lists only the parts the key stops
kind: class
universal: false
---

# An off switch that leaves new output standing

## Symptom

A mechanism lands behind a policy key, and its brief says the earlier behaviour holds with the key
off. Some of its parts are deliberately independent of the key, because they grade history and
not the act the key gates. With the key off they still print their lines on every run and can still
red. The help page's switch section describes what the key stops and is silent on what it leaves.
An adopter who turns the key off sees new output and new findings no document accounts for.

## Where it bit

aNimbleMend's red-fix lane. With `bar.inline-red-fixes` off, the commit grader still printed one
limits line per graded population on every run, still graded every commit carrying the trailer
against the limits, and the red-fix join still ran. Two specs had chosen that on purpose. The switch
section of `help/red-fix-lane.md` described the write gate and the pushed range alone. The closing
review's round 1 found it as L4
(`memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`).

## The fix

A help page's switch section lists everything that still runs with the key off: each part, the
line it prints, and whether it can red. `TOOL-aNimbleMend-15` added that paragraph to the page.
Suppressing the output instead is the wrong fix where a spec requires the line.

No machine gate: no check joins a key's readers to a page's switch section. This record is the
checklist entry, selected by `gotchas.py --for-paths` for a diff touching that page, and a reviewer
of any unit that adds a key asks which of its parts never read it.
