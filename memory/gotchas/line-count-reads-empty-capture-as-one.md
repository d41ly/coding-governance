---
name: line-count-reads-empty-capture-as-one
description: a line count over a captured variable that adds a newline before counting reads an EMPTY capture as one line, so a one-line assertion cannot fail on a command that wrote nothing
kind: class
universal: false
---

# The line count that reads nothing as one line

## Symptom

A helper asserts that a command wrote exactly one line of stdout, and the assertion is meant to red
on the empty case too — "reds as loudly as two". It never does. The count is taken as
`printf '%s\n' "$_o" | wc -l`, or `echo "$_o" | wc -l`, or `wc -l <<< "$_o"`, and every one of those
ADDS a newline to the capture before counting. On an empty capture the newline is the whole input,
`wc -l` reads `1`, and the `same … "1"` passes for a command that wrote nothing at all. Green by
absence, one helper down: the arm exists to catch the silent verb and is the one shape that cannot
see it.

## The measurement

```
_o=""; printf '%s\n' "$_o" | wc -l     # 1  — the added newline is counted
_o=""; printf '%s'   "$_o" | grep -c ''  # 0  — nothing in, nothing counted
```

`grep -c ''` counts lines the way `wc -l` does on non-empty input, counts a final line with no
trailing newline (which `wc -l` misses), and reads `0` on empty input — the one property the helper
needs. `printf '%s' "$x" | wc -l` with no added newline reads empty as `0` too, but misses the
unterminated final line; it counts embedded newlines correctly and is the driver's own idiom, which
is why the gate below does not red it.

## The instance

`check_status_one_line` in `tools/unattended/unattended.test.sh` at spec rev-1 of
`TOOL-aWokenSentinel-17`: the driver's `--status` was asserted to write one stdout line through
`printf '%s\n' "$_o" | wc -l`, and the empty case the spec said "reds as loudly as `2`" could not
fail. Spec-audit round 3 H3, folded at rev-2 to `printf '%s' "$_o" | grep -c ''` with a third
reading against a driver copy whose status `printf` is deleted, and the class promoted to
`TOOL-aWokenSentinel-23`.

## The remedy

Count with `printf '%s' "$x" | grep -c ''`, never through a command that appends a newline first;
and give every one-line assertion a reading against a copy that writes NOTHING, because a count that
cannot distinguish empty from one is the vacuous-selector class with the number typed in.

## Gating

Gated by check 33 in `tools/unattended/check-unattended.sh`: every shell file beside the checker,
the suites INCLUDED (the instance lived in a suite helper, and the checker's `KIT_SH` population
skips the suites), minus the checker itself and `tools/unattended/check-unattended.test.sh` by name, is
grepped on code lines for the three spellings that add a newline — `printf '%s\n'`, `echo` or a
here-string into `wc -l` over a quoted variable — and any hit reds naming the file, the line and the
remedy. The arm in the kit gate's own suite stages the `printf` line into a copy of the driver suite,
assembled from fragments so the suite never carries the banned bytes on a code line; the `echo` and
here-string spellings are `TOOL-aWokenSentinel-28`'s arms over the same copy.

The class is gated over THIS kit's directory only. A suite helper under another kit is not read; the
repo-wide home would be a `CLASSES` row in `tools/gate-lint/sh_hygiene.py`, whose population is every
tracked shell file, weighed in spec 23 §4 and not taken there — so this record anchors that scanner, and a
diff touching it is shown the class. A fourth spelling of the same defect (`"${x}"` with braces, a
variable not immediately quoted) passes the gate; the class is the added newline, not the spellings.
