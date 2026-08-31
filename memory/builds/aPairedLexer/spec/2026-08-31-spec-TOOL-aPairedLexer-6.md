# TOOL-aPairedLexer-6 — a DECLINED slash announces itself, to BOTH views

**Status:** SPECCED · rev-5 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md) | spec-audit | TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md) | spec-audit | TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md) | spec-audit | TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

A `/` this file DECLINES as a regex start leaks the rest of the line into code mode. Two mis-lexed
backticks balance, `unterminated` stays false, `clean` stays true, and a raw `parallel(` between them
is blanked out of the view. Declining is defensible; declining SILENTLY is not.

Round-2 review **D3**. rev-1 fixed this in `renderCodeView` alone and claimed `blankLiterals` had
already been given the same half by `TOOL-aPairedLexer-4`. **That claim was false and the spec audit
measured it**: `dirty = true` occurs exactly ONCE in the file, in the unpaired-quote branch, and
never fires on a declined slash. Rules 3 and 5 gate on `blankLiterals.clean`, so rev-1 widened a
population those rules never read — adding exactly ZERO where it mattered while its precision cost
was real. rev-2 puts the signal in the SHARED predicate and routes BOTH views through it.

## 2. Scope (IN)

- **S1** — both `renderCodeView` and `blankLiterals` consume `TOOL-aPairedLexer-8` S3's LEAK report
  and set a per-line `dirty` from it. Neither computes the condition itself.
- **S2** — `renderCodeView` returns `unterminated: stack.length > 0 || mode !== 'code' || dirty`, and
  `blankLiterals` folds the same `dirty` into `clean`. Rules 1 and 2 fall back on the first; rules 3
  and 5 fall back on the second. **All four rules, or the fix is the defect it was promoted for.**
- **S3** — there is no opener set. `TOOL-aPairedLexer-8` S3 reports AMBIGUITY, not a leak, and this
  unit routes on that. The opener set is retired with the leak test that needed it — including
  `*/`, a CLOSER the predicate could never have reported.
- **S5** — arms pinning the SIGNAL per RULE, not per fixture.

## 3. Non-goals (OUT)

- Not changing which positions are regex positions — `TOOL-aPairedLexer-7` and `-8`.
- Not unifying the two scanners (`TOOL-aPairedLexer-5`), though S1 touches both.

## 4. Design

**The correction rev-1 needed is "both views", and the audit's better answer is "neither view".** The
leak question is answered once, in `-8`'s predicate, and both scanners read the answer. Two views
that must agree and compute separately are the shape that produced three of this file's four
fail-opens, and rev-1 reproduced it inside the build that promoted it.

**The condition is `TOOL-aPairedLexer-8` S3's, and this unit does not restate it.** A declined
slash sharing its line with a later slash IN CODE MODE reports AMBIGUITY; this unit routes on that
report and computes nothing itself. rev-4 left the retired opener/extent wording standing here, so §4
described a mechanism §2 had already discarded.

The per-line view this routes back to is the false-positive source `TOOL-aPairedLexer-2` was built to
remove, which is why the TOKEN reading is binding rather than the raw one: measured, the raw reading
routes 3 of this repo's 4 workflow harnesses — every hit the hook's own mandated marker-comment
idiom — and the token reading routes none of them.

**Ordering.** `-8` lands first: S1 consumes its predicate AND its `--selftest` seam.
`-7` may land with either.

**Fixture discipline, and it is the reverse of the sibling units'.** Every arm here needs a slash
`-8` DECLINES — one after `)`, an identifier or a number. A `return`-position trigger is DISSOLVED
by `-8` two steps earlier, so an arm written that way goes green with this unit unimplemented.
Units 9, 10 and 11 avoid triggers their siblings REMOVE; this unit must avoid triggers its
siblings RESOLVE, which is the same rule read from the other end.

## 5. Production-readiness checklist

- security — restores the fallback on a view that could be gutted, for ALL FOUR rules.
- perf / scale — one boolean per line; no change in cost class.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged.
- observability — a fallback is now REACHED where it silently was not.
- risks — routing to the per-line view costs PRECISION, and the audit measured that cost as real: it
  is the view whose false positives `TOOL-aPairedLexer-2` removed. The extent-scoped condition in §4
  is what bounds it, and AC6 is the control that pins the bound. This is stated against
  `blankLiterals.clean` and `renderCodeView.unterminated` BY NAME, because rev-1's risk line named a
  mechanism it did not actually widen.
- testing + left-shift gates — S5's one-arm-per-RULE shape; four fixtures of one shape is the
  instance arm that has now missed this four times.
- migration / rollback — revert restores the prior behaviour.
- user docs — `memory/map/features/agent-cap.md` gap list refreshed.

## 6. Acceptance criteria

