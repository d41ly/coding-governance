# Acceptance ledger — TOOL-aGraftedHelix-13

**Serves:** journal TOOL-aGraftedHelix-13

Node `a`, 2026-10-05. The build commit is `8b286f71`, over the spec's rev-3 commit `91f0ab58`,
which recorded the pass's one divergence before any code: the fixture is copy-installed as unit 14's
check-27 fixture is, and the engine run is the fixture's copy of the kit. Measured first, rev-2's
staged break in a kit copy outside the fixture redded checks 9 and 17-19 as well, and the worktree's
engine run over a fixture read check 26 against the host repository. No merge bar and no self-test
suite ran in this pass. The direct checks were the engine commands AC1 and AC2 name, over a fixture
built by the arm's own steps under a short `%TEMP%` directory, and a slice of the suite: its
prologue plus the new block alone, green at 3 arms. Each arm was observed RED on a real staged break,
each made in the fixture's copy of the kit and never in the tracked tree: the block's `status=1`
deleted redded the branch arm, its green-run print deleted redded the clean-main arm, and its
`add_offender_keys 28` line deleted redded the `--offenders` arm, which read `[]`. The block unit 6
built needed no repair, so S2 owed nothing beyond the version line and the stamp.

**Evidences:** TOOL-aGraftedHelix-13
- AC1 — `check 28:` — at `8b286f71`, under rev-3's wording, the fixture's copy of `tools/memory-tree/check-memory-hygiene.sh` on its branch under `GOV_DEFAULT_BRANCH=main` exited 1 and printed `check 28: 2 records hold one content key — memory/gotchas/held-once.md (held-once), memory/gotchas/held-twice.md (held-twice)`, with no other line opening `check <n>:` and `--offenders` keying `check 28` alone. With `status=1` deleted in that copy the same run exited 0.
- AC2 — `row-grammar: check 28 graded` — the same command on the fixture's `main` exited 0 and printed `row-grammar: check 28 graded 2 record(s) in f5f37419..HEAD — 1 row(s), 1 gotcha(s), 0 with an empty key, 0 key(s) held twice`.
- AC3 — `bash skills/session-kickoff/manifest-check.sh` — at `8b286f71` it exited 0 with no `MANIFEST check 5 FAILED` line, and `python tools/govkit/govkit.py epoch --base 91f0ab58` printed `epoch: memory-tree · clean · 2.126` with exit 0, as it did with the unit's starting HEAD `5ef0a64c` as the base.
- AC4 — `python tools/memory-tree/gotchas.py --check` — at `8b286f71` it exited 0, and `gotchas.py --for-paths tools/memory-tree/check-memory-hygiene.sh` listed `a-grep-for-a-word-is-a-presence-probe` among 13 anchored classes.
