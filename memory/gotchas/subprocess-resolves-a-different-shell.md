---
name: subprocess-resolves-a-different-shell
description: Python subprocess resolving the bare name bash finds the WSL launcher, which sees another filesystem
kind: class
universal: false
---

# The name of a shell is not a program

## Symptom

A Python tool shells out to a script. The script plainly exists. The error names the script and says
no such file, and a relative path resolves under a mount prefix belonging to another filesystem.

## Cause

Resolving the bare command name goes through the Windows loader, which finds the System32 WSL
launcher or the WindowsApps alias before git-bash. WSL then sees a different filesystem. Worse,
`shutil.which` in the same process may report git-bash and still not be what the subprocess uses.

Upstream hit the same class from the other direction: a hygiene harness run through the wrong shell
saw a six-path tree and reported collateral failures that drowned the real signal.

## The fix

Name the EXECUTABLE, not the command, and refuse the known launchers by path — `resolve_bash()` in
`tools/memory-tree/corpus_ids.py`, with an environment override. No machine gate: the class has no
source-level signature worth banning, and the remedy is one function every caller shares.
