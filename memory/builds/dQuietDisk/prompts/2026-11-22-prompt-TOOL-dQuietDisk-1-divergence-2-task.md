**Serves:** research TOOL-dQuietDisk-1 TOOL-dQuietDisk-7

# Spec task — dQuietDisk: unit 1's second-pass divergences, ruled; unit 7's §7

You write specs only. Do not commit. Unit 1's second pass (unit harness run `wf_e88edf82-25c`) completed the code
and saved it as a patch. `--dispatch` check 49 then refused it on the spec. The run has ruled on each point (M3).
Write the rulings into the specs.

## TOOL-dQuietDisk-1, rev-3 → rev-4

1. **§7 Gates.** The leg line names `history-store selftest`, the leg S11 adds. The spec-token checker reds without it:
   PINNED from the checker's output: `[guards] history-store selftest <- tools/lib/history_store.py — §4 files-touched names tools/lib/history_store.py,
   which trips the guard of leg 'history-store selftest', absent from the §7 leg line`.

2. **The shell-line ledger.** The bash face stays, because units 2 and 3 are bash consumers of it. The unguarded leg
   `portability (shell lines only shrink)` reds on:
   - the new `tools/lib/history-store.sh`, which has no row;
   - the grown `tools/unattended/lib-unattended.sh` and `tools/lib/resolve-python.test.sh`.

   **Ruling:**
   - The pass widens those three rows through the ledger factory's widen route, writing
     `memory/project/shell-role.txt` and a widen record under `memory/builds/dQuietDisk/build/`, as
     dWitnessedBar's units 58 and 60 did with `ratchet.py widen shell-role`.
   - Add both paths to Files touched.
   - The widen record states two figures separately: the lines this unit adds, and the base excess the merge
     `b3f5a2bc3` already carried. Today that is 1420 against 1557 for `resolve-python.test.sh` and 1319 against 1331
     for `lib-unattended.sh`.
   - The base excess is inherited from dWitnessedBar's land tip. It is reconciled when the run re-merges main after
     dWitnessedBar's landing: the row is re-measured there and the record amended.
   - Rows for files this unit does not touch are not this unit's.

3. **The reader's protocol, §4.** `read_info`'s oid comes from `git rev-parse --verify <rev>^{object}` (or
   `--batch-check`), not from `git cat-file -t`. Say which, and spell it.

4. **The env-leak block.** The module carries the `git_env_leaks_py` block inline. That way, a `GIT_DIR` exported by a
   hook never points the selftest's scratch-repo git calls at gov's own repo. Say so in §4, and name it in the parity
   rows if the block is parity-checked.

5. **The saved patch.** The next pass applies it:
   `C:/Users/d41ly/AppData/Local/Temp/claude/b3f6db677b077b04/0840beea-0651-4dc3-9fe7-f227915b6b42/scratchpad/unit1-work/TOOL-dQuietDisk-1.patch`.
   You need not mention it in the spec. The brief carries it.

## TOOL-dQuietDisk-7

Its §4 names `tools/lib/`, which trips the same leg's guard. Name `history-store selftest` on its §7 leg line, bump
its rev, and add a revision-log line naming this task.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-1 TOOL-dQuietDisk-7`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` on each spec.
- Run `python tools/check-spec-tokens.py --spec <path>` on each spec, and also a plain whole-tree
  `python tools/check-spec-tokens.py`, so check 49 reads green.
- Fix every finding.
