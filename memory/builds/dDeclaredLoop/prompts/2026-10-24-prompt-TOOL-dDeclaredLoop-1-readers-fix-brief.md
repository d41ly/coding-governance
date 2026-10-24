**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29

# Readers-fix brief — hygiene check 25 over the staged dDeclaredLoop specs

Fix every hit `bash tools/memory-tree/check-memory-hygiene.sh --only 25` reports over the staged dDeclaredLoop
specs, so check 25 prints no dDeclaredLoop line, changing nothing else.

- Each hit is a §2 scope item whose words retire, replace, remove or rename a named thing. Read the item. Where it
  truly retires a name (a conf key, a function, a file, a field, a table, a literal), add a `**Readers:**` clause to
  that item in the grammar check 25 states: `by name:` then every reader that spells the name, by path, each found
  by `git grep -n` over the tree at HEAD; then `by value:` and the readers of its value (fixtures and asserted
  literals included), or `NO VALUE READERS` and a reason. Copy the shape of a passing clause, for example
  `memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md` S6, or the clauses already in
  TOOL-dDeclaredLoop-7 and -11.
- Where the item retires nothing (a planted case's "removed", a row the unit adds), reword the item so it no longer
  reads as a retirement, keeping its meaning; say which you chose in your return.
- The specs are uncommitted at rev-1 and unaudited, so edit them in place with no rev bump. Touch no deviation
  record and no other spec.
- Do not commit, do not stage, and do not run the build-index generator. Re-run check 25 (`--only 25`) and report its
  dDeclaredLoop lines (zero is the target).

## The hits, verbatim

- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-21.md: S7
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md: S6
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-29.md: S1, S6
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-4.md: S3
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-6.md: S1

Each reads: "§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and
the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason".
