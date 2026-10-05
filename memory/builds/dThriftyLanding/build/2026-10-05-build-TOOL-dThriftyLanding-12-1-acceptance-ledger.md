# Acceptance ledger — TOOL-dThriftyLanding-12

**Serves:** journal TOOL-dThriftyLanding-12

Built on `cd2e441e`. Slices of the canary and of the hook suite, and the govkit D4 block run
standalone, passed against this code. Against the code before this unit: the hook's M2 and M5 arms
failed, the D4 keep-the-edit arm failed, and the old character-prefix rule passed `notes/a`. The
env-reader arm failed under a mutation removing the runner's unset. L3's inherited-green and
linked-worktree arms pass on both, as coverage of behaviour units 2 and 3 already had.

**Evidences:** TOOL-dThriftyLanding-12
- AC1 — `GATE ok    reads b only` — units 8 and 9's merged-side-branch arms pass, which closes M1's findings 6, 7 and 23
- AC2 — `reads park, so it is not scoped as doc-only` — printed for a doc push under park at R, with no `docs-only`; the prior hook scoped it doc-only
- AC3 — `differs from what the receipt recorded` — reported by apply after a hand-edit of an owned row's doc_reads, and the edit kept; the prior govkit overwrote it
- AC4 — `notes/a bad` — the component-boundary rule fails a string prefix of a tracked file and passes the directory; arm 1b uses that rule
- AC5 — `not a plain repo path` — printed for `GATE_DOC_PATHS="."`, and a code push stays out of the doc class; the prior hook classified it doc-only
- AC6 — `"doc_reads": []` — on the `kit version markers` row a fixture apply of check-kit-versions wrote; D1 refuses 1.24
- AC7 — `last writer wins` — in the README and in the runner comment; the hook's FULL path no longer re-reads the own record
- AC8 — `unset` — the env reader leg's record; the inherited-green doc push hands the bar R, a linked worktree adopts `the common dir's gate-full-green`, and the 3i2 full run writes `gate-full-green`
- AC9 — `DECLARED leg` — the charter's reworded sentence, 11 bytes under its cap; `TOOL-dThriftyLanding-13` records the dropped sentence in memory/DECISIONS.md
