# Synthesis return: the closing pair compared

**Serves:** research PLAY-dClosedLoop-1

Dispatch 210's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-48-synthesizer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I wrote the comparison record. All 25 of run A's findings and all 24 of run B's are placed in its map.

**Record:** `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-audit-closing-reviews-compared.md`

**Map rows by disposition (29 rows):**
- **fold: 21.** Four of them take a skeptic's corrected fix:
  - `unit-lease-needs-cycle` takes A's.
  - `mailbox-answer-targets` takes A's.
  - `stage0-red-unreported` takes B's.
  - `close-path-writes-refused` takes B's.
  - The other 17 rows are plain folds.
- **fork: 1.** This is `flakes-measured-no-writer`.
- **no fold: 7.** These are the rows where every finding was refuted.

**Fork question:**
- `flakes-measured-no-writer`: who derives the threshold for `verdict.flakes.entry: measured` from the flake records, and when does a leg switch from 2/10 to it? I recommend option (a): dWitnessedBar's gate-health clause cl-0339 derives it.

**Finding ids I could not place:** none.

The two runs drew opposite lines on the `mailbox.answer` actor, and I took run B's:
- **Actor fix not folded:** row `mailbox-answer-actor` is a plain fold, not A's skeptic's corrected fix. That fix makes one fixed role (e.g. the architect) the actor. It would contradict layer-roles `[matrix]` and the 2026-10-20 `role_matrix.py`, which already accept "the role that owns". The fold teaches Stage 0's K1 that form instead.
- **Roles dependency:** run A's skeptic refuted it in finding 5, while run B's confirmed it in finding 23 (`answer-dispatch-non-ancestor`). The single stand-in in that fold covers both halves, so the conflict does not change what the fold does.
