# cMendedVintage — the acceptance ledger for unit 22

**Serves:** journal DEPL-cMendedVintage-22

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every criterion below was observed by running the real verbs against scratch
fixture targets under the run's scratch root, twice: once against the engine as it shipped and once
against the engine as it now stands.*

## The one thing worth reading twice

**The wedge was reproduced end to end BEFORE anything was touched, and it is worse than the finding
reads.** On a fixture holding a manifest byte-identical to what gov itself wrote, a gov-side argv
change produced, in order: the drift refusal naming the leg, the WHOLE manifest withheld, the receipt
re-stamped with the same prior rows, a second run comparing identically, and
`apply`
refusing for the same reason. Six properties, all confirmed at BASE. After the change all six are
gone and the new row lands in both the manifest and the receipt.

**The other direction was confirmed in the same run and is the half nobody had ever seen.** A row the
fixture hand-edited was silently overwritten — the hand edit erased, the row replaced with gov's, and
a sibling row the target had removed re-appended — while the message that exists to report exactly
that printed nothing. Three properties, all red at BASE, all green now.

**The comment that admitted the gap is gone, not left standing.** The shipped suite recorded
*tampering the RUNNER changes neither side and apply silently repairs it* as a fixture inconvenience.
That sentence was true and was describing the defect. It is replaced by what is now true, with a
pointer to the block that arms the runner side, because an amendment that leaves its other half
standing has fired four times in this build already.

**Evidences:** DEPL-cMendedVintage-22

- AC1 — `update --target <fixture> --write` — a fixture applied at one vintage, committed, then
  hand-edited in its own manifest — a third element appended to the argv of a row gov owns — REFUSES
  with exit 1, naming the leg and the
  `differs from what the receipt recorded`
  text. Against the engine as it shipped the same fixture exited 0 and the hand edit was gone from the
  file, which is the red this criterion declares. A precondition asserts both gov-owned rows are
  present before the edit, so the arm cannot pass over a manifest that never held them.
- AC2 — `update --target <fixture> --write` — with the fixture's manifest left exactly as gov wrote
  it and the fixture GOV's descriptor edited to drop the third element, the run emits the new row and
  raises no drift. Asserted in three parts, because absence of a refusal is satisfied by a run that
  emitted nothing: no refusal text, the manifest row now carries the two-element argv, and the receipt
  records the vintage that is on disk. The new vintage comes out of the SAME gov checkout — applying
  from one scratch gov and updating from a second refuses upstream of this step, since the receipt's
  recorded gov commit does not resolve in another clone, and the first cut of these fixtures graded a
  run that never reached the legs step at all: three arms passed vacuously and the rest went red for
  a reason with nothing to do with gate legs.
- AC3 — `install.json` — when AC1's refusal fires, the target's manifest is byte-identical to the file
  the target tampered with and the receipt carries the previous emitted rows. Two constructions keep
  it from being vacuous. The sibling row the receipt still claims is DELETED from the manifest before
  the run, so a refusal narrowed into a per-leg skip would re-append it; and the tampered file is
  re-serialised at an indent the emitter never produces, so a rewrite that changed no row is still
  visible bytewise. Without either, a per-leg skip and a whole-manifest withhold produce identical
  bytes on this fixture and the criterion grades nothing.

## What was measured at BASE, property by property

Run against the engine as it shipped, on two scratch fixtures, before the edit:

- **W1** the new vintage is REFUSED as drift · **W2** the whole manifest is withheld · **W3** the
  manifest never moves · **W4** the receipt is re-stamped with the old rows · **W5** the second run
  compares identically · **W6**
  `apply`
  does not clear it either. All six confirmed. All six absent afterwards, with the new row landing in
  manifest and receipt.
- **T1** the tamper is refused · **T2** no leg reaches the manifest · **T3** the sibling is not
  re-appended. All three RED at BASE. All three green afterwards.

