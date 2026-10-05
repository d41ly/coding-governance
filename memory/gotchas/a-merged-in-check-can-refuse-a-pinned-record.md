---
name: a-merged-in-check-can-refuse-a-pinned-record
description: a merge of the remote's default branch into a run branch brings in a check, or narrows one, that the running record cannot satisfy because the bytes it grades are pinned at BASE; nothing grades it again until the verb that owns it, and for a non-overridable item the only exits left are rotation and hand-off
kind: class
universal: false
---

# A merged-in check can refuse a record pinned at BASE

## Symptom

A run merges the remote's default branch into its run branch, mid-build or at the landing, and
every pass after the merge goes green. Hours later `--close` refuses `authorization-reachable`
with a numbered check the run never saw at preflight, after spending its full bar. The item takes
no override and the bytes it read cannot change, so the work cannot land under the record that
built it.

## Why

The driver the run calls, `tools/unattended/unattended.sh`, is the work tree's, so after the merge
commit it is the merged driver, carrying whatever checks the default branch gained. The build
README `authorization-reachable` grades is read at the pinned BASE, a commit the run cannot
rewrite. A check that arrives with the merge and refuses that README is therefore permanent for
this record. Nothing re-graded the item between the merge and the close: `--close` grades
`gates-green` first, so the refusal surfaced only after the bar.

## Where it bit

- This build's first run, under BASE `5266d22e`: its README declared `spec-audit:` under a
  prompt-mode `authorized-by:`, which preflight admitted. The mid-build merge `909c5e0b9`
  brought in check 89, enforcing the ruling TOOL-aWardedAudit-4 and its narrowing
  TOOL-aEvidencedLens-22 that only the owner opts a build into the spec audit. The run built 73
  more first-parent commits, from 10:36 to 19:43 +0300 on 2026-10-05, then rotated onto BASE
  `018b5675`. The closing review's H2 found it; TOOL-aGraftedHelix-30 is the left-shift.

## What to do

Run `bash tools/unattended/unattended.sh --authorization <slug>` after ANY merge of the remote's
default branch into the run branch, before the next pass, and under `in-place` between the
lander's `--prepare` and `--close`. The Skill, rendered from `tools/unattended/SKILL.template.md`,
says both. A refusal there names the two exits: rotate (a README this driver admits, then `--abort
--code repo-state-out-of-mandate` and a fresh `--preflight`) or hand off (`--park`, then `--handoff
--code owner-decision`). A not-evaluated answer is an unanswered remote or an unpublished branch,
which the printed refusal's own remedy clears. The lander, `tools/push-main.sh`, does not run the
verb itself; the Skill line is the trigger. A change to `.unattended.conf` on the default branch
can move the same answer, so the same verb is the check after a merge that brings one.

## Its gate

The verb is **gated by** four arms in the driver's self-test: met with nothing moved, check 89
with the one exits line, not evaluated with no exits, and a source arm holding the verb to the one
`dod_met` call `--close` makes. The CLASS has **no machine gate**: whether a run ran the verb after
a merge is in the machine-local run log, which nothing tracked records. It is a documented check: a
reviewer of a reconciling merge that touches the driver asks whether `--authorization` was run on
the merge commit and what it answered.

## What this does NOT say

It does not say a merged-in check is wrong to refuse: the refusal is usually the ruling working.
It does not cover the other Definition-of-Done items, which `--close` grades and which an override
or a later pass can still answer.
