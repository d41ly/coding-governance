---
name: swallowed-delegate-reads-as-clean
description: a gate that discards its delegate's exit status reads a delegate that never ran as a clean population
kind: class
universal: false
---

# A delegate that could not answer looks exactly like a corpus with nothing to report

## Symptom

A check hands its parse to a sibling program, captures the output, and selects findings from it by
row shape. The capture carries `2>/dev/null || true`. When the delegate fails, the capture is empty,
every selection over it is empty, and every branch prints nothing, which is what a pass prints.
The population guard beside it stays green too, because it measures the SELECTOR's input and never
the delegate's output.

## Where it bit

`tools/memory-tree/check-memory-hygiene.sh` check 21, which reads `gen_build_index.py
--print-bindings`. An adopter carried a forked generator that never gained the mode: exit 2, a usage
line on stderr, and four population branches that could not fire on any of its 1531 records for as
long as the fork stood. The one branch that still fired was the one that does not read the parse,
so the check even looked partly alive.

## The fix

A delegate's exit status is part of its answer, and so is a row it always prints. The check fails
on a non-zero exit, and on a zero exit with no `N` row, since that is a delegate that did nothing:
an unknown flag some other generator reads as its default. It prints the delegate's last lines, so
the refusal names the cause.

`vacuous-selector-empty-population` is the sibling. There the SELECTOR matches nothing; here it
matches everything and the classifier behind it is what answered nothing. A guard written for one
does not see the other.

Gated by `tools/memory-tree/check-memory-hygiene.sh` check 21's parse-refusal branch, armed in
`tools/memory-tree/check-memory-hygiene.test.sh` by two stub generators and a green control.
