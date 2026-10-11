---
name: signal-killed-hook-reads-as-success
description: on Git for Windows a git hook that dies by a signal is read by git as exit 0, so an untrapped TERM, HUP or INT, a KILL or a TerminateProcess lands a push the hook was about to refuse
kind: class
---

# A hook killed by a signal reads as success on Git for Windows

## Symptom

A push to the default branch lands while its pre-push bar never ran, and nothing printed a verdict.
The hook's run-log END line reads `rc=0 exit=unclean` a few seconds before the push. The hook's bash
may still show in `ps` afterwards with `ppid 1`, which is normal for every hook bash there and is not
evidence: its parent is the native `env.exe` stub git waits on, not a Cygwin process.

## Where it bit

aRoutedQuill's landing on node `a`, 2026-10-11 01:33:35 +0300: `push-main.sh --land` pushed
d22cca6c..69e0ff0f with its bar queued at position 2 in the turnstile. The session stopped a
background shell at the same moment, and the bar logged a fork failing with 0xC0000142, the shape a
torn-down console gives. The hook's END reads `rc=0 exit=unclean decision=full` at 01:33:30.
Reproduced on a scratch clone with git 2.54.0.windows.1 and MSYS bash 5.3.9: TERM, HUP, INT and
KILL to the hook's bash, and a `taskkill /F` of its Windows pid, each landed a push; `exit 1` did not.
The same transcript shape, queued and then the remote contacted, is `TOOL-aSurfacedLexicon-25`.

## Why

MSYS hands a native parent a signal death as Windows exit code `n << 8`, and Git for Windows reads a
hook's status as `GetExitCodeProcess(...) & 0xff`, which is 0. On Linux git sees the signal and
refuses. A bash script with no trap runs its EXIT trap and then dies by the signal, so a hook's own
"clean exit" bookkeeping records the death without preventing it.

## The fix

**Every catchable fatal signal is trapped in a gate hook and turned into an ordinary non-zero `exit`**,
which git reads correctly everywhere. bash runs a trap only after a foreground child returns, so the
long-running part runs as a background child the hook `wait`s on; `wait` returns as soon as a trapped
signal arrives. KILL and TerminateProcess cannot be trapped, so the caller does not take git's exit 0
as the verdict: the hook writes a positive allow record at its one success exit, and the lander calls
a push with no such record `landed UNGATED` (`TOOL-aSignalledHook-1`).

A fixture that grades this must prove its hook is installed. An empty hooks directory lands every
push too, and reads exactly like the fail-open.

**This overrides the fix in `trapped-signal-waits-for-the-foreground-child.md` for a git hook.**
"Trap EXIT and nothing else" is right for a script whose caller reads a signal death as a failure,
and it is the fail-open for anything git runs on Windows. The cost that record names, a trap delayed
behind a foreground child, is paid by running the child in the background and waiting on it.

## Gate

Gated by `.githooks/pre-push.test.sh`, the SG arms: TERM and HUP to the hook mid-bar and TERM before the bar
must each refuse, and the signal must be handled before the stub bar's sleep ends. Staged RED by
installing the hook as it stood at b726385f, which landed all three pushes, and by moving the bar back
into the foreground, which held the signal 32 s behind it. `.githooks/pre-push.runlog.test.sh` AC3
reads the refusal on the END line. `tools/push-main.test.sh` SG AC3 grades the lander half with a
hook that exits 0 and leaves no allow record, and was staged RED on the lander as it stood at
b726385f, which called that push landed.
