---
name: reflowed-prompt-string-reads-as-a-deleted-stop
description: check 12 of the unattended gate greps the kickoff engine's READY prompt string as one fixed string on one physical line, so a reflow that wraps it at the house width reads as the READY stop having been deleted
kind: class
universal: false
---

# A wrapped literal is an absent literal to a fixed-string grep

## Symptom

`tools/unattended/check-unattended.sh` reports the kickoff engine's READY stop as missing after an
edit that changed no rule — the prompt sentence is still there, wrapped across two lines at 100
columns like every other sentence in the file.

## Where it bit

`KICK-aReplayedCard-3` trimmed `skills/session-kickoff/SKILL.md` to fit three clauses under its
18432 B gate and reflowed Step 5. Check 12 anchors the engine's hand-back on three literals — the
Step 5b heading, the exact READY prompt string, and the six numbered exits — and reads the prompt
string with a fixed-string grep over physical lines. Wrapped, it matched nothing, and the check
would have reported the stop deleted. Caught by grepping the three anchors before the commit, as
the brief asked; the 16040 s leg itself was not the reader that found it.

## The fix

Keep an anchored literal on one physical line however long that makes the line, or make the check
read a whitespace-squeezed view of the file, the way the spec template's §8 readers do. Gated by
check 12 itself, which is what reds; the class is the gate reading a physical line where the
document's own convention wraps.
