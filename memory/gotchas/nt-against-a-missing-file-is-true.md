---
name: nt-against-a-missing-file-is-true
description: a -nt b is TRUE when b does not exist, so a has-it-changed test against a stamp nobody wrote yet reports a change on the very first call
kind: class
universal: false
---

# A comparison against nothing is not "unchanged"

## Symptom

A tool asks whether a file changed since it last looked, as `[ "$file" -nt "$stamp" ]`. On the first
call there is no stamp yet, and the test answers TRUE: the file reads as edited behind the tool's
back although nothing touched it.

## Cause

`-nt` is true when the first file exists and the second does not. That is the documented meaning in
bash and in POSIX `test`, and it is the opposite of what a "changed since" question wants when the
baseline is missing. No baseline means no claim, not "changed".

## Where it bit

The unattended driver's run log, in `tools/unattended/unattended.sh`. Its START line sets `oob=1`
when RUN.md is newer than the stamp the previous END left, so as first specced every worktree's
first call would have carried the flag. The spec's round-1 audit caught it before any code existed.

## The fix

Test the baseline's EXISTENCE first and read its absence as absence:
`[ -e "$stamp" ] && [ "$file" -nt "$stamp" ]`. The flag is then omitted on a first call, not set.

## Gate

Gated by `tools/unattended/runlog-writer.test.sh`, arm AC4: a first call with no stamp must carry no
`oob` key. The arm was staged RED by deleting the existence test.
