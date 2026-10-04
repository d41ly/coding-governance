---
name: a-new-local-collides-in-a-long-function
description: a local added to a function thousands of lines long can share its name with one a distant block already binds, and the later binding silently replaces the new value only on the inputs that reach that block
kind: class
---

# A new local collides with one a distant block already binds

## Symptom

A change adds a local near the top of a very long function, uses it near the bottom, and every test
it ships passes. A whole suite, or a real target, then fails with an error about a TYPE the new local
never has: `'NoneType' object has no attribute 'items'` on a value that was assigned a dict.

The reason is that a block in between, written years earlier for something else, binds the SAME name
to a different kind of value. Python has one scope per function, so the later binding replaces the
new local, and only on the inputs that reach that block. The new tests never reach it, because the
fixture that would is the one feature nobody thought was related.

The tell is a short, generic local name in a function whose body runs past a screen or two, such as
`_held`, `_out`, `_rows` or `_seen`. Ask one question: **does this name already appear in the
function, as an assignment target, anywhere?** `grep -n '\b<name>\s*[:=]'` over the function answers
it before the first test does.

## Where it bit

`tools/govkit/govkit.py`, unit `DEPL-aHalvedInstall-5`. `_cmd_update` gained `_held: dict` for the
kits a refused row holds back, read at the HELD BACK print about 1,500 lines later. The lf-pin block
in between already bound `_held` to the pin block's text, a string or `None`. Every slice of the new
arms passed, because their scratch kits declared no `[[lf_pin]]`. The whole govkit selftest crashed
at `[-23]`, whose fixture carries an `attributes` row. At an adopter, that row is present whenever
any selected kit pins line endings. Renamed to `_held_kits`. The unit's fixture kit now carries a pin,
so the arms walk the pin block on every run.

## Gate

No gate for the class: whether two bindings of one name in a function mean the same thing is a
judgement no scan makes. The instance is gated by the `[aHI-5]` arms in `tools/govkit/selftest.py`,
whose fixture kit declares an `[[lf_pin]]`, so they walk the block that collided.

## Check

- Before adding a local to a function longer than a few hundred lines, grep the WHOLE function for
  the name as an assignment target, not just the region you are editing.
- Prefer a name that says what the value IS (`_held_kits`) over what the code is doing (`_held`).
- A fixture for a new branch should cross every optional block of the function that a real target
  can reach. A block your fixture skips is where a collision hides.
