**Serves:** spec-audit TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-7

# Spec audit round 2 — the shell pin, the coupling nobody read, and a generated column that over-claims

Tier-2 spec audit, round 2 · 2026-09-05 · node `a` · build `aSurfacedLexicon` · streams tooling ·
designs only, no code exists yet.

Round 1 is `2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round1.md`: BLOCKED, 22 confirmed
findings — seven blockers, nine highs, five mediums, one low.

## Verdict: CLEAN WITH FIXES

**Confirmed-blocker count, by subject.** Unit 13: 4 to 0. Unit 14: 5 to 0. Unit 7: 7 to 0. Strictly
smaller and zero in all three, so the loop CONVERGED for each.

Twenty of twenty-two were closed by the fold and graded CLOSED by an adversarial verifier. Two were
graded HEDGED and both were closed in the single-writer pass that followed, together with three
defects the fold itself introduced.

## What this round was actually about

**Three of the seven blockers were one clerical fact.** Five of fourteen specs were never re-pinned
off the original base, three of them this batch's subjects. Their population figures were not merely
mentioned — they were embedded in acceptance criteria as PASS CONDITIONS. A correct implementation
would have failed on arithmetic, and the failure would have looked like a bug in the code.

**The fold found something the audit did not, and it is the largest number in the build.** Arming the
shell cell puts 608 shell function names in front of the verb predicate, and 508 of them lead with a
token the declared table does not carry — this repo's own test-harness idioms, `verb`, `fail`, `ok`,
`bad`, `mk`, `say`, `is`. The spec that arms shell had budgeted none of it.

**And that figure is an upper bound, which took a second pass to see.** It was measured with the
NAIVE same-line pattern, and the same spec's AC1 requires the parser's population to DIFFER from that
pattern's — a parser count equal to the naive count is a finding there, not a pass. So the population
that produced 508 is one the unit is committed to replacing, and pinning it would gate the regex the
unit exists to retire. The direction is measurable and only the direction: a heredoc-aware refinement
returns 336 rather than 608.

**A spec reasoned about a number a sibling owns more of than it does.** Unit 7 states the offender
scalar it hands on, enumerated the two units that move it, and never opened the one at the build
order immediately before it that moves it by two orders of magnitude more. The equality it wrote could
not pass at its own landing order. This is the same class as batch B's — a claim about a sibling
written without opening the sibling — and it is now the third round in which that class dominated.

## The one finding that outlives this build

**The generated build-order table's `Parallel` column asserts a property nothing checked.** It renders
`yes` for every step holding more than one unit, which is a statement about the step's CARDINALITY.
M6 permits concurrency only where disjointness is PROVEN. Step 5 holds two units whose Files-touched
tables both name the engine and the self-test, and the table says `yes` over them — and nearly every
unit in this build writes the engine, so the column is wrong precisely where a reader would use it.

The generator cannot see write sets. The unattended kit's `--dispatch` already records them per pass.
So the column should read from recorded dispatches or rename to something derivable. Filed as
`TOOL-aSurfacedLexicon-17`; both units concerned now pin the sequencing in their own specs, which is a
remembered constraint rather than a gated one and is stated as such.

## A new bug class, left-shifted

The unit 7 fold wrote a triple-backtick span INLINE in prose. The hygiene gate reads specs through a
line-oriented fence machine, so that one line opened a fence 106 lines from the end of the file and
silently truncated four sections out of the body it graded. The gate then reported three TRUE
consequences of the truncation — a heading-canon diff, a rev not logged, a §10 missing its evidence —
and never the truncation, while the file greps as complete.

Recorded as `inline-fence-swallows-the-rest-of-the-file`, claimed in the memory-tree-hygiene dossier,
with the parity check that finds it: count fence-shaped lines allowing leading whitespace, and an odd
count is an unclosed fence. The obvious `grep -c '^```'` misses it, because an inline span sits inside
wrapped prose and prose is indented.

## The limit of this round

Unchanged from batches A and B: every observed-RED obligation these specs carry is owed AGAIN at build
time against real code. Staged experiments were observed once by the agent that staged them. No
spec-audit round can pay that debt early.
