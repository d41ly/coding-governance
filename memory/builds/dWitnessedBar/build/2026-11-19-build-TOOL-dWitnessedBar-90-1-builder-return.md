**Serves:** journal TOOL-dWitnessedBar-90

# TOOL-dWitnessedBar-90 — builder return 1 (run `wf_ff7cd4ad-9b9`), committed da3fbc953e0214526a29594fe5bac8bb4e12290d

## Why

Built TOOL-dWitnessedBar-90 (rev-3) as written. Before any edit, every code claim in spec section 4 Evidence checked out against the tree. That covers suite lines 243-288 and the call site at 968-979 (the file is unchanged since 9b0ad9c97), the 17 Raised/RAISED count, FLOOR_ASSERTIONS=80, the shell-role row at 852 and the owner derivation's output of 28. No divergence was found.

## Summary

Commit da3fbc953 on branch/unattended-dwitnessedbar-2ed3b3, built from base 197df554d. Its trailers are Decided, Pass: TOOL-dWitnessedBar-90 and Co-Authored-By. The spec header is set to CLOSED with date 2026-11-21. The spec's gen:spec-records region also moved, as S13 requires.

Code changes, all in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh:
- S1: the canary call site has a new elif for any check_canary_keys return outside 0 to 3. It prints `gov-canary: check_canary_keys returned <rc>, a code it does not define`, sets fail=1, and rgf_ok is now set only on code 0 or 1 (it used to be set on anything but 3). A two-line comment above the block describes the branch.
- S11: the TOOL-aShardedFloor-2 comment pair and the 41 floor-history lines below the constant are deleted. The one line above the constant now reads `# Raised to 80 by TOOL-dWitnessedBar-90, counting every arm built through order 47; stated ABSOLUTELY.` and the constant stays FLOOR_ASSERTIONS=80, because S1 adds no increment of `a`.
- The suite now measures 853 code lines. The shell-role row in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/project/shell-role.txt went from 852 to 853 through `ratchet.py widen`, which wrote memory/builds/dWitnessedBar/build/2026-11-21-build-TOOL-dWitnessedBar-90-widen-25.md.

Records: the acceptance ledger memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-90-1-acceptance-ledger.md has one line per criterion, each marked observed or OWED. `gen_build_index.py --write` rewrote README.md, LIVE.md, backlog/TOOL.md and the spec's region, and all of them are committed with RUN.md. No function was added, so the codebase map did not need regenerating. All of these paths were in the declared write set.

Probes run (fixtures and probes only; no gate, suite or bar ran):
- AC1, standing in for the gov-canary arm: the call site was cut out and sourced over a stubbed check_canary_keys. On codes 7 and 4 the new line printed, fail was 1 and rgf_ok was 0. Codes 0, 1, 2 and 3 behaved as before. The base blob's call site passed on 7 and 4, so the probe tells the old code from the new.
- AC3: the built sed line run over S3's seven fixture lines counted `sha)` once in every file. The first five lines each changed by one line and the two modifier arms changed by none.
- AC11, standing in for the testsuite-counts and gov-canary floor checks: the comment greps were run on the file. There is one Raised line at 244 directly above FLOOR_ASSERTIONS at 245; the line above the constant names only this unit; the anchored assignment counts 1; each of the three comments that must stay counts 1.
- AC14: the cut of check_canary_keys holds its definition line and no increment of `a`. Called with CANARY_KEYS both as defined and emptied, it left a=0 each time.
- AC15: the owner derivation printed 28 and spec/2026-10-25-spec-TOOL-dWitnessedBar-90.md. In scratch copies it gave MALFORMED REGION with exit 3, REGION READER NOT FOUND with exit 4, and REGION READ FAILED (rc 2) with exit 6. The `python3? -c` grep over that section printed 0.
- `sh_hygiene.py --measure` gave 853, standing in for the portability and ratchet legs.
- `bash -n` passed on the suite.

Owed by the main loop at the close:
- AC1, AC2 and AC9: the scratch-clone arm runs.
- AC11: the arm's `PASS (<n> assertions)` with n equal to 80. The floor was counted by reading, not by running the suite.
- AC13: the porcelain check after the commit.
- Every ledger line this unit writes into the ledgers of units 76, 87 and 89 (AC1-AC15 at close), per section 4 Rollout.
- The bar's gates: run-gates gov canary (held unless GATE_SELFTESTS is set), testsuite counts, portability, ratchet, recall floor, recall floor arms and memory hygiene.
- The New arm's RED-first observation on tools/run-gates/run-gates.gov.test.sh, covering AC1 and AC2. One staged break is a call site that handles only 0, 1 and 2, so the isolated clone ends `PASS (`. The other is a match with non-optional quotes, which shows `variant changed 0 lines`.

Bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`, rc 0, 30 classes) was gone through:
- The guard-above-a-fold class does not apply: 0 and 1 still reach the slot loop.
- The heredoc class does not apply: the Python edit used a quoted heredoc with no escapes, and the result was checked.
- Each ledger line is a single line, so no token wraps, and the ledger has no inline fence.
- The retirement-inventory class does not apply: nothing in tools/ reads the deleted floor comments. check-testsuite-counts.sh reads only the assignment and its use, and the drift-audit check that wants a justification comment only fires when a pin weakens, and 80 to 80 does not.

The working tree still shows help/reference/drive.md and help/reference/units.md as modified. They have no content diff and were not mine, so they are not staged. Nothing timed out or was skipped.
