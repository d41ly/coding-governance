**Serves:** research TOOL-dWitnessedBar-88

# Round-10 fix brief — unit 88's spec-token hits, before the round-11 audit

The round-10 spec audit's disposal wrote TOOL-dWitnessedBar-85 to -88. Clear the spec-token hits below, changing
nothing else, so that the main loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit and
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` stays clean.

- Unit 88 is uncommitted at rev-1 and unaudited: edit it in place with no rev bump. Touch no other spec, no `order`
  verb and no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role
  admits the hygiene gate and the lexicon only.

## The hits

- **[bar]** Two criteria of unit 88 name the suite `run-gates.gov.test.sh` as their observation. Observe the code
  the unit changes on a staged break, a `--selftest` flag or a fixture instead, and name the suite on a `New arm:`
  line in §7.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-88.md [bar] `tools/run-gates/run-gates.gov.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-88.md [bar] `tools/run-gates/run-gates.gov.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
