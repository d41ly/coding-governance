**Serves:** research PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-11

# The owner's two rulings after the spec run's landing, 2026-11-04

The spec run landed at `923954b61` and surfaced two decisions in its wrap-up. The owner asked for them ("put the
decisions to me") and answered both through the session's question tool on 2026-11-04.

## The spec-audit disposal's effort

Asked: "What effort should the spec-audit disposal stage run at? It folds findings into specs and promotes units;
finders, skeptics and synthesis already run at medium."

Answered: **Keep high.** The disposal stage keeps the roles kit's `high` for `disposal` (`handoff.py stage-efforts
spec-write`); the finders, skeptics and synthesizer stay at `medium`. The reason offered with the option: the disposal
writes spec text no audit reads until the next round, and fold text has seeded most of a later round's findings
before. Nothing changes in the roles kit.

## PLAY-dConvergedCharter-11's size

Asked: "PLAY-dConvergedCharter-11 is about 67 KB against the 49,152-byte spec ceiling (warn-only today). What should
happen before its build run?"

Answered: **Split in two.** The seam first offered (the house-file `[effort]` and `[gates]` fallback alone into a new
unit) was then measured at about 5 to 6 KB, which would leave unit 11 near 61 KB and still over the ceiling, so the
seam was put again.

Asked: "The house-file seam only moves ~5–6 KB, leaving unit 11 near 61 KB. Which split do you want?"

Answered: **Fold vs re-points.** Unit 11 keeps the fold itself: the catalogue rows, gov's values moved, the both-homes
reader, the red arm and `derive_readers`. A new unit, PLAY-dConvergedCharter-41, built after unit 11, re-points the
named readers: the four `read_policy_key` copies with their callers, `held_halves.py`, `transition_audit.read_modes`
and govkit's conf-key gap checks, with the house-file arm. Clause `cl-dClosedLoop-0485` is carried in two parts. Done
as an attended records change with a spec-writer pass, the two halves spec-audited because the README declares the
audit, and landed on the owner's ask.

## After round 3 of the spec-audit chain

Round 3's disposal took PLAY-dConvergedCharter-11 from 48,596 to 75,698 bytes; PLAY-dConvergedCharter-12 reads
49,217. Asked: "What now?" Answered: **Accept the size.** The ceiling stays warn-only for these units and no further
split is made.

`--chain-verdict` read CONTINUE for round 4 over ten units. Asked whether to run it. Answered: **Run round 4.**
