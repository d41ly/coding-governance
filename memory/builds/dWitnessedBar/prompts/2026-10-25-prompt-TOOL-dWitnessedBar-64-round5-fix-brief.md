**Serves:** research TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65

# Round-5 fix brief — units 64 and 65's path hits, before the round-6 audit

The round-5 spec audit's disposal wrote TOOL-dWitnessedBar-64 and -65. Clear the spec-token hits below, changing
nothing else, so that the main loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit and
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` stays clean.

- Both units are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. Touch no other spec and
  no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role admits the
  hygiene gate and the lexicon only.
- Report the byte count of TOOL-dWitnessedBar-51 (you do not edit it).

## The hits

- **[path]** A §6 criterion spells, in backticks, the full path of a file this build or a parent will CREATE, which
  is not tracked at HEAD (`tools/lib/legacy_ledger.py` in unit 64, `tools/run-gates/verdict_backends.py` twice in
  unit 65). In §6, cite each by its basename (`legacy_ledger.py`, `verdict_backends.py`), keeping the full path in
  §2, §4 and Files touched; a command that reads it takes it as an argument.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-64.md [path] `tools/lib/legacy_ledger.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-65.md [path] `tools/run-gates/verdict_backends.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-65.md [path] `tools/run-gates/verdict_backends.py` — not tracked by git ls-files
