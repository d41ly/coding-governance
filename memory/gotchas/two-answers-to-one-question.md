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

## The prose form — a Skill that names a hook's behaviour

A rendered Skill or a template says what a hook DOES ("the deny refuses a resumed session's first
commit"), and the hook's own evaluation-order comment says the opposite (an absent card and a
replay-written one both ALLOW). Two answers again, and the prose copy is the one that rots, because
nothing byte-compares a sentence against a predicate. Hit on `tools/unattended/SKILL.template.md`
by the aReplayedCard closing review (F11): the Resume section claimed a backstop the shipped
`tools/hooks/scratch-guard.js` had resolved AWAY in its own spec.

**The documented check, since no gate fits a sentence:** a template or Skill that names a hook's
behaviour is graded by reading that hook's evaluation-order comment beside it, in the same review,
and the prose is rewritten to the contract the comment states — or the backstop is built as a
predicate change and the sentence follows the code, never the other way round.

**A live instance, retired by a pointer.** Round 3 of build `dPolishedVitrine`'s closing review
found the `brief-recorded` population stated three times, and one copy,
`tools/unattended/.unattended.conf.example`, had dropped the condition that HEAD must still bear
the finished claim out. The fold replaced that copy with a pointer to the protocol's
`BRIEF_RECORDED_CUTOFF` row, so it cannot be half-fixed again. The leg's header in
`tools/unattended/check-brief-recorded.sh` still states the predicate, because a gate's header says
what it checks; the row and the header are the two carriers left.

## The fixture form — four self-tests red on `main` at once

A self-test's fixture is a COPY of the contract it feeds the product, and a later unit that moves
the contract moves the product and its own arms, never the sibling suite's copy. Measured on
2026-09-21, six red self-test legs on `main`, four of them this shape: `tools/runlog/selftest.py`
carried the driver's run-state scaffold text from before `TOOL-aWokenSentinel-1` added the lease
sentence; two disposal doubles in `tools/workflows/unattended-build.test.sh` predated
`TOOL-cMendedVintage-19`'s `edges` and `placements`; `tools/check-playbook-parity.test.sh`'s
control fixture built no `skills/` tree, so the one pair `TOOL-aHonedRuleset-5` declared outside
`tools/` had no owning source; and `tools/govkit/selftest.py`'s "older vintage" fixture hashed
`tools/check-wiring.fragment.json` at a commit a month before `TOOL-aReplayedCard-2` put it in the
kit, recording the EMPTY blob as its identity, which govkit refuses. None of the four named the
unit that broke it, and each was green in that unit's own bar because the self-test legs are held
by default. Behind the govkit refusal sat five more of the same shape, invisible until it cleared:
two `2/2` counts typed beside a kit that had grown to three, a text arm naming a binding
`DEPL-cMendedVintage-13` had inlined away, a staged break that removed one guard after round 3
had removed the fallback the break relied on, and the `-18` sweep sitting past the exit of the
scratch it swept — grading 2 orders of the suite's 9 and, once moved, flagging a fixture the
`-14` arm requires.

**The check:** a unit that changes a contract another suite's fixture copies runs
`GATE_SELFTESTS=1` over the kits whose fixtures FEED the changed surface, not only the kit it
edited; and where the fixture can be replaced by a read of the product — the runlog scaffold can be
captured from the driver rather than retyped — it is.
