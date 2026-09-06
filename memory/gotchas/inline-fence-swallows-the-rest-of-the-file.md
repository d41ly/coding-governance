---
name: inline-fence-swallows-the-rest-of-the-file
description: a triple-backtick written inline in prose opens a fence the reader never closes, so every section after it silently disappears from the checker's view
kind: class
universal: true
---

# An inline fence is a fence

## Symptom

A document passes every structural check until an author writes a triple-backtick span INSIDE a
prose line — quoting a command's output, say. Markdown renderers treat that as an inline code span
and the page looks right. A line-oriented fence machine does not: it sees a line matching
`^[[:space:]]*(```|~~~)`, opens a fence, and closes it only on a LATER line that matches the same
marker. Everything from that line to the next such line is dropped from the body it reads.

The failure is silent in the worst way: the checker reports a TRUE consequence of the truncation
rather than the truncation. A spec whose §7 through §10 vanished is reported as *sections differ from
the canonical ten*, with a diff showing four headings missing — so the reader goes looking for
deleted sections that are still there, in a file that greps as complete.

## Where it bit

A spec fold quoted a CLI's advice inline as ```` ``` use `seed_x` … ``` ```` on one indented prose
line. `tools/memory-tree/check-memory-hygiene.sh` reads specs through an unfenced-body machine, and
that one line opened a fence 106 lines before the end of the file. Check 12 then produced three
findings at once — a heading-canon diff, a *header rev not logged in the §9 Revision log*, and a §10
missing its reuse evidence — none of which named a fence, and all three of which were about
structure that was present and correct in the file.

Diagnosis went: read the headings (all ten, in order), diff the sizes, check for CRLF and a BOM
(clean), read the checker's diff logic, and only then grep for fence-shaped lines WITH leading
whitespace, which is what the earlier `grep -n '^```'` had excluded.

## The fix

Never write a triple-backtick span inline. Use single backticks for a quoted fragment, or a real
fenced block on its own lines. Where the quoted text itself contains backticks, paraphrase it.

## How to catch it

Parity, not eyeballing. Count fence-shaped lines the way the reader counts them — with leading
whitespace allowed — and an ODD count means an unclosed fence:

```
grep -cE '^[[:space:]]*(```|~~~)' <file>
```

There is **no machine gate** for this class today, and the parity count above is the documented
check. Nothing in the tree counts fence-shaped lines: the readers that tokenize fences each keep
their own machine and none of them reports an odd count, which is precisely why the truncation
surfaces as somebody else's finding.

Run it across the tree the reader scans, not only the file you edited: the same author habit repeats.
`grep -c '^```'` is NOT the same predicate and will miss the indented case, which is the case that
actually happens, because an inline span sits inside wrapped prose and prose is indented.

## The general shape

**When a structural check reports a surprising finding, ask what the checker READ before asking what
it CONCLUDED.** A reader with its own tokenizer — a fence machine, a heredoc scanner, a front-matter
splitter — can be handed a file that greps as correct and see a different document. The consequence
it reports is downstream of the truncation, so it points away from the cause every time.
