---
name: anchor-literal-resolves-above-its-target
description: a check that locates code by searching its own source for a literal finds an earlier occurrence inside a docstring or a string constant, so the comparison it anchors is made against the wrong place and reds on a correct file
kind: class
---

# The anchor resolves above the thing it was meant to find

## Symptom

A check locates a construct by searching a file's text for a literal — `src.find("@check(")`,
`src.partition("def main():")`, a grep for a decorator — and then asserts something about where that
offset sits. The literal is distinctive, the assertion is right, and the check reds against a file
that is correct.

The reason is that the same file DISCUSSES the construct before it USES it. A docstring explaining
why decorators are counted contains the decorator's spelling. A helper that partitions on a function
header contains that header as a string constant. Those occurrences come first in the text, so the
search resolves above the target and every comparison downstream is made against prose.

The tell is a search literal that is also a word the file writes ABOUT. Ask one question: **does
this file, or any file this check reads, mention the construct in prose or hold it as a string?** A
check over a file's own source almost always answers yes, because a file that gates its own shape
explains that shape somewhere.

The mirror-image failure is worth naming too, because it looks like a fix: anchoring the search on a
leading newline so it only matches at column 0, and then believing the arm's own string constants
are what a relocated definition will match. They are not. A literal written with a backslash-n
escape is two characters, not a newline, so a real-newline search never matches it — which is what
makes column-0 anchoring work, and what makes any reasoning built on "the arm will find its own
constant" false.

## Where it bit

`tools/memory-recall/selftest.py`, unit `TOOL-dHashedPrelude-2`, caught by the round-1 spec audit
before a line of it was written. The unit's arm compares three source offsets to prove the live-log
baseline is assigned above the first decorated arm. The spec described the comparison and never
named the bytes searched. Measured on the blob at `3cf05f29`:

| searched | occurrences | first resolves to |
|---|---|---|
| `@check(` | 72 | line 145, inside `check_provenance_chain()`'s docstring |
| `\n@check(` | 71 | line 287, the first decorated arm |
| `def main() -> int:` | 2 | line 2379, inside a `src.partition(...)` literal |
| `\ndef main() -> int:` | 1 | line 2634, the definition |

Line 145 reads ``counting `@check(` decorators by reading the source``. The baseline's home is near
line 285, so an arm on the bare form would have compared 285 against 145, concluded the baseline
came after the first arm, and redded on a correct tree. The arm exists to keep a guard honest, so it
would have been a check that fails on the thing it certifies.

## The remedy

Anchor on a leading newline when the target is a column-0 construct, and make the arm assert its own
anchors are unambiguous BEFORE it compares anything: a count of exactly one for each anchor that
should be unique, at least one for a repeating anchor, redding by name when the count is wrong. That
converts a future duplicate from a silently re-pointed comparison into a red that names the anchor.

Do not pin byte offsets. An offset differs between a CRLF working copy and an LF blob by one per
preceding line, so a pinned pair is wrong under the read mode nobody used, and it moves on every
edit above it. Pin LINE numbers in the comment if anything, and have the arm derive offsets at run
time. That mistake was made here too, in the rev-2 fold: the offsets 7955 and 14712 were read from
the CRLF worktree and labelled as measured at BASE, where the blob gives 7811 and 14426.

Run the candidate predicate over the real tree before wiring it, printing hits AND near-misses.
Counting both the bare and the anchored form of every anchor is the two-second version of that, and
it is what the spec's reuse audit had skipped.

## Gating

Gated in the product, by the arm itself: `test_the_live_log_baseline_is_taken_before_any_arm_runs`
in `tools/memory-recall/selftest.py` counts `\n_LIVE_LOG_BEFORE = ` and `\ndef main() -> int:` at
exactly one each and `\n@check(` at one or more, and fails naming the anchor before it compares an
offset. Observed red against four synthetic sources, including one carrying no anchor at all.

What that does NOT gate is the class anywhere else. It is one arm over one file, and nothing scans
the corpus for a `str.find` over `__file__` whose literal also occurs in prose. Any new check that
locates code by searching source is on its author to census first.
