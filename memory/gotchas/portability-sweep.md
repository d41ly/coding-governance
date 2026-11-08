---
name: portability-sweep
description: a change to a file where a Windows, Git for Windows or MSYS trap already bit is swept for the whole domain, CRLF to clock skew, not only for the one instance recorded at that file
kind: class
universal: false
---

# Portability — the domain's sweep, at the files where its traps bit

## Symptom

A change that is green on the machine and the shell it was written on reds, or passes by finding
nothing, on another: a fresh worktree checks a file out with CRLF, a text-mode read eats a bare CR, the
MSYS layer rewrites an argument or a path, a path past the length limit fails to clone, a hook killed
by a signal exits in a way its caller reads as success, a spawn per item costs seconds under
antivirus, or two clocks disagree. Each instance has its own record, anchored where it bit, and a
reviewer handed one of them is handed none of the domain's others.

## The sweep

For a subject touching a file below, ask each question of the change, not only the one its member
record answers:

- CRLF and autocrlf: does a fresh worktree check this file, or a file it writes, out with CRLF, and
  does every reader of those bytes, a grep count included, survive a CR at a line end?
- text-mode reads: does a read decode or split lines in text mode, where a bare CR is a line break?
- MSYS argument and path rewriting: does an argument, a multi-line script or a drive path cross from
  a native process into MSYS bash, or back, where it is re-parsed?
- path length: does a path built here, a scratch or a clone path, grow past what Windows admits?
- Git for Windows signal semantics: does a process here die by a signal, or start a job, whose exit
  status or ignored SIGINT the caller misreads?
- spawn cost under antivirus: does the change add a process per item, where each creation is scanned?
- clock skew: does a comparison read two clocks, or a file time against a wall time?

## Members

- bash-c-multiline-flattens-under-msys
- msys-grep-counts-cr-on-every-line
- text-mode-read-eats-a-bare-cr
- gate-green-by-accident-on-generated-bytes
- worktree-crlf-outside-the-gated-population
- signal-killed-hook-reads-as-success
- process-creation-is-the-suite-cost
- allowlist-narrower-than-the-root-it-guards
- async-job-starts-with-sigint-ignored

## Where it bit

Each file below is an anchor of at least one member, so the sweep reaches a review only where a
recorded defect of the domain already landed: `tools/check-wiring.sh`, `tools/settings-merge.py`,
`tools/unattended/check-unattended.sh`, `tools/memory-tree/gen_build_index.py`,
`.githooks/pre-push.test.sh`, `tools/push-main.test.sh`, `tools/unattended/run-unattended-gates.sh`,
`tools/hooks/scratch-guard.js` and `tools/run-gates/run-gates.runlog.test.sh`.

## Gate

This class has no machine gate: the sweep is a reviewer's question over a domain, and each member
names its own gate or documented check for its one instance.
