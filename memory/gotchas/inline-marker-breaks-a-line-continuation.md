---
name: inline-marker-breaks-a-line-continuation
description: appending a per-line annotation to the lines a gate selected breaks any of them that ended in a backslash, and the result is valid shell that silently drops the rest of the command
kind: class
universal: false
---

# A per-line marker lands after a trailing backslash, and the continuation dies quietly

## Symptom

A gate names a set of offending lines. The remedy is a per-line annotation — `gov:root-fixture`,
`gov:literal-python`, any of this repo's inline markers — appended to each one. The edit is
mechanical, the gate goes green, and `bash -n` passes on every touched file.

Some of those lines ended in a line continuation. The backslash now escapes the SPACE before the
comment rather than the newline, so the statement ends there and the following line becomes a
separate command. In a `for ... in` list the iteration set is silently truncated. In a `$(...)` the
remaining arguments become a new command. Nothing crashes, nothing warns, and the suite around it
may still pass — because the truncated branch is a fallback that a green tree never reaches.

## Why

A trailing `\` and a trailing `#` comment are mutually exclusive in shell, and there is no syntax
that carries both. The annotation tool does not know that, because it is operating on `<path>:<line>`
pairs a gate printed — a coordinate space with no grammar in it.

`bash -n` cannot help: `cmd \  # comment` is well-formed. So is the truncated loop it produces.

The mirror image of this is the same edit made through a Bash-tool heredoc, where a backslash level
is eaten and the intended `\` + newline arrives as the two characters `\n`. That produces a line that
is also valid — `git ls-files -- 'a' 'b' 2>/dev/null \n | grep …` passes `n` as a pathspec — and it
is invisible for exactly the same reason.

## Where it bit

`TOOL-cWidenedNet-1`, 2026-09-13, while marking the deliberate root-prefix fixtures the widened
install-prefix predicate had just made visible. Twenty markers were appended; three landed on
continued lines:

- `tools/check-wiring.test.sh` — the `for rel in …` dependency list, truncated to its first line.
- `tools/check-wiring.test.sh` — the AC10 launcher assertion, whose `&&` clause became a new command.
- `tools/hooks/agent-cap.test.sh` — the last-resort `git ls-files` fallback for locating the hook.

The first two were caught because `check-wiring.test.sh` went from 92 arms passing to `91 passed,
1 failed`. The third was caught by reading, not by a suite: `agent-cap.test.sh` reported
`215 passed, 0 failed` both before and after, because the fallback only fires at a prefix no fixture
builds. The repair of the first two then reintroduced the class in its heredoc form, and the gate
itself caught that by naming the same two lines as unmarked again.

## The fix

Restructure so the marked line carries no continuation, rather than trying to carry both:

- a list becomes one or more variable assignments, each a complete statement that can be marked
- a pattern or glob argument moves into a variable on its own line, and the marker goes there
- never move the marker to the line ABOVE — the predicate matches the line holding the spelling, so
  the gate simply reports it unmarked again, which is the one benign outcome of the three

Then verify the BYTES, not the parse: `sed -n '<a>,<b>p' <file> | cat -A`. A surviving continuation
shows as `\` immediately before the line end; a broken one shows the comment after it, and the
heredoc variant shows a literal `\n` mid-line.

## Arming it

There is **no machine gate** for this class today, and saying so is better than implying a check
exists. The arms that caught two of the three were the touched suites' own, which is coverage by
luck of what those fixtures happen to reach.

A gate would be cheap and narrow: over the tracked `*.sh`, refuse any line matching `\\[[:space:]]+#`
and any line containing a literal backslash-n outside a `printf`/`sed` argument. Both predicates are
near-zero-false-positive on this tree — measured at zero hits after the repair. It is not built here
because this build was closing a different class and a gate written in passing is how a predicate
lands without its failing case ever being observed.
