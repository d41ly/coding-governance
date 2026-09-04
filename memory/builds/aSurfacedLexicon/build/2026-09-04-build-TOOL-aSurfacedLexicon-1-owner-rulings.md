# The ten open questions, ruled

**Serves:** journal TOOL-aSurfacedLexicon-1

All ten questions in the research record's §8 were put to the owner on 2026-09-04 and all ten
resolved. Six took the recommended default; **four went against it**, and those four are written up
with their consequences rather than their arguments — the argument was had, the owner ruled, and a
record that re-litigates is worse than no record.

## The rulings

| Q | Ruling | vs recommended |
|---|---|---|
| Q1 | Keep both P1 pins — gate reach unchanged at 461 | as recommended |
| Q2 | **Full two-sided equality: a FALLING pin count reds** | **override** |
| Q3 | Ship `py.file` armed at 7; renames are their own unit | as recommended |
| Q4 | Build the owner-declarable `PATTERNS:` block (U8) now | as recommended |
| Q5 | **Arm `sh.function` — but only after a real shell parser exists** | **override** |
| Q6 | **Arm `py.constant` on the 331 public population** | **override** |
| Q7 | AMBIGUOUS reds, with a message distinct from VIOLATION | as recommended |
| Q8 | `drift_report.py` is the sole carrier; one more reading owed | as recommended |
| Q9 | Write all three owed records | as recommended |
| Q10 | **Build the prefix/decorator selector in this rebuild** | **override** |

## The four overrides, and what each costs

**Q2 — the ratchet becomes real.** The pin must now EQUAL the count in both directions, so a correct
rename blocks the bar until a second commit edits the scalar. The measured hazard is concurrency: two
nodes each draining one name produce a conflicting single-line edit in a shared mutable value, and
§3 says shared mutable files reconcile additively, which one scalar cannot.

*The mitigation I wrote here first was FALSE, and the spec pass caught it.* This paragraph claimed
the row-shaped `PINS:` block "reconciles under this repo's existing `merge.rows.driver` the way the
backlogs do". It does not, and both halves fail. `git check-attr merge -- .lexicon.conf` reports
`unspecified`, because `.gitattributes` wires that driver for `memory/DECISIONS.md` and
`memory/backlog/*.md` and nothing else. And even if it were wired, `merge-rows.py:252` defines a row
as `^\s*[-*]\s` — a markdown bullet — so an indented conf row is STRUCTURE to that driver, not a row.
The claim was reasoning from a shape rather than from the attribute, which is the error this repo
files under two-answers-to-one-question, committed by the record that rules on it.

*What is actually true, measured rather than reasoned.* Git's ordinary text merge already reconciles
the block when rows are SEPARATED: two branches each draining a different cell merge at rc 0 with a
blank line between rows, and at rc 1 with one conflict marker when the rows are dense and adjacent.
So the row shape does buy the concurrency property Q2's ruling needs, but it buys it from the text
merge and from a deliberate separation, not from a driver. `TOOL-aSurfacedLexicon-4` carries the
three options as its fork F1, each measured against a real merge, and AC5 is a standing selftest arm
that performs the merge including the adjacent-row case rather than asserting the property once.
Q2's ruling therefore makes the per-cell pin block a REQUIREMENT of U3 rather than a convenience, and
U3's acceptance check gains an arm: two branches each draining a different cell must merge clean.

**Q5 — `sh.function` is blocked on a parser nobody has scoped.** The practical effect today is that
shell stays dark and `sh.file` stays armed, which is the same posture as the recommended default. The
difference is the commitment: a shell-parser unit joins the build rather than the question being
closed. Shell is 79 of the 80 unarmed definition-carrying files here, so this is the largest coverage
gain available — and it is also the unit most likely to be the one that does not get built. It is
recorded as owed, not as done.

**Q6 — `py.constant` arms on the self-selecting population.** The 331/331 result is clean because the
predicate chooses the names it grades: "public module-body simple assignments" is a rule that excludes
the assignments most likely to violate. Both other readings carry real violations (539/419 and
432/413).

*The mitigation, and it is not optional under this ruling.* The per-cell report must print the
population RULE beside the count, not the count alone — `py.constant  screaming  331 graded of 539
module-body targets (rule: public simple assignments)`. A cell reporting `331 · 0 violations` with no
denominator context reads as coverage; the same cell reporting what it excluded reads as a scope. That
line is what keeps this ruling honest, and it belongs in U5's acceptance check.

**Q10 — the selector joins the build.** Prefix and decorator routing sends a subset of a cell's
population to a different convention, which is what lets Go's export rule and React's PascalCase
components be graded rather than declared dark. It also grades the 31 `cmd_*` subcommand handlers and
the 106 `test_*` arms without inventing surfaces for them. The cost is scope: a rebuild at 11 units
goes to 13 with this and the shell parser, and the selector is the one mechanism here with no
in-repo population to test against — its fixtures will be synthetic, and the record should say so when
they are.

## What the unit count now is

Thirteen build units, plus the research unit that produced this record — and the ids are NOT U1–U13.

`TOOL-aSurfacedLexicon-1` is this research and design pass, and it is merged in three commits. The
thirteen build units are therefore `-2` through `-14`, decided by section 2's residual tie-break
rather than by preference: the later-to-merge re-mints its UNMERGED ids and an already-merged id
wins. The specs were written as 1–13 and renumbered before landing. Two further rows were filed as
`-15` and `-16`, being Q3's rename unit and the unfiled review finding against the identifier
splitter, both of which the specs named and neither of which was anybody's unit.

The two units the overrides added:

- **`TOOL-aSurfacedLexicon-13` — the prefix selector** (Q10). Its routing half is exercised against a
  real in-repo population and its verdict half is not, so the component fixtures are synthetic and
  its spec says so in as many words.
- **`TOOL-aSurfacedLexicon-14` — a real shell parser** (Q5). The largest coverage gain here, and the
  unit most at risk of indefinite deferral; the build sequences it at order 4 or says plainly that it
  will not ship.

Q2's operator was owned by no spec when the thirteen were first written — four named its consequences
and none edited the comparison. It is now `TOOL-aSurfacedLexicon-4`'s S9, assigned rather than
escalated, because the owner had already ruled the behaviour and only the routing was open.

Q8's ruling settles the arithmetic but does NOT close the pressure-chain question: today's 3.6% is the
first of the two further readings the docstring requires, so a third reading is owed before
`TOOL-dScaffoldedMirror-4`, `-9` and `-11`'s cut fourth pin can be abandoned. The two prose copies and
`dScaffoldedMirror/README.md`'s "reading one of two" are superseded by the docstring and are corrected
under Q9's record (a).
