---
name: assertion-between-two-derived-values
description: a check comparing two values the same code derives from one source is a tautology, and it arms cleanly
kind: class
universal: false
---

# If the checker builds both sides, the check cannot fail

## Symptom

A gate asserts that A contains B, or that A equals B, and A is COMPOSED by the same code from B. The
assertion is a tautology. It reads like a real check, it has a message, it has a `fail` branch,
`check-arms.py` scores it ARMED because the sibling test names its text — and no state of the world
can make it fire.

It is the [[vacuous-selector-empty-population]] class one level up. That one is about a selector
finding nothing; this one is about an assertion having nothing to disagree with. The tell is
different: the population is fine, the code path runs, and the comparison is still decided before
any data is read.

## Where it bit

`tools/unattended/check-unattended.sh`, first cut. The spec called for "every CORE phase member must
be present in the effective vocabulary", to stop a project deleting one. The leg built the effective
vocabulary as `$PHASES_CORE $PHASES_EXTRA` — so core was a subset by construction. Same for the
Definition-of-Done set. Two branches, both armed, both unfailable.

It was caught the only way it can be caught: by writing the RED fixture and watching it stay green.
No amount of reading the branch finds it, because the branch is correct about what it says.

## The fix

Assert against something declared INDEPENDENTLY of the thing under test.

- A shrink-only COUNT pinned in the project layer (`CORE_FLOOR="6:6"`), while the member NAMES stay
  single-sourced in the kit. Deleting a member drops the count; nothing is spelled twice. This is the
  shape `ARMS_FLOORS` and `baseline.toml` already use.
- An UNDECLARED pin is its own refusal. Omitting the key is the quietest way to disarm a shrink-only
  floor, and "the pin is absent" must not read as "the pin passed".
- Where two sets genuinely ARE declared apart, assert across them: every TERMINAL phase must be in
  the effective vocabulary is falsifiable, because those two lists are written independently.

## How to see it before shipping

Before trusting a new comparison, name the edit that should make it red and MAKE that edit. If you
cannot construct one — if every way of breaking the rule leaves the assertion true — the assertion is
not about the rule. Gated by `tools/unattended/check-unattended.sh` and armed in
`tools/unattended/check-unattended.test.sh`, whose core-floor arms delete a member from the driver
and watch the count fall.