The harness that took those measurements is a throwaway under the run's scratch root. What ships is
the same pair of fixtures written into the suite against its own `check`, so the observations are
repeatable by the gate rather than by a script nobody kept.

## The staged breaks

The nine shipped arms were then run STANDALONE — cut out of the suite by line span as bytes and
exec'd against its own `check`, so what ran is what ships rather than a paraphrase — three times:
once clean, once per staged break. Each break is applied to a COPY of the engine the fixtures are
built from, and the substitution is asserted to have MATCHED, so a renamed or reindented target stages
nothing rather than passing quietly.

- **Clean** — nine arms, zero failures.
- **B1 — the shipped predicate restored**, both operands taken from gov again. SIX arms red: all three
  AC2 arms, AC1, and two of the three AC3 arms. Both preconditions stay green, which is what makes
  them preconditions. The one AC3 arm that stays green is the receipt-rows one, and that is honest
  rather than a gap: the shipped predicate overwrites the tamper without ever raising, so the receipt
  really does end up carrying rows equal to the previous ones. It is armed by B2 instead.
- **B2 — the refusal narrowed into a per-leg skip**, the `r.fail` dropped and the `continue` kept.
  AC1 and ALL THREE AC3 arms red, while every AC2 arm stays green — which is the shape the spec's own
  non-goal warns about, since a per-leg skip looks like a kinder fix and passes everything the gov-side
  half asserts. Both of AC3's constructions earn their keep here: without the deleted sibling and the
  foreign indent this break leaves the manifest byte-identical and all three arms pass.

## What did not run, and why

- **No merge bar and no `*.test.sh` suite ran in this pass.** The govkit self-test suite is this
  unit's own gate and the pass was told to run it; its verdict is in the return. The brief spells
  its invocation as a subcommand of the deployer, which the deployer rejects by name — it is a
  program of its own, run directly.
- **`govkit selfcheck`, the refusal join and the acceptance matrix are OWED** and are named in the
  return. Nothing in this unit adds or removes a refusal branch, so the join's shrink-only pin does
  not move; nothing here changes the repo shapes the matrix drives.
- **gov keeps no govkit receipt**, so no criterion here is observable against this repository. Every
  fixture is a throwaway target under the run's scratch root.
- **The lexicon gate did not run**, but both names this unit adds were put to
  `--suggest`,
  which is the authority: `read_leg_row22` and `read_emitted_rows22` each lead with a declared verb
  and satisfy `py.function`. Two definitions, zero verb offenders, so the pin does not move.

## Two notes on scope

**The predicate was fixed, not a descriptor.** The same mechanism was confirmed a HIGH as
`aPacedTurnstile` D3 and that repair went to the offending kit's descriptor row, so the class survived
and this build re-armed it by shipping another argv change. Nothing in this unit touches a descriptor.

**The runbook gained a short subsection rather than the single sentence section 5 named.** Same
content, one heading and one paragraph: a gov-side leg change is delivered rather than refused, and an
adopter must not answer a red leg by editing a row gov emits. No criterion changed, so this is
recorded here rather than as a revision. The open question's ruling is untouched — it asks whether the
refusal MESSAGE should name a remedy, and the message is byte-identical to what it was.

## The bug classes this unit was graded against

`assertion-between-two-derived-values` is the finding's own class and is what the change removes: the
comparison now has one operand from the target and one from the receipt.

`gate-you-have-only-seen-pass` is why both fixtures were run against the shipped engine first. Nine
properties were observed failing before any of them was made to pass.

`fixture-passes-by-finding-nothing` is why AC2 asserts the row LANDS and not merely that no refusal
printed, and why AC1 carries a precondition that both gov-owned rows exist before the edit.

`amendment-leaves-its-other-half-standing` is why the suite's fixture comment was rewritten in the
same commit as the predicate it describes.

`ledger-token-wrapped-across-a-line-joins-nothing` was checked rather than assumed: every backticked
span in this record sits whole on its own line.
