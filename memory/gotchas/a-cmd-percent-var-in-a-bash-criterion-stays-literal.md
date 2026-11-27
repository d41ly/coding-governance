---
name: a-cmd-percent-var-in-a-bash-criterion-stays-literal
description: a spec criterion spells a cmd.exe `%VAR%` inside a bash command, bash leaves it literal, and the probe reads a path or value nobody meant
kind: class
universal: false
---

# A cmd.exe variable in a bash criterion stays literal

## Symptom

A spec's acceptance criterion or gate names a command for bash to run, and the command spells a
Windows environment variable in cmd.exe's form, `%TEMP%` or `%USERPROFILE%`. Bash does not expand
`%...%`: the command runs with the percent signs in place, so a path argument names a directory
called `%TEMP%` under the working directory, a value compares against the literal text, and the
criterion is observed against something its author never meant. Nothing errors. A scratch tree is
written into the repository, or a probe that should find a file reports it absent.

## Where it bit

Raised by the round-1 spec audit of units 36 to 43 of dTotalRecall, finding 21, at
`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`, and
batched into `TOOL-dTotalRecall-53` as its item S31: a criterion that a bash runner would execute
spelled its scratch path through cmd.exe's variable form.

## The fix

**No machine gate.** A criterion is prose; telling a command in it from a quotation of one needs the
reader. The class is named so the checklist reaches every spec a criterion is written in, which is why
its one anchor is the `/spec/` token, selecting every tracked path under a build's spec folder and
nothing else.

- Spell a variable in the shell the criterion runs in: `$TEMP` or `${TEMP}` for bash, and write a
  scratch path out absolute where the run hands one over.
- Where a command is meant for cmd.exe or PowerShell, say which shell runs it; never leave a reader to
  infer it from the variable's spelling.
- On review, read every `%` pair in a criterion's command as a question: which shell expands it?
- It coexists-with `observed-by-claim-no-arm-discharges`: both leave a criterion observed against
  something its author never meant, there an arm that never reads the surface, here a path bash
  never expanded.
