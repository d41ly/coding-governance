---
name: borrowed-seed-inherits-its-head-state
description: a fixture built from another suite's seed inherits that seed's HEAD state, and a probe that reads HEAD is dead on an unborn one
kind: class
---

# A borrowed seed hands its borrower an unborn HEAD

## Symptom

An arm that borrows another suite's `seed()` for its fixture is red on every run, and the refusal
names something in the CHECKER under test — a dead probe, a missing verdict — rather than the
fixture. The seed looked like "a git repo with the kit in it", and it was one: `git init`, an
identity, files staged. Nobody asked whether it had ever COMMITTED, because the suite that owns
the seed never reads HEAD.

## Where it bit

Build `aWokenSentinel`, spec-audit round 1, H6. Two real-driver integration arms — unit 3's AC11
and unit 4's AC10 — run `--liveness` inside a `git init` fixture seeded the way
`tools/unattended/adopt-unattended.test.sh`'s `seed()` builds one. That seed staged one stub and
never committed. The driver's clock block in `tools/unattended/unattended.sh` reads
`git log -1 --format=%ct`, marks the probe DEAD on the empty answer an unborn HEAD gives, and
refuses with `fail 52` and no verdict line. The `Stop` hook then read `liveness-unreadable` and
allowed, so "the invocation blocks" could never go green and the `last-stall:` line never printed
— both arms red for a reason unrelated to the hooks they exist to test.

The owning suite was correct for its own arms: the adopter's `--check` reads the working tree,
and no arm of it asserts a log. The defect was in the BORROW: a fixture is a bundle of state, and
the borrower inherits every part of it, including the parts the owner never declared because the
owner never depended on them.

## The fix

Two halves, both taken in `TOOL-aWokenSentinel-14`.

A seed that a driver's clock will read commits once. `seed()` in
`tools/unattended/adopt-unattended.test.sh` ends with `git add -A && git commit -q -m seed` under
`GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null` — the kit's existing idiom in
`tools/unattended/check-playbook.test.sh`, hermetic against the machine's `commit.gpgsign` and
hooks, which is the sibling class `fixture-inherits-ambient-machine-state` — and a commit that
fails is the seed's own loud refusal, exit 2, never a quiet subshell exit that leaves HEAD unborn
and every borrower red for a reason it cannot name.

A fixture that borrows a seed STATES the HEAD state it inherits. Specs 3 and 4 say in their
fixture paragraphs and `fixture:` lines that the seed commits once, so HEAD is born and the
driver's `git log` probe is live. The sentence is what makes the next borrower ask the question.

Gated by the real-driver arms of units 3 and 4 in `tools/unattended/adopt-unattended.test.sh`,
which red on an unborn HEAD through the driver's `fail 52` — the dead-probe refusal is the correct
behaviour and stays; the fixture stopped triggering it. Beyond those arms there is no source-level
pattern to scan for: "reads HEAD" is a property of the consumer, not of the seed, so the check is
the question asked at the borrow — what does this probe read, and does the fixture have it.
