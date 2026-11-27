**Serves:** journal TOOL-dTotalRecall-116
**Caused-by:** TOOL-dTotalRecall-116

# TOOL-dTotalRecall-116 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `270795c1b` from [2026-11-25-prompt-TOOL-dTotalRecall-116-build-2-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-116-build-2-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `8451b1de2`.

## Why

Built to spec rev-2 with no divergence. All six criteria were answered by the pass and recorded in the acceptance ledger. The spec is set to CLOSED in the same commit, and the worktree is clean after it.

## Summary

WHAT LANDED
- C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/record_find.py: `check_blob_path`, the rev-2 blob branch of `read_section`, the three plants and the docstring. The branch includes the empty-`got` refusal.
- check-memory-hygiene.test.sh: three arms, six assertions. FLOOR_ASSERTIONS goes from 830 to 836, counted by reading (DERIVED 2026-11-25).
- The shell-role row was widened through `ratchet.py widen` (widen-29). The door raised it by one, so I set it by hand to the measured 3750, as widen-28 was; a Decided trailer says so (DERIVED 2026-11-25).
- symbols.json, the README and LIVE.md were re-rendered. RUN.md and the ledger (memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-116-2-acceptance-ledger.md) are in the commit.

CHECKS RUN (DERIVED 2026-11-25; they stand in for the memory-hygiene self-test's arms)
- AC1, AC2: the three blob plants each printed their refusal and exit 2. Every other plant printed what its existing arm expects, except that only the tail of the output was read for nine of them.
- AC3: `unheld-blob` printed `the second`, never `the third`, with exit 0. The probe's path ends `deviation-1.md`.
- AC4: over this worktree both foreign addresses raised FindError, and the stem at its own file's blob returned its text. The three reads took 261 s cold, then 78 s and 57 s (DERIVED 2026-11-25).
- AC5: the grep printed 3, and the measured shell-role count is 3750 (DERIVED 2026-11-25).
- AC6: the fixture read each file's own path at lines 5 and 3. The archive's former blob read `memory/DECISIONS.md` with the former text (DERIVED 2026-11-25).
- Extra probes: a bracketed record name does not match a neighbour's blob (`--literal-pathspecs`), and a refused git is a FindError. With `check_blob_path` cut to a constant yes in a scratch copy, `blob-foreign-record` and `blob-foreign-text` each exited 0.
- Other: `bash -n`, the lexicon's `--suggest check_blob_path`, and the commit's own pre-commit legs passed.

OWED TO THE CLOSE
- Every leg in the spec's section 7.
- The RED-first observation of the one New arm (the three blob plants): red on the whole-blob fallback, and `blob-foreign-record` red on `check_blob_path` cut.
- The suite's executed count against floor 836.

BUG CLASSES: I ran `gotchas.py --for-diff HEAD~1..HEAD` and nothing needed a change. The empty-`got` guard in the universal class about dead fallbacks is spec-stated as unreachable, and it refuses. `check_blob_path` raises on a non-zero git exit. No deviation record is owed.

SKIPPED: nothing timed out. `--brief` answered already recorded, and no extra `--dispatch` path was needed.
