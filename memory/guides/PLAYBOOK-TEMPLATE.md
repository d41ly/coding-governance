<!-- gov:kit unattended@1.13 -->
# The playbook template — the canon a playbook is written from

A PLAYBOOK is the instruction set for making one KIND of thing repeatedly: articles, images, videos,
pages, sites, tests, plans. A run in `recipe` mode follows one to the letter and produces the number
of pieces the owner asked for. This file is the shape every playbook takes, and
`check-playbook.sh` grades a playbook against it.

**Copy the canon below, fill it, and freeze it.** The canon is CLOSED: twelve required sections in
order. A section that genuinely does not apply keeps its heading and carries the single line
`none — <why>`. That is a declared null and it PASSES; an EMPTY section reds, because an absent
section is indistinguishable from a forgotten one.

**Nothing here states a count of anything derived.** How long a segment may be, how many steps a
playbook has, how many of its checks carry a witness — the checker derives and prints every one of
those on each run. A number typed beside the thing it counts is wrong at the next commit and nobody
notices.

## Why a playbook is not a prompt, and not a spec

A prompt is consumed once. A spec describes one change. A playbook is READ AGAIN for every piece,
by a reader who has forgotten the last one — so it is written for re-reading, and the two properties
that follow from that are the ones most often lost:

- **It is SEGMENTED.** A pass reads the segment its step lives in and re-reads it per piece rather
  than carrying it forward. Instruction-following degrades with instruction-set length; the answer is
  not a shorter playbook, which would lose the negative knowledge that makes it valuable, but an
  addressable one.
- **It carries its own FAILURES.** Sections 10, 11 and 12 are where a playbook earns its keep. A
  playbook with no ruled-out list is a playbook whose next reader repeats the mistake that produced
  it.

## The declaration block

One fenced TOML block, immediately after section 1's heading. Every machine-read value lives here so
a reader sees the whole contract at once and the checker has one parse.

```toml
step_selector = ""   # a regex; every line it matches IS a step. You declare it because
                     # no two playbooks agree on what a step looks like, and a kit-fixed
                     # selector either misses your steps entirely — reporting "every step
                     # is tagged" over an empty set — or selects your prose.
step_floor   = 0     # shrink-only. The gate REDS when the selector matches fewer lines
                     # than this. It is what stops a selector that quietly selects nothing.
outputs      = []    # globs. Where pieces land. A `recipe`-mode run's diff may touch
                     # these and its own records, and nothing else.
grain        = ""    # a glob whose every MATCH is exactly ONE piece. Without it a piece
                     # count is unresolvable — three files can be one piece or three.
records      = ""    # where per-piece evidence records are written. DECLARED, because the
                     # governance tree's own structure is closed and a piece record is not
                     # a build record: it is evidence about content, and it belongs with the
                     # project that owns the content. Found by building — the first design
                     # put it under the build folder and the memory-tree gate refuses both a
                     # new subdir there and a new top-level directory.
piece_checks = []    # the checks that run over ONE piece.
set_checks   = []    # the checks that run over ALL N. See section 8; this is the one
                     # population a per-piece review structurally cannot see.
legs         = {}    # leg NAME -> something runnable: an argv, or a path that resolves
                     # in this repo. Every `GATE <leg>` tag names a key here.
coverage     = ""    # how completely `legs` can decide runnability. One of:
                     #   resolvable — every target resolves; a target that does not REDS
                     #   probe      — existence only; the incompleteness prints every run
                     #   dark       — a named refusal, never a silent skip
                     # UNDECLARED reds. A gate that quietly skips what it forgot looks
                     # exactly like coverage.
curated      = ""    # who ratified this playbook, and when. The freeze. Absent reds.
```

## The tag grammar — every step is `GATE` or `CHECK`

Each step carries exactly one tag, and the tag is the honest statement of what enforces it:

- **`GATE <leg>`** — a named machine check fails if you get this wrong. `<leg>` must be a key in
  `legs`, and the gate reds when it is not.
- **`CHECK <why>`** — no machine can see this, and `<why>` says why not. Optionally
  `CHECK <why> · witness <field>` naming the artifact that records the judgement.

**Write the witness where you can.** A process instruction that produces no artifact is followed far
less often than one that does — the difference is large and measured. The gate validates every
witness present and PRINTS the drain rate; it does not red on absence, so an existing playbook can
adopt this a step at a time rather than in one migration.

**An untagged step is a defect in the playbook**, and so is a `GATE` naming a leg that does not
resolve. Both red. The point is not tidiness: a step whose enforcement is unstated gets treated as
enforced by every reader who did not write it.

## THE EXEMPLAR RULE — read this before writing any example

**Every sentence quoted in a playbook as an illustration is PROHIBITED OUTPUT unless it is a tracked
fixture.** Mark it so, in the sentence itself.

