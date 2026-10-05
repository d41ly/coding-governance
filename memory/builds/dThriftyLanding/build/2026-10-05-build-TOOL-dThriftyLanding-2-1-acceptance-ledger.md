# Acceptance ledger — TOOL-dThriftyLanding-2

**Serves:** journal TOOL-dThriftyLanding-2

Built on `5e4bf845`. AC1's arm sits in the evidence harness after the stamp's control; AC2 and AC3
are arms 30, 30b and 30c of the hook suite. Slices of both suites holding their own prologues ran
against the new code and against the unit-1 runner and the base hook swapped in.

**Evidences:** TOOL-dThriftyLanding-2
- AC1 — `gate-full-green.shared` — written in the common dir by a fully-green run in a linked worktree, carrying that worktree stamp's sha; the common dir's own stamp untouched; the unit-1 runner wrote no shared file
- AC2 — `scoped gate` — with no own stamp and a usable shared one, the decision line names `the common dir's gate-full-green.shared`; the base hook printed `FULL gate` with `no recorded full green`
- AC3 — `FULL gate` — with an unreachable shared sha the reason names `no recorded full green` and the shared stamp's `not an ancestor` refusal; arm 30c's control keeps a usable own stamp first, worded as before
