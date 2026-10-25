**Serves:** research TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84

# Round-9 fix brief — units 83 and 84's spec-token hits, before the round-10 audit

The round-9 spec audit's disposal wrote TOOL-dWitnessedBar-79 to -84. Clear the spec-token hits below, changing
nothing else, so that the main loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit and
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` stays clean.

- Units 83 and 84 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. Touch no other spec,
  no `order` verb and no deviation record. Do not commit, do not stage, and do not run the build-index generator.
  Your role admits the hygiene gate and the lexicon only.

## The hits

- **[path]** A backticked token ends in a quote character, so the path arm reads a path no file carries
  (`tools/run-gates/run-gates.gov.test.sh'` in unit 83, `memory/guides/MERGE-BAR.md'` in unit 84). Move the quote
  out of the backticks, or pass the path as an argument, so the token is the tracked path alone.
- **[guards]** Unit 84's Files touched names `tools/gate-legs.json`, which trips the guard of the leg
  `run-gates canary`; add that leg to unit 84's §7 leg line.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-83.md [path] `tools/run-gates/run-gates.gov.test.sh'` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-84.md [path] `memory/guides/MERGE-BAR.md'` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-84.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
