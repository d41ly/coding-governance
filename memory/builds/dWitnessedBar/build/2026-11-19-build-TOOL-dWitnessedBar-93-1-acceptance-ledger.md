# TOOL-dWitnessedBar-93 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-93

No merge bar, no self-test suite and no gate leg ran in this pass. This unit writes records only: it touches no code file and mints no function. Its pass-time probe ran on node d, 2026-11-21, from base `2ac88ccaf`, over a scratch root under the run's scratch directory, with 92 §4's note check cut from spec-92 at `3ffc6c67c` and a copy carrying S1's line. Every line marked OWED is the main loop's at the close, after the last unit is terminal: AC1's and AC2's fixtures, S3's note in unit 92's ledger and AC3's read of it (§4 Rollout).

**Evidences:** TOOL-dWitnessedBar-93
- AC1 — `NOTES OK 2` — at the pass, a scratch 88 ledger with the `TOOL-dWitnessedBar-92 S4` note under `- AC6` and `- AC18`, fed both `92|S4|88` rows, printed `NOTES OK 2`, exit 0, through the check with S1's line, and `MISPLACED 92 S4 resolve_python:` twice, exit 1, through spec-92's unreplaced script (PINNED 2026-11-21). OWED: the fixture's run at the close, with the fragments of units 94, 96 and 97 composed beside S1's.
- AC2 — `MISPLACED 92 S4 resolve_python:` — at the pass, the same scratch root with the note under `- AC18` removed printed it once, exit 1, through the check with S1's line (PINNED 2026-11-21). OWED: the fixture's run at the close.
- AC3 — `NOTES OK 1` — OWED: S3's note labelled `TOOL-dWitnessedBar-93 S3`, a continuation line under the `- AC4` answer of `2026-11-19-build-TOOL-dWitnessedBar-92-1-acceptance-ledger.md` carrying the backticked `NOTES OK 2`, and the note check with S1's line fed `93|S3|92|AC4|NOTES OK 2`, at the close; both figures are PINNED by the spec's S3 and AC3.