- **AC1** — When a declined-slash phantom span wraps a raw `parallel(D.map(...))`, the hook exits
  `2`. Trigger-deleted control exits `2` too; the tip exits `0`.
- **AC2** — When the same span wraps `const v = byRef[finding.ref]`, RULE 5 denies: exit `2`, with a
  trigger-deleted control. Measured at the tip as exit `0` — rule 5 blind.
- **AC3** — When the same span wraps `boundedParallel(L.map(...), 500)`, RULE 3 denies: exit `2`,
  with its control. Measured at the tip as exit `0` — rule 3 blind.
- **AC4** — When the span wraps a rule-2 per-item fan (`D.map((d) => () => agent(d))` with no
  bounded receiver), RULE 2 denies, with its control. AC1–AC4 are one arm per RULE, which is the
  class arm.
- **AC5** — When the declined slash carries `/*` rather than a backtick
  (`if (a) /x[/*]y/.test(s)` … `if (a) /z[*/]w/.test(s)`), the hook exits `2`. Measured at the tip
  as exit `0`: no backtick appears anywhere, so rev-1's condition never fired. Table-driven over the
  opener set, one row per opener.
- **AC6** — When a script carries ordinary DIVISION twice on one line together with a lens prompt
  naming a primitive, it exits `2`. **This is a RE-BASELINE and the cost of the §8 resolution**:
  rev-2 and rev-3 both wrote this fixture as an ADMIT control, and the audit measured that the
  admit and deny shapes are indistinguishable. The fail-closed answer is the one this file's own
  rule requires, so the script denies and §4 names the class of legal script that now does. A
  criterion that cannot fail was the alternative, and this build has shipped four of those.
- **AC8** — When `renderCodeView` is called through that seam on a declined-slash-plus-backtick line,
  `.unterminated === true`; and `blankLiterals` on the same line gives `.clean === false`. Both
  asserted, because the two answering differently is the defect rev-1 shipped.
- **AC9** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is
  green after it.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`,
`bash tools/check-kit-versions.sh`.

## 8. Open questions

none — AC6 decides the precision question the audit raised, in the DENY direction, which is the cost
of `TOOL-aPairedLexer-8` §8 F1 and is recorded there. rev-4 said ADMIT here while AC6 denied.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D3.
- rev-2 · 2026-08-31 · folded spec-audit findings 26, 1, 36, 18, 4, 38, 3 and 30. The rev-1 premise
  was FALSE — `blankLiterals` never had a declined-slash `dirty`, so patching `renderCodeView` alone
  left rules 3 and 5 with the identical fail-open and widened their gate by zero (26, 1, 30). The
  condition keyed on a backtick and missed the `/*` opener `TOOL-aLexedStripper-5` names (36, 18).
  Four criteria across the set called internal functions with no seam to call them through, so S4
  adds one (4). The precision claim was false against the tip it lands on, so §4 scopes `dirty` to
  the declined span's extent and AC6 pins the control (38, 3).
- rev-3 · 2026-08-31 · folded round-2 audit B2, B4 and H5. B2: the seam moves to `-8`, which lands
  first and needs it for its own criteria — rev-2 put it here at order 7 behind two units that
  depend on it. B4: no fixture-discipline paragraph, and the arms' trigger was the return-position
  span `-8` dissolves, so all four class arms would have gone green with this unit unimplemented.
  H5: AC6's precision control had no later slash on its line, so the leak test could not fire on it
  under any reading — a control that could not fail, in the unit whose subject is exactly that.
- rev-4 · 2026-08-31 · folded round-3 B2 and the `*/` high. S3 loses its opener set entirely:
  `TOOL-aPairedLexer-8` §8 resolves the fork toward reporting AMBIGUITY, so there is nothing to
  enumerate and the `*/` closer the predicate could never report goes with it. AC6 is RE-BASELINED
  from admit to deny, which is the honest cost of that resolution and is named as such in §4.
- rev-5 · 2026-08-31 · folded round-4 B2. §4 still stated the retired opener/extent routing
  condition after §2 discarded it, and §8 read ADMIT while AC6 denies. Both corrected, and the token
  reading is named as the one that makes the cost bearable.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "lexing javascript source into a comment-free code view
for a static guard"` and `python tools/memory-recall/query.py` with terms `agent-cap fanout regex
literal division blankLiterals renderCodeView fail-open lexer prev token stripStrings capFindings
unterminated`, both run 2026-08-31.

**The seam this unit extends is `TOOL-aPairedLexer-8` S3's predicate**, which is where the leak
question is answered once for both callers. rev-1 claimed to extend `blankLiterals`' existing
`dirty`/`clean` pair; the audit measured that pair as covering only the unpaired-quote branch, so
that citation was wrong and is corrected here. `TOOL-aLexedStripper-5` is cited by `-8` §10 for the
`/*` opener.
