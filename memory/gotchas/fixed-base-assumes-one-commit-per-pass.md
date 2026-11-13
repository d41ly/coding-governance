---
name: fixed-base-assumes-one-commit-per-pass
description: a diff scope spelled as a relative rev is right only while every pass makes exactly one commit, and nothing enforces that, so a two-commit pass is graded on its last commit alone
kind: class
universal: false
---

# A fixed base that assumes one commit per pass

## Symptom

A command that scopes its work by a diff is handed out with its base spelled as a relative rev,
the parent of `HEAD`, under a comment that a pass makes one commit. No check holds that invariant.
A pass that makes two commits, which a catalogue edit with a re-rendered mirror forces, is then
scoped to its second commit. A guard that the first commit would have selected reads not-run, the
run reads green, and its record gives no sign the scope was short.

## Where it bit

aNimbleMend's parent harness, `tools/workflows/unattended-build.template.js`, spelled the pass-leg
command with the parent of `HEAD` as its base. That build's own units 1 and 11 each made two pass
commits. Over unit 1's pass the last commit held no path of the policy kit, so a leg guarded on it
was skipped and the red its first commit caused waited for the close's bar, the delay the pass legs
exist to remove. The closing review's round 1 found it as M13
(`memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`).

## The fix

Carry the pass's real base. `TOOL-aNimbleMend-15` hands the command out with no base; the unit
harness asks its builder for the commit it started from, shape-tests the answer, and spells the
command with it. Where the answer is unusable it tells the main loop to use the commit it read
before the dispatch. No return path spells a relative rev.

Gated by the `passLegs` arms of `tools/workflows/unattended-build.test.sh`: a builder's base that
is a third sha must be the one the command names, a return with no base must spell the fallback
sentence, and the parent's `dispatch.args` must end at the script. For any other scope spelled as a
relative rev, this record is the checklist entry: state the invariant that makes the rev right,
and name the check that enforces it.
