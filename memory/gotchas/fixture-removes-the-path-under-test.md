---
name: fixture-removes-the-path-under-test
description: a fixture stabilised by DELETING a dependency stops the branch under test from executing, so both A/B arms run the other code twice and agree
kind: class
---

# A fixture frozen by deletion measures everything except the change

## Symptom

You build an honest A/B: one clone, both arms back to back, each arm asserting rc, line count and a
marker only real work emits. To keep it stable you remove the thing that could move under you — a
remote, a service, a clock source, an env var — because a frozen input is what makes two runs
comparable.

Both arms pass every assertion. The outputs are byte-identical. The timing shows no difference, and
you conclude your change is neutral.

The branch you changed never executed. Removing the dependency did not freeze its VALUE, it deleted
the input that GUARDS the branch, and the guard took the whole path with it. Every arm assertion
still passes, because they were written to prove the RUN happened, not to prove the CHANGED CODE ran.

The signature is agreement that is too complete: a rewrite of a hot function that changes neither
the timing nor a single byte of output.

## Where it bit

`TOOL-aQuenchedHarness-10`, node `a`, 2026-09-07. `tools/unattended/check-unattended.sh`'s
`is_published` was rebuilt from two git processes per commit per tip to two for the whole function.
The A/B ran on a clone whose `origin` had been DETACHED, so that my own pushes could not move the
tips the leg observes.

`ADV_HEAD` and `ADV_TIPS` are read from `git ls-remote`. With no remote they are empty,
`is_published` returns before touching either the old code or the new, and check 9 reports its
own no-remote refusal instead. The A/B reported **IDENTICAL** and **857 s against 895 s**, and I
recorded that the rebuild bought nothing.

It had in fact bought a **defect**: the new warm-up parsed `git cat-file --batch-check` as four
fields when it prints three — `<oid> <type> <size>`, not echoing its input — so the type was read
one field late, every advertised tip looked unreadable, and every answer became CANNOT TELL. On a
clone WITH a remote that reds check 9 on every record in the tree. The fixture that was supposed to
catch it could not have.

Re-run against a bare frozen origin advertising the same 28 heads: the defect appeared on the first
run, and the corrected rebuild measured **618 s to 316 s** with output byte-identical.

## The fix

**Freeze by pinning the value, not by deleting the input.** For a git remote that is three commands
and it is stable forever, because nothing else can write it:

```bash
git init --bare "$O"
git push --no-verify "$O" 'refs/remotes/origin/*:refs/heads/*'   # the tips as they are, now
git -C "$O" symbolic-ref HEAD refs/heads/main
git -C "$CLONE" remote add origin "$O" && git -C "$CLONE" fetch -q origin
```

Then confirm the fixture is REPRESENTATIVE before trusting an arm: count what the real subject sees
and what the fixture advertises, and require the pair to match. Here that was
`git ls-remote --heads origin | wc -l` = 28 on both.

**And assert the changed path itself, not only the run.** The arm marker must be something ONLY the
new code emits — a log line, a counter, a table size — because rc, line count and even byte-identity
are all satisfied by a run that skipped the change entirely.

## What it is not

Not `ab-arm-never-did-the-work`, which is an arm that REFUSED and exited early: there the run is
missing and the duration is suspiciously small. Here both runs are complete, correct, and the right
length. What is missing is one branch inside them, and nothing about the shape of the result says so.

Not fixed by interleaving or more rounds. Both arms are biased identically, so every round agrees.

## The gate

There is **no machine gate** and a general one would be a lie: nothing in a tree can know which
branch a given A/B was meant to exercise. What replaces it is a documented check, in one line —
**a fixture that removes an input must be shown to still execute the code under test.** Name the
input the fixture drops, name the branch that reads it, and if they intersect, pin the input instead
of dropping it. Run it as part of the recurring-bug-class checklist over any diff that adds or edits
a measurement harness.
