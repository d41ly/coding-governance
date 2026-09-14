---
name: observation-before-the-last-fold-of-the-same-commit
description: an acceptance observation taken before the last fold of the same commit is an observation of nothing, because the tree it saw is one the commit never held
kind: class
---

# An observation taken before the commit's last fold saw a tree that never landed

## Symptom

An acceptance ledger records `exited 0` for a leg. The leg is RED at the commit the ledger sits in.
Nothing was rewritten and nobody lied: the observation was taken, it was green, and then the SAME
commit folded one more change — a review finding, a hook that denied the pass's own syntax check —
and the fold moved the thing the leg counts. The ledger line was already written, it named no sha,
and the commit that landed both is the first tree the leg ever graded.

The shape is `amendment-leaves-its-other-half-standing` one level down: the amendment is inside
the commit, and the half left standing is the observation of the tree from before it.

## Where it bit

`TOOL-aDeferredBar-3`, node `a`, 2026-09-14. The pass wrote a hand-justified row in
`tools/install-prefix-carried.txt` for its suite's 37 fixture-internal command strings, ran
`bash tools/check-install-prefix.sh`, saw exit 0 and wrote the AC9 ledger line. Minutes later the
wired hook denied the pass's own `bash -n` over its suite; the spec went to rev-5 and two arms
carrying the suite's path as a command string joined `tools/unattended/gate-guard.test.sh` in the
same build commit. The row said 37, the suite carried 39, `install-prefix (shipped surface)` was
RED at the tip, and the ledger said `exited 0`. The closing diff review found it as its first
high, and the bar would have refused the landing until the row moved.

## The fix

**An observation names the tree it was taken on, and the LAST fold re-takes every observation
the fold could have moved.** Two rules, both cheap:

- A ledger line that records a leg's exit records the sha, or says in as many words that it was
  taken on the staged tree before the commit — the unit-2 ledger already does the second for a
  commit that cannot observe itself. A line with neither is a claim about no tree in particular.
- Before writing the build commit, list what the last fold touched and ask which observations
  read a COUNT or a POPULATION over those files. A ratchet row, a floor, a carrier count, a
  `PASS (<n> assertions)` line: each is an observation the fold can move without touching its
  line. Re-run those, not the whole set.

## What it is not

Not `amendment-leaves-its-other-half-standing`: that class is two records disagreeing across a
fold. Here there is ONE record and it is honest about a tree that no longer exists.

Not a stale ratchet in the ordinary sense. The row was correct when written; the tree moved under
it inside the same commit, which is why the ratchet's own `ROSE` verdict is the signal and the
ledger line is the defect.

## The gate

There is **no machine gate** for the ledger half, and the honest statement of why: a ledger line
carries no sha the grammar demands, so nothing can compare its `exited 0` to the leg at HEAD. The
memory-tree ledger grammar could grow that field, and the closing review's DoD could then refuse a
line whose recorded exit disagrees with the leg at the commit; that is a backlog row, not this
record. What binds today is a documented check: **every ledger line that records a leg's exit
names the sha or the staged-tree convention, and the pass re-takes every count-shaped observation
after its last fold.** The ratchet half already has its gate — `tools/check-install-prefix.sh`
reds `ROSE` on the next bar — which is what caught this one.
