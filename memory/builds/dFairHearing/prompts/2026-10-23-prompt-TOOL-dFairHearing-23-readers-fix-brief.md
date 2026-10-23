**Serves:** research TOOL-dFairHearing-23

# Readers-fix brief — hygiene check 25 on TOOL-dFairHearing-23's S17

Hygiene check 25 (`memory/HYGIENE.md` item 25) refuses `TOOL-dFairHearing-23`'s S17. Its trigger reads the verb "deleted", beside the identifier-shaped token `refs/replay/<name>`, as retiring a named thing.

S17 retires nothing. It describes a transient ref that a replay creates and removes.

- Reword the phrase so that no retirement verb from the check's list (`tools/memory-tree/check-memory-hygiene.sh`, the trigger word list) sits beside an identifier-shaped token. For example, say the ref lives only for the bundle. The recipe's meaning must not change.
- Check every other §2 item of the spec against the same list while you are there.
- The spec is uncommitted and unaudited, so edit it in place with no rev bump.
- Touch only `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-23.md`.
- Do not commit, do not stage, and do not run any gate. Report the old and new text.
