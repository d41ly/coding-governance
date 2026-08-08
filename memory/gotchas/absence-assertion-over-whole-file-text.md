---
name: absence-assertion-over-whole-file-text
description: a ban that greps whole file text reds on the comment documenting its own fix
kind: class
universal: false
---

# The documentation of a fix is not a reintroduction of the bug

## Symptom

A source-level ban is added: this construct must not appear in these files. It is written as a
whole-file text search. The very commit that removes the construct also explains why it is gone, and
the explanation necessarily spells the construct — so the ban reds on the prose describing its own
remedy.

## Where it bit

`tools/workflows/check-review-join.sh` bans the retired ref-keyed verdict join, and
`tools/workflows/tier2-review.js` carries a comment spelling that join verbatim, because a reader who
does not know what was removed cannot avoid re-adding it. An earlier instance of the same class: both
source-level bans added in `TOOL-aBatchedLintel-1` were wrong on their first run — one matched the
brace opening each if-block, the other fired on the comment explaining the ban.

## The fix

Judge CODE lines only. The stripper is a character scan, not a regex on the comment marker: a regex
cannot tell the comment opener from the one inside a URL string, and cutting on the wrong one turns a
code line into prose and the ban into a no-op. Quote state and block-comment state carry across
lines; a backslash escape consumes its next character.

Gated by `tools/workflows/check-review-join.sh`, with the comment-only case and the URL-in-a-string
case both armed in `tools/workflows/check-review-join.test.sh`.
