**Serves:** research TOOL-dWitnessedBar-78

# Round-8 fix brief — unit 78's path hits, before the round-9 audit

The round-8 spec audit's disposal wrote TOOL-dWitnessedBar-74 to -78. Clear the spec-token hits below in unit 78,
changing nothing else, so that the main loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit and
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` stays clean.

- Unit 78 is uncommitted at rev-1 and unaudited: edit it in place with no rev bump. Touch no other spec, no `order`
  verb and no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role
  admits the hygiene gate and the lexicon only.

## The hits

- **[path]** A §6 criterion spells in backticks the full path of a file this build creates
  (`tools/run-gates/verdict_backends.py`), or a path inside a quoted Python literal (`open('tools/gate-legs.json'`,
  `open('tools/run-gates/verdict_backends.py'`). Cite a created file by its basename in §6 (a command over it runs
  in its directory), keeping the full path in §2, §4 and Files touched; pass a read file as an argument read
  through `sys.argv`, never inside the literal.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-78.md [path] `json.load(open('tools/gate-legs.json',` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-78.md [path] `tools/run-gates/verdict_backends.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-78.md [path] `print(e.scan_text_io(ast.parse(open('tools/run-gates/verdict_backends.py',` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-78.md [path] `tools/run-gates/verdict_backends.py` — not tracked by git ls-files
