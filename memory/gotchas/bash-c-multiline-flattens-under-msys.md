---
name: bash-c-multiline-flattens-under-msys
description: a multi-line script handed to `bash -c` from a Windows python re-parses as one line under the MSYS layer, and a backslashed `C:\` path handed to MSYS bash loses its separators, so a probe that works in a shell fails from a subprocess with an error naming neither cause
kind: class
universal: false
---

# `bash -c` with a multi-line body, launched from Windows python

## Symptom

A self-test written in python spawns `bash -c "<several lines>"` to probe a shell helper and gets
`syntax error near unexpected token` or a command that resolves to nothing, while the same lines
pasted into a terminal run clean. A path in the body spelled `C:\projects\...` arrives as
`C:projects...`.

## Where it bit

`TOOL-aReplayedCard-2`'s merger self-test lifted `matchers_of` from `tools/check-wiring.sh` and
ran it through `bash -c` from `tools/settings-merge.py`'s `--selftest` on node `a`. The MSYS layer
between a native python and the bash it resolves re-parses the argument: newlines inside the one
`-c` string collapse, so a `local` after a function header lands on the header's line, and a
backslashed drive path is read as escapes. The sibling class
`memory/gotchas/subprocess-resolves-a-different-shell.md` names the first half of this — which bash
a subprocess gets — and this record is the second half: what that bash makes of the bytes.

## The fix

Write the script to a file under the suite's `mktemp -d` and run `bash <file>`; hand every path in
forward-slash spelling, `C:/...`, which both bashes and native python accept. Gated in
`tools/settings-merge.py`'s self-test arm 17, which resolves a non-WSL bash and runs the lifted
function from a file; elsewhere a documented check.
