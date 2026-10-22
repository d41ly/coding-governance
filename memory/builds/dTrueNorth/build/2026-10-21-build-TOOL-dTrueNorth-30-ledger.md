# TOOL-dTrueNorth-30 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-30

No merge bar, no self-test suite and no gate leg ran in this pass. Each line below is a probe of the
changed suite over `653e811ef`, with its red side observed over `a75750ce5`'s spelling where one is
named. The fixture repository sat under a short `%TEMP%` path with no hook installed. The suite's
second writer-test arm, the spec's `New arm:` line, is owed to the close RED-first and then GREEN.

**Evidences:** TOOL-dTrueNorth-30
- AC1 — `write_pk_conf.*RECORD_UNDATED_ARTIFACTS="exempt"` — the spec's `awk` range over the suite
  piped to `grep -c` printed 1, and the matched line also carries `SPEC_AUDIT_PIN_CUTOFF="2026-09-01"`
  (a second `grep -c` printed 1); the same command over `a75750ce5`'s suite printed 0.
- AC2 — `git diff -U0 a75750ce5 -- tools/memory-tree/check-memory-hygiene.test.sh` — two hunks: one
  `+` line, the block header's `# ----` comment naming TOOL-dTrueNorth-30, and one `-`/`+` pair, the
  conf line gaining `\nRECORD_UNDATED_ARTIFACTS="exempt"`. A `grep` of the changed lines for `echo`
  or a `case` pattern counted 0.
- AC3 — `check 21: 1 undated non-markdown artifact(s) not graded` — the base tree, the rf10 plants
  with the `:3218` legacy list and the block's commits with `WF_KIT=tools/workflows`, replayed from
  the suite's own lines into a scratch repository, then this tree's `check-memory-hygiene.sh` run
  there once under the base conf plus the three keys, printed that line and
  `1 written by a harness before renderAuditBinding`, and no `HYGIENE check 21 FAILED`; its one red
  was check 3 on the rf10 block's `zz-probe.txt`, which the suite plants on purpose. The same replay
  under the two-key conf `a75750ce5` writes printed `HYGIENE check 21 FAILED` naming
  `memory/builds/tOne/build/result.json — no Serves line in the first 12 unfenced lines`.
- AC4 — `python tools/memory-tree/deviation_join.py --approval author-recorded` — its header read
  `records 32 (0 malformed)` and `refused 0`, no `malformed:` or `refused:` line named deviation-32,
  and the rescope add of `TOOL-dTrueNorth-30` joined
  `2026-10-22-build-TOOL-dTrueNorth-30-deviation-32`.
