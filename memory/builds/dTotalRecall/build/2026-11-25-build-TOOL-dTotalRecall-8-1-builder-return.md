**Serves:** journal TOOL-dTotalRecall-8
**Caused-by:** TOOL-dTotalRecall-8

# TOOL-dTotalRecall-8 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `2c58c6eb3` from [2026-11-25-prompt-TOOL-dTotalRecall-8-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-8-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `bad7e5bff`.

## Why

TOOL-dTotalRecall-8 is built to spec rev-10 and committed in one pass commit, with the spec header set to CLOSED. S1 was measured before any other code and met all three lines on both trees.

## Summary

Every figure below is DERIVED 2026-11-25, on node a.

S1/AC1:
- The first cold runs read 15.44 s, 833615 bytes and 1589527 facts bytes on gov's tree, and 18.17 s, 835156 and 1589527 on the adopter fixture. (DERIVED 2026-11-25, the pass)
- At the committed bytes they read 21.63 s, 832405 and 1588606, and 19.41 s, 833946 and 1588606. (DERIVED 2026-11-25, the pass)

Checks run in place of gates. No bar, suite, `--selftest` or leg ran.
- `code_record.run_selftest()` was called as a function and passed. It stands in for the AC2-AC8 and AC11 arms.
- The new codebase-map test function passed, and `python map_diff.py --stale-dossiers` was run by CLI, exiting 1 for a bad anchor (AC9). (DERIVED 2026-11-25, the pass)
- `record_kinds.py --fixture --plant form-generated` exited 0 (AC12).
- A probe held the three `invocation_segments` copies and the four `extract_code` copies equal, and read AC10, AC11 and AC13.
- `parse_shell_defs` answers the same before and after over 142 shell files. Runlog's moved lines differ from the base only by the two markers and blank lines. (DERIVED 2026-11-25, the pass)
- `check_code_record` was called in process at the pass tip. It returned rc 0 in 30.9 s cold. (DERIVED 2026-11-25, the pass)
- `python tools/lexicon/lexicon.py --measure` gave `VERB_OFFENDER_PIN` 1443, up six for the new `extract_code.py` copy. (DERIVED 2026-11-25, the pass)
- The pre-commit and commit-msg hooks passed.
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` was run. `--for-paths` before the commit led to one fix: `parse_code_record` now refuses an unknown line kind.

Owed to the close:
- Every leg in section 7, plus the new leg `code record` itself. (DERIVED 2026-11-25, the pass)
- AC5's run of the leg at the pass tip.
- The RED-first observation of all four `New arm:` lines, in `tools/playbook/code_record.py`, `tools/lib/resolve-python.test.sh`, `tools/codebase-map/selftest.py` and `tools/memory-tree/record_kinds.py`.

Watch at the close:
- `adopt-playbook.sh --selftest` now runs `code_record.py --selftest`, about 73 s here, against the `playbook render selftest` ceiling of 300. That leg's evidence row is stale at 1.5 s. (DERIVED 2026-11-25, the pass)
- A cold `--check` is mostly the write, because it lists this clone's 105 worktrees. The recorded t is 36.7, so the ceiling is 157. (DERIVED 2026-11-25, the pass)
- `check-install-prefix.sh`, the docs leg and the encoding-posture, temp-name, cleanup and spawn-idiom ratchets were not run over the new files.

Deviation 1019 records what the spec did not state: an interpreter held in a variable counts as one; a JavaScript name bound to a literal is no definition, which took definitions from 12525 to 12493; and the carriers beyond Files touched. Those are `adopt-playbook.sh`, `kinds.toml`, `HYGIENE.template.md` and `memory/HYGIENE.md`, and the codebase-map README. All were declared by `--dispatch` with rc 0, but the codebase-map README, `kinds.toml` and deviation 1019 were edited while their declarations were still in flight. (DERIVED 2026-11-25, the pass)

The widen-37 record covers the two shell-role rows. `.governance/policy.json` was rendered from a loose commit object of the staged tree, because `mirror --write` refuses uncommitted changes. No kit version moved: kit epoch reads a branch as owed at the lander. A cached record answers `neighbourhood` whatever `--ceiling` says, so AC11's exit 2 is observable only before the text is cached. (DERIVED 2026-11-25, the pass)

No command was skipped. The brief was already recorded, and the rerun said unchanged. The adopter fixture under C:/Temp was removed.
