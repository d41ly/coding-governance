---
name: read-allowlist-admits-a-writing-option
description: an allow-list of reading programs decides a shell call only reads, and one of those programs takes an option that writes, so a call that changes a file is counted as a read
kind: class
universal: false
---

# The program reads, and one of its options writes

## Symptom

A classifier holds a closed list of programs that read, and answers read for any call naming one of them. It
checks the shell's own write, a redirect to a file. A listed program also writes through an option of its own:
`git diff --output=<file>`, `find -delete`, `find -fprint <file>`, `find -exec <command>`, `sed -i`. The call is
answered a read, and what stands behind the answer, a byte count, a permission or a guard, carries on past the act.

## Where it bit

The dTotalRecall closing review, round 2, of 2026-11-25
(`memory/builds/dTotalRecall/reviews/2026-11-25-review-TOOL-dTotalRecall-115-closing-diff-review-round2.md`,
findings 3 and 9). `tools/workflows/replay_scorer.py#check_read_call` refused `sed` its in-place option and
admitted every option of `git` and `find`, so the bytes a lens read before its first act ran on past a
`git diff --output` and a `find -delete`. `find -exec` stood in its docstring as a gap; the other options did not.

The same closing review, round 3, of 2026-11-26
(`memory/builds/dTotalRecall/reviews/2026-11-26-review-TOOL-dTotalRecall-122-closing-diff-review-round3.md`,
finding 1). The round-2 fix refused the writing options and admitted every option that RUNS a program: `rg --pre`,
`git grep -O`, `git diff --ext-diff`, `git log --textconv`, and an env assignment or a `git -c` ahead of the read,
`GIT_PAGER=rm git log` among them. ripgrep's `--hostname-bin`, which the report did not name, runs one too.

## The fix

- Read each admitted program's manual for what it writes AND for what it runs, and refuse each such option beside
  the program's name: `rg --pre` and `--hostname-bin`, `git grep -O` and `--open-files-in-pager`, `--ext-diff` and
  `--textconv`.
- Deny by default for what precedes the subcommand: any env assignment ahead of a read program, and any git option
  outside a short allow-list (`-C`, `--no-pager`) ahead of a git subcommand, makes the call the act, so the next hook
  variable or config option is refused without being named.
- Match the option whole. `git grep -o` and `git ls-files -o` read, so a short option is never refused by its letter.
  Where the parser takes prefixes, as `git grep` takes any unambiguous prefix of a long option, match from the
  shortest unique spelling up (`--op`, `--textc`); and match a short option inside a cluster only behind letters
  that take no argument, so `-nOrm` is the pager and `-eOops` a pattern.
- Write one case per option, each seen red with that option's test cut.

## Gated by

`tools/workflows/replay_scorer.py`, whose `map-transcript` arm reads zero bytes before a call of each option, each
run option and each form that precedes a subcommand, and reads its own bytes before each read beside them. A
program joining the list owes its own cases; nothing reds one that arrives without them.

## What this does NOT say

- It coexists-with `an-allow-that-bypasses-a-judge-names-none`: there an answer of allow drops the judge the call
  would have met; here the judge is asked, and reads the program's name for what the call does.
