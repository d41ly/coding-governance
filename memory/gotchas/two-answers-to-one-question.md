---
name: two-answers-to-one-question
description: a fact stated in two places drifts, and the copies need not disagree loudly to be wrong
kind: class
universal: true
---

# One fact, one home

## Symptom

A value is declared twice — a pattern in a shell gate and the same pattern in a Python module, a
status in front matter and a status derived from records, a set transcribed from one script into
another. The copies drift. Often neither is obviously wrong; they simply answer slightly different
questions.

## Where it bit

Upstream typed the declares-a-gate alternation twice and the two disagreed on scope: the shell
grepped the whole file while the module searched only the body, so a description carrying the word
gated satisfied one and not the other. Upstream also transcribed a byte-capped index set from shell
into Python and had to guard the transcription in BOTH directions, because a shell-side addition the
Python side still excluded left a file under no cap at all.

Here, `tools/memory-tree/SPEC-TEMPLATE.template.md` described a nine-section canon while the
installed copy and the gate had required ten for four days. Nothing connected them.

## The fix

Ask, do not copy. `tools/memory-tree/check-memory-hygiene.sh` owns the append-only set and the index
set and prints them on demand; `tools/memory-tree/corpus_ids.py` asks. The id grammar lives in
`tools/memory-recall/extract.py` and is imported. `tools/memory-tree/gotchas.py` exposes a single
declares predicate. Where a fact genuinely has two possible sources — a build status derived from
specs versus declared in front matter — one is an ERROR whenever the other is available.

Gated by `tools/memory-tree/kit-dogfood-parity.test.sh` for the document pair, and by construction
elsewhere: the second copy does not exist.

## The acute form — a multi-carrier fix that lands at one carrier

The section above is about copies drifting over TIME. There is a faster version: copies drifting
during the very edit meant to converge them. A review finding names three carriers of one fact and
says "at all three sites"; the fold edits the site the finding QUOTED and not the ones it merely
LISTED; the finding is marked resolved. Before the fold the copies agreed and were wrong together,
so a reader had one answer. After it they disagree, and the reader must adjudicate a conflict
nobody flagged.

Hit hard on `TOOL-aScannedThrottle-1`, round 2 of its closing diff review, 2026-08-21: **eight of
eighteen defects were this class**, two of them highs, in a fold whose whole purpose was applying
round 1's findings. One finding named three carriers of a floor figure and two moved. One said a
backlog row lacked a disposition; the fold added the row to the report's table and never touched the
backlog, which is where the build's own closing condition reads.

**The fix is to grep for the FACT, not for the finding.** Take the distinctive substring of the
value being corrected and grep the whole tree; that set, not the Site line, is the edit's scope. A
reviewer's site list is a sample, never an enumeration. Then grep again for the OLD value after the
edit, and require an empty result or a named reason for each survivor — the same discipline as
running a candidate gate predicate over the real tree before wiring it. Where the correction is
prose rather than a value, replace the copy with a pointer: the copy that does not exist cannot be
half-fixed.

**No machine gate** — this is a documented check. The mechanical form would be a
`multi-site-fix-parity` leg reading a review record's site list against the commit that claims to
resolve it; it is unbuilt, its failing case has not been observed, and a gate nobody has seen go red
is an assertion about nothing. Tracked as `TOOL-aScannedThrottle-9`.
