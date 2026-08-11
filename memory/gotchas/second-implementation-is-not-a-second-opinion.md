---
name: second-implementation-is-not-a-second-opinion
description: a gate that recomputes the driver's answer from the driver's inputs confirms it rather than checking it, and the same hole opens at the READ path
kind: class
universal: false
---

# Two copies of one computation agree; that is not verification

## Symptom

A tool decides something and a gate checks the decision. Both are written well, both are armed, and
the gate re-derives the answer **the same way from the same inputs**. When the inputs are wrong, the
gate computes the identical wrong value and *confirms* it. The bar goes green on exactly the state it
exists to catch, and it goes green loudly — with a passing check, not a skipped one.

Two shapes, and the second is the one that survives a fix of the first:

- **Shared INPUT.** Both read a value the subject supplies. Removing it from one and leaving it in
  the other is worse than either, because now they disagree silently.
- **Shared READ PATH.** Both establish "what the record said at commit X" by asking git. Hardening
  *which commit* X is does nothing, because the defeat is in what `git show X:path` returns.

## Where it bit

`tools/unattended/`, the run-authorization kit — twice, in both shapes.

The driver resolved a merge-base and the gate leg re-resolved it. Both read `GOV_DEFAULT_BRANCH`,
which the run process sets. Setting it to an unresolvable name did not make the gate *wrong*; it made
the gate **silent** — the candidate loop fell off the end with no `fail`, so the only BASE assertion
on the bar was switched off by one environment variable, and no arm noticed because every fixture in
the suite exported that same variable at setup.

Then the read path. Both sides established the mandate "as committed at BASE" with
`git show <base>:RUN.md`, which resolves through git's object layer and therefore applies
`refs/replace/*`. One `git update-ref refs/replace/<base> <a same-parent commit-tree forgery>` makes
that read return bytes the run authored seconds earlier — with the recorded base, the remote-tracking
ref and `origin/HEAD` all left honest, and the ancestry check passing on an affirmative **match**.
Every proposed hardening of the anchor left it open, because the anchor was never the thing being
attacked.

The same review found the marker grammar had a third instance of the pattern: `region()` identified
a marker with a **prefix** test and skipped the line, so text appended to the
`<!-- run:mandate -->` line was in neither extracted slice. Both sides compared byte-equal while the
sentence a human reads inside the block said something else entirely.

## The fix

- **Ask a different question, not the same question twice.** The gate's job is not to recompute the
  driver's value; it is to assert a property the driver's value must have — that the recorded base is
  an ancestor of the anchor, that the block at it is byte-equal. Independence lives in the question,
  not in a duplicated code path.
- **Enumerate who SUPPLIES each input**, and drop the ones the subject writes. See
  [[inputs-inside-the-subjects-reach]] for the enumeration discipline.
- **Neutralise the read path AND refuse its presence.** `GIT_NO_REPLACE_OBJECTS=1` disarms the
  mechanism for one process; a replace ref or a grafts file in a repo running the thing being
  authorized is *itself* the violation, and is refused separately. Doing only the first ships a green
  forgery to the next tool that reads the same objects.
- **A silent path in an authorization check is a disarmed check.** Every exit gets a named refusal —
  including "the input could not be resolved", which is the one that reads most like success.

## How to see it before shipping

Write the fixture where the subject supplies a hostile value, and assert the gate's output is
**byte-identical** to the same tree without it. "Both are green" is not that assertion: it also holds
when the check stopped running. And when a fixture must set a value for the gate to work at all, that
value is an input the gate depends on — check what happens when it is absent, because that is the
state a real adopter is already in. Related: [[assertion-between-two-derived-values]],
[[vacuous-selector-empty-population]], [[fixture-passes-by-finding-nothing]].

Gated by `tools/unattended/check-unattended.sh` — check 14 refuses a replace ref or a grafts file
outright, and check 9's exits are each a named refusal rather than a `continue` — and armed in
`tools/unattended/check-unattended.test.sh`, whose hostile-variable arms assert the gate's output is
byte-identical with and without the value, and whose replace-ref arm asserts the mandate comparison
still fires after the presence check does.
