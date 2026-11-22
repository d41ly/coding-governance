**Serves:** journal TOOL-dWitnessedBar-70

# TOOL-dWitnessedBar-70 — builder return 1 (run `wf_4133ee0c-d3b`), committed 0890c99d1

## Why

The spec was buildable as written. Its claims held at HEAD: the cut range, the sed pattern turning `_rg_v=${_rg_v%$'\r'}` into `_rg_v=${_rg_v}`, the evidence suite's diff-count idiom, the stale comment and the shell-role row at 706. A probe reproduced the §4 Evidence table on all four hook copies (counts 1, 2, 0 and 1; mutant rec_sha at 41 with CR, 40, 41 with CR, and 82).

## Summary

Pass commit 0890c99d1 for TOOL-dWitnessedBar-70. Its trailers are `Pass: TOOL-dWitnessedBar-70` and Co-Authored-By. The spec header moves INPROGRESS to CLOSED with no other edit; the generator also rewrote the spec's own records table.

What changed:
- `C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh`: the AC12 arm now builds a mutant of the cut `read_green_file` by `sed 's/%[$].[\]r.}/}/'`. It counts the `diff` lines opening `>` and requires exactly 1. It evals the mutant in a subshell over `$rgf_rec` and requires `rec_sha` to be 41 bytes ending in CR. If that fails, the arm prints `gov-canary: the planted CR never reached read_green_file on $(uname -s); the CR-strip assertion is not counted` and sets `fail=1`. The `rec_sha` compare's `a=$((a+1))` only runs when the canary passes, but the compare itself always runs and prints its own line (F3). No assertion was added, so FLOOR_ASSERTIONS stays 54. The arm's comment now names the canary and S3's two breaks. Its WHAT THIS DOES NOT CHECK clause says a strip spelled other than `%$'\r'}`, or spelled twice, fails the canary at its count; the "lose the CR" sentence is gone. (DERIVED from the builder's probe)
- Unit 66's acceptance ledger: the AC2 line was rewritten in place (S4). It now names the cause (gawk's text-mode input and bash `$(...)` drop the CR on Git for Windows), says unit 69's loop now passes the CR on, cites this spec's §4 Evidence and names TOOL-dWitnessedBar-70. It no longer says OWED.
- The shell-role row is widened to the measured 715 under `memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-70-widen-12.md`, which I declared with `--dispatch` before staging (admitted). The acceptance ledger is `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-70-1-acceptance-ledger.md`.
- Generator output is committed too: gen_build_index rewrote README, LIVE, backlog/TOOL.md and the spec's records table. gen_map ran and changed nothing.

A platform fact I found while probing, which needs a left-shift (recorded in a `Decided:` trailer): on this node's bash 5.3.9 (cygwin), a `$'\r'` written inside `$(...)` becomes an empty string. So `case ... in *$'\r')` inside the subshell matched every value and the canary passed on the awk copy. The canary now uses `rgf_crb=$'\r'`, set outside the subshell. No gotchas entry exists for this yet; one should be added at the close.

Checks that ran:
- `bash -n` on the suite.
- A scratch probe (`C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/u70probe.sh`). It evals the arm's own lines, cut from the suite, over a hand-built CRLF record laid out like the arm's. `ROOT` pointed at four trees under `%TEMP%/u70p`: HEAD's hook, the AC2 awk copy, the copy with the strip line deleted, and S3's print-every-match copy. This stands in for the `run-gates gov canary` leg for AC1 and AC2:
  - **HEAD:** count 1, mutant `wc -c` 41, `od -c` `\r`, `a` 1, `fail` 0, no canary line.
  - **Awk copy:** count 2, 40 bytes, canary line printed, `fail` 1, `a` 0, the compare held. (DERIVED from the builder's probe)
  - **Strip deleted:** count 0, canary line printed and the compare's `'b…b\r'` line.
  - **Print-every-match:** count 1, 82 bytes, canary line printed and the compare's `'a…a|b…b'` line. (DERIVED from the builder's probe)
- `grep -c 'lose the CR'` on the suite printed 0.
- AC4 was checked by reading the rewritten line.

Owed to the main loop at the close:
- The `run-gates gov canary` leg over the arm's real run_local_plant record. My probe's record was hand-built, which is the synthetic-value gotcha class.
- The `New arm:` RED-first observation for the canary under the three staged breaks.
- AC3: the two S3 breaks staged on a Windows node and recorded as `- AC2 — ` lines in unit 66's ledger, with the failing lines and `uname -s`.
- The legs `portability (shell lines only shrink)`, `recall floor`, `recall floor arms` and `memory hygiene`.

`gotchas.py --for-diff HEAD~1..HEAD` exited 0 with a 30-class checklist. I acted on it: every ledger token is on one line and spelled by its criterion, none of the changed files has a CR or control byte, the arm's comment was rechecked against the amendment class, and the synthetic record is named above. No command timed out or was skipped. `help/reference/drive.md` and `help/reference/units.md` were already modified when I started; I left them unstaged and untouched.
