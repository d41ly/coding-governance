---
name: trailer-parse-reads-only-the-final-block
description: a reader that selects trailers through git interpret-trailers --parse sees only the message's final trailer block, so a trailer followed by any plain line reads as absent
kind: class
universal: false
---

# A trailer parse reads only the final block

## Symptom

A rule asks whether a commit message carries a trailer, or where it sits, and answers through
`git interpret-trailers --parse`. Git reads trailers only from the message's last paragraph, and only
when that paragraph is a trailer block. Put one plain line after the trailer, in the same paragraph or
after a blank line, and git sees no trailer block at all: the parse prints nothing, the rule reads the
trailer as absent, and a message the rule exists to refuse is admitted as one that carries nothing.

The tell to hand a reviewer: **for each rule over a trailer, ask whether it is about git's own trailer
meaning or about presence or position anywhere in the message.** Only the first is git's parse to answer.

## Where it bit

The closing diff review of build `dWitnessedBar`, round 2, item H1
(`memory/builds/dWitnessedBar/reviews/2026-11-21-review-TOOL-dWitnessedBar-106-closing-diff-review-round2.md`).
`check_message_attribution` in `tools/lib/commit_trailers.py` chose the agent's `Co-Authored-By:`
lines from git's parse, so a drifted value or a correct trailer followed by prose read `none`, and the
commit-time check admitted both, which is the class its check 49 exists to refuse.

## The fix

Scan the message as git keeps it, comment lines, blank lines and everything past a scissors line left
out, where a rule is about position or presence anywhere: `TOOL-dWitnessedBar-109` reads the agent
lines and the last line from one list, `extract_message_lines`. Keep git's parse where the rule is
git's own trailer meaning, as `Pass:` is: every reader of a committed `Pass:` reads git's parse, and a
message reader that read more would disagree with them.

Gated by the attribution arms in `tools/unattended/unattended.test.sh` and the `--fixture` cases of
`tools/lib/commit_trailers.py`, which exit 1 on a case whose state is not its planted one.

Its siblings are `rule-stated-with-no-check-that-fails`, a rule whose check cannot fail on the case it
names, and `refusal-branch-with-no-arm`, a refusal no arm reaches.

## What this does NOT say

It does not say git's parse is wrong. It answers what git will treat as a trailer, and a rule about
that meaning should read it. The class is a rule about a line's presence or position read through a
parser that answers a narrower question.
