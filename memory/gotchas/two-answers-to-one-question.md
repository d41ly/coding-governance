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

TOOL-dRenderedAnchor-1 changed the rule for an absent harness in the role render's docstring, the
roles README and `help/roles.md`, while `memory/map/features/roles.md`, the dossier claiming
`tools/roles/**`, still called such a harness a note, not a defect (its closing review round 1, L4,
id 11). TOOL-dRenderedAnchor-2 rewrote the map's rule in the same diff as the rule's final form. No
gate here compares a dossier's stated rule with the code it claims.

The same unit's `MISPLACED_LINE` said the harness `is installed`, and its comment and the help page
said `kit directory`, while the scan matched any directory under the tool root by file name alone
(L5, id 12). TOOL-dRenderedAnchor-2 wrote the predicate it ships, a file beside the harness's
template or a `kit.toml` declaring its home, into the line, its comment, the docstring, the README
and the help page together. No selftest matches the line's text, so no gate holds the wording to
the scan.

TOOL-dRenderedAnchor-2's `help/roles.md` listed two tools that print the missing-harness note,
`render_agents.py` and check-wiring's report, while `tools/roles/README.md` listed three, the
catalogue checker `check_roles.py` among them (its closing review round 2, L1, ids 2, 4, 6 and 11).
TOOL-dRenderedAnchor-3 named all three on the help page. No machine gate compares a help page's list
with the README's.

The same unit's help page and render docstring said a file of a harness's name beside neither mark
of its kit is the adopter's own, and the README and the map said so too, while the scan establishes
only that it is not counted: `unattended-unit.js` ships with no template, so a copy-install that
pruned its `kit.toml` holds the kit's own file there (round 2, L7, id 13). TOOL-dRenderedAnchor-3
wrote what the scan counts into all four. No machine gate compares a page's account of a
predicate's outcome with the predicate.

TOOL-dRenderedAnchor-3's `help/roles.md`, `tools/roles/README.md` and adopter header said a file at
the repository root never answers a citation that is no harness, which holds only at a prefixed
install: at a root install the tool root is the repository, so the kit directory's second probe
reaches that file (its closing review round 3, L1, ids 4 and 6). `TOOL-dRenderedAnchor-4` wrote "at
a prefixed install" into those three and into arm 15's comment in
`tools/roles/adopt-roles.test.sh`. The check: a docs claim about resolver reach states the install
shape it holds for.

The same three carriers and the `resolve_cited_paths` docstring in `tools/roles/roles_lib.py` said
"a harness of the workflow table", while the predicate that ships keeps only a `workflow` driver and
the table's merge bar is a `program`-driver harness (round 3, L2, id 7). `TOOL-dRenderedAnchor-4`
wrote "a `workflow`-driver harness of the workflow table" into all of them and arm 15's comment, each
on one line: the phrase had wrapped at the help page and the adopter header, so the review's own
one-line grep could not see those two carriers.

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

## The roster form — a hand-kept Status column beside the generated one

A build README carries two tables of its units: the authored `roster:units` table, which plans
them, and the generated `build-units` region, which `gen_build_index.py` renders from each spec's
status header. In `aLevelledCopy` the authored roster carried a Status column that read OPEN while
the generated table beside it read CLOSED rev-2, and the closing review found it (L4, finding id 18).
An awk walk of every `memory/builds/*/README.md` on 2026-10-09 found 31 of the 144 authored rosters
carrying a `Status` header, so the shape is common rather than one build's slip.

**The check:** write no status into an authored roster. The generated `build-units` region IS the
status, and a column beside it is a second answer that is right only on the day it was typed.

**Why it is not gated** (`TOOL-aLevelledCopy-9` §8 F3): refusing the column in the index generator
would red 31 landed READMEs or need a new cutoff key, which is a memory-tree kit change and its
version bump, outside the unit that found it. This record is the left-shift until a unit owns that.
