---
name: text-mode-read-eats-a-bare-cr
description: reading a CRLF worktree file in text mode turns a bare CR inside a regex into a newline
kind: class
universal: false
---

# A bare CR is DATA, and universal newlines cannot tell it from a line ending

## Symptom

An edit script reads a tracked script, replaces one string, writes it back — and an awk or sed
program somewhere else in that file, one the edit never touched, becomes a syntax error. The
diff looks like the file grew a line break out of nowhere, in the middle of a regex.

## Why

This tree's shell and Python carry `sub(/\r$/, "")` written with a **literal CR byte** inside the
pattern rather than the two-character escape. In the committed LF blob that is one line holding one
bare CR. On Windows the worktree is smudged to CRLF, so every line ALSO ends with CR — and Python's
default text mode applies universal newlines, which translates `\r\n`, `\n` AND a lone `\r` to `\n`.

The line endings survive, because they are rewritten on the way out. The bare CR inside the regex
does not: it becomes a newline, and `sub(/` and `$/, "")` end up on separate lines.

Writing with `newline="\n"` does not save you. The damage happens on the READ.

## Where it bit

`TOOL-dHonouredPark`, closing review round 3. A one-string append to
`tools/unattended/check-unattended.sh` broke all THREE of its awk programs at once. The failure
surfaced as check 18 reporting that the Skill template names no `--preflight` invocation — a claim
about a completely different file — because the awk that reads that template no longer parsed.

Nothing had corrupted the template. The gate that read it had been corrupted by an edit to itself.

## The rule

**Edit a tracked script in BINARY mode when it may hold a bare CR.** Read bytes, replace bytes,
write bytes, and pick the line ending from the file you read rather than imposing one.

```python
with open(p, "rb") as fh: data = fh.read()
nl = b"\r\n" if data.count(b"\r\n") > data.count(b"\n") // 2 else b"\n"
```

Text mode remains fine for markdown and for any file you have confirmed holds no bare CR.

## How to detect it

The corrupted shape is a line that ENDS at an opening regex delimiter:

```bash
grep -rnE 'sub\(/$' --include='*.sh' --include='*.py' .
```

Zero hits is the healthy state. Compare against `HEAD` before assuming a hit is pre-existing — and
count bare CRs per blob rather than trusting a line count, since a CRLF worktree puts a CR on every
line and hides the one that matters:

```python
sum(1 for i, b in enumerate(d) if b == 13 and (i + 1 >= len(d) or d[i + 1] != 10))
```

## Gate

**There is no machine gate for this class yet, and that is a statement rather than an omission.** The probe above is exact and has no
near-miss population, so this class is cheaply gateable - a grep leg banning a line that ends at an
opening regex delimiter across tracked `.sh` and `.py`. Nothing runs it today. Filed as a backlog row
rather than added here, because a new bar leg carries a registry declaration and an exemption review
that do not belong in a closing fold.

Until it exists, the compensating check is the one this build actually used: after any scripted edit
to a tracked script, compare the bare-CR count of every touched blob against its parent.

## What made it cheap this time

The damage never reached a commit. The bar caught it as a wrong-file failure, and comparing that
bare-CR count between the build's base and `HEAD` across every tracked `.sh` and `.py` proved no
earlier commit in the same session had taken it — which is the check to run FIRST, because the
alternative is discovering it in an adopter's tree after the kit ships.
