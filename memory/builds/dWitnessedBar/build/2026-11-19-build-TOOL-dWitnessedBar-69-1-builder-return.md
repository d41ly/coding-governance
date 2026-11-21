**Serves:** journal TOOL-dWitnessedBar-69

# TOOL-dWitnessedBar-69 — builder return 1 (run `wf_e30e4e79-91f`), committed 298369174

## Why

TOOL-dWitnessedBar-69 is built as its rev-5 spec states it. I checked the spec against the tree before editing, and every claim it makes about current code still held: read_green_file has seven `$(awk ...)` reads in the END-print form, read_local_verdict calls slot.read_text, read_tag_lines uses splitlines() and rstrip("\r"), run-gates.sh#read_record_keys has the shape S1 copies, the hook calls read_green_file once, the shell-role row was 1719, and neither file is on the kickoff manifest's watch list. So there is no divergence to report.

## Summary

Built and committed TOOL-dWitnessedBar-69 as 298369174. The base was 09281c279. All four acceptance criteria were seen pass, and where a criterion has a red case, that red was seen too. No gate, suite or bar ran.

**S1 (`.githooks/pre-push#read_green_file`):** the seven `$(awk ...)` reads are now one loop, `while IFS= read -r _rg_l || [ -n "$_rg_l" ]; do ... done 2>/dev/null < "$1"`. A line with no TAB is skipped. The key is the text before the first TAB and the value everything after it. One trailing CR is stripped with `${_rg_v%$'\r'}`, on a line of its own. A `case` assigns each key without quotes (`sha) rec_sha=$_rg_v ;;` and so on). The three new variables are `local`, the comments now sit beside their case lines and never name awk, and the closing `}` is still the only one at column 0.

**S2 (`tools/run-gates/verdict_backends.py`):** `read_local_verdict` now opens the record with `open(slot, encoding="utf-8", errors="replace", newline="")` and still turns an `OSError` into DEAD PROBE. `read_tag_lines` splits on `"\n"` only, still skips a line with no TAB, and strips one trailing `"\r"` from the value.

**Other files in the commit:**
- `memory/project/shell-role.txt`: the `.githooks/pre-push` line limit was raised from 1719 to 1720 through `ratchet.py widen shell-role`. That writes a record, `memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-69-widen-9.md`, which I declared through `--dispatch` first. Its reason line first said 1731, a raw count of non-comment lines that does not match how the gate counts; I corrected it to the gate's 1720 before committing.
- The acceptance ledger `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-69-1-acceptance-ledger.md`.
- The spec status set to CLOSED, with no other change to the spec.
- `RUN.md`, plus what `gen_build_index.py --write` rewrote: `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README, and the spec's generated records table.

I added no function, so `symbols.json` did not need regenerating. `--brief` said the brief was already recorded, unchanged.

**What I checked, and the gates each check stands in for:**
- **AC1–AC3** (stand in for the pre-push self-test and the gov canary's AC12 hook half): I cut the function with the awk range from `.githooks/pre-push`, sourced it, and ran it on AC1's record under `%TEMP%/wb69`.
  - AC1: `rec_sha` read 40 `b`, `rec_man` read `x \t`, `rec_fp` read 40 `c` (the bare `fingerprint` line after it was skipped), and `rec_st` read `on`. A missing path and a directory path each left all seven variables empty.
  - AC2: with the strip removed by the `sed` (diff shows one changed line), `rec_sha` was 41 bytes ending in `\r`. This is the red case. (DERIVED from the builder's probe)
  - AC3: `grep -c 'awk'` printed 0 and `grep -c 'IFS= read -r'` printed 1.
  - The hook also passes `bash -n`.
- **AC4** (stands in for the gov canary's `key-no-tab` plant and its `read_tag_lines` check): a Python probe built a scratch `git init` repo under `%TEMP%/wb69py` holding the record with CR-LF endings and `run_id` set to `r<CR>1`. It read GREEN, and the why's `repr` held `run r\r1,`. A copy of `verdict_backends.py` with the strip removed (one changed line) read DEAD PROBE. `grep -n 'newline=""'` finds the open in `read_local_verdict`. Both scratch folders were removed afterwards.

**Bug-class checklist:** ran `gotchas.py --for-diff HEAD~1..HEAD` and went through it:
- "an attested count must count what the grader counts" is the 1731-to-1720 correction above.
- For "empty field collapses unless it is last", I confirmed the trailing TAB in AC1's `manifest` line is kept, and that `split("\n")` leaving an empty last piece is skipped because it has no TAB.
- For "fixture passes by finding nothing", both breaks were seen red, so the probes do catch something.
- The rest of the selected classes don't apply to this diff.

**Left for the main loop at the close (not run here):** the legs of §7, which are measure-legs selftest, pre-push self-test, run-gates gov canary, portability (shell lines only shrink), recall floor, recall floor arms and memory hygiene. Section 7 adds no new check. It does name two breaks to stage and record as red with their failing lines: deleting the hook's strip should turn the AC12 arm's hook half red, and deleting the Python strip should turn the `key-no-tab` plant and the AC12 `read_tag_lines` check red.

No command hit its time limit. The changes already in `help/reference/drive.md` and `help/reference/units.md` before this pass are not mine; I left them unstaged.
