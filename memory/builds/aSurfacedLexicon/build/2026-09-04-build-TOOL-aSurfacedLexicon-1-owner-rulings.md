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

*The mitigation is already in the design and should now be treated as load-bearing rather than
cosmetic.* The `PINS:` block is ROW-SHAPED — one row per cell — so it reconciles under this repo's
existing `merge.rows.driver` the way the backlogs do. A single `VERB_OFFENDER_PIN` scalar does not.
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

Thirteen, not eleven. U1–U11 stand as the research record has them, with U3 and U5 gaining the two
acceptance arms named above, plus:

- **U12 — the prefix/decorator selector** (Q10). Synthetic fixtures; no in-repo population.
- **U13 — a real shell parser, arming `sh.function`** (Q5). The largest coverage gain, and the unit
  most at risk of being deferred indefinitely; the build should sequence it early or say plainly that
  it will not.

Q8's ruling settles the arithmetic but does NOT close the pressure-chain question: today's 3.6% is the
first of the two further readings the docstring requires, so a third reading is owed before
`TOOL-dScaffoldedMirror-4`, `-9` and `-11`'s cut fourth pin can be abandoned. The two prose copies and
`dScaffoldedMirror/README.md`'s "reading one of two" are superseded by the docstring and are corrected
under Q9's record (a).
