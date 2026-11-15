# TOOL-aMeasuredDrag-10 — acceptance ledger

**Serves:** journal TOOL-aMeasuredDrag-10

No merge bar and no self-test suite ran in this pass. The pass started at 274110dd. The parent hook
was saved with `git show HEAD:.githooks/pre-commit` before the edit, and the spec's §4 probe ran as
`u10probe.sh` in the session scratchpad from the worktree root in Git Bash, its fixture under
`%TEMP%`, once over the parent copy and once over the edited `.githooks/pre-commit`, then a second
round of both. Each probe run is a "before" (parent) or "after" (edited) reading at 274110dd.

**Evidences:** TOOL-aMeasuredDrag-10
- AC1 — `cmp` — the parent run's and the edited run's `transcript.txt` compared with `cmp`, which
  printed nothing and exited 0, the `commit-all` and `commit-only` cases included. The second round
  matched the first byte for byte on both hooks, so each transcript is reproducible.
- AC2 — `diff-cached=1` — the edited hook's `counts.txt` reads `diff-cached=1` on 13 cases and
  `diff-cached=2` on `commit-all` and `commit-only` (PINNED at 274110dd). The parent read
  `diff-cached=5` on all 15 cases (PINNED at 274110dd), the spec's figure at 6d98c39ca.
- AC3 — `py-resolutions` — the edited hook reads at most 1 on every case and 0 on
  `memory-added`, `memory-renamed-within` and `memory-non-ascii`, the three cases the parent read
  at 0 (PINNED at 274110dd). The parent read 3 on `policy-py-no-memory` and 2 on four cases
  (PINNED at 274110dd), the spec's figure.
- AC4 — `time bash` — each probe run timed beside `time (for i in 1 2 3 4 5 6 7 8 9 10; do
  /usr/bin/true; done)` in the same shell, PINNED at 274110dd:
  - round 1: before 277.4 s real with baseline 2.15 s; after 63.8 s real with baseline 0.50 s
    (PINNED at 274110dd).
  - round 2, back to back: before 78.9 s real with baseline 0.94 s; after 44.8 s real with
    baseline 0.55 s (PINNED at 274110dd).
  - the edited hook is faster in both rounds, by 34.1 s in the paired round 2, which clears every
    baseline taken beside it and the spec's 0.35 s (PINNED at 6d98c39ca). The spec's parent figure
    is 50.2 s (PINNED at 6d98c39ca), so this machine was under load when sampled, round 1 most of
    all, as the -7, -8 and -9 ledgers also found.

**Owed to the close (the main loop, after every unit is terminal):**
- No new arm. Spec §6 adds none, so no RED-first observation is owed.
- The gates in spec §6: `branch-guard self-test`, `straggler-guard arms`, `python resolver
  (behaviour + inline parity + idiom ban)` and `lexicon naming predicates`. The two new function
  names were checked here with `lexicon.py --suggest ... --as sh.function`, which answered OK for
  both; that stands in for the lexicon leg's naming check, not for the leg.
