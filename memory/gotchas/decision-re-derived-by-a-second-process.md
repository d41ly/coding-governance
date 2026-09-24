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

## Its gate

No class-wide machine gate: a predicate that found two processes reading one name would red on every
sanctioned shared setting. The instance is gated by `tools/push-main.test.sh` arms H1 and H1b, which
drive the lander with the escape set only inside `gate-env.sh`, committed and then excluded, and
assert the marker is absent. The documented check, for a review: for each decision one process
records about another's act, name the file or token that carries the verdict between them. If the
answer is "both read the same variable", that is this class.

## Related

[[two-guards-one-question-two-answers]] is the same root, one question with two derivations, seen
where the two guards wedge each other. Here they do not wedge; they silently agree to disagree.
