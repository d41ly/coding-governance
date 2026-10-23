**Serves:** research TOOL-dFairHearing-3 TOOL-dFairHearing-9

# Readers-fix brief — hygiene check 25 over the first spec pass

Hygiene check 25 (`memory/HYGIENE.md`, item 25, read it whole) refuses the first spec commit on three §2 scope items
that its trigger reads as retiring a named thing: TOOL-dFairHearing-3's S3 and S4, and TOOL-dFairHearing-9's S3.

- For each item, decide whether it does retire, rename or remove a named thing.
- If it does, add a `**Readers:**` clause to that item, with the literal `by name:` followed by every reader that spells the name, as backticked names that resolve in the tree, then the literal `by value:` followed by the readers of its value, or `NO VALUE READERS` and a reason. Find the readers by grep, not by recollection.
- If it does not, and the trigger fired on a verb beside an identifier-shaped token, reword the item so it states what it adds or changes without a retirement verb. Change no meaning.
- The specs are uncommitted at rev-1 and unaudited, so edit them in place with no rev bump.
- Change nothing else. Do not commit, do not stage, and do not run the build-index generator or the hygiene check; the main loop runs it.
- Report, per item, which of the two you did and why.

The refusal, verbatim:

- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-3.md (§2 items that retire a named thing carry no **Readers:** clause): S3, S4
- memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-9.md (§2 items that retire a named thing carry no **Readers:** clause): S3
