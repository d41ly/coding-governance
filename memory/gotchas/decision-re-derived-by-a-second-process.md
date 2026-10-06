---
name: decision-re-derived-by-a-second-process
description: a second process that re-derives a decision the first one already acted on, from its OWN inputs, answers a different question whenever those inputs differ, and the gap is exactly where an attacker stands
kind: class
---

# A decision re-derived by a second process from a different input

## Symptom

Process A makes a decision and acts on it. Process B, later or around it, needs to know what A
decided, and instead of READING A's answer it asks the question again from what B can see: its own
environment, its own copy of a config, its own clock. Both code paths are correct against their own
inputs. Whenever those inputs differ, B records a decision A never made, and every consumer of B's
record believes it.

The tell is a variable NAME shared between the two processes and no file, token or return value
carrying A's verdict to B.

## Where it bit

`TOOL-aRepatriatedFork-5`, closing diff review round 1, H1. `.githooks/pre-push` decided whether the
merge bar was a declared stub from `GOV_GATE_CMD_TEST`, read after it sourced `.githooks/gate-env.sh`.
`tools/push-main.sh` decided whether to write the lander marker from `GOV_GATE_CMD_TEST` too, read in
its OWN environment, which never sources that file. A `gate-env.sh` setting the escape and
`GOV_GATE_CMD=true`, committed or merely excluded through `.git/info/exclude`, gave the hook a stub
bar and gave the lander no reason to withhold the marker. So a push nobody's bar gated read as a
gated landing to `unattended.sh --landed`, falsifying the build's first security invariant while
the run log said `bar=stub` to nobody who decides anything.

## Why it survives review

Each half reads correctly alone, and each names the same variable, so a reviewer checking "does the
lander honour the escape?" finds that it does. The inputs differ only through an indirection, here a
sourced file, that neither half mentions near the read. `gotchas.py --for-diff` did not select a
class for it, because the two reads look like one rule spelled twice rather than two derivations.

## What to do

**Give the decision ONE channel.** The process that acted writes what it acted on, the verdict and
its evidence, to a place the second process reads; the second process never re-asks. Here the hook
clears and then writes `pre-push-bar` in its git dir, `<class><TAB><path><TAB><blob>`, once the bar
is vetted and before it runs, and push-main writes its marker only when that file reads `default` or
`tracked`. An ABSENT verdict is not a pass: it is a hook that predates the channel or never reached
the decision, and the consumer fails closed.

**Then vet the indirection** that made the inputs differ, since a sourced file can also just decide
for the first process. `gate-env.sh` is now sourced only when tracked at the pushed sha and clean.

## The second instance: a verdict file with a second writer

`TOOL-aGraftedHelix-32` (the closing review of that build, M3). The lander trusts two files the
tracked pre-push hook writes in its git dir, `pre-push-refusal` and `pre-push-bar`, and that hook
clears both on EVERY run, before its own skip of a non-default branch. The run claim's push in
`write_claim` (`tools/unattended/unattended.sh`) runs that same hook, and the resume tick's `--beat`
pushes a claim from the run's worktree while a landing bar there takes far longer than one beat
interval. So a beat landing mid-bar erased the landing's verdict, push-main wrote no lander marker,
and `--landed` refused a green, pushed landing. Here the second process does not re-derive the
verdict; it deletes it. The remedy is the same channel rule turned on writers: every file the lander
trusts has exactly one writer per push, so `write_claim` pushes nothing while `push-main-active`
sits in that git dir, returning its not-completed code with a reason naming the marker.

That guard was itself a check-then-act (`TOOL-aGraftedHelix-36`, from the rotated closing review's
L1): a claim push that tested the marker a moment before push-main touched it went on to push, and
its hook cleared the files the lander had just cleared and was about to have rewritten. The window is
closed by a lock both sides honour in the same git dir. `write_claim` takes `claim-push.lock` before
it tests the marker, records its deadline in it, and releases it on every path; push-main touches
its marker, then waits for no live lock, then clears its verdict files and pushes, and clears the
marker only after it has read them. Whichever side moves second sees the other.

## The third instance: a stale lock broken on a stale read

`TOOL-aGraftedHelix-37`, a discovery of unit 36's builder. That lock's own break was the class again:
a writer finding `claim-push.lock` stale removed it and made it afresh, acting on a staleness it had
read before the removal. Two writers reading one stale deadline both broke it, the lagging one
removing the fresh lock the first had just made, and both pushed. Measured on node `a`: every trial
in which the second writer lagged the first by about one process spawn let both in. The decision to
break is now taken under a guard directory only one writer can make, and the guard's holder re-reads
the deadline before it removes anything, so the act follows a reading taken where no other breaker
can move it. A release removes the lock only while its `owner` file holds the releaser's token.

## Its gate

The verdict-file instance is **gated by** the driver suite's GH32 AC6 arm, which plants
`push-main-active` and a `pre-push-refusal` beside a due beat and asserts the file byte-identical and
the claim ref unmoved; it read RED against a driver copy without the guard. The lock is gated by
the driver suite's GH36 AC14 arms, a live lock skipping the beat and an expired one cleared and
released, and by `tools/push-main.test.sh` cases 2d and 2e, the lander waiting on a live lock and
passing an expired one; each read RED with its half of the lock cut. The stale-read break is gated
by the driver suite's GH37 arms over the lock functions extracted from the driver: two writers
racing over one stale lock, the abandoned-guard bound, two writers interleaved on one aged guard,
and the owner check; each reads RED on a `mutate` of its own extracted copy, the race with the
re-read under the guard cut.

No class-wide machine gate: a predicate that found two processes reading one name would red on every
sanctioned shared setting. The instance is gated by `tools/push-main.test.sh` arms H1 and H1b, which
drive the lander with the escape set only inside `gate-env.sh`, committed and then excluded, and
assert the marker is absent. The documented check, for a review: for each decision one process
records about another's act, name the file or token that carries the verdict between them. If the
answer is "both read the same variable", that is this class. And for each such file, name every
process that writes or clears it during the act it records; more than one is the second instance.

## Related

[[two-guards-one-question-two-answers]] is the same root, one question with two derivations, seen
where the two guards wedge each other. Here they do not wedge; they silently agree to disagree.
