**Serves:** research TOOL-dWitnessedBar-97

# Round-14 H1 brief — unit 97's title row is over the index cap

TOOL-dWitnessedBar-97's H1 is 293 bytes, so the build index row `gen_build_index.py` renders for it in
`memory/builds/dWitnessedBar/README.md` is 380 characters against hygiene check 7's cap of 350, and the round-14
commit is refused. Shorten the H1 to at most 255 bytes, line included, keeping the `# TOOL-dWitnessedBar-97 — `
prefix with its em dash and the title's meaning; the scope items stay as they are.

- Unit 97 is uncommitted at rev-1 and unaudited: edit it in place with no rev bump. Change the H1 line only. Touch
  no other spec and no deviation record. Do not commit, do not stage, and do not run the build-index generator.
  Your role admits the hygiene gate and the lexicon only.
- Return the new H1 and its byte count.
