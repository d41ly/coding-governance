---
name: a-pair-exists-and-it-is-the-wrong-one
description: a scanner that pairs a delimiter with the next one of its kind finds a pair for a delimiter that opens nothing, and the span it then blanks is where the defect hides
kind: class
universal: false
---

# A pair exists, and it is the wrong one

## Symptom

A scanner blanks quoted spans so prose cannot be read as code. It pairs a quote with the next quote
of the same kind on the line. Prose earlier on that line carries an apostrophe — `don't`, `won't`,
`it's`, `run 'em` — and that apostrophe pairs with the quote that opens a real string argument. The
span blanked between them is not a string. It is code, and it is the code the scanner was looking
for.

The tell is that a repair demanding a **matching pair** looks like it closes the class and does not.
An unpaired delimiter is one failure; a MISPAIRED one is another, and the second is invisible to
every fixture written for the first — because a fixture for "unpaired" carries exactly one quote, and
mispairing needs two.

## Where it bit

`tools/hooks/agent-cap.js`, the hook enforcing this repo's agent fan-out cap, in three of its string
views at once and defeating four of its five rules:

- rule 1 admitted a raw `parallel(` — `const re = /won't/; const r = await parallel([() => agent('a'), () => agent('b')])` exited 0
- rule 2's verifier-arity counter lost the `agent(` it counts
- rule 3 read a declared cap of `50` as the helper's default of `5`
- rule 5's ref-keyed-join ban stopped firing

Two closing-review rounds had already looked at that branch. `addc6169` repaired the unpaired case
and wrote *"needs a matching PAIR before it blanks anything, and so does this now"* — which was true,
and was the sentence that kept the class open for another release. The regression arm those rounds
left behind carries ONE apostrophe on its line, so it passes under the defect.

## The check

**Ask what the delimiter OPENS, not whether it has a partner.** A quote opens a string literal only
where one may legally begin: in JavaScript, never glued to the character that ends an expression, and
never after a bare word that is not a keyword. A partner test cannot reach that question.

Two consequences worth carrying into any scanner of this shape:

- **A fixture for "unpaired" does not cover "mispaired".** The mispairing needs a second delimiter on
  the same line, so the arm's name has to say SAME LINE and its fixture has to have two.
- **Correcting the pairing UN-HIDES everything else the wrong span was blanking.** Delimiters,
  comment openers and mode-switching characters all come back, and any consumer that reads across
  the line boundary — a paren balance, a bracket walk, a later comment strip — sees them for the
  first time. Three DENY-to-ADMIT moves were reproduced that way, by the fix, not by the defect. If
  the scanner's verdict matters, evaluate the rules over the OLD view as well and let a denial from
  either stand; that is monotone by construction and needs no argument about which characters moved.

Provenance: `TOOL-dMispairedQuote-1` and `TOOL-dMispairedQuote-3`, 2026-09-01.

Gated by `tools/hooks/agent-cap.test.sh`. The class arms are the ones named `mispaired quote: …`,
each carrying TWO quotes on the fan-out line and each with a control that removes the apostrophe;
`mispaired quote: SAME LINE is the load-bearing part` is the one that names the placement, because
the arm this class slipped past for a release put its single apostrophe on the line above. The
un-hiding half is gated by the `no-regress: …` arms and by the property arm over the tracked corpus.
