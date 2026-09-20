---
name: worktree-crlf-outside-the-gated-population
description: a worktree checkout lands CRLF on eol-pinned files, no wiring gate sees it, and the reader that breaks is a consumer no gate byte-compares
kind: class
---

# Worktree CRLF lives outside the population any gate compares

## Symptom

A file pinned `eol=lf` in `.gitattributes` holds CRLF in a worktree. `git status` is clean, because
the index normalises on commit and the committed bytes are LF. Every gate that byte-compares a
render is green, because it normalises or never reads this file. What breaks is a CONSUMER that
reads the file whole — a launcher, a sourced conf, a hook — and reads a `\r` as part of a value.

## Where it bit

A harness-created worktree carries CRLF on the four `eol=lf`-pinned `.claude/` renders, and that
gates NOTHING: measured 2026-09-02 with CRLF forced into all four, every wiring leg and
`tools/check-wiring.sh` under `--check` (also `WIRING_CHECK`) exit 0. The check's eol population is scoped
to the `.claude/` paths carrying the pin, and its question is "are the committed bytes right", which
they are. `gate-green-by-accident-on-generated-bytes.md` is the sibling class for the byte-compare
gates themselves; this one is what those gates leave uncovered.

## The fix

Ask which CONSUMER reads a file whole, not which gate diffs it. The population to inspect is "files
a runtime reads as bytes", which is larger than "files a gate compares", and the two are not
related by the pin. When a worktree behaves differently from the primary tree on a file whose
committed bytes are known good, `git diff --cached --check` and `cat -A` on the WORKING copy are
the first two commands, before any theory about the diff.

No machine gate: the measurement above is the evidence that the wiring legs cannot see it, and a
gate over every consumer's read path is not written. The documented check is the consumer question
plus `cat -A`, run in the worktree that misbehaves.
