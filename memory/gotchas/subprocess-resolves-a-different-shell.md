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

Name the EXECUTABLE, not the command, and refuse the known launchers by path — `resolve_bash()`, with
an environment override. TWO copies carry it, because a copy-installed kit cannot import across kit
boundaries: `tools/memory-tree/corpus_ids.py` and `tools/govkit/govkit.py`, the latter paired with
`shell_argv()`, which rewrites a descriptor argv's LEADING `bash` and nothing else.

The govkit instance is worth reading before assuming this class is rare. It sat RED on `main` and
blocked every `push-main.sh`, and nobody saw it: the leg is GUARDED, so only `GATE_FULL=1` runs it,
and it only reproduces where WSL is INSTALLED. Nodes without WSL are green on the same commit. The
first root cause proposed for it was wrong in a way worth remembering — an old python was blamed,
when every python on the node was 3.12+ and the old one belonged to the WSL the shell name pulled in.

No machine gate on the CLASS: it has no source-level signature worth banning. The govkit copy is
armed in its own selftest instead, including that the resolver never returns a System32 or
WindowsApps path.
