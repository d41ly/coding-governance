---
name: heredoc-escape-reaches-the-regex
description: source written through a shell heredoc into a non-raw string turns an escape into a control byte, and the symptom never looks like a quoting problem
kind: class
universal: true
---

# A backspace where a word boundary was meant

## Symptom

A regex silently matches nothing, or matches without its boundaries. The pattern PRINTS correctly —
a terminal renders the control byte as nothing at all — and `repr()` is the only thing that shows it.
Three instances in one session, each with a different and entirely misleading symptom:

| Where | What it looked like |
|---|---|
| a citation scan | zero ids found while the anchor scan kept working, so a corpus full of ids reported clean |
| an anchor pattern | anchors matched but their boundaries did not |
| a branch parser | zero branches found in a file with fourteen |

Each read as a logic bug. None was.

## Cause

Generating source with a shell heredoc into a NON-raw Python string: the escape is interpreted while
writing the file, so the file receives the control character rather than the two characters that
spell the escape. Quoting the heredoc delimiter does not help — the interpretation happens in the
inner language, not the shell.

## The fix

Write source with a file-writing tool, or with a RAW string, and verify with `repr()` on the compiled
pattern rather than by printing it. When repairing, sweep tracked AND untracked files — the first
sweep here scanned tracked files only and reported zero, because the offending module was not yet
staged.

No machine gate: a control byte in a source file is legal, and banning one class of byte across every
file would cost more than it catches. The remedy is the writing habit and the `repr()` check, both
recorded in the kickoff manifest's environment traps.
