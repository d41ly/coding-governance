---
name: msys-grep-counts-cr-on-every-line
description: on an MSYS node `grep -c $'\r'` matches every line of an LF-only file, so a CR probe reports the whole file as CRLF and a clean tree as dirty
kind: class
universal: false
---

# An MSYS `grep` sees a CR on every line of a file that has none

## Symptom

A probe that counts carriage returns — to decide whether a rendered file, a fixture or a staged
blob is CRLF — reports a count equal to the file's line count on a file `git cat-file` shows to be
LF. The probe never errors, and its number looks like evidence.

## Where it bit

`KICK-aReplayedCard-1`'s pass checked its written card and its self-test fixtures for CRLF with
`grep -c $'\r'` before committing, on node `a`, and every LF file counted every line. The MSYS
runtime strips CR at the text layer before `grep` sees a byte on this node — the same layer the
manifest's own trap about CR guards under Cygwin describes — so the ANSI-C-quoted `\r` pattern is
matched by the line terminator `grep` reconstructs, not by any byte in the file. A gate written
this way would red a clean tree, and the reflex fix, deleting the probe, would leave real CRLF
unseen.

## The fix

Count bytes, not lines, and outside the text layer:

```sh
tr -dc '\r' < "$f" | wc -c        # the number of CR bytes in the file
git diff --cached --check          # what the commit boundary already grades
```

Gated by `git diff --cached --check` at the commit boundary and by the `eol` arm of
`tools/check-wiring.sh` for the pinned `.claude/` renders; a probe of a file outside those two
populations is a documented check written the `tr` way. `skills/session-kickoff/manifest-check.test.sh`
asserts the card is LF through the byte count.
