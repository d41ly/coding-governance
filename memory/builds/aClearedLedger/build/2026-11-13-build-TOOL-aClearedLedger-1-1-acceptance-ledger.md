# Acceptance ledger — TOOL-aClearedLedger-1

**Serves:** journal TOOL-aClearedLedger-1

Built against spec rev-1 in this record's own commit, from base 1f3462666.
The catalogue row was edited by hand; the charter, its lock row and the two role agents were written by `bash tools/playbook/adopt-playbook.sh --target .` and then `python tools/roles/render_agents.py --write`, and no rendered file was edited.
Each line is a probe the builder made in the pass. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section. The spec declares no new arm.

**Evidences:** TOOL-aClearedLedger-1
- AC1 — `git diff --numstat 8db6f4be -- tools/playbook/practices.toml` — printed one row, one line added and one removed, and the grep for the exception's clause over the catalogue printed 1; the row's tag and its two reach keys are outside the diff.
- AC2 — `git hash-object AGENTS.md` — printed 85e99b617ac9acdff18745944f3d0864e68414b6, the `blob` value of the charter's row in the lock; the `[spec]` line measured 195 characters, one number, under the cap of 200; and the numstat over the charter printed one line added and one removed. (PINNED, 2026-11-13)
- AC3 — `gov-spec-writer.md` — the grep printed 1 for it and for `gov-spec-reviewer.md` and 0 for each of the seven other role agents, and the numstat over the agents folder printed two rows, each one line added and one removed.
- AC4 — `an inline red fix` — the `git grep` printed four lines, one in each of the catalogue, the charter and the two role agents, and each of the four carries the clause.
