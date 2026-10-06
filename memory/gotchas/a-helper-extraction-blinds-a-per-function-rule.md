---
name: a-helper-extraction-blinds-a-per-function-rule
description: a source rule that pairs two facts on lines of ONE function goes blind when a refactor moves one half into a new helper, naming a correct function or exempting one that no longer holds the half
kind: class
universal: false
---

# A helper extraction blinds a per-function rule

## Symptom

A check reads source by function: a function that does X must also do Y, on a line of the same
function, or it is a hit unless a list names it. A later unit extracts a helper so two paths share
one implementation, and moves the Y line into it. The code is still correct. The check is now wrong
in one of two ways: it names the function that lost the line, which still does Y through the call;
or an exemption keyed on a function NAME keeps naming the function the line left, and the helper
that now holds it reads as unguarded.

The tell is a red that appears in a unit that changed no behaviour, on a function the unit only
refactored, and a fix that is "add the caller to the exemption list" — which widens the list and
leaves the next extraction to red the same way.

## Where it bit

Both at `TOOL-aGraftedHelix-38`, from the pooled calibrate of that build's owed suites at VERIFYING.

- **Check 51** of `tools/unattended/check-unattended.sh`: a function writing a terminal phase must
  call `write_claim`. `TOOL-aGraftedHelix-36` moved `run_settle`'s claim write into
  `write_settle_claim`, called from the settle's `first` and `retry` paths, and the check named
  `run_settle()` on the real tree. Every fixture that copies the real driver went red with it: 41
  failing arm lines across nine outputs.
- **Rule 2** of `tools/unattended/unattended.test.sh`: a function that parks carries the bypass-flag
  guard, and `verb_preflight()` was exempted by literal because its guard lives in `check_waivers`.
  `TOOL-aGraftedHelix-32` moved the waiver park into `write_preflight_record`. The exemption kept
  naming a function that parks nothing, and the function that now parks read as unguarded.

## Why the two do not share one mechanism

They follow calls in OPPOSITE directions. Check 51's claim write moved DOWN, into a callee, so the
rule reaches it by following the call one declared level. Rule 2's guard sits BESIDE the park: in
the caller's EARLIER callee, so following `write_preflight_record`'s own calls, one level or
transitively, never reaches `check_waivers`. One call-following engine for both would answer a
question neither asks.

`two-guards-one-question-two-answers` reads as the family and its remedy, derive once and call the
derivation from both, was measured here and does not apply: the two rules do not ask one question.

## What to do

**Declare the indirection, and grade the declaration.** Following every call is not the rule: a
terminal writer that calls `run_hold`, which writes a `held` claim, would pass, and that is the very
shape check 51 exists to catch. So the helper is DECLARED, and the declaration is graded in both
directions: an entry that is no function, or whose own body does not do Y, is a hit naming it.

**Key an exemption on the call structure it rests on, not on a name.** The rule 2 exemption is a
pair, the parking function and its guard function, and an arm derives the parking function's callers
and checks each calls the guard on an earlier line. A stale-entry arm checks the exempted function
still does the thing it is exempted for.

## Its gate

Each instance is gated, and the class is a documented check:

- check 51: `TERMINAL_CLAIM_HELPER_FNS` and its five arms in `tools/unattended/check-unattended.test.sh`.
- rule 2: `park_exempt_fn` and `park_exempt_guard`, with the stale-entry and call-structure arms in
  `tools/unattended/unattended.test.sh`.

The other per-function rules of this kit read a function the same way and are green today: rule 1
of `tools/unattended/unattended.test.sh` (a function writing the phase stages it), and checks 39 and
48 of `tools/unattended/check-unattended.sh`. When a unit extracts a helper out of a function one of
these grades, re-run that rule over the result and read whether its subject moved. A green that
survives an extraction because the rule now reads an empty function is the failure, not the pass.

## Related

[[two-guards-one-question-two-answers]] — measured against both instances; its one-derivation remedy
does not apply, for the reason above.
