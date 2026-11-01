# dFoldedAudit — what the close owes, as the units report it

**Serves:** journal TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-7

Every unit's own return is recorded under `build/`. This record lists only what they hand to the close.

## Before the bar

- Observe every `New arm:` RED on its staged break and GREEN restored, in a scratch clone, and record both in that unit's acceptance ledger under a `Pass: none` commit (M8). Unit 7 holds seven arms, unit 2 ten, unit 3 five.
- Write `SPEC_FOLD_CUTOFF` in `.unattended.conf` to the day after the newest old-contract record, after the read of every ref that unit 7's §5 spells. `dTendedCadence` and `dScopedBuild` began 2026-11-01, so 2026-11-02 is the floor; re-read at the close.
- The harness and suite FLOOR figures units 2, 3 and 7 moved are COUNTED, not measured. The first suite run tests them.

## Findings for the closing review

- Lexicon pin: `lexicon.py --check` reports 1214 verb offenders over a pin of 1212. The two names this build's diff adds are `foldconf` (`tools/unattended/check-unattended.test.sh:486`) and `commit_fold_fixture` (`tools/unattended/unattended.test.sh:2503`), from TOOL-dFoldedAudit-2.
- `two-answers-to-one-question`: the severity and nature lists are spelled twice, in `DISPOSAL_SCHEMA`'s enums and `deriveDispositionFault`. Unit 3 tried to unify them after its CLOSED flip and the write gate refused.
- The `promote-all` prompt never says every entry is `new-mechanism`. An agent marking a promoted finding `local` is refused by rule 4 with a DEGRADED return, so the failure is loud.
- Three check 2 branches about the rescope acts carry no literal arm line in a `check-arms.py` probe. Unit 2 did not touch them; the `harness arms` leg judges them.
