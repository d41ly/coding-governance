**Serves:** journal TOOL-dWitnessedBar-85

# TOOL-dWitnessedBar-85 — builder return 1 (run `wf_709652e5-bbb`), committed 0a5a198f6

## Why

Built as the spec states. I checked every claim spec rev-3 makes about the code against the tree at base e7504f024, and all of them hold: a=0, FLOOR_ASSERTIONS=76, the tail and length calls at :980 and :982, the floor check at :1315, check_key_variant returning 0 only when the variant is seen red, CANARY_KEYS with two words, and the shell-role row at 850. Nothing diverged from the spec.

## Summary

TOOL-dWitnessedBar-85 is built and committed as 0a5a198f6. The subject names the unit and the trailer block ends with `Pass: TOOL-dWitnessedBar-85` and Co-Authored-By. It touches only paths that were declared, so no extra --dispatch was needed.

Changes:
- **S1:** In the liveness loop of tools/run-gates/run-gates.gov.test.sh, the tail call and the length call of check_key_variant each have `&& a=$((a+1)) ||` on their existing continuation line. This is at the loop's top level, outside the `$(...)`, so `a` only goes up when the call returns 0. That adds 2 per key and 4 across today's two keys.
- **S2:** `FLOOR_ASSERTIONS=80`, which is 76 plus 4, with nothing after the number. The new `# RAISED 76 -> 80 by TOOL-dWitnessedBar-85` comment sits directly below the constant and above unit 84's, and its first line names no other unit id. The owner line above the constant is unchanged.
- **S3:** No code line was added. I also brought two existing comments up to date: the one that said the loop "adds none", and the loop's header, which got one added comment line.

Also in the commit:
- The spec status header, changed from INPROGRESS to CLOSED (date 2026-11-21) and nothing else by hand. gen_build_index added the ledger's row to the spec's generated records table.
- The new acceptance ledger at memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-85-1-acceptance-ledger.md, and RUN.md.
- What `gen_build_index --write` rewrote: memory/LIVE.md, memory/backlog/TOOL.md and memory/builds/dWitnessedBar/README.md.
- No function was added, so I did not run gen_map. The suite is not on the kickoff manifest's watch list, so no re-stamp was needed.
- The unstaged help/reference/drive.md and help/reference/units.md were already modified before this pass. They show no content diff, and I left them out.

Checks that ran (probes, not gates):
1. I cut the liveness loop out of the suite with awk and sourced it in bash -c, with a stub check_key_variant. With both variants seen red it gave a=4 and rgf_seen naming rec_sha and rec_fp. With the length variant not seen red it gave a=2 and an empty rgf_seen, and the tail-not-seen-red case gave the same. So a `-ge 0` clone also loses the two gated compares, and reads 4 below in total. This stands in for the `run-gates gov canary` arm (AC1).
2. `sh_hygiene.py --shell-role --measure` prints 850, matching the base row. This stands in for `portability (shell lines only shrink)` (AC3).
3. The AC2 greps on the working copy: -A1 prints the 85 RAISED line, -B1 prints the line it printed at base, and `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$'` prints 1. This stands in for `testsuite counts (every bar self-test prints one)`.
4. `bash -n` on the suite passes.

The gotchas checklist over HEAD~1..HEAD ran and I acted on it. Each ledger token sits on one physical line, and the stale "adds none" comment was fixed. A search for anything that reads the old floor of 76 by value found only historical prompt and ledger records.

Owed to the main loop at the close:
- **AC1:** the build_commit lookup and the scratch clones of the pass commit, its first parent and the `-ge 0` copy. The `-ge 0` clone must print `below the pinned floor` and read 4 below the unedited count.
- **AC2:** the arm printing `PASS (80 assertions)`.
- **AC3:** the shell-role measure in the clones, and an empty `git diff` of memory/project/shell-role.txt.
- **legs of §7:** run-gates gov canary, testsuite counts, portability and memory hygiene.
- **New arm:** the RED-first observation of the tools/run-gates/run-gates.gov.test.sh arm on its `-ge 0` staged break.

Nothing was skipped on a timeout.
