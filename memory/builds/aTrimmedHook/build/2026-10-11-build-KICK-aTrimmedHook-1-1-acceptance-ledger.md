# KICK-aTrimmedHook-1 — acceptance ledger

**Serves:** journal KICK-aTrimmedHook-1

No merge bar and no self-test suite ran in this pass. The new arms were observed through a slice of
`skills/session-kickoff/manifest-check.test.sh`: its helpers, arms 1 to 21 and the new block, run
against the checker this pass ships, held 27 of 27. A second slice of the helpers, arm 17, arm 20 and
the new block, run against a copy of the checker whose exit lists only the manifest and whose C6
zero-confirm is gone, printed FAIL for arm 17, for the verify-path deletion arm and for the glob arm,
which is each arm observed RED. On the measured commit, one staged `RUN.md` line, `--staged` went from
114 s to 8 s on node a with the NOTE line printed. The close owes the whole `manifest-check self-test` leg.

**Evidences:** KICK-aTrimmedHook-1
- AC1 — `manifest-check.sh --staged` — in a fixture staging only `unrelated.txt`, with a placeholder
  committed in the manifest, it printed `staged leg skipped — nothing staged touches the manifest`
  and exited 0, and reported no C1.
- AC2 — `manifest-check.sh --staged` — arm 17's staged watched `Makefile` with no re-stamp still
  reported C5s and exited 1; with the exit listing only the manifest, it exited 0, observed RED.
- AC3 — `manifest-check.sh --staged` — the same fixture with a manifest edit staged reported
  `check 1 FAILED` and exited 1.
- AC4 — `manifest-check.sh --staged` — a staged `git rm` of `docs/GOV.md`, the fixture's
  verify-path, reported `is not tracked content` and exited 1; with the exit listing only the
  manifest it exited 0, observed RED.
- AC5 — `manifest-check.sh` — run with no argument on the base tree, the pre-unit and shipped
  checkers printed byte-identical output, and `--staged` with the manifest staged did too; both
  were silent on that clean tree, so the pair was repeated with a placeholder in the manifest and
  `.memory-tree.conf` staged, and the C1 and C5s refusals matched byte for byte in both modes.
- AC6 — `manifest-check.sh` — on a fixture manifest naming `Makefile`, `docs/` and `Make*` it exited
  0 with nothing reported, arm 20's dead pathspec still reported C6, and with the zero-confirm gone
  the glob arm reported C6, observed RED.
