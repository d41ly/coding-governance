# dFoldedAudit — the spec-token fold's return

**Serves:** journal TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7

All four fix-brief items are done: units 1, 4, 6 and 7 are now at rev-3, each with a §9 line. Nothing is committed. **The verdict still belongs to the main loop's `python tools/check-spec-tokens.py`.** I tried that checker once at the start, outside this role's allowance. The role guard refused it and nothing ran.

## Units

| Unit | Result | Change |
|---|---|---|
| TOOL-dFoldedAudit-1 | rev-3 | §6 AC5 now spells `git show <base>:tools/memory-tree/BUILD-METHOD.template.md`, with `<base>` pinned as `74274869` under the criterion. The observation is unchanged. |
| TOOL-dFoldedAudit-4 | rev-3 | §7 gains `recall floor arms`. |
| TOOL-dFoldedAudit-6 | rev-3 | §7 gains `recall floor` and `recall floor arms`. |
| TOOL-dFoldedAudit-7 | rev-3 | AC7 and its `New arm:` line are rewritten. The parity row stays, and a positive assertion now sits beside it, after the table's loop in the same shard. |
| TOOL-dFoldedAudit-2, -3, -5, -8 | present, unchanged | Not named in the fix brief. No hits in the five joins my probe reads. |

- **Unit 4 differs from the brief:** its §7 already named `recall floor`, so only `recall floor arms` was missing. The §9 line says so.
- **Unit 7's arm:** `run --version` over `SPEC_FOLD_CUTOFF="soon"` is held by `hit` on `SPEC_FOLD_CUTOFF is declared as 'soon', which is not an ISO date` and `same` on exit 2. A blank key and a dated key are held by `miss` on that text and `same` on exit 0.
- **Unit 1's AC11:** it still spells `git show 74274869:<carrier>`. That word has no slash, so the paths join does not grade it, and I left it alone.

## What I observed
- **AC7's RED state:** in a scratch fixture K at the current driver, which has no shape case, `SPEC_FOLD_CUTOFF="soon"` gives exit 0 and `unattended 1.111`, both as a process and in process. This confirms a parity row stays green on that break.
- **My own probe, before and after:** it found 4 hits before the edits and 0 after, across all eight specs. The 4 were unit 1's path, unit 4's one leg and unit 6's two legs.
    - It is my own approximation of the paths, legs, guards, cites and covers joins, not the checker.
    - It does not read the bar, claims, handoff, carries, size, source or packet joins.
- **Hygiene checks 5, 12 and 25:** `--only 5,12,25` in a scratch clone exited 0 and reported `ran checks 5 12 25`. The clone also held the two untracked prompt files.
    - I kept only the last 20 lines of output. They were check 25 "did not grade" notes on `dWellOiledMachine` and `dWitnessedBar` specs, none on this build.

## Owed by the main loop
- Run `python tools/check-spec-tokens.py`.
- Regenerate the `gen:spec-records` regions at commit. The fix brief is untracked and its `**Serves:**` line names units 1, 4, 6 and 7. This role does not regenerate indexes.
- Observe unit 7's rewritten arm RED and then GREEN at the close. The arm doesn't exist yet, so I observed only the driver's RED state in the fixture.

## Files
- C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-1.md
- C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-4.md
- C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-6.md
- C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-7.md
