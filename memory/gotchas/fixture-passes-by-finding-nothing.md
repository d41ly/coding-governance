---
name: fixture-passes-by-finding-nothing
description: a test arm whose fixture never triggers the rule passes, and proves nothing
kind: class
universal: true
---

# An arm satisfied by a fixture that does not exercise it

## Symptom

A red arm is green. Not because the rule fires, but because the fixture never produced the condition
the rule looks for, and the assertion was phrased so that absence satisfies it.

## Where it bit

The orphan-id arm in `tools/memory-tree/corpus_ids.py`. Its fixture put the orphan id in a backlog
row — but a dash-led id row IS an anchor, so the row DEFINED the id and the corpus had no orphan at
all. The arm asserted a message that never appeared, for a reason unrelated to the rule. Upstream
counted six probes across one session that reported success while exercising nothing.

## The fix

Every arm asserts the SPECIFIC message its branch emits, never a process exit code, and the fixture
is checked against the classifier before the arm is trusted — a report mode exists partly for this.

No machine gate: this is a review discipline, not a source-level pattern. The nearest mechanical
protection is that every arm names a branch message, so an arm whose fixture stops working fails
instead of passing.

## The sub-shape that recurs: the fixture trips an EARLIER guard

Measured four times in one build (`aPromptedMandate`, 2026-08-18), each time on a first attempt. The
fixture looks exactly like the failing state and never reaches the branch under test, because some
precondition ordered ahead of it refuses first:

- a README edited in the WORKING COPY, where the checker reads the blob at a pinned BASE — the pin
  does not move, so the edit is invisible and the arm reports nothing;
- a fixture authored on the UNIT BRANCH for a check that runs after the authorization, which refuses
  at `fail 6` before the region validation is reached;
- a re-run used to produce a disagreement between two facts that are both PINNED ONCE, so neither
  moves and no disagreement is producible;
- an arm asserting a sibling branch's message: the regression it guards emits a DIFFERENT string, so
  the arm is green over the broken implementation.

Two of the four were green-and-wrong rather than loudly missing, and one of those shipped into a
commit and was caught by a closing review rather than by the suite.

Two more from the same build, both in arms written to guard against this very class:

- **a boundary value that disables the instrument.** An arm forced its subject to time out with
  `timeout 0` — and a zero duration in coreutils means NO LIMIT, not an instant one. Measured:
  `timeout 0 sleep 2` exits 0, `timeout 0.05 sleep 2` exits 124. The control finished, the wrong
  branch fired, and the arm reported that its two outcomes were indistinguishable. It caught its own
  author.
- **a bespoke fixture where the suite already had one.** Arms hand-rolled their tree with the generic
  reset helper while a purpose-built helper existed two hundred lines up. The hand-rolled tree left
  the unit non-terminal and the roster region absent, so the positive arms measured those rather than
  the subject. Look for an existing `<subject>open`-shaped helper before building state.

**The tell** is that a passing arm and a never-reached arm look identical. So: break the subject
DELIBERATELY and watch the arm's own message appear, before writing the arm. If the refusal that
appears names something else, the fixture is testing that something else.
