---
name: bounded-through-a-pipe-is-unbounded
description: a wall-clock timeout captured through a command substitution bounds the verdict and not the clock, and reports success on schedule while the caller blocks
kind: class
universal: false
---

# `out=$(timeout N cmd)` bounds the verdict, not the clock

## Symptom

A deadline is added to a command that can hang. The verdict is correct — the caller sees exit 124 and
reports a timeout, naming the right thing — and the wall clock is unchanged. The run takes exactly as
long as it did before the deadline existed, and the pool slot, the worker or the push stays held for
the whole hang.

The knob looks like it works, because the only thing anybody checks is the message.

## Why

`$( )` reads until EOF. EOF arrives when the LAST inherited write end of the pipe closes, not when
the direct child exits. `timeout` signals the process it started; a surviving grandchild, or anything
backgrounded by that child, still holds the pipe. So the substitution blocks until the descendant
finishes, and `timeout` has already reported 124 on schedule.

GNU coreutils signals the process group, which helps — and does not reach a grandchild reliably under
MSYS, which is where this was measured.

## Where it bit

Twice in this repo, independently, days apart:

- `tools/run-gates/run-gates.sh` — the per-leg timeout. Measured against a real fixture: 51.4 s wall
  against a declared 1 s bound, and a four-run set against a 30 s sleeper with a 3 s bound measured
  18.7 / 22.1 / 27.0 / 27.0 s. Same wall clock with the knob on and off. Three carriers documented a
  bound that was not enforced, latent only because every shipped profile row set the timeout to 0.
- `tools/unattended/unattended.sh` — the bounded remote observation, caught BEFORE it shipped, by the
  recall probe the build method requires before a pass. Reproduced standalone on node `c`:
  `out=$(timeout 1 bash -c 'sleep 6 & exit 0')` returned after 6 s; the same command redirected to a
  file returned in 0 s.

- The HARNESS, not the product, and it is the orphan half of this note arriving on schedule.
  Four selftests were killed mid-run over one session. Each left its scratch subtree held open by a
  surviving grandchild: 99 stale `/tmp/tmp.*` directories, 94 removable and 5 not, and the next
  suite aborted at startup with `rm: cannot remove ...: Device or resource busy`. Six orphaned
  `*.test.sh` processes had accumulated 3 to 21 s of CPU each and were still running; with them
  alive every suite produced ZERO bytes for twenty minutes and read as a hang in the code under
  test. After killing them by command line, the hygiene engine finished in 42 s green. Nothing was
  wrong with the code, and two rounds of bisecting it found nothing because there was nothing.
  **Diagnostic:** a suite emitting no output at all, rather than stopping partway, is a machine
  symptom and not a logic one — check for orphans before reading the diff.

## The fix

Redirect to a file, let `timeout` return, then read the file. Add `-k` for the child that ignores
SIGTERM. The file read cannot block on anybody.

```sh
timeout -k 5s "$BOUND" "${argv[@]}" </dev/null >"$work/out.raw" 2>&1; rc=$?
out=$(cat "$work/out.raw" 2>/dev/null)
```

If the orphans themselves must die — they may hold a scratch directory — run the command under
`setsid` and signal the group rather than trusting `timeout` alone.

## Arming it

**An arm that asserts the message cannot see this defect** — the message is the half that was always
correct. The arm has to MEASURE ELAPSED TIME and fail if the run outlived a small multiple of the
declared bound. The first arm written for the gate-runner knob asserted the string and the RED verdict
and was satisfied by the broken code, which is why this class is catalogued rather than considered
fixed.

A source-level ban on the substitution form is worth having beside it, but scope it to CODE LINES: a
whole-file grep reds on the comment documenting the fix, which is
`absence-assertion-over-whole-file-text` happening inside the guard.

## Gating

Gated by `tools/unattended/unattended.test.sh`, in two halves, and PARTIALLY — the scope is stated
because a class this cheap to reintroduce deserves an honest coverage line rather than a reassuring
one. The first half is a source-level ban on the substitution form across `tools/unattended/`, scoped
to code lines so the comment documenting the fix does not red it. The second is a MEASURED elapsed
assertion on the node running the suite, which is the only half that can see the defect at all,
because the message was always the correct part.

**What nothing gates:** the class repo-wide. `tools/run-gates/run-gates.sh` carries the same fix and
its own suite asserts a rendezvous rather than elapsed time for the concurrency arm — deliberately,
since elapsed time there is a fact about the node — so the runner's bound is correct today by
inspection and by its comment, not by an arm that would catch a regression. Nothing sweeps other kits
for `out=$(timeout`. Adding a repo-wide source scan is cheap and is not done here; the two dossiers
that claim this class are the two places it has actually bitten.
