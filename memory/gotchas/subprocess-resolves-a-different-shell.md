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

Name the EXECUTABLE, not the command, by RUNNING each candidate. ONE rule does it: the
`resolve_bash_py` block of `tools/lib/resolve_bash.py` and its JavaScript twin, the `resolve_bash_js`
block of `tools/lib/resolve_bash.js` (TOOL-dWitnessedBar-26). `GOV_BASH` first, then Git's own
`bin/bash.exe`, then PATH, each candidate run with `uname -s` and the caller's script; on Windows the
answer must start `MINGW` or `MSYS`, so the WSL launcher, which answers `Linux` and drops the script
argument, is refused under any name, and a System32 or WindowsApps path is never run. No candidate
passing is a refusal naming each one tried, never the bare name. A copy-installed kit cannot import
across kit boundaries, so every file that starts a bash carries the block inline behind its own
adapter, and `tools/lib/resolve-python.test.sh`'s parity rows hold each copy to its canonical. Count
the copies with `git grep -l '>>> resolve_bash_'`, never in prose here: an earlier revision of this
paragraph counted two, then three, and named a function by a name it no longer had.

The govkit instance is worth reading before assuming this class is rare. It sat RED on `main` and
blocked every `push-main.sh`, and nobody saw it: the leg is GUARDED, so only `GATE_FULL=1` runs it,
and it only reproduces where WSL is INSTALLED. Nodes without WSL are green on the same commit. The
first root cause proposed for it was wrong in a way worth remembering — an old python was blamed,
when every python on the node was 3.12+ and the old one belonged to the WSL the shell name pulled in.

The CLASS is gated by its source signature: `scan_bare_bash` in `tools/run-gates/measure_legs.py`
lists every tracked `*.py` and `*.js` line outside the block that launches the bare name `bash`,
falls back to it, or loops over PATH for it. It does not see a PATH lookup through a variable or a
name bound to `"bash"` and launched later.
