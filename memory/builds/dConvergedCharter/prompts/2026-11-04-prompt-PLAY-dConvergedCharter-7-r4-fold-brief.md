**Serves:** research PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-40

# Fold brief — round 4 of the spec-audit chain, the retirement and move set (units 7, 9, 13, 17, 38, 40)

The round-4 audit came back CONVERGING with 1 blocker and 5 HIGHs, and the review loop holds until its confirmed
findings are folded. You fold the ones that touch units 7, 9, 13, 17, 38 and 40. A second writer folds units 11, 41
and 20 at the same time, so edit no spec outside your set; if finding 10's edge fix needs the reverse edge in unit 1,
make it there and say so.

Your findings: 4, 7, 17 and 33 (L1, unit 7's `SESSION-KICKOFF.md` readers), 8, 10, 14, 15, 16, 19, 26, 37, 38.

## How to fold

- The review is `memory/builds/dConvergedCharter/reviews/2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1.md`. Read each finding's full row in its Appendix and its section above (B/H/M/L heading); fold the fix the review judges SOUND, or a fix that closes the same defect more simply, and say which in your return.
- Findings 20, 25 and 27 were refuted: fold nothing for them. Where two ids share one heading, fold once.
- A finding naming several specs folds into EACH spec it names that is in your set (BUILD-METHOD M4).
- Each spec you edit takes one rev bump (status stays DEFERRED, base unchanged) and one section 9 line naming `2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1`, the finding ids folded and the sections touched.
- Fold tersely. The owner accepted unit 11's size (75.7 KB) on 2026-11-04, but every added sentence is unreviewed surface the next round reads: replace text where a fix changes a rule, never restate a rule beside its old form.
- Keep every `**Carries:**` pin, `amends` row and §3 edge reciprocal. A new departure from a clause is a deviation record under `memory/builds/dConvergedCharter/build/` in the existing records' grammar; take the next free number for that unit.
- Write nothing outside `memory/builds/dConvergedCharter/spec/` and `memory/builds/dConvergedCharter/build/`. Do not commit; the main loop commits.

## Checks before you return

- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exits 0 with no red on this build's specs.
- `python tools/check-spec-tokens.py` exits 0 (take rc from a plain run, not `--list`).
- No acceptance criterion names the bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run; a path a criterion names that does not exist at HEAD is cited by basename there.

Return: per spec, its new rev and byte size; per finding id, the spec(s) it folded into and one line on the fix; the hygiene and token exits.
