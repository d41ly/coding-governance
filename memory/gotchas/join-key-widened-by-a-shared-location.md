---
name: join-key-widened-by-a-shared-location
description: a join keyed on WHERE something happened takes every place the subject ever touched, and one of those places is shared by every subject, so the key admits everyone's lines
kind: class
universal: false
---

# A join key widened by a location every subject shares

## Symptom

A reader attributes records to a subject by location: a line belongs to a run when it was made in a
tree the run worked in, a request belongs to a tenant when it came from a host the tenant used. The
key is built from EVERY location the subject's own records name, and it reads as precise, because
each of those locations really did appear in the subject's history.

One of those locations is not the subject's. It is a place every subject passes through: the tree
every run lands from, the jump host every operator logs in through, the shared CI runner. One visit
by the subject, or one look by an observer acting in its name, puts that place in the key, and from
then on every other subject's records made there join this one.

The tell to hand a reviewer is one question: **which location in the key would appear in EVERY
subject's key, and what put it there — work the subject did, or a visit anyone could make?**

A second tell sits beside it, for keys that outlive their subject: **a location the subject once
held is not the subject's for ever.** A worktree outlives its run and is reused. A key with no end
admits the next tenant's records.

## Where it bit

The closing diff review of build `dLoggedFlight`, round 1, confirmed it as a HIGH. The run model in
`tools/runlog/model.py` joined bars and pushes to a run by the tree they were made in, and built that
key from the tree of every driver call in the run's journal segment. The run's own `--landed` runs
in the primary tree, as the protocol lands, and an owner running `--status` there is ordinary. Either
call made the primary tree one of the run's trees for its whole window. Another run's landing bar
and push, and a refused raw push to the default branch by anyone in that tree, then joined this run,
entered its journal commitment and fired `push-outside-lander` on it. A skeptic reproduced it on the
kit's own landed fixture, and no arm had staged a `--landed` from any tree but the run's own.

The fix for the window end in the same fold met the second tell. A non-terminal window now reaches
the run's last bar in a tree it holds. With no end to the hold, a worktree a later build reused would
have stretched a dead run's window to the other build's last bar.

## The fix

- **Build the key from acts that claim the location, not from every visit.** A driver call claims
  its tree when it is a preflight, or when its START read a phase before the close and its verb is
  none of `--status`, `--resume` and `--landed`. Those three read the record or land the run, and
  every tree can run them.
- **Give the claim an end.** A tree is held from the run's first claim there to another run's first
  claim there after the run's last one. The same hold also starts only at the first claim, so a tree
  the run moves to mid-window was the previous tenant's until then.
- **Keep the key by content where one exists.** The landing push still joins by the sha it pushed,
  and the landing bar by the run id that push pinned. Neither needs the shared tree in the key.

Gated by the runlog kit's self-test, `tools/runlog/selftest.py`, model AC20: the landed fixture lands
from the primary tree, the run's calls there cover each of the claim rule's exclusions, and foreign
lines there, in a reused worktree after the next run's claim, and in a second worktree before the run
claims it, each stay out. Each exclusion and each end of the hold was seen RED with its own break.

## What this does NOT say

It does not say a location key is wrong. A tree is the only key a bar with no pinned id has, and it
is right for the tree a run holds alone. Nor does it say two subjects can always be separated: two
runs that claim one tree in the same stretch both hold it, and a line made there joins both. The class
is about the location EVERY subject passes through, and about a claim with no end.
