# PLAY-dOrderedCharter-45 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-45

Each line is a probe this pass ran at rev-3 of the spec, from the worktree root with the pass applied:
`instructions_edit.py fixture --plant <case>` through a real `git merge` in its throwaway repository, and a
scratch probe that loads the driver and calls it directly and through its CLI. Unit 15 had already minted
`resolve_tables`, `TableConflict` and the `main` arm that catches it, in a thinner form, so this pass extended
them rather than adding them. The same probe over unit 15's driver reds at AC2 on `TOMLDecodeError`, and the
new arm's inputs red seven of eight cases there. The suite arm itself, its RED-first observation, the legs the
spec's section 7 names, the `gov_tag.py check` leg the role's scratch guard refused, and the merge bar are the
main loop's at the close. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-45
- AC1 — `python instructions_edit.py fixture --plant merge` printed `two branches' adds merge with both tags once` and `the table class ran and the row plane did not`; the scratch probe, wrapping the three functions, recorded `resolve_tables` alone, with `skeleton` and `resolve_rows` never called
- AC2 — `--plant merge-multiline` printed `edits around a string holding a header line merge clean`, `the output parses with no tag cut from the string` and `that unit's chunk is byte-identical to its side's`, over a `text` string holding a line reading `[[unit]]`
- AC3 — `merge-both-edit`, `merge-delete-edit` and `merge-edit-delete` each printed `is a whole-file conflict naming the tag`, the closing marker reading `table conflict: unit.unit.base`; `merge-same-add` printed `one tag added with the same bytes lands once`
- AC4 — `--plant merge-parse` printed `a side whose cut does not reproduce its parse fails closed with both sides`, `%A` holding both sides entire; the scratch probe also altered the merged text four ways between merge and re-read, and each was refused: `TOMLDecodeError`, `RowLoss`, `DuplicatedContent` and `StructureDrift`
- AC5 — `--plant merge-policy` printed two policy rows added on each side merge keyed by `key`, and both sides editing one row's `default` names `policy.<key>`, here `policy.adopter.one`, over the overlay's `[[policy]]` rows
