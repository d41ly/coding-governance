---
name: rationale-names-a-consumer-that-does-not-exist
description: a comment justifies a real invariant with a checkable reason that is false, so the maintainer who checks the reason deletes the guard
kind: class
universal: false
---

# A load-bearing invariant defended by a reason that is not true

## Symptom

A docstring or comment states an invariant AND the reason for it. The invariant is real and
load-bearing. The reason is checkable, and false — it names a consumer, a field, a format or a
contract that does not exist.

The danger is not the wrong sentence. It is that the reason is the only thing telling a future
maintainer whether the guard still matters. Someone checks the stated reason, finds it absent,
concludes the guard is vestigial, and deletes the protection for the reason that IS real.

An invariant with no stated reason is safer than one with a false stated reason: the first invites a
question, the second answers it wrongly.

## Where it bit

`tools/codebase-map/map_lib.py`, `render_comment_free`. The docstring said line count is preserved
"because the caller reports `file:line` and `symbols.json` is committed". Neither half was true —
both callers build rows of exactly `{id, kind, file}`, the committed `symbols.json` had no line
field, and nothing in the kit reported a line number anywhere. The claim was echoed twice more in the
self-test comments, so all three copies agreed with each other and none agreed with the code.

The invariant was genuinely load-bearing, for a reason stated correctly 160 lines away:
`JS_DEFINITION_RULES` are `re.M` anchored at a leading-whitespace escape and `enumerate_exports`
iterates `splitlines()` with `marker_re.match`, so collapsing two lines pushes the second definition
out of statement-leading position and it silently stops being found. That reason appeared nowhere in
the docstring or in the arm guarding it, so a maintainer had a guard, a false justification, and no
route to the true one.

## The fix

State the reason as a property of a NAMED mechanism in the same repo, in the place that owns it, and
only once. Where the reason is a consumer's requirement, name the consumer precisely enough that its
absence is greppable — then a stale claim is a failing grep rather than a plausible sentence.

Do not write the reason twice. The self-test comments repeating this one turned a single false claim
into three mutually-confirming ones, which is the shape that survives review.

## No machine gate

There is no machine gate for this class — a false rationale is well-formed prose, and deciding whether
a stated reason is true needs the reader to go and look. It is a documented check on the Tier-2
review checklist instead: a rationale asserting a fact about a CONSUMER gets grepped, once.

## The tell

The rationale is phrased as a fact about the system rather than about the code in front of you —
"the caller reports X", "the artifact is committed", "downstream needs Y". Those are the ones worth
checking, because they are the ones that rot when the downstream changes. A rationale about the
function's own mechanics cannot go stale without the function changing.

Related: [[amendment-leaves-its-other-half-standing]], where the surviving half is a clause rather
than a justification.
