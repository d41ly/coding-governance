**Serves:** research TOOL-dWitnessedBar-84

# Carry-forward H1 brief — unit 84's title row is over the index cap once DEFERRED

The spec run's carry-forward flipped every spec's Status from OPEN to DEFERRED, a status-only header edit the main
loop makes. That adds four characters to each row `gen_build_index.py` renders in
`memory/builds/dWitnessedBar/README.md`, and TOOL-dWitnessedBar-84's row is now 353 characters against hygiene check
7's cap of 350, so the carry-forward commit is refused. Shorten unit 84's H1 by at least 10 bytes, keeping the
`# TOOL-dWitnessedBar-84 — ` prefix with its em dash and the title's meaning.

- Unit 84 is committed and audited, and its Status line now reads DEFERRED in the working tree; keep that line as it
  is. Change the H1 line, and add one line to the spec's latest rev entry in §9 saying the H1 was shortened for the
  index row cap and nothing else moved. Do not bump the rev. Touch no other spec and no deviation record. Do not
  commit, do not stage, and do not run the build-index generator. Your role admits the hygiene gate and the lexicon
  only.
- Return the new H1 and its byte count.
