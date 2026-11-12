# Acceptance ledger — TOOL-aNimbleMend-8

**Serves:** journal TOOL-aNimbleMend-8

Built against spec rev-2 in one pass commit. Each line is a probe of the changed code the builder made in the pass: a `node -e` or `python` call from the run's scratch directory, the grader's probe over a scratch repository, or the hook run as a process over a scratch repository's payload. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section, and the RED-first then GREEN observation of its two new arms, the lane rows of `tools/hooks/scratch-guard.test.sh` and the lane arms of the self-test of `tools/memory-tree/routed_commits.py`, which were written and never run.

**Evidences:** TOOL-aNimbleMend-8
- AC1 — `["leg one","leg three"]` — `readOpenReds` printed that list over the five-line ledger fixture and `[]` over an empty directory.
- AC2 — `checkRedLane` — called once per row of the decision table: rows 1, 2, 3 and 7 returned null, row 7 tried with a spec role, the untyped harness agent and an agent-false product role; rows 4, 5 and 6 returned a `witness` string naming `leg one` and `Red-fix:`. The hook run as a process over a scratch repository exited 0 with that one line while a red row stood and the key read on, and exited 2 with the key off, its refusal byte-identical to the base hook's.
- AC3 — `grep -c "checkRedLane(" tools/hooks/scratch-guard.js` — printed 2, and the position test over `String(checkRouted)` printed `true`.
- AC4 — `python lane-probe.py on` — both halves listed C3 with `leg nine` and `legs.json`, listed C4 as `names no unit`, did not list C2, and the WHOLE, RANGE and WHOLE-beside summary lines each held `1 red-fix`.
- AC5 — `python lane-probe.py off` — the RANGE half listed C2, C3 and C4 each as `no unit id — names no unit`, and the first block, graded WHOLE, did not list C2 and held `1 red-fix`. The 91ca33f2 baseline was not re-run; the spec states it.
- AC6 — `True True` — printed by the import probe, and `grep -c "policy.py" tools/memory-tree/routed_commits.py` printed 0.
- AC7 — `grep -ci "red-fix lane" tools/hooks/scratch-guard.js` — printed 6; `grep -c "Red-fix"` printed 1 over `tools/hooks/README.md` and 3 over the docstring lines of `tools/memory-tree/routed_commits.py`.
