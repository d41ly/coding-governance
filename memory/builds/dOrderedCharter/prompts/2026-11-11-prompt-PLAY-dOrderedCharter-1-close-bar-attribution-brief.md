**Serves:** research PLAY-dOrderedCharter-1

# Brief: attribute the close bar's reds over daf84987f

## The prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The close's bar (`GATE_FULL=1`, no self-tests, the unattended kit gate leg left out by the owner's
2026-11-11 order) ran over `daf84987f` and failed eight legs.

## The brief

### Goal

For each red leg, say whether this build caused it, the merge base carried it, or it is owed at the lander by design, and name the
narrowest fix and who makes it.

### Items

1. The legs and their logs, under `C:/projects/coding-governance/.git/worktrees/unattended-dorderedcharter-725f52/gate-logs/`:
   `install-prefix__shipped_surface_.log`, `dead-path_carriers__deleted_files_still_named_.log`, `govkit_selfcheck.log`,
   `kit_epoch__shipped_bytes_move__the_version_moves_.log`, `govkit_runbook_parity.log`, `govkit_acceptance_matrix.log`,
   `policy_check.log`. The memory hygiene leg is the main loop's own and is out of scope.
2. For each leg, read its log whole and quote the exact red lines, separating them from the notes the leg prints on green.
3. Attribute each red: run the leg's own command at the merge base `8bec4cefd` in a scratch clone under `%TEMP%`, or read the diff
   `8bec4cefd..daf84987f`, and say which unit's commit introduced it. The kit epoch leg says some versions are owed at the lander:
   say whether `tools/push-main.sh` mints them, so the leg is expected red on a branch.
4. For each own red, name the narrowest fix: the file, the line, the change, and whether it is a record the main loop writes or a
   product change a builder makes. Never fix anything yourself.
5. Bound your work: no self-test suite, no bar, no lander.

### Acceptance

- Every one of the seven legs has its red lines quoted, an attribution with the evidence that shows it, and a named fix.

### Gates

None. A read-only attribution.

### Non-goals

- No edit anywhere in the repository. No suite run.
