**Serves:** journal TOOL-aHoistedPass-6

# Brief — TOOL-aHoistedPass-6, folding round-1's BLOCKER plus findings 6 and 25


*What the round-1 fold pass was handed for this unit, recorded because "which instructions produced
this diff" must have an answer on disk rather than in a transcript nobody kept. The pass ran as a
subagent with write access to ONE file, concurrently with the sibling brief for
`TOOL-aHoistedPass-5`; the two write sets are disjoint by file.*

## The write set declared before dispatch

`memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-6.md`, and nothing else. In
particular NOT `tools/workflows/unattended-build.js`, which this spec describes and which the unit
will edit later, at its own build pass. Re-deriving an address is a READ.

`--dispatch` was NOT used to record this pair, for the reason the sibling brief gives: it grades a
BUILD pass against the declared order and this unit sits at `order 5`. A fold is not a build pass.

## The instructions

Fold three confirmed findings from
[the round-1 spec audit](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md),
one of them the round's only BLOCKER.

**Finding 31 (BLOCKER).** Section 4 addresses `tools/workflows/unattended-build.js` by `c4fcf5ad`
line numbers throughout, and the file has grown from 531 to 835 lines. The spans S2 names for
deletion now hold the AUDIT stage rather than the BUILD stage: at BASE `:485` is the audit-subjects
agent, the real BUILD agent is `:784`, `BUILD_SCHEMA` is `:298`, `const unbuilt` is `:804`. **A
builder following section 4 literally deletes the audit stage and leaves BUILD standing.** AC15 is
worse than stale — it runs `sed -n '276,277p'` and asserts a comment that lives at `:467-468`, so it
cannot pass however the edit is made.

Re-derive every address by opening the real file rather than trusting the reviewer's reading, restate
S2 by NAME, and replace AC15's line range with a grep for the comment's own text. Adopt the rule for
every citation touched: **cite by NAME, not by span** — an acceptance criterion is executable, so an
AC anchored on a line range rots between authoring and landing, in the one place where rot is graded
as failure.

Carry the reviewer's caveat forward as the pass's own: section 4's substance beyond the addresses was
never reviewed, because the blocker stopped it, and a corrected address set may change what S2
actually deletes. If it does, say so in the revision entry rather than forcing the old intent onto
new line numbers.

**Finding 6 (medium).** AC2 is an absence-only grep over four phrases, so DELETING the two surviving
sites satisfies it exactly as well as rewriting them does — while S3 exists precisely because those
two do not leave with the BUILD agent, and section 4 specifies positive replacement text for both.
Add a positive assertion beside AC2. A scope item specifying replacement TEXT may not be graded
solely by an absence assertion.

**Finding 25 (medium).** Section 4 books `memory/backlog/TOOL.md` in Files-touched and S1 through S12
file no row. Add an S13 naming the rows and an AC asserting each exists, or drop the file from the
table.

## The bounds it was given

- No commit, no `git add`, no `gen_build_index.py`.
- Bump `rev-3` to `rev-4`, date `2026-09-05`, leave `base c4fcf5ad` alone, append one revision entry.
- LF only; binary mode if edited through Python.
- **Keep the NARROWING of the pass-order claim intact and quotable.** Round 1's finding 41 is being
  folded into the sibling `TOOL-aHoistedPass-2`, which was going to STRIKE the same claim from
  `UNATTENDED-PROTOCOL.md:642`; the sibling is being corrected to match this spec's narrowing, so
  this spec must not switch to a strike. One build may not ship strike-and-narrow on one fact.
- Invent no measurement. Every address written must be one the pass opened.
