**Serves:** spec-audit TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4

# Spec audit round 2 — the fold verification, and the two defects the fold itself exposed

Tier-2 spec audit, round 2 · 2026-09-04 · node `a` · build `aSurfacedLexicon` · streams tooling ·
designs only, no code exists yet.

**Subjects**, at the revs this round measured: unit 2 at rev-3, unit 3 at rev-4, unit 4 at rev-6.
Round 1 is `2026-09-04-review-TOOL-aSurfacedLexicon-2-spec-audit-round1.md`, which returned BLOCKED
with 16 deduplicated findings — one blocker, ten highs, four mediums, one low.

## Verdict: CLEAN WITH FIXES

**What this round WAS, stated first because it bounds every claim below.** Round 1 was a four-lens
adversarial find with batched skeptics and a synthesis pass. Round 2 was NOT that shape: it was a
single adversarial verifier reading the folded specs against round 1's findings, re-running the
commands the folds claimed to have run, and re-deriving several conclusions independently rather
than re-running the fold's own command. That is a narrower instrument than round 1 and this record
does not pretend otherwise. It is the right instrument for the question round 2 asks — did the fold
close the findings or merely acknowledge them — and it is the wrong one for finding a seventeenth
defect of a kind no round-1 lens looked for.

**Result: all 16 findings CLOSED. None hedged, none untouched, none made worse.** The verifier went
looking for the hedge specifically, because a fold report is exactly the artifact that can be prose
dressed as a change. It is not: the blocker removed a scope item and its criterion outright rather
than annotating them, the two could-not-fail criteria were rewritten into ones that can fail, and
the refused name was changed rather than argued for.

**Confirmed-blocker count, by subject.** Unit 2: 2 to 0. Unit 3: 5 to 0. Unit 4: 6 to 0. Strictly
smaller in all three, and zero, so the loop CONVERGED for each.

## The two defects this round found, both introduced or exposed by the fold

Both are the `fold-text-is-unreviewed-surface` class — the fold's own fresh prose is where the next
round's findings are — and both were fixed in the same pass, as `rev-4` on unit 3 and `rev-6` on
unit 4.

**Unit 3 AC2 hard-coded a count its order-1 sibling falsifies.** The fold rewrote "its pin lines are
byte-identical" into "all three pin lines are byte-identical". `TOOL-aSurfacedLexicon-2` sits at the
same build order and deletes one of those pins, so the criterion is true on a tree where that
sibling has not landed and false where it has — an order-independent criterion turned
order-dependent by a word. AC1 already excluded that sibling by name; AC2 now does too, and states
no count at all.

**Unit 4 AC2 expected a guarded leg to red on a stage that cannot select it.** The bytes were
unchanged from rev-4, so the fold did not author this one — the fold is what made it wrong, by
establishing in the same revision that the `lexicon naming predicates` guard is
`tools/`, `skills/session-kickoff/`, `.githooks/` and `.claude/`. A conf-only stage therefore SKIPS
that leg, and a criterion phrased against it could never observe its own red: the identical shape to
the six criteria round 1 found that could not fail, surviving inside the revision that removed them.
AC2 now observes the command directly and names the unguarded path the conf actually reaches on the
bar, which is `lexicon wiring` shelling out through `adopt-lexicon.sh --check` to `load_conf`.

## Corrections this round made to round 1

Round 1 is not rewritten; these stand here instead.

- **Round 1's H2 fix named the wrong leg as unguarded.** It directed the adjacency invariant onto
  `lexicon naming predicates`, which is guarded. The genuinely unguarded lexicon leg is
  `lexicon wiring`. The fold corrected the placement and verified the path end to end: a conf-only
  parse failure exits `adopt-lexicon.sh --check` at rc 1.
- **Round 1's H5 survivor figure was short by one file and one line**, because its grep carried an
  extension allow-list. Over the tracked set with no such list the count is 36 across seven files;
  the seventh carrier is under `tools/workflows/`.
- **Round 1 hypothesised a registry-exempt route around the blocker; it works mechanically.** With
  the conf added to the govkit registry's exempt list and the widened guard both staged,
  `govkit selfcheck` exits 0. It was still rejected, on meaning rather than mechanics: that list is
  for paths gov deliberately does not ship, and this conf is the one file every adopter authors. The
  measurement is recorded in unit 4's Alternatives so a later reader does not re-derive it, and the
  door is documented as open if an owner ever decides the early signal is worth buying.

## The limit of this round, stated so a green row is not misread

The verifier edited nothing. The staged experiments the folds report — the govkit guard entry, the
registry exempt route, the AST-staged deletions, an appended declaration function — were confirmed
by reading the code that decides them and by exercising copies outside the tree, NOT by re-staging
them. The mechanisms check out. The staged reds themselves were observed once, by the folding agent,
and not independently re-observed here.

That matters because this build's own rules require a failing case to be OBSERVED before a predicate
lands. Nothing above discharges that obligation: it is owed again at BUILD time, per unit, against
real code, and no spec-audit round can pay it early.
