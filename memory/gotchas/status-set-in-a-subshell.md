---
name: status-set-in-a-subshell
description: a gate that prints FAILED from inside a pipeline sets a status the parent never sees, so it reports the violation and exits 0
kind: class
universal: false
---

# Reporting a failure and failing are two different things

## Symptom

A check finds the defect it was written for. It prints its `FAILED —` line, with the right message
and the right offender named. The leg exits 0 and the merge bar is green.

Nobody notices, because the one place a green bar is read is the summary line, and the summary line
says what the exit code says.

## Where it bit

`tools/unattended/check-unattended.sh`, check 22's orphan-successor arm, caught by this build's own
closing review. The arm was written as

```sh
printf '%s\n' "$rs_rows" | grep -oE '…' | sort -u \
| while IFS= read -r rssucc; do
    fail 22 "…"
  done
```

`fail` sets `status=1`. The `while` runs in a subshell because it is the right-hand side of a pipe,
so `status=1` is set in a process that exits immediately afterwards and the parent's `status` is
untouched. The arm had a fixture. The fixture asserted the MESSAGE, which is emitted correctly, so
it passed.

## The fix

A `for` over a command substitution, never a `| while`, in any loop whose body can `fail`:

```sh
for rssucc in $(printf '%s\n' "$rs_rows" | grep -oE '…' | sort -u); do
```

The substitution runs in a subshell; the LOOP BODY runs in the parent, which is the half that
matters. Word-splitting is safe here only because the values are id-shaped — for anything that can
carry whitespace, read into an array or use a process substitution, not a pipe.

## Why a message fixture cannot catch it

A test that greps stdout for the message is testing the `echo` inside `fail`, not the exit code. Both
halves need an arm: the text AND the status. `tools/unattended/check-unattended.test.sh` asserts the
run's exit status separately for exactly this reason, and the arm that missed this one asserted only
the text.

The general shape is [[armed-but-unreachable-rule]] seen from the other side: there, the predicate
could never match; here, the predicate matches and the verdict is thrown away.

## Gate

**No machine gate, and the attempt is worth recording.** A predicate was written and run over every
tracked `.sh` before being wired, as the charter requires: track `| while`, then look for `fail` or a
`status=1` in the body. Over this tree it produced two hits and BOTH were false positives — one
matched the prose of a comment warning against the shape, and the other ran past a loop whose `done)`
shares a line with its body and landed on an unrelated refusal forty lines later.

A predicate that reds two innocent sites out of two is not a gate, it is a tax with a false-confidence
rider. Catching this reliably needs a shell parser that knows where a compound command ends, and that
is a larger tool than the class justifies today. So: a documented check, run by eye at review time,
and this record is the thing that makes it a check rather than a hope.