This is the single most expensive lesson available here and it is measured, not preferred. In a
production corpus one checklist's own example phrase shipped verbatim in eight of nine finished
pieces; its model refusal in five of nine. **An exemplar in a checklist that N readers follow is a
template, whatever the surrounding paragraph calls it.** For a document whose entire purpose is N
pieces from one source, this is the characteristic failure, and every per-piece check is blind to it.

The same logic bans a DEFAULT in a closed vocabulary. Offer five registers with one marked default
and you will ship one register five times.

## The twelve sections

| # | Section | What it must carry |
|---|---|---|
| 1 | Identity and provenance | what this makes · the ratifying decision and date · links to the evidence · the `curated` line |
| 2 | Ground rules | the non-negotiable frame every piece inherits, and the lane it may not leave |
| 3 | Inputs and preconditions | what must exist before a piece can start |
| 4 | Outputs | where pieces land, what ONE piece physically is, and the grain that says so |
| 5 | The step checklist | the numbered steps, each tagged, in the order they run |
| 6 | The producer recipe | the scaffold and which slots vary; `none — <why>` where there is no fixed recipe |
| 7 | Per-piece checks | the passes over ONE piece, each with a binary anchored verdict |
| 8 | Set-scoped checks | the passes over ALL N |
| 9 | Declared gate legs | what each leg name in section 5 actually runs |
| 10 | Ruled out — do not re-try | what was tried, what it cost, who ruled, and when |
| 11 | Measured failure modes | failure classes with observed RATES, not impressions |
| 12 | Corrections to this file | this playbook's own prior claims, superseded, dated, attributed |

### On section 5 — step ids are LABELS, not ranks

A step's id is permanent. When the run ORDER differs from the id order, state the order and the
reason; do not renumber, because every record that ever cited a step id would silently change
meaning. Ordering has consequences worth stating: a compliance finding is a deletion and a style
finding is a restructure, so running compliance first certifies prose the style pass then rewrites.

### On section 7 — a verdict is binary, anchored and recorded

`PASS` / `FAIL` / `N/A`-with-reason. Never a 1–5: an undecided reviewer writes the midpoint, and the
score becomes a record of reviewer effort rather than of the piece. Never averaged into a composite,
because eight cheap passes must not drown the one failure that mattered. A `FAIL` quotes the span it
is about.

**Define `blocking` POSITIVELY and DERIVE severity.** A severity the reviewer picks freely, on the
pass they wrote themselves, is not a severity — measured once as fourteen FAILs, every one labelled
a nit, none blocking anything.

**A PASS must stay reachable.** A check that can never pass is as broken as one that can never fail;
it just fails in a way that looks like rigour.

**A check that has never once failed is decoration.** Track which of your checks have ever
discriminated. Rewrite the criterion, or retire it deliberately — that is a diffable admission
rather than a default.

### On section 8 — the population a per-piece review cannot see

Set-scoped checks run over all N at once. They exist because composition failures are invisible to
per-piece review, and that is structural rather than a lapse: a reviewer who has just spent an hour
inside one piece cannot see that its shape is the previous piece's shape.

The measured case: nine pieces, each reviewed carefully, each passing — and the nine together a
monoculture no single review could have caught. Repetition of a move, an argument arriving the same
way, a narrator with the same relationship to the reader twice.

**Measure the SHIPPED population, never the planned one.** A census over planned rows reported
healthy variety across pieces nobody had written, while every shipped piece carried one value.

`none — <why>` is legal here and is a real answer for a playbook that produces one piece ever. It is
rarely the right one.

### On sections 10 to 12 — the negative knowledge

These are what a playbook has that a prompt does not, and the first thing a hurried author cuts.

- **Ruled out** — each entry names what was tried, why it lost, who ruled and when. A rejected
  approach with no recorded test is indistinguishable from one nobody tried, and the next run pays
  to re-run it.
- **Measured failure modes** — rates, not impressions. "Three of eight failed on hands, and the
  failing three were all raised or unsupported hands" is actionable; "watch the hands" is not.
- **Corrections** — when this file was wrong, say so in it, dated, with the id that corrected it. A
  playbook that silently edits its own history teaches its readers that its claims are weather.

### The self-defending clause

Write one. A playbook accumulates helpful additions until it is an outline, and the additions are
each individually reasonable. Name the addition you most expect a later reader to make, and say in
the file that making it is a defect — so the sentence is read before the edit, not after.

## What the gate does NOT check

Stated here because a structural check reads as a semantic one to everyone who did not write it:

- whether a `CHECK`'s `<why>` is TRUE;
- whether a `GATE`'s named leg tests what the step says;
- whether a step followed in letter was followed in spirit;
- whether the playbook is right about its subject at all.

The gate reads SHAPE. Everything above is yours, and section 7's discrimination census is the only
quantitative handle on the third.
