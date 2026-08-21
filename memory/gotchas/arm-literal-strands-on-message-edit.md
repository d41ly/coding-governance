---
name: arm-literal-strands-on-message-edit
description: editing a fail message strands its arm silently — the branch stays armed-looking, the count drops by one, and only the arms gate notices
kind: class
universal: false
---

# Editing a `fail` message strands its arm, and nothing in the diff says so

## Symptom

A refusal's wording is improved — a clause added, a verb name appended to a list, a parenthetical
dropped. The change is obviously correct and obviously local. The sibling test still contains an
assertion that *looks* like it covers the branch, because it quotes most of the old sentence.

The branch is now UNARMED. Nothing in the diff, the review, or the suite output says so: the suite
still passes, because the arm asserts a string the message no longer contains only when the fixture
actually reaches that branch — and most arms for refusal paths do not run on a green tree.

## Why

`check-arms.py` takes the LONGEST literal run between interpolations as the branch's signature and
requires some non-comment line of the sibling test to CONTAIN it. Shortening the message shortens the
signature and the old arm still matches; LENGTHENING it, or editing anywhere inside the longest run,
leaves the arm holding a prefix that is no longer a superstring — and `sig in line` fails.

The signature does not stop where the sentence does. A message ending
`"... is not the remedy: refs/heads/$cur"` has the signature `... is not the remedy: refs/heads/`,
trailing path fragment included, because that text precedes the first interpolation. Only `:`, `"`
and spaces are trimmed.

## Where it bit

Three times in one session, in one file, all on the same refusal:

- adding `--review` to the driver's unknown-argument list
- adding `--attest` to it, after an arm caught that verb missing from the same list
- adding `--version` to it, after a review found the verb documented on no surface

Each time the arms gate caught it, and each time the diff looked complete. It also bit twice more on
newly written arms that stopped one word short of the signature.

## The fix

Run `python tools/memory-tree/check-arms.py --report` and COPY the signature it prints. Do not retype
the message into the arm from the code — the two look identical and differ at the tail.

Treat any edit to a `fail` string as a two-file edit, the same way a protocol change is a two-carrier
edit. The gate is reliable here, so the cost is one extra run, not a missed defect.

## Arming it

This class is **gated by** `python tools/memory-tree/check-arms.py --check`, which is the gate for it
rather than a check written against it, and that gate is armed by its own selftest. What
is worth pinning is the FLOOR — `ARMS_FLOORS` in `.memory-tree.conf` — because a stranded arm shows up
as an armed-count that dropped by one, and without a floor that number is just a report nobody reads.
