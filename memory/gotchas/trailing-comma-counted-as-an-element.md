---
name: trailing-comma-counted-as-an-element
description: a counter scoring one-plus-every-top-level-comma reads a trailing comma as a real item, so every multi-line literal measures one too many
kind: class
universal: false
---

# A trailing comma is not an element, and only the multi-line form knows

## Symptom

A counter reports one more item than the source contains. It is written as `1 + every top-level
comma`, which is correct for `[a, b, c]` and wrong for the same literal formatted across lines, where
a formatter leaves a trailing comma after the last element. The inflated count then either denies
something legitimate, or — far worse — is believed, and a limit is widened to accommodate it.

The single-line form counts correctly. That is what makes the class invisible: the obvious fixture is
the one-liner, it is green under the defect, and it proves nothing.

## Where it bit

Four times inside one unit, TOOL-aNumeralWarden-1, all from one root cause:

1. The call-site walk in `tools/hooks/agent-cap.js` split a prettier-formatted
   `boundedParallel(\n  LENSES.map(…),\n)` into two arguments and read the phantom second one as a
   cap argument of nothing. It denied `tools/workflows/tier2-review.js` — this repo's own review
   harness — on its formatting, not on its behaviour.
2. The array-literal element counter in the same file measured every five-element lens array as six.
   `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js` both ship exactly
   that shape, so both were mis-measured for as long as the counter existed.
3. **The inflated number became a CONSTANT.** `MAX_LENSES` was 6 because five lenses measured six —
   the limit had been widened to fit the miscount. A spec fork was then written asking why the lens
   allowance disagreed with the charter's 5, inheriting the wrong premise from the constant and
   recommending the wrong answer on it.
4. And that spec's own non-goal — "no code moves for this" — was false in consequence, and had to be
   amended after the fact.

Instance 3 is the expensive one and the reason this record exists. An off-by-one that is merely wrong
gets found and fixed. An off-by-one that gets NORMALISED INTO A CONSTANT stops looking like a defect:
it survives review, ships, and is then defended by the number it produced.

## The fix

One splitter, shared by every caller, and it drops a trailing empty segment: `topLevelArgs` in
`tools/hooks/agent-cap.js`. Both the argument walk and the element counter call it, so there is one
answer to "what is an element" rather than two that agree until a formatter runs.

The shape to refuse on sight is `n = 1 + count(top-level commas)`. Split, drop trailing blanks, take
the length.

## Detection

**The regression fixture must be the MULTI-LINE trailing-comma form.** A fixture built from the
single-line literal passes under the defect and under the fix alike — see
fixture-passes-by-finding-nothing, which is this failure one level up.

Assert BOTH directions, or the comma buys the extra element back:

- at the limit, written across lines with a trailing comma → must PASS;
- over the limit, in the same form → must still FAIL.

Gated by `tools/hooks/agent-cap.test.sh`, arms "rule2: five lenses, prettier-formatted with a
trailing comma" (allow) and "rule2: six lenses with a trailing comma" (deny). The single-line
six-element arm beside them is deliberately kept as the control: it passed before the fix too, and a
suite holding only that one would have proved nothing.
