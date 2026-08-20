---
name: allowlist-narrower-than-the-root-it-guards
description: a guard keyed on a path prefix denies the sanctioned destination too, because on this platform the sanctioned destination is INSIDE the prefix
kind: class
---

# An allowlist narrower than the root it guards

## Symptom

A guard is written as "deny writes under X, except Y". It looks obviously correct in review, its
self-test passes, and it then denies most of the legitimate traffic on the machine — because on this
platform Y is not beside X, it is *inside* X, and so are several other things nobody enumerated.

The tell is that the guard's own remedy message names a destination the guard itself would refuse.

## Where it bit

`tools/hooks/scratch-guard.js`, at spec rev-1, before a line of it was written.

The rule was "deny a write under `$HOME` that is not under `~/.claude`". On Windows,
`TEMP` is `C:\Users\<user>\AppData\Local\Temp` and the Claude Code session scratchpad is a subtree of
it — both under `$HOME`. `/tmp` is an MSYS `usertemp` mount onto the same place, so bash `mktemp` and
Python `tempfile` land there too. The rule therefore denied every legitimate temp write on the node,
including `export TMPDIR=…/claude/gatetmp`, which is verbatim the workaround the kickoff manifest
prescribes for a crowded temp root, and which the guard's own acceptance run depended on.

Measured over the real corpus — 93,208 historical `Bash` tool calls in `~/.claude/projects/*/*.jsonl`
— the rev-1 predicate denied 123 commands, of which **73 were legitimate**.

A second, narrower instance of the same shape survived one more round: the allowlist was then derived
from `TEMP`, but the machine hands `TEMP` 8.3-contracted (`C:\Users\DAILY-~1\...`) while commands
spell it long (`C:/Users/daily-agent/...`). One directory, two alphabets, and a prefix test sees two
unrelated paths. That cost **259 false positives** on the next corpus run.

## The fix

**Derive the allowlist from the environment at run time; never author it.** The sanctioned roots are
whatever `TMPDIR`, `TEMP` and `TMP` currently say, plus the one path that is genuinely fixed. A
derived allowlist also self-corrects when the roots move, which an authored one cannot.

**Then re-spell every root under every known spelling of the prefix it sits under**, and `realpath`
it where it exists. A prefix comparison is only as good as the alphabet both sides are written in.

**Measure over the real corpus before wiring, not over a population you chose.** Both defects above
were found by running the predicate over actual historical tool calls and printing hits *and*
near-misses. The population rev-1's acceptance criterion named — tracked `*.sh` files and gate-leg
argv vectors — was structurally incapable of containing a shell redirect at all, so it would have
reported zero hits regardless of whether the predicate was any good. That is
[[fixture-passes-by-finding-nothing]] wearing the costume of a false-positive check.

Gated by `tools/hooks/scratch-guard.test.sh` (leg `scratch-guard self-test`), which pins both halves — a DENY arm per home
spelling, and an ALLOW arm per sanctioned root in all three spellings, including the long/8.3 pair
that produced the 259. The corpus probe itself is not a gate (it reads machine-local transcripts);
its result is recorded in `memory/builds/aTetheredScratch/`.

## The general shape

Before writing "deny under X except Y", check whether Y is under X on the platform you are on, and
whether X has more than one spelling. Both questions are cheap and both were skipped here.
