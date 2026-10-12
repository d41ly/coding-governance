---
name: index-derivation-reads-a-half-staged-move-as-a-deletion
description: a derivation over git ls-files reads a move whose destination is not yet staged as a deletion, and a writer driven by it renders that deletion into every file citing what moved
kind: class
universal: false
---

# A derivation over git's index reads a half-staged move as a deletion

## Symptom

A generator derives its output from the TRACKED set, `git ls-files`, so that what it renders is
what the commit will hold. A move then happens in two steps: content leaves a tracked file, and
lands in a new file nobody has staged yet. Between the two, the content exists on disk and is
absent from every input the generator reads.

The generator does not fail. It renders a world where the moved content was deleted, and every
artifact that cited it is rewritten to match. A read-only check over the same state reports drift
whose remedy is the write, which does the damage. Nothing says an untracked file was ignored,
because ignoring it is what reading the index means.

The tell to hand a reviewer is one question: **what does this derivation print when an input it
would read is on disk but not staged — and is that distinguishable from the input being gone?**

## Where it bit

`tools/memory-tree/gen_build_index.py` derives every build README's `ids:` and `LIVE.md` from
`git ls-files`. On 2026-10-09 inCMS core rotated its decision index into a new archive and ran
`--write` before staging it. Seventeen unrelated build READMEs and `LIVE.md` were re-rendered,
because every id whose row had moved looked gone. With the archive staged the same render changed
nothing. The hygiene suite's `rotarchive` fixture had built exactly this state since
`cSteadyMetronome`, and asserted only the orphan line check 14 prints there.

## The fix

Before deriving, list the untracked files in the folder the move lands in and REFUSE, naming each
one and the `git add` that clears it, from the writer AND from the read-only check, whose own remedy
would otherwise be the write (`TOOL-dHomedResolver-2`). Scope the refusal to where moves land; an
untracked draft elsewhere is ordinary work. A tool that performs the move should stage what it
wrote before it renders.

This instance is gated by the half-staged arms of `gen_build_index.py --selftest` and the check 9
arm over the `rotarchive` fixture in `tools/memory-tree/check-memory-hygiene.test.sh`. The CLASS has
no machine gate: whether another index-derived writer refuses a half-staged move is a reviewer's
question.

## What this does NOT say

- It does not say to read untracked files into the derivation. The derivation would then disagree
  with every gate that reads the index, which is a second answer to one question.
- It does not cover an IGNORED file: git will not stage it, so a refusal would have no remedy.
- It does not cover a move into a tracked destination. That is a real change, and the render is
  right to follow it.
- It coexists-with `porcelain-diff-names-a-rename-by-its-destination`, a different failure of a
  move: there a touched-set read sees the destination and misses the source; here a derivation
  sees the emptied source and misses a destination nobody staged.
