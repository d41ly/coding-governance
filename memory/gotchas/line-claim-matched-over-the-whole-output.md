---
name: line-claim-matched-over-the-whole-output
description: an arm that asserts a line names X tests two substrings over the whole output, so it passes when X appears on some other line and the line it means names something else
kind: class
universal: false
---

# Two substrings are not one line

## Symptom

An arm means to observe ONE printed line, say "the keep line names the leg", and is written as two
substring tests over the whole captured output: the phrase is somewhere, and the name is somewhere.
Any other print that quotes the same name satisfies the second half, so the arm stays green while the
line it was written about names the wrong thing, or nothing. The risk grows with the tool's
chattiness: a checker whose other arms red on the same staged break prints the same name on lines
the arm never meant.

## Where it bit

`DEPL-aBenchedProbe-2`'s `check_ceiling_emission` in `tools/govkit/selftest.py` asserted CE4 as
`"kept the target's ceiling" in out and f"'{leg}'" in out`. `tools/govkit/govkit.py` prints other
lines in the same `gate leg '<name>':` shape, the doc_reads-omitted note and the UNGUARDED note among
them, so either would have carried the name for a keep line that lost it. The aBenchedProbe closing
review recorded it (H-L2), and `DEPL-aBenchedProbe-4` matched the leg inside the keep line. The same
unit's staged-break arms for selfcheck 7j4 and the 7h ceiling clause red runs where the subject-pin
ratchet and the stale-exemption check also print the leg, so each asserts on one line.

## The fix

Match every part of the claim inside one line:
`any(all(p in ln for p in parts) for ln in out.splitlines())`. Where the claim spans lines, anchor on
the line that opens it and read the next one by position, never by a search over everything.

## Gate

There is no machine gate for this. No predicate over test source tells a two-substring assertion that means one line from one
that means two facts, so this is a review checklist entry: an arm whose label says a line names X is
read for whether it matches X within that line.
