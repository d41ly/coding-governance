---
name: ledger-token-wrapped-across-a-line-joins-nothing
description: hygiene check 23 extracts a ledger line's backticked tokens PER LINE, so a token the writer wrapped across a line break belongs to no line and the criterion it answers reads as unanswered
kind: class
universal: false
---

# A backticked token wrapped at the house width joins nothing

## Symptom

An acceptance ledger that plainly answers every criterion reds hygiene check 23 for one of them,
naming a criterion whose ledger line is right there. The line is longer than the house width, was
wrapped, and the shared token sits on the continuation.

## Where it bit

`KICK-aReplayedCard-1`'s acceptance ledger answered AC1 with a token wrapped across two lines at
100 columns, the width every other document in `memory/` is wrapped to. Check 23 in
`tools/memory-tree/check-memory-hygiene.sh` reads a ledger line as ONE physical line when it joins
the answer's backticked tokens to the criterion's, so a token that starts on the bullet line and
ends on the next belongs to neither, and the criterion grades as answered by nothing. The staged
run did not show it — check 23 is HELD under `--staged` and announces the hold — so the full gate
was the first reader to say so, one commit later.

## The fix

Keep every backticked token of a ledger answer on the bullet's first physical line, however long
that line gets; wrap the prose after it. Or run the full `bash tools/memory-tree/check-memory-hygiene.sh`
before the commit that adds a ledger, because the staged leg holds the one check that reads it.
Gated by check 23 itself on the full gate; the `--staged` hold is the reason it reaches the
commit before the reader does.
