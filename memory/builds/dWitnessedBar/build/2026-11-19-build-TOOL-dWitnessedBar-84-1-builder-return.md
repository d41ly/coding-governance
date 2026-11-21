**Serves:** journal TOOL-dWitnessedBar-84

# TOOL-dWitnessedBar-84 — builder return 1 (run `wf_b8b2787a-c48`), committed e1ad4ef32f2f7ef1261b2f7166a724b780383495

## Why

TOOL-dWitnessedBar-84 is built from its rev-5 spec in one pass commit, e1ad4ef32 on top of base 78cf6b856. The pass commit sets the spec header to CLOSED and carries the `Pass: TOOL-dWitnessedBar-84` trailer. Before writing, I checked the spec's claims against the tree and none had drifted. The suite lines, `FLOOR_ASSERTIONS=74` with unit 82's comment, the registry guard row, the read loops of both hook readers and the four DEFERRED specs naming the guide under Files touched all matched. So there was no divergence to return.

## Summary

**What was built** (all in `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh` unless named):
- **S13, return codes:** `check_cr_reached` unsets `read_green_file`, then returns 2 for a file it cannot source, a file that defines no `read_green_file`, or a record that is not a regular file. It returns 1 only after measuring a value that failed. `check_canary_keys` prints a variable only on a 1 and returns 2 on any 2. On a 2, `check_key_variant` prints `<label>variant could not be sourced or read (rc 2)` after its two count reasons. The canary then prints its line once for `unread`.
- **S14, visit counts:** `check_canary_keys` and the liveness loop each count the pairs they visit, against one top-level count of the words in `${CANARY_KEYS[*]}` (`rgf_km`), which must be at least 2. The canary's failure goes to stderr and returns 2 (F4 (a)). Each check adds one assertion, so `FLOOR_ASSERTIONS` goes from 74 to 76. Its `# RAISED 74 -> 76 by TOOL-dWitnessedBar-84` comment sits below the constant, and the line above the constant is unchanged.
- **S6:** the `<key>)` sed in `check_key_variant` now also matches the quoted form `rec_sha="$_rg_v"`.
- **S10/S11:** a private helper `_derive_case_keys <cut-file> <prefix>` replaces both derivations, called once with `rec_` and once with `bg_`. It handles several arms on one line, and returns 1 with both numbers on stderr when its count differs from a `grep -o` count. Each caller's existing assertion now requires its 0.
- **S9:** the `run-gates gov canary` guard in `tools/govkit/registry.toml` gains `memory/guides/MERGE-BAR.md`, and `tools/gate-legs.json` was re-rendered with `leg_factory.py --write`.
- **S9 ask rows:**
  - `TOOL-dBoundRoles-76` for `TOOL-dBoundRoles-25`
  - `PLAY-dConvergedCharter-43`, `-44` and `-45` for `PLAY-dConvergedCharter-1`, `-7` and `-19`
  - `TOOL-dWitnessedBar-104` for the `AGENTS.md` (charter) half
  - each has a `SEV` line.
- **Records:** the ledgers of units 72 and 74 to 78 gain the lines for S1, S3 to S8, S10, S15 and S16, and this unit's own acceptance ledger is written. The shell-role row was widened with `ratchet.py widen` (record `-widen-23`), then set to the measured 850 code lines.
- **Generated files in the commit:** `gen_build_index.py --write` output, and the kickoff manifest `memory/guides/SESSION-KICKOFF.md` re-stamped at the base sha for the watched `tools/gate-legs.json`. I declared the four extra paths with `--dispatch` before staging them. The map needed no render: `gen_map.py --check` exits 0, because a private helper adds no symbol key.

**Checks that ran:** probes only, no gate, suite or bar. Each stands in for the gate leg named in brackets.
- `bash -n` on the suite passed [portability / the gov canary's parse].
- AC2: the awk probe prints nothing on the built suite and prints the planted line on a scratch copy [gov canary single-copy arm].
- AC3: unit 74's pass commit `7c579ad47` shows 2 matching lines, and the probe restricted to `rec_sha` prints nothing there.
- AC6: with the cut's functions sourced in `bash -c`, the quoted `sha` arm is edited and passes both variants, and a split arm prints `tail variant changed 0 lines` and `length variant changed 0 lines`.
- AC13: return code 2 in all three read-failure cases, 1 on the length mutant, 0 on the canary's mutant. A variant pointed at a path it never wrote prints `could not be sourced or read (rc 2)`.
- AC14: an empty `CANARY_KEYS` prints `visited 0 of 0` for both loops; loops that stop after the first pair print `visited 1 of 2`.
- AC10: the definition grep prints 1 and the call grep prints 2.
- AC11: `read_bar_file` gives 16 = 16 with return 0, and `read_green_file` gives 7. A copy with two arms on one line still gives 16, while a helper that reads only the first label per line returns 1 and prints the cut and the numbers 15 and 16.
- AC9 and AC16, through `check-spec-tokens.py --legs-for`: the guide now maps to the gov canary, and `leg_factory.py --check` reports fresh. In a scratch clone under `%TEMP%/u84c` (removed afterwards), a manifest without the hook entry, or with it spelled `{prefix}/.githooks/pre-push`, prints no gov-canary line.
- AC7: each grep prints 1 and `gen_map.py --check` exits 0.
- AC15: 0 cited spec lines in the specs of units 75 and 77.
- The name `_derive_case_keys` passed `lexicon.py --suggest`.
- The pre-commit hook's staged memory-hygiene run passed and the commit landed.
- `gotchas.py --for-diff HEAD~1..HEAD` ran, and I checked my changes against its relevant classes (wrapped ledger tokens, heredoc escapes, readers stranded by a changed return code, empty-population fixtures); none needed a change.

**Owed to the main loop at the close:**
- the 17 legs of §7, plus the kickoff manifest check for the re-stamp; (DERIVED from the builder's probe)
- the arm runs in scratch clones for AC5, AC6, AC13, AC14 and AC17. AC5's printed `for count 2` line has to be quoted into unit 72's AC1 ledger line; I measured only that the break changes 2 lines; (DERIVED from the builder's probe)
- the ledger greps for AC1, AC4, AC8, AC12 and AC15, and AC12's eight greps;
- the `New arm:` RED-first observations for AC11, AC13, AC14 and AC17: a helper reading one label per line, a variant path never written, an empty `CANARY_KEYS`, and loops that stop after the first pair.

**Decisions to know about:**
- The ask rows for `TOOL-dBoundRoles-25` and `PLAY-dConvergedCharter-7` were filed even though those specs' §7 already names the gov canary. S9 and AC9 name all four specs the guard reaches, and each of the two rows says its leg is already owed.
- The canary's visit-count increment sits only in the branch that calls `check_canary_keys`, so a failed diff count skips it.

Nothing was skipped for timeout. The pre-existing changes to `help/reference/drive.md` and `help/reference/units.md` are not this unit's and were left unstaged.
