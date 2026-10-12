# TOOL-aBriskPreflight-6 — acceptance ledger

**Serves:** journal TOOL-aBriskPreflight-6

No merge bar and no self-test suite ran in this pass. Every criterion was observed directly: the
claim-push instrument in a throwaway clone, and temporary slices of the straggler, pre-push and
unattended suites, each run alone and deleted. Each slice ran against hook copies in the scratch
dir: the hook before this unit at `138b0c457`, the built hook, and one-line staged breaks of the
built hook. The figures and the slice verdicts are in
`2026-10-11-build-TOOL-aBriskPreflight-6-claim-push-ab.md`. The suites themselves are owed to the
close.

**Evidences:** TOOL-aBriskPreflight-6
- AC1 — `2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh` built `%TEMP%/bp6` with
  `core.hooksPath` on its own hooks and `origin/HEAD` recorded, and fed `refs/gov/runs/x` to each
  hook four times traced, A/B interleaved, and once each untraced. The built hook took 9 forks and
  10 execs both times, a figure of 5.7 s and 5.6 s at `spawn5` 1.49 s and 1.47 s, and 11.3 s
  untraced, all under 30 s. The hook before this unit took 46 forks and 33 and 32 execs, 17.2 s and
  22.0 s by the same figure, and 28.1 s untraced.
- AC2 — `decision=skip-nondefault` — the clone's `pushes.log` holds one `ev=end` line per run, six in
  all, each `rc=0`, `exit=clean` and `decision=skip-nondefault`, for both hooks. Every run exited 0.
- AC3 — `DEAD PROBE` — the straggler slice passed all 15 assertions against the built hook,
  including the F3 refusal naming the merge sha and `--repair`, the landing once accounted, the
  `did NOT run` line and the `DEAD PROBE` line. With S2's predicate replaced by `true`, the first F3
  push landed and the arm went red, as did the two skip-line arms. Restored, it passed.
- AC4 — `migrate_backlog.py --relocate --as <your-slug>` — the same slice's pre-flip feature push
  printed the recipe and landed against the built hook. Under AC3's staged break it printed no
  recipe and the arm went red. Restored, it passed.
- AC5 — `refs/tags/t-strag` — S4's two arms passed against the built hook: the tag push and the
  push of `refs/gov/runs/x` beside `feat` were both refused naming the merge. Both were refused by
  the hook before this unit too. With the candidates limited to `refs/heads/`, only the tag arm went
  red. With the shortcut taken when any candidate is an empty root, only the mixed arm went red.
- AC6 — `init_straggler_guard` — the build's `trace-spawns.py` over the built hook's two traces
  printed `execs by program` with `git` 9 and `rm` 1 and no python row, and `wall by function` with
  no `init_straggler_guard` row. The traces of the hook before this unit carry `python3` 4 and an
  `init_straggler_guard` row each.
- AC7 — `Sanctioned use: GOV_BRANCH_GATE_CMD=` — with no runner placed, the hook before this unit
  printed the placeholder, so the pre-push suite now places `run-gates/run-gates.sh` for the
  branch-bar arm and asserts the line. Placed, both hooks printed the line naming
  `bash run-gates/run-gates.sh`, byte for byte. With S3's condition reduced to the default-branch
  test, the line fell back to the placeholder and the new assertion went red.
- AC8 — `TOOL-aGraftedHelix-10` — the unattended suite's hooked claim block, sliced with its
  prologue and the claim helpers, copied the built hook in itself and passed 47 assertions with no
  SKIP: the create, the CAS update, the unset-HEAD refusal and the stale-refusal-file arms.
