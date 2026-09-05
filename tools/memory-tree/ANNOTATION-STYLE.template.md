<!-- gov:kit memory-tree@2.60 -->
# Annotation style — what a code comment that cites a record must carry

## A1 — What this is, and what it is not

The convention for a comment in product source that points at a governance record — a unit id, a
decision, a measured incident. It is a WRITING convention. Nothing grades it, no grammar defines it,
no marker declares it, and no gate reads it. Every one of those was designed and refused on
measurement in the build that produced this file; that build's record owns the numbers and this file
does not repeat them.

It restates nothing another file owns. The id grammar belongs to the recall extractor, where your
memory tree ships one. The ban on writing a derived count into prose belongs to the governance
charter. The measurements behind every claim here belong to that build record. Each is named; none
is copied. A second spelling of a rule is how the first one rots.

## A2 — Annotation is VOLUNTARY, and that is load-bearing

No rule requires a comment to cite anything, and this file does not add one.

The reason is not modesty. A repo whose records are cited from source can ask whether a unit
shipped, by looking for its id in product code — and that question only discriminates while citation
is SPARSE and LATE. Make citation mandatory and every unit is cited the moment it is written, so the
signal answers "was this specced" instead of "did this ship" and stops being worth reading. A
mandate would also need a marker to filter on, a grammar to define the marker, and a gate to enforce
the grammar, none of which exists.

So the rule is: cite when the pointer earns its place. Then write the comment so it survives losing
the pointer, which is what the rest of this file is about.

## A3 — MUST / MAY / MUST NOT

**MUST carry the counterfactual.** What was tried, or what the obvious reading would do, and what it
actually did instead. A comment that only restates the code is the code again, at twice the
maintenance cost.

**MAY carry:**

- the producing unit's id, as a TRAILING pointer;
- a clause naming what the adjacent check does NOT cover, and the file that owns each such question;
- a deliberate-shortcut marker with its ceiling and its upgrade path;
- a number, under exactly one of A4's three dispositions and no other.

**MUST NOT carry:**

- a present-tense count of a live derived population;
- a value another file declares;
- a restatement of the class its memory record already owns;
- a second spelling of a rule already spelled in the same file;
- an assertion with no observation behind it.

The last one is the one to re-read. "This is safe because X" with nothing that observed X is the
same defect as a gate nobody has watched fail.

## A4 — The three dispositions of a number in a comment

The charter bans writing a derived count into prose beside the source that owns it. Comments in a
healthy tree are nonetheless full of numbers, and the best writing in most trees is exactly those
blocks. Both are right, because a number in a comment is safe under three conditions and unsafe
otherwise. A number is:

- **FROZEN** by its conditions — the population, the sha, or the node and date sit beside it, so the
  figure describes an EXPERIMENT and cannot go stale. It stops being a claim about now.
- **GATED** by a pin — the number is a declared value some checker compares against, and the comment
  points at the declaration rather than restating the digits.
- **POINTED** at its owner — the reasoning stays in the comment, the digits move to the file that
  declares them.

Anything else is a present-tense count of something that moves, and it is wrong on the next commit
with nobody watching. That is the shape to look for when reviewing a comment that carries a figure:
not "is this number right today" but "what makes it still right in a month".

## A5 — The one-line test

**Delete the id, and the block must still be worth reading.**

That is the whole test. A comment whose value survives losing its pointer is a comment; one that
collapses to nothing was never annotation, it was a citation with prose wrapped around it — and it
is exactly the shape whose pointer can dangle for its entire life without anyone noticing, because
nobody was reading the id anyway.

Applied, it means the EVIDENCE is the required part and the ID is the optional pointer, never the
reverse. Write the incident, the control, the measurement. Then, if it helps a reader find more,
append the id.

The failure mode it catches, from a real repair: a sentence stating an incident, followed by a bare
parenthesised id and nothing else. The sentence was fine. The id had pointed at no record since the
day it was written, and the block read perfectly without it — which is precisely why the dangle
survived so long.
