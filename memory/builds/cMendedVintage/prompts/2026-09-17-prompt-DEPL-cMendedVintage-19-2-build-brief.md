# Build brief — DEPL-cMendedVintage-19

**Serves:** journal DEPL-cMendedVintage-19

Read the spec whole first. It opens by catching a claim another unit's spec made that the engine
cannot produce, so part of this unit's job is making a documented sentence true.

*Standing note: nineteen briefs in this build carried a figure or mechanism measurement disproved,
and every one of the last twelve units amended its own spec mid-build after measuring. The last one
found its own S4 wording would have stayed green over the exact defect it was written to close.
Treat this as evidence, not authority.*

## S3 is the guard, and widening it is the failure mode

The schema-1 disagreement refusal is KEPT for `schema < 2` alone. A schema-1 role is untrusted for a
different reason and refusing is still correct there. S2's new disposition is the schema-2-and-up
answer, and the spec asks for TWO branches rather than one widened one — because a single widened
branch demotes a refusal that should survive. That is the same shape `TOOL-cMendedVintage-8` was held
to one unit ago, and the same shape `DEPL-cMendedVintage-18` just repaired.

Stage a schema-1 disagreement and confirm it still refuses after your change.

## What `role-moved` must NOT do

It writes nothing for that row and does not count it as a change. A disagreement is a descriptor
transition, not a byte question — so a run that reports one and then writes bytes anyway has answered
a question nobody asked. Report the old role, the new role and the path.

Two live adopters see this on their first update after this and `DEPL-cMendedVintage-6` both land,
so the wording is operator-facing: it should say what happened and what is now true, not name an
internal disposition and stop.

## The fixture must be an AGED receipt

S4's arm is built on a receipt that already exists carrying an `engine` row, with the descriptor then
edited to claim that destination as `project-owned`. A fresh install cannot reproduce it — install
and descriptor would agree by construction and the arm would grade nothing. This is the
fixture-passes-by-finding-nothing class, and your spec has already pre-empted it.

## The floor, conditionally

§7 says `refusal_join.py`'s `BRANCH_PIN` is re-derived in the same commit IF the branch split moves
the live count. It is 255 right now. DERIVE it from the engine's own output — do not type a number,
and do not raise it if the count did not move. `DEPL-cMendedVintage-14` correctly DECLINED a
conditional raise one unit ago because its change added no branch; declining with a reason is a legal
and preferred answer.

## Every line number in the spec is stale

It names `tools/govkit/govkit.py:5379`, `:5781`, `:5787`, `:6331` and `:6325`. Nine units have edited
that file since this spec was written, four of them within the last few hours. Locate every site by
symbol and by the text the spec quotes.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`, including helpers added to
`matrix.py` — that class has landed twice in this build, both in test-side helpers, and three specs
have since proposed names `--suggest` corrected. Spell no `tools/<kit>/…` path in shipped prose or
comments.

## Required of every unit

gov does not dogfood govkit and keeps no receipt of its own, so no criterion here is observable
against this repo. Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-19-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED.

**The ledger bullet shape.** `memory/HYGIENE.md` gives the form as `- AC1 — ``<token>`` — what was
observed`: the backticked witness on the bullet's FIRST line, immediately after the label. Check 23
reads form from that line alone, so a witness on a continuation line is graded `bad` however tidy it
looks — eleven criteria in this build failed exactly that way. The AMENDED form is
`- AC2 — amended rev-<n> — …` and carries no backtick. The token must share content with the
criterion's own backticked token, case-folded, either way round. Check 23 is HELD under `--staged`,
so no commit hook will tell you.

Re-declare with `--dispatch` if your write set grows; it refuses a declaration naming `RUN.md`. Bound
every command at 900s or more.
