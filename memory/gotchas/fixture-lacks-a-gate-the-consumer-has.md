---
name: fixture-lacks-a-gate-the-consumer-has
description: a runbook's fixture passes because it lacks a commit-time gate the consumer runs, and the consumer refuses the step the fixture let through
kind: class
universal: false
---

# A fixture that passes because the consumer's gate is missing from it

## Symptom

A procedure written for another repository runs green on its fixture and is refused at the
repository it was written for. The refusal comes from a gate the fixture never had: a hook, a
commit-message rule, a merge-bar leg. Nothing in the fixture could fail the way the consumer fails,
so every arm over it is an assertion about a repository nobody runs.

## Where it bit

The review-harness consumer migration in `WIRE-INTO-PROJECT.md`, build `dPolishedVitrine`, two
closing-review rounds running, each with the class as its blocker. Round 2: the fixture committed in
a repository with no hooks, and inCMS core's pre-commit receipt check refused the migration's first
commit. The fold modelled that hook. Round 3: core also runs a `commit-msg` rule wanting an
attribution line, the fixture did not, and no commit the runbook made could land there. Each round
fixed the gate it was shown, which is fixing the instance.

## The fix

Declare the consumer's gate SET, not the gate that just bit. `tools/govkit/selftest.py` lists every
hook inCMS core installs, marks each one that fires on a plain `git commit` as modelled, names the
rest out of scope with a reason, and a PRECONDITION arm reds when the fixture's hooks and that
declaration disagree. The next hook is one row in a table. The declaration is dated, because it
describes another repository and nothing here can re-read it.

Gated by that PRECONDITION for the migration's fixture only. For a new runbook aimed at a consumer,
this is a documented check: list the consumer's commit-time and push-time gates before writing the
first arm, and model each, or say why it cannot fire.
