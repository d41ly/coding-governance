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

## The limit of that gate, MEASURED

`check-arms` grades the SIGNATURE — the longest literal run between interpolations — and nothing
else on the line. An arm may therefore CONTAIN the signature and still assert text the message no
longer emits, which leaves the branch reported ARMED and the arm RED at runtime. The two states are
indistinguishable to this gate.

Measured by `TOOL-dFoldedVerdict-2` on 2026-09-01. `check-unattended.test.sh:714` asserted
`gained only 1 unit id(s) this run BASE lacked` while the shipped message had said
`gained only %d non-WONTDO unit id(s)` since the WONTDO filter landed at `ccb5492c`. The signature
stops at that `%d`, the arm contained every byte of it, and `--check` was green for the whole
interval. Nothing found it but a reader comparing the two strings by hand.

**A SECOND EXCLUSION, from the same unit.** A message COMPOSED INSIDE an awk sub-program and
appended to a `fail` argument is outside the population `check-arms` signs at all. Check 2's third
clause in `tools/unattended/check-unattended.sh` builds a per-record sentence in awk, accumulates it
into a shell variable, and passes it as the tail of one `fail 2 "...:$rv_bad"`. What gets signed is
the OUTER head — `review loops that ran past the ceiling, …` — and `--report` duly lists that branch
ARMED on it. Every per-record message inside is unsigned: it can be reworded, deleted, or made
unreachable with no gate anywhere noticing. Three of those messages were rewritten by
`TOOL-dFoldedVerdict-2` and two more added, and `--check` stayed green throughout.

So: the gate covers a message edit that shortens or moves the SIGNATURE, and does not cover one
that changes the text AFTER the first interpolation. For the second class the arm is still a
two-file edit and the only check is reading both. A refusal whose distinguishing words all sit after
an interpolation has, in effect, no automated arm at all — which is a reason to put the distinguishing
words BEFORE the first one.
